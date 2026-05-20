## 2024-05-24 - Explicit Label Associations
**Learning:** Found a systemic accessibility issue where `<label>` elements were used for styling but lacked the `for` attribute to programmatically associate them with their inputs. Also found inputs lacking labels entirely, relying on placeholder text.
**Action:** Always ensure `<label>` elements have a `for` attribute matching the input's `id`. For inputs where a visible label disrupts the design, add a visually hidden label (e.g., using Tailwind's `sr-only` class) to maintain screen reader accessibility.
