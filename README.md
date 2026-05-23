# Experiência Tábua YVORA Global

Aplicativo multilíngue da Experiência Tábua YVORA, com suporte a Português, English e 中文.

## Arquitetura

- O aplicativo lê a mesma base Google Sheets da experiência validada.
- O conteúdo em português usa as colunas originais.
- Inglês utiliza campos com sufixo `_en`.
- Chinês simplificado utiliza campos com sufixo `_zh`.
- A versão portuguesa em produção no repositório original permanece intacta.

## Deploy no Streamlit

Arquivo principal: `app.py`

Configurar nos secrets a conta de serviço Google e, opcionalmente, `SPREADSHEET_ID`. A base padrão já aponta para a planilha da Experiência Tábua YVORA.
