---
slug: "ipdl-otdoa"
url: "/mobilnisite/slovnik/ipdl-otdoa/"
type: "slovnik"
title: "IPDL-OTDOA – Idle Period Downlink - Observed Time Difference Of Arrival"
date: 2025-01-01
abbr: "IPDL-OTDOA"
fullName: "Idle Period Downlink - Observed Time Difference Of Arrival"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ipdl-otdoa/"
summary: "Specifická aplikace techniky IPDL pro vylepšení metody určování polohy OTDOA v sítích UMTS. Jedná se o síťově asistovanou lokalizační službu, kde síť vytváří downlinkové nečinné periody, aby umožnila"
---

IPDL-OTDOA je síťově asistovaná metoda určování polohy v UMTS, při níž síť vytváří downlinkové (sestupné) nečinné periody, aby umožnila přesná měření signálů sousedních buněk prováděná UE pro výpočet zeměpisné polohy.

## Popis

IPDL-OTDOA není samostatná technologie, ale specifický případ použití a vylepšení standardní metody určování polohy [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival), umožněné technikou [IPDL](/mobilnisite/slovnik/ipdl/) (Idle Period Downlink). Definována v rámci architektury lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP představuje provozní režim, ve kterém se určování polohy OTDOA provádí s asistencí IPDL za účelem překonání problému slyšitelnosti (hearability) vlastního systému WCDMA. Služba zahrnuje koordinované akce mezi uživatelským zařízením (UE), rádiovou přístupovou sítí (RAN – Node B a RNC) a lokalizačním serverem jádra sítě (Serving Mobile Location Centre – SMLC).

Proces začíná, když klient lokalizační služby (např. záchranná služba nebo komerční aplikace) požaduje polohu cílového UE. Požadavek je směrován přes jádro sítě k SMLC. SMLC, která zná obsluhující buňku UE, vybere vhodnou metodu určování polohy. Pokud je zvolena OTDOA a síť podporuje IPDL, SMLC zahájí IPDL-OTDOA relaci. SMLC odešle požadavek na určení polohy k RNC řídícímu obsluhující buňku UE. RNC následně nakonfiguruje obsluhující Node B tak, aby aktivoval IPDL, a definuje parametry pro tiché periody. Současně RNC prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) instruuje UE, aby během těchto nečinných period provedlo měření referenčního časového rozdílu (RTD).

Během nakonfigurovaných IPDL mezer přijímač UE měří čas příjmu primárního synchronizačního kanálu (P-Sch) z vlastní obsluhující buňky a z alespoň dvou sousedních buněk. UE vypočítá pozorované časové rozdíly ([OTD](/mobilnisite/slovnik/otd/)) mezi těmito příchody. Tato surová měření nebo vypočtené OTD jsou nahlášeny zpět RNC. RNC tyto údaje přepošle SMLC. SMLC také disponuje znalostí skutečných časových rozdílů (RTD) mezi zúčastněnými Node B (které jsou buď známé v synchronních sítích, nebo měřeny jednotkami [LMU](/mobilnisite/slovnik/lmu/) – Location Measurement Units). Pomocí měření OTD a dat RTD SMLC provede výpočty hyperbolické trilaterace pro odhad polohy UE.

Klíčovým aspektem IPDL-OTDOA je bezproblémová integrace fyzikálního mechanismu IPDL do protokolu určování polohy OTDOA na vyšší vrstvě. Tím transformuje OTDOA z potenciálně nespolehlivé metody na robustní, standardizovanou lokalizační službu pro UMTS. Služba je charakteristická svým síťově asistovaným charakterem; měření provádí UE, ale síť řídí prostředí (prostřednictvím IPDL) a provádí konečný výpočet polohy. Tato architektura vyvažuje požadavky na přesnost s komplexitou UE a životností baterie, což z ní činilo životaschopné řešení určování polohy pro masový trh před všudypřítomností integrovaných přijímačů [GNSS](/mobilnisite/slovnik/gnss/) v telefonech.

## K čemu slouží

IPDL-OTDOA byla standardizována, aby uspokojila rostoucí poptávku po přesném, síťově založeném určování polohy mobilních zařízení v sítích 3G UMTS, poháněnou jak regulačními, tak komerčními požadavky. Předpisy jako [FCC](/mobilnisite/slovnik/fcc/) E911 ve Spojených státech a směrnice E112 v Evropě ukládaly mobilním sítím povinnost poskytovat stále přesnější informace o poloze pro tísňová volání. Zatímco Cell-ID poskytoval hrubou polohu a Assisted-GPS (A-GPS) nabízel vysokou přesnost, A-GPS vyžadoval specifický hardwar UE a často selhával v interiérech. Existovala jasná potřeba spolehlivé, síťově založené metody, která by mohla poskytovat střední přesnost (např. 50–150 metrů) bez závislosti na satelitech nebo speciálních schopnostech UE.

Základní metoda OTDOA, jak byla koncipována pro GSM a rané UMTS, byla zásadně limitována CDMA povahou WCDMA. Silný signál obsluhující buňky maskoval slabší signály sousedních buněk, což znemožňovalo měření. IPDL-OTDOA přímo řešila tento technický problém. Tím, že se obsluhující buňka na okamžik odmlčela, vytvořila nezbytné podmínky pro fungování OTDOA. Tím byl vyřešen hlavní problém, který bránil síťově založené trilateraci v UMTS.

Její zavedení v Release 10 (jak je formálně odkazováno v požadavcích na služby TS 22.071) konsolidovalo dřívější práci na IPDL a OTDOA do definované servisní schopnosti. Představovala vyzrání určování polohy v UMTS a poskytovala operátorům standardizovaný, interoperabilní nástroj pro služby založené na poloze, plánování sítě, optimalizaci a regulační shodu. IPDL-OTDOA zajistila, že sítě UMTS mohly nabízet komplexní portfolio metod určování polohy, zaplňující klíčovou mezeru mezi nízkopřesným Cell-ID a vysokopřesným, na UE závislým A-GPS.

## Klíčové vlastnosti

- Vylepšuje standardní OTDOA integrací techniky IPDL pro zajištění slyšitelnosti sousedních buněk
- Poskytuje síťově asistované, na UE založené určování polohy s lepší přesností než Cell-ID
- Funguje v rámci standardizované architektury lokalizačních služeb (LCS) UMTS
- Vyžaduje koordinaci mezi SMLC, RNC, Node B a UE
- Poskytuje odhady polohy vhodné pro tísňové služby a komerční LBS
- Funguje nezávisle na satelitních signálech, poskytuje schopnost určování polohy v interiérech

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1

---

📖 **Anglický originál a plná specifikace:** [IPDL-OTDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipdl-otdoa/)
