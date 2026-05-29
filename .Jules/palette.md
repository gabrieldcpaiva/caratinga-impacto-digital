
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
## 2025-05-29 - [Inline Validation and Dynamic Feedback]
**Learning:** Using `aria-live="polite"` on dynamic error message containers and result components is critical for screen reader users to be notified of state changes without interrupting their current task. Additionally, reserving space with `min-h-[16px]` prevents layout shift (jank) when these elements become visible.
**Action:** Always add `aria-live` to dynamically updated error and result containers, explicitly associate error messages with inputs using `aria-describedby`, and use minimum heights to preserve layout stability in all future component enhancements.
