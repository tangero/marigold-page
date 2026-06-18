---
slug: "pegc"
url: "/mobilnisite/slovnik/pegc/"
type: "slovnik"
title: "PEGC – PIN Elements with Gateway Capability"
date: 2026-01-01
abbr: "PEGC"
fullName: "PIN Elements with Gateway Capability"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pegc/"
summary: "PEGC označuje prvky osobního identifikačního čísla (PIN) rozšířené o funkcionalitu brány, které umožňují zabezpečenou autentizaci a řízení přístupu v sítích 5G. Podporuje scénáře jako síťové segmentov"
---

PEGC je prvek 3GPP, který rozšiřuje PIN o funkcionalitu brány, aby poskytoval zabezpečenou autentizaci a řízení přístupu, podporující scénáře jako síťové segmentování (network slicing) a edge computing v sítích 5G.

## Popis

[PIN](/mobilnisite/slovnik/pin/) Elements with Gateway Capability (PEGC) je koncept zavedený ve specifikaci 3GPP Release 18, definovaný napříč více specifikacemi včetně TS 23.501 a TS 29.583. Spočívá v rozšíření tradičních autentizačních prvků založených na PIN o bránové schopnosti, aby bylo možné usnadnit zabezpečený a efektivní přístup v pokročilých síťových architekturách, jako je 5G. Architektura integruje PEGC do autentizačního a bezpečnostního rámce, kde funguje jako prostředník mezi uživatelským zařízením (UE) a síťovými funkcemi, poskytující jak ověřování identity, tak bránové služby. To je zvláště relevantní ve scénářích zahrnujících síťové segmentování (network slicing), edge computing a neveřejné sítě (NPNs), kde je důvěryhodný přístup klíčový.

Při provozu PEGC funguje tak, že využívá prvky PIN – jako jsou ty používané v [SIM](/mobilnisite/slovnik/sim/) kartách nebo vestavěných zabezpečených prvcích – k autentizaci uživatelů nebo zařízení, zatímco bránová schopnost mu umožňuje směrovat provoz, vynucovat zásady a spravovat konektivitu. Například v síťovém segmentu pro průmyslový IoT může PEGC ověřit senzor pomocí jeho přihlašovacích údajů PIN a následně bránovat data senzoru do konkrétní instance segmentu, čímž zajišťuje izolaci a zabezpečení. Klíčové komponenty zahrnují funkci správy PIN, která zpracovává ověřování PIN, a bránovou funkci, která poskytuje směrování, filtrování a překlad protokolů. PEGC komunikuje s ostatními síťovými funkcemi prostřednictvím rozhraní založených na službách (např. Nudm pro autentizaci) nebo referenčních bodů, jak je podrobně popsáno ve specifikacích jako TS 24.501 a TS 33.127.

Role PEGC v síti spočívá v posílení zabezpečení a flexibility při řízení přístupu. Umožňuje podrobné (fine-grained) ověřování, kde jsou prvky PIN použity nejen pro počáteční přístup, ale i pro průběžné ověřování v dynamických prostředích. Kombinací s bránovými schopnostmi může PEGC také podporovat směrování provozu, například přesměrování ověřených uživatelů na lokalizované edge služby. To je zásadní pro případy užití, jako jsou komunikace pro kritické mise nebo privátní 5G sítě, kde je vyžadována nízká latence a vysoká spolehlivost. PEGC přispívá k celkové bezpečnostní architektuře tím, že poskytuje důvěryhodný bod pro tvrzení identity, snižuje riziko neoprávněného přístupu a umožňuje plynulou mobilitu napříč různými síťovými doménami.

## K čemu slouží

PEGC byl vytvořen, aby řešil vyvíjející se bezpečnostní a přístupové potřeby sítí 5G, zejména s rozšířením síťového segmentování (network slicing), edge computingu a různorodých typů zařízení (např. IoT senzory, [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/) brýle). Předchozí přístupy spoléhaly na oddělené autentizační a bránové funkce, což mohlo vést ke složitosti, latenci a bezpečnostním mezerám v dynamických scénářích. Mezi omezení patřilo neefektivní zpracování autentizace založené na [PIN](/mobilnisite/slovnik/pin/) v kontextech bran, nedostatečná integrace se síťovým segmentováním a omezená podpora pro edge přístup, což ztěžovalo zajištění důvěryhodného a efektivního připojení pro specializované služby.

Motivace pro PEGC vychází ze snah 3GPP posílit síťovou flexibilitu a zabezpečení ve verzi Release 18 a dalších. Řeší problémy, jako je zabezpečená autentizace zařízení v edge lokalitách bez centralizovaných serverů, jak bránovat provoz pro izolované síťové segmenty a jak zjednodušit řízení přístupu pro neveřejné sítě (NPNs). Historicky byly prvky PIN používány primárně pro identitu účastníka v mobilních sítích, ale s PEGC jsou rozšířeny tak, aby poskytovaly bránové služby, což umožňuje integrovanější a škálovatelnější řešení. Tím se řeší potřeba lehkých, ale robustních autentizačních mechanismů v decentralizovaných architekturách.

PEGC také podporuje trend směrem k síťové automatizaci a architekturám založeným na službách. Vložením bránových schopností do prvků PIN snižuje závislost na externích branách pro základní směrování, čímž snižuje latenci a zlepšuje efektivitu. To je zvláště důležité pro časově citlivé aplikace v průmyslovém IoT nebo vozidlových komunikacích. Jeho zařazení do více specifikací, od základní sítě (23.501) po zabezpečení (33.127), ukazuje jeho průřezovou roli ve vývoji 5G. PEGC pomáhá operátorům nasazovat zabezpečené, na segmenty citlivé sítě při zachování zpětné kompatibility se stávajícími systémy založenými na PIN, což zajišťuje plynulý přechod k pokročilejším autentizačním a přístupovým paradigmatům.

## Klíčové vlastnosti

- Integrace autentizace založené na PIN se směrováním na bráně
- Podpora řízení přístupu pro síťové segmentování (network slicing)
- Posílené zabezpečení pro scénáře edge computingu
- Schopnosti směrování provozu a vynucování zásad
- Spolupráce s funkcemi 5G core sítě (např. AUSF, SMF)
- Kompatibilita se stávajícími systémy správy PIN

## Související pojmy

- [PIN – Personal Identification Number](/mobilnisite/slovnik/pin/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.542** (Rel-20) — Application layer support for Personal IoT Network
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.583** (Rel-19) — Application Layer Support for Personal IoT Network
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 29.583** (Rel-19) — PINAPP Stage 3 Protocol for PIN-9 Interface
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.882** (Rel-18) — Technical Report on 5G Security for Personal IoT Networks

---

📖 **Anglický originál a plná specifikace:** [PEGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pegc/)
