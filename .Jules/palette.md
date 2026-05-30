
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
## 2024-05-14 - Dynamic Error Messages Layout Shift and Accessibility
**Learning:** When injecting dynamic inline error messages for calculators or forms, lack of a minimum height container causes layout shifts (jank). Adding `aria-live="polite"` to both the error container and dynamic result sections ensures screen readers announce the state changes.
**Action:** Always use `min-h-[16px]` (or equivalent) for error message containers to reserve space, and utilize `aria-live="polite"` on dynamically updating UI elements.
