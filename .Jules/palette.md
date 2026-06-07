
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-06-07 - Dynamic Calculator Accessibility and Validation
**Learning:** Dynamic calculators without inline validation fail silently when users click the calculate button without input. Additionally, dynamically appearing elements (like the result box or error messages) aren't announced to screen readers unless specifically marked. This leads to a confusing experience for assistive technologies.
**Action:** When creating or modifying dynamic calculators/forms, ensure inline validation is present, linked via `aria-describedby` to inputs, and wrap dynamic results/errors in elements with `aria-live="polite"` (and a minimum height to prevent layout shift) so screen readers announce changes without interrupting the user's flow.
