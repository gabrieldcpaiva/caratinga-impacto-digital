
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2026-06-03 - Inline Validation and Layout Shift
**Learning:** When adding dynamic error messages to form inputs, it's critical to prevent layout shift (jank) which can disorient users. It's also necessary to associate these errors with the input via `aria-describedby` and ensure screen readers announce them using `aria-live="polite"`.
**Action:** Always wrap dynamic inline error messages in a container with a fixed minimum height (e.g., `min-h-[16px]`) to reserve space in the layout. Always use `aria-describedby` on the input linking to the error's ID, and wrap the error text in an `aria-live="polite"` container.
