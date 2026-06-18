---
slug: "dfe"
url: "/mobilnisite/slovnik/dfe/"
type: "slovnik"
title: "DFE – Downlink Frame Error"
date: 2025-01-01
abbr: "DFE"
fullName: "Downlink Frame Error"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dfe/"
summary: "Metrika udávající selhání při správném příjmu sestupné přenosové rámečkové jednotky. Měří spolehlivost sestupného kanálu a používá se pro adaptaci spojení, řízení výkonu a rozhodování o předávání spoj"
---

DFE (Downlink Frame Error, chyba sestupné rámečkové přenosové jednotky) je metrika udávající selhání při správném příjmu sestupné přenosové rámečkové jednotky. Používá se k měření spolehlivosti sestupného kanálu pro adaptaci spojení, řízení výkonu a rozhodování o předávání spojení.

## Popis

Downlink Frame Error (DFE, chyba sestupné rámečkové přenosové jednotky) je základní metrika výkonu v bezdrátových komunikačních systémech 3GPP, která konkrétně měří míru selhání příjmu sestupných datových rámečkových jednotek na uživatelském zařízení (UE). Představuje poměr neúspěšně dekódovaných sestupných transportních bloků k celkovému počtu vyslaných bloků, obvykle vypočítaný za určité měřicí období nebo okno. Detekce chyby rámečkové jednotky nastává, když kontrolní součet cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)) připojený k přijatému transportnímu bloku na straně UE selže, což indikuje, že data obsahují neopravitelné chyby i přes použití dekódovacích algoritmů pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)). Tato metrika je vnitřně propojena s výkonem fyzické vrstvy a poskytuje přímou indikaci kvality sestupného kanálu, jak ji zažívá terminál.

Proces měření DFE zahrnuje několik klíčových komponent v přijímacím řetězci UE. Po přijetí sestupného přenosu UE provede odhad kanálu, ekvalizaci, demodulaci a dešifrování, aby obnovila zakódované bity. Tyto bity jsou následně zpracovány dekodérem FEC (například Turbo dekodérem nebo [LDPC](/mobilnisite/slovnik/ldpc/) dekodérem v závislosti na generaci technologie). Po dekódování se na obnovených datech vypočítá CRC a porovná s přijatými CRC bity. Neshoda spustí událost DFE. UE typicky udržuje čítače pro úspěšné i neúspěšné příjmy rámečkových jednotek, které se používají pro výpočet poměru DFE. Tyto informace jsou často hlášeny síti prostřednictvím měřicích hlášení, zejména když jsou spuštěny nakonfigurované události související s monitorováním rádiového spoje.

Z architektonického hlediska je monitorování DFE funkcí rozdělenou mezi fyzickou vrstvu UE a protokoly vyšších vrstev. Fyzická vrstva provádí skutečnou detekci chyb, zatímco vrstva 2 ([RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/)) nebo vrstva 3 ([RRC](/mobilnisite/slovnik/rrc/)) může tyto statistiky agregovat a podmíněně je hlásit síti. Síť používá informace o DFE pro kritické funkce správy rádiových zdrojů. Například řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS nebo gNB v NR využívá hlášení DFE k úpravě schémat modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), změně úrovní vysílacího výkonu, zahájení předání spojení k buňkám s lepší kvalitou signálu nebo dokonce ke spuštění procedur selhání rádiového spoje, pokud se míra DFE trvale zvýší. Konkrétní prahové hodnoty a mechanismy hlášení pro DFE jsou definovány v příslušných specifikacích 3GPP, což zajišťuje standardizované chování napříč zařízeními různých výrobců.

Role DFE přesahuje pouhé monitorování výkonu; je to zásadní vstup pro uzavřené regulační smyčky, které zajišťují spektrální účinnost a kontinuitu služeb. V adaptivní modulaci a kódování (AMC) může vysoká míra DFE způsobit, že síť přepne na robustnější (avšak s nižší propustností) MCS, čímž vymění datový tok za spolehlivost. Naopak nízká míra DFE umožňuje použití modulací vyššího řádu pro zvýšení propustnosti. Dále se trendy DFE analyzují pro správu mobility – rostoucí DFE na obsluhující buňce spolu s lepší kvalitou na sousední buňce tvoří základ pro rozhodování o předání spojení. V podstatě DFE poskytuje měřítko schopnosti sestupného spoje doručit data neporušená v reálném čase a nezávisle na aplikaci, což z ní činí základní metriku pro autonomní optimalizaci rádiových sítí.

## K čemu slouží

Účelem definice a standardizace metriky Downlink Frame Error (DFE) je poskytnout síťovému zařízení a koncovým zařízením společné, jednoznačné měřítko spolehlivosti sestupného přenosu. Před standardizovanými metrikami, jako je DFE, mohli výrobci používat proprietární měření chyb, což ztěžovalo interoperabilitu a konzistentní optimalizaci sítě. DFE řeší problém objektivního posouzení výkonu fyzické vrstvy z perspektivy UE, které je často reprezentativnější pro uživatelský zážitek než metriky na straně sítě, jako jsou odhady míry chyb bloků (BLER). Umožňuje datově řízené regulační smyčky, které jsou nezbytné pro udržení stabilního rádiového spoje za měnících se podmínek kanálu.

Historicky, jak se buněčné systémy vyvíjely od okruhově přepínaných hlasových služeb k paketově přepínaným datovým službám, potřeba přesné a dynamické adaptace spojení se stala prvořadou. Hlasové služby mohly tolerovat periodické ztráty rámečkových jednotek díky robustním kodekům a skrývání chyb, ale datové služby, zejména ty vyžadující vysokou integritu, jako jsou stahování souborů nebo hraní her v reálném čase, jsou citlivější. Vytvoření DFE jako standardizované metriky bylo motivováno potřebou posunout se za jednoduchá měření síly signálu (jako RSCP nebo RSRP) a začlenit skutečný úspěch doručení dat do rozhodování sítě. Síla signálu může být vysoká, ale rušení nebo útlum by stále mohly způsobit časté chyby rámečkových jednotek; DFE tento efekt zachycuje přímo.

Dále DFE řeší omezení dřívějších, hrubších metrik tím, že poskytuje detailní pohled na výkon na úrovni jednotlivých transportních bloků. Umožňuje síti rozlišit mezi přechodnými chybami a trvalým zhoršením spoje. Tato schopnost je klíčová pro implementaci pokročilých funkcí správy rádiových zdrojů zavedených v LTE a 5G NR, jako je zpřesnění hlášení indikátoru kvality kanálu (CQI), výběr víceanténních technik (např. volba mezi přenosovou diverzitou a prostorovým multiplexováním na základě skutečných chybových měr) a správa komponent agregace nosných. Stručně řečeno, DFE existuje proto, aby převedla fyzickou realitu rádiového kanálu na kvantifikovatelnou, akční metriku, kterou automatizované síťové algoritmy mohou použít k maximalizaci propustnosti, minimalizaci latence a zajištění spolehlivého připojení pro koncové uživatele.

## Klíčové vlastnosti

- Poskytuje přímé měření úspěšnosti příjmu sestupných dat na UE
- Spouští se na základě selhání kontrolního součtu cyklickou redundancí (CRC) po dekódování FEC
- Slouží jako klíčový vstup pro adaptaci schématu modulace a kódování (MCS)
- Používá se jako klíčové kritérium pro rozhodování o předání spojení a převýběru buňky
- Podporuje monitorování rádiového spoje a procedury při selhání rádiového spoje
- Umožňuje optimalizaci sítě a benchmarkování výkonu

## Související pojmy

- [BLER – Block Error Rate](/mobilnisite/slovnik/bler/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [RLF – Radio Link Failure](/mobilnisite/slovnik/rlf/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)

## Definující specifikace

- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [DFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dfe/)
