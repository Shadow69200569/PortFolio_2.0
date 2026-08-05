---
name: Obsidian Glass
colors:
  surface: '#1A1A1A'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c7c4d8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#918fa1'
  outline-variant: '#464555'
  surface-tint: '#c4c0ff'
  primary: '#c4c0ff'
  on-primary: '#2000a4'
  primary-container: '#8781ff'
  on-primary-container: '#1b0091'
  inverse-primary: '#4f44e2'
  secondary: '#d0bcff'
  on-secondary: '#3c0091'
  secondary-container: '#571bc1'
  on-secondary-container: '#c4abff'
  tertiary: '#ddb7ff'
  on-tertiary: '#490080'
  tertiary-container: '#b76dff'
  on-tertiary-container: '#400071'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c4c0ff'
  on-primary-fixed: '#100069'
  on-primary-fixed-variant: '#3622ca'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#f0dbff'
  tertiary-fixed-dim: '#ddb7ff'
  on-tertiary-fixed: '#2c0051'
  on-tertiary-fixed-variant: '#6900b3'
  background: '#111111'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
  text-high: '#FFFFFF'
  text-low: rgba(255, 255, 255, 0.6)
  glass-border: rgba(255, 255, 255, 0.1)
  accent-cyan: '#5EAEEA'
  accent-orange: '#F0531C'
typography:
  display-hero:
    fontFamily: Hanken Grotesk
    fontSize: 120px
    fontWeight: '700'
    lineHeight: 110%
    letterSpacing: -0.04em
  display-hero-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 110%
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 64px
    fontWeight: '600'
    lineHeight: 120%
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 130%
  body-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '300'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-mono:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 100%
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  section-padding-lg: 12rem
  section-padding-md: 8rem
  section-padding-sm: 4rem
  gutter: 2rem
  container-max: 1440px
---

## Brand & Style

This design system is engineered for high-end digital portfolios and creative showcases where the interface acts as a silent, premium gallery for the work it contains. The brand personality is sophisticated, avant-garde, and meticulously curated, drawing inspiration from Apple’s precision and Framer’s fluid motion.

The visual direction combines **Minimalism** with **Glassmorphism**. It utilizes expansive negative space to create a sense of luxury, while depth is established through layered translucent surfaces and subtle atmospheric background gradients. The aesthetic is anchored in a dark, nocturnal environment that allows vibrant accent colors to appear self-illuminated. 

Key attributes:
- **Atmospheric Depth:** Usage of background "blobs" and grain textures.
- **Precision:** Razor-sharp typography paired with generous, intentional padding.
- **Fluidity:** Soft transitions and magnetic interactions that respond to user intent.

## Colors

The color palette is built on a "True Dark" foundation. The primary background uses a deep charcoal (`#111111`) to ensure pure black levels on OLED displays, while the surface color (`#1A1A1A`) provides a subtle lift for interactive containers.

- **Primary/Secondary Accents:** A spectrum of electric indigos and violets creates a sense of "digital neon" that guides the eye toward calls to action.
- **Text Contrast:** High-contrast white is reserved for headlines and primary labels. Body copy and secondary metadata utilize a lowered opacity (60%) to prevent visual fatigue and establish hierarchy.
- **Glassmorphism:** All elevated surfaces must implement a 1px white border at 10% opacity and a 12px backdrop blur to simulate frosted obsidian glass.

## Typography

The typography system relies on a high-contrast pairing of **Hanken Grotesk** for impactful headings and **Inter** for legible, modern body text.

- **Fluid Scaling:** For display headings, use a viewport-width-based calculation (e.g., `clamp(48px, 8vw, 120px)`) to ensure the type dominates the screen on all devices.
- **Editorial Labels:** **Space Mono** is used sparingly for metadata, categories, and technical labels to add a "designed" editorial feel.
- **Leading:** Body text utilizes a 1.6 line-height to maintain the "airy" feel of the overall design system.

## Layout & Spacing

This design system employs an **extreme whitespace** philosophy. Layouts are built on a 12-column fluid grid, but the focus is on the vertical rhythm and the "breathing room" between sections.

- **Sectioning:** Vertical separation between major content blocks should never drop below `8rem` on desktop. This forces the user to focus on one piece of content at a time.
- **Margins:** Desktop layouts should maintain a minimum of `4rem` side margins. On mobile, this reduces to `1.5rem`.
- **Reflow:** As the screen narrows, the 12-column grid collapses into 4 columns. Section padding should scale linearly from `12rem` (desktop) to `4rem` (mobile).

## Elevation & Depth

Depth is not communicated through heavy drop shadows but through **tonal layering and translucency**.

1.  **The Void (Level 0):** The base background (`#111111`) with a subtle 3% grain/noise overlay.
2.  **Atmosphere (Level 1):** Large, soft-edged gradient "blobs" (using primary/secondary accents) with 40% opacity, placed behind content to create a sense of backlighting.
3.  **Glass Containers (Level 2):** Surfaces (`#1A1A1A`) with 80% opacity, 12px backdrop blur, and a 1px white border at 10% opacity.
4.  **Floating Elements (Level 3):** Buttons and active chips that use a subtle `0 20px 40px rgba(0,0,0,0.4)` shadow to appear physically closer to the user.

## Shapes

The shape language is generous and friendly, contrasting the technical nature of the dark mode. 

- **Containers:** All cards, modal windows, and main surface containers use a `24px` radius.
- **Buttons:** Primary buttons use a fully rounded "pill" shape or a minimum of `12px` to ensure they feel tactile.
- **Consistency:** If an element is nested within a `24px` container, the child element should have a slightly smaller radius (e.g., `16px`) to maintain concentric visual harmony.

## Components

### Buttons
- **Magnetic Buttons:** All primary calls to action should implement a magnetic hover effect where the button subtly follows the cursor within a 20px range.
- **Styles:** Primary buttons use a gradient from `#6C63FF` to `#A855F7`. Secondary buttons use the "Glass" style (border + blur).

### Cards
- Cards do not have visible shadows. They rely on the `1px` border and background blur to separate from the background. 
- On hover, the border opacity should increase from 10% to 30%.

### Input Fields
- Inputs are dark and minimal: `#1A1A1A` background, `24px` radius, and a `1px` border that glows with the primary accent color on focus.

### Navigation
- The navigation bar should be a "floating" glass pill, centered at either the top or bottom of the viewport, with high backdrop blur.

### Imagery
- Images should feature a very subtle `24px` corner radius and, where possible, a grayscale-to-color hover transition to maintain the premium, monochromatic aesthetic.