---
slug: "cr"
url: "/mobilnisite/slovnik/cr/"
type: "slovnik"
title: "CR – Conformance Requirement"
date: 2025-01-01
abbr: "CR"
fullName: "Conformance Requirement"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cr/"
summary: "CR označuje formální specifikace a testovací kritéria, která zajišťují soulad telekomunikačního zařízení a softwaru se standardy 3GPP. Jde o základní mechanismus pro zaručení interoperability, spolehl"
---

CR (Conformance Requirement) je formální specifikace a testovací kritéria, která zajišťují, že telekomunikační zařízení a software jsou v souladu se standardy 3GPP pro interoperabilitu, spolehlivost a konzistentní výkon.

## Popis

Conformance Requirement (CR) v 3GPP je formální dokument, který definuje konkrétní soubor technických specifikací, protokolů, chování nebo výkonnostních měřítek, které musí produkt (např. uživatelské zařízení - UE, síťový uzel nebo softwarová komponenta) splnit, aby byl považován za kompatibilní s daným standardem 3GPP. Je základní jednotkou pro vytváření specifikací testů shody (TS) a testovacích případů. Proces začíná tím, že technické specifikační skupiny (TSG) definují normativní požadavky v základních specifikacích. Tyto požadavky jsou následně převedeny na konkrétní, spustitelné testovací případy skupinami, jako je pracovní skupina pro rádiový přístup RAN WG5 pro rádiové aspekty nebo pracovní skupina [CT](/mobilnisite/slovnik/ct/) WG4 pro protokoly jádra sítě a terminálů. Každý CR je pečlivě dokumentován, odkazuje na přesné klauzule základních specifikací, které ověřuje, a obsahuje podrobné účely testů, testovací postupy, očekávané zprávy a kritéria úspěšnosti/neúspěšnosti.

Architektura testování shody je postavena kolem těchto CR. Testovací platformy, jako jsou ty používané akreditovanými testovacími laboratořemi, implementují testovací sady odvozené od CR. Pro uživatelská zařízení (UE) to zahrnuje testování shody protokolů (PCT) pro vrstvy 2 a 3, testování rádiového vysílání a příjmu (T&R) pro fyzickou vrstvu a testování správy rádiových zdrojů (RRM). Pro síťové elementy testování shody ověřuje rozhraní jako [N2](/mobilnisite/slovnik/n2/), N3 nebo Xn. Testovací systém typicky zahrnuje testovací kontrolér, systémový simulátor (emulující síť) a testované zařízení ([EUT](/mobilnisite/slovnik/eut/)). Kontrolér provede testovací případ, simulátor generuje požadované signalizace a rádiové podmínky a odezvy EUT jsou monitorovány a vyhodnocovány vůči očekávaným výsledkům definovaným v CR.

Klíčové součásti CR zahrnují jeho jedinečné identifikační číslo, dotčené specifikace, podrobný popis problému nebo požadavku, navržené řešení nebo testovací případ a odůvodnění. CR jsou předkládány a schvalovány příslušnými pracovními skupinami 3GPP. Jejich role spočívá v odstranění nejednoznačnosti ve standardech, což zajišťuje, že různé implementace interpretují specifikace stejným způsobem. To je zásadní pro funkce jako předávání hovoru (handover), zřizování přenosových kanálů (bearer), bezpečnostní procedury a správu relací. Bez důsledně definovaných CR by byla interoperability mezi zařízeními od různých dodavatelů vážně narušena, což by vedlo k selhání sítě, zhoršení služeb a zvýšeným nákladům pro operátory.

V konečném důsledku jsou CR mostem mezi abstraktními standardními specifikacemi a reálnými, interoperabilními produkty. Poskytují měřitelná a ověřitelná kritéria, která certifikační orgány jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB používají k udělení certifikace. Celý ekosystém testování shody, včetně dodavatelů testovacích nástrojů a certifikačních agentur, se spoléhá na přesné definice v rámci CR při vývoji svých nabídek a služeb, což zajišťuje konzistentní a kvalitní uživatelský zážitek po celém světě.

## K čemu slouží

Účelem Conformance Requirements je řešit základní problém interoperability v telekomunikačním prostředí s více dodavateli. Standardy 3GPP jsou komplexní dokumenty, které mohou být předmětem různých interpretací. Bez formalizovaného procesu pro definování přesných, testovatelných požadavků by různí výrobci mohli vytvářet zařízení, která jsou teoreticky „standardně kompatibilní“, ale v praxi spolu nefungují. To by vedlo k fragmentovaným sítím, špatné uživatelské zkušenosti a potlačení inovací kvůli závislosti na jednom dodavateli (vendor lock-in). CR byly vytvořeny, aby poskytly jednoznačnou, na implementaci nezávislou definici toho, co skutečně znamená soulad pro každý kritický protokol a rozhraní.

Historicky, jak se mobilní sítě vyvíjely z proprietárních systémů na otevřené standardy, potřeba důsledného rámce shody se stala prvořadou. Zavedení GSM a později 3G vyžadovalo mechanismus, který by zajistil, že telefon od jednoho výrobce bude bezproblémově fungovat v síti postavené jiným. Proces CR tuto potřebu formalizuje. Odstraňuje omezení dřívějších, méně strukturovaných přístupů tím, že poskytuje sledovatelnou a řízenou metodu převodu textu standardu vysoké úrovně na nízkou, spustitelnou testovací verzi. To umožňuje efektivní certifikaci, zkracuje dobu uvedení nových produktů na trh a dává síťovým operátorům jistotu, že nasazené zařízení bude fungovat podle očekávání.

CR jsou navíc nezbytné pro udržení síťové bezpečnosti a spolehlivosti. Zajišťují, že bezpečnostní protokoly, jako je Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), jsou správně implementovány ve všech zařízeních, čímž předcházejí zranitelnostem. Také garantují, že procedury správy mobility a kvality služeb (QoS) fungují jednotně, což je klíčové pro služby jako hlas přes LTE (VoLTE) nebo plynulé předávání hovorů v 5G. V podstatě je systém CR páteří zajištění kvality ekosystému 3GPP, který umožňuje rozsah, spolehlivost a globální dosah moderních mobilních sítí.

## Klíčové vlastnosti

- Definuje jednoznačná, testovatelná kritéria pro soulad se standardy 3GPP
- Tvoří základ pro všechny testovací případy shody a certifikační programy
- Zajišťuje interoperabilitu mezi více dodavateli pro protokoly a rozhraní
- Poskytuje sledovatelnost od testovacích výsledků zpět ke klauzulím základních specifikací
- Pokrývá více domén včetně signalizace protokolů, rádiového výkonu a RRM
- Spravuje se prostřednictvím formálního procesu předkládání a schvalování v rámci pracovních skupin 3GPP

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 29.230** (Rel-19) — 3GPP Diameter Protocol Codes Specification
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.127** (Rel-18) — UICC-terminal interaction testing specification
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [CR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cr/)
