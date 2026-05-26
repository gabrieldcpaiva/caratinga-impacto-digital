
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2026-05-26 - Dynamic Inline Validation and Aria-Live
**Learning:** When adding dynamic inline validation to forms or updating results, injecting error messages can cause layout shifts (jank) and screen readers may miss the updates.
**Action:** Always provide a dedicated container for dynamic feedback styled with a minimum height (e.g., `min-h-[16px]`) to prevent layout shifts. Ensure these containers use `aria-live="polite"` so screen readers announce changes immediately, and link validation containers to their inputs using `aria-describedby`.
