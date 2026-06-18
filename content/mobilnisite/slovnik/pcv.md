---
slug: "pcv"
url: "/mobilnisite/slovnik/pcv/"
type: "slovnik"
title: "PCV – Phase Center Variation"
date: 2025-01-01
abbr: "PCV"
fullName: "Phase Center Variation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pcv/"
summary: "Phase Center Variation (PCV, variace fázového středu) označuje odchylku efektivního fázového středu antény od jejího geometrického středu, která se mění s úhlem příchodu/odchodu signálu. V 3GPP se jed"
---

PCV je odchylka efektivního fázového středu antény od jejího geometrického středu, která se mění v závislosti na úhlu signálu a musí být korigována pro přesné určování polohy v LTE a 5G NR.

## Popis

Phase Center Variation (PCV, variace fázového středu) je jev a kalibrovaný parametr spojený s rádiovými anténami, zvláště relevantní pro vysoce přesné určování polohy v celulárních sítích. Fázový střed antény je virtuální bod, ze kterého se zdánlivě šíří elektromagnetické záření. U ideální antény by tento bod byl pevný a shodoval by se s fyzickým geometrickým středem antény. U reálných antén se však efektivní fázový střed posouvá v závislosti na směru (azimut a elevace) příchozího nebo odchozího rádiového signálu. Tato směrová závislost je právě Phase Center Variation. Způsobuje systematickou chybu v měřené fázi signálu, která se přímo přenáší na chybu měření vzdálenosti u metod určování polohy využívajících měření fáze nosné, jako je Real-Time Kinematic ([RTK](/mobilnisite/slovnik/rtk/)) nebo Precise Point Positioning ([PPP](/mobilnisite/slovnik/ppp/)).

V kontextu 3GPP je PCV řešeno ve specifikacích pro lokalizační protokoly LTE (36.305) a NR (38.305), zejména pro LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR Positioning Protocol A (NRPPa). Když User Equipment (UE) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) vypočítává polohu pomocí signálů z více základnových stanic ([eNB](/mobilnisite/slovnik/enb/)/gNB), měří fázi nosného signálu. PCV vysílací antény základnové stanice i přijímací antény UE zavádí do těchto fázových měření úhlově závislý posuv. Pokud není korigován, tento posuv snižuje přesnost určení polohy, potenciálně z chyb na úrovni centimetrů na chyby v řádu metrů.

Pro zmírnění tohoto efektu standardy 3GPP definují mechanismy pro korekci PCV. Operátoři sítí mohou charakterizovat antény svých základnových stanic a vytvořit tak korekční data PCV. Tato data, která mapují hodnoty fázové korekce na úhly příchodu/odchodu, mohou být následně poskytnuta UE pomocí asistenčních dat v LPP/NRPPa zprávách. UE následně aplikuje tyto korekce na svá nezpracovaná měření fáze nosné před provedením výpočtu polohy. Specifikace podrobně popisují formát a poskytování těchto informací specifických pro anténu, což umožňuje interoperabilitu mezi sítěmi a zařízeními od různých výrobců. Řízení PCV je zvláště klíčové pro pokročilé případy užití 5G vyžadující ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a vysoce přesné určování polohy pro průmyslový IoT, autonomní vozidla a rozšířenou realitu.

## K čemu slouží

Korekce PCV byla zavedena do standardů 3GPP za účelem podpory náročných požadavků na přesnost nových lokalizačních služeb v LTE-A a 5G NR. Tradiční metody určování polohy v celulárních sítích, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) využívající měření kódové fáze, nabízely přesnost v řádu desítek metrů. Aplikace jako navigace vozidel, řízení dronů a chytrá výroba však vyžadují přesnost na úrovni decimetrů nebo dokonce centimetrů, kterou lze dosáhnout pouze pomocí technik založených na fázi nosné. Hlavní překážkou této vysoké přesnosti je systematická chyba způsobená nedokonalostmi antén, primárně kvantifikovaná jako PCV.

Motivací pro standardizaci zpracování PCV bylo odstranění klíčového zdroje chyby, který byl dříve specifický pro výrobce a nebyl zohledňován ve výpočtech polohy. Bez standardizovaných korekčních dat by bylo určování polohy založené na fázi nosné nespolehlivé napříč různými nasazeními sítí a typy zařízení. Definováním způsobu charakterizace a sdělování korekcí PCV umožňuje 3GPP konzistentní, vysoce přesné určování polohy nezávislé na použitém hardwaru. Tím se řeší omezení předchozích přístupů, kdy byly chyby způsobené anténami buď ignorovány (což omezovalo přesnost), nebo vyžadovaly proprietární, neinteroperabilní řešení. Jedná se o základní prvek umožňující přesné lokalizační funkce, které jsou pilířem podpory vertikálních odvětví v 5G.

## Klíčové vlastnosti

- Parametr charakterizace antény: Kvantifikuje směrovou odchylku efektivního fázového středu antény od jejího geometrického referenčního bodu.
- Korekce chyb fáze nosné: Poskytuje kalibrační data pro korekci systematických posuvů v měřeních fáze nosné používaných pro vysoce přesné určování polohy.
- Standardizovaná asistenční data: Definovaný formát v protokolech LPP a NRPPa umožňuje sítím doručovat UEs korekce PCV antén základnových stanic.
- Modelování závislé na úhlu: Korekční hodnoty jsou typicky poskytovány jako funkce azimutu a elevace vůči anténě.
- Kritické pro přesnost na úrovni centimetrů: Umožňuje technikám založeným na fázi nosné, jako je RTK a PPP, dosáhnout plného potenciálu v celulárních sítích.
- Hardwarově agnostické určování polohy: Umožňuje, aby vysoce přesné určování polohy fungovalo konzistentně napříč různými implementacemi antén a UE od různých výrobců.

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [PCV na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcv/)
