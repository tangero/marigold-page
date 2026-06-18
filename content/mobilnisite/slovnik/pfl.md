---
slug: "pfl"
url: "/mobilnisite/slovnik/pfl/"
type: "slovnik"
title: "PFL – Positioning Frequency Layer"
date: 2025-01-01
abbr: "PFL"
fullName: "Positioning Frequency Layer"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pfl/"
summary: "Polohovací kmitočtová vrstva (PFL) je soubor polohovacích referenčních signálů (PRS) v downlinku a s nimi spojené konfigurace vysílaných na konkrétní kmitočtové vrstvě. Je to základní koncept v rámci"
---

PFL je soubor polohovacích referenčních signálů v downlinku a jejich konfigurace vysílaných na konkrétní kmitočtové vrstvě, který tvoří základní zdroj pro vysoce přesná měření polohy v sítích 3GPP.

## Popis

Polohovací kmitočtová vrstva (PFL) je klíčová architektonická komponenta v rámci polohovací architektury New Radio (NR) 3GPP, definovaná pro organizaci a správu vysílání polohovacích referenčních signálů. Koncepčně PFL sdružuje všechny potřebné polohovací zdroje v downlinku – především Polohovací referenční signály ([PRS](/mobilnisite/slovnik/prs/)) – které jsou vysílány z jednoho nebo více přenosových/přijímacích bodů ([TRP](/mobilnisite/slovnik/trp/)) na konkrétní kmitočtové vrstvě. Každá PFL je charakterizována jedinečnou sadou konfiguračních parametrů, včetně kmitočtové vrstvy, šířky pásma, struktury PRS (comb struktura, muting pattern), periodicity a prostorového vztahu (např. informace o beamu) vysílaných signálů. Síť může nakonfigurovat více PFL, případně na různých kmitočtech, aby poskytla polohovací asistenční data uživatelskému zařízení (UE).

UE tuto konfiguraci používá k provádění přesných měření správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) na určených PRS zdrojích. Pro downlinkové polohovací metody, jako je Downlink Time Difference of Arrival ([DL-TDOA](/mobilnisite/slovnik/dl-tdoa/)) nebo Downlink Angle of Departure (DL-AoD), měří UE čas příchodu nebo úhel signálů z více TRP patřících ke stejné nebo různým PFL. Struktura PFL umožňuje síti efektivně spravovat polohovací zdroje napříč potenciálně heterogenním nasazením s více kmitočtovými pásmy a TRP. Umožňuje funkci správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) přesně instruovat UE, které signály má měřit, čímž optimalizuje přesnost a snižuje spotřebu energie UE tím, že se vyhne nepotřebným měřením.

Konfigurace PFL je doručena UE pomocí signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) nebo v rámci zpráv Long Term Evolution (LTE) Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) od LMF. PFL je úzce spojena s konkrétním číslem absolutního rádiového kmitočtového kanálu NR ([NR-ARFCN](/mobilnisite/slovnik/nr-arfcn/)). Při nasazení na více kmitočtech může být pro UE nakonfigurována primární PFL (např. na kmitočtu její obslužné buňky) a jedna nebo více sekundárních PFL na jiných kmitočtech, které může měřit, pokud je toho schopna. Tento koncept je zásadní pro podporu scénářů agregace nosných a duální konektivity v polohování, protože umožňuje UE kombinovat měření z různých vrstev pro zvýšení přesnosti, zejména v náročných rádiových prostředích, jako jsou podmínky bez přímé viditelnosti.

## K čemu slouží

Polohovací kmitočtová vrstva (PFL) byla zavedena, aby uspokojila potřebu strukturované a škálovatelné metody pro podporu vysoce přesného polohování v sítích 5G NR. Před polohováním v NR Rel-16 spoléhalo polohování v LTE na buňkové referenční signály (CRS) nebo vyhrazené PRS, ale architektuře chyběl formalizovaný koncept vrstvy pro správu rostoucí složitosti nasazení s více kmitočty a více TRP, která se očekávala v 5G. Rozšíření kmitočtových pásem pro 5G, včetně FR1 (sub-6 GHz) a FR2 (mmWave), a využití hustých sítí s mnoha TRP si vyžádalo model organizace zdrojů, který by mohl efektivně sdělit, které signály má UE měřit pro účely polohování.

Vytvoření konceptu PFL řeší problém jednoznačné konfigurace polohovacích zdrojů. Umožňuje síti abstrahovat fyzikální detaily přenosu PRS z více zdrojů do logické 'vrstvy', které může UE rozumět. To je klíčové pro umožnění pokročilých polohovacích technik, které vyžadují koordinaci napříč různými nosnými a TRP, jako je multi-RTT (Round Trip Time) nebo vylepšený DL-TDOA. Bez struktury PFL by asistence UE při provádění měření mezi kmitočty byla těžkopádná a náročná na signalizaci. PFL poskytuje základní stavební kámen, na kterém jsou postaveny ambiciózní cíle 3GPP pro přesnost polohování (např. subměrová v interiéru), a to tím, že zajišťuje, aby UE mohla spolehlivě přistupovat a měřit vysoce kvalitní, sítí koordinované polohovací signály.

## Klíčové vlastnosti

- Sdružuje zdroje PRS v downlinku vysílané na konkrétní kmitočtové vrstvě NR
- Definována jedinečnou sadou konfiguračních parametrů včetně NR-ARFCN, šířky pásma a struktury PRS
- Umožňuje síťovou konfiguraci primárních a sekundárních polohovacích vrstev pro měření UE
- Podporuje downlinkové polohovací metody jako DL-TDOA a DL-AoD
- Usnadňuje polohování ve scénářích s více kmitočty a agregací nosných
- Konfigurace je poskytnuta UE prostřednictvím signalizace RRC nebo LPP od LMF

## Související pojmy

- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [DL-TDOA – Downlink Time Difference Of Arrival](/mobilnisite/slovnik/dl-tdoa/)
- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [NR-ARFCN – NR Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/nr-arfcn/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TR 38.859** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [PFL na 3GPP Explorer](https://3gpp-explorer.com/glossary/pfl/)
