---
slug: "nsap"
url: "/mobilnisite/slovnik/nsap/"
type: "slovnik"
title: "NSAP – Network Service Access Point"
date: 2025-01-01
abbr: "NSAP"
fullName: "Network Service Access Point"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nsap/"
summary: "Konceptuální bod v architektuře síťové vrstvy, kde jsou poskytovány služby vrstvě nadřazené. Definuje rozhraní pro přenos dat a řízení mezi síťovou vrstvou a transportní vrstvou v protokolovém zásobní"
---

NSAP je konceptuální bod v architektuře síťové vrstvy 3GPP, který poskytuje rozhraní pro přenos dat a řídicí služby transportní vrstvě nad ním.

## Popis

Network Service Access Point (NSAP) je základní koncept v protokolové architektuře 3GPP, konkrétně v rámci řídicí roviny. Představuje logický rozhraní na horní hranici síťové vrstvy (vrstva 3). V tomto bodě síťová vrstva poskytuje své služby – především správu spojení a přenos dat – transportní vrstvě nebo aplikacím vyšších vrstev. NSAP není fyzická entita, ale definovaný přístupový bod služeb, který umožňuje nadřazené vrstvě vyžádat síťové služby pomocí sady primitiv. Tato primitiva typicky zahrnují požadavky, indikace, odpovědi a potvrzení, které usnadňují procedury jako je zřizování, udržování a rušení kontextů [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) v systémech [GPRS](/mobilnisite/slovnik/gprs/) a UMTS.

Prakticky je NSAP klíčový pro interakci mezi podsložkou správy relace ([SM](/mobilnisite/slovnik/sm/)) a podsložkou správy mobility GPRS ([GMM](/mobilnisite/slovnik/gmm/)), nebo mezi SM a vlastními uživatelskými aplikacemi. Například když mobilní stanice iniciuje datovou relaci, aplikace vyžádá síťovou službu prostřednictvím NSAP. To spustí síťovou vrstvu k provedení potřebné signalizace se sítí za účelem aktivace kontextu PDP, který přidělí IP adresu a nastaví datovou cestu. NSAP zajišťuje, že tato interakce následuje standardizovaný model, což umožňuje různým implementacím bezproblémově spolupracovat.

Architektura zahrnuje více NSAP pro současnou podporu různých služeb nebo profilů kvality služeb (QoS). Každý NSAP je asociován s konkrétním identifikátorem přístupového bodu služeb síťové vrstvy ([NSAPI](/mobilnisite/slovnik/nsapi/)), který jednoznačně identifikuje přístupový bod služeb v rámci mobilní stanice a sítě. To umožňuje nezávislou správu více kontextů PDP (např. pro přístup k internetu a služby IMS) přes stejné fyzické spojení. Koncept NSAP je definován v různých specifikacích 3GPP, které detailně popisují servisní primitiva a stavy přístupového bodu služeb, a tvoří tak jádro vrstvového protokolového návrhu, který umožňuje spolehlivou a efektivní mobilní datovou komunikaci.

## K čemu slouží

NSAP byl zaveden, aby poskytl standardizované, abstraktní rozhraní pro služby síťové vrstvy v systémech mobilní telekomunikace, počínaje [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Před jeho definicí byla interakce mezi protokolovými vrstvami často specifická pro implementaci, což vedlo k problémům s interoperabilitou a složitou integrací. NSAP vytváří jasné oddělení odpovědností, což umožňuje transportní vrstvě a aplikacím vyžadovat služby přenosu dat bez nutnosti porozumět podkladovým detailům síťové signalizace. Tato abstrakce je nezbytná pro podporu více souběžných datových relací a různorodých aplikací na jediném zařízení.

Jeho vytvoření bylo motivováno potřebou strukturované protokolové architektury, která by mohla podporovat paketově přepínané datové služby vedle tradičních okruhově přepínaných hlasových služeb. NSAP umožňuje síťové vrstvě nabízet služby jako zřizování spojení, přenos dat a uvolnění spojení konzistentním způsobem. Definováním přesných servisních primitiv a stavů zajišťuje, že různé síťové prvky (např. UE, [SGSN](/mobilnisite/slovnik/sgsn/), GGSN) mohou efektivně komunikovat, což usnadňuje vývoj od 2G přes 3G a dále. NSAP řeší omezení ad-hoc interakcí mezi vrstvami a poskytuje model, který škáluje s rostoucí složitostí služeb a požadavky na QoS.

## Klíčové vlastnosti

- Definuje servisní rozhraní mezi síťovou vrstvou a transportní vrstvou/aplikacemi
- Pro řízení využívá standardizovaná servisní primitiva (request, indication, response, confirm)
- Podporuje více souběžných instancí pro různé služby prostřednictvím jedinečného mapování NSAPI
- Umožňuje aktivaci, modifikaci a deaktivaci kontextů PDP
- Umožňuje nezávislou správu QoS na přístupový bod služeb
- Poskytuje stavový model pro správu podmínek přístupového bodu služeb

## Související pojmy

- [NSAPI – Network layer Service Access Point Identifier](/mobilnisite/slovnik/nsapi/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [NSAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsap/)
