---
slug: "mb-smf"
url: "/mobilnisite/slovnik/mb-smf/"
type: "slovnik"
title: "MB-SMF – Multicast/Broadcast Session Management Function"
date: 2026-01-01
abbr: "MB-SMF"
fullName: "Multicast/Broadcast Session Management Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mb-smf/"
summary: "Funkce jádra sítě 5G zavedená pro služby 5G Multicast-Broadcast (5G MBS). Spravuje zřizování, modifikaci a uvolňování multicast/broadcast relací, řídí prostředky uživatelské roviny a koordinuje s osta"
---

MB-SMF je funkce jádra sítě 5G, která spravuje zřizování, modifikaci a uvolňování multicast/broadcast relací a řídí prostředky uživatelské roviny pro efektivní doručování skupinových dat.

## Popis

Funkce pro správu multicast/broadcast relace (Multicast/Broadcast Session Management Function, MB-SMF) je specializovaná funkce jádra sítě 5G (5GC) definovaná ve specifikacích 3GPP od Release 17 pro podporu služeb 5G Multicast-Broadcast (5G [MBS](/mobilnisite/slovnik/mbs/)). Je zodpovědná za aspekty správy relací při přenosu dat z bodu do více bodů. Na rozdíl od standardní funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), která spravuje jednosměrné (unicast) PDU relace pro jednotlivá koncová zařízení (UE), spravuje MB-SMF multicast/broadcast relace určené pro skupinu koncových zařízení, například příjemců živého videosignálu, softwarových aktualizací nebo výstražných systémových zpráv.

Z architektonického hlediska je MB-SMF logická síťová funkce, kterou lze nasadit jako samostatnou entitu nebo společně s unicast SMF. S ostatními funkcemi jádra sítě komunikuje prostřednictvím architektury 5GC založené na službách. Mezi klíčová rozhraní patří rozhraní Nmbmf k funkci pro správu multicast/broadcast uživatelské roviny ([MB-UPF](/mobilnisite/slovnik/mb-upf/)) pro její řízení, rozhraní Namf k funkci pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) pro koordinaci připojování a odpojování koncových zařízení k relaci a rozhraní Npcf k funkci řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) pro uplatňování multicast-specifických politik. MB-SMF je zodpovědná za životní cyklus multicast relace: přijímá žádosti o zřízení relace (např. od aplikační funkce), přiděluje multicastovou IP adresu nebo identifikátor koncového bodu tunelu, vybírá a konfiguruje příslušnou MB-UPF nebo MB-UPF pro vytvoření multicastového distribučního stromu a spravuje kvalitu služby (QoS) pro multicastový datový tok.

Její provoz zahrnuje dva primární režimy: broadcast (kde jsou data zasílána všem koncovým zařízením v určité oblasti) a multicast (kde jsou data zasílána pouze koncovým zařízením, která se explicitně připojila ke skupině). MB-SMF úzce spolupracuje s rádiovým přístupovým sítem (RAN), která byla rozšířena o multicastové schopnosti (např. Single-Cell Point-To-Multipoint - SC-PTM, Multicast Broadcast Service - MBS). Poskytuje RAN nezbytné kontextové informace relace, včetně QoS profilů a informací pro směrování multicastového provozu. Pro multicastový režim také komunikuje s AMF pro správu dynamického připojování a odpojování koncových zařízení prostřednictvím funkce proxy pro [IGMP](/mobilnisite/slovnik/igmp/)/[MLD](/mobilnisite/slovnik/mld/) nebo přímé signalizace, čímž zajišťuje efektivní využití zdrojů rádiové a transportní sítě tím, že aktivuje multicastové přenosové kanály pouze v době a na místech, kde jsou aktivní příjemci.

## K čemu slouží

Funkce MB-SMF byla vytvořena, aby odstranila zásadní omezení sítí 5G před Release 17: absenci nativní, efektivní podpory služeb point-to-multipoint v jádru sítě 5G. Zatímco LTE se vyvinulo s eMBMS (evolved Multimedia Broadcast Multicast Service), počáteční specifikace 5G se zaměřovaly na ultra-spolehlivé nízkolatenční služby a hromadný IoT, přičemž broadcast/multicast zůstaly opomíjeny. MB-SMF řeší problém neefektivního využití zdrojů pro skupinovou komunikaci; používání unicastových přenosů pro doručování stejného obsahu (jako živý přenos sportovní události) tisícům uživatelů ve stejné buňce plýtvá cenným rádiovým spektrem i propustností jádra sítě.

Její vývoj byl motivován vznikajícími případy použití vyžadujícími efektivní hromadnou komunikaci, jako je živé streamování událostí, zábavní systémy v automobilech, komunikace pro veřejnou bezpečnost a bezdrátové aktualizace softwaru pro velké flotily IoT zařízení. MB-SMF jako součást ucelené architektury 5G [MBS](/mobilnisite/slovnik/mbs/) poskytuje standardizovaný, nativní síťový mechanismus pro správu těchto služeb. Odstraňuje omezení předchozích přístupů (jako bylo eMBMS v LTE, které mělo složitou integraci a omezené přijetí) tím, že je navržena od základů v rámci flexibilního, na službách založeného jádra 5G. To umožňuje dynamičtější správu relací, lepší integraci s unicastovými službami a podporu jak broadcastu, tak multicastu na vyžádání, což operátorům otevírá nové obchodní modely a služby.

## Klíčové vlastnosti

- Spravuje zřizování, modifikaci a uvolňování relací služby 5G MBS
- Podporuje jak režim broadcastového (na základě oblasti), tak multicastového (na základě skupiny) doručování
- Vybere a řídí funkci multicast/broadcast uživatelské roviny (MB-UPF) pro správu uživatelské roviny
- Poskytuje rádiové přístupové síti (RAN) kontext multicastové relace a parametry QoS
- Zpracovává dynamické procedury připojování a odpojování koncových zařízení (UE) k multicastovým relacím (např. prostřednictvím proxy pro IGMP/MLD)
- Komunikuje s PCF pro uplatňování multicast-specifických politik a s AMF pro koordinaci koncových zařízení

## Související pojmy

- [MB-UPF – Multicast/Broadcast User Plane Function](/mobilnisite/slovnik/mb-upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 29.537** (Rel-19) — 5G Multicast/Broadcast Policy Control Services
- **TS 29.581** (Rel-19) — MBSTF Service Based Interface Protocol Specification
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.290** (Rel-19) — 5G Charging for Service Based Interface
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [MB-SMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mb-smf/)
