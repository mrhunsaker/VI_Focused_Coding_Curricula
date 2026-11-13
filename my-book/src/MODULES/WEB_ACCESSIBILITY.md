# Web Accessibility: ARIA, WCAG, and Accessible Design

## Purpose

Web accessibility is the practice of building websites and applications that people can use regardless of disability — including blind and low-vision users who rely on screen readers, keyboard-only users, and users with cognitive or motor disabilities. This module introduces accessibility as an engineering discipline: the standards (WCAG), the technologies (semantic HTML, ARIA, CSS, and the accessibility tree), the testing workflow (keyboard first, then screen reader), and the legal and professional context.

This module extends the HTML and CSS module. It assumes learners can write semantic HTML and basic stylesheets, and builds the accessibility layer on top. For a curriculum aimed at visually impaired learners, accessibility is not merely a compliance topic: it is a domain in which blind developers are, with proper training, among the most credible experts in the industry.

## Learning objectives

By the end of this module, learners should be able to explain how the accessibility tree connects the DOM to assistive technology; state the four WCAG principles (POUR) and give an example conformance technique for each; write semantic HTML that needs no ARIA; apply ARIA roles, states, and properties correctly and explain the first rule of ARIA; implement accessible forms, tables, and dialogs; design and test keyboard interaction, focus order, and visible focus; write text alternatives for images, charts, and controls; and conduct a basic screen-reader and keyboard audit of a web page.

## How assistive technology sees the web

A screen reader does not read the rendered pixels; it reads the **accessibility tree**, a parallel structure derived from the DOM. Each element exposes a **name** (its accessible label), a **role** (what it is), a **value** (its current state, where applicable), and its **state and properties** (expanded, checked, disabled, required). Browsers compute this tree from native HTML semantics first, then from ARIA attributes where authors supply them.

This is why semantic HTML is the foundation: a native `<button>` automatically has role `button`, is focusable, responds to Enter and Space, and announces itself correctly. A `<div onclick=...>` has none of that, and no amount of styling will add it.

## WCAG: the standard

The Web Content Accessibility Guidelines (WCAG), published by the W3C, organize success criteria under four principles — **POUR**:

- **Perceivable:** information must be available to sight, hearing, or touch. Examples: text alternatives for images, captions for video, sufficient contrast.
- **Operable:** every function must be usable without requiring specific physical abilities. Examples: full keyboard operability, no time limits without a way to extend, no seizure-inducing content.
- **Understandable:** content and controls must be predictable. Examples: consistent navigation, labeled inputs, clear error messages.
- **Robust:** content must work with current and future assistive technology. Examples: valid markup, correct name/role/value.

WCAG 2.1 and 2.2 define levels A, AA, and AAA. Level AA is the common legal and contractual target (including under the ADA, Section 508, and the European Accessibility Act). Learn the AA criteria relevant to your work; do not try to memorize all of them at once.

## Semantic HTML first

The most effective accessibility technique is choosing the right element:

- `<button>` for actions, `<a href>` for navigation — never a clickable `<div>`.
- `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>`, `<article>` for landmarks, which screen readers expose for direct navigation.
- One `<h1>` per page and a heading hierarchy without gaps.
- `<label for="id">` bound to every form control.
- `<table>` with `<th scope="col|row">` for genuine data tables — never for layout.
- Native `<details>`/`<summary>` for disclosure widgets when possible.

## ARIA: when HTML is not enough

ARIA (Accessible Rich Internet Applications) supplies semantics the platform does not. Its first rule: **do not use ARIA if a native element would work** — incorrect ARIA is worse than none.

~~~html
<!-- Bad: a div with a click handler has no role, no focus, no keyboard support -->
<div class="btn" onclick="save()">Save</div>

<!-- Good: native semantics -->
<button type="button" onclick="save()">Save</button>

<!-- Necessary ARIA: a tabbed interface has no single native element -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">Details</button>
  ...
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">...</div>
~~~

Key attribute families:

- **Roles:** `tab`, `dialog`, `alert`, `switch`, `progressbar`, `grid`.
- **States:** `aria-expanded`, `aria-checked`, `aria-disabled`, `aria-current`.
- **Properties:** `aria-label` and `aria-labelledby` (naming), `aria-describedby` (description), `aria-live` (announcing dynamic updates).

`aria-live` regions are how a page reports changes without a page load: form validation results, status messages, new chat lines. Use `role="status"` (polite) or `role="alert"` (assertive) rather than raw `aria-live` values where possible.

## Keyboard and focus

- Everything clickable must be reachable with Tab and operable with Enter, Space, and arrow keys as appropriate.
- Manage focus in scripts: when a dialog opens, move focus into it; when it closes, restore focus to the trigger; trap focus inside while it is open (use the native `<dialog>` element, which does much of this for you).
- Never remove the focus outline without providing an equally visible replacement style.
- Respect `prefers-reduced-motion` in animations.
- Provide a "skip to main content" link as the first focusable element on pages with long navigation.

## Forms and errors

~~~html
<label for="email">Email address</label>
<input id="email" type="email" autocomplete="email"
       aria-describedby="email-hint email-error">
<p id="email-hint">We send one confirmation message.</p>
<p id="email-error" role="alert">Enter an address in the name@example.com format.</p>
~~~

Errors must be text, associated with the field, and announced. Do not report errors by color or icon alone, and do not rely on placeholder text as the only label.

## Testing workflow

1. **Unplug the mouse (figuratively):** navigate the page with Tab, Shift+Tab, Enter, Space, and arrow keys only.
2. **Screen-reader pass:** test with at least NVDA (free, Windows) and VoiceOver (built into macOS and iOS); JAWS on Windows is also common. Learn the headings list, links list, and form-controls list commands — those are how real users audit a page.
3. **Automated scan:** axe DevTools, Lighthouse, or WAVE catch roughly a third of issues (missing alt text, contrast, unlabeled controls). Automation finds *violations*, not *usability*.
4. **Zoom and reflow:** at 200% zoom and 320px width, no content may be lost or require two-dimensional scrolling (WCAG 1.4.10).
5. **Manual judgment:** the remaining two-thirds of accessibility problems — focus order, announcement timing, meaningful alt text — require a human, and this is where trained screen-reader users have a professional edge.

## Accessibility as a career path

Digital accessibility is a growing, undersupplied specialty: auditors, remediation engineers, accessibility QA, and inclusive-design consultants. Professional credentials include the IAAP Certified Professional in Accessibility Core Competencies (CPACC) and Web Accessibility Specialist (WAS). Blind professionals are well represented — and highly sought after — in this field.

## Practice sequence

1. Take a page built with `<div>` buttons and rebuild it with semantic elements; verify the tab order and announcements improve with no JavaScript changes.
2. Add a complete ARIA tabbed interface with correct roving tabindex and arrow-key navigation, testing entirely by keyboard.
3. Build a form with labeled fields, hint text, and an `aria-live` error region; trigger each error and confirm it is announced.
4. Run an axe or Lighthouse scan on a real page, fix every reported issue, and list two issues the scan missed that you found by keyboard testing.
5. Write alt text for five images of increasing complexity, including one chart, using a short description plus a data table for the chart.
6. Audit one public website with NVDA's headings and links lists and write a one-page findings memo.

## Recommended introductory books

- W3C Web Accessibility Initiative. *Web Accessibility Perspectives* and the WCAG quick reference. Free, and the authoritative mapping of requirements to techniques. [WCAG 2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/).
- Gilbert, Regine. *Inclusive Design for a Digital World*. Apress, 2019. A practitioner-oriented introduction covering design and code.
- Kalbag, Laura. *Accessibility for Everyone*. A Book Apart, 2017. A short, plain-language orientation to the whole discipline, useful before diving into standards.

**Suggested use:** start with *Accessibility for Everyone* for the framing, then work directly from the WCAG quick reference while coding — it is the reference you will actually use professionally. Use the *Perspectives* videos to understand user impact.

## Further learning

- [W3C WAI: Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — tested interaction patterns for widgets
- [MDN Accessibility documentation](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)
- [Deque axe DevTools](https://www.deque.com/axe/) and [WebAIM](https://webaim.org/) — testing tools and articles
- [NVDA screen reader](https://www.nvaccess.org/) — free, open source, and scriptable