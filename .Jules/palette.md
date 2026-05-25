
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-25 - Dynamic UI Calculator Accessibility
**Learning:** Dynamic result containers or inline validation feedback (such as in calculator micro-tools) often go unnoticed by screen readers if they lack proper live region markup, causing a disconnect when the user clicks 'Calculate' but hears no result or error message.
**Action:** Always ensure that inline validation feedback is linked via `aria-describedby` to the relevant input, and wrap both the error messages and dynamic result containers in `aria-live="polite"` so screen readers can announce state changes without interrupting the user. To prevent layout shifts (jank), style the error container with a minimum height (e.g., `min-h-[16px]`).
