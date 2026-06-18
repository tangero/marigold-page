---
slug: "pstn"
url: "/mobilnisite/slovnik/pstn/"
type: "slovnik"
title: "PSTN – Public Switched Telecommunications Network"
date: 2025-01-01
abbr: "PSTN"
fullName: "Public Switched Telecommunications Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pstn/"
summary: "Globální telefonní síť s komutací okruhů poskytující tradiční hlasové telefonní služby. V 3GPP představuje legacy síť, s níž se mobilní systémy propojují za účelem zajištění globální hlasové konektivi"
---

PSTN je globální telefonní síť s komutací okruhů, která poskytuje tradiční hlasové telefonní služby a slouží jako legacy síť, s níž se mobilní systémy propojují.

## Popis

Veřejná telefonní síť (PSTN) je celosvětový agregát telefonních sítí s komutací okruhů, které primárně provozují národní a regionální operátoři. Je charakteristická využitím vyhrazených fyzických okruhů (nebo virtuálních okruhů je emulujících) po dobu trvání hovoru a používá signalizační systémy jako [SS7](/mobilnisite/slovnik/ss7/) (Signaling System No. 7) pro sestavení, směrování a správu hovorů. V rámci architektury 3GPP není PSTN sítí definovanou 3GPP, ale externí sítí, s níž musí systémy 3GPP spolupracovat. Prvky jádrové sítě (CN), konkrétně ústředna mobilní komunikace ([MSC](/mobilnisite/slovnik/msc/)) v jádru s komutací okruhů ([CS](/mobilnisite/slovnik/cs/)) a později subsystém IP multimédií (IMS) v jádru s komutací paketů ([PS](/mobilnisite/slovnik/ps/)), poskytují bránovou funkcionalitu pro připojení mobilních účastníků k účastníkům PSTN.

Vzájemné propojení je dosaženo prostřednictvím definovaných referenčních bodů a protokolů. Pro tradiční CS hlas se MSC připojuje k PSTN přes rozhraní založené na [TDM](/mobilnisite/slovnik/tdm/), často s využitím signalizace [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) přes SS7. MSC provádí potřebnou konverzi protokolů mezi signalizací specifickou pro mobilní sítě (jako [BSSAP](/mobilnisite/slovnik/bssap/)) a signalizací PSTN. S vývojem směrem k plně IP sítím a Voice over LTE (VoLTE) se bod propojení s PSTN přesouvá do IMS. Zde zajišťují vzájemné propojení funkce řízení mediální brány (MGCF) a mediální brána (MGW) v rámci IMS. MGCF překládá mezi protokolem SIP (Session Initiation Protocol) používaným v IMS a signalizací ISUP/BICC používanou směrem k PSTN, zatímco MGW konvertuje mediální proud mezi paketově orientovaným RTP/UDP/IP používaným v PS doméně a formáty s komutací okruhů TDM nebo paketizovanými hlasovými formáty (jako G.711) používanými na straně PSTN.

Z pohledu služeb představuje PSTN konečný cíl mnoha hlasových hovorů pocházejících z mobilní sítě. Zajištění bezproblémové interoperability s PSTN je základním požadavkem pro jakoukoli komerční mobilní síť, protože umožňuje účastníkům volat na jakýkoli pevný telefon na světě. Specifikace 3GPP toto vzájemné propojení podrobně pokrývají, detailně popisují scénáře pro směrování hovorů, překlad čísel (s využitím čísel E.164), vzájemné propojení doplňkových služeb (jako přesměrování hovorů, zákazy) a směrování tísňových služeb. PSTN také slouží jako model a záložní řešení pro některé telefonní služby v rámci samotné mobilní sítě, zejména před plným nasazením IMS.

## K čemu slouží

PSTN existovala dlouho před buněčnými sítěmi. Primárním účelem definice vzájemného propojení s PSTN ve standardech 3GPP bylo zajistit, aby se nové digitální mobilní systémy (GSM, UMTS, LTE) mohly od prvního dne integrovat do globálního telekomunikačního ekosystému. Bez standardizovaného vzájemného propojení by mobilní sítě byly izolovanými ostrovy. Řešeným problémem byla univerzální konektivita: umožnit mobilnímu účastníkovi volat na jakýkoli pevný telefon a naopak. Toto byl nekompromisní komerční požadavek pro úspěch 2G GSM.

Historicky byly počáteční architektury 3GPP (GSM, UMTS) postaveny s jádrem s komutací okruhů, které odráželo mnoho principů PSTN, což činilo vzájemné propojení relativně přímočarým prostřednictvím standardizovaných TDM rozhraní a signalizace SS7. Jak se sítě 3GPP vyvíjely směrem k paketově orientovaným plně IP architekturám s LTE, objevila se nová výzva: jak zachovat tuto bezproblémovou konektivitu s PSTN, když je nativní přenosová technologie mobilní sítě paketově orientovaná IP a jádrová síť se vzdaluje od prvků s komutací okruhů. To motivovalo vývoj řešení založených na IMS, jako je VoLTE a mechanismus předání SRVCC (Single Radio Voice Call Continuity). IMS se svými MGCF a MGW poskytlo standardizovanou, budoucím vývoji odolnou IP bránu k legacy PSTN, což zajišťovalo kontinuitu služeb při modernizaci síťové infrastruktury. Specifikace pro vzájemné propojení s PSTN se tak vyvinuly z přímého propojení TDM trunků k sofistikované IP signalizaci a konverzi médií.

## Klíčové vlastnosti

- Globální síť s komutací okruhů pro hlasovou telefonii
- Používá číslovací plán E.164 pro adresování účastníků
- Spoléhá na signalizaci SS7 pro řízení hovorů a služby
- Propojuje se se sítěmi 3GPP přes MSC (CS jádro) nebo MGCF/MGW (IMS)
- Poskytuje referenční model pro základní telefonní služby
- Slouží jako primární síť pro směrování tísňových služeb v mnoha regionech

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TR 22.925** (Rel-4) — UMTS QoS and Network Performance Parameters
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- … a dalších 91 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pstn/)
