---
slug: "dl-prs"
url: "/mobilnisite/slovnik/dl-prs/"
type: "slovnik"
title: "DL-PRS – Downlink Positioning Reference Signal"
date: 2025-01-01
abbr: "DL-PRS"
fullName: "Downlink Positioning Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dl-prs/"
summary: "Vyhrazený referenční signál vysílaný gNB v downlinku pro umožnění přesné lokalizace UE. Poskytuje vysoce přesná měření času a fáze pro techniky jako DL-TDOA a multi-RTT. Je základní součástí lokalizač"
---

DL-PRS je referenční signál v downlinku vysílaný gNB, který umožňuje přesnou lokalizaci UE tím, že poskytuje vysoce přesná měření času a fáze pro služby jako DL-TDOA a multi-RTT.

## Popis

Downlink Positioning Reference Signal (DL-PRS) je signál fyzické vrstvy definovaný v 3GPP 5G New Radio (NR) speciálně pro účely lokalizace. Jedná se o pseudonáhodnou sekvenci vysílanou gNodeB (gNB) na konfigurovaných časových a frekvenčních zdrojích v rámci tzv. positioning reference signal occasion. DL-PRS je navržen tak, aby měl nízké vlastnosti vzájemné korelace, což umožňuje uživatelskému zařízení (UE) rozlišit signály z více sousedních gNB, a to i v hustých scénářích nasazení. Jeho konfigurace, včetně šířky pásma, hřebenového vzoru (comb pattern), periodicity, muting patternů a struktury sady zdrojů (resource set), je vysoce flexibilní a signalizována UE prostřednictvím protokolů [RRC](/mobilnisite/slovnik/rrc/) a [LPP](/mobilnisite/slovnik/lpp/) za účelem optimalizace výkonu lokalizace pro různá prostředí a požadavky na přesnost.

Z architektonického hlediska jsou generování a vysílání DL-PRS řízeny fyzickou vrstvou gNB na základě parametrů poskytovaných vyššími vrstvami, které často pocházejí od funkce Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v core networku. UE přijímá tyto konfigurační parametry a provádí na DL-PRS měření, jako je Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)) pro [DL-TDOA](/mobilnisite/slovnik/dl-tdoa/) nebo rozdíl času Rx-Tx pro multi-RTT. Návrh signálu klade důraz na vysokou přesnost odhadu doby příchodu (ToA) a odolnost proti rušení. Mezi klíčové komponenty patří generování [PRS](/mobilnisite/slovnik/prs/) sekvence založené na Goldově sekvenci, mapování na resource elements v mřížce [OFDM](/mobilnisite/slovnik/ofdm/) symbolů a podpora beamformingu pro zlepšení kvality signálu a pokrytí.

V rámci provozu sítě LMF orchestruje lokalizační relaci, určuje, která gNB mají vysílat DL-PRS a s jakou konfigurací. UE měří DL-PRS z více gNB a hlášení o měřeních (např. RSTD) odesílá zpět LMF prostřednictvím obsluhujícího gNB. LMF poté tato měření používá v lokalizačních algoritmech k výpočtu polohy UE. Role DL-PRS je klíčová, protože poskytuje společný, kvalitní měřicí referenční bod, který umožňuje síťové, downlink-centrické lokalizační metody, a tvoří tak jádro lokalizačního rámce 5G spolu s uplinkovými a uplink-downlinkovými metodami.

## K čemu slouží

DL-PRS byl představen ve 3GPP Release 16, aby uspokojil rostoucí poptávku po vysoce přesných lokalizačních službích s nízkou latencí v sítích 5G, které předchozí buněčné systémy, jako je LTE, nemohly adekvátně uspokojit. Před NR se lokalizace primárně spoléhala na signály, které nebyly specificky optimalizovány pro lokalizaci, jako byly Cell-specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)) v LTE, které nabízely omezenou přesnost (desítky metrů) a nebyly navrženy pro hustá vícebuněčná měření. Omezení těchto starších přístupů zahrnovala nedostatečnou šířku pásma, nízké rozlišení doby příchodu a náchylnost k rušení, což je činilo nevhodnými pro nové případy užití, jako je průmyslový IoT, autonomní vozidla a rozšířená realita.

Vytvoření DL-PRS bylo motivováno potřebou vyhrazeného, síťově řízeného downlinkového signálu, který by mohl poskytovat přesnost na úrovni centimetrů až metrů. Řeší problém získání přesných časových měření z více základnových stanic tím, že nabízí signál s konfigurovatelnou vysokou šířkou pásma, nízkou vzájemnou korelací a předvídatelnými vzory vysílání. To umožňuje efektivní fungování pokročilých lokalizačních technik, jako jsou DL-TDOA a multi-RTT. Historicky byl vývoj hnut požadavky vertikálních průmyslů a regulatorními požadavky (např. E911), což vedlo 3GPP ke standardizaci nativního, vysoce výkonného lokalizačního řešení jako integrální součásti 5G NR rozhraní.

## Klíčové vlastnosti

- Vyhrazená pseudonáhodná sekvence s nízkou vzájemnou korelací pro rozlišení vysílání z více gNB
- Vysoce flexibilní konfigurace šířky pásma, periody a mapování zdrojů prostřednictvím RRC a LPP
- Podpora beamformingu a vysílání v kmitočtových pásmech FR1 (pod 6 GHz) a FR2 (mmWave)
- Konfigurovatelné muting patterny pro zmírnění rušení a identifikaci silných zdrojů DL-PRS
- Navrženo pro vysokou přesnost měření doby příchodu (ToA) a rozdílu času referenčního signálu (RSTD)
- Integrace s NR lokalizačními protokoly (LPP, NRPPa) pro správu lokalizační relace end-to-end

## Související pojmy

- [DL-TDOA – Downlink Time Difference Of Arrival](/mobilnisite/slovnik/dl-tdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [DL-PRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dl-prs/)
