
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2026-06-06 - Calculator Inline Validation & ARIA Live Regions
**Learning:** Dynamic calculators in the project lack inline validation feedback for empty or invalid states, leading to a confusing UX when results aren't generated. Furthermore, dynamic result containers often appear without notifying screen readers.
**Action:** When working on dynamic UI components (like calculators), implement inline validation using `aria-describedby` to link error messages to inputs. Wrap both error messages and result containers with `aria-live="polite"` so screen readers announce state changes smoothly, and ensure error containers have a minimum height (e.g., `min-h-[16px]`) to prevent layout jank.
