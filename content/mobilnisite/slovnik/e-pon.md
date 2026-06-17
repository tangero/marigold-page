---
slug: "e-pon"
url: "/mobilnisite/slovnik/e-pon/"
type: "slovnik"
title: "E-PON – Ethernet Passive Optical Network"
date: 2025-01-01
abbr: "E-PON"
fullName: "Ethernet Passive Optical Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-pon/"
summary: "Standardizovaná technologie přístupové optické sítě, která využívá pasivní rozdělovače k doručování vysokorychlostních ethernetových služeb z centrální ústředny k více koncovým uživatelům. Vytváří arc"
---

E-PON je standardizovaná technologie přístupové optické sítě, která využívá pasivní optické rozdělovače v architektuře point-to-multipoint k poskytování vysokorychlostních ethernetových služeb pro širokopásmový přístup a mobilní backhaul.

## Popis

Ethernet Passive Optical Network (E-PON), jak je odkazováno ve specifikacích 3GPP, je technologie přístupové sítě typu fiber-to-the-x (FTTx) založená na standardu [IEEE](/mobilnisite/slovnik/ieee/) 802.3ah (Ethernet in the First Mile). Jedná se o síťovou architekturu point-to-multipoint (P2MP), kde je jediné optické vlákno z centrálního optického koncového zařízení (Optical Line Terminal, OLT) pasivně rozděleno pomocí optických rozdělovačů, aby obsloužilo více optických síťových jednotek (Optical Network Units, ONU) u zákazníka. „Pasivní“ povaha odkazuje na použití neaktivních (nepoháněných) rozdělovačů ve venkovní části sítě, což snižuje provozní náklady a požadavky na napájení ve srovnání s aktivními optickými sítěmi. E-PON používá pro provoz v obou směrech (upstream i downstream) jediné vlákno s využitím různých vlnových délek (typicky 1490 nm pro downstream, 1310 nm pro upstream). Provoz ve směru downstream je vysílán z OLT všem ONU, přičemž každá ONU filtruje rámce na základě svého jedinečného identifikátoru logického spoje (Logical Link Identifier, LLID). Přenos ve směru upstream je sdílený a řízený OLT pomocí protokolu s multiplexním přístupem s časovým dělením (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/), TDMA), kdy OLT přiděluje každé ONU konkrétní časové sloty pro vysílání, čímž zabraňuje kolizím dat. Klíčové specifikace 3GPP, jako je TR 22.906, zkoumají využití E-PON jako důvěryhodné přístupové sítě mimo 3GPP pro konvergenci pevných a bezdrátových sítí a jako vysokokapacitní, nízkolatenční přenos pro mobilní backhaul, zejména pro 4G a 5G small cells a centralizovaný RAN (C-RAN) fronthaul. Jeho jednoduchost, vysoká přenosová kapacita (dle standardu 1 Gbps symetricky) a nativní podpora ethernetových rámců z něj činí nákladově efektivní řešení pro poskytování širokopásmového přístupu a podporu network slicing v konvergentních přístupových scénářích.

## K čemu slouží

E-PON byl vyvinut, aby poskytl standardizované, vysokokapacitní a nákladově efektivní optické přístupové řešení pro uspokojení explodující poptávky po rezidenčním a podnikovém širokopásmovém internetu. Řešil omezení tradičního [DSL](/mobilnisite/slovnik/dsl/) na bázi měděných vedení a aktivního point-to-point optického vlákna, které byly buď kapacitně omezené, nebo nákladné na nasazení a údržbu pro hromadný trh. Využitím pasivních rozdělovačů E-PON dramaticky snižuje množství optického vlákna a aktivního zařízení potřebného v terénu, čímž snižuje kapitálové i provozní výdaje. V rámci ekosystému 3GPP bylo jeho zahrnutí od Release 11 motivováno potřebou standardizovaných, vysoce výkonných technologií pevného přístupu, které umožní bezproblémovou integraci s mobilními sítěmi pro konvergenci pevných a mobilních sítí (Fixed-Mobile Convergence, [FMC](/mobilnisite/slovnik/fmc/)), a aby poskytly spolehlivý, vysokokapacitní backhaul a fronthaul pro hustá nasazení 4G/5G. Slouží jako základní technologie pro síťové operátory budující jednotnou přístupovou infrastrukturu.

## Klíčové vlastnosti

- Architektura point-to-multipoint využívající pasivní optické rozdělovače
- Nativní přenos ethernetových rámců (vrstva 2)
- Multiplexování broadcast ve směru downstream a TDMA ve směru upstream
- Obousměrný provoz na jediném vlákně s využitím vlnového multiplexu (Wavelength Division Multiplexing, WDM)
- Standardizované možnosti správy, provozu a údržby (Operation, Administration, and Maintenance, OAM)
- Podporuje symetrické přenosové rychlosti 1 Gbps dle základního standardu

## Definující specifikace

- **TR 22.906** (Rel-19) — IMS P2P Content Distribution Services

---

📖 **Anglický originál a plná specifikace:** [E-PON na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-pon/)
