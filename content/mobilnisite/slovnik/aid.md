---
slug: "aid"
url: "/mobilnisite/slovnik/aid/"
type: "slovnik"
title: "AID – Application Identifier"
date: 2025-01-01
abbr: "AID"
fullName: "Application Identifier"
category: "Identifier"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/aid/"
summary: "AID je standardizovaný identifikátor používaný na kartách UICC/SIM k jednoznačné identifikaci aplikací, zejména pro USIM a další telekomunikační služby. Umožňuje koexistenci více aplikací na jedné čip"
---

AID (Application Identifier) je standardizovaný kód sloužící k jednoznačné identifikaci a správě konkrétních aplikací, jako je USIM, na kartě UICC/SIM, což umožňuje koexistenci více bezpečnostních aplikací.

## Popis

Application Identifier (AID) je základní součástí ekosystému karet UICC (Universal Integrated Circuit Card) a [SIM](/mobilnisite/slovnik/sim/), definovaná normou [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-4 a přijatá 3GPP pro telekomunikační aplikace. AID se skládá ze dvou částí: Registered Application Provider Identifier ([RID](/mobilnisite/slovnik/rid/)) a Proprietary Application Identifier Extension (PIX). RID je 5bajtová hodnota přidělená organizací ISO k identifikaci poskytovatele aplikace, zatímco PIX (až 11 bajtů) definuje poskytovatel pro identifikaci konkrétních aplikací. Tato hierarchická struktura zajišťuje globální jedinečnost a zároveň poskytovatelům poskytuje flexibilitu v organizaci jejich aplikací.

V systémech 3GPP se AID primárně používá k identifikaci aplikace [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) na kartách UICC. Standardní AID pro USIM je definován jako 'A0000000871002FF...', kde 'A000000087' identifikuje telekomunikační průmysl, '10' označuje rodinu aplikací (aplikace GSM/UMTS) a následující bajty specifikují aplikaci USIM. Když mobilní zařízení inicializuje komunikaci s kartou UICC, odešle příkaz SELECT s AID k aktivaci konkrétní aplikace. UICC odpoví schopnostmi aplikace a dostupnými soubory.

Mechanismus AID umožňuje koexistenci více aplikací na jedné kartě UICC, včetně USIM, [ISIM](/mobilnisite/slovnik/isim/) (pro IMS) a různých přidaných služeb. Každá aplikace udržuje vlastní souborový systém a bezpečnostní doménu, izolovanou od ostatních. Během personalizace karty se AID používá k vytvoření vyhrazené souborové struktury aplikace. Během provozu terminál používá AID k navigaci mezi aplikacemi, přičemž právě vybrané AID určuje, ke kterým souborům a příkazům aplikace má přístup. Tato architektura podporuje víceaplikční schopnost, která je klíčová pro moderní karty UICC.

Kromě základní identifikace hrají AID klíčovou roli v zabezpečení a správě aplikací. Umožňují navázání zabezpečeného kanálu mezi terminálem a konkrétními aplikacemi, přičemž kryptografické klíče a bezpečnostní politiky jsou asociovány s každým AID. Při vzdálené správě aplikací ([OTA](/mobilnisite/slovnik/ota/)) se AID používají k cílení aktualizací na konkrétní aplikace, což operátorům umožňuje upravovat nebo přidávat služby bez fyzické výměny karty. Standardizovaná struktura AID zajišťuje interoperabilitu mezi různými výrobci karet, mobilními zařízeními a síťovými operátory po celém světě.

## K čemu slouží

AID byl vytvořen k řešení základního problému identifikace a výběru aplikací ve víceaplikčních čipových kartách, což se stalo nezbytným s vývojem karet UICC/[SIM](/mobilnisite/slovnik/sim/) z jednoduchých autentizačních modulů na platformy hostující více služeb. Před standardizovanými AID byl výběr aplikací proprietární a nekonzistentní, což ztěžovalo interoperabilitu mezi různými výrobci karet a mobilními zařízeními. Norma ISO/IEC 7816-4, přijatá 3GPP, poskytla univerzální adresovací schéma, které umožnilo koexistenci telekomunikačních aplikací spolu s dalšími službami na jedné kartě.

S vývojem mobilních sítí od GSM přes UMTS po LTE výrazně vzrostla potřeba více aplikací na kartách UICC. Aplikace USIM pro 3G/4G autentizaci, ISIM pro služby IMS a různé přidané aplikace všechny potřebovaly sídlit na stejné fyzické kartě. Systém AID poskytl standardizovaný způsob, jak tyto aplikace identifikovat, vybírat a spravovat bez konfliktů. To bylo obzvláště důležité pro globální roaming, kdy musí UICC účastníka fungovat s vybavením různých síťových operátorů po celém světě.

Hierarchická struktura AID (RID + PIX) řešila jak požadavky na globální jedinečnost, tak potřeby flexibility poskytovatelů. Správou přidělování RID organizací ISO se předešlo konfliktům mezi různými poskytovateli aplikací. Mezitím PIX umožnil poskytovatelům organizovat jejich vlastní rodiny aplikací a verze. Tento vyvážený přístup umožnil explozivní růst služeb založených na UICC při zachování zpětné kompatibility se stávajícími systémy a zajištění budoucí rozšiřitelnosti pro nové aplikace.

## Klíčové vlastnosti

- Hierarchická struktura s komponentami RID a PIX
- Globálně jedinečná identifikace aplikace
- Umožňuje koexistenci více aplikací na UICC
- Standardizovaný mechanismus výběru aplikace
- Podporuje vzdálenou správu aplikací (OTA)
- Zajišťuje interoperabilitu mezi různými dodavateli a operátory

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [ISIM – IMS Subscriber Identity Module](/mobilnisite/slovnik/isim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application
- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TR 31.822** (Rel-18) — Technical Report on GBA_U based APIs
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [AID na 3GPP Explorer](https://3gpp-explorer.com/glossary/aid/)
