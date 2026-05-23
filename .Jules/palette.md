
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-11-25 - Dynamic Calculators ARIA Live Region & Validation
**Learning:** Dynamic calculators in this app previously relied entirely on visual cues for feedback and didn't gracefully handle invalid inputs. Screen reader users would not be notified when results changed dynamically.
**Action:** Always wrap dynamic result containers and inline error messages in `aria-live="polite"` so screen readers announce state changes automatically. Additionally, always validate inputs before executing calculations and provide inline feedback correctly linked via `aria-describedby`.
