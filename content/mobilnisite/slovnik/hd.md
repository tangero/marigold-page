---
slug: "hd"
url: "/mobilnisite/slovnik/hd/"
type: "slovnik"
title: "HD – Half-Duplex for Sidelink Operation"
date: 2025-01-01
abbr: "HD"
fullName: "Half-Duplex for Sidelink Operation"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hd/"
summary: "Schopnost zařízení a provozní režim pro sidelink komunikaci, kdy zařízení nemůže na sidelinku současně vysílat a přijímat. Zjednodušuje složitost zařízení a snižuje náklady, což je klíčové pro aplikac"
---

HD je provozní režim a schopnost zařízení pro sidelink, kdy přenos a příjem nemohou probíhat současně, což zjednodušuje složitost a snižuje náklady pro aplikace jako ProSe, V2X a IoT pro veřejnou bezpečnost.

## Popis

Half-Duplex pro Sidelink Operation (HD) označuje rádiovou schopnost definovanou ve specifikacích 3GPP, kde uživatelské zařízení (UE) podporující sidelink komunikaci (např. Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)), Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/))) je schopné v daném okamžiku pouze vysílat nebo přijímat na sidelink nosné, nikoli však obojí současně. To je v protikladu k plně duplexnímu ([FD](/mobilnisite/slovnik/fd/)) provozu, který by vyžadoval pokročilé a nákladné techniky potlačení vlastního rušení. Schopnost HD je základním omezením, které ovlivňuje návrh sidelink protokolu, přidělování zdrojů a mechanismy plánování.

Z architektonického hlediska ovlivňuje HD provoz fyzickou vrstvu a vrstvu řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) sidelink rozhraní. Rádiové frekvenční ([RF](/mobilnisite/slovnik/rf/)) řetězce a řetězce základního pásma UE jsou navrženy pro jeden směr najednou. To vyžaduje časové dělení mezi vysílacími a přijímacími sloty. V režimu 2 (autonomní výběr zdrojů UE), definovaném pro V2X a pozdější vylepšení sidelink, musí UE zahrnovat proceduru snímání (sensing). Během snímání UE naslouchá sidelink kanálu, aby identifikovalo zdroje používané jinými UE. Kvůli omezením HD, když UE vysílá vlastní data, nemůže současně snímání provádět, což vytváří období „hluchoty“, které musí být zohledněno v algoritmech výběru zdrojů, aby se předešlo trvalým kolizím.

Z pohledu sítě, když je přidělování sidelink zdrojů plánováno sítí (režim 1 pro V2X, režim 3 pro LTE sidelink), musí základnová stanice (eNodeB nebo gNB) znát HD omezení UE. Plánovací povolení musí zajistit, že UE není naplánována k příjmu a vysílání v překrývajících se časech, pokud není použito pokročilé koordinace nebo prostorového oddělení. Specifikace, zejména v TS 36.101 a 38.101 pro RF požadavky, definují konkrétní požadavky na výkon HD UE pro nežádoucí emise, citlivost přijímače a časy přepínání mezi vysílacím a přijímacím stavem. Tyto požadavky zajišťují, že i při HD provozu je možná spolehlivá a nízkolatenční sidelink komunikace pro kritické služby jako autonomní řízení a veřejná bezpečnost.

## K čemu slouží

HD sidelink provoz byl standardizován primárně za účelem umožnění nízkonákladových, energeticky účinných implementací zařízení pro přímou komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)). Původním impulzem byly služby Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) v Release 12/13 pro veřejnou bezpečnost a komerční objevování. Implementace plně duplexních rádií vyžaduje složité a drahé obvody pro zvládnutí obrovského vlastního rušení způsobeného tím, že vlastní vysílač zařízení přehluší jeho blízký přijímač. Pro hromadně vyráběné IoT senzory, nositelnou elektroniku a dokonce i vozidla jsou tyto náklady a složitost nepřijatelné.

HD provoz tento problém řeší tím, že přijímá omezení nesimultánního vysílání/příjmu, což je běžná vlastnost mnoha nízkonákladových bezdrátových systémů (jako WiFi). Výzvou pro 3GPP bylo navrhnout sidelink protokol v rámci tohoto omezení, který stále splňuje přísné požadavky na spolehlivost a latenci, zejména pro pozdější [V2X](/mobilnisite/slovnik/v2x/) aplikace. Specifikace musely definovat nové fyzické kanály (PSCCH, PSSCH), synchronizační signály (PSSS/SSSS, S-PSS/S-SSS) a režimy přidělování zdrojů, které efektivně fungují s HD UE. Toto návrhové rozhodnutí bylo klíčové pro rozšířené přijetí sidelink technologie založené na 3GPP, což umožnilo její vestavbu do široké škály zařízení bez nutnosti průlomového a drahého RF hardwaru.

## Klíčové vlastnosti

- Schopnost UE indikující nemožnost současného sidelink vysílání a příjmu
- Ukládá časové dělení multiplexu pro vysílací a přijímací operace
- Ovlivňuje přesnost snímání (sensing) při autonomním výběru zdrojů (režim 2/4) kvůli obdobím hluchoty
- Ovlivňuje rozhodnutí síťového plánování v režimech plánovaného přidělování zdrojů (režim 1/3)
- Definované RF požadavky na dobu přepínání vysílání/příjmu a související výkon
- Umožňuje významné snížení nákladů, složitosti a spotřeby energie UE

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TR 23.764** (Rel-17) — Study on V2X Application Layer Enhancements
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.925** (Rel-19) — Media Traffic Characteristics for 3GPP Networks
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [HD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hd/)
