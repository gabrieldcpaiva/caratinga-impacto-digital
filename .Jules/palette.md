
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-31 - Missing Inline Validation and aria-live in Dynamic Calculators
**Learning:** Dynamic UI calculators across landing pages often lack inline validation feedback for empty or invalid inputs. Even when a result or error is displayed, it is not announced to screen readers because of missing `aria-live` attributes and `aria-describedby` associations, leading to a silent failure experience for assistive technology users.
**Action:** For dynamic UI calculators and components, always ensure inline validation feedback is provided and linked via `aria-describedby`. Wrap error messages and dynamic result containers in `aria-live="polite"` so screen readers announce state changes without interrupting. To prevent layout shift (jank), ensure error container spans/elements are styled with a minimum height (e.g., `min-h-[16px]` or `min-height: 18px`).
