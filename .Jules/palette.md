
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-17 - Dynamic Inline Validation UX
**Learning:** In dynamic UI calculators, layout shifts (jank) caused by newly injected inline validation error messages can disrupt the user experience. Additionally, changes in error state or successful result calculations often go unnoticed by screen readers if they lack live regions.
**Action:** Always wrap dynamically updated result and error message containers with `aria-live="polite"` so screen readers announce the changes without interrupting the user. For error message spans/divs below inputs, guarantee a minimum height (e.g. `min-h-[16px]` or `min-height: 18px`) in the CSS to prevent layout shift when the text content changes from empty to visible. Finally, link the error message explicitly to the input using `aria-describedby`.
