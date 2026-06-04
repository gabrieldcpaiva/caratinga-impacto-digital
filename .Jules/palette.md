
## 2024-05-15 - Missing Label Form Associations
**Learning:** Across the various landing pages in this repository, form inputs (such as the calculator inputs for 'ticket' or 'revenue') consistently lacked proper `for` attributes on their labels, which breaks screen reader accessibility by preventing the association between the label and the input field. Additionally, some inputs had no label at all.
**Action:** Always verify that `<label>` elements have a `for` attribute that strictly matches the `id` of their corresponding `<input>`. If a visible label disrupts the design, use a visually hidden (screen-reader only) label (e.g., `class="sr-only"`) to ensure accessibility is not compromised.
## 2024-05-16 - Prevent layout shift on error injection
**Learning:** Adding dynamic error text beneath inputs often causes layout jank by shifting elements down. In the MEI calculator in Solução Contabilidade, missing error states led to a silent failure.
**Action:** Implemented inline error spans with a minimum height (`min-h-[16px]`) to reserve space and prevent layout shifts. Linked errors with `aria-describedby` and used `aria-live="polite"` for dynamic result and error announcements.
