
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-06-25 - Dynamic Form Validation and Accessibility
**Learning:** Simple HTML calculators and micro-tools often fail silently if a user clicks "Calculate" with an empty or invalid input. Furthermore, if a dynamic error message or result *does* appear, screen readers might not announce it, leaving users confused.
**Action:** When creating or modifying dynamic calculators, always implement inline validation. Use `aria-describedby` to associate inputs with their error containers. Ensure both error containers and dynamic result containers use `aria-live="polite"` so state changes are announced. Lastly, prevent layout shift by giving error containers a minimum height.
