# Introductory Module: HTML and CSS

## Purpose and scope

HTML and CSS are foundational web technologies, not general-purpose programming languages. HTML describes document structure and meaning; CSS controls presentation and layout. This module introduces accessible, semantic web documents and the separation of content from presentation. It is intentionally not forced into the Python problem sequence.

## Unit 1: Web foundations and accessible setup

### Lesson 1.1: How the web works
Explain browser, server, URL, request/response, HTML document, stylesheet, and DOM. Distinguish client-side structure from server-side programming.

### Lesson 1.2: Tools and workflow
Use a plain-text editor or VS Code. Create a project folder with `index.html` and `styles.css`. Open the HTML file in a browser and inspect the source. Use the browser's accessibility tree and developer tools where they are keyboard- and screen-reader-accessible.

**Skills checklist**
- [ ] I can explain the role of a browser, server, HTML, and CSS.
- [ ] I can create and save an HTML file and stylesheet.

## Unit 2: HTML document structure

### Lesson 2.1: Elements, tags, and attributes
Teach doctype, html, head, title, body, headings, paragraphs, links, lists, images, and attributes. Explain nesting and closing tags.

### Lesson 2.2: Semantic structure
Use header, nav, main, section, article, aside, and footer. Use headings in a logical hierarchy; do not choose elements for their default visual appearance.

### Lesson 2.3: Links, images, and alternative text
Use descriptive link text, meaningful image alternatives, and empty alt text for decorative images. Avoid instructions that depend only on color or position.

**Worked example**
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Student Reading List</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header><h1>Student Reading List</h1></header>
  <main>
    <section aria-labelledby="books-heading">
      <h2 id="books-heading">Books to read</h2>
      <ul>
        <li><a href="https://example.com/book">Accessible Web Design</a></li>
      </ul>
    </section>
  </main>
</body>
</html>
```

**Activities:** Add a second section, a descriptive link, and a meaningful image with alternative text. Validate nesting and read the page with a screen reader.

**Skills checklist**
- [ ] I can construct a valid HTML document.
- [ ] I can use semantic landmarks and a logical heading hierarchy.
- [ ] I can provide appropriate alternative text.

## Unit 3: Forms and structured content

### Lesson 3.1: Tables for data
Use table, caption, thead, tbody, tr, th, and td for genuinely tabular information. Associate headers with data cells; do not use tables for layout.

### Lesson 3.2: Accessible forms
Use label, input, select, textarea, button, fieldset, and legend. Ensure each control has an accessible name and instructions. Use native HTML validation where appropriate.

### Lesson 3.3: Lists and content structure
Choose ordered, unordered, and description lists according to meaning. Avoid using repeated line breaks or spaces to simulate layout.

**Activity:** Build a short contact form with visible labels, required fields, and clear error guidance. Test keyboard order and screen-reader announcements.

## Unit 4: CSS foundations

### Lesson 4.1: Selectors and declarations
Teach selector, property, value, rule set, class, id, inheritance, and cascade. Connect an external stylesheet using a link element.

### Lesson 4.2: Typography, color, and spacing
Use readable font sizing, line height, contrast, spacing, and focus indicators. Never use color as the only carrier of meaning.

### Lesson 4.3: Box model
Explain content, padding, border, margin, width, and box-sizing. Demonstrate how the computed box size is determined.

**Worked example**
```css
:root {
  color-scheme: light;
  font-family: system-ui, sans-serif;
  line-height: 1.5;
}
body {
  max-width: 48rem;
  margin: 0 auto;
  padding: 1rem;
}
a:focus-visible, button:focus-visible, input:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

**Activities:** Change one CSS property at a time. Test keyboard focus, zoom, text spacing, and contrast.

## Unit 5: Layout and responsive design

### Lesson 5.1: Normal flow and display
Understand block, inline, inline-block, and normal document flow.

### Lesson 5.2: Flexbox and Grid
Use Flexbox for one-dimensional alignment and Grid for two-dimensional layouts. Ensure source order remains meaningful without CSS.

### Lesson 5.3: Responsive design
Use relative units, media queries, and mobile-first design. Test zoom and reflow. Avoid fixed widths that force horizontal scrolling.

## Unit 6: Web accessibility and project

### Lesson 6.1: Accessible interaction
Teach keyboard operation, visible focus, landmarks, headings, labels, errors, target size, reduced motion, and semantic controls. Use native HTML before custom ARIA.

### Lesson 6.2: Test and validate
Validate HTML and CSS, test keyboard-only operation, inspect headings and landmarks with a screen reader, zoom to 200–400%, and check responsive reflow.

### Lesson 6.3: Mini-project
Build an accessible personal profile or reading-list site with two pages, semantic structure, a stylesheet, and an accessible form or data table.

**Assessment checklist**
- [ ] HTML structure is semantic and valid.
- [ ] Links, images, forms, and tables have appropriate accessible names and relationships.
- [ ] CSS does not remove focus visibility or meaning.
- [ ] The page works with keyboard, screen reader, zoom, and narrow viewport.
- [ ] Content and presentation are separated.

## References

- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/)
- [MDN HTML guides](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)
- [MDN CSS guides](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)
- [W3C Web Accessibility Initiative](https://www.w3.org/WAI/)
- [W3C Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
