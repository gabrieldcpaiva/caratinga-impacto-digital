
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-27 - Inline Validation and Aria-Live Dynamics
**Learning:** Dynamic calculator results and inline form validation were modifying the DOM without screen reader announcements or proper structural cues, potentially confusing visually impaired users and causing layout shifts when errors appeared.
**Action:** When adding inline error messages, allocate a minimum height (e.g., `min-h-[16px]`) to prevent jank. Use `aria-describedby` on inputs to link to errors, toggle `aria-invalid` appropriately, and wrap dynamic message containers (errors and results) with `aria-live="polite"` so state changes are properly announced.
