
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-20 - Dynamic Calculator Accessibility (ARIA Live & Describedby)
**Learning:** For interactive UI components like dynamic calculators that update their results inline and might throw validation errors, screen readers often fail to announce these changes by default. Relying solely on visual changes (like text turning red or a box appearing) makes the application unusable for visually impaired users.
**Action:** Always ensure dynamic result containers and inline error messages use `aria-live="polite"` so state changes are announced without interrupting the user. Additionally, ensure form inputs are linked to their corresponding inline error messages using `aria-describedby` so the error context is clear upon focusing the input.
