---
slug: "u-psmf"
url: "/mobilnisite/slovnik/u-psmf/"
type: "slovnik"
title: "U-PSMF – UTRAN Position Signal Measurement Function"
date: 2025-01-01
abbr: "U-PSMF"
fullName: "UTRAN Position Signal Measurement Function"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-psmf/"
summary: "Funkční entita v rámci UTRAN odpovědná za sběr a zpracování měření rádiových signálů pro určení polohy uživatelského zařízení (UE). Je klíčovou součástí pro služby založené na poloze, která umožňuje s"
---

U-PSMF je funkční entita UTRAN odpovědná za sběr a zpracování měření rádiových signálů za účelem určení polohy uživatelského zařízení pro služby založené na poloze.

## Popis

[UTRAN](/mobilnisite/slovnik/utran/) Position Signal Measurement Function (U-PSMF) je kritická komponenta v architektuře UTRAN určená k podpoře služeb určování polohy. Funguje jako logická funkce, typicky umístěná v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)), odpovědná za sběr, zpracování a hlášení měření rádiových signálů nezbytných pro určení polohy uživatelského zařízení (UE). U-PSMF komunikuje s dalšími síťovými prvky, jako je Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) v jádru sítě, aby podpořila různé metody určování polohy definované standardy 3GPP.

Hlavní operační role U-PSMF spočívá v koordinaci procesu měření. Po přijetí požadavku na určení polohy, často vyvolaného aplikací služby založené na poloze, U-PSMF nařídí příslušným Node B a cílovému UE provedení specifických měření signálu. Tato měření mohou zahrnovat parametry jako doba zpátečního letu ([RTT](/mobilnisite/slovnik/rtt/)), pozorované časové rozdíly nebo úrovně signálu. U-PSMF agreguje tato nezpracovaná měřicí data z více zdrojů v rámci rádiové přístupové sítě.

Po sběru U-PSMF tato měření zpracovává. Toto zpracování může zahrnovat filtrování, časové značkování a formátování dat podle požadavků zvolené metody určování polohy, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Uplink Time Difference of Arrival ([U-TDOA](/mobilnisite/slovnik/u-tdoa/)). Zpracovaná měřicí zpráva je následně předána SMLC. SMLC, který obsahuje algoritmy pro výpočet polohy, použije tuto zprávu k výpočtu odhadovaných geografických souřadnic UE. U-PSMF tedy funguje jako zástupce RAN pro určování polohy, abstrahující složitost sběru rádiových měření od lokálního serveru v jádru sítě.

## K čemu slouží

U-PSMF byla zavedena za účelem standardizace a centralizace procesu sběru měření signálů pro určování polohy UE v rámci [UTRAN](/mobilnisite/slovnik/utran/). Před jejím formálním definováním byly možnosti určování polohy méně strukturované a často závislé na dodavateli, což bránilo interoperabilitě a spolehlivému nasazení služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)). Vytvoření U-PSMF reagovalo na rostoucí regulatorní a komerční poptávku po přesné mobilní lokalizaci, poháněnou požadavky jako Enhanced 911 (E911) ve Spojených státech a rozvíjejícím se trhem aplikací využívajících polohu.

Jejím účelem je řešit problém efektivního a spolehlivého shromažďování přesných rádiových měření potřebných pro síťové a UE-asistované techniky určování polohy. Definováním vyhrazené funkční entity v RNC zajistil 3GPP konzistentní rozhraní (např. k SMLC přes rozhraní Lup) a řízený proces pro koordinaci měření. Toto oddělení odpovědností umožňuje SMLC v jádru sítě soustředit se na algoritmy výpočtu polohy, zatímco U-PSMF se stará o měření specifická pro rádiové rozhraní v reálném čase, čímž zlepšuje celkovou spolehlivost a výkon systému pro požadavky na určení polohy.

## Klíčové vlastnosti

- Koordinuje měření rádiových signálů pro určování polohy UE v rámci UTRAN
- Komunikuje se Serving Mobile Location Centre (SMLC) v jádru sítě
- Sbírá a zpracovává měření, jako je doba zpátečního letu (RTT) a pozorované časové rozdíly
- Podporuje více metod určování polohy podle 3GPP včetně OTDOA a Cell-ID
- Je implementována jako logická funkce typicky v rámci Radio Network Controller (RNC)
- Formátuje a doručuje měřicí zprávy pro výpočet polohy

## Související pojmy

- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [U-TDOA – Uplink Time Difference Of Arrival](/mobilnisite/slovnik/u-tdoa/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-PSMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-psmf/)
