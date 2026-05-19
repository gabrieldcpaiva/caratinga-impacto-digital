## 2024-05-17 - [Form Input Accessibility]
 **Learning:** Discovered inputs across the business directories lacked programmatic association with their labels, reducing screen reader accessibility. Some standalone inputs like the revenue field in `solucao/index.html` were entirely missing `aria-label` or visible `<label>` tags.
 **Action:** Always ensure `<label>` tags explicitly use the `for="..."` attribute matching the `id` of their input. When a visible label is intentionally omitted for design reasons, explicitly apply `aria-label="..."` directly on the input element.
