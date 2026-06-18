---
slug: "pnp"
url: "/mobilnisite/slovnik/pnp/"
type: "slovnik"
title: "PNP – PCS-1900 Number Portability"
date: 2026-01-01
abbr: "PNP"
fullName: "PCS-1900 Number Portability"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pnp/"
summary: "Přenositelnost čísel v pásmu PCS-1900 (PNP) je regulační a síťová funkce umožňující účastníkům zachovat si svá telefonní čísla při změně poskytovatele služeb v kmitočtovém pásmu PCS-1900 MHz v Severní"
---

PNP je regulační a síťová funkce umožňující účastníkům ponechat si svá mobilní čísla při přechodu mezi poskytovateli služeb v pásmu PCS-1900 MHz v Severní Americe.

## Popis

Přenositelnost čísel v pásmu PCS-1900 (PNP) je specifická implementace přenositelnosti mobilních čísel ([MNP](/mobilnisite/slovnik/mnp/)) pro pásmo osobních komunikačních služeb ([PCS](/mobilnisite/slovnik/pcs/)) na 1900 MHz, nasazená primárně v Severní Americe (USA a Kanada). Jedná se o komplexní službu zahrnující regulační požadavky, úpravy síťové architektury a standardizované signalizační postupy, které umožňují účastníkovi změnit síťového operátora (poskytovatele služeb) při zachování stávajícího čísla [MSISDN](/mobilnisite/slovnik/msisdn/). Technicky odděluje telefonní číslo účastníka od směrovacího identifikátoru operátora sítě, což vyžaduje změny ve směrování hovorů, signalizaci a správě databází účastníků.

Architektonicky PNP spoléhá na centralizovanou databázi přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)) nebo na řadu propojených databází operátorů. Když účastník přenese své číslo od Operátora A (dárce – Donor network) k Operátorovi B (příjemce – Recipient network), informace o přenosu se aktualizuje v NPDB. Hlavním síťovým mechanismem pro zpracování přenesených čísel je signalizační dotazování. Pro příchozí hovor na přenesené číslo musí ústředna výchozí sítě ([MSC](/mobilnisite/slovnik/msc/) v okruhově spínaných doménách nebo příslušná funkce řízení relací v IMS) dotazovat NPDB, aby zjistila aktuální obsluhující síť (směrovací číslo sítě příjemce). Tento proces je znám jako All Call Query (ACQ) nebo nepřímé směrování. Dotaz vrátí číslo pro směrování podle polohy ([LRN](/mobilnisite/slovnik/lrn/)) nebo podobnou směrovací adresu, která je následně použita k směrování hovoru na gateway MSC sítě příjemce pro konečné doručení účastníkovi.

Z pohledu protokolů implementace PNP zahrnuje rozšíření signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)) a později protokolů Diameter a [SIP](/mobilnisite/slovnik/sip/). Klíčové signalizační zprávy, jako je požadavek Send Routing Information (SRI) v protokolu MAP, jsou upraveny, aby obsahovaly příznaky dotazu na přenositelnost čísel. Home Location Register (HLR) také hraje klíčovou roli; když je číslo přeneseno, HLR sítě dárce se aktualizuje, aby indikovalo, že číslo již není hostováno, často vrací specifickou chybu nebo přesměrovává dotazy. V éře IMS pro VoLTE a VoNR jsou dotazy na přenositelnost čísel integrovány do logiky směrování hovorů v IMS, obvykle je provádí Interrogating Call Session Control Function (I-CSCF) nebo vyhrazený Number Portability SCP.

Provozní proces zahrnuje centrum koordinace přenosů a přísné validační postupy, aby se zabránilo neoprávněnému přenosu čísla. Technické specifikace (např. 3GPP TS 22.066, TS 29.002) definují datové struktury, signalizační toky a hodnoty časovačů pro zajištění interoperability mezi sítěmi různých operátorů. PNP je kritickým základem pro konkurenční telekomunikační trh, protože odstraňuje významný faktor setrvačnosti spotřebitele. Její implementace vyžaduje koordinaci mezi systémy podpory podnikání (BSS), provozními podpůrnými systémy (OSS) a základními síťovými prvky, aby byl zajištěn bezproblémový provoz během a po procesu přenosu.

## K čemu slouží

Přenositelnost čísel v pásmu PCS-1900 byla zavedena primárně jako regulační nařízení ke stimulaci konkurence na severoamerickém bezdrátovém trhu. Před jejím zavedením byli účastníci efektivně 'uzamčeni' u svého stávajícího operátora, protože změna poskytovatele znamenala změnu telefonního čísla – což byla významná komplikace, která odrazovala od přechodu. Tento nedostatek mobility spotřebitele umožňoval stávajícím operátorům udržovat si tržní podíl bez konkurenčního tlaku na ceny nebo kvalitu služeb. PNP, nařízená americkou Federální komunikační komisí (FCC), byla navržena k potlačení tohoto efektu uzamčení.

Technologicky, před zavedením PNP, číslo MSISDN obsahovalo vložené směrovací informace (jako je kód mobilní sítě – MNC), které přímo odkazovaly na domovskou síť účastníka a jeho HLR. Toto jednoduché, integrované směrování se stalo překážkou přenositelnosti. Starší přístup nevyžadoval žádné databázové dotazy; ústředna mohla směrovat hovor pouze na základě volaného čísla. PNP tento problém vyřešila zavedením vrstvy oddělení: volané číslo již implicitně neurčovalo síť. To si vyžádalo vývoj nových síťových prvků (jako je NPDB) a významné upgradu všech ústředen a signalizační infrastruktury, aby mohly provádět databázové dotazy v reálném čase pro každý hovor na potenciálně přenesené číslo.

Vytvoření PNP také řešilo problémy interoperability v prostředí s více dodavateli a operátory. Standardizace prostřednictvím 3GPP (počínaje Release 4) byla zásadní pro zajištění konzistentní implementace této funkce všemi síťovými operátory a výrobci zařízení. To umožnilo celostátní a nakonec celoseveroamerickou přenositelnost čísel. Řešení muselo být vysoce spolehlivé a s nízkou latencí, protože přidání databázového dotazu do cesty sestavení hovoru zvyšuje prodlevu po vytáčení. Technickou výzvou bylo navrhnout systém, který je pro koncového uživatele transparentní, zachovává vysokou úspěšnost dokončení hovorů a je škálovatelný pro zvládnutí celé základny účastníků velkého trhu.

## Klíčové vlastnosti

- Umožňuje účastníkům zachovat si svůj MSISDN při změně poskytovatele služeb v pásmu PCS-1900.
- Využívá centralizovanou nebo distribuovanou databázi přenositelnosti čísel (NPDB) pro vyhledávání směrovacích informací.
- Implementuje směrování typu All Call Query (ACQ), kdy každý hovor na mobilní číslo spustí databázový dotaz.
- Vrací číslo pro směrování podle polohy (LRN), které navedou hovor na gateway ústřednu sítě příjemce.
- Vyžaduje úpravy signalizace v základní síti (MAP, ISUP, SIP) a chování HLR/HLR-FE.
- Zahrnuje formální proces přenosu čísla s validací a koordinací mezi operátory dárcem a příjemcem.

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 32.582** (Rel-19) — HNB Management Information Model for Type 1 Interface
- **TS 32.584** (Rel-19) — HNB OAM&P XML Definitions for Type 1 Interface
- **TS 32.592** (Rel-19) — HeNB OAM&P Information Model
- **TS 32.594** (Rel-19) — Data definitions for HeNB to HeMS Type 1 interface
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [PNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pnp/)
