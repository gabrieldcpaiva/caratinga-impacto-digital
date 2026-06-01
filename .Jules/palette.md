
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
## 2024-11-20 - [ARIA Live for Dynamic Calculators]
**Learning:** Adding validation to a calculator that relies on JS manipulation requires both error containers and result containers to use `aria-live="polite"` so screen readers are informed of state changes dynamically, rather than just visually appearing. Preventing layout shift (jank) with a fixed height container is equally crucial.
**Action:** When creating inline validation or dynamic feedback, always pair `aria-describedby` with `aria-live="polite"` and a fixed min-height for error text containers.
