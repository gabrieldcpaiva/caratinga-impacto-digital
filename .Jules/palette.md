
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Inline Validation and Live Regions for Calculators
**Learning:** The simple dynamic calculators in these landing pages provided no feedback when submitted empty. Screen readers were unaware of either failure or success, and keyboard users lost context when nothing happened.
**Action:** When implementing or fixing dynamic UI calculators, always ensure inline validation feedback is provided (e.g., an error message below the input) and that it's linked via `aria-describedby`. Crucially, wrap both error messages and dynamic result containers in `aria-live="polite"` so screen readers announce state changes without interrupting the user.
