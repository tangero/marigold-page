---
slug: "dra"
url: "/mobilnisite/slovnik/dra/"
type: "slovnik"
title: "DRA – Diameter Routing Agent"
date: 2025-01-01
abbr: "DRA"
fullName: "Diameter Routing Agent"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dra/"
summary: "Diameter Routing Agent (DRA) je síťový prvek, který zajišťuje směrovací a proxy funkce pro signalizační zprávy protokolu Diameter v Evolved Packet Core (EPC) a 5G Core (5GC). Je klíčový pro škálovatel"
---

DRA je síťový prvek, který zajišťuje směrovací a proxy funkce pro signalizační zprávy protokolu Diameter v EPC a 5G Core a centralizuje směrovací logiku pro škálovatelnou správu politik, účtování a autentizaci.

## Popis

Diameter Routing Agent (DRA) je základní komponenta signalizační architektury 3GPP založené na protokolu Diameter, používaná primárně v Evolved Packet Core (EPC) pro sítě LTE a v určitých scénářích propojení i s 5G Core (5GC). Funguje jako specializovaný relay agent protokolu Diameter, který zachytává, zkoumá a přeposílá zprávy Diameter mezi různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), jako jsou Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Jeho hlavní funkcí je provádět směrování na základě informací obsažených v těchto zprávách, včetně AVPs (Attribute-Value Pairs) Application-ID, Destination-Realm a Destination-Host. Tato směrovací inteligence odděluje síťové funkce od nutnosti mít přímé, statické znalosti adres všech ostatních, což je zásadní pro rozsáhlá nasazení s více dodavateli a pro usnadnění roamingu.

Z architektonického hlediska může DRA pracovat ve dvou hlavních režimech: bezstavovém (stateless) a stavovém (stateful). V bezstavovém režimu směruje DRA každý požadavek Diameter nezávisle na základě informací v dané jednotlivé zprávě. Ve stavovém režimu, který je povinný pro určité procedury jako rozhraní Gx pro řízení politik, DRA udržuje stav transakce. Spojuje tak požadavek a odpověď v rámci relace Diameter, což zajišťuje, že všechna následná signalizace pro danou relaci je směrována zpět přes stejnou instanci DRA a ke stejné následné síťové funkci (např. ke stejnému PCRF). Toto propojení relace je klíčové pro udržení konzistentního kontextu politik a účtování. DRA toho dosahuje vložením proprietárního [AVP](/mobilnisite/slovnik/avp/) Route-Record při přeposílání požadavku, který je pak použit pro směrování odpovídající odpovědi zpět.

Role DRA přesahuje pouhé jednoduché směrování. Poskytuje klíčové síťové funkce, jako je vyrovnávání zatížení (load balancing) mezi fondy síťových prvků (např. více PCRF), upřednostňování zpráv, skrývání topologie a funkčnost Diameter Edge Agent (DEA) pro roamingová rozhraní mezi operátory (např. S9, S6a). Tím, že funguje jako centrální směrovací uzel, dramaticky snižuje počet přímých spojení Diameter (síť typu NxN) potřebných mezi síťovými funkcemi, zjednodušuje správu sítě, zlepšuje škálovatelnost a zvyšuje odolnost sítě. V sítích 5G, zatímco Service-Based Architecture ([SBA](/mobilnisite/slovnik/sba/)) používá [HTTP](/mobilnisite/slovnik/http/)/2 a rozhraní založená na službách, zůstává DRA relevantní pro propojení s EPC, pro starší rozhraní Diameter a v rámci Binding Support Function ([BSF](/mobilnisite/slovnik/bsf/)) pro řízení politik v 5GC, což zajišťuje plynulý přechod mezi generacemi sítí.

## K čemu slouží

DRA byl zaveden, aby vyřešil kritické problémy škálovatelnosti a provozní výzvy vyplývající z přijetí protokolu Diameter jako primárního signalizačního protokolu pro politiky, účtování a autentizaci v 3GPP Evolved Packet Core (EPC) počínaje Release 8. Před zavedením DRA se předpokládalo, že síťové funkce jako PCRF, OCS a HSS budou komunikovat prostřednictvím přímých point-to-point spojení Diameter. Ve velké síti s více instancemi každé funkce to vytváří síť spojení typu NxN, kterou je složité zřizovat, spravovat a škálovat. Přidání nové síťové funkce by vyžadovalo rekonfiguraci všech existujících partnerských uzlů, což vede k provozní neefektivitě a potenciálním výpadkům služeb.

DRA tento problém řeší zavedením centralizované směrovací vrstvy. Jeho vytvoření bylo motivováno potřebou podpořit komerční nasazení zahrnující zařízení od více dodavatelů a usnadnit bezproblémový roaming mezi operátory. Bez DRA by roaming vyžadoval složité dvoustranné dohody a přímá spojení mezi každým HSS a PCRF navštívené sítě, což je nepraktické. DRA, fungující jako Diameter Edge Agent, poskytuje standardizovaný, zabezpečený bod vzájemného propojení pro roamingové partnery. Dále umožňuje pokročilé síťové schopnosti, jako je vyrovnávání zatížení a propojení relací, které jsou nezbytné pro spolehlivé řízení politik a účtování. Abstrahuje podkladovou síťovou topologii, což operátorům umožňuje škálovat, upgradovat nebo nahrazovat síťové funkce bez dopadu na celou signalizační strukturu.

## Klíčové vlastnosti

- Směrování zpráv Diameter na základě AVPs Application-ID, Realm a Host
- Stavové propojení relací (session binding) pro rozhraní Gx, Rx a další rozhraní politik/účtování
- Vyrovnávání zatížení (load balancing) mezi fondy síťových funkcí (např. PCRF, OCS)
- Skrývání topologie a funkčnost Diameter Edge Agent (DEA) pro roaming
- Redukce signalizačních spojení typu NxN na model hub-and-spoke
- Podpora jak bezstavového (stateless), tak stavového (transaction-stateful) režimu provozu

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 29.154** (Rel-19) — Nt Reference Point Protocol
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.809** (Rel-12) — Diameter Overload Control Study
- **TS 29.810** (Rel-13) — Diameter Load Control Study
- **TS 29.816** (Rel-10) — PCRF Failure & Restoration Study
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC

---

📖 **Anglický originál a plná specifikace:** [DRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dra/)
