## 2024-05-15 - Missing form label associations in templates
**Learning:** Landing page templates often use generic inputs (like id="ticket") without explicitly connecting them to their visible labels using the `for` attribute, breaking screen reader navigation. Forms without visible labels (like in the Solução template) are also missing `aria-label` alternatives.
**Action:** Always verify that `<label>` elements have a `for` attribute matching the input ID, and add `aria-label` to standalone inputs without visible labels during template creation or review.
