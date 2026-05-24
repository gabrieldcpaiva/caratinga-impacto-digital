
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Dynamic State Announcements via ARIA
**Learning:** For dynamic UI components like calculators (e.g., in `metta/index.html`), screen readers will remain silent when results appear or error states are triggered unless explicit roles are provided. When an error is simply styled as `display: block` or a result container fades in, visually impaired users receive no context.
**Action:** Always link inline validation error messages to inputs using `aria-describedby` so the error is read aloud upon focus. For dynamic result areas and error containers, apply `aria-live="polite"` so screen readers seamlessly announce the text (or error) as it updates without interrupting the user's flow.
