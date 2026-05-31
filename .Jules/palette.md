
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
## 2026-05-31 - Add aria-live to dynamic result containers
**Learning:** Dynamic result containers that appear or change value after user interaction (like calculators) without a page reload need `aria-live="polite"` so screen readers know to announce the new content. Without this, visually impaired users may not realize a result has been calculated.
**Action:** Always verify that dynamic update containers (like error messages, tooltips, or calculation results) have an `aria-live` attribute to ensure state changes are announced without interrupting the user.
