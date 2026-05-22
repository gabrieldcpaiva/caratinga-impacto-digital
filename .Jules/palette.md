
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Dynamic UI Calculators Accessibility
**Learning:** Calculators and dynamic UI elements that display results based on user input often lack announcements for screen readers, leading to a confusing experience where users are unaware the result has updated or if an error occurred.
**Action:** Always wrap dynamic result containers and validation error messages in `aria-live="polite"` so screen readers announce state changes. Furthermore, link inline validation messages to their inputs using `aria-describedby` to provide immediate context to assistive technologies.
