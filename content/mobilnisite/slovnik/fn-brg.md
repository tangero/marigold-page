---
slug: "fn-brg"
url: "/mobilnisite/slovnik/fn-brg/"
type: "slovnik"
title: "FN-BRG – Fixed Network Broadband Residential Gateway"
date: 2026-01-01
abbr: "FN-BRG"
fullName: "Fixed Network Broadband Residential Gateway"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fn-brg/"
summary: "FN-BRG je standardizovaná domácí brána pro pevný širokopásmový přístup v architektuře systému 5G. Slouží jako zařízení na straně zákazníka (CPE), které připojuje domácnosti k jádru sítě 5G prostřednic"
---

FN-BRG je standardizovaná domácí brána v systémech 5G, která slouží jako zařízení na straně zákazníka (customer premises equipment) pro připojení domácností prostřednictvím pevného širokopásmového přístupu k jádru sítě 5G.

## Popis

Fixed Network Broadband Residential Gateway (FN-BRG) je síťová funkce a fyzické zařízení definované ve specifikaci 3GPP Release 16 a novějších jako součást architektury 5G System (5GS) pro konvergenci pevných bezdrátových a drátových sítí. Nachází se na straně zákazníka a ukončuje pevnou přístupovou linku (např. [GPON](/mobilnisite/slovnik/gpon/) optické vlákno, [DOCSIS](/mobilnisite/slovnik/docsis/) kabel nebo Ethernet). FN-BRG funguje jako User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a potenciálně i jako část řídicí roviny pro provoz rezidenčního uživatele při přístupu k jádru sítě 5G (5GC). V podstatě rozšiřuje architekturu založenou na službách (service-based architecture) 5GC do domácí sítě a zachází s pevným širokopásmovým připojením jako s dalším typem přístupu 5G.

Architektonicky se FN-BRG připojuje k jádru sítě 5G prostřednictvím rozhraní N3 (uživatelská rovina) a [N2](/mobilnisite/slovnik/n2/) (řídicí rovina), obdobně jako se připojuje gNB u mobilního přístupu. Obsahuje instanci UPF, která zajišťuje směrování paketů, přeposílání, vynucování QoS a měření provozu pro datové toky rezidenčního účastníka. Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5GC spravují řídicí rovinu FN-BRG. Klíčové specifikace jako TS 23.501 (systémová architektura) a TS 23.316 (vývoj drátového přístupu) detailně popisují její integraci. FN-BRG se k 5GC autentizuje pomocí 5G Authentication and Key Agreement (5G-AKA) nebo metod založených na [EAP](/mobilnisite/slovnik/eap/), přičemž využívá Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro přihlašovací údaje účastníka.

Jeho provoz zahrnuje vytvoření Packet Data Unit (PDU) session pro rezidenčního účastníka, stejně jako u mobilního zařízení. FN-BRG zapouzdřuje/rozpouzdřuje uživatelský provoz do tunelů GTP-U (přes N3) směrem k UPF v jádru nebo k jiným datovým sítím. Aplikuje pravidla QoS (mapování 5QI) přijatá od SMF přes rozhraní N4, aby vhodně prioritizovala provoz (např. hlas, video) na pevné přístupové lince. FN-BRG také poskytuje typické funkce domácí brány, jako je Network Address Translation (NAT), firewall, DHCP server a přístupový bod Wi-Fi, které jsou nyní spravovány a orchestraovány prostřednictvím síťových řezů a politik 5G, což umožňuje skutečnou paritu služeb pro pevné a mobilní sítě.

## K čemu slouží

FN-BRG byl vytvořen za účelem plné integrace vysoce výkonného pevného širokopásmového přístupu do architektury založené na službách 5G, čímž reaguje na průmyslový trend Fixed Mobile Convergence (FMC). Před Release 16 byly pevné širokopásmové sítě (DSL, optika) a mobilní sítě (4G/5G) do značné míry oddělené domény s různými systémy správy, řízení politik a mechanismy poskytování služeb. Toto oddělení vedlo k provozní složitosti, neschopnosti nabízet jednotné smlouvy o úrovni služeb (SLA) napříč typy přístupu a k promarněným příležitostem pro optimalizaci síťových zdrojů.

FN-BRG tento problém řeší tím, že z domácí brány dělá plnohodnotnou součást jádra 5G. Umožňuje operátorům využívat jediné, jednotné jádro 5G (s jeho cloud-nativními, škálovatelnými a řezům-aware schopnostmi) k poskytování služeb jak mobilním, tak pevným účastníkům. To umožňuje vytváření síťových řezů, které pokrývají oba typy přístupu – například jeden řez URLLC (ultra-reliable low-latency communication) může obsluhovat mobilní roboty ve výrobním závodě i jeho senzory připojené pevnou linkou. Také zjednodušuje uživatelský zážitek tím, že poskytuje jednotnou identitu, politiky a fakturační profil bez ohledu na to, zda se uživatel připojuje prostřednictvím smartphonu přes 5G rádiové rozhraní nebo notebooku přes domácí Wi-Fi přes FN-BRG. Motivace vychází z touhy operátorů snížit náklady prostřednictvím konsolidovaných síťových jader a rychleji uvádět inovativní konvergované služby (jako plynulé předání videohovoru z mobilní sítě na domácí Wi-Fi).

## Klíčové vlastnosti

- Funguje jako 5G User Plane Function (UPF) na straně zákazníka pro pevný přístup
- Připojuje se k jádru 5G prostřednictvím standardizovaných rozhraní N2 (řídicí rovina) a N3 (uživatelská rovina)
- Podporuje 5G autentizaci (5G-AKA) a zabezpečené tunelování (GTP-U) pro provoz účastníka
- Vynucuje politiky QoS 5G (5QI) na pevné přístupové lince pro diferenciaci služeb
- Umožňuje integraci pevného přístupu do síťových řezů 5G pro zajištění služeb end-to-end
- Poskytuje jednotné rozhraní pro správu a orchestraci prostřednictvím jádra 5G (např. prostřednictvím NFs)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [FN-BRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/fn-brg/)
