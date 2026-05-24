
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-24 - Dynamic Calculator Validation & A11y
**Learning:** Dynamic UI calculators often lack inline validation feedback, which leaves users confused when they interact with the tool without providing input. Furthermore, simply displaying text on the screen isn't enough; screen readers need to be notified.
**Action:** Always provide inline validation feedback for dynamic components. Link error messages to inputs using `aria-describedby` and wrap both error messages and dynamic result containers in `aria-live="polite"` so screen readers announce state changes without interrupting the user.
