
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-24 - Dynamic Calculator Accessibility & Validation
**Learning:** Dynamic calculators lacked screen reader announcements for the result elements and inline validation feedback. Users with screen readers would not know when the results updated or if their input was invalid.
**Action:** When adding dynamic UI features or calculators, ensure error containers and dynamic result containers use `aria-live="polite"` so screen readers announce state changes. Always associate inline validation feedback to the input field using `aria-describedby` and ensure the error container has a minimum height to prevent layout shift (jank) when messages appear.
