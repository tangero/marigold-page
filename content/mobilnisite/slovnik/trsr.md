---
slug: "trsr"
url: "/mobilnisite/slovnik/trsr/"
type: "slovnik"
title: "TRSR – Trace Recording Session Reference"
date: 2026-01-01
abbr: "TRSR"
fullName: "Trace Recording Session Reference"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/trsr/"
summary: "Jedinečný identifikátor používaný v rámci frameworku 3GPP Management and Orchestration pro odkazování na konkrétní sezení záznamu trasování. Umožňuje síťovým operátorům korelovat, spravovat a získávat"
---

TRSR je jedinečný identifikátor používaný v rámci frameworku 3GPP Management and Orchestration pro odkazování na konkrétní sezení záznamu trasování (trace recording session) za účelem korelace a získání podrobných síťových logů a dat o výkonu.

## Popis

Trace Recording Session Reference (TRSR) je klíčový identifikátor v rámci správy sítí 3GPP, konkrétně definovaný v kontextu služby Trace Control and Configuration Management Service (TCCMS) a širšího rámce Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)). Slouží jako jedinečný klíč, který jednoznačně identifikuje aktivní nebo historické sezení záznamu trasování zahájené síťovým operátorem. Sezení záznamu trasování je řízený proces, při kterém jsou konkrétní síťové funkce (např. Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), gNB) nebo uživatelská zařízení (UE) instruovány ke sběru a logování podrobných, granulárních dat o signalizačních procedurách, aktivitách uživatelské roviny, měřeních výkonu nebo specifických událostech.

Z architektonického hlediska je TRSR generován a spravován funkcí Trace Control Function, která často sídlí v systému Operations, Administration and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) nebo v Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)). Když se operátor nebo automatizovaná analytická funkce rozhodne zahájit trasování – například pro diagnostiku degradace služby konkrétního účastníka nebo pro monitorování výkonu v konkrétním síťovém řezu (slice) – odešle žádost o aktivaci trasování. Po úspěšné aktivaci přiřadí řídící funkce tomuto sezení jedinečný TRSR. Tento TRSR je pak zahrnut ve všech následných komunikačních zprávách správy týkajících se tohoto trasování. Používá se, když sběrné síťové funkce (trace collection entities) hlásí zachycená data trasování (Trace Records) zpět do centrální entity Trace Collection Entity. TRSR umožňuje systému správně přiřadit všechny příchozí záznamy trasování ke správnému kontextu sezení.

TRSR funguje ve spojení s dalšími parametry trasování, jako jsou Trace Reference, Trace Depth a Interfaces To Trace. Je základním kamenem pro správu životního cyklu sezení trasování: aktivaci, modifikaci, deaktivaci a získávání dat. Logy a záznamy uložené v archivu sběru trasování jsou indexovány pomocí TRSR, což umožňuje efektivní dotazování a analýzu. V servisně orientované architektuře 5G se TRSR používá v servisních operacích definovaných ve službách jako Nnrf_NFManagement, kde spotřebitelé služeb [NF](/mobilnisite/slovnik/nf/) se mohou přihlásit k odběru notifikací o datech trasování filtrovaných podle TRSR. Identifikátor zajišťuje izolaci a bezpečnost dat, protože data trasování jsou často citlivá a obsahují informace související s účastníky. Jeho strukturovaný formát umožňuje škálovatelnost ve velkých sítích, kde mohou být aktivní tisíce souběžných sezení trasování napříč různými doménami (5GC, NG-RAN).

## K čemu slouží

TRSR byl zaveden, aby vyřešil problém správy a korelace obrovského množství diagnostických dat generovaných distribuovanými sezeními trasování v moderních, složitých telekomunikačních sítích. Před jeho formální definicí byla správa trasování spíše ad-hoc a specifická pro dodavatele, což operátorům ztěžovalo konzistentní aktivaci trasování napříč více-vendorovými sítěmi a slučování dat z různých síťových prvků pro jednotný pohled na problém se službou nebo na cestu účastníka.

Jeho vytvoření bylo motivováno potřebou standardizovaného, automatizovaného odstraňování problémů a optimalizace sítí v sítích 3GPP, zejména s nasazením LTE a rostoucí složitostí jádra sítě. TRSR poskytuje standardizovaný 'uchop' (handle), který systémy [OAM](/mobilnisite/slovnik/oam/) a nové analytické funkce (jako [NWDAF](/mobilnisite/slovnik/nwdaf/) v 5G) mohou použít k programové kontrole a spotřebě dat trasování. To je zásadní pro implementaci automatizace s uzavřenou smyčkou, kde síť může sama diagnostikovat problémy: analytická funkce detekuje anomálii, automaticky aktivuje sezení trasování (obdrží TRSR), shromáždí data, analyzuje je a poté provede nápravnou akci, přičemž ve všech krocích používá TRSR jako identifikátor sezení.

Navíc, s příchodem síťových řezů (slicing) v 5G, je schopnost trasovat aktivity v rámci konkrétního řezu bez ovlivnění ostatních klíčová. TRSR, používaný ve spojení s identifikátory řezů, umožňuje trasování s ohledem na řez. Podporuje také regulatorní požadavky, jako je zákonné odposlouchávání (Lawful Interception - LI), tím, že poskytuje řízený framework pro aktivaci cílených trasování, ačkoli LI používá své vlastní specifické identifikátory a rozhraní. Stručně řečeno, TRSR je základním prvkem umožňujícím efektivní, škálovatelnou a automatizovanou pozorovatelnost a správu sítě v ekosystému 3GPP.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro síťové sezení záznamu trasování v rámci domény správy
- Umožňuje korelaci záznamů trasování shromážděných z více distribuovaných síťových funkcí a uživatelských zařízení (UE)
- Ústřední prvek pro správu životního cyklu sezení trasování (aktivace, modifikace, deaktivace)
- Používá se v servisně orientovaných rozhraních (např. Nnrf) pro přihlášení k odběru a získávání dat trasování
- Podporuje cílené trasování pro konkrétní účastníky, oblasti, řezy (slices) nebo služby
- Nezbytný pro automatizované odstraňování problémů a pracovní postupy Management Data Analytics (MDA)

## Definující specifikace

- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study

---

📖 **Anglický originál a plná specifikace:** [TRSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/trsr/)
