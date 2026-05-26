
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-26 - Missing Inline Validation and ARIA Live Regions
**Learning:** The calculator interfaces (e.g., in `solucao/index.html`) lacked inline validation feedback for empty submissions. They also failed to communicate dynamic state changes to screen readers (e.g., displaying the result or an error message) due to the absence of `aria-live` regions and `aria-describedby` associations.
**Action:** When implementing or fixing interactive UI components like calculators, always ensure inputs have an associated error container using `aria-describedby`. Dynamically updated containers (such as error messages or calculation results) must have `aria-live="polite"` so screen readers announce changes. Set a minimum height (e.g., `min-h-[16px]`) on empty error containers to prevent layout shift (jank) when the message appears.
