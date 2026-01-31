# Visão geral do mapeamento de campos ZUGFeRD

## Introdução

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) é um padrão alemão de faturação eletrónica baseado no UN/CEFACT Cross Industry Invoice (CII) e no padrão ISO 19005-3 (PDF/A-3). Permite a troca de dados de fatura estruturados num arquivo PDF.

O DocBits extrai campos de documentos ZUGFeRD e alinha-os com os sistemas ERP da Infor (M3, LN) utilizando os padrões OAGIS BOD.

## Versões ZUGFeRD suportadas

O DocBits suporta várias versões do padrão ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Fluxo de dados

O fluxo de dados de um documento ZUGFeRD para o seu sistema ERP segue estas etapas:

1. **Extração**: O DocBits analisa os dados XML incorporados no PDF com base na versão ZUGFeRD.
2. **Mapeamento de campos do DocBits**: Os dados extraídos são mapeados para os campos padrão do DocBits.
3. **Alinhamento do ERP**: Os campos do DocBits são mapeados para os campos Infor BOD (Business Object Document) ou para os campos de API específicos do M3/LN.
4. **Exportação**: Os dados mapeados são exportados para o sistema Infor.

## Padrões de mapeamento

O mapeamento baseia-se nos seguintes padrões:
* **UN/CEFACT CII**: A base para a estrutura XML ZUGFeRD.
* **OAGIS/OASIS**: O padrão para os BODs da Infor.
* **EN 16931**: O padrão europeu para faturação eletrónica com o qual o ZUGFeRD 2.x é compatível.
