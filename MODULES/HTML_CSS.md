# HTML and CSS: Structure and Presentation for the Web

## Purpose

This introductory module explains how web documents are structured with HTML and presented with CSS. It is designed for learners who already understand basic files, folders, and text editing. It does not assume prior web-development experience.

## Learning objectives

By the end of this module, learners should be able to explain the roles of HTML and CSS; create a semantic HTML document with a meaningful title, headings, paragraphs, links, lists, and form controls; distinguish semantic structure from visual presentation; associate labels with form controls; apply basic CSS selectors and box-model properties; and explain why accessibility belongs in document structure.

## HTML: semantic document structure

HTML (HyperText Markup Language) describes the meaning and structure of web content. Elements are represented by tags and may contain text, attributes, and nested elements. Browsers construct a document object model from the markup.

Semantic elements communicate purpose. Use headings in a logical hierarchy, paragraphs for prose, lists for grouped items, links for navigation, buttons for actions, and labels for form controls. Prefer native HTML semantics over generic containers with improvised behavior.

~~~html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Course Notes</title>
</head>
<body>
  <header>
    <h1>Course Notes</h1>
  </header>
  <main>
    <h2>Current topic</h2>
    <p>Semantic HTML describes the meaning of content.</p>
    <ul>
      <li>Structure content with meaningful elements.</li>
      <li>Use links for navigation.</li>
    </ul>
  </main>
</body>
</html>
~~~

The heading hierarchy should reflect the document outline. A heading is not simply a larger font. A screen-reader user may navigate directly by headings, links, landmarks, or form controls, so each must have a clear purpose.

## CSS: presentation rules

CSS (Cascading Style Sheets) describes how elements are presented. A rule consists of a selector and declarations. A declaration contains a property and value.

~~~css
body {
  font-family: system-ui, sans-serif;
  line-height: 1.5;
  margin: 2rem;
}

main {
  max-width: 70ch;
}

a {
  text-decoration: underline;
}
~~~

Selectors identify elements. Properties describe presentation. The cascade resolves competing declarations based on origin, importance, specificity, and source order. The box model describes content, padding, border, and margin. Layout systems such as Flexbox and Grid support responsive page structure.

## Accessibility principles

- Use semantic HTML before adding ARIA attributes.
- Preserve a logical heading hierarchy.
- Provide descriptive link text and labels for all form controls.
- Ensure keyboard access and visible focus.
- Do not use color alone to communicate state or meaning.
- Maintain sufficient text and interface contrast.
- Avoid removing browser zoom or text-resizing capabilities.
- Use alternative text for informative images; use empty alternative text for decorative images.
- Ensure dynamic content changes are perceivable and do not unexpectedly move focus.
- Test with keyboard navigation and screen readers, not only visual inspection.

Accessible HTML does not guarantee an accessible page. The complete interaction, browser behavior, CSS, and any JavaScript must be tested.

## Practice sequence

1. Identify the semantic elements in a supplied page and explain their roles.
2. Create a page with one main heading, two subheadings, paragraphs, a list, and descriptive links.
3. Add CSS for readable line length, spacing, and link distinction without relying on color alone.
4. Inspect the page using keyboard navigation and a screen reader.
5. Explain one difference between a semantic HTML element and a generic div.

## Further learning

- [MDN HTML documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN CSS documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [W3C Web Accessibility Initiative](https://www.w3.org/WAI/)
