
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-10-24 - Prevent Layout Shift with Dynamic Inline Validation
**Learning:** When using `aria-live` to announce dynamic validation errors on input fields, dynamically revealing the error text can cause distracting layout shifts (jank) in the form.
**Action:** Always pre-allocate space for dynamic inline validation using CSS rules like `min-h-[16px]` or `min-height: 16px` on the error container before it becomes visible, ensuring a smoother visual experience while keeping it accessible to screen readers.
