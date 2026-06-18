---
slug: "edc"
url: "/mobilnisite/slovnik/edc/"
type: "slovnik"
title: "EDC – Error Detection Code byte"
date: 2026-01-01
abbr: "EDC"
fullName: "Error Detection Code byte"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/edc/"
summary: "Jeden bajt používaný v protokolech 3GPP k ověření integrity přenášených datových bloků. Obsahuje kontrolní součet vypočítaný z dat, což přijímači umožňuje detekovat chyby vzniklé během přenosu. Jde o"
---

EDC je jeden bajt obsahující kontrolní součet, který se používá v protokolech 3GPP k ověření integrity dat a umožňuje přijímači detekovat přenosové chyby.

## Popis

Bajt kódu pro detekci chyb (Error Detection Code – EDC) je základní součástí protokolů linkové a fyzické vrstvy v systémech 3GPP, používaný primárně ve specifikacích GSM a raného UMTS. Jedná se o 8bitové pole připojené k datovému bloku nebo rámci před přenosem. Hodnota tohoto bajtu se vypočítá aplikací specifického polynomu cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) na informační bity bloku. K vygenerování kontrolního součtu, který je funkcí všech datových bitů, se používají běžné polynomy, například CRC-8. Po přijetí přijímající entita nezávisle přepočítá EDC na základě přijatých datových bitů a porovná jej s přijatým EDC bajtem. Nesoulad indikuje, že jeden nebo více bitů bylo během přenosu poškozeno, což spustí procedury jako je automatický požadavek na opakování ([ARQ](/mobilnisite/slovnik/arq/)) pro retransmisi nebo zahození chybného rámce.

Z architektonického hlediska se vkládání a ověřování EDC zpracovává v protokolovém zásobníku vrstvy 2, často v podsložkách řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) nebo řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), v závislosti na konkrétním kanálu a technologii (např. datové kanály GSM, [GPRS](/mobilnisite/slovnik/gprs/) nebo rané transportní kanály UMTS). Jeho role je nedílnou součástí funkce detekce chyb, která funguje před složitějšími technikami opravy chyb, jako je korekce chyb vpřed ([FEC](/mobilnisite/slovnik/fec/)). Zatímco FEC dokáže některé chyby opravit, EDC poskytuje definitivní, nenáročnou kontrolu neopravitelných chyb, čímž zajišťuje, že vyšším vrstvám nejsou předána poškozená data.

Jednoduchost EDC je jeho hlavní předností; přidává minimální režii (pouze jeden bajt) a zároveň poskytuje vysokou pravděpodobnost detekce náhodných a shlukových chyb typických pro rádiové prostředí. Jeho účinnost je kvantifikována Hammingovou vzdáleností, která určuje minimální počet chyb bitů potřebných k tomu, aby zůstaly neodhaleny. V praxi je pro krátké bloky vysoce účinný. Pro větší datové bloky nebo v prostředích vyžadujících extrémně vysokou spolehlivost jsou však v pozdějších technologiích, jako jsou LTE a 5G NR, používány robustnější schémata, jako jsou delší CRC pole (např. CRC-16, CRC-24). Bajt EDC tedy představuje základní, efektivní mechanismus detekce chyb v legacy systémech 3GPP.

## K čemu slouží

Bajt EDC byl vytvořen, aby řešil inherentní nespolehlivost prostředí rádiového přenosu. Bezdrátové kanály jsou náchylné k šumu, interferenci a útlumu, které mohou během přenosu dat změnit bity. Bez mechanismu pro detekci těchto chyb by byla poškozená data předávána aplikacím vyšších vrstev, což by způsobovalo poruchy, poškozené soubory nebo chybně interpretované signalizační zprávy. Primárním účelem EDC je poskytnout první obrannou linii tím, že přijímači umožní s vysokou mírou jistoty identifikovat poškozené rámce.

Historicky byl zaveden jako standardní metoda s nízkou režií v rámci GSM a raných datových služeb 3G ke zlepšení spolehlivosti datových služeb přes spojově orientovaná a počáteční paketově orientovaná připojení. Řešil problém skrytého poškození dat, kdy chyby zůstanou nepovšimnuty. Detekcí chyb může protokol zahájit nápravné akce, jako je zahození špatného rámce nebo vyžádání jeho opětovného přenosu, čímž je zajištěna integrita dat. To byl kritický krok k tomu, aby se bezdrátové datové služby staly použitelnými pro aplikace mimo hlas, kde je tolerance k chybám bitů extrémně nízká.

Motivace vycházela z potřeby vyváženého přístupu mezi režií a spolehlivostí. Složitější oprava chyb přidává významnou redundanci a složitost zpracování. Bajt EDC nabízí kompromis: přidává pouze 8 bitů režie, což je pro používané velikosti bloků zanedbatelné, ale poskytuje dostatečnou schopnost detekce pro charakteristiky chyb kanálů 2G a 3G. Položil základy pro sofistikovanější hybridní [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) a pokročilá CRC schémata používaná v pozdějších generacích.

## Klíčové vlastnosti

- 8bitové (jeden bajt) pole kontrolního součtu
- Typicky generováno pomocí CRC polynomu (např. CRC-8)
- Připojeno k datovým blokům před přenosem
- Poskytuje vysokou pravděpodobnost detekce náhodných a shlukových chyb
- Při detekci chyby spouští procedury opakovaného přenosu nebo zahození
- Nízká implementační složitost a minimální režie protokolu

## Související pojmy

- [CRC – Cyclic Redundancy Check](/mobilnisite/slovnik/crc/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 27.007** (Rel-19) — AT Command Set for UE

---

📖 **Anglický originál a plná specifikace:** [EDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/edc/)
