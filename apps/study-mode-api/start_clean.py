#!/usr/bin/env python3
"""Clean startup script for Study Mode API.

This script:
1. Kills any existing Python processes on port 8000
2. Waits for port to be freed
3. Starts the backend fresh
4. Verifies health endpoint

Usage:
    python apps/study-mode-api/start_clean.py

Or via pnpm:
    pnpm nx run study-mode-api:start-clean
"""

import os
import socket
import subprocess
import sys
import time

PORT = 8000
MAX_WAIT = 10  # seconds to wait for port to free


def is_port_in_use(port: int) -> bool:
    """Check if port is in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0


def kill_processes_on_port(port: int) -> bool:
    """Kill any processes using the specified port (Windows)."""
    try:
        # Find PIDs using the port
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True,
            text=True,
            shell=True,
        )

        pids_killed = set()
        for line in result.stdout.split("\n"):
            if f":{port}" in line and "LISTENING" in line:
                parts = line.split()
                if parts:
                    pid = parts[-1]
                    if pid.isdigit() and pid not in pids_killed:
                        print(f"[Cleanup] Killing PID {pid} on port {port}")
                        subprocess.run(
                            ["taskkill", "/F", "/PID", pid],
                            capture_output=True,
                            shell=True,
                        )
                        pids_killed.add(pid)

        # Also kill any stray python processes that might be uvicorn workers
        subprocess.run(
            ["taskkill", "/F", "/IM", "python.exe"],
            capture_output=True,
            shell=True,
        )

        return len(pids_killed) > 0
    except Exception as e:
        print(f"[Cleanup] Error: {e}")
        return False


def wait_for_port_free(port: int, timeout: int = MAX_WAIT) -> bool:
    """Wait for port to become free."""
    print(f"[Startup] Waiting for port {port} to be free...")
    start = time.time()
    while time.time() - start < timeout:
        if not is_port_in_use(port):
            print(f"[Startup] Port {port} is free")
            return True
        time.sleep(0.5)
    return False


def check_health(port: int, timeout: int = 30) -> bool:
    """Wait for health endpoint to respond."""
    import urllib.request
    import urllib.error

    print(f"[Startup] Waiting for server to be healthy...")
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as resp:
                if resp.status == 200:
                    print(f"[Startup] Server is healthy!")
                    return True
        except (urllib.error.URLError, ConnectionRefusedError, TimeoutError):
            pass
        time.sleep(1)
    return False


def main():
    print("=" * 60)
    print("STUDY MODE API - CLEAN STARTUP")
    print("=" * 60)

    # Step 1: Kill existing processes
    if is_port_in_use(PORT):
        print(f"[Cleanup] Port {PORT} is in use, cleaning up...")
        kill_processes_on_port(PORT)

        if not wait_for_port_free(PORT):
            print(f"[ERROR] Could not free port {PORT} after {MAX_WAIT}s")
            sys.exit(1)
    else:
        print(f"[Startup] Port {PORT} is already free")

    # Step 2: Start the server
    print(f"[Startup] Starting server on port {PORT}...")

    # Get the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))

    # Change to project root for pnpm
    os.chdir(project_root)

    # Start uvicorn directly (not via pnpm to avoid subprocess issues)
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    # Start the server
    process = subprocess.Popen(
        [
            sys.executable, "-m", "uvicorn",
            "study_mode_api.main:app",
            "--host", "127.0.0.1",
            "--port", str(PORT),
            "--log-level", "info",
        ],
        cwd=os.path.join(script_dir, "src"),
        env=env,
    )

    # Step 3: Wait for health
    if check_health(PORT):
        print("=" * 60)
        print(f"SERVER READY: http://127.0.0.1:{PORT}")
        print("=" * 60)
        print("\nPress Ctrl+C to stop the server")

        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n[Shutdown] Stopping server...")
            process.terminate()
            process.wait()
            print("[Shutdown] Server stopped")
    else:
        print(f"[ERROR] Server failed to become healthy")
        process.terminate()
        sys.exit(1)


if __name__ == "__main__":
    main()
