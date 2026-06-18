---
slug: "bcsm"
url: "/mobilnisite/slovnik/bcsm/"
type: "slovnik"
title: "BCSM – Basic Call State Model"
date: 2025-01-01
abbr: "BCSM"
fullName: "Basic Call State Model"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bcsm/"
summary: "Základní model stavů hovoru (BCSM) je model konečného automatu definovaný 3GPP, který popisuje fáze zpracování hovoru nebo relace v jádru sítě. Je zásadní pro architekturu Inteligentní sítě (IN), prot"
---

BCSM je model konečného automatu definovaný 3GPP, který popisuje fáze zpracování hovoru nebo relace v jádru sítě a umožňuje služby Inteligentní sítě, jako je přesměrování hovoru nebo předplacené účtování.

## Popis

Základní model stavů hovoru (BCSM) je klíčový koncept v architektuře Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) 3GPP, konkrétně definovaný ve specifikacích [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic). Poskytuje abstraktní, standardizovanou reprezentaci logiky řízení hovoru a relace z pohledu funkce přepínání služeb ([SSF](/mobilnisite/slovnik/ssf/)). BCSM je v podstatě konečný automat, který modeluje průběh hovoru nebo relace prostřednictvím řady odlišných zpracovatelských fází, známých jako body ve hovoru (PICs). Každý [PIC](/mobilnisite/slovnik/pic/) představuje významný milník při sestavování, správě nebo ukončování hovoru, například 'Authorize_Origination_Attempt', 'Collect_Information', 'Analyze_Information', 'Routing_and_Alerting' a 'Active'.

Mezi těmito PIC se nacházejí detekční body (DPs). DPs jsou specifické události nebo podmínky během zpracování hovoru, kdy může SSF pozastavit své normální řízení a komunikovat s externí funkcí řízení služeb ([SCF](/mobilnisite/slovnik/scf/)). DPs jsou klasifikovány jako spouštěcí detekční body (TDPs), které jsou nastaveny staticky na základě předplatitelských dat, a jako událostní detekční body (EDPs), které jsou nastaveny dynamicky SCF během aktivní relace servisní logiky. Když je dosaženo nastaveného [DP](/mobilnisite/slovnik/dp/), SSF odešle oznámení SCF, která pak může SSF dát pokyn, jak pokračovat – například pokračovat, spojit se s jiným číslem nebo přehrát oznámení.

Architektonicky je BCSM implementován uvnitř funkce přepínání služeb (SSF), která sídlí v síťových uzlech, jako je ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) nebo funkce řízení relací hovoru ([CSCF](/mobilnisite/slovnik/cscf/)) v IMS. SSF používá BCSM ke sledování stavů hovoru a řízení dialogu se SCF. Existují dvě hlavní instance BCSM: BCSM volajícího (O-BCSM), který modeluje hovor z pohledu volající strany, a BCSM volaného (T-BCSM), který jej modeluje z pohledu volané strany. Tento přístup s dvojím modelem umožňuje aplikovat servisní logiku nezávisle na základě role účastníka v hovoru.

Úlohou BCSM je oddělit základní zpracování hovoru v ústředně od provádění složité, přidané servisní logiky. Poskytnutím standardizovaného stavového modelu a dobře definovaných interakčních bodů (DPs) umožňuje síťovým operátorům nasazovat a spravovat širokou škálu doplňkových služeb – jako je předplacené účtování, přesměrování hovoru, bezplatná čísla nebo služby VPN – flexibilním a nezávislým na dodavateli způsobem. Model zajišťuje, že aplikace servisní logiky mají konzistentní a předvídatelný pohled na síťové události, což je klíčové pro spolehlivé provádění služeb napříč různým síťovým vybavením.

## K čemu slouží

BCSM byl vytvořen, aby řešil omezení tradičních telefonních ústředen, kde byla servisní logika pevně integrována a naprogramována přímo do přepínacího softwaru. To zavedení nových služeb činilo pomalým, nákladným a závislým na konkrétním dodavateli, protože vyžadovalo softwarové aktualizace každé ústředny v síti. Primární motivací bylo umožnit rychlé vytváření a nasazování služeb nezávisle na základní přepínací infrastruktuře, což je koncept ústřední pro paradigma Inteligentní sítě (IN).

Jeho vytvoření vyřešilo problém přenositelnosti a flexibility služeb. Definováním standardizovaného abstraktního modelu stavů hovoru umožnil BCSM vyvíjet servisní logiku jednou a nasazovat ji napříč sítěmi od různých dodavatelů. Tato abstraktní vrstva znamenala, že servisní aplikace, běžící na externích bodech řízení služeb (SCPs), potřebovaly rozumět pouze stavům a detekčním bodům BCSM, nikoli proprietárnímu vnitřnímu fungování ústředen každého výrobce. To dramaticky zkrátilo dobu uvedení nových služeb na trh.

Historicky byl koncept BCSM převzat z pevných standardů Inteligentní sítě (ITU-T CS-1) a přizpůsoben 3GPP pro mobilní sítě, nejvýznamněji v rámci frameworku CAMEL pro GSM a UMTS. Poskytl základní mechanismus pro implementaci operátorsky specifické, reálné kontroly nad mobilními hovory a relacemi, což bylo zásadní pro pokročilé účtovací schémata (jako předplacené), služby založené na poloze a personalizované zacházení s hovory – služby, které se stávaly klíčovými konkurenčními rozdíly pro mobilní operátory.

## Klíčové vlastnosti

- Modelování fází zpracování hovoru/relace jako konečného automatu (body ve hovoru - PICs)
- Definované detekční body (DPs) pro interakci mezi přepínacími a řídicími funkcemi služeb
- Rozdělení na instance BCSM volajícího (O-BCSM) a BCSM volaného (T-BCSM)
- Podpora pro staticky nastavené spouštěcí detekční body (TDPs) a dynamicky nastavené událostní detekční body (EDPs)
- Umožňuje pozastavení základního zpracování hovoru pro provedení externí servisní logiky
- Standardizované abstraktní rozhraní umožňující vytváření služeb nezávislé na dodavateli

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [BCSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcsm/)
