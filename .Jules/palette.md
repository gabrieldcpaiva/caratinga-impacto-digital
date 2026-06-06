
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-06-06 - Inline Validation and Layout Shifts
**Learning:** Adding dynamic error messages inline can cause layout shifts (jank) which are poor UX. Screen readers also need to be explicitly told about dynamic content changes using `aria-live`.
**Action:** When adding inline validation, always pre-allocate space for the error message container using a minimum height (e.g., `min-h-[16px]`), link it to the input with `aria-describedby`, and use `aria-live="polite"` on both error messages and dynamic result containers.
