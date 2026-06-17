---
slug: "aal5"
url: "/mobilnisite/slovnik/aal5/"
type: "slovnik"
title: "AAL5 – ATM Adaptation Layer type 5"
date: 2025-01-01
abbr: "AAL5"
fullName: "ATM Adaptation Layer type 5"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aal5/"
summary: "AAL5 je protokolová vrstva v zásobníku ATM navržená pro efektivní, spojově orientovaný přenos datových paketů proměnné délky, především IP datagramů, přes sítě asynchronního přenosového režimu (ATM)."
---

AAL5 je protokol adaptační vrstvy ATM navržený pro efektivní, spojově orientovaný přenos datových paketů proměnné délky, jako jsou IP datagramy, přes sítě ATM, který poskytuje segmentaci a zpětnou skládání s nízkou režií.

## Popis

[ATM](/mobilnisite/slovnik/atm/) Adaptation Layer type 5 (AAL5) je specifická protokolová vrstva v rámci širšího zásobníku protokolů ATM (Asynchronous Transfer Mode), definovaná [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatá organizací 3GPP pro rané verze. Jejím hlavním úkolem je adaptovat protokoly vyšších vrstev, zejména nespojové protokoly jako IP (Internet Protocol), na podkladovou vrstvu ATM, která pracuje s pevně velikými buňkami o délce 53 bajtů (48bajtový datový obsah plus 5bajtová hlavička). AAL5 se nachází nad vrstvou ATM a pod vrstvami jako je Service-Specific Convergence Sublayer (SSCS) nebo přímo pod IP. Je klasifikována jako 'jednoduchá a efektivní' [AAL](/mobilnisite/slovnik/aal/) (SEAL), optimalizovaná pro datový provoz, kde je obnova po chybách a řazení zajišťováno vyššími vrstvami.

Z architektonického hlediska se AAL5 skládá ze dvou podvrstev: podvrstvy pro segmentaci a zpětnou skládání (SAR) a konvergenční podvrstvy ([CS](/mobilnisite/slovnik/cs/)). Konvergenční podvrstva se dále dělí na společnou část konvergenční podvrstvy ([CPCS](/mobilnisite/slovnik/cpcs/)) a služebně specifickou konvergenční podvrstvu (SSCS), ačkoli AAL5 často pracuje s nulovou SSCS pro základní přenos dat. CPCS je zodpovědná za přípravu datové jednotky protokolu (PDU) z paketu vyšší vrstvy. Na konec PDU přidá CPCS zápatí, které obsahuje pole Délka (udávající velikost datového obsahu CPCS), kontrolní součet CRC-32 pro detekci chyb v celé CPCS PDU a pole CPCS User-to-User pro indikaci. Celá struktura – datový obsah plus zápatí – musí být odsazena tak, aby byla celočíselným násobkem 48 bajtů, aby byla zarovnána s datovými obsahy buněk ATM.

Podvrstva pro segmentaci a zpětnou skládání následně fragmentuje tuto připravenou CPCS PDU na řadu 48bajtových segmentů. Každý segment je umístěn do datového pole standardní buňky ATM. Všechny buňky pro jednu CPCS PDU, kromě poslední, mají v hlavičce ATM pole Payload Type (PT) nastaveno tak, aby indikovalo buňku, která není poslední v sekvenci. Poslední buňka má bit PT nastaven na '1', což signalizuje konec rámce AAL5. Tento mechanismus umožňuje přijímači identifikovat hranici rámce bez explicitních polí délky v každé buňce. Podvrstva SAR přijímače shromažďuje buňky patřící ke stejnému virtuálnímu kanálovému spojení (VCC), dokud neodhalí buňku označující konec rámce. Poté předá zpětně složený bajtový proud CPCS, která použije CRC-32 k ověření integrity dat a pole Délka k odstranění případného odsazení a doručení původního paketu vyšší vrstvy.

V architektuře 3GPP byl AAL5 specifikován jako přenosová možnost pro několik kritických rozhraní, zejména v paketové doméně (PS) během éry 3G (UMTS). Byl používán přes rozhraní Iu-PS (mezi RNC a SGSN), Gn (mezi SGSN a mezi SGSN a GGSN) a Gi (mezi GGSN a externími paketovými datovými sítěmi), když tato rozhraní byla založena na fyzické infrastruktuře ATM. Jeho úlohou bylo poskytnout standardizovanou, efektivní metodu pro přenos IP-based řídicí roviny (např. [GTP-C](/mobilnisite/slovnik/gtp-c/)) a uživatelské roviny (např. [GTP-U](/mobilnisite/slovnik/gtp-u/)) přes spolehlivé, spojově orientované páteřní sítě ATM, které převládaly v raných nasazeních 3G. Návrh AAL5 minimalizoval protokolovou režii ve srovnání s dřívějšími typy AAL, jako je AAL3/4, což jej činilo vhodným pro přerušovaný, proměnně dlouhý charakter IP provozu v mobilních jádrových sítích.

## K čemu slouží

AAL5 byl vytvořen, aby řešil specifickou potřebu efektivního přenosu nespojových datových paketů proměnné délky (především IP) přes spojově orientované sítě [ATM](/mobilnisite/slovnik/atm/), které byly dominantní vysokorychlostní páteřní technologií na konci 90. let a začátku 21. století. Před AAL5 byly adaptační vrstvy ATM, jako AAL3/4, složitější, obsahovaly pořadová čísla, identifikátory multiplexování a kontrolní součet CRC na buňku, což zavádělo významnou režii pro datové aplikace, které tyto funkce nepotřebovaly. Telekomunikační průmysl, včetně 3GPP pro své počáteční specifikace UMTS, potřeboval štíhlejší adaptační metodu, aby mohl efektivně využívat schopnosti ATM v oblasti kvality služeb (QoS) a přepínání pro datové služby bez zbytečné protokolové nadváhy.

Historický kontext představuje konvergenci telefonních a datových sítí. ATM bylo vybráno pro raná jádra sítí 3G díky svým přednostem v podpoře více typů provozu se zaručenou QoS, což odpovídalo vizi multimediálních mobilních služeb. Nicméně hlavní uživatelský datový obsah byl stále více založen na IP. AAL5 vyřešil tento nesoulad tím, že poskytl jednoduchý mechanismus segmentace s kontrolou chyb na koncích (přes CRC-32), ale přenechal opakovaný přenos a řízení toku protokolům vyšších vrstev, jako je TCP. Tato filozofie návrhu uznala, že pro datový provoz jsou efektivita a nižší zatížení zpracováním důležitější než robustní mechanismy obnovy po chybách na úrovni buňky v AAL3/4.

Přijetím AAL5 umožnilo 3GPP výrobcům zařízení a operátorům využít stávající investice do infrastruktury ATM pro budování raných paketových jader 3G. Poskytlo standardizovanou, spolehlivou přenosovou vrstvu pro GTP tunely přenášející uživatelská data a signalizaci, což zajišťovalo interoperabilitu mezi síťovými prvky od různých výrobců. Zatímco pozdější verze 3GPP přešly na čistě IP přenos (Ethernet/IP), čímž odpadla potřeba adaptace ATM, AAL5 byla klíčovou přemosťovací technologií, která umožnila průmyslu nasadit vysokorychlostní paketově přepínané mobilní datové služby na síťové technologii dostupné v dané době.

## Klíčové vlastnosti

- Efektivní segmentace paketů proměnné délky do 48bajtových datových obsahů buněk ATM
- Nízká režie ve srovnání s AAL3/4, využívající pouze 8bajtové zápatí na CPCS PDU
- Silná detekce chyb prostřednictvím 32bitového kontrolního součtu (CRC-32) vypočteného přes celou CPCS PDU
- Využití bitu Payload Type v hlavičce buňky ATM k vymezení hranic rámce bez explicitních polí délky v každé buňce
- Podpora spojově orientovaného přenosu přes virtuální kanálová spojení ATM (VCC)
- Odsazení pro zarovnání, které zajišťuje, že CPCS PDU je násobkem 48 bajtů pro efektivní segmentaci do buněk

## Související pojmy

- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.442** (Rel-19) — Node B Implementation Specific O&M Transport via RNC
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [AAL5 na 3GPP Explorer](https://3gpp-explorer.com/glossary/aal5/)
