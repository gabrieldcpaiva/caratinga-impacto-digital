
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Missing Inline Validation & Aria-Live Regions in Dynamic Calculators
**Learning:** Dynamic calculators (like in `solucao` and `estacionamento-caratinga`) previously failed silently on empty inputs, leaving users without feedback. Additionally, dynamically updated results lacked `aria-live` attributes, meaning screen reader users wouldn't be notified when the calculation result appeared.
**Action:** Always implement inline validation for input fields with clear error messages (linked via `aria-describedby`). Wrap both error message containers and dynamic result displays in `aria-live="polite"` so screen readers announce changes gracefully without interrupting the user. To prevent layout jank, use `min-h-[size]` on error containers.
