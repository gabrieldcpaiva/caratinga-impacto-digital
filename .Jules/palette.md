## 2024-05-24 - Persistent Labels over Placeholders
**Learning:** Using placeholders as the only label for input fields is bad for accessibility and cognitive load since the label disappears when typing. Persistent `<label>` elements associated via the `for` attribute are essential.
**Action:** Always add persistent explicit `<label>` tags linked to input fields (`for="inputId"`) instead of relying solely on placeholders.
