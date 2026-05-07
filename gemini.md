# Projeto: Caratinga Impacto Digital
## 1. Regras Comportamentais (Behavioral Rules)
- A.N.T. 3-layer architecture e framework B.L.A.S.T. são obrigatórios.
- Todo o código, relatórios e textos voltados ao usuário devem estar em PT-BR nativo.
- Estética exigida: "Minimalist Luxury".

## 2. Invariantes Arquiteturais
- **Layer 1 (Architecture):** SOPs em markdown no diretório `architecture/`.
- **Layer 2 (Navigation):** Roteamento lógico executado pelo Agente.
- **Layer 3 (Tools):** Scripts determinísticos (`tools/`).
- Operações intermediárias e testes locais no diretório `.tmp/`.

## 3. Data Schema (Payloads)
### 3.1 Input Schema (Dados Brutos dos Negócios)
```json
{
  "business_name": "string",
  "phone": "string",
  "whatsapp": "string",
  "email": "string",
  "location": "string",
  "instagram": "string"
}
```

### 3.2 Output Schema (Payload de Contato)
```json
{
  "business_name": "string",
  "outreach_message": "string",
  "gmb_proposal": "string",
  "landing_page_url": "string"
}
```
