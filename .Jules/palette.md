
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Missing Inline Validation and ARIA Live Regions
**Learning:** Dynamic calculators in the project (like the MEI tax calculator in 'solucao') lacked inline validation feedback for empty submissions and did not announce result updates to screen readers, causing a confusing experience for assistive technologies.
**Action:** Always provide inline validation feedback linked via `aria-describedby` when validating dynamic inputs. Wrap error messages and dynamic result containers in `aria-live="polite"` so screen readers announce state changes smoothly without interrupting the user. Ensure error containers have a minimum height (e.g., `min-h-[16px]`) to prevent layout jank.

## 2024-06-20 - Missing Focus-Visible Styles
**Learning:** Custom interactive components (like buttons and inputs) in the various design systems ('The Void Principle' and 'Golden Mold') lacked explicit `:focus-visible` styles. This meant keyboard users had no visual indicator of which element was focused, making keyboard navigation difficult or impossible, while using just `:focus` would negatively impact mouse users with unwanted outlines.
**Action:** Always ensure explicit `*:focus-visible` styles are defined in the root CSS files (`void-styles.css`, `proposta-styles.css`, `gold-mold/css/styles.css`). Use high-contrast colors appropriate for the theme (e.g., `white` for dark themes, `--accent-clay` for light themes) with a 2px solid outline and a 2px outline-offset to ensure the focus ring is clearly visible and detached from the element's border.
