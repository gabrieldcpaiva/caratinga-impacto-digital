# Projeto: Caratinga Impacto Digital (System Pilot)

## 1. Project Constitution (Law)
- **Protocol:** B.L.A.S.T. (Blueprint, Link, Architect, Stylize, Trigger).
- **Architecture:** A.N.T. 3-Layer (Architecture, Navigation, Tools).
- **Language:** Technical (EN), User-facing/Copy (PT-BR).
- **Aesthetic:** Minimalist Luxury / Cinematic.

## 2. Behavioral Rules
- Zero Friction: Gabriel is the Approver. Henry is the Executor.
- Deterministic Logic: No guessing on business rules.
- Local First: All operations in `.tmp/` before deployment.
- No Apologies: Correct and execute.

## 3. Data Schema (The Payload)
### 3.1 Input Schema (Leads)
```json
{
  "business_name": "string",
  "phone": "string",
  "whatsapp": "string",
  "email": "string",
  "location": "string",
  "instagram": "string",
  "category": "string"
}
```

### 3.2 Output Schema (Outreach Payload)
```json
{
  "business_id": "string",
  "recipient_name": "string",
  "message_body": "string",
  "link_url": "string",
  "status": "pending | sent | failed",
  "timestamp": "iso-date"
}
```

## 4. Architectural Invariants
- **Layer 1 (Architecture):** SOPs in `architecture/`. Mandatory before coding.
- **Layer 2 (Navigation):** Agent-led reasoning and tool orchestration.
- **Layer 3 (Tools):** Atomic Python scripts in `tools/`. No side effects outside `.tmp/` or target APIs.
