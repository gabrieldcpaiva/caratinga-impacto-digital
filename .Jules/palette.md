
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-27 - Inline Validation and Layout Shifts
**Learning:** Adding dynamic inline error messages to input calculators without reserving vertical space causes jarring layout shifts that degrade the UX. Also, dynamically changing these text areas requires explicit `aria-live` attributes to ensure screen readers announce the state changes to visually impaired users.
**Action:** When adding inline validation, always ensure the error container has a minimum height (`min-h-[16px]` or `min-height: 18px`) and includes `aria-live="polite"` so screen readers can announce feedback naturally. Use `aria-describedby` on the input to link to the error message container.
