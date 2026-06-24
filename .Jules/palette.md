
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Missing Inline Validation and ARIA Live Regions
**Learning:** Dynamic calculators in the project (like the MEI tax calculator in 'solucao') lacked inline validation feedback for empty submissions and did not announce result updates to screen readers, causing a confusing experience for assistive technologies.
**Action:** Always provide inline validation feedback linked via `aria-describedby` when validating dynamic inputs. Wrap error messages and dynamic result containers in `aria-live="polite"` so screen readers announce state changes smoothly without interrupting the user. Ensure error containers have a minimum height (e.g., `min-h-[16px]`) to prevent layout jank.

## 2024-05-17 - Missing Keyboard Focus Visible Styles
**Learning:** Custom UI components across the project lacked explicit `*:focus-visible` styles, relying only on default or general `:focus` styles. This disrupts keyboard navigation accessibility, making it hard for keyboard-only users to see which element is active without affecting mouse/touch users.
**Action:** Always ensure explicit `*:focus-visible` styles are defined in root CSS files using appropriate contrast colors (e.g., `--accent-clay` for light themes and `white` for dark themes).
