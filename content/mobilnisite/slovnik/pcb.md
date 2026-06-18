---
slug: "pcb"
url: "/mobilnisite/slovnik/pcb/"
type: "slovnik"
title: "PCB – Protocol Control Byte"
date: 2025-01-01
abbr: "PCB"
fullName: "Protocol Control Byte"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pcb/"
summary: "PCB je řídicí bajt používaný v některých protokolech 3GPP, konkrétně v GSM/EDGE Radio Access Network (GERAN) pro přenos dat. Spravuje stav protokolu, synchronizaci rámců a řízení chyb v rámcích vrstvy"
---

PCB (Protocol Control Byte) je řídicí bajt protokolu používaný v protokolech 3GPP GERAN pro správu stavu protokolu, synchronizace rámců a řízení chyb v rámcích vrstvy datového spoje za účelem spolehlivé komunikace po rádiovém rozhraní.

## Popis

Protocol Control Byte (PCB) je základní součástí protokolů vrstvy datového spoje v systémech GSM a [EDGE](/mobilnisite/slovnik/edge/), jak je specifikováno v technických specifikacích 3GPP. Jedná se o 8bitové pole vestavěné v hlavičce datových rámců, například těch používaných v protokolech Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro paketový datový provoz. Primární úlohou PCB je přenos řídicích informací nezbytných pro správu vysílání a příjmu datových bloků mezi sítí a uživatelským zařízením (UE). To zahrnuje označení typů rámců, čísel sekvencí, pollovacích bitů pro vyžádání potvrzení a příznaků řízení opakovaného vysílání, které jsou klíčové pro spolehlivý přenos dat přes náchylné k chybám rádiové rozhraní.

V architektuře paketových datových protokolů [GERAN](/mobilnisite/slovnik/geran/) je PCB součástí struktury RLC/MAC bloku používaného na [PDTCH](/mobilnisite/slovnik/pdtch/) (Packet Data Traffic Channel). Každý RLC/MAC blok se skládá z hlavičky (obsahující PCB a další pole) a datové části. Bity PCB jsou detailně definovány pro podporu různých funkcí: například rozlišuje mezi datovými a řídicími bloky, nese Temporary Flow Identity ([TFI](/mobilnisite/slovnik/tfi/)) pro multiplexování, obsahuje pole Power Reduction (PR) pro řízení výkonu a poskytuje Retry bit pro indikaci opakovaných přenosů. V potvrzovaném režimu obsahuje PCB také Sequence Number ([SN](/mobilnisite/slovnik/sn/)) a Polling (P) bit, který spouští odeslání potvrzení příjemcem. Toto detailní řízení umožňuje efektivní mechanismy [ARQ](/mobilnisite/slovnik/arq/) (Automatic Repeat Request), řízení toku a synchronizaci mezi odesílatelem a příjemcem.

Fungování PCB je nedílnou součástí provozu GPRS a EDGE. Když síť vysílá RLC datový blok k UE, nastaví příslušné bity PCB pro definování kontextu bloku. Příjemce (UE nebo síť) analyzuje PCB, aby pochopil, jak blok zpracovat – zda se jedná o nová data, opakovaný přenos nebo řídicí příkaz. Pollovací mechanismus řízený P bitem zajišťuje, že vysílač může vyžádat potvrzení (ACK/NACK) v klíčových bodech, což mu umožňuje vyprázdnit svůj vysílací buffer nebo zahájit opakované vysílání ztracených bloků. To přispívá ke spolehlivosti vrstvy RLC a zajišťuje integritu dat navzdory změnám rádiového kanálu. Dále PCB podporuje různé režimy RLC: potvrzovaný režim pro spolehlivý přenos (s využitím ARQ) a nepotvrzovaný režim pro streamové služby, kde je kritické zpoždění, ale určitá ztráta je přijatelná.

Mezi klíčové komponenty ovlivněné PCB patří stavové automaty entity RLC, algoritmy plánování MAC a celkový datový výkon a latence. Zapouzdřením řídicích informací do jednoho bajtu minimalizuje PCB režii a zároveň poskytuje robustní řídicí schopnosti. Jeho návrh odráží omezení starších GSM kanálů, kde je šířka pásma omezená a efektivita je prvořadá. Role PCB pokračuje ve vylepšeních EDGE, kde jsou modulační a kódovací schémata (MCS) pokročilejší, ale základní řídicí struktura zůstává zachována pro zachování zpětné kompatibility. Porozumění PCB je klíčové pro inženýry optimalizující datový výkon GERAN, protože jeho nastavení přímo ovlivňuje míru opakovaných přenosů, signalizační zátěž a uživatelský komfort u mobilních datových služeb.

## K čemu slouží

Protocol Control Byte byl vytvořen, aby poskytl kompaktní a efektivní mechanismus pro řídicí signalizaci v pásmu v rámci protokolů RLC/MAC systémů GPRS a EDGE. Před GPRS GSM primárně podporovalo okruhově spínanou řeč a nízkorychlostní data, což nevyžadovalo sofistikované paketově orientované řízení spoje. Zavedení paketově spínaných dat v GSM Phase 2+ (GPRS) si vyžádalo nový protokol vrstvy datového spoje schopný zpracovat pakety proměnné velikosti, obnovu po chybách a multiplexování více uživatelů na sdílených kanálech. PCB řeší problém vložení nezbytných řídicích informací bez nadměrné režie, což je kritické vzhledem k omezené kapacitě rádiových kanálů a potřebě efektivního využití spektra.

Jeho účelem je umožnit spolehlivý přenos dat přes nespolehlivé rádiové rozhraní podporou ARQ, řízení toku a synchronizace. PCB nese klíčové informace, jako jsou čísla sekvencí a pollovací bity, které umožňují příjemci detekovat chybějící bloky a vysílači spravovat opakované přenosy. Tím řeší problém vysoké míry bitových chyb v mobilním prostředí a zajišťuje, že paketové datové služby (jako e-mail a prohlížení webu) jsou doručovány s přijatelnou spolehlivostí. Dále PCB usnadňuje multiplexování prostřednictvím TFI, což umožňuje více UE sdílet stejné fyzické prostředky, což ve srovnání s vyhrazenými kanály zlepšuje kapacitu sítě a efektivitu využití prostředků.

Historicky byl návrh PCB motivován potřebou vyvinout GSM v paketovou datovou síť při současném znovuvyužití stávajících kanálových struktur a minimalizaci změn rádiového rozhraní. Poskytl zpětně kompatibilní způsob zavedení paketově spínaných schopností vedle okruhově spínaných služeb. S vývojem EDGE (Enhanced Data rates for GSM Evolution) byl rámec PCB rozšířen pro podporu vyšších přenosových rychlostí a nových modulačních schémat, což demonstruje jeho flexibilitu. PCB tak sehrál klíčovou roli při umožnění prvních rozšířených zkušeností s mobilním internetem a překlenul propast mezi čistě hlasovými sítěmi a pozdějšími širokopásmovými systémy 3G/4G. Jeho principy lehkého řízení v pásmu ovlivnily následné datové protokoly 3GPP, ačkoli konkrétní implementace se vyvíjely v UMTS a LTE.

## Klíčové vlastnosti

- 8bitové řídicí pole v hlavičkách RLC/MAC bloků pro GERAN paketová data
- Podporuje identifikaci typu rámce (datové vs. řídicí bloky)
- Nese čísla sekvencí pro provoz ARQ v potvrzovaném režimu
- Obsahuje pollovací bit pro vyžádání potvrzení od příjemce
- Kóduje Temporary Flow Identity (TFI) pro multiplexování uživatelů
- Umožňuje řízení opakovaného vysílání a indikátory snížení výkonu

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [PCB na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcb/)
