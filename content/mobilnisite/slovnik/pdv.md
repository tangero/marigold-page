---
slug: "pdv"
url: "/mobilnisite/slovnik/pdv/"
type: "slovnik"
title: "PDV – Packet Delay Variation"
date: 2026-01-01
abbr: "PDV"
fullName: "Packet Delay Variation"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdv/"
summary: "Packet Delay Variation (PDV, variace zpoždění paketů) je klíčová metrika kvality služeb (QoS), která měří variaci latence mezi pakety v datovém toku. Je zásadní pro časově citlivé aplikace, jako jsou"
---

PDV je klíčová metrika kvality služeb (QoS), která měří variaci latence mezi pakety v datovém toku.

## Popis

Packet Delay Variation (PDV, variace zpoždění paketů), často synonymní s pojmem jitter v IP sítích, je v 3GPP formálně definována jako rozdíl v koncové latenci mezi vybranými pakety v toku, přičemž ztracené pakety jsou ignorovány. Jde o statistickou míru, typicky vypočítanou jako rozdíl mezi maximálním a minimálním zpožděním paketů pozorovaným v konkrétním měřicím intervalu nebo okně. V systémech 5G je PDV základním parametrem pro služby Ultra-Reliable Low-Latency Communication ([URLLC](/mobilnisite/slovnik/urllc/)) a deterministické sítě. Síť využívá požadavky na PDV, specifikované ve smlouvách o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) nebo v 5G QoS indikátorech ([5QI](/mobilnisite/slovnik/5qi/)), k alokaci prostředků a konfiguraci plánovacích algoritmů v rádiové přístupové síti (RAN) i v jádře sítě (Core Network), aby zajistila doručení paketů v omezeném okně zpoždění.

Architektonicky zahrnuje správa PDV koordinaci napříč více síťovými funkcemi. Funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) definuje politiky PDV na základě dat o předplatném a požadavků aplikační funkce. Funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) tyto politiky vynucuje konfigurací příslušných QoS toků a pravidel pro funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a gNB. V RAN se pro minimalizaci zpoždění ve frontách a jeho variací používají algoritmy plánování paketů, jako je časově řízené tvarování definované v [IEEE](/mobilnisite/slovnik/ieee/) 802.1Qbv. UPF provádí police provozu a značkování, aby pakety nesplňující podmínky nepříznivě neovlivnily PDV jiných toků.

PDV se měří end-to-end, od zdrojového aplikačního serveru k uživatelskému zařízení (UE), nebo na konkrétních síťových segmentech. Metodologie měření jsou definovány ve specifikacích jako 29.122 (rozhraní N5) a 29.514 ([CAPIF](/mobilnisite/slovnik/capif/)), které poskytují rámce pro expozici a analytiku. Mezi klíčové komponenty zajištění PDV patří funkce síťové datové analytiky (NWDAF), která může shromažďovat metriky PDV a předpovídat porušení, a 5G přístupová síť (5G-AN), která musí poskytovat nízkou a předvídatelnou latenci pomocí technik jako mini-sloty, grant-free uplink a pre-emptivní přístup. Jejím úkolem je umožnit deterministický výkon, který je základním kamenem pro transformaci 5G z datové sítě typu best-effort na platformu pro kritické komunikační služby.

## K čemu slouží

PDV bylo zavedeno, aby řešilo přísné požadavky nově vznikajících aplikací v reálném čase a interaktivních aplikací v sítích 5G a novějších. Tradiční mobilní sítě optimalizované pro propustnost a průměrnou latenci byly nedostatečné pro aplikace, jako jsou autonomní vozidla, vzdálená chirurgie a hmatový internet, kde je klíčová nejen nízká latence, ale také její předvídatelnost a konzistence. Vysoká PDV (jitter) může způsobit přetečení/podtečení vyrovnávacích pamětí, zhoršenou kvalitu zvuku/videa a nestabilitu řízení v kyberneticko-fyzikálních systémech. Zavedení PDV jako standardizovaného parametru QoS v Rel-18 bylo motivováno potřebou tento aspekt výkonu v rámci 3GPP formálně kvantifikovat, spravovat a garantovat.

Historicky se jitter řešil na aplikační vrstvě nebo v izolovaných podnikových sítích. Omezením byl nedostatek standardizované kontroly s ohledem na síť. Standardizace PDV v 3GPP umožňuje síti být vnitřně vědoma tolerance aplikace na variaci zpoždění a podle toho rezervovat a konfigurovat prostředky v celém mobilním paketovém jádru a RAN. To řeší problém best-effort přístupu ke kritickým datovým tokům ve sdílené infrastruktuře a umožňuje síťové segmentování (network slicing) pro vertikální odvětví s přesnými časovými požadavky. Představuje posun od reaktivního řízení přetížení k proaktivní deterministické záruce služeb.

## Klíčové vlastnosti

- Standardizovaný parametr QoS 3GPP pro systém 5G (5GS) definovaný v TS 23.501
- Klíčový pro umožnění služeb Ultra-Reliable Low-Latency Communication (URLLC)
- Spravován end-to-end prostřednictvím řízení politik (PCF) a správy relací (SMF)
- Podporuje síťové segmentování (network slicing) tím, že poskytuje deterministický výkon v rámci segmentu
- Měření a expozice definovány pro správu a analytiku (např. prostřednictvím CAPIF)
- Ovlivňuje plánování v RAN a směrování provozu v jádře sítě za účelem minimalizace variace

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [PDV na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdv/)
