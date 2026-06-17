---
slug: "drb"
url: "/mobilnisite/slovnik/drb/"
type: "slovnik"
title: "DRB – Data Radio Bearer"
date: 2025-01-01
abbr: "DRB"
fullName: "Data Radio Bearer"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/drb/"
summary: "Data Radio Bearer (DRB) je logický kanál zřízený mezi uživatelským zařízením (UE) a základnovou stanicí (eNodeB/gNB) pro přenos dat v uživatelské rovině. Jde o klíčový koncept v LTE a 5G NR, který zaj"
---

DRB je logický kanál mezi uživatelským zařízením a základnovou stanicí, který přenáší datový provoz uživatele se specifickým zacházením z hlediska kvality služby v sítích LTE a 5G.

## Popis

Data Radio Bearer (DRB) je základní konstrukcí v rádiovém protokolovém zásobníku LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a 5G NR (NG-RAN). Představuje logické spojení neboli „potrubí“ přes rozhraní Uu, které je výhradně určeno pro přenos dat uživatelské roviny pro konkrétní službu nebo aplikační tok. Každý DRB je nakonfigurován specifickou sadou protokolových vrstev a parametrů, které definují, jak jsou data zpracovávána, chráněna a přenášena mezi UE a uzlem přístupové sítě (RAN) – eNodeB v LTE nebo gNB v 5G NR. DRB je místem, kde je diferenciace QoS fyzicky vynucována na rádiovém spoji.

Zřízení a konfigurace DRB jsou řízeny uzlem RAN prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). Když UE zahájí datovou relaci (PDU Session v 5G nebo EPS Bearer v LTE), základnová síť (5GC nebo EPC) požaduje nastavení QoS toku (5G) nebo EPS beareru se specifickými charakteristikami QoS ([QCI](/mobilnisite/slovnik/qci/)/[5QI](/mobilnisite/slovnik/5qi/), [ARP](/mobilnisite/slovnik/arp/), [GBR](/mobilnisite/slovnik/gbr/) atd.). Uzel RAN tento požadavek přeloží do konfigurace jednoho nebo více DRB. Klíčovou funkcí je mapování QoS: RAN mapuje více QoS toků (v 5G) nebo Service Data Flows (v LTE) se shodnými požadavky na QoS na jeden DRB. Každý DRB je asociován se specifickou hodnotou 5QI/QCI, která určuje jeho zacházení z hlediska plánovací priority, rozpočtu zpoždění paketů a míry chybovosti.

Technicky je DRB realizován konfigurací vrstev Packet Data Convergence Protocol (PDCP), Radio Link Control (RLC) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). PDCP poskytuje kompresi hlaviček, šifrování a ochranu integrity. RLC zajišťuje segmentaci, konkatenaci a opravu chyb prostřednictvím [ARQ](/mobilnisite/slovnik/arq/). MAC provádí plánování, priorizaci logických kanálů a multiplexování více DRB (a SRB) na sdílené transportní kanály. Fyzická vrstva (PHY) následně data přenáší přes rozhraní. DRB je identifikován pomocí DRB ID a jeho životní cyklus – zřízení, modifikace (např. pro předání spojení nebo změnu QoS) a uvolnění – je dynamicky řízen tak, aby odpovídal datové aktivitě uživatele a událostem mobility, což zajišťuje efektivní využití rádiových zdrojů při splnění požadované kvality služby.

## K čemu slouží

Koncept DRB byl zaveden spolu s LTE ve specifikaci 3GPP Release 8, aby poskytl flexibilní a efektivní mechanismus pro poskytování IP služeb se zaručenou kvalitou služby (QoS) přes rádiový spoj. Řešil omezení předchozích 3G systémů, kde bylo mapování mezi nosiči základnové sítě a rádiovými kanály méně flexibilní. Primární problém, který řeší, je efektivní převod požadavků na QoS ze základnové sítě do konkrétní alokace a zacházení s rádiovými zdroji.

V systémech před LTE byly rádiové nosiče často pevněji vázány na konkrétní služby. DRB spolu s rámcem QCI (QoS Class Identifier) vytvořil standardizovaný, granulární způsob aplikace různých chování při přeposílání paketů (plánování, správa front atd.) na základě typu služby (např. hlas, video, prohlížení webu). To umožňuje síťovým operátorům upřednostňovat citlivý provoz na latenci, jako je VoIP, před provozem typu best-effort, čímž zlepšují uživatelský zážitek. Dynamická povaha DRB navíc umožňuje síti zřizovat nosiče na vyžádání při aktivaci služeb, čímž šetří rádiové zdroje, když nejsou potřeba. V 5G NR se účel vyvinul tak, aby podporoval ještě flexibilnější model QoS s QoS toky. DRB funguje jako kontejner RAN pro tyto toky, umožňuje jejich efektivní agregaci a snižuje signalizační režii. Je klíčovým prvkem pro síťové segmentování na rádiové úrovni, protože různé segmenty mohou být podporovány různými sadami DRB s odlišnými QoS profily, což izoluje výkon mezi segmenty.

## Klíčové vlastnosti

- Logický transportní kanál pro data uživatelské roviny přes rozhraní Uu
- Konfigurován prostřednictvím signalizace RRC se specifickými parametry PDCP, RLC a MAC
- Mapuje jeden nebo více QoS toků (5G) nebo SDF (LTE) se shodnými požadavky na QoS
- Asociován s hodnotou 5QI (5G) nebo QCI (LTE) definující plánovací prioritu a zacházení s pakety
- Podporuje dynamické zřízení, modifikaci a uvolnění na základě poptávky po službách a mobility
- Umožňuje vynucení QoS na rádiové úrovni a izolaci výkonu v rámci síťového segmentování

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 33.853** (Rel-17) — Study on User Plane Integrity Protection
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.314** (Rel-19) — E-UTRA Radio Measurements Specification
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.360** (Rel-19) — LTE-WLAN Aggregation Adaptation Protocol
- **TS 36.361** (Rel-19) — LWIP Encapsulation Protocol Specification
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions
- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TS 37.480** (Rel-19) — E1 Interface General Aspects and Principles
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.460** (Rel-19) — E1 Interface General Aspects and Principles
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [DRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/drb/)
