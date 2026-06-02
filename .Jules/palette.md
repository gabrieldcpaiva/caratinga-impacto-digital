
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-15 - Missing Inline Validation and ARIA-Live Feedback
**Learning:** Dynamic calculators within the application often fail to provide accessible feedback for validation errors and state changes. Screen readers are unaware of updates because dynamic result containers and error messages are missing `aria-live` attributes. Furthermore, error containers lack a minimum height, leading to layout shift (jank) when validation messages appear.
**Action:** For dynamic components, always provide inline validation linked via `aria-describedby`, wrap error messages and result containers in `aria-live="polite"`, and ensure error containers have a minimum height (e.g., `min-h-[16px]`) to prevent layout shift.
