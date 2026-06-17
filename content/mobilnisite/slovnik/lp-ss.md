---
slug: "lp-ss"
url: "/mobilnisite/slovnik/lp-ss/"
type: "slovnik"
title: "LP-SS – Low Power Synchronization Signal"
date: 2025-01-01
abbr: "LP-SS"
fullName: "Low Power Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lp-ss/"
summary: "Nízkopříkonový synchronizační signál zavedený ve specifikaci 3GPP Release 18 pro NR. Umožňuje energeticky úsporné vyhledávání buněk a počáteční přístup pro zařízení, jako jsou IoT senzory, snížením sp"
---

LP-SS je nízkopříkonový synchronizační signál zavedený ve specifikaci 3GPP Release 18 pro NR, který umožňuje energeticky úsporné vyhledávání buněk a počáteční přístup, čímž snižuje spotřebu energie uživatelského zařízení (UE) a prodlužuje životnost baterie pro zařízení IoT.

## Popis

Low Power Synchronization Signal (LP-SS) je signál fyzické vrstvy definovaný ve specifikaci 3GPP Release 18 pro New Radio (NR), který je speciálně navržen pro minimalizaci spotřeby energie během procedur vyhledávání buňky a počátečního přístupu. Funguje jako součást rámce synchronizačního signálového bloku (SSB), ale je optimalizován pro nízkopříkonový provoz. LP-SS je vysílán gNB se specifickými charakteristikami, jako je snížená šířka pásma, nižší vysílací výkon nebo optimalizovaná periodicita, aby umožnil uživatelskému zařízení (UE) provádět synchronizaci s minimální dobou aktivace přijímače. Tento signál je klíčový pro zařízení, jako jsou IoT senzory a nositelná elektronika, která vyžadují ultra dlouhou životnost baterie, protože snižuje energii vynaloženou během kritické fáze počátečního připojení k síti.

Architektonicky je LP-SS integrován do specifikací fyzické vrstvy NR (řada TS 38.211) a je řízen vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) gNB. Typicky se skládá z primárního a sekundárního synchronizačního signálu (PSS/SSS), ale s úpravami pro snížení složitosti. Může například používat jednodušší sekvence nebo být vysílán méně často ve srovnání s konvenčními SSB. Zpracování signálu LP-SS ve fyzické vrstvě UE zahrnuje nízkopříkonové přijímací obvody, které mohou tyto signály detekovat s vysokou účinností, často využívají technologii wake-up přijímače (WUR) k minimalizaci použití hlavního přijímače. Parametry signálu, jako je kmitočtová poloha a časový vzor, jsou konfigurovány prostřednictvím systémových informací nebo vyhrazeného signalizačního RRC, aby byly v souladu se síťovými politikami úspory energie.

Během provozu, když se UE napájené baterií potřebuje synchronizovat s buňkou, aktivuje svůj nízkopříkonový přijímač k vyhledání LP-SS namísto plného SSB. Po detekci UE získá časovou a kmitočtovou synchronizaci spolu se základní identifikací buňky, než případně probudí svůj hlavní přijímač pro další procedury, jako je čtení fyzického vysílacího kanálu (PBCH). Tento dvoukrokový proces výrazně snižuje spotřebu energie. LP-SS je specifikován v několika dokumentech 3GPP, včetně TS 38.101 pro rádiové požadavky UE, TS 38.300 pro celkovou architekturu a TS 38.331 pro RRC protokoly, což zajišťuje interoperabilitu a výkonnostní standardy pro nízkopříkonové scénáře.

## K čemu slouží

LP-SS byl vytvořen, aby řešil rostoucí poptávku po energeticky úsporné komunikaci v 5G a dalších generacích, zejména pro případy použití Internetu věcí (IoT) a hromadné komunikace mezi stroji (mMTC). Před Release 18 se synchronizace v NR spoléhala na standardní SSB, které, ačkoli byly účinné pro vysoce výkonná zařízení, spotřebovávaly nadměrnou energii pro zařízení s omezenou kapacitou baterie během častého vyhledávání buněk nebo v prostředí s obtížným pokrytím. Toto omezení bránilo nasazení IoT senzorů a nositelné elektroniky s dlouhou životností v sítích NR, protože neustálá synchronizace rychle vybíjela baterie.

Motivace vychází z potřeby prodloužit životnost baterie zařízení z let na desetiletí, což je klíčový požadavek pro aplikace, jako je monitorování životního prostředí, chytré zemědělství a průmyslové senzory. Historické přístupy v LTE-M a NB-IoT nabízely nízkopříkonové funkce, ale nebyly nativně integrovány do rámce NR. LP-SS tuto mezeru zaplňuje zavedením nativního řešení NR, které snižuje spotřebu energie UE během počátečního přístupu, a je v souladu s vylepšeními RedCap (Reduced Capability) a IoT v 3GPP. Řeší problém plýtvání energií při synchronizaci optimalizací návrhu signálu, což umožňuje zařízením zůstat déle v klidovém režimu a aktivovat se minimálně pouze pro připojení k síti, a tím umožňuje udržitelná hromadná nasazení IoT v 5G sítích.

## Klíčové vlastnosti

- Optimalizován pro nízkopříkonovou synchronizaci UE
- Snížená šířka pásma a vysílací výkon ve srovnání se standardními SSB
- Integrován se specifikacemi fyzické vrstvy NR
- Podporuje vyhledávání buněk a počáteční přístup pro zařízení IoT
- Konfigurovatelný prostřednictvím signalizace RRC pro síťovou flexibilitu
- Umožňuje prodlouženou životnost baterie v hromadných scénářích IoT

## Související pojmy

- [LP-WUR – Low Power Wake Up Receiver](/mobilnisite/slovnik/lp-wur/)
- [LP-WUS – Low Power Wake Up Signal](/mobilnisite/slovnik/lp-wus/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [LP-SS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lp-ss/)
