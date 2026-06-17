---
slug: "dl-tdoa"
url: "/mobilnisite/slovnik/dl-tdoa/"
type: "slovnik"
title: "DL-TDOA – Downlink Time Difference Of Arrival"
date: 2025-01-01
abbr: "DL-TDOA"
fullName: "Downlink Time Difference Of Arrival"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dl-tdoa/"
summary: "Metoda lokalizace založená na síti, při které UE měří rozdíl v časech příchodu signálů z více synchronizovaných gNB. UE hlásí tato měření Reference Signal Time Difference (RSTD) síti, která polohu UE"
---

DL-TDOA je metoda lokalizace v 5G NR, při které UE měří rozdíl v časech příchodu (TDOA) downlinkových signálů z více gNB a hlásí tato měření síti pro výpočet polohy.

## Popis

Downlink Time Difference Of Arrival (DL-TDOA) je metoda lokalizace standardizovaná v 3GPP pro sítě LTE a 5G NR. Při této metodě uživatelské zařízení (UE) měří rozdíl v časech příchodu mezi lokalizačními referenčními signály (např. PRS v NR, PRS nebo [CRS](/mobilnisite/slovnik/crs/) v LTE) přijatými z více sousedních základnových stanic (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) a referenční buňky. Tato naměřená veličina se nazývá Reference Signal Time Difference (RSTD). UE hlásí tato RSTD měření síti, konkrétně funkci Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G core síti. LMF, která zná přesné zeměpisné souřadnice a časové vztahy zapojených základnových stanic, používá algoritmy multilaterace k výpočtu polohy UE. Základním principem je, že každé RSTD měření definuje hyperbolickou linii polohy; průsečík více takových hyperbol z různých párů základnových stanic určuje polohu UE.

Z architektonického hlediska provoz DL-TDOA zahrnuje několik síťových prvků. LMF řídí lokalizační relaci: vybírá referenční a sousední buňky pro měření, konfiguruje vysílání downlinkových lokalizačních referenčních signálů ([DL-PRS](/mobilnisite/slovnik/dl-prs/) v NR) a žádá UE prostřednictvím LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) o provedení RSTD měření. Zapojené gNB musí mít synchronizovaný čas vysílání, čehož se obvykle dosahuje pomocí [GNSS](/mobilnisite/slovnik/gnss/) (např. [GPS](/mobilnisite/slovnik/gps/)) nebo síťových synchronizačních protokolů jako [IEEE](/mobilnisite/slovnik/ieee/) 1588v2 (PTP). Fyzická vrstva UE provádí přesná měření času příchodu na nakonfigurovaných DL-PRS signálech. Mezi klíčové komponenty patří měřicí procedura (filtrace, průměrování), hlášení RSTD s přidruženou metrikou kvality a výpočetní engine pro lokalizaci v LMF, který řeší hyperbolické rovnice, často s využitím metody nejmenších čtverců pro zpracování chyb měření.

V celém pracovním postupu LMF zahájí proceduru LPP Provide Assistance Data, aby odeslala UE potřebné informace: seznam buněk, jejich DL-PRS konfigurace a očekávané vyhledávací okno pro RSTD. UE následně provádí měření během určených lokalizačních okamžiků a hlásí hodnoty RSTD zpět v LPP Provide Location Information zprávě. LMF může také používat NR Positioning Protocol A (NRPPa) ke shromažďování časových a konfiguračních dat od gNB prostřednictvím AMF a NG-RAN. Úlohou DL-TDOA je poskytnout škálovatelnou metodu lokalizace řízenou sítí, která využívá stávající downlinkovou infrastrukturu, nevyžaduje specificky pro lokalizaci žádné uplinkové přenosy od UE, a je proto vhodná pro širokou škálu zařízení a nabízí dobrou rovnováhu mezi přesností, latencí a dopadem na síť.

## K čemu slouží

DL-TDOA byl standardizován, aby poskytl vysoce přesné síťové řešení lokalizace, které vylepšuje schopnosti dřívějších buněčných technologií jako Cell-ID a OTDOA v LTE. Předchozí metody často trpěly omezenou přesností (desítky až stovky metrů), citlivostí na mnohocestné šíření a podmínky bez přímé viditelnosti a vysokou latencí. Tato omezení byla zvláště patrná pro služby tísňového volání (E911/E112), kde je přesná poloha kritická, a pro nové komerční aplikace jako sledování majetku, navigace a služby založené na poloze, které vyžadují přesnost na úrovni metrů.

Vytvoření a vylepšení DL-TDOA v 5G NR (od Release 16 dále) bylo motivováno potřebou splnit přísné požadavky na lokalizaci pro nové vertikály, jako je průmyslový IoT, autonomní systémy a rozšířená realita. Řeší problém určení polohy zařízení bez spoléhání se výhradně na satelitní systémy (GNSS), které jsou nedostupné nebo nespolehlivé v interiérech a městských kaňonech. DL-TDOA využívá husté nasazení buněčných základnových stanic a kvalitní vyhrazené DL-PRS signály k dosažení mnohem lepšího rozlišení času příchodu. Historicky je jeho vývoj součástí širšího úsilí 3GPP učinit z 5G jednotnou platformu nejen pro komunikaci, ale také pro snímání a lokalizaci, a tyto schopnosti nativně integrovat do návrhu rádiové přístupové sítě.

## Klíčové vlastnosti

- UE měří Reference Signal Time Difference (RSTD) mezi signály z více synchronizovaných gNB
- Spoléhá se na vysoce přesné downlinkové referenční signály, jako je DL-PRS, pro přesný odhad času příchodu
- Výpočet založený na síti prováděný funkcí Location Management Function (LMF) pomocí multilaterace
- Vyžaduje těsnou časovou synchronizaci (např. prostřednictvím GNSS nebo PTP) mezi zúčastněnými vysílacími body
- End-to-end konfigurováno a řízeno pomocí LTE Positioning Protocol (LPP) mezi UE a LMF
- Poskytuje přesnost lokalizace na úrovni metrů, zejména se signály širokého pásma a dobrou geometrií

## Související pojmy

- [DL-PRS – Downlink Positioning Reference Signal](/mobilnisite/slovnik/dl-prs/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.855** (Rel-16) — Study on NR Positioning Support
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [DL-TDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dl-tdoa/)
