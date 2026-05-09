# Caratinga Impacto Digital Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Replicate the "Golden Mold" (minimalist luxury landing page + proposal) for 10 local businesses in Caratinga, replacing the current "messy" dark theme with a premium light/cream aesthetic.

**Architecture:** 
- Centralized CSS: All sites link to `../gold-mold/css/styles.css`.
- Localized HTML: Each folder (`metta`, `blocomais`, etc.) gets a personalized `index.html` and `proposta.html`.
- Dynamic Calculators: Each `index.html` includes a "Lost Demand" calculator with industry-specific default tickets.

**Tech Stack:** Vanilla HTML5, CSS3 (Organic Tech Preset), Minimal JS.

---

### Task 1: Global Asset Audit
**Files:**
- Modify: `gold-mold/css/styles.css` (Ensure absolute robustness)

**Step 1: Verify CSS stability**
Ensure no hardcoded absolute paths that might break on GitHub Pages.

### Task 2: Replicate for Metta Engenharia
**Files:**
- Modify: `metta/index.html`
- Modify: `metta/proposta.html`

**Step 1: Replace index.html**
Apply the Golden Mold structure. Headline: "Precisão que constrói sua <span class='italic-garamond'>autoridade.</span>". Ticket: 5000.
**Step 2: Replace proposta.html**
Personalize with Metta's problem (gap in technical authority).

### Task 3: Replicate for Bloco Mais Materiais
**Files:**
- Modify: `blocomais/index.html`
- Modify: `blocomais/proposta.html`

**Step 1: Replace index.html**
Headline: "O alicerce digital para quem <span class='italic-garamond'>constrói Caratinga.</span>". Ticket: 1500.
**Step 2: Replace proposta.html**
Personalize with Bloco Mais's problem (logistics vs. convenience gap).

### Task 4: Replicate for Frederico Auto Mecânica
**Files:**
- Modify: `frederico/index.html`
- Modify: `frederico/proposta.html`

**Step 1: Replace index.html**
Headline: "Confiança que se vende antes de <span class='italic-garamond'>abrir o capô.</span>". Ticket: 800.
**Step 2: Replace proposta.html**
Personalize with Frederico's problem (trust gap in emergency searches).

### Task 5: Replicate for Estacionamento Caratinga
**Files:**
- Modify: `estacionamento-caratinga/index.html`
- Modify: `estacionamento-caratinga/proposta.html`

**Step 1: Replace index.html**
Headline: "Segurança e localização no <span class='italic-garamond'>coração da cidade.</span>". Ticket: 300.
**Step 2: Replace proposta.html**
Personalize with Estacionamento's problem (visibility for transients).

### Task 6: Replicate for Vidraçaria Caratinga
**Files:**
- Modify: `vidracaria-caratinga/index.html`
- Modify: `vidracaria-caratinga/proposta.html`

**Step 1: Replace index.html**
Headline: "A grife do design em vidro em <span class='italic-garamond'>Caratinga.</span>". Ticket: 2000.
**Step 2: Replace proposta.html**
Personalize with Vidraçaria's problem (commodity vs. luxury gap).

### Task 7: Replicate for Claudio Sapateiro
**Files:**
- Modify: `claudio-sapateiro/index.html`
- Modify: `claudio-sapateiro/proposta.html`

**Step 1: Replace index.html**
Headline: "A arte do mestre artesão agora <span class='italic-garamond'>na palma da mão.</span>". Ticket: 150.
**Step 2: Replace proposta.html**
Personalize with Claudio's problem (tradition vs. findability gap).

### Task 8: Replicate for Vidraçaria Sousa
**Files:**
- Modify: `vidracaria-sousa/index.html`
- Modify: `vidracaria-sousa/proposta.html`

**Step 1: Replace index.html**
Headline: "Agilidade e precisão para sua <span class='italic-garamond'>obra não parar.</span>". Ticket: 1800.
**Step 2: Replace proposta.html**
Personalize with Sousa's problem (response time gap).

### Task 9: Replicate for Só Vidros
**Files:**
- Modify: `so-vidros/index.html`
- Modify: `so-vidros/proposta.html`

**Step 1: Replace index.html**
Headline: "Onde a tecnologia encontra a <span class='italic-garamond'>transparência.</span>". Ticket: 2200.
**Step 2: Replace proposta.html**
Personalize with Só Vidros's problem (avenue dominance gap).

### Task 10: Replicate for Limpeza Pro
**Files:**
- Modify: `limpeza-pro/index.html`
- Modify: `limpeza-pro/proposta.html`

**Step 1: Replace index.html**
Headline: "A ciência da higienização para o <span class='italic-garamond'>seu bem-estar.</span>". Ticket: 400.
**Step 2: Replace proposta.html**
Personalize with Limpeza Pro's problem (social proof gap).

### Task 11: Deployment & Hub Update
**Files:**
- Modify: `index.html` (Main Hub)
- Modify: `DECISIONS.md`

**Step 1: Update Main Hub**
Refactor the root `index.html` to match the Golden Mold aesthetic (Centralized Hub).
**Step 2: Log Completion**
Update `DECISIONS.md` and `STATE.md`.
