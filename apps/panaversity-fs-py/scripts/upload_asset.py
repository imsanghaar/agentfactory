#!/usr/bin/env python3
"""Upload any asset (PDF, image, video, audio) and get the CDN URL back.

Simple script for authors to upload assets during lesson writing.

Usage:
    # Upload PDF slides
    uv run python scripts/upload_asset.py --file ./quiz.pdf --type slides --part 01 --chapter 01

    # Upload image (alternative to upload_image.py)
    uv run python scripts/upload_asset.py --file ./diagram.png --type images --part 02 --chapter 05

    # Upload video
    uv run python scripts/upload_asset.py --file ./demo.mp4 --type videos --part 03 --chapter 10

    # With custom name
    uv run python scripts/upload_asset.py --file ./quiz.pdf --type slides --part 01 --chapter 01 --name chapter-assessment

    # Dry run (preview URL without uploading)
    uv run python scripts/upload_asset.py --file ./quiz.pdf --type slides --part 01 --chapter 01 --dry-run

Output:
    ✓ Uploaded: https://pub-xxx.r2.dev/books/ai-native-dev/static/slides/part-1/chapter-01/chapter-assessment.pdf

Asset Types:
    images  - PNG, JPG, JPEG, GIF, SVG, WEBP
    slides  - PDF, PPTX, KEY
    videos  - MP4, WEBM, MOV
    audio   - MP3, WAV, OGG, M4A
"""

import argparse
import asyncio
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from dotenv import load_dotenv
load_dotenv()


# Valid extensions by asset type
VALID_EXTENSIONS = {
    'images': {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'},
    'slides': {'.pdf', '.pptx', '.key'},
    'videos': {'.mp4', '.webm', '.mov'},
    'audio': {'.mp3', '.wav', '.ogg', '.m4a'},
}

# All valid asset types
ASSET_TYPES = list(VALID_EXTENSIONS.keys())


def sanitize_filename(name: str) -> str:
    """Sanitize filename for URL safety."""
    # Remove extension if present
    name = Path(name).stem
    # Convert to lowercase, replace spaces with hyphens
    name = name.lower().replace(' ', '-').replace('_', '-')
    # Remove non-alphanumeric except hyphens
    name = re.sub(r'[^a-z0-9\-]', '', name)
    # Collapse multiple hyphens
    name = re.sub(r'-+', '-', name)
    return name.strip('-')


def get_asset_type_for_extension(ext: str) -> str | None:
    """Auto-detect asset type from file extension."""
    ext = ext.lower()
    for asset_type, extensions in VALID_EXTENSIONS.items():
        if ext in extensions:
            return asset_type
    return None


async def upload_asset(
    file_path: Path,
    asset_type: str,
    part: str,
    chapter: str,
    name: str | None,
    book_id: str,
    dry_run: bool
) -> str | None:
    """Upload asset to storage and return CDN URL."""

    # Validate file exists
    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}")
        return None

    # Get extension
    ext = file_path.suffix.lower()

    # Validate asset type
    if asset_type not in ASSET_TYPES:
        print(f"ERROR: Invalid asset type: {asset_type}")
        print(f"  Valid types: {', '.join(ASSET_TYPES)}")
        return None

    # Validate extension matches asset type
    valid_ext = VALID_EXTENSIONS[asset_type]
    if ext not in valid_ext:
        # Try to auto-detect
        detected_type = get_asset_type_for_extension(ext)
        if detected_type:
            print(f"WARNING: Extension {ext} is for '{detected_type}', not '{asset_type}'")
            print(f"  Use --type {detected_type} instead")
        else:
            print(f"ERROR: Invalid file type: {ext}")
            print(f"  Supported for {asset_type}: {', '.join(valid_ext)}")
        return None

    # Build filename
    if name:
        safe_name = sanitize_filename(name)
    else:
        safe_name = sanitize_filename(file_path.stem)

    filename = f"{safe_name}{ext}"

    # Build storage path: books/{book_id}/static/{asset_type}/part-{N}/chapter-{NN}/{filename}
    # Normalize part/chapter numbers
    part_num = part.lstrip('0') or '0'
    chapter_num = chapter.zfill(2)

    storage_path = f"books/{book_id}/static/{asset_type}/part-{part_num}/chapter-{chapter_num}/{filename}"

    # Get config
    try:
        from panaversity_fs.config import get_config
        config = get_config()
    except Exception as e:
        print(f"ERROR: Configuration failed: {e}")
        print("  Make sure .env is configured with storage settings")
        return None

    # Build CDN URL
    cdn_base = config.cdn_base_url
    if not cdn_base:
        print("ERROR: CDN_BASE_URL not configured in .env")
        return None

    cdn_url = f"{cdn_base}/{storage_path}"

    # Read file
    file_bytes = file_path.read_bytes()
    file_size = len(file_bytes)
    size_str = f"{file_size / 1024:.1f} KB" if file_size < 1024 * 1024 else f"{file_size / (1024*1024):.2f} MB"

    # Check size limit (varies by asset type)
    max_sizes = {
        'images': 10 * 1024 * 1024,   # 10MB
        'slides': 50 * 1024 * 1024,   # 50MB for PDFs/presentations
        'videos': 100 * 1024 * 1024,  # 100MB
        'audio': 50 * 1024 * 1024,    # 50MB
    }
    max_size = max_sizes.get(asset_type, 10 * 1024 * 1024)
    max_mb = max_size / (1024 * 1024)
    if file_size > max_size:
        print(f"ERROR: File too large: {size_str} (max {max_mb:.0f}MB for {asset_type})")
        print("  For larger files, use presigned URL upload (not yet implemented)")
        return None

    # Compute hash
    content_hash = hashlib.sha256(file_bytes).hexdigest()

    if dry_run:
        print("\n[DRY RUN] Would upload:")
        print(f"  Source: {file_path}")
        print(f"  Type: {asset_type}")
        print(f"  Size: {size_str}")
        print(f"  Path: {storage_path}")
        print(f"  URL: {cdn_url}")
        return cdn_url

    # Upload
    try:
        from panaversity_fs.storage import get_operator
        op = get_operator()

        print(f"Uploading {file_path.name} ({size_str}) as {asset_type}...")
        await op.write(storage_path, file_bytes)

        # Sync to FileJournal
        try:
            from panaversity_fs.database.connection import get_session
            from panaversity_fs.database.models import FileJournal

            # Journal path is relative (without books/{book_id}/)
            journal_path = f"static/{asset_type}/part-{part_num}/chapter-{chapter_num}/{filename}"

            async with get_session() as session:
                entry = FileJournal(
                    book_id=book_id,
                    path=journal_path,
                    user_id="__base__",
                    sha256=content_hash,
                    last_written_at=datetime.now(timezone.utc),
                    storage_backend=config.storage_backend
                )
                await session.merge(entry)

        except Exception as e:
            print(f"  Warning: FileJournal sync failed: {e}")

        return cdn_url

    except Exception as e:
        print(f"ERROR: Upload failed: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Upload any asset and get the CDN URL",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        "--file", "-f",
        type=Path,
        required=True,
        help="Path to asset file"
    )

    parser.add_argument(
        "--type", "-t",
        type=str,
        required=True,
        choices=ASSET_TYPES,
        help=f"Asset type: {', '.join(ASSET_TYPES)}"
    )

    parser.add_argument(
        "--part", "-p",
        type=str,
        required=True,
        help="Part number (e.g., 01 or 1)"
    )

    parser.add_argument(
        "--chapter", "-c",
        type=str,
        required=True,
        help="Chapter number (e.g., 05 or 5)"
    )

    parser.add_argument(
        "--name", "-n",
        type=str,
        default=None,
        help="Custom filename (without extension). Default: use source filename"
    )

    parser.add_argument(
        "--book-id", "-b",
        type=str,
        default="ai-native-dev",
        help="Book identifier (default: ai-native-dev)"
    )

    parser.add_argument(
        "--dry-run", "-d",
        action="store_true",
        help="Preview URL without uploading"
    )

    args = parser.parse_args()

    # Run upload
    cdn_url = asyncio.run(upload_asset(
        file_path=args.file,
        asset_type=args.type,
        part=args.part,
        chapter=args.chapter,
        name=args.name,
        book_id=args.book_id,
        dry_run=args.dry_run
    ))

    if cdn_url:
        print(f"\n✓ {'Would upload to' if args.dry_run else 'Uploaded'}:")
        print(f"  {cdn_url}")

        # Show appropriate embed syntax
        filename = cdn_url.split('/')[-1]
        name_only = Path(filename).stem
        ext = Path(filename).suffix.lower()

        print("\nReady to use:")
        if ext in VALID_EXTENSIONS['images']:
            print(f"  ![{name_only}]({cdn_url})")
        elif ext == '.pdf':
            print(f"  [Download {name_only}]({cdn_url})")
            print(f"  Or embed: <embed src=\"{cdn_url}\" type=\"application/pdf\" width=\"100%\" height=\"600px\" />")
        else:
            print(f"  [{name_only}]({cdn_url})")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
