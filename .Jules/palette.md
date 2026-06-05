
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
## 2024-05-19 - Dynamic Calculators Validation & Accessibility
**Learning:** Dynamic calculators without explicit validation feedback and accessibility features (like `aria-live` and `aria-describedby`) cause screen reader interruptions and layout shifts when showing results/errors.
**Action:** Always add inline validation feedback linked via `aria-describedby`, wrap error messages and dynamic result containers in `aria-live="polite"`, and use fixed-height error containers (`min-h-[16px]`) to prevent layout shift.
