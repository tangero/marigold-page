---
slug: "meo"
url: "/mobilnisite/slovnik/meo/"
type: "slovnik"
title: "MEO – Medium-Earth Orbiting satellites"
date: 2026-01-01
abbr: "MEO"
fullName: "Medium-Earth Orbiting satellites"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/meo/"
summary: "MEO označuje satelity operující na střední oběžné dráze (Medium Earth Orbit), typicky ve výškách mezi 2 000 a 35 786 km. V rámci 3GPP jsou klíčovou součástí Neterestriálních sítí (NTN) a poskytují pro"
---

MEO je typ satelitu operujícího na střední oběžné dráze (Medium Earth Orbit), který slouží jako klíčová součást 3GPP Neterestriálních sítí (Non-Terrestrial Networks) a poskytuje ve srovnání s GEO satelity širší pokrytí a nižší latenci pro globální konektivitu.

## Popis

Satelity na střední oběžné dráze (Medium-Earth Orbiting, MEO) jsou kritickým prvkem v architektuře Neterestriálních sítí ([NTN](/mobilnisite/slovnik/ntn/)) podle 3GPP, navrženým k rozšíření služeb 5G a budoucích celulárních sítí po celém světě. Operují na drahách v rozsahu přibližně od 2 000 kilometrů až po oblast těsně pod geostacionárním pásem ve výšce 35 786 kilometrů. Tato oběžná výška představuje strategický kompromis, který nabízí výrazně širší oblast pokrytí na jeden satelit ve srovnání s konstelacemi na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)), a zároveň poskytuje mnohem nižší signálovou latenci a snížený útlum na dráze ve srovnání s geostacionárními satelity ([GEO](/mobilnisite/slovnik/geo/)). V rámci systému 3GPP jsou MEO satelity integrovány jako transparentní („bent-pipe“) nebo regenerativní (s palubním zpracováním) užitečné zatížení. Jako transparentní užitečné zatížení jednoduše zesilují a převádějí frekvence mezi pozemní stanicí brány (známou jako NTN Gateway) a uživatelským zařízením (UE). Regenerativní užitečná zatížení, která jsou složitější, dokážou signály na palubě demodulovat, dekódovat, přepínat a znovu kódovat, čímž efektivně fungují jako základnové stanice na obloze (gNodeB).

Integrace MEO satelitů do 3GPP rádiové přístupové sítě (RAN) vyžaduje specifické úpravy pro zvládnutí jedinečných charakteristik satelitních spojů. Mezi klíčové technické výzvy řešené ve specifikacích patří velmi dlouhé šířkové zpoždění (v rozsahu od desítek do přes sto milisekund), vysoké Dopplerovy posuvy způsobené pohybem satelitu vůči zemi a významný útlum na dráze. Protokoly 3GPP RAN a jádra sítě jsou vylepšeny, aby tyto podmínky podporovaly. Například jsou upraveny postupy časového předstihu (timing advance), procesy hybridního automatického opakovaného dotazu ([HARQ](/mobilnisite/slovnik/harq/)) jsou přizpůsobeny nebo deaktivovány pro scénáře s velmi dlouhým zpožděním a je upraveno plánování. Jádro sítě, prostřednictvím funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), musí být také informováno o charakteristikách obsluhujícího satelitu pro správnou správu mobility a relací, zejména při předávání UE mezi satelitními paprsky nebo mezi satelity.

MEO satelity hrají klíčovou roli při dosahování skutečně globální a bezproblémové konektivity. Jsou základní technologií pro 5G NTN, umožňují kontinuitu služeb pro pozemní sítě a poskytují služby přímo do zařízení nebo přenosové služby (backhaul). Z architektonického hlediska se připojují k pozemním NTN Gateway, které následně komunikují se standardní 5G jádrovou sítí (5GC). To umožňuje MEO konstelacím poskytovat služby definované 3GPP, jako je rozšířené mobilní širokopásmové připojení (eMBB) a masivní IoT (mIoT), v regionech bez pozemní infrastruktury. Specifikace pokrývající MEO zahrnují požadavky na služby (řada 22), systémovou architekturu (řada 23), protokoly (řady 24, 25, 36, 38) a správu (řady 28, 32), čímž zajišťují komplexní rámec pro satelitně integrované celulární sítě.

## K čemu slouží

Standardizace MEO satelitů v rámci 3GPP byla motivována potřebou rozšířit vysoce kvalitní mobilní širokopásmové a IoT služby do neobsluhovaných a nedostatečně obsluhovaných regionů po celém světě. Tradiční pozemní sítě je ekonomicky náročné nasazovat v odlehlých oblastech, nad oceány a v letovém prostoru. Před formální integrací 3GPP existovala satelitní komunikace jako samostatný, často proprietární ekosystém s omezenou interoperabilitou s celulárními zařízeními a službami. Účelem definice MEO ve standardech 3GPP je překlenout tuto mezeru a vytvořit jednotnou síťovou architekturu, kde jsou satelity nativní, integrovanou součástí, nikoli externím doplňkem.

Tato integrace řeší kritické problémy pokrytí, odolnosti a kontinuity služeb. Řeší problém nedostatečného pokrytí tím, že poskytuje škálovatelné řešení pro globální konektivitu, které je nezbytné pro aplikace jako námořní a letecká komunikace, reakce na katastrofy a venkovský širokopásmový přístup. Dále zvyšuje odolnost sítě tím, že poskytuje alternativní přenosovou vrstvu (backhaul) nebo přístupovou vrstvu při výpadcích pozemních sítí způsobených přírodními katastrofami. Z pohledu služeb umožňuje bezproblémovou mobilitu uživatelům pohybujícím se mezi oblastmi s pozemním a satelitním pokrytím, což je koncept zásadní pro vizi 3GPP všudypřítomné konektivity.

Vytváření standardů pro MEO bylo historicky poháněno konvergencí satelitního a telekomunikačního průmyslu a vypuštěním nových MEO konstelací (jako O3b a jeho nástupci). 3GPP Release 15 zahájilo seriózní studium Neterestriálních sítí, přičemž následující releasy upřesňovaly architekturu a protokoly. Specifické orbitální charakteristiky MEO nabídly životaschopný střední průběh pro raná nasazení 5G [NTN](/mobilnisite/slovnik/ntn/), vyvažujíce velikost konstelace (počet potřebných satelitů) vůči latenci a složitosti pozemních stanic, což z nich činí strategicky důležitou součást celkového portfolia NTN definovaného 3GPP.

## Klíčové vlastnosti

- Operuje na oběžných drahách ve výškách mezi 2 000 km a 35 786 km
- Funguje jako transparentní („bent-pipe“) nebo regenerativní (s palubním zpracováním) užitečné zatížení v rámci NTN
- Integrován s 5G jádrovou sítí prostřednictvím NTN Gateway a standardních rozhraní N2/N3
- Vyžaduje úpravy v protokolech RAN pro dlouhé zpoždění, Dopplerův jev a správu mobility
- Poskytuje rozsáhlé pokrytí na jeden satelit, čímž snižuje celkový počet potřebných satelitů ve srovnání s LEO pro globální službu
- Umožňuje služby jako eMBB a IoT v odlehlých, námořních a leteckých prostředích

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [LEO – Low-Earth Orbiting satellites](/mobilnisite/slovnik/leo/)
- [GEO – Geostationary satellite Earth Orbit](/mobilnisite/slovnik/geo/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 22.887** (Rel-20) — Study on satellite access - Phase 4
- **TS 23.008** (Rel-19) — Organization of Subscriber Data
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [MEO na 3GPP Explorer](https://3gpp-explorer.com/glossary/meo/)
