# 📖 Projector Video Modal - Quick Start Guide

## 🚀 5-Minute Setup

### Step 1: Import Components (30 seconds)

```tsx
import { ChapterVideoModal, ChapterVideoPlayer } from "@/components/ChapterVideoModal";
```

### Step 2: Add Player to Page (1 minute)

```tsx
// In your page component (e.g., preface-agent-native.md)
export default function PrefacePage() {
  return (
    <Layout>
      <MDXContent />
      {/* Hidden player that listens for events */}
      <ChapterVideoPlayer />
    </Layout>
  );
}
```

### Step 3: Add Play Button (2 minutes)

#### Option A: Floating Action Button

```tsx
<button 
  className="play-video-float"
  onClick={() => {
    const event = new CustomEvent("open-chapter-video");
    window.dispatchEvent(event);
  }}
  title="Watch Video"
>
  <PlayIcon />
</button>
```

#### Option B: Inline Button

```tsx
<button 
  className="doc-page-actions-play"
  onClick={() => {
    const event = new CustomEvent("open-chapter-video");
    window.dispatchEvent(event);
  }}
>
  <PlayIcon />
  <span>Play Video</span>
</button>
```

### Step 4: Test (1 minute)

1. Navigate to your page
2. Click the Play button
3. Watch the projector animation
4. Verify video plays
5. Test close button

**Done! 🎉**

---

## 📝 Quick Reference

### Props

```tsx
<ChapterVideoModal
  isOpen={boolean}           // Required: Control visibility
  onOpenChange={function}     // Required: State change handler
  videoUrl={string}           // Optional: YouTube embed URL
/>
```

### Default Video URL

```typescript
// Default: imsanghaar YouTube video
"https://www.youtube.com/embed/Yl_yOFXZKrY"
```

### Custom Video

```tsx
<ChapterVideoModal
  isOpen={showModal}
  onOpenChange={setShowModal}
  videoUrl="https://www.youtube.com/embed/YOUR_VIDEO_ID"
/>
```

---

## 🎨 Styling Quick Tips

### Change Projector Color

```css
.projector-body {
  background: linear-gradient(145deg, #YOUR_COLOR 0%, #DARKER 100%);
}
```

### Adjust Animation Speed

```tsx
// In ChapterVideoModal.tsx
const projectorTimer = setTimeout(() => setShowProjector(true), 100);  // Change this
const screenTimer = setTimeout(() => setShowScreen(true), 800);        // Change this
const playerTimer = setTimeout(() => setIsPlayerReady(true), 1200);    // Change this
```

### Modify Screen Size

```css
.projection-screen {
  width: 900px;        /* Change width */
  max-width: 90vw;     /* Change max-width */
}
```

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Modal doesn't open | Check if `ChapterVideoPlayer` is rendered |
| Projector doesn't descend | Verify `showProjector` state updates |
| Video doesn't play | Check `isPlayerReady` state |
| Animation is choppy | Enable GPU: `will-change: transform` |
| Close button not working | Verify `onOpenChange` callback |

---

## 📱 Responsive Breakpoints

```css
/* Desktop (default) */
Screen: 900px
Projector: 180px × 80px

/* Mobile (≤768px) */
Screen: 100% (max 90vw)
Projector: 140px × 60px
```

---

## ⚡ Performance Tips

1. **Lazy Load**: Video only loads when modal opens
2. **GPU Acceleration**: Uses CSS transforms for smooth animations
3. **Cleanup**: All timers cleared on unmount
4. **Bundle Size**: ~5KB gzipped (code-split)

---

## 🎯 Common Use Cases

### Use Case 1: Preface Page

```tsx
// Already implemented!
// See: docs/preface-agent-native.md
<ChapterVideoPlayer />
```

### Use Case 2: Chapter Introduction

```tsx
function ChapterIntro() {
  const [showVideo, setShowVideo] = useState(false);
  
  return (
    <>
      <button onClick={() => setShowVideo(true)}>
        Watch Chapter Intro
      </button>
      
      <ChapterVideoModal
        isOpen={showVideo}
        onOpenChange={setShowVideo}
        videoUrl="https://www.youtube.com/embed/CHAPTER_VIDEO_ID"
      />
    </>
  );
}
```

### Use Case 3: Tutorial Video

```tsx
function TutorialSection() {
  return (
    <div className="tutorial">
      <h2>Learn by Watching</h2>
      <button 
        className="play-video-float"
        onClick={() => window.dispatchEvent(
          new CustomEvent("open-chapter-video")
        )}
      >
        <PlayIcon />
      </button>
    </div>
  );
}
```

---

## 📚 Learn More

- **[README.md](./README.md)** - Full documentation
- **[DESIGN.md](./DESIGN.md)** - Visual design guide
- **[IMPLEMENTATION.md](./IMPLEMENTATION.md)** - Technical details

---

## 🆘 Need Help?

1. Check the [Troubleshooting Guide](./README.md#troubleshooting)
2. Review [Implementation Details](./IMPLEMENTATION.md)
3. Contact: imsanghaar Team

---

**Quick Start Version**: 1.0.0  
**Last Updated**: February 2026
