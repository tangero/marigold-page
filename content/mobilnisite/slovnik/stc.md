---
slug: "stc"
url: "/mobilnisite/slovnik/stc/"
type: "slovnik"
title: "STC – Signalling Transport Converter"
date: 2025-01-01
abbr: "STC"
fullName: "Signalling Transport Converter"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/stc/"
summary: "STC je síťový prvek, který převádí signalizační protokoly mezi různými transportními vrstvami, například mezi signalizací založenou na SS7 a IP transportem. Umožňuje spolupráci v jádrech sítí a zajišť"
---

STC je síťový prvek, který převádí signalizační protokoly mezi různými transportními vrstvami, například mezi SS7 a IP, aby umožnil spolupráci mezi staršími a moderními systémy jádra sítě.

## Popis

Signalling Transport Converter (STC) je funkční entita definovaná ve specifikacích 3GPP, která adaptuje signalizační zprávy mezi různými transportními technologiemi, především během přechodu od přepojování okruhů k přepojování paketů. Funguje na transportní vrstvě a převádí protokoly jako Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)) používaný v tradiční signalizaci [SS7](/mobilnisite/slovnik/ss7/) na Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)) nebo jiný IP transport. STC přijímá signalizační jednotky z jedné síťové domény, extrahuje datovou část a zabalí ji do formátu vyžadovaného cílovou doménou, přičemž zajišťuje integritu zpráv a zachování jejich pořadí. Může také řešit překlad adres a úpravy směrování pro sladění s různými síťovými adresními schématy.

Architektonicky je STC často nasazen jako samostatný uzel nebo integrovaný do signalizačních bran v jádru sítě. Mezi klíčové komponenty patří zásobníky protokolů pro zdrojový i cílový transport, logika převodu a rozhraní pro správu pro konfiguraci a monitorování. Ve vydáních 3GPP je specifikován v dokumentech jako 25.420 a 25.424, které detailně popisují jeho roli v rozhraních jako Iu-CS (propojující [RNC](/mobilnisite/slovnik/rnc/) s [MSC](/mobilnisite/slovnik/msc/)) nebo při spolupráci s externími sítěmi. STC funguje transparentně pro signalizační aplikace vyšších vrstev, jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)), což jim umožňuje pracovat beze změn přes nové transportní sítě.

Role STC je klíčová pro vývoj sítě, neboť umožňuje operátorům modernizovat svou infrastrukturu při zachování kompatibility se staršími systémy. Snižuje náklady a složitost migrace tím, že se vyhne okamžité výměně všech síťových prvků. Tím, že umožňuje hladkou spolupráci, zajišťuje nepřetržitou dostupnost služeb pro hlasové a signalizační služby během přechodů. Jeho důležitost spočívá v podpoře hybridních síťových prostředí, kde koexistuje tradiční signalizace založená na TDM i moderní signalizace založená na IP, čímž se prodlužuje životnost stávajících investic.

## K čemu slouží

STC byl vyvinut pro řešení výzev spojených s migrací telekomunikačních sítí ze starší signalizace založené na SS7/TDM na IP transportní systémy, jako jsou ty používané ve 3G a novějších generacích. Řeší problém nekompatibility protokolů mezi starými a novými síťovými segmenty, která by jinak mohla narušit kritickou signalizaci pro řízení hovorů, správu mobility a doplňkové služby. Motivací byla potřeba postupných síťových upgradů, které operátorům umožňují zavádět IP transport postupně bez nutnosti okamžité výměny veškeré infrastruktury (tzv. 'big bang').

Historicky, před existencí STC, vyžadovala spolupráce složité brány nebo implementace s dvojím zásobníkem, které byly nákladné a neefektivní. 3GPP standardizovalo STC počínaje R99, aby poskytlo jednotný mechanismus převodu a řešilo tak omezení proprietárních řešení. Umožnilo bezproblémové propojení mezi doménami s přepojováním okruhů (např. 2G/3G MSC) a jádry s přepojováním paketů (např. v UMTS nebo LTE), podporující služby jako hlas přes IP přenosovou síť. To usnadnilo vývoj směrem k plně IP sítím, snížilo provozní náklady a zlepšilo škálovatelnost při zachování interoperability se stávajícími globálními signalizačními sítěmi.

## Klíčové vlastnosti

- Převod protokolů mezi SS7/MTP a IP transporty jako SCTP
- Transparentní provoz pro signalizační aplikace vyšších vrstev
- Podpora signalizačních rozhraní jako Iu-CS v UMTS
- Překlad adres a adaptace směrování mezi doménami
- Zajišťuje integritu pořadí zpráv během převodu
- Umožňuje postupnou migraci sítě z TDM na IP

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling

---

📖 **Anglický originál a plná specifikace:** [STC na 3GPP Explorer](https://3gpp-explorer.com/glossary/stc/)
