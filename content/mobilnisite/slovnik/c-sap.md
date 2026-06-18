---
slug: "c-sap"
url: "/mobilnisite/slovnik/c-sap/"
type: "slovnik"
title: "C-SAP – Control Service Access Point"
date: 2025-01-01
abbr: "C-SAP"
fullName: "Control Service Access Point"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/c-sap/"
summary: "Control Service Access Point (C-SAP) je logické rozhraní definované v podsložce Radio Link Control (RLC) protokolového zásobníku UTRAN. Poskytuje standardizovaný přístupový bod pro vyšší vrstvu (RRC)"
---

C-SAP je logické rozhraní v podsložce RLC sítě UTRAN, které vrstvě RRC poskytuje standardizovaný přístupový bod pro výměnu řídicích informací a zajišťuje oddělení funkcí řídicí a uživatelské roviny.

## Popis

Control Service Access Point (C-SAP) je základní architektonický koncept v protokolové architektuře 3GPP Universal Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně definovaný pro podsložku Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)). Funguje jako logický přístupový bod služby (Service Access Point), což je konceptuální místo, kde jedna protokolová vrstva (vrstva RLC) poskytuje službu vyšší vrstvě (vrstvě Radio Resource Control neboli [RRC](/mobilnisite/slovnik/rrc/)). C-SAP je jedním z několika [SAP](/mobilnisite/slovnik/sap/) definovaných pro vrstvu RLC, dalšími jsou například Data Service Access Point (D-SAP) pro uživatelská data a Broadcast/Multicast Control Service Access Point (BMC-SAP). Toto logické rozdělení je klíčové pro zachování čistého oddělení mezi řídicí signalizací a provozem uživatelských dat, což je základní princip vrstevnatých komunikačních systémů.

Z architektonického hlediska se vrstva RLC nachází jak v uživatelském zařízení (UE), tak v radiovém síťovém řadiči ([RNC](/mobilnisite/slovnik/rnc/)). C-SAP poskytuje rozhraní, přes které může vrstva RRC, zodpovědná za veškerou signalizaci řídicí roviny související se správou radiových prostředků, přistupovat ke službám vrstvy RLC. Když vrstva RRC potřebuje odeslat řídicí zprávu (např. zprávu Radio Bearer Setup, příkaz k předání spojení nebo hlášení o měřeních), předá tuto zprávu vrstvě RLC prostřednictvím C-SAP. Vrstva RLC pak tuto zprávu zpracuje podle svého nakonfigurovaného režimu – typicky Acknowledged Mode ([AM](/mobilnisite/slovnik/am/)) pro kritickou signalizaci, aby zajistila doručení. Toto zpracování zahrnuje segmentaci, konkatenaci a v režimu AM opravu chyb prostřednictvím mechanismů Automatic Repeat Request ([ARQ](/mobilnisite/slovnik/arq/)). Zpracované RLC Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)) jsou následně předány do podkladové vrstvy Medium Access Control (MAC) pro přenos přes rozhraní vzdušného rozhraní.

Fungování C-SAP se řídí sadou primitiv definovaných ve specifikacích 3GPP (TS 25.322 pro RLC, přičemž definice SAP jsou často odkazovány v přidružených specifikacích jako 25.323 a 25.324). Tato primitiva, například RLC-AM-DATA-REQ (request) a RLC-AM-DATA-IND (indication), definují přesný formát a parametry pro výměnu informací mezi vrstvami RRC a RLC. Klíčové parametry zahrnují identitu logického kanálu, samotnou RLC Service Data Unit (SDU) a různé stavové indikátory. C-SAP zajišťuje, že signalizace řídicí roviny těží ze spolehlivých služeb doručení v pořadí vrstvy RLC, což je nezbytné pro udržení stability sítě, provádění předání spojení a efektivní správu radiových přenosových kanálů. Bez tohoto dobře definovaného přístupového bodu by interakce mezi řídicí a spojovou vrstvou byla ad-hoc, což by vedlo k potenciálním problémům s interoperabilitou a snížené spolehlivosti systému.

V celkové síti hraje C-SAP tichou, ale kritickou roli. Je součástí zásobníku protokolů řídicí roviny, který končí v RNC. Spolehlivostní mechanismy (jako ARQ) aplikované na provoz přes C-SAP jsou klíčové pro robustní výměnu RRC zpráv, které následně řídí zřizování, rekonfiguraci a uvolňování radiových přenosových kanálů. To přímo ovlivňuje úspěšnost nastavování hovorů, výkon předání spojení a celkovou kvalitu služeb pro koncové uživatele. Zatímco koncept SAP je abstraktní, jeho implementace v hardwaru a softwaru zajišťuje, že řídicí signalizace je zpracovávána s odpovídající prioritou a zárukami spolehlivosti, čímž se odlišuje od provozu uživatelských dat s doručením podle možností (best-effort), který může využívat D-SAP s režimem Unacknowledged Mode (UM) nebo Transparent Mode (TM).

## K čemu slouží

Control Service Access Point (C-SAP) byl zaveden za účelem formalizace a standardizace interakce mezi vrstvou Radio Resource Control (RRC) a vrstvou Radio Link Control (RLC) v architektuře 3GPP UTRAN definované od Release 99. Před takovými formálními vrstevnatými architekturami mohly být interakce řídicí a datové roviny těsně propojené nebo špatně definované, což vedlo ke složitým, monolitickým softwarovým návrhům, které bylo obtížné udržovat, upgradovat nebo standardizovat napříč různými výrobci zařízení. C-SAP jako součást komplexního vrstevnatého protokolového modelu to řeší tím, že poskytuje jasné, specifikací definované rozhraní. To umožňuje vrstvě RRC (zabývající se síťovým řízením) požadovat konkrétní, spolehlivé služby přenosu dat od vrstvy RLC (zabývající se spolehlivostí na úrovni spoje) bez nutnosti rozumět vnitřním mechanismům RLC.

Primární problém, který řeší, je zajištění spolehlivého doručování pro kritickou signalizaci řídicí roviny. V mobilní síti musí být zprávy pro předání spojení, nastavení radiového přenosového kanálu a vysílání systémových informací doručeny přesně a v pořadí, aby se předešlo přerušením hovorů nebo selháním spojení. C-SAP umožňuje RRC využívat Acknowledged Mode vrstvy RLC, který zahrnuje detekci chyb a opakovaný přenos (ARQ). Definováním tohoto bodu jako přístupového bodu služby specifikace 3GPP zajišťují, že všechna kompatibilní UE a RNC implementují tuto řídicí cestu konzistentně. Tato interoperabilita je základní pro vícevýrobcový ekosystém celulárních sítí.

Historicky je koncept Service Access Points zakořeněn v modelu Open Systems Interconnection (OSI), který protokolové zásobníky 3GPP silně využívají. Vytvoření C-SAP speciálně pro vrstvu RLC UTRAN v Release 4 (a jeho pokračující přítomnost v pozdějších releasech) odráží zrání protokolového návrhu 3GPP s důrazem na modularitu a jasné oddělení funkcí. Řešilo to omezení spočívající v tom, že řídicí signalizace byla závislá na potenciálně méně spolehlivých mechanismech nebo proprietárních rozhraních, čímž se zvýšila robustnost a spravovatelnost řídicí roviny radiové sítě 3G UMTS.

## Klíčové vlastnosti

- Poskytuje standardizované logické rozhraní pro výměnu řídicích informací mezi RRC a RLC
- Umožňuje přístup k režimu Acknowledged Mode (AM) vrstvy RLC pro zaručené doručování signalizačních zpráv v pořadí
- Používá definovaná primitiva (např. DATA-REQ, DATA-IND) s konkrétními parametry pro komunikaci mezi vrstvami
- Zajišťuje oddělení provozu řídicí roviny a uživatelské roviny v rámci podsložky RLC
- Podporuje kritické síťové procedury jako předání spojení, správu radiových přenosových kanálů a hlášení měření
- Usnadňuje interoperabilitu mezi UE a RNC od různých výrobců díky dodržování specifikací

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol

---

📖 **Anglický originál a plná specifikace:** [C-SAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-sap/)
