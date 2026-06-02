
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Dynamic Calculator Accessibility and Layout Stability
**Learning:** Dynamic calculators that display inline validation errors or results need clear communication with screen readers and stable layouts to prevent jank.
**Action:** When creating dynamic validation or results, always use `aria-describedby` to link inputs to their error containers, and apply `aria-live="polite"` to error and result containers so screen readers announce changes. Use `min-h-[16px]` or similar minimum height on error containers to prevent the layout from shifting when text is injected.
