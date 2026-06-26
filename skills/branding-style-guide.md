# Branding Style Guide — GlobalMail Pro

## Purpose

This is the global branding skill for GlobalMail Pro. It is pre-embedded
inside the agent system prompt in agents/one-command-agent.md and applies
to every output the agent produces — HTML release notes, diagrams, and
any visual artefacts.

You never need to open or paste this file when running the agent.

---

## Brand Identity

| Element | Value | Usage |
|---------|-------|-------|
| Product name | GlobalMail Pro | Use in page titles, navigation, and formal references |
| Help centre | GlobalMail Pro Help Centre | Used in HTML page titles |
| Copyright holder | GlobalMail Pro | Used in the required footer line |

---

## Colour Palette

These are the only colours permitted in agent output. They are derived
from the GlobalMail Pro product UI (dark navy sidebar, green primary action,
white content area).

### Primary colours
| Name | Hex | Usage |
|------|-----|-------|
| GMP Navy | #1B2A4A | H1, H2, sidebar backgrounds, primary headings |
| GMP Green | #2ECC71 | Primary action colour — "Validate Address" button, badges, accents |
| GMP Dark Green | #27AE60 | Hover state, borders on green elements |
| White | #FFFFFF | Page backgrounds, card surfaces |

### Supporting colours
| Name | Hex | Usage |
|------|-----|-------|
| GMP Light Navy | #2C3E6B | H3 headings, secondary headings |
| GMP Navy Tint | #EDF0F7 | Page background, table row alternates, card fills |
| GMP Green Tint | #E8F8F0 | Success states, "Valid" badges, callout backgrounds |

### Status colours (for validation history badges)
| Name | Hex | Usage |
|------|-----|-------|
| Valid Green | #2ECC71 | "Valid" status |
| Corrected Teal | #1ABC9C | "Corrected" status |
| Review Amber | #F39C12 | "Needs Review" status |

### Neutrals
| Name | Hex | Usage |
|------|-----|-------|
| Text Dark | #1A1A2E | Body text |
| Gray 1 | #6C7A8D | Muted text, captions |
| Gray 2 | #95A5B8 | Borders, secondary labels |
| Gray 3 | #D5DCE8 | Light borders, dividers |
| Gray 4 | #F0F3F8 | Table row alternates, backgrounds |

---

## Typography

| Role | Font | Weight | Notes |
|------|------|--------|-------|
| All text | Inter | Primary | Load from Google Fonts |
| Fallback | -apple-system, Arial | Any | Use when Inter unavailable |
| H1 | Inter Bold | 700 | GMP Navy #1B2A4A |
| H2 | Inter Bold | 700 | GMP Navy #1B2A4A, border-bottom GMP Green |
| H3 | Inter SemiBold | 600 | GMP Light Navy #2C3E6B |
| Body | Inter Regular | 400 | Text Dark #1A1A2E |
| Caption | Inter Regular | 400 | Gray 1 #6C7A8D |

In HTML output, always include this Google Fonts import:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

CSS font stack:
```css
font-family: "Inter", -apple-system, Arial, sans-serif;
```

---

## HTML Release Note CSS Template

Every HTML release note produced by the agent must use exactly this CSS:

```css
body {
  font-family: "Inter", -apple-system, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.75;
  color: #1A1A2E;
  background: #FFFFFF;
  max-width: 760px;
  margin: 0 auto;
  padding: 2rem 1.5rem 4rem;
}
h2 {
  font-size: 1.35rem;
  font-weight: 700;
  color: #1B2A4A;
  border-bottom: 3px solid #2ECC71;
  padding-bottom: 0.4rem;
  margin: 2rem 0 1rem;
}
h3 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #2C3E6B;
  margin: 1.5rem 0 0.75rem;
}
p {
  margin-bottom: 1rem;
  color: #1A1A2E;
}
strong {
  font-weight: 700;
  color: #1B2A4A;
}
ul {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 1rem;
}
ul li {
  padding: 0.25rem 0 0.25rem 1.25rem;
  position: relative;
  color: #1A1A2E;
}
ul li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.65rem;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #2ECC71;
}
hr {
  border: none;
  border-top: 1px solid #D5DCE8;
  margin: 1.5rem 0 0.75rem;
}
.version {
  font-size: 0.85rem;
  color: #95A5B8;
  font-weight: 600;
}
.rn-header {
  background: #1B2A4A;
  color: #FFFFFF;
  padding: 1rem 1.5rem;
  margin: -2rem -1.5rem 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.rn-header .product-name {
  font-size: 1rem;
  font-weight: 700;
  color: #FFFFFF;
}
.rn-header .header-rule {
  font-size: 0.85rem;
  color: rgba(255,255,255,0.55);
}
.rn-footer {
  margin-top: 3rem;
  padding-top: 1rem;
  border-top: 1px solid #D5DCE8;
  font-size: 0.8rem;
  color: #95A5B8;
  text-align: center;
}
```

---

## Required Page Header

Every HTML release note must begin with this header inside the body:
```html
<div class="rn-header">
  <span class="product-name">GlobalMail Pro</span>
  <span class="header-rule">|</span>
  <span class="header-rule">Help Centre</span>
</div>
```

---

## Required Copyright Footer

Every HTML release note must end with:
```html
<footer class="rn-footer">
  &copy; 2026 GlobalMail Pro. All rights reserved.
</footer>
```

---

## Diagram Rules

When diagrams are referenced in release notes:
- Use only GlobalMail Pro palette colours
- Use Inter/-apple-system/Arial font
- No drop shadows, no 3D effects, no decorative gradients
- Simple flat shapes: rectangles, circles, arrows
- Placeholder format: [INSERT: diagram — GlobalMail Pro brand colours, Inter font]

---

## File Naming Convention

`release-note-[version]-[short-slug].html`

Examples:
- release-note-3-2-0-real-time-validation.html
- release-note-3-2-0-dashboard-metrics-fix.html
- release-note-3-2-1-confidence-scoring.html

---

## Dual Output Rule

Every agent run produces two files per release note — a Markdown file
and an HTML file. Both files contain identical content. The Markdown
file is for version control and review. The HTML file is for publication.

### File naming — both files use the same slug

```
output/release-note-[version]-[slug].md
output/release-note-[version]-[slug].html
```

Where:
- `[version]` is the release number with hyphens: `1-1` for release 1.1
- `[slug]` is two to four lowercase words describing the change, hyphenated

Examples:
```
output/release-note-1-1-whats-new.md
output/release-note-1-1-whats-new.html
output/release-note-1-1-dashboard-metrics-fix.md
output/release-note-1-1-dashboard-metrics-fix.html
```

### HTML file requirements (applied on top of Markdown content)

The HTML file wraps the Markdown content in the full brand template:
- `<!DOCTYPE html>` with `lang="en"`
- `<title>` set to: `[Section heading] — GlobalMail Pro Help Centre`
- Inter Google Fonts import
- All CSS from the HTML Release Note CSS Template in this skill (inline)
- `<div class="rn-header">` with product name and Help Centre label
- Content rendered with branded h2, h3, p, ul, hr, and .version elements
- `<footer class="rn-footer">` copyright line

The HTML file is self-contained. No external CSS files. No external JS.
