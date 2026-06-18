---
slug: "sfc"
url: "/mobilnisite/slovnik/sfc/"
type: "slovnik"
title: "SFC – Service Function Chain"
date: 2026-01-01
abbr: "SFC"
fullName: "Service Function Chain"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sfc/"
summary: "Service Function Chain (SFC) je uspořádaná posloupnost síťových funkcí (např. firewallů, vyrovnávačů zatížení), přes které je směrován provoz za účelem poskytnutí konkrétní služby. V 3GPP umožňuje fle"
---

SFC je uspořádaná posloupnost síťových funkcí, přes které je směrován provoz, aby umožnila flexibilní poskytování služeb a síťové krájení (network slicing) v systémech 3GPP.

## Popis

Service Function Chain definuje orientovaný graf služebních funkcí (Service Functions, [SF](/mobilnisite/slovnik/sf/)), které musí být aplikovány na pakety nebo toky v určitém pořadí, aby byla realizována síťová služba. V architektuře 3GPP, zejména v rámci 5G Core sítě, je SFC klíčovým prvkem pro síťové krájení a služebně orientované směrování provozu. Řetězec je popsán Deskriptorem síťové služby (Network Service Descriptor, [NSD](/mobilnisite/slovnik/nsd/)), který zahrnuje topologii a požadavky virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) a/nebo kontejnerizovaných síťových funkcí ([CNF](/mobilnisite/slovnik/cnf/)) tvořících službu.

Implementace SFC zahrnuje několik komponent: Service Function Forwarder (SFF), který směruje provoz mezi SF, SFC Classifier, který mapuje příchozí pakety na konkrétní řetězec na základě politik, a SFC Proxy, který může adaptovat provoz pro starší SF. Provoz je často zapouzdřen s hlavičkou síťové služby (Network Service Header, NSH) nebo podobnými metadaty, která nesou kontext SFC včetně identifikátoru řetězce a pozice, čímž zajišťují, že pakety projdou správnou posloupností funkcí bez ohledu na podkladovou síťovou topologii.

V rámci 3GPP je SFC spravována funkcí Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)) a Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) ve spolupráci s Service Communication Proxy ([SCP](/mobilnisite/slovnik/scp/)). Umožňuje vytváření end-to-end síťových řezů, kde každý řez může mít svůj vlastní unikátní SFC přizpůsobený specifickým požadavkům služby, jako je rozšířené mobilní širokopásmové připojení (eMBB), ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) nebo hromadný IoT. Tato orchestrace je typicky řízena systémy pro správu a orchestraci (MANO), jako je NFV Orchestrator (NFVO) a SDN kontroléry.

## K čemu slouží

Service Function Chaining byl vytvořen, aby řešil rigiditu tradičních nasazení založených na hardwarových middleboxech, kde byly síťové služby implementovány jako fyzická zařízení na pevných místech a v pevných sekvencích. To činilo inovace služeb, škálování a údržbu nákladnými a pomalými. SFC, umožněný virtualizací síťových funkcí (NFV) a softwarově definovanými sítěmi (SDN), umožňuje operátorům dynamicky skládat a nasazovat řetězce virtualizovaných funkcí, což vede k agilní tvorbě služeb a efektivnímu využití zdrojů.

Vývoj směrem k 5G a síťovému krájení si vyžádal mechanismus pro poskytování izolovaných, přizpůsobených logických sítí nad sdílenou fyzickou infrastrukturou. SFC poskytuje technický rámec pro realizaci těchto řezů tím, že definuje, jak je provoz pro konkrétního nájemce nebo typ služby zpracován přes specifickou sadu funkcí (např. firewall, NAT, optimalizér TCP, optimalizér videa). Řeší problém statických, monolitických síťových architektur tím, že umožňuje automatizované, politikami řízené směrování provozu.

Dále SFC podporuje interoperabilitu více dodavatelů a automatizaci služeb. Standardizací logiky řetězení a hlaviček (např. prostřednictvím spolupráce IETF a 3GPP) zabraňuje závislosti na dodavateli a umožňuje smíšená prostředí. Tato schopnost je klíčová pro splnění rozmanitých požadavků 5G případů užití, což operátorům umožňuje rychle nasazovat nové služby generující příjmy se zaručenými výkonnostními a bezpečnostními charakteristikami.

## Klíčové vlastnosti

- Definuje uspořádanou posloupnost virtualizovaných nebo kontejnerizovaných služebních funkcí
- Umožňuje dynamické, politikami řízené směrování provozu pro síťové řezy
- Využívá zapouzdření metadat (např. NSH) pro identifikaci řetězce a stav
- Orchestrována systémy MANO (NFVO) a řízena principy SDN
- Podporuje automatizaci služeb a správu životního cyklu řetězců funkcí
- Umožňuje end-to-end síťové krájení s přizpůsobenými datovými cestami

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [SFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfc/)
