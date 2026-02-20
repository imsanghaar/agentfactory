# 🎬 Chapter Video Modal - Projector Animation

A cinematic video modal component that creates a realistic projector animation experience when playing chapter videos.

## 📋 Overview

The Chapter Video Modal replaces the traditional TV-style video player with an immersive projector animation. When triggered, a projector descends from the top of the screen, casts light rays, and projects the video onto a floating screen with a black background for a cinematic experience.

## 🎯 Features

- **Cinematic Animation Sequence**: Projector descends, light rays appear, screen fades in
- **Realistic Projector Design**: Detailed 3D-style projector with lens and vents
- **Light Ray Effects**: 5 animated light beams with blur and glow
- **Projection Screen**: Floating screen with glowing blue border
- **YouTube Iframe Integration**: Direct iframe embedding for reliable playback
- **Responsive Design**: Adapts to all screen sizes with 16:9 aspect ratio
- **Black Background**: Full-screen black overlay for theater-like experience

## 📁 File Structure

```
src/components/ChapterVideoModal/
├── README.md                    # This documentation file
├── ChapterVideoModal.tsx        # Main modal component
├── ChapterVideoModal.test.tsx   # Component tests
├── ChapterVideoPlayer.tsx       # Player wrapper component
├── ChapterVideoButton.tsx       # Play button component
├── ChapterVideoButton.test.tsx  # Button tests
└── index.ts                     # Export barrel file
```

## 🏗️ Architecture

### Component Hierarchy

```
ChapterVideoModal
├── DialogPrimitive.Root (Radix UI)
│   └── DialogPrimitive.Portal
│       ├── DialogPrimitive.Overlay (Black background)
│       └── DialogPrimitive.Content
│           ├── Projector Assembly
│           │   ├── Projector Body
│           │   │   ├── Projector Lens
│           │   │   │   └── Lens Glass
│           │   │   └── Projector Vents
│           │   └── Light Rays (5 beams)
│           ├── Projection Screen Container
│           │   ├── Projection Screen
│           │   │   └── Screen Border (ReactPlayer)
│           │   └── Screen Glow
│           └── Close Button
```

## 🎬 Animation Sequence

```
┌─────────────────────────────────────────────────────────┐
│                    User Clicks Play                      │
│                         (0ms)                            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Background Turns Black                      │
│                         (0ms)                            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           Projector Descends from Top                    │
│                       (100ms)                            │
│                                                          │
│    ┌──────────────────────────┐                         │
│    │      PROJECTOR           │                         │
│    │         [Lens]           │  ↓                      │
│    └──────────────────────────┘                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Light Rays Appear                           │
│                       (300ms)                            │
│                                                          │
│    ┌──────────────────────────┐                         │
│    │      PROJECTOR           │                         │
│    │         [Lens]           │                         │
│    └──────────────────────────┘                         │
│         ╲    │    ╱                                     │
│          ╲   │   ╱   ← Light Beams                      │
│           ╲  │  ╱                                       │
│            ╲ │ ╱                                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           Projection Screen Fades In                     │
│                       (800ms)                            │
│                                                          │
│    ┌──────────────────────────┐                         │
│    │      PROJECTOR           │                         │
│    │         [Lens]           │                         │
│    └──────────────────────────┘                         │
│         ╲    │    ╱                                     │
│          ╲   │   ╱                                      │
│           ╲  │  ╱                                       │
│            ╲ │ ╱                                        │
│    ┌────────────────────────┐                           │
│    │   PROJECTION SCREEN    │                           │
│    │                        │                           │
│    └────────────────────────┘                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Video Starts Playing                        │
│                       (1200ms)                           │
│                                                          │
│    ┌──────────────────────────┐                         │
│    │      PROJECTOR           │                         │
│    │         [Lens]           │                         │
│    └──────────────────────────┘                         │
│         ╲    │    ╱                                     │
│          ╲   │   ╱                                      │
│           ╲  │  ╱                                       │
│            ╲ │ ╱                                        │
│    ┌────────────────────────┐                           │
│    │   ▶ VIDEO PLAYING      │                           │
│    │                        │                           │
│    └────────────────────────┘                           │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Component API

### ChapterVideoModal Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `isOpen` | `boolean` | `false` | Controls modal visibility |
| `onOpenChange` | `(open: boolean) => void` | - | Callback for open state changes |
| `videoUrl` | `string` | YouTube embed URL | Video source URL |

### Usage Example

```tsx
import { ChapterVideoModal } from "@/components/ChapterVideoModal";

function MyComponent() {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)}>
        Play Video
      </button>
      
      <ChapterVideoModal
        isOpen={showModal}
        onOpenChange={setShowModal}
        videoUrl="https://www.youtube.com/embed/Yl_yOFXZKrY"
      />
    </>
  );
}
```

## 🎨 CSS Architecture

### Class Structure

```css
/* Main Containers */
.projector-assembly          /* Projector housing */
.projector-descended         /* Descended state */
.projection-screen-container /* Screen wrapper */
.screen-visible             /* Visible state */

/* Projector Components */
.projector-body    /* Main housing */
.projector-lens    /* Lens assembly */
.lens-glass        /* Glass element */
.projector-vents   /* Ventilation */

/* Light Effects */
.projector-rays    /* Ray container */
.rays-visible      /* Visible state */
.ray               /* Individual ray */
.ray-center        /* Center beam */
.ray-left          /* Left beam */
.ray-right         /* Right beam */
.ray-far-left      /* Far left beam */
.ray-far-right     /* Far right beam */

/* Screen Components */
.projection-screen  /* Screen container */
.screen-border      /* Video border */
.screen-glow        /* Glow effect */

/* Controls */
.projector-close-button  /* Close button */
```

### Animation Timing

| Element | Duration | Delay | Easing |
|---------|----------|-------|--------|
| Projector Descend | 1000ms | 100ms | cubic-bezier(0.4, 0, 0.2, 1) |
| Light Rays Fade In | 500ms | 300ms | ease |
| Screen Fade In | 600ms | 500ms | cubic-bezier(0.4, 0, 0.2, 1) |
| Video Play | - | 1200ms | - |
| Screen Glow Pulse | 3000ms | - | ease-in-out (infinite) |

## 🎯 Design Specifications

### Projector Dimensions

```
Desktop (≥768px):
┌─────────────────────────┐
│  Projector Body         │
│  Width: 180px           │
│  Height: 80px           │
│                         │
│  Lens: 50px diameter    │
│  Glass: 35px diameter   │
└─────────────────────────┘

Mobile (<768px):
┌─────────────────┐
│  Projector Body │
│  Width: 140px   │
│  Height: 60px   │
│                 │
│  Lens: 40px     │
│  Glass: 28px    │
└─────────────────┘
```

### Light Ray Configuration

```
                    PROJECTOR
                       │
          ╲            │            ╱
           ╲           │           ╱
            ╲     ╲    │    ╱     ╱
             ╲     ╲   │   ╱     ╱
              ╲     ╲  │  ╱     ╱
               ╲     ╲ │ ╱     ╱
                ╲     ╲│╱     ╱
                 ╲     │     ╱
                  ╲    │    ╱
                   ╲   │   ╱
                    ╲  │  ╱
                     ╲ │ ╱
                      ╲│╱
                       
Ray Angles:
- Center: 0° (vertical)
- Left: -15°
- Right: 15°
- Far Left: -25°
- Far Right: 25°
```

### Color Palette

| Element | Color | Usage |
|---------|-------|-------|
| Projector Body | `#2a2a2a` → `#0d0d0d` | Gradient housing |
| Lens Glass | `rgba(100, 181, 246, 0.3)` | Blue tint |
| Light Rays | `rgba(100, 181, 246, 0.15)` | Beam color |
| Screen Glow | `rgba(100, 181, 246, 0.1)` | Ambient glow |
| Screen Border | `rgba(100, 181, 246, 0.3)` | Border glow |

## 📱 Responsive Breakpoints

```css
/* Desktop (Default) */
.projector-body { width: 180px; height: 80px; }
.projector-rays { width: 600px; height: 400px; }
.projection-screen { width: 900px; }

/* Mobile (≤768px) */
@media (max-width: 768px) {
  .projector-body { width: 140px; height: 60px; }
  .projector-rays { width: 400px; height: 300px; }
  .projection-screen { width: 100%; max-width: 90vw; }
}
```

## 🔧 Customization

### Changing Video Source

```tsx
<ChapterVideoModal
  isOpen={showModal}
  onOpenChange={setShowModal}
  videoUrl="https://www.youtube.com/embed/YOUR_VIDEO_ID"
/>
```

### Adjusting Animation Speed

Edit the timeouts in `ChapterVideoModal.tsx`:

```tsx
const projectorTimer = setTimeout(() => setShowProjector(true), 100);  // Adjust
const screenTimer = setTimeout(() => setShowScreen(true), 800);        // Adjust
const playerTimer = setTimeout(() => setIsPlayerReady(true), 1200);    // Adjust
```

### Modifying Colors

Update CSS variables in `doc-pages.css`:

```css
/* Change blue theme to another color */
.lens-glass {
  background: radial-gradient(
    circle at 30% 30%,
    rgba(YOUR_COLOR, 0.3) 0%,
    rgba(YOUR_COLOR, 0.1) 40%,
    rgba(0, 0, 0, 0.8) 100%
  );
}
```

## 🧪 Testing

### Component Tests

```tsx
import { render, screen } from '@testing-library/react';
import { ChapterVideoModal } from './ChapterVideoModal';

describe('ChapterVideoModal', () => {
  it('renders when isOpen is true', () => {
    render(<ChapterVideoModal isOpen />);
    expect(screen.getByRole('dialog')).toBeInTheDocument();
  });

  it('calls onOpenChange when close button clicked', () => {
    const onOpenChange = jest.fn();
    render(<ChapterVideoModal isOpen onOpenChange={onOpenChange} />);
    
    fireEvent.click(screen.getByRole('button', { name: /close/i }));
    expect(onOpenChange).toHaveBeenCalledWith(false);
  });
});
```

## 🎯 Performance Considerations

1. **Animation Performance**: Uses CSS transforms and opacity for smooth 60fps animations
2. **Lazy Loading**: Video player only initializes when modal is open
3. **Cleanup**: All timeouts are properly cleared on unmount
4. **Portal Rendering**: Renders outside DOM hierarchy to avoid z-index issues

## 🌐 Browser Support

| Browser | Version | Support |
|---------|---------|---------|
| Chrome | 90+ | ✅ Full |
| Firefox | 88+ | ✅ Full |
| Safari | 14+ | ✅ Full |
| Edge | 90+ | ✅ Full |
| Mobile Safari | 14+ | ✅ Full |
| Chrome Android | 90+ | ✅ Full |

## 📝 Related Components

- [`DocPageActions`](../DocPageActions/) - Play button integration
- [`ChapterVideoButton`](./ChapterVideoButton.tsx) - Trigger button
- [`ChapterVideoPlayer`](./ChapterVideoPlayer.tsx) - Player wrapper

## 📄 License

Part of the AI Agent Factory book - Open Source Education
