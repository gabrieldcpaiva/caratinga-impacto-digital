## 2026-05-25 - Dynamic Calculator Accessibility and Layout Shift
**Learning:** When injecting dynamic error messages for validation feedback in micro-tools/calculators, the absence of a reserved space for the error causes a layout shift (jank) which is unpleasant. Additionally, screen readers need to be aware of the error without losing focus.
**Action:** Always reserve space for error spans using CSS minimum heights (e.g., `min-h-[16px]`), link the error to the input using `aria-describedby`, and use `aria-live="polite"` on the error container and result boxes to ensure screen readers announce state changes without interrupting the user's flow.

## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
