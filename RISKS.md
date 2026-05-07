# RISKS: Local Business Impact v2 (Hub)

- **Manutenibilidade:** Com 10 empresas, qualquer mudança estrutural no Hub exige atualização manual múltipla.
- **SEO:** O hub central é excelente para o projeto, mas cada landing page individual precisa de metadados específicos para ranquear localmente no Google.
- **Integração Google Docs (Henry):** Como optamos por criar as copys no `OUTREACH_REPORT.md` local, há a fricção manual necessária de copiar/colar para o GDocs do usuário. Um sistema automatizado de injeção direta via API exigiria validação OAuth explícita.
- **Dependência Externa Frágil (Tailwind CDN):** O uso de CDN injetado diretamente no head provou ser um risco de nível crítico. Quando a tag ou o script falham por atualizações no lado do servidor, os 10 sites perdem a formatação completamente e de forma simultânea.