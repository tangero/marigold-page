---
slug: "tdcp"
url: "/mobilnisite/slovnik/tdcp/"
type: "slovnik"
title: "TDCP – Time Domain Channel Properties"
date: 2025-01-01
abbr: "TDCP"
fullName: "Time Domain Channel Properties"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tdcp/"
summary: "TDCP označuje charakteristiky rádiového kanálu v časové oblasti, jako je rozprostření zpoždění a rozprostření Dopplerova jevu, které ovlivňují šíření signálu a výkon přijímače. V 3GPP NR se používá pr"
---

TDCP je charakterizace časových vlastností rádiového kanálu, jako je rozprostření zpoždění (delay spread) a rozprostření Dopplerova jevu (Doppler spread), které se v NR používají pro hlášení stavu kanálu a správu paprsků.

## Popis

Časové vlastnosti kanálu (Time Domain Channel Properties, TDCP) jsou parametry popisující chování bezdrátového komunikačního kanálu v čase, klíčové pro návrh robustních algoritmů fyzické vrstvy. Mezi tyto vlastnosti patří klíčové metriky, jako je rozprostření zpoždění, které charakterizuje časovou disperzi vícecestných složek, a rozprostření Dopplerova jevu, které udává rychlost změn kanálu v důsledku mobility. V 3GPP New Radio (NR) se TDCP využívá v rámcích pro hlášení informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) definovaných v specifikacích jako 38.214 a 38.331, což umožňuje gNB a UE dynamicky přizpůsobovat přenosové parametry.

Odhad TDCP zahrnuje zpracování referenčních signálů, jako jsou referenční signály pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) nebo bloky synchronizačních signálů (SSB). UE měří impulsní odezvu kanálu a profil zpoždění výkonu, aby extrahovalo rozprostření zpoždění, které ovlivňuje volby jako délka cyklického prefixu nebo návrh ekvalizéru. Podobně se rozprostření Dopplerova jevu odvozuje z časové korelace kanálu, což má vliv na zvládání mobility a šířku pásma sledovacích smyček. Tyto vlastnosti jsou kvantovány a hlášeny síti prostřednictvím řídicích kanálů v uplinku, což usnadňuje informovaná rozhodnutí o plánování a beamformingu.

TDCP hraje zásadní roli v pokročilých funkcích NR, jako je správa paprsků a massive [MIMO](/mobilnisite/slovnik/mimo/). Například znalost rozprostření zpoždění pomáhá při výběru vhodných prekódovacích matic a adaptaci ranku, zatímco rozprostření Dopplerova jevu informuje o spouštěčích předávání spojení (handover) a rychlostech přepínání paprsků. Integrace TDCP do signalizace řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) umožňuje konfigurovat síťově nastavené periody hlášení a prahové hodnoty, čímž vyvažuje režii a výkon. Přesnou charakterizací časových variací kanálu TDCP zvyšuje spektrální účinnost, spolehlivost a uživatelský komfort v různých scénářích nasazení.

## K čemu slouží

TDCP existuje, aby poskytoval standardizovanou metodu pro kvantifikaci časově proměnných podmínek kanálu, čímž reaguje na potřebu adaptivních technik fyzické vrstvy v moderních bezdrátových systémech. Řeší problémy související s degradací signálu v prostředích s vícecestným šířením a vysokou mobilitou, kde jsou statické modely kanálu nedostatečné. Motivace vychází z rostoucí složitosti nasazení NR, která vyžadují přesnou znalost kanálu pro funkce jako beamforming a ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)).

Historicky starší systémy, jako LTE, obsahovaly indikátory kvality kanálu, ale postrádaly podrobné hlášení časových vlastností. TDCP v NR tuto mezeru zaplňuje tím, že nabízí detailní metriky umožňující sofistikovanější adaptaci spoje. Řeší omezení hlášení pouze ve frekvenční oblasti, které nemusí zachytit časové variace klíčové pro správu mobility. Vytvoření TDCP bylo hnací silou poptávky po vyšších přenosových rychlostech a spolehlivosti v 5G, zejména pro případy užití zahrnující rychle se pohybující vozidla nebo dynamické rozptylovače.

## Klíčové vlastnosti

- Kvantifikace rozprostření zpoždění pro charakterizaci vícecestného šíření
- Měření rozprostření Dopplerova jevu pro posouzení mobility
- Integrace s rámci pro hlášení CSI v NR
- Podpora správy paprsků a adaptace spoje
- Konfigurovatelné hlášení prostřednictvím signalizace RRC
- Využití referenčních signálů, jako je CSI-RS, pro odhad

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TDCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdcp/)
