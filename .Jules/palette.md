## 2024-05-24 - Form Input Label Association
**Learning:** Many interactive inputs across the multi-page project were missing explicit label associations (missing `for` attributes) or completely lacked labels, which negatively affects screen readers and prevents users from clicking labels to focus inputs.
**Action:** Always ensure that every `<input>` has an explicitly associated `<label>` using the `for` attribute matching the input's `id`. For inputs without a visible label, use `aria-label` to maintain accessibility context.
