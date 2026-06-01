
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.

## 2024-05-16 - Dynamic Form Inline Validation and Announcements
**Learning:** In interactive widgets (like the MEI calculator), simply un-hiding error messages or dynamic results causes layout shifts (jank) and can fail to alert screen reader users who expect feedback after taking action.
**Action:** Always provide inline validation feedback using an element linked to the input via `aria-describedby`. Wrap both error messages and dynamic result containers with `aria-live="polite"` so state changes are announced seamlessly. To prevent layout jank, give error containers a minimum height (e.g., `min-h-[16px]`).
