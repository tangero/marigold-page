---
slug: "saal"
url: "/mobilnisite/slovnik/saal/"
type: "slovnik"
title: "SAAL – Signalling ATM Adaptation Layer"
date: 2025-01-01
abbr: "SAAL"
fullName: "Signalling ATM Adaptation Layer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/saal/"
summary: "Soubor protokolů adaptační vrstvy ATM (AAL), konkrétně AAL5 a funkce specifické koordinace služeb (SSCF) a spojově orientovaného protokolu specifického pro služby (SSCOP), používaný k přenosu signaliz"
---

SAAL je Signalizační adaptační vrstva ATM, soubor protokolů používaných k přenosu signalizačních zpráv pro rozhraní jako Iu a Iub přes ATM sítě.

## Popis

Signalizační adaptační vrstva [ATM](/mobilnisite/slovnik/atm/) (SAAL) označuje zásobník protokolů používaný k adaptaci zpráv signalizační roviny pro spolehlivý přenos přes síť asynchronního přenosového režimu (ATM). V kontextu 3GPP byl SAAL primárně používán v pozemní rádiové přístupové síti UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) pro rozhraní Iu (RNC-CN), Iur (RNC-RNC) a Iub (RNC-Node B) od vydání 99 až po vydání 7. SAAL není jediný protokol, ale kombinace adaptační vrstvy ATM typu 5 ([AAL5](/mobilnisite/slovnik/aal5/)) spolu s vyššími vrstvami specifickými pro službu, definovanými [ITU-T](/mobilnisite/slovnik/itu-t/) pro signalizaci: funkce specifické koordinace služeb ([SSCF](/mobilnisite/slovnik/sscf/)) a spojově orientovaný protokol specifický pro služby ([SSCOP](/mobilnisite/slovnik/sscop/)).

SAAL funguje tak, že segmentuje signalizační zprávy z protokolů vyšších vrstev (jako je Radio Access Network Application Part - [RANAP](/mobilnisite/slovnik/ranap/) na Iu, nebo Node B Application Part - [NBAP](/mobilnisite/slovnik/nbap/) na Iub) do ATM buněk. AAL5 provádí segmentaci a opětovné složení (SAR) proměnně dlouhých protokolových datových jednotek (PDU) do 48bajtového užitečného zatížení ATM buněk a přidává zápatí pro detekci chyb. Samotná AAL5 však poskytuje pouze nezajištěnou, spojově orientovanou službu. Pro signalizaci, která vyžaduje garantované doručení a zachování pořadí, jsou nad AAL5 přidány vrstvy SSCF a SSCOP. SSCOP zajišťuje spolehlivý přenos dat přes ATM spojení. Zahrnuje mechanismy pro číslování sekvencí, opravu chyb selektivním retransmisí, řízení toku a udržování spojení. Vrstva SSCF funguje jako adaptační vrstva mezi SSCOP a konkrétním signalizačním uživatelem (např. MTP3-B pro broadbandovou signalizaci nebo přímo adaptací specifickou pro 3GPP).

V architektuře UTRAN tvořil SAAL vrstvu datového spoje pro řídicí rovinu. Například na rozhraní Iu-CS mezi řadičem rádiové sítě (RNC) a jádrem s přepojováním okruhů (MSC) byly zprávy RANAP přenášeny přes SAAL/ATM spojení. SAAL spojení bylo navázáno přes trvalý virtuální okruh (PVC) nebo komutovaný virtuální okruh (SVC) nakonfigurovaný mezi koncovými body. To poskytovalo spolehlivý signalizační kanál s zachováním pořadí, který byl nezávislý na provozu v uživatelské rovině, jež také používala ATM, ale s jinými typy AAL (jako AAL2 pro hlas). Použití ATM a SAAL bylo charakteristickým rysem raných 3G sítí, které nabízely vysokou efektivitu využití šířky pásma a diferenciaci kvality služby (QoS) prostřednictvím možností správy provozu ATM.

## K čemu slouží

SAAL byl vytvořen, aby splnil přísné požadavky na spolehlivost telekomunikační signalizace přes nově se objevující vysokorychlostní, buňkovou transportní technologii ATM. Tradiční signalizační systémy založené na TDM, jako je signalizační systém č. 7 (SS7), používaly vrstvy přenosové části zpráv (MTP) přes vyhrazené časové sloty. Když se sítě v 90. letech přesouvaly k broadbandovému ISDN (B-ISDN) a infrastruktuře založené na ATM, byla potřeba nová adaptační metoda pro přenos signalizačních zpráv se srovnatelnou spolehlivostí. SAAL, standardizovaný ITU-T, tuto mezeru zaplnil tím, že poskytoval spojově orientovanou službu s opravou chyb nad inherentně spojově orientovanou, ale potenciálně ztrátovou vrstvou ATM.

Pro 3GPP UMTS byl SAAL přijat, aby využil výhod ATM v přístupové síti. ATM nabízelo statistické multiplexování, efektivní využití šířky pásma pro přerušovaná data a vestavěné třídy QoS – výhody oproti čistému TDM pro smíšený provoz raných 3G. SAAL poskytoval důvěryhodnou, spolehlivou transportní vrstvu potřebnou pro kritickou řídicí signalizaci mezi síťovými prvky (RNC, Node B, MSC, SGSN). Vyřešil problém, jak provozovat komplexní, transakčně orientované signalizační protokoly jako RANAP a NBAP přes rychlou paketovou síť, aniž by byla ohrožena robustnost očekávaná od telekomunikačních sítí. Sloužil jako přechodová technologie, která umožnila funkčně bohatou architekturu UTRAN až do celoodvětvového přechodu na čistě IP transport v pozdějších vydáních 3GPP.

## Klíčové vlastnosti

- Skládá se z AAL5, funkce specifické koordinace služeb (SSCF) a spojově orientovaného protokolu specifického pro služby (SSCOP)
- Poskytuje spolehlivé doručování signalizačních zpráv s zachováním pořadí přes virtuální okruhy ATM
- Zahrnuje opravu chyb prostřednictvím selektivní retransmise a ověřování sekvenčních čísel
- Podporuje procedury navázání, údržby a uvolnění spojení
- Používá se jako vrstva datového spoje pro řídicí rovinu rozhraní Iu, Iur a Iub v UTRAN
- Umožňuje přenos signalizačních protokolů specifických pro 3GPP (RANAP, RNSAP, NBAP)

## Související pojmy

- [AAL – ATM Adaptation Layer](/mobilnisite/slovnik/aal/)
- [AAL5 – ATM Adaptation Layer type 5](/mobilnisite/slovnik/aal5/)
- [SSCOP – Service Specific Connection Oriented Protocol](/mobilnisite/slovnik/sscop/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling

---

📖 **Anglický originál a plná specifikace:** [SAAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/saal/)
