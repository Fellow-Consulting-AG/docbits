# Aperçu du mappage des champs ZUGFeRD

## Introduction

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) est un standard allemand de facturation électronique basé sur le UN/CEFACT Cross Industry Invoice (CII) et la norme ISO 19005-3 (PDF/A-3). Il permet l'échange de données de facture structurées dans un fichier PDF.

DocBits extrait les champs des documents ZUGFeRD et les aligne avec les systèmes ERP Infor (M3, LN) en utilisant les standards OAGIS BOD.

## Versions ZUGFeRD supportées

DocBits supporte plusieurs versions du standard ZUGFeRD :

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Flux de données

Le flux de données d'un document ZUGFeRD vers votre système ERP suit ces étapes :

1. **Extraction** : DocBits analyse les données XML intégrées du PDF en fonction de la version ZUGFeRD.
2. **Mappage des champs DocBits** : Les données extraites sont mappées vers les champs DocBits standards.
3. **Alignement ERP** : Les champs DocBits sont mappés vers les champs Infor BOD (Business Object Document) ou les champs API spécifiques à M3/LN.
4. **Export** : Les données mappées sont exportées vers le système Infor.

## Standards de mappage

Le mappage est basé sur les standards suivants :
* **UN/CEFACT CII** : La base de la structure XML ZUGFeRD.
* **OAGIS/OASIS** : Le standard pour les BOD Infor.
* **EN 16931** : La norme européenne pour la facturation électronique à laquelle ZUGFeRD 2.x est conforme.
