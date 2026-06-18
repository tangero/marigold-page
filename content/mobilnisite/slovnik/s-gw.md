---
slug: "s-gw"
url: "/mobilnisite/slovnik/s-gw/"
type: "slovnik"
title: "S-GW – Serving Gateway"
date: 2025-01-01
abbr: "S-GW"
fullName: "Serving Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s-gw/"
summary: "Serving Gateway (S-GW) je klíčový uzel jádrové sítě v architekturách 3GPP EPS (4G) a raných 5G NSA. Působí jako kotva mobility pro uživatelskou rovinu při předávání spojení mezi eNodeB a jako lokální"
---

S-GW je uzel jádrové sítě ve 4G a raných 5G NSA, který směruje uživatelská data, spravuje přenosové kanály (bearery), slouží jako kotva mobility při předávání spojení a provádí zákonné odposlechy.

## Popis

Serving Gateway (S-GW) je základní entita uživatelské roviny v rámci Evolved Packet Core (EPC), což je jádrová síť pro systémy 4G LTE, a používá se také v nasazeních 5G Non-Standalone ([NSA](/mobilnisite/slovnik/nsa/)). Je to uzel s granularitou na jednotlivé uživatelské zařízení (UE), což znamená, že UE je v daném okamžiku pro svá aktivní připojení k [PDN](/mobilnisite/slovnik/pdn/) spojeno s jedním S-GW. Architektonicky se S-GW nachází mezi rádiovou přístupovou sítí (RAN), konkrétně eNodeB v LTE, a bránou Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)). Jeho primární funkcí je být kotvou mobility pro uživatelskou rovinu. Při předávání spojení mezi eNodeB zůstává S-GW koncovým bodem a datová cesta je přepnuta ze zdrojového na cílové eNodeB, což zajišťuje plynulou kontinuitu relace bez zapojení P-GW. Pro neaktivní (idle) UE S-GW ukončuje downlinkovou datovou cestu a při příchodu downlinkových dat spouští paginaci. Pakety ukládá do vyrovnávací paměti a iniciuje proceduru síťově iniciované žádosti o službu (network-triggered service request) za účelem opětovného nastavení přenosových kanálů. S-GW také slouží jako kotva pro mobilitu mezi různými 3GPP přístupovými technologiemi (např. předání spojení z LTE na 2G/3G [GPRS](/mobilnisite/slovnik/gprs/)), přičemž komunikuje s 2G/3G [SGSN](/mobilnisite/slovnik/sgsn/) přes rozhraní S4. Směruje a přeposílá všechny uživatelské IP pakety a provádí základní funkce, jako je označování uplinkových a downlinkových paketů pomocí QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) a Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)). S-GW také generuje záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro účtování na bázi přenosových kanálů pro jednotlivá UE, které odesílá funkci Charging Gateway Function (CGF). Pro vynucování QoS politik na přenosových kanálech GPRS Tunneling Protocol (GTP) komunikuje s Policy and Charging Rules Function (PCRF) přes referenční bod Gxc. Zákonný odposlech uživatelského provozu je také prováděn na S-GW. Pro signalizaci řídicí roviny se připojuje k MME přes rozhraní S11 a pro uživatelskou rovinu k P-GW přes rozhraní S5/S8.

## K čemu slouží

S-GW byl vytvořen jako součást revoluční ploché IP architektury Evolved Packet System (EPS) ve 3GPP Release 8, které definovalo LTE. Vyřešil klíčové problémy vlastní předchozí architektuře 3G UMTS. V UMTS obsluhovala Serving GPRS Support Node (SGSN) jak řídicí, tak uživatelskou rovinu, což vytvářelo potenciální úzké místo. EPS tyto funkce rozdělilo: MME pro řídicí rovinu a S-GW pro uživatelskou rovinu, což umožnilo jejich nezávislé škálování a optimalizované směrování dat. Zásadním problémem byla efektivní správa mobility. Role S-GW jako lokální kotvy mobility pro předávání spojení uvnitř LTE minimalizovala signalizační zátěž na jádru (P-GW) a snížila latenci při předání spojení, což bylo zásadní pro podporu služeb v reálném čase. Poskytlo také stabilní kotvící bod pro mobilitu mezi různými rádiovými přístupovými technologiemi (inter-RAT), což zjednodušilo předávání spojení mezi LTE a staršími 2G/3G sítěmi během přechodného období. Dále centralizací ukončení uživatelské roviny pro dané UE umožnilo efektivní ukládání downlinkových dat do vyrovnávací paměti a paginaci pro neaktivní zařízení, což je klíčové pro optimalizaci životnosti baterie. Návrh S-GW byl motivován potřebou výkonného, škálovatelného a nákladově efektivního jádra sítě, které by zvládlo masivní nárůst mobilního datového provozu očekávaný s příchodem 4G, při zachování robustní mobility a kontinuity služeb.

## Klíčové vlastnosti

- Lokální kotva mobility pro uživatelskou rovinu při předávání spojení uvnitř LTE (mezi eNodeB)
- Kotva pro mobilitu mezi různými 3GPP rádiovými přístupovými technologiemi (např. z LTE na GERAN/UTRAN)
- Ukončuje downlinkovou datovou cestu pro neaktivní (idle) UE a spouští paginaci
- Směruje a přeposílá uživatelské IP pakety mezi eNodeB (S1-U) a P-GW (S5/S8)
- Spravuje a vynucuje QoS na přenosových kanálech Evolved Packet System (EPS)
- Provádí zákonný odposlech a generuje záznamy o účtování (CDR)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.804** (Rel-8) — CT3 Aspects of System Architecture Evolution
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 32.820** (Rel-8) — Charging Architecture Study for Evolved 3GPP
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [S-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-gw/)
