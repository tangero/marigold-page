---
slug: "sar"
url: "/mobilnisite/slovnik/sar/"
type: "slovnik"
title: "SAR – Security Assurance Requirements"
date: 2025-01-01
abbr: "SAR"
fullName: "Security Assurance Requirements"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sar/"
summary: "Rámec povinných bezpečnostních požadavků a testovacích specifikací pro produkty a funkce sítí 3GPP. Zajišťuje, že implementace zařízení a softwaru splňují základní úrovně zabezpečení pro ochranu před"
---

SAR je rámec povinných bezpečnostních požadavků a testovacích specifikací, který zajišťuje, aby produkty sítí 3GPP splňovaly základní úrovně zabezpečení pro certifikaci.

## Popis

Požadavky na bezpečnostní záruky (Security Assurance Requirements, SAR) představují komplexní a strukturovanou sadu bezpečnostních specifikací definovaných 3GPP. Jsou navrženy tak, aby poskytovaly standardizovanou metodologii pro hodnocení odolnosti síťových prvků z hlediska zabezpečení, včetně uživatelských zařízení (UE), uzlů rádiového přístupu a funkcí jádra sítě. Rámec funguje tak, že definuje konkrétní bezpečnostní cíle, úrovně záruk a podrobné testovací postupy (známé jako specifikace bezpečnostních záruk, [SCAS](/mobilnisite/slovnik/scas/)) pro různé typy produktů. Tyto požadavky nejsou volitelné; jsou povinné pro soulad a certifikaci v rámci schémat, jako je [GSMA](/mobilnisite/slovnik/gsma/)'s Network Equipment Security Assurance Scheme ([NESAS](/mobilnisite/slovnik/nesas/)). Proces zahrnuje nezávislá bezpečnostní hodnocení, při nichž jsou produkty testovány vůči svým definovaným SAR, aby se ověřilo, že jsou odolné vůči široké škále hrozeb, jako jsou logické útoky, zneužití protokolů nebo fyzické narušení.

Architektura SAR je modulární, přičemž požadavky jsou kategorizovány podle síťové domény (např. 5G Core, NG-RAN, UE) a podle bezpečnostní funkčnosti (např. autentizace, zabezpečený start, kryptografické algoritmy). Každá sada požadavků je dokumentována ve vyhrazené řadě specifikací. Například TS 33.805 specifikuje metodologii bezpečnostních záruk, zatímco další specifikace podrobně popisují požadavky na konkrétní síťové funkce, jako je [AMF](/mobilnisite/slovnik/amf/) nebo [UPF](/mobilnisite/slovnik/upf/). Rámec definuje, jak jsou funkční bezpečnostní požadavky (co produkt musí dělat) propojeny s požadavky na bezpečnostní záruky (jak jsme přesvědčeni, že to dělá správně a robustně). To je často sladěno s koncepty Common Criteria, včetně úrovní záruk hodnocení (EAL).

Role SAR je nedílnou součástí celého bezpečnostního životního cyklu 3GPP. Přesouvá zabezpečení z čistě fáze návrhu do ověřitelného a testovatelného atributu nasazených produktů. Poskytnutím společné základní úrovně zabraňuje dodavatelům implementovat slabá bezpečnostní opatření za účelem snížení nákladů nebo složitosti. Také pomáhá operátorům při zadávání zakázek tím, že jim dává jistotu, že certifikované produkty prošly důkladným, standardizovaným bezpečnostním testováním. Požadavky se vyvíjejí, aby řešily nové hrozby, jako jsou ty, které přináší virtualizace sítí, cloudová nasazení a rizika dodavatelského řetězce, čímž zajišťují, že bezpečnostní záruky drží krok s technologickým pokrokem v mobilních sítích.

## K čemu slouží

SAR byl vytvořen, aby řešil kritickou potřebu standardizovaného, nezávislého ověřování zabezpečení telekomunikačních zařízení. Před jeho vývojem bylo zajišťování bezpečnostních záruk často ad-hoc, specifické pro dodavatele nebo založené na netelekomunikačních standardech, což vedlo k nekonzistentní úrovni zabezpečení v síti a potenciálním slabým místům, která by mohla být zneužita. Rostoucí složitost mobilních sítí, přechod na protokoly založené na IP a rostoucí hodnota přenášených dat učinily nezbytným stanovit jednotnou, vysokou laťku pro zabezpečení.

Primární problém, který SAR řeší, je nedostatek důvěry a transparentnosti v zabezpečení síťových produktů. Poskytuje společný jazyk a soubor měřitelných kritérií pro zabezpečení, což umožňuje spravedlivé srovnání mezi dodavateli a dává síťovým operátorům spolehlivý mechanismus pro posouzení rizika. To je zvláště klíčové v prostředích s více dodavateli, kde jedna nezabezpečená komponenta může ohrozit celý systém. SAR také řeší regulační a národní bezpečnostní obavy tím, že poskytuje rámec pro certifikaci, že zařízení splňuje požadované úrovně zabezpečení, což je zásadní pro kritickou infrastrukturu.

Historicky byl jeho vývoj motivován spoluprací mezi 3GPP a [GSMA](/mobilnisite/slovnik/gsma/), které uznaly, že zabezpečení nemůže být pouze záležitostí návrhu protokolu, ale vyžaduje důkladné testování implementace. Formalizuje koncept 'zabezpečení již při návrhu' do 'zabezpečení ověřením', čímž zajišťuje, že robustní bezpečnostní mechanismy definované ve specifikacích 3GPP (jako je autentizace a šifrování) jsou správně a odolně implementovány v reálných produktech, a tím uzavírá mezeru mezi specifikací a nasazením.

## Klíčové vlastnosti

- Standardizovaná testovací metodologie pro zabezpečení síťových produktů
- Povinné požadavky pro soulad a certifikaci (např. NESAS)
- Specifikace bezpečnostních záruk pro konkrétní produkty (SCAS)
- Soulad s úrovněmi záruk hodnocení Common Criteria (EAL)
- Pokrytí napříč všemi síťovými doménami: UE, RAN a Core
- Vývoj pro řešení cloudových a virtualizovaných síťových funkcí

## Související pojmy

- [NESAS – Network Equipment Security Assurance Scheme](/mobilnisite/slovnik/nesas/)
- [SCAS – 3GPP Security Assurance Specification](/mobilnisite/slovnik/scas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [SAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sar/)
