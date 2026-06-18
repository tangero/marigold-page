---
slug: "mbno"
url: "/mobilnisite/slovnik/mbno/"
type: "slovnik"
title: "MBNO – Mobile Broadcast/Multicast Network Operator"
date: 2025-01-01
abbr: "MBNO"
fullName: "Mobile Broadcast/Multicast Network Operator"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mbno/"
summary: "Obchodní a provozní role definovaná pro subjekty, které poskytují vysílací nebo skupinové vysílací služby přes mobilní síť. MBNO spravuje nabídku služeb, získávání obsahu a případně BM-SC, ale může sp"
---

MBNO je role mobilního operátora pro subjekt, který poskytuje a spravuje vysílací (broadcast) nebo skupinové vysílací (multicast) služby včetně obsahu a BM-SC, často využívající rádiovou a jádrovou infrastrukturu jiného operátora.

## Popis

Mobile Broadcast/Multicast Network Operator (MBNO) je logická a komerční role definovaná v rámci servisního modelu 3GPP pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Není to konkrétní síťový uzel nebo protokol, ale spíše administrativní subjekt odpovědný za poskytování vysílacích a/nebo skupinových vysílacích služeb koncovým uživatelům. MBNO má obchodní vztah s koncovým uživatelem pro službu MBMS a je odpovědné za celkové poskytování služby, její správu a případně fakturaci.

Z hlediska síťové architektury MBNO typicky provozuje nebo řídí Broadcast Multicast-Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)). BM-SC je vstupní bod pro obsah do systému MBMS a zajišťuje funkce jako oznámení služby, plánování, šifrování obsahu (správa klíčů) a iniciaci relací přenosu MBMS. MBNO je tedy subjekt, který rozhoduje o tom, jaký obsah se vysílá, kdy se vysílá a v jakých geografických oblastech (oblasti služby MBMS). Rozhraní má k poskytovatelům obsahu nebo jím samo může být.

MBNO může, ale nemusí vlastnit podkladovou infrastrukturu rádiového přístupu a jádrové sítě. To vede k běžným provozním modelům: kombinovaný scénář, kdy Mobile Network Operator ([MNO](/mobilnisite/slovnik/mno/)) zároveň vystupuje jako MBNO a využívá vlastní síť; nebo oddělený scénář, kdy je MBNO poskytovatel služeb, který si pronajímá kapacitu od jednoho nebo více MNO (která vlastní rádiové spektrum a infrastrukturu). V odděleném scénáři MBNO vyjednává s MNO o využití rádiových a přenosových zdrojů pro doručení svých relací MBMS do cílové oblasti služby. Technická realizace zahrnuje připojení BM-SC od MBNO k MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a jádrové síti MNO přes standardizovaná rozhraní.

Koncept MBNO je klíčový pro vytvoření konkurenčního a flexibilního ekosystému pro vysílací/skupinové vysílací služby. Umožňuje specializovaným poskytovatelům služeb (např. mediálním společnostem) nabízet mobilní [TV](/mobilnisite/slovnik/tv/) nebo rozsáhlou distribuci software, aniž by museli být plnohodnotným mobilním operátorem. Specifikace 3GPP, zejména v servisních požadavcích (TS 22.146), definují nezbytné schopnosti a rozhraní pro podporu tohoto oddělení poskytování služeb od provozování sítě, zajišťující interoperabilitu mezi MBNO a jedním nebo více MNO.

## K čemu slouží

Role MBNO byla definována, aby podpořila inovace a konkurenci na trhu mobilních vysílacích a skupinových vysílacích služeb. Před jejím formálním zavedením se často předpokládalo, že pouze tradiční Mobile Network Operator ([MNO](/mobilnisite/slovnik/mno/)) může takové služby nabízet, protože kontroloval síťovou infrastrukturu. To mohlo omezovat rozmanitost dostupného obsahu a obchodních modelů. Vytvoření konceptu MBNO to řeší oddělením role poskytovatele služeb od role síťového operátora.

Toto oddělení řeší několik problémů. Umožňuje specialistům na obsah (např. vysílatelům, mediálním domům) vstoupit na mobilní trh bez obrovských kapitálových výdajů potřebných pro licencované spektrum a celostátní nasazení sítě. Umožňuje MNO generovat velkoobchodní příjmy prodejem vysílací síťové kapacity více MBNO. Dále umožňuje MBNO potenciálně agregovat publikum napříč sítěmi více MNO, čímž dosáhne větší celkové uživatelské základny, než kterou může poskytnout jakýkoli jednotlivý MNO. Tento model byl zvláště důležitý pro ekonomickou životaschopnost služeb jako mobilní [TV](/mobilnisite/slovnik/tv/), protože otevřel dveře partnerství mezi telekomunikačními operátory a mediálními společnostmi.

## Klíčové vlastnosti

- Definuje komerční subjekt odpovědný za nabídku služby MBMS a vztah s uživatelem
- Typicky vlastní nebo provozuje síťovou funkci BM-SC
- Určuje obsah služby, plánování a cílové oblasti služby
- Může fungovat nezávisle na vlastníkovi podkladové rádiové přístupové sítě (MNO)
- Umožňuje velkoobchodní obchodní modely pro vysílací/skupinovou vysílací kapacitu
- Umožňuje vstup poskytovatelů obsahu na trh mobilního vysílání

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MNO – Mobile Network Operator](/mobilnisite/slovnik/mno/)

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [MBNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbno/)
