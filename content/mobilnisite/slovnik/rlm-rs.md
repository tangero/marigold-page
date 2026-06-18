---
slug: "rlm-rs"
url: "/mobilnisite/slovnik/rlm-rs/"
type: "slovnik"
title: "RLM-RS – Reference Signal for Radio Link Monitoring"
date: 2025-01-01
abbr: "RLM-RS"
fullName: "Reference Signal for Radio Link Monitoring"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rlm-rs/"
summary: "RLM-RS (Reference Signal for RLM) je konfigurovatelný referenční signál v downlinku, který UE využívá speciálně pro Radio Link Monitoring v 5G NR. Poskytuje flexibilitu nad rámec vždy vysílaného SSB,"
---

RLM-RS je konfigurovatelný referenční signál v downlinku, který UE využívá speciálně pro monitorování kvality rádiového spoje v 5G NR, a poskytuje tak větší flexibilitu než standardní synchronizační signály.

## Popis

Reference Signal for Radio Link Monitoring (RLM-RS) je koncept zavedený v 5G New Radio (NR) počínaje 3GPP Release 15. Označuje konkrétní referenční signál(y) v downlinku, které je UE nakonfigurováno měřit pro účely Radio Link Monitoring ([RLM](/mobilnisite/slovnik/rlm/)). V NR, na rozdíl od LTE, kde byly pro RLM vždy dostupné a používány Cell-specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)), má síť flexibilitu konfigurovat, který signál má UE monitorovat. Primárními kandidáty pro RLM-RS jsou Synchronization Signal Block (SSB) a Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)).

Konfigurace RLM-RS je UE poskytnuta prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace v rámci informačního elementu RadioLinkMonitoringRS. Tato konfigurace specifikuje sadu zdrojů (např. konkrétní sadu zdrojů CSI-RS nebo index SSB) a přidružené předpoklady kvazi-ko-lokace ([QCL](/mobilnisite/slovnik/qcl/)). UE používá nakonfigurovaný RLM-RS k odhadu kvality rádiového spoje v downlinku a porovnává ji s nakonfigurovanými prahy Q_out a Q_in. Tento měřicí proces je kontinuální během režimu RRC_CONNECTED, kdykoli se UE nenachází v měřicí mezeře nebo v období spánku [DRX](/mobilnisite/slovnik/drx/).

Použití konfigurovatelného RLM-RS je zvláště důležité pro beamově orientovaný provoz NR. gNB může vysílat více beamů (prostřednictvím SSB nebo CSI-RS beamů) a obslužný beam UE se může měnit v důsledku procedur správy beamů. Síť může nakonfigurovat RLM-RS tak, aby odpovídal aktivnímu stavu Transmission Configuration Indication ([TCI](/mobilnisite/slovnik/tci/)) UE, čímž zajistí, že UE monitoruje kvalitu konkrétního beamu používaného pro přenos dat. Pokud se tento beam zhorší, procedura RLM může spustit obnovu dříve, než dojde k úplnému selhání rádiového spoje.

RLM-RS navíc umožňuje úsporu energie sítě. V LTE musely být CRS vysílány nepřetržitě ve všech buňkách, aby podporovaly starší funkce jako RLM, což vedlo k neustálé spotřebě energie. V NR, pokud síť nakonfiguruje RLM na základě periodického CSI-RS, může potenciálně utlumit nebo snížit vysílání SSB v určitých obdobích a tím ušetřit energii. Síť musí zajistit, aby byl nakonfigurovaný RLM-RS vysílán s dostatečnou periodicitou a hustotou, aby UE mohlo splnit požadovanou přesnost a včasnost vyhodnocení RLM.

## K čemu slouží

RLM-RS byl vytvořen, aby řešil omezení modelu [RLM](/mobilnisite/slovnik/rlm/) z LTE a podporoval nové architektonické principy 5G NR. V LTE se RLM spoléhalo výhradně na vždy přítomný Cell-specific Reference Signal (CRS). To nutilo všechny buňky k nepřetržitému vysílání CRS, což přispívalo k neustálé spotřebě energie sítě a omezovalo flexibilitu. NR si kladlo za cíl být efektivnější a beamově orientovanější.

Hlavním problémem, který RLM-RS řeší, je poskytnutí flexibilního a efektivního mechanismu pro monitorování rádiového spoje v síti, kde nemusí být vysílány vždy zapnuté, celobuněčné referenční signály. Umožňuje síti přizpůsobit monitorovací signál konkrétnímu provoznímu kontextu UE, jako je její aktivní beam. To je klíčové pro udržení spolehlivého připojení ve vysokofrekvenčních pásmech (např. mmWave), kde je beamforming zásadní. Také umožňuje pokročilé techniky úspory energie sítě tím, že odděluje nutnost neustálého vysílání synchronizačních signálů od požadavku na kontinuální monitorování spoje.

## Klíčové vlastnosti

- Konfigurovatelný prostřednictvím RRC signalizace (IE RadioLinkMonitoringRS), což umožňuje síti definovat referenční signály pro RLM.
- Podporuje jak SSB, tak CSI-RS jako potenciální typy RLM-RS.
- Soulad se správou beamů; RLM-RS může být propojen s aktivním stavem TCI UE pro beamově specifické monitorování.
- Umožňuje úsporu energie sítě tím, že umožňuje fungování RLM bez nutnosti nepřetržitého vysílání SSB.
- Poskytuje informace o kvazi-ko-lokaci (QCL) přidružené k RLM-RS, které definují prostorové parametry příjmu (Rx) pro přesné měření.
- Umožňuje periodické nebo semi-persistentní vysílání nakonfigurovaného zdroje RLM-RS.

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification

---

📖 **Anglický originál a plná specifikace:** [RLM-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlm-rs/)
