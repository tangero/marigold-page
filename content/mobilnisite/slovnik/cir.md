---
slug: "cir"
url: "/mobilnisite/slovnik/cir/"
type: "slovnik"
title: "CIR – Carrier to Interference Ratio"
date: 2025-01-01
abbr: "CIR"
fullName: "Carrier to Interference Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cir/"
summary: "CIR je základní měření rádiové frekvence představující poměr výkonu požadovaného signálu nosné k výkonu rušení. Je to klíčový parametr pro hodnocení kvality signálu, určení výkonnosti spoje a pro rozh"
---

CIR (Carrier to Interference Ratio) je poměr výkonu požadovaného signálu nosné k výkonu rušení. Jedná se o klíčový parametr pro hodnocení kvality signálu a určení výkonnosti spoje v bezdrátových sítích.

## Popis

Carrier to Interference Ratio (CIR, poměr signálu nosné k rušení) je bezrozměrná veličina vyjádřená v decibelech (dB), která kvantifikuje kvalitu přijímaného rádiového signálu porovnáním výkonu požadovaného signálu nosné s kombinovaným výkonem všech rušivých signálů ve stejném kmitočtovém pásmu. Matematicky CIR = P_nosná / P_rušení, kde P_nosná je přijímaný výkon požadovaného signálu a P_rušení je celkový výkon ze všech zdrojů rušení, včetně ko-kanálového rušení, rušení sousedním kanálem a dalších rádiově frekvenčních zkreslení. Toto měření se provádí na fyzické vrstvě během příjmu a zpracování signálu, typicky v rámci RF předkoncového stupně přijímače a řetězce základního pásma.

V systémech 3GPP k měření CIR dochází nepřetržitě během aktivních spojení prostřednictvím vyhrazených referenčních signálů a pilotních symbolů vestavěných do struktury přenosového rámce. Přijímač vypočítává CIR porovnáním známého vzoru vysílaného referenčního signálu s přijímaným signálem a izoluje složky rušení pomocí korelačních technik. Pro systémy LTE a NR slouží jako základ těchto měření buňkově specifické referenční signály ([CRS](/mobilnisite/slovnik/crs/)) v LTE a referenční signály pro demodulaci ([DM-RS](/mobilnisite/slovnik/dm-rs/)) v NR. Měřená šířka pásma pro hodnocení CIR typicky odpovídá alokaci zdrojových bloků nebo systémové šířce pásma, v závislosti na tom, zda jsou požadována měření širokopásmová nebo subpásmová.

Hodnota CIR přímo určuje dosažitelný poměr signálu k šumu plus rušení (SINR), který následně podle tabulek adaptace spoje systému určuje maximálně podporovatelné schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)). Vyšší hodnoty CIR umožňují modulační schémata vyššího řádu (jako 256-QAM nebo 1024-QAM) a nižší kódovou režii, což vede k vyšší spektrální účinnosti a propustnosti. Naopak nízké hodnoty CIR nutí systém používat robustní, ale méně účinnou modulaci (jako QPSK) s vyšší kódovou ochranou. Síťové algoritmy používají měření CIR pro řadu funkcí včetně rozhodování o předávání spojení, koordinaci rušení, úpravy řízení výkonu a řízení paprsků v systémech massive [MIMO](/mobilnisite/slovnik/mimo/).

CIR se od poměru nosná-šum ([CNR](/mobilnisite/slovnik/cnr/)) liší tím, že ze jmenovatele konkrétně vylučuje tepelný šum a zaměřuje se čistě na umělé zdroje rušení. V praktických nasazeních pomáhají měření CIR operátorům identifikovat ohniska rušení, optimalizovat kmitočtové plánování a implementovat techniky pro zmírnění rušení, jako je Enhanced Inter-Cell Interference Coordination (eICIC) v LTE nebo konfigurace Interference Measurement Resource ([IMR](/mobilnisite/slovnik/imr/)) v NR. Přesnost odhadu CIR přímo ovlivňuje výkon sítě, přičemž pokročilé přijímače používají kombinaci s potlačením rušení ([IRC](/mobilnisite/slovnik/irc/)) a ekvalizaci s minimální střední kvadratickou chybou ([MMSE](/mobilnisite/slovnik/mmse/)), aby zlepšily CIR v náročných podmínkách rušení.

## K čemu slouží

Měření CIR bylo zavedeno, aby řešilo zásadní problém bezdrátových systémů omezených rušením, kde je výkon limitován nikoli tepelným šumem, ale rušením od jiných vysílačů používajících stejné kmitočtové zdroje. V raných celulárních systémech vytvářely vzorce opakovaného využití kmitočtů předvídatelné scénáře rušení, ale jak se sítě vyvíjely směrem k vyšším faktorům opakovaného využití kmitočtů (blížícím se 1), stalo se rušení dominantním limitujícím faktorem výkonu. CIR poskytuje přímou kvantitativní míru tohoto dopadu rušení, což umožňuje inteligentní správu a optimalizaci sítě.

Před standardizovanými technikami měření CIR se síťoví operátoři spoléhali na subjektivní metriky kvality nebo jednoduché indikátory síly přijímaného signálu (RSSI), které nedokázaly rozlišit mezi silným požadovaným signálem a silným rušením. Toto omezení ztěžovalo diagnostiku rušení a činilo optimalizaci neefektivní. Formalizace měření CIR ve standardech 3GPP vytvořila konzistentní, srovnatelnou metriku napříč zařízeními různých výrobců a generacemi sítí, což umožnilo automatizované algoritmy pro správu rušení a srovnávací testy výkonu.

Primární účel CIR přesahuje pouhé měření – slouží jako základ pro adaptivní přidělování zdrojů, plánování s ohledem na rušení a koordinované operace multipoint. V moderních sítích využívajících agregaci nosných, duální konektivitu a síťové slicing umožňuje přesný odhad CIR inteligentní výběr komponentních nosných, plánování napříč nosnými a správu rušení specifickou pro slice. Vývoj směrem k ultra-hustým sítím a nasazením v milimetrových vlnách učinil CIR ještě kritičtějším, protože tato prostředí vykazují rychle se měnící vzorce rušení vyžadující měření a reakci v reálném čase.

## Klíčové vlastnosti

- Kvantitativní měření rušení nezávislé na tepelném šumu
- Základ pro výběr adaptivního schématu modulace a kódování
- Vstup pro rozhodování o předávání spojení a správu mobility
- Základ pro algoritmy koordinace rušení jako eICIC a FeICIC
- Umožňuje plánování a přidělování zdrojů s ohledem na rušení
- Podporuje řízení paprsků a měření rušení v NR

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [CIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cir/)
