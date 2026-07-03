# Branding Style Guide — WealthWise



## Purpose



This is the global branding skill for WealthWise. It is pre-embedded

inside the agent system prompt in agents/one-command-agent.md and applies

to every output the agent produces — HTML release notes, diagrams, and

any visual artefacts.



You never need to open or paste this file when running the agent.



---



## Brand Identity



| Element | Value | Usage |

|---------|-------|-------|

| Product name | WealthWise | Use in page titles, navigation, and formal references |

| Help centre | WealthWise Help Centre | Used in HTML page titles |

| Copyright holder | WealthWise | Used in the required footer line |



---



## Colour Palette



These are the only colours permitted in agent output. They are derived

from the WealthWise product UI (light neutral canvas, green primary action,

purple reserved exclusively for AI-generated content).



### Primary colours

| Name | Hex | Usage |

|------|-----|-------|

| WW Green | #1D9E75 | Primary action colour — buttons, links, active nav, positive values, H2 accent rule |

| WW Dark Green | #0F6E56 | Hover state, emphasis text on green tints |

| WW Green Tint | #E1F5EE | Success/active backgrounds, badges, callouts |

| White | #FFFFFF | Page backgrounds, card surfaces |



### AI Accent colours — reserved

| Name | Hex | Usage |

|------|-----|-------|

| WW Purple | #534AB7 | **Reserved exclusively for AI-generated content** — AI Advisor callouts, AI-tagged features. Never used for standard UI or non-AI content |

| WW Dark Purple | #3C3489 | AI text on light purple backgrounds |

| WW Purple Tint | #EEEDFE | Background for AI insight/suggestion callout boxes |



> **Rule:** If a release note item, badge, or callout does not describe AI-driven functionality, it must never use the purple family. This consistency is what trains readers to recognize "this came from the AI" at a glance.



### Supporting colours

| Name | Hex | Usage |

|------|-----|-------|

| WW Navy Text | #1A1A1A | H1, H2 headings, primary body text |

| WW Slate | #5A6475 | H3 headings, secondary text, captions |

| WW Page Tint | #F4F6F8 | Page background, table row alternates, card fills |



### Status colours (for release categories and validation/badge states)

| Name | Hex | Usage |

|------|-----|-------|

| Success Green | #1D9E75 | "New", "Fixed", "Valid" / positive status |

| Caution Amber | #BA7517 | "Needs Review", "Deprecated", near-limit warnings |

| Error Red | #A32D2D | "Critical", "Breaking Change", failed/error status |

| AI Purple | #534AB7 | "AI" tag — used only alongside AI-authored content |

| Info Blue | #0C447C | Neutral informational tags |



### Neutrals

| Name | Hex | Usage |

|------|-----|-------|

| Text Dark | #1A1A1A | Body text |

| Gray 1 | #5A6475 | Muted text, captions, metadata |

| Gray 2 | #9AA3AF | Placeholder text, tertiary labels |

| Gray 3 | rgba(0,0,0,0.09) | Light borders, dividers |

| Gray 4 | rgba(0,0,0,0.18) | Input borders, stronger separators |

| Gray 5 | #F4F6F8 | Table row alternates, subtle backgrounds |



---



## Typography



| Role | Font | Weight | Notes |

|------|------|--------|-------|

| All text | System UI stack | Primary | No external font load required |

| Fallback | -apple-system, Arial | Any | Applies automatically within the stack |

| H1 | System Bold | 800 | WW Navy Text #1A1A1A, letter-spacing -0.3px |

| H2 | System Bold | 700 | WW Navy Text #1A1A1A, border-bottom WW Green |

| H3 | System SemiBold | 600 | WW Slate #5A6475 |

| Body | System Regular | 400–500 | Text Dark #1A1A1A |

| Caption | System Regular | 400 | Gray 1 #5A6475 |



WealthWise intentionally uses the native OS font stack rather than a web font — no Google Fonts import is required or permitted, to keep release notes loading instantly and consistent with the product's own typography choice.



CSS font stack:

```css

font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

```



---



## HTML Release Note CSS Template



Every HTML release note produced by the agent must use exactly this CSS:



```css

body {

  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

  font-size: 16px;

  line-height: 1.7;

  color: #1A1A1A;

  background: #FFFFFF;

  max-width: 760px;

  margin: 0 auto;

  padding: 2rem 1.5rem 4rem;

}

h1 {

  font-size: 1.6rem;

  font-weight: 800;

  color: #1A1A1A;

  letter-spacing: -0.3px;

  margin: 0 0 0.5rem;

}

h2 {

  font-size: 1.3rem;

  font-weight: 700;

  color: #1A1A1A;

  border-bottom: 3px solid #1D9E75;

  padding-bottom: 0.4rem;

  margin: 2rem 0 1rem;

  display: flex;

  align-items: center;

  gap: 0.5rem;

}

h3 {

  font-size: 1.02rem;

  font-weight: 600;

  color: #5A6475;

  margin: 1.5rem 0 0.75rem;

}

p {

  margin-bottom: 1rem;

  color: #1A1A1A;

}

strong {

  font-weight: 700;

  color: #1A1A1A;

}

ul {

  list-style: none;

  padding: 0;

  margin: 0.5rem 0 1rem;

}

ul li {

  padding: 0.3rem 0 0.3rem 1.25rem;

  position: relative;

  color: #1A1A1A;

}

ul li::before {

  content: '';

  position: absolute;

  left: 0;

  top: 0.7rem;

  width: 7px;

  height: 7px;

  border-radius: 50%;

  background: #1D9E75;

}

hr {

  border: none;

  border-top: 1px solid rgba(0,0,0,0.09);

  margin: 1.5rem 0 0.75rem;

}

.version {

  font-size: 0.85rem;

  color: #9AA3AF;

  font-weight: 600;

}

.tag {

  display: inline-flex;

  align-items: center;

  gap: 4px;

  padding: 2px 9px;

  border-radius: 20px;

  font-size: 0.72rem;

  font-weight: 700;

  margin-left: 0.4rem;

  vertical-align: middle;

}

.tag-ai {

  background: #EEEDFE;

  color: #3C3489;

}

.tag-security {

  background: #FCEBEB;

  color: #A32D2D;

}

.tag-deprecated {

  background: #FAEEDA;

  color: #BA7517;

}

.rn-header {

  background: #1A1A1A;

  color: #FFFFFF;

  padding: 1rem 1.5rem;

  margin: -2rem -1.5rem 2rem;

  display: flex;

  align-items: center;

  gap: 0.75rem;

  border-radius: 0 0 12px 12px;

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

.rn-known-issue {

  background: #FAEEDA;

  border: 1px solid #BA7517;

  border-radius: 12px;

  padding: 1rem 1.25rem;

  margin: 1rem 0;

}

.rn-footer {

  margin-top: 3rem;

  padding-top: 1rem;

  border-top: 1px solid rgba(0,0,0,0.09);

  font-size: 0.8rem;

  color: #9AA3AF;

  text-align: center;

}

```



---



## Required Page Header



Every HTML release note must begin with this header inside the body:

```html

<div class="rn-header">

  <span class="product-name">WealthWise</span>

  <span class="header-rule">|</span>

  <span class="header-rule">Help Centre</span>

</div>

```



---



## Required Copyright Footer



Every HTML release note must end with:

```html

<footer class="rn-footer">

  &copy; 2026 WealthWise. All rights reserved.

</footer>

```



---



## Category Icon & Tag Rules



Release note category headings (`h2`) must use exactly these icons, in this fixed order, omitting any category with zero entries:



| Category | Icon | Order |

|----------|------|-------|

| What's New | 🚀 | 1 |

| Enhancements | ✨ | 2 |

| Bug Fixes| 🐛 | 3 |

| Known Issues | — | 6 (footer section, no numbered order above it) |



Any list item describing AI-driven functionality (AI Advisor, AI insights, AI-generated suggestions) must include an inline `<span class="tag tag-ai">AI</span>` immediately after the feature name.

Known Issues must be wrapped in a `<div class="rn-known-issue">` block rather than a plain bullet, so they are visually distinct from resolved items.



---



## Diagram Rules



When diagrams are referenced in release notes:

- Use only WealthWise palette colours (§ Colour Palette above)

- Use the system font stack (-apple-system, Segoe UI, Roboto)

- No drop shadows beyond the standard card elevation (`0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.05)`) — no 3D effects, no decorative gradients

- Simple flat shapes with rounded corners (8px/12px radius per the product's own component style): rectangles, circles, arrows

- AI-related diagram elements must be filled with WW Purple (#534AB7) or WW Purple Tint (#EEEDFE) exclusively — never green

- Placeholder format: [INSERT: diagram — WealthWise brand colours, system font]



---



## File Naming Convention



`release-note-[version]-[short-slug].html`



Examples:

- release-note-1-0-ai-advisor-launch.html

- release-note-1-0-investment-tracking.html

- release-note-1-1-budget-rounding-fix.html



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

- `[version]` is the release number with hyphens: `1-0` for release 1.0

- `[slug]` is two to four lowercase words describing the change, hyphenated



Examples:

```

output/release-note-1-0-whats-new.md

output/release-note-1-0-whats-new.html

output/release-note-1-0-dashboard-metrics-fix.md

output/release-note-1-0-dashboard-metrics-fix.html

```



### HTML file requirements (applied on top of Markdown content)



The HTML file wraps the Markdown content in the full brand template:

- `<!DOCTYPE html>` with `lang="en"`

- `<title>` set to: `[Section heading] — WealthWise Help Centre`

- No external font import — relies on the system font stack only

- All CSS from the HTML Release Note CSS Template in this skill (inline)

- `<div class="rn-header">` with product name and Help Centre label

- Content rendered with branded h1, h2, h3, p, ul, hr, .tag, .version, and .rn-known-issue elements

- `<footer class="rn-footer">` copyright line



The HTML file is self-contained. No external CSS files. No external JS.
