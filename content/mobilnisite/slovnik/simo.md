---
slug: "simo"
url: "/mobilnisite/slovnik/simo/"
type: "slovnik"
title: "SIMO – Single Input, Multiple Output"
date: 2025-01-01
abbr: "SIMO"
fullName: "Single Input, Multiple Output"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/simo/"
summary: "SIMO je konfigurace MIMO antén, při níž jedna vysílací anténa vysílá signál k více přijímacím anténám. Poskytuje přijímací diverzitu, která zlepšuje spolehlivost signálu a pokrytí bojem proti útlumu a"
---

SIMO je konfigurace MIMO antén, při níž jedna vysílací anténa komunikuje s více přijímacími anténami, čímž poskytuje přijímací diverzitu, zlepšuje spolehlivost signálu a pokrytí.

## Popis

Single Input, Multiple Output (SIMO) je specifická konfigurace v rámci širší rodiny technologie Multiple Input, Multiple Output ([MIMO](/mobilnisite/slovnik/mimo/)). V systému SIMO je vysílač vybaven jedinou anténou, zatímco přijímač využívá více antén. Základním principem je využití prostorové dimenze na straně přijímače ke zlepšení kvality signálu prostřednictvím přijímací diverzity. Více přijímacích antén zachycuje více nezávisle utlumených verzí stejného vysílaného signálu. Protože pravděpodobnost, že všechny signálové cesty současně zažijí hluboký útlum, je nízká, může přijímač tyto signály zkombinovat a vytvořit spolehlivější a kvalitnější složený signál.

Fungování systému SIMO závisí na technikách zpracování signálu na straně přijímače. Mezi běžné kombinační metody patří výběrová kombinace (Selection Combining, [SC](/mobilnisite/slovnik/sc/)), při níž přijímač vybere větev antény s nejvyšším okamžitým poměrem signál-šum ([SNR](/mobilnisite/slovnik/snr/)); maximální poměrová kombinace (Maximal Ratio Combining, [MRC](/mobilnisite/slovnik/mrc/)), která váží a sčítá všechny přijímané signály úměrně jejich SNR a poskytuje optimální zisk z diverzity; a stejnoměrná kombinace (Equal Gain Combining, EGC), která sladí fáze a sečte signály se stejnými vahami. V systémech 3GPP je často preferovanou metodou MRC díky své lepší výkonnosti. Přijímač provádí odhad kanálu pro každou anténní větev, aby pochopil podmínky šíření, a před demodulací a dekódováním použije příslušný kombinační algoritmus.

Z architektonického hlediska je SIMO implementováno v uživatelském zařízení (UE) pro příjem uplinku na základnové stanici (např. [eNB](/mobilnisite/slovnik/enb/), gNB) a v základnové stanici pro příjem downlinku na UE. Je to základní stavební kánek bezdrátových standardů od 3G UMTS přes 4G LTE až po 5G NR. Zatímco samo SIMO poskytuje zisk z diverzity, často slouží jako výchozí bod nebo součást složitějších MIMO schémat, jako je Single User MIMO ([SU-MIMO](/mobilnisite/slovnik/su-mimo/)) nebo Multi-User MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)). Jeho role je klíčová pro zlepšení výkonu na okraji buňky, zvětšení plochy pokrytí a zajištění konzistentnějšího uživatelského zážitku tím, že zmírňuje účinky vícecestného útlumu a ko-kanálové interference bez zvýšení vysílacího výkonu.

## K čemu slouží

Hlavním účelem SIMO je zvýšit spolehlivost a kvalitu bezdrátového komunikačního spoje prostřednictvím přijímací diverzity. Bezdrátové kanály jsou z podstaty nepřátelské prostředí kvůli jevům, jako je vícecestné šíření, které způsobuje útlum signálu – výrazný pokles síly přijímaného signálu. Před rozšířením víceanténových technik systémy spoléhaly na jednoduché transceivery s jednou anténou, což je činilo velmi náchylnými k těmto útlumům, což vedlo k přerušeným hovorům a nízké datové propustnosti. SIMO tento problém řeší tím, že na straně přijímače poskytuje více prostorově oddělených 'uší', které statisticky zajišťují, že alespoň jedna anténa přijme použitelný signál.

Historicky se SIMO objevilo jako jedna z prvních praktických aplikací prostorové diverzity, která předcházela složitějším [MIMO](/mobilnisite/slovnik/mimo/). Vyřešilo kritický problém nespolehlivosti spoje bez nutnosti složitých změn na straně vysílače, což z něj učinilo atraktivní a nákladově efektivní cestu upgradu. Přímo řeší omezení systémů Single Input, Single Output (SISO), které nemají žádný vlastní mechanismus pro boj s útlumem kromě zvýšení výkonu. Zlepšením efektivního SNR na straně přijímače umožňuje SIMO spolehlivě používat modulace a kódování vyššího řádu, čímž zvyšuje spektrální účinnost a kapacitu sítě v dané oblasti pokrytí. Jeho implementace byla klíčovým krokem k sofistikovaným víceanténovým technologiím, které definují moderní mobilní sítě.

## Klíčové vlastnosti

- Poskytuje zisk z přijímací diverzity pro boj proti útlumu signálu
- Zlepšuje spolehlivost spoje a pokrytí, zejména na okrajích buňky
- Implementováno pomocí kombinačních technik, jako je Maximal Ratio Combining (MRC)
- Vyžaduje pouze jednu vysílací anténu, což zjednodušuje návrh vysílače
- Tvoří základní přijímací komponentu pro pokročilejší MIMO schémata
- Zlepšuje kvalitu signálu bez zvýšení vysílacího výkonu

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report

---

📖 **Anglický originál a plná specifikace:** [SIMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/simo/)
