
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2026-05-28 - Dynamic Validation Accessibility
**Learning:** Dynamic calculator results and inline validation errors frequently lacked 'aria-live' properties to announce state changes, and errors were not explicitly associated with inputs via 'aria-describedby'.
**Action:** Ensure all dynamically injected validation messages and result containers are wrapped in 'aria-live="polite"' and properly associated with inputs using 'aria-describedby'.
