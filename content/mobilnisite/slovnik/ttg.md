---
slug: "ttg"
url: "/mobilnisite/slovnik/ttg/"
type: "slovnik"
title: "TTG – Transmit/receive Transition Gap"
date: 2015-01-01
abbr: "TTG"
fullName: "Transmit/receive Transition Gap"
category: "Physical Layer"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ttg/"
summary: "Ochranná perioda v rádiových rámcích s duplexním dělením času (TDD), která odděluje downlinkový (DL) přenosový podrámec od následujícího uplinkového (UL) přijímacího podrámce. Umožňuje rádiovému hardw"
---

TTG je ochranná perioda v TDD rádiovém rámci, která odděluje downlinkový přenosový podrámec od následujícího uplinkového přijímacího podrámce a umožňuje základnové stanici přepnout z režimu vysílání do režimu příjmu.

## Popis

Transmit/receive Transition Gap (TTG, přechodová mezera mezi vysíláním a příjmem) je klíčový časovací parametr v [TDD](/mobilnisite/slovnik/tdd/) buňkových systémech, jako jsou ty definované v [UTRA](/mobilnisite/slovnik/utra/) TDD ([TD-SCDMA](/mobilnisite/slovnik/td-scdma/)) a LTE/5G NR TDD módech 3GPP. Jedná se o ochrannou periodu nečinnosti vloženou mezi poslední symbol downlinkového ([DL](/mobilnisite/slovnik/dl/)) podrámce a první symbol následujícího uplinkového ([UL](/mobilnisite/slovnik/ul/)) podrámce ve stejné kmitočtové nosné. Primární funkcí TTG na fyzické vrstvě je poskytnout základnové stanici (NodeB, eNodeB, gNB) dostatek času na vypnutí výkonového zesilovače vysílače a přeconfiguraci rádiového předkoncového stupně pro režim příjmu.

Tento přechod není okamžitý kvůli hardwarovým omezením. Výkonový zesilovač ([PA](/mobilnisite/slovnik/pa/)) potřebuje čas na snížení výstupního výkonu, aby během uplinkové periody nevysílal šum nebo parazitní signály do příjmového pásma. Současně musí být aktivován a ustálen přijímací řetězec včetně šumových zesilovačů ([LNA](/mobilnisite/slovnik/lna/)) a filtrů. Doba trvání TTG, měřená v mikrosekundách nebo periodách symbolů, je pečlivě vypočítána tak, aby zahrnovala součet zpoždění vypnutí vysílače, zpoždění zapnutí přijímače a rádiového šířicího zpoždění k nejvzdálenějšímu uživatelskému zařízení (UE) v pokrytí buňky. Tato poslední složka zajišťuje, že základnová stanice je plně připravena přijímat před příchodem prvního uplinkového signálu od vzdáleného UE.

Z pohledu návrhu systému je TTG spárována s podobnou ochrannou periodou zvanou Receive/transmit Transition Gap (RTG), která se vyskytuje mezi uplinkovým podrámcem a následujícím downlinkovým podrámcem. Délky TTG a RTG jsou definovány v systémové struktuře rámce a vysílány jako část systémové informace buňky. UE tuto informaci používají k synchronizaci vlastního přepínání vysílání/příjmu. V LTE a NR jsou tyto mezery součástí konfigurace speciálního podrámce v TDD, kde speciální podrámec obsahuje Downlink Pilot Time Slot (DwPTS), Guard Period ([GP](/mobilnisite/slovnik/gp/), ochrannou periodu) a Uplink Pilot Time Slot (UpPTS). GP v této struktuře slouží jako kombinovaná funkce TTG a RTG.

Hodnota TTG přímo ovlivňuje maximální poloměr buňky. Delší TTG umožňuje větší velikost buňky, protože akomoduje větší obousměrná šířicí zpoždění, ale také představuje režii, která snižuje dostupný čas pro přenos dat v rámci rámce, a tím ovlivňuje spektrální účinnost. Plánování sítě proto zahrnuje výběr vhodné hodnoty TTG na základě zamýšlené velikosti buňky a požadované rovnováhy mezi pokrytím a kapacitou.

## K čemu slouží

TTG bylo vytvořeno k řešení základního problému vlastního TDD rádiovému provozu na jediném kmitočtu: zabránění interferenci vlastního silného vysílaného signálu základnové stanice s jejím citlivým přijímačem při přepínání mezi režimy vysílání a příjmu. Bez dostatečné ochranné periody by zbytkový výstup vysílače a přechodové jevy při přepínání zcela přehlušily slabé příchozí signály od vzdálených UE, což by znemožnilo uplinkový příjem – problém známý jako vlastní interference nebo izolace Tx-Rx.

V raných TDD systémech byly hardwarové doby přepínání relativně pomalé, což vyžadovalo významné ochranné periody. Standardizace TTG v rámci 3GPP poskytla jasný, univerzální rámec pro správu tohoto přechodu. Definovala předvídatelnou časovou strukturu, kterou musí dodržovat všechny kompatibilní základnové stanice a UE, čímž zajišťuje interoperabilitu. To bylo zvláště důležité pro UTRA TDD a později pro LTE TDD, které umožnily flexibilní a asymetrické DL/UL alokace odpovídající charakteru provozu.

TTG spolu s RTG je klíčovým prvkem umožňujícím praktické nasazení TDD sítí. Řeší omezení rádiového hardwaru tím, že poskytuje potřebný 'ustalovací čas'. Jeho návrh odráží kompromis: minimalizace mezery pro zlepšení spektrální účinnosti versus její maximalizace pro podporu větších buněk a robustnějšího provozu. Vývoj rádiového hardwaru s rychlejšími přepínacími schopnostmi umožnil v průběhu času zkracovat doby trvání těchto mezer, čímž se zlepšila celková účinnost systému při zachování základní funkce izolace vysílacích a přijímacích operací.

## Klíčové vlastnosti

- Ochranná perioda mezi downlinkovými a uplinkovými podrámci v TDD provozu
- Umožňuje základnové stanici vypnout vysílač a zapnout přijímač
- Doba trvání zohledňuje hardwarová přepínací zpoždění a maximální šířicí zpoždění v buňce
- Definována v systémové struktuře rámce a vysílána v systémové informaci
- Ovlivňuje maximální poloměr buňky: delší TTG podporuje větší buňky
- Představuje režii, která kompromisně směňuje spektrální účinnost za provozní proveditelnost

## Definující specifikace

- **TS 28.601** (Rel-12) — Telecom management; CN and non-3GPP access NRM IRP Requirements
- **TS 32.252** (Rel-12) — 3GPP WLAN Interworking Charging
- **TS 36.938** (Rel-9) — E-UTRAN to 3GPP2/Mobile WiMAX Mobility

---

📖 **Anglický originál a plná specifikace:** [TTG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttg/)
