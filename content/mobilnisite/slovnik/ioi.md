---
slug: "ioi"
url: "/mobilnisite/slovnik/ioi/"
type: "slovnik"
title: "IOI – Inter Operator Identification"
date: 2025-01-01
abbr: "IOI"
fullName: "Inter Operator Identification"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ioi/"
summary: "IOI je globálně jednoznačný identifikátor používaný v sítích 3GPP k rozlišení různých poskytovatelů služeb nebo síťových operátorů zapojených do komunikační relace. Je nezbytný pro směrování, účtování"
---

IOI je globálně jednoznačný identifikátor používaný v sítích 3GPP k rozlišení různých poskytovatelů služeb nebo síťových operátorů zapojených do komunikační relace.

## Popis

Inter Operator Identification (IOI, identifikace mezi operátory) je klíčový identifikátor v architektuře 3GPP, konkrétně definovaný pro použití v IP Multimedia Subsystem (IMS) a dalších protokolech jádra sítě. Slouží jako token, který jednoznačně identifikuje síťového operátora nebo poskytovatele služeb spojeného s konkrétní relací nebo transakcí. IOI je přenášen v rámci zpráv SIP (Session Initiation Protocol), zejména v hlavičce P-Charging-Vector, a v rozhraních pro účtování založených na protokolu Diameter. Jeho primární funkcí je umožnit síťovým prvkům rozpoznat, kteří operátoři jsou zapojeni do poskytování služby od konce ke konci, což je zásadní pro zpracování v prostředí s více operátory.

Z architektonického hlediska je IOI generován IMS uzlem výchozí sítě, jako je Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) nebo Serving-CSCF (S-CSCF), při zahájení relace. Poté je zahrnut do příslušných signalizačních zpráv, jak relace prochází různými sítěmi. Identifikátor obvykle následuje strukturovaný formát, často založený na doménovém jménu operátora nebo globálně přiděleném kódu, což zajišťuje jeho globální jednoznačnost. Když signalizace relace dorazí do cílové sítě, přijímající IMS uzly mohou IOI zkontrolovat a identifikovat výchozího operátora. Tento mechanismus funguje ve spolupráci s funkcemi účtování, kde se IOI používá ke korelaci záznamů o účtování vygenerovaných v různých sítích pro stejnou servisní relaci.

Klíčové komponenty využívající IOI zahrnují jádro IMS (P-CSCF, S-CSCF, [I-CSCF](/mobilnisite/slovnik/i-cscf/)), funkci Policy and Charging Rules Function (PCRF) a offline/online systémy účtování ([OFCS](/mobilnisite/slovnik/ofcs/)/[OCS](/mobilnisite/slovnik/ocs/)). V architektuře účtování je IOI klíčovým polem v Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) nebo v Diameter Accounting Requests ([ACR](/mobilnisite/slovnik/acr/)). Umožňuje fakturačním systémům přesně přiřadit náklady a výnosy mezi operátory podle jejich obchodních dohod. IOI také hraje roli při vynucování servisních politik, protože ty se mohou lišit v závislosti na zapojených operátorech (např. pro roamující uživatele).

Jeho role přesahuje základní identifikaci; je základním kamenem pro vypořádání mezi operátory, detekci podvodů a zajištění služeb. Ve složitých servisních řetězcích zahrnujících více poskytovatelů (např. IMS hovor, který prochází přes přístupového poskytovatele, tranzitního poskytovatele a ukončovacího poskytovatele) pomáhá řetězec IOI rekonstruovat cestu služby. Identifikátor musí být generován a přenášen bezpečně, aby se zabránilo falšování, protože má přímý dopad na finanční vypořádání. Specifikace jako TS 29.165 (Inter-IMS Network to Network Interface) a TS 24.229 (IP multimedia call control protocol) podrobně popisují jeho syntaxi a použití v protokolech.

## K čemu slouží

IOI byl vytvořen k vyřešení základního problému identifikace poskytovatelů služeb v decentralizovaném, více-dodavatelském a více-operátorském telekomunikačním světě založeném na IP. Před IMS a plně IP sítěmi používala tradiční telefonie přepojování okruhů, kde byla identifikace operátora implicitní v síťové hierarchii a skupinách spojů. Přechod na paketově přepínané multimediální služby založené na SIP tento implicitní model zrušil, což si vyžádalo explicitní, standardizovaný identifikátor pro sledování zapojení operátorů pro komerční a provozní účely.

Primární motivací bylo umožnit životaschopné obchodní modely pro IMS služby, jako je Voice over LTE (VoLTE) a Rich Communication Services (RCS). Aby operátoři mohli nabízet bezproblémový roaming a služby propojení sítí, potřebují spolehlivý způsob, jak se vzájemně identifikovat pro účtování, směrování a správu podvodů. IOI toto poskytuje tím, že je povinným prvkem v rámci účtování a signalizace. Řeší omezení dřívějších systémů IP komunikace, kterým chyběl standardizovaný identifikátor operátora, což mohlo vést k fakturačním sporům a složitým procesům vypořádání.

Historicky se jeho zavedení ve verzi Release 5 časově shodovalo s prvními kompletními specifikacemi IMS. Položilo základy pro meziodběratelské IMS sítě (ION). Jak se služby rozvíjely a zahrnovaly videohovory, zasílání zpráv a scénáře s více zařízeními, ukázal se mechanismus IOI jako nezbytný pro globální škálování těchto služeb. Podporuje nejen bilaterální dohody, ale také složité více-stranové řetězce poskytování služeb, běžné v dnešních cloudových komunikačních ekosystémech. Bez IOI by byla komerční interoperabilita moderních IP komunikačních služeb mezi konkurenčními operátory výrazně omezena.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor pro síťové operátory a poskytovatele služeb
- Přenášen v SIP signalizaci v hlavičce P-Charging-Vector
- Používán v rozhraních pro účtování Diameter (např. Ro, Rf) pro korelaci
- Nezbytný pro meziodběratelské fakturační a vypořádací procesy
- Podporuje rozhodování o směrování a politikách v IMS relacích s více operátory
- Umožňuje detekci podvodů a zajištění služeb přes hranice sítí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [IOI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ioi/)
