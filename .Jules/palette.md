## 2026-05-18 - Form Accessibility Improvements
**Learning:** Across multiple site templates, form inputs for numerical simulators lacked explicit `<label for="...">` associations, which impairs screen reader navigation and tap target usability.
**Action:** Added proper `for` attributes to all labels pointing to their respective input `id`s, improving keyboard and assistive technology accessibility.
