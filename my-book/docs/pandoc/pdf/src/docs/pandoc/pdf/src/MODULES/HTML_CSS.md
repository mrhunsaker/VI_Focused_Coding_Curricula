[Header 2 ("html-and-css-structure-and-presentation-for-the-web", [], []) [Str "HTML and CSS: Structure and Presentation for the Web"], Header 3 ("purpose", ["unnumbered", "unlisted"], []) [Str "Purpose"], Para [Str "This introductory module explains how web documents are structured with HTML and presented with CSS. It is designed for learners who already understand basic files, folders, and text editing. It does not assume prior web-development experience."], Header 3 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning objectives"], Para [Str "By the end of this module, learners should be able to explain the roles of HTML and CSS; create a semantic HTML document with a meaningful title, headings, paragraphs, links, lists, and form controls; distinguish semantic structure from visual presentation; associate labels with form controls; apply basic CSS selectors and box-model properties; and explain why accessibility belongs in document structure."], Header 3 ("html-semantic-document-structure", ["unnumbered", "unlisted"], []) [Str "HTML: semantic document structure"], Para [Str "HTML (HyperText Markup Language) describes the meaning and structure of web content. Elements are represented by tags and may contain text, attributes, and nested elements. Browsers construct a document object model from the markup."], Para [Str "Semantic elements communicate purpose. Use headings in a logical hierarchy, paragraphs for prose, lists for grouped items, links for navigation, buttons for actions, and labels for form controls. Prefer native HTML semantics over generic containers with improvised behavior."], CodeBlock ("", ["html"], []) "<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
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
", Para [Str "The heading hierarchy should reflect the document outline. A heading is not simply a larger font. A screen-reader user may navigate directly by headings, links, landmarks, or form controls, so each must have a clear purpose."], Header 3 ("css-presentation-rules", ["unnumbered", "unlisted"], []) [Str "CSS: presentation rules"], Para [Str "CSS (Cascading Style Sheets) describes how elements are presented. A rule consists of a selector and declarations. A declaration contains a property and value."], CodeBlock ("", ["css"], []) "body {
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
", Para [Str "Selectors identify elements. Properties describe presentation. The cascade resolves competing declarations based on origin, importance, specificity, and source order. The box model describes content, padding, border, and margin. Layout systems such as Flexbox and Grid support responsive page structure."], Header 3 ("accessibility-principles", ["unnumbered", "unlisted"], []) [Str "Accessibility principles"], BulletList [[Plain [Str "Use semantic HTML before adding ARIA attributes."]], [Plain [Str "Preserve a logical heading hierarchy."]], [Plain [Str "Provide descriptive link text and labels for all form controls."]], [Plain [Str "Ensure keyboard access and visible focus."]], [Plain [Str "Do not use color alone to communicate state or meaning."]], [Plain [Str "Maintain sufficient text and interface contrast."]], [Plain [Str "Avoid removing browser zoom or text-resizing capabilities."]], [Plain [Str "Use alternative text for informative images; use empty alternative text for decorative images."]], [Plain [Str "Ensure dynamic content changes are perceivable and do not unexpectedly move focus."]], [Plain [Str "Test with keyboard navigation and screen readers, not only visual inspection."]]], Para [Str "Accessible HTML does not guarantee an accessible page. The complete interaction, browser behavior, CSS, and any JavaScript must be tested."], Header 3 ("practice-sequence", ["unnumbered", "unlisted"], []) [Str "Practice sequence"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Identify the semantic elements in a supplied page and explain their roles."]], [Plain [Str "Create a page with one main heading, two subheadings, paragraphs, a list, and descriptive links."]], [Plain [Str "Add CSS for readable line length, spacing, and link distinction without relying on color alone."]], [Plain [Str "Inspect the page using keyboard navigation and a screen reader."]], [Plain [Str "Explain one difference between a semantic HTML element and a generic div."]]], Header 3 ("recommended-introductory-books", ["unnumbered", "unlisted"], []) [Str "Recommended introductory books"], BulletList [[Plain [Str "Robbins, Jennifer. ", Emph [Str "Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, and Web Graphics"], Str ", 5th edition. O'Reilly Media, 2018. A broad introduction to web fundamentals, semantic HTML, CSS, responsive layouts, and web design tools. ", Link ("", [], []) [Str "Publisher page"] ("https://www.oreilly.com/library/view/learning-web-design/9781491960196/", ""), Str "."]]], Para [Strong [Str "Accessibility note:"], Str " this is a visual-design-oriented book and may use diagrams, screenshots, and visual examples. Use it selectively for terminology and reference; this module's semantic, keyboard-first, and screen-reader-oriented explanations remain the required learning path. Validate examples against current HTML and CSS standards."], Header 3 ("further-learning", ["unnumbered", "unlisted"], []) [Str "Further learning"], BulletList [[Plain [Link ("", [], []) [Str "MDN HTML documentation"] ("https://developer.mozilla.org/en-US/docs/Web/HTML", "")]], [Plain [Link ("", [], []) [Str "MDN CSS documentation"] ("https://developer.mozilla.org/en-US/docs/Web/CSS", "")]], [Plain [Link ("", [], []) [Str "W3C Web Accessibility Initiative"] ("https://www.w3.org/WAI/", "")]]]]