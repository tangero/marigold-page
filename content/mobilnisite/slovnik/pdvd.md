---
slug: "pdvd"
url: "/mobilnisite/slovnik/pdvd/"
type: "slovnik"
title: "PDVD – Percentage of Degraded Video Duration"
date: 2025-01-01
abbr: "PDVD"
fullName: "Percentage of Degraded Video Duration"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pdvd/"
summary: "Procento doby s degradovaným videem (PDVD) je klíčový ukazatel výkonu (KPI) pro kvalitu videostreamingu. Měří podíl celkové doby přehrávání, během níž koncový uživatel vnímá kvalitu videa jako degrado"
---

PDVD je klíčový ukazatel výkonu (KPI), který měří procento celkové doby přehrávání videa, během níž uživatel vnímá kvalitu videa jako degradovanou.

## Popis

Procento doby s degradovaným videem (PDVD) je standardizovaná metrika 3GPP definovaná v dokumentu TS 26.902 pro hodnocení percepční kvality videostreamingové relace. Kvantifikuje kvalitu uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)) výpočtem procenta celkové doby přehrávání média, během níž je kvalita videa považována za degradovanou. Degradace se typicky určuje porovnáním doručené kvality videa (z hlediska rozlišení, snímkové frekvence nebo datového toku) s předdefinovaným prahem nebo očekávanou úrovní kvality. Metrika se často počítá na straně klienta, uvnitř mediálního přehrávače nebo speciálního měřícího klienta, analýzou událostí jako jsou opětovná načítání bufferu, přepnutí na nižší rozlišení nebo období nízkého datového toku.

Z architektonického hlediska lze měření PDVD integrovat do funkce Media Delivery Function nebo do klientské aplikace. Proces měření zahrnuje kontinuální sledování parametrů přehrávání. Mezi klíčové komponenty patří analytický engine mediálního přehrávače, který sleduje stav přehrávání, a doručovací síť, která ovlivňuje dostupnou propustnost a stabilitu. Hodnoty PDVD se často hlásí zpět do sítě nebo na server analytiky QoE (např. Application Function nebo [NWDAF](/mobilnisite/slovnik/nwdaf/)) pomocí protokolů definovaných ve specifikaci 26.114. Tato zpětná vazba umožňuje potenciální optimalizaci sítě, jako jsou úpravy adaptivního streamování s proměnným datovým tokem nebo změny politik QoS za účelem zlepšení relace.

PDVD funguje ve spojení s dalšími [KPI](/mobilnisite/slovnik/kpi/), jako je počáteční zpoždění před přehráváním, poměr opětovného načítání bufferu a průměrná propustnost, aby poskytlo komplexní pohled na kvalitu uživatelského prožitku (QoE) u videa. Jeho role v síti spočívá v převodu technického výkonu sítě (např. latence, ztráta paketů) na obchodní a uživatelsky orientovanou metriku. Poskytovatelé služeb používají PDVD k benchmarkování výkonu doručování videa, řešení problémů s kvalitou a zajištění souladu se smlouvami o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). Je to kritický nástroj pro řízení zlepšování strategií Content Delivery Network ([CDN](/mobilnisite/slovnik/cdn/)), přidělování rádiových prostředků pro video provoz a vývoj účinnějších videokodeků.

## K čemu slouží

PDVD bylo vytvořeno, aby vyhovělo potřebě standardizované, objektivní a uživatelsky orientované metriky pro hodnocení služeb videostreamingu v mobilních sítích. Když video provoz začal dominovat mobilní spotřebě dat, operátoři a poskytovatelé obsahu potřebovali způsob, jak měřit vnímanou kvalitu nad rámec jednoduché propustnosti sítě nebo míry chyb. Tradiční metriky, jako je ztráta paketů nebo zpoždění, nestačily k zachycení komplexního percepčního dopadu zastavování přehrávání, pixelace nebo kolísání kvality během přehrávání. PDVD tento problém řeší přímým měřením doby trvání špatného uživatelského prožitku.

Historický kontext představuje evoluce služby paketového streamingu ([PSS](/mobilnisite/slovnik/pss/)) a multimediální služby vysílání/multicastu ([MBMS](/mobilnisite/slovnik/mbms/)) 3GPP směrem k dynamickému adaptivnímu streamování přes [HTTP](/mobilnisite/slovnik/http/) (DASH). Dřívější přístupy se spoléhaly na metriky síťové vrstvy, které byly špatně korelované se skutečnou spokojeností uživatelů. PDVD, zavedené v Release 8 jako součást sady metrik QoE, poskytlo společný jazyk pro zajištění služeb. Motivovalo to vývoj inteligentnějších algoritmů adaptivního datového toku a vylepšení síťově asistovaného videostreamingu, což umožnilo síti proaktivně zmírňovat podmínky, které by vedly k vysoké hodnotě PDVD.

## Klíčové vlastnosti

- Standardizovaný KPI QoE pro videoslužby podle 3GPP TS 26.902
- Měří časový aspekt degradace kvality z pohledu uživatele
- Obvykle se počítá na straně klienta na základě událostí přehrávání a úrovní kvality
- Používá se pro monitorování výkonu služby a plnění SLA
- Lze reportovat do sítě pro analytiku a optimalizaci (např. prostřednictvím MDT)
- Spolupracuje s metrikami, jako je poměr opětovného načítání bufferu a průměrný datový tok videa

## Související pojmy

- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MDT – Minimization of Drive Tests](/mobilnisite/slovnik/mdt/)

## Definující specifikace

- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services

---

📖 **Anglický originál a plná specifikace:** [PDVD na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdvd/)
