---
slug: "srs"
url: "/mobilnisite/slovnik/srs/"
type: "slovnik"
title: "SRS – Space Radiocommunication Stations"
date: 2026-01-01
abbr: "SRS"
fullName: "Space Radiocommunication Stations"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srs/"
summary: "SRS označuje pozemní stanice nebo satelitní užitečná zatížení, které poskytují rádiové komunikační služby z vesmíru. Jsou klíčové pro satelitní sítě 3GPP, umožňují globální pokrytí, přenosovou kapacit"
---

SRS je pozemní stanice nebo satelitní užitečné zatížení, které poskytuje rádiové komunikační služby z vesmíru pro satelitní sítě 3GPP, umožňující globální pokrytí, přenosovou kapacitu (backhaul) a služby přímo do zařízení.

## Popis

Vesmírné rádiokomunikační stanice (SRS) jsou základním prvkem ve standardizaci nepozemských sítí ([NTN](/mobilnisite/slovnik/ntn/)) v 3GPP. SRS může být satelitní užitečné zatížení (např. průchozí transpondér nebo regenerativní procesor) nebo pozemní bránová stanice komunikující se satelity. V architektuře tvoří SRS vesmírné nebo pozemní rádiové rozhraní pro uživatelské zařízení (UE) nebo síťové uzly jako gNB. U průchozího užitečného zatížení (bent-pipe) SRS přijímá, zesiluje, převádí frekvenci a retransmituje signál mezi UE a pozemní bránou. U regenerativního užitečného zatížení SRS zahrnuje palubní zpracování pro demodulaci/dekódování a následnou remodulaci/rekódování signálu, čímž v podstatě funguje jako základnová stanice ve vesmíru.

Provoz SRS je definován přísnými parametry rádiového vysílání a příjmu, aby se vyrovnal s jedinečnými výzvami satelitních spojů. Mezi ně patří velmi dlouhé přenosové zpoždění (až stovky milisekund), vysoké Dopplerovy posuny způsobené pohybem satelitu a výrazný útlum na trase. Specifikace 3GPP podrobně popisují požadovaný výkon SRS z hlediska maximálního výstupního výkonu, frekvenční stability, nežádoucích emisí a citlivosti přijímače. SRS musí podporovat konkrétní tvary vln a šířky kanálů definované 3GPP, přizpůsobující pozemská rozhraní NR nebo LTE pro šíření ve vesmírném prostředí.

Klíčové součásti systému SRS zahrnují anténní subsystém (často s natáč[ec](/mobilnisite/slovnik/ece-c/)ími nebo vícevýkonovými anténami pro tvarování pokrytí), vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) předzesilovač pro zesílení a převod a digitální zpracovatelskou jednotku. U regenerativních užitečných zatížení to zahrnuje moduly pro zpracování základního pásma ekvivalentní funkcím gNB. Úlohou SRS je rozšířit rádiovou přístupovou síť (RAN) 3GPP do vesmíru, poskytovat kontinuitu služeb, všudypřítomné pokrytí a přenosovou konektivitu v odlehlých oblastech, nad oceány a pro letecká vozidla. Je to klíčový uzel umožňující přímou komunikaci mezi standardními UE 3GPP a satelity, jak je standardizováno od Release 15 pro 5G NTN.

## K čemu slouží

Standardizace vesmírných rádiokomunikačních stanic (SRS) v rámci 3GPP byla motivována rostoucí potřebou bezproblémové integrace satelitních sítí s pozemskými mobilními sítěmi. Historicky satelitní komunikace fungovala v proprietárních izolovaných systémech používajících ne-3GPP technologie, které bránily interoperabilitě s miliardami existujících mobilních zařízení. To vytvářelo mezery v pokrytí ve venkovských, námořních a leteckých scénářích, kde je pozemská infrastruktura ekonomicky neproveditelná. Účelem definice SRS je přivést satelity do ekosystému 3GPP jako standardizované rádiové uzly, což umožní globální a bezproblémové pokrytí službami.

Vytvořením technických specifikací pro SRS řeší 3GPP omezení předchozích fragmentovaných přístupů. Umožňuje operátorům mobilních sítí začlenit satelitní aktiva do svých sítí pomocí standardizovaných rozhraní a protokolů. To řeší kritické problémy, jako je zajištění odolnosti při katastrofách, kdy pozemské sítě selžou, umožnění služeb internetu věcí (IoT) na rozsáhlých geografických oblastech a podpora konektivity pro pohyblivé platformy, jako jsou lodě a letadla. Definice SRS zajišťují, že satelitní sítě mohou splňovat stejná očekávání kvality služeb, zabezpečení a správy mobility jako pozemské sítě 5G, což usnadňuje vizi skutečně všudypřítomné konektivity.

## Klíčové vlastnosti

- Podpora jak průchozích (bent-pipe), tak regenerativních (s palubním zpracováním) architektur užitečného zatížení
- Adaptace rádiových rozhraní 3GPP NR a LTE pro satelitní kanály s velkým zpožděním a vysokým Dopplerovým jevem
- Definice přísných požadavků na RF výkon (např. výstupní výkon, frekvenční stabilita, nežádoucí emise)
- Umožnění globálního pokrytí včetně polárních oblastí prostřednictvím satelitních svazků
- Podpora provozu pro spojovací článek (gateway-to-satellite) a služební článek (satellite-to-UE)
- Integrace s jádrem sítě 5G pro správu služeb a mobility end-to-end

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 36.111** (Rel-19) — LMU Requirements for UTDOA Positioning
- **TS 36.112** (Rel-19) — E-UTRAN LMU Conformance Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- … a dalších 31 specifikací

---

📖 **Anglický originál a plná specifikace:** [SRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/srs/)
