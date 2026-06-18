---
slug: "wlan"
url: "/mobilnisite/slovnik/wlan/"
type: "slovnik"
title: "WLAN – Wireless Local Area Network"
date: 2026-01-01
abbr: "WLAN"
fullName: "Wireless Local Area Network"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wlan/"
summary: "Wireless Local Area Network (WLAN) je bezdrátová radiová technologie, běžně známá jako Wi-Fi, standardizovaná IEEE 802.11. V 3GPP se tento termín vztahuje k integraci a spolupráci WLAN s mobilními sít"
---

WLAN je bezdrátová radiová technologie standardizovaná jako IEEE 802.11 (Wi-Fi), kterou 3GPP integruje s mobilními sítěmi pro přesměrování dat (offloading), plynulou mobilitu a konvergovaný přístup ke službám.

## Popis

Wireless Local Area Network (WLAN), převážně založená na standardech [IEEE](/mobilnisite/slovnik/ieee/) 802.11 (Wi-Fi), je základní technologií radiového přístupu pro lokální konektivitu. V rámci ekosystému 3GPP není WLAN definována jako 3GPP [RAT](/mobilnisite/slovnik/rat/) sama o sobě, ale její integrace s 3GPP mobilními sítěmi je rozsáhle standardizována. Tato integrace, známá jako WLAN Interworking nebo Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) v dřívějších vydáních a později jako Non-3GPP Interworking nebo Access Traffic Steering, Switching and Splitting ([ATSSS](/mobilnisite/slovnik/atsss/)) v 5G, umožňuje uživatelskému zařízení (UE) využívat WLAN pro IP konektivitu, často ve spojení s mobilním přístupem.

Z architektonického hlediska 3GPP definuje několik scénářů spolupráce. Pro 3G a 4G jádrová síť komunikuje s WLAN prostřednictvím specifických rozhraní, jako je S2a (pro důvěryhodný WLAN přístup k Packet Data Network Gateway - [PGW](/mobilnisite/slovnik/pgw/)) s použitím protokolů jako [GTP](/mobilnisite/slovnik/gtp/) nebo PMIPv6. Síťové entity jako ePDG (evolved Packet Data Gateway) poskytují zabezpečené [IPsec](/mobilnisite/slovnik/ipsec/) tunely pro nedůvěryhodný WLAN přístup. ANDSF poskytuje zařízení UE pravidla pro výběr sítě. V 5G připojuje Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) nedůvěryhodný non-3GPP přístup (jako veřejné Wi-Fi) k 5G Core, zatímco důvěryhodný WLAN se připojuje přímo k AMF/UPF. 5G jádro zachází s WLAN jako s dalším typem přístupu, což umožňuje plynulé ověřování (prostřednictvím 5G-AKA nebo EAP-AKA'), jednotné řízení politik a kontinuitu relace.

Jak to funguje: Dvou režimové UE zjistí dostupné WLAN sítě a na základě pravidel operátora (z ANDSF nebo politik UE) se může připojit k WLAN přístupovému bodu. Pro důvěryhodný přístup se UE ověří pomocí přihlašovacích údajů EAP-SIM/AKA/AKA' a získá IP konektivitu směrovanou přes jádrovou mobilní síť. Uživatelský provoz může být přesměrován lokálně na WLAN (Local Breakout) nebo směrován zpět do jádra (Home Routed). Klíčové specifikace 3GPP definují mechanismy ověřování, mobility, řízení politik a kvality služeb pro vytvoření jednotného uživatelského zážitku. Jejím úkolem je poskytnout vyšší kapacitu, zlepšit přenosové rychlosti v hustě obydlených oblastech, snížit přetížení mobilní sítě a umožnit konvergenci pevných a mobilních sítí.

## K čemu slouží

Integrace WLAN do standardů 3GPP byla motivována explozivním růstem Wi-Fi a potřebou mobilních operátorů využít nelicencované spektrum k přesměrování datového provozu z přetížených makro buněk mobilních sítí. Raná spolupráce mezi mobilními sítěmi a WLAN měla za cíl poskytnout jednoduchý přístup k internetu, ale účel se vyvinul k nabídce plynulého, zabezpečeného a pravidly řízeného přístupu k operátorským službám, čímž vytvořil kombinovanou služební strukturu mobilních sítí a WLAN.

Historicky počáteční práce ve vydání 6 definovaly volné propojení pro základní spolupráci. Pozdější vydání řešila omezení, jako je absence plynulé mobility, nekonzistentní zabezpečení a špatný uživatelský zážitek při přepínání sítí. Vývoj směrem k těsnější integraci, kdy EPC a 5GC zachází s WLAN jako s důvěryhodným přístupem, řeší problémy transparentnosti ověřování (pomocí stejných přihlašovacích údajů SIM), plynulé kontinuity relace (např. prostřednictvím IFOM nebo ATSSS) a konzistentní aplikace operátorských politik a účtování. To umožňuje operátorům spravovat WLAN jako nedílnou součást jejich strategie heterogenní sítě (HetNet), čímž zlepšuje celkovou efektivitu sítě a spokojenost uživatelů.

## Klíčové vlastnosti

- Přesměrování provozu z mobilní sítě na WLAN sítě
- Plynulé ověřování pomocí 3GPP přihlašovacích údajů (EAP-AKA')
- Výběr a zjišťování přístupové sítě založené na pravidlech (ANDSF/URSP)
- Podpora důvěryhodného a nedůvěryhodného WLAN přístupu k jádru
- Kontinuita relace a mobilita mezi 3GPP a WLAN (např. ATSSS)
- Integrace s 5G jádrem pro jednotné ověřování a řízení politik

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TR 22.906** (Rel-19) — IMS P2P Content Distribution Services
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- … a dalších 61 specifikací

---

📖 **Anglický originál a plná specifikace:** [WLAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/wlan/)
