---
slug: "psc"
url: "/mobilnisite/slovnik/psc/"
type: "slovnik"
title: "PSC – Packet-Switched Conversational service"
date: 2025-01-01
abbr: "PSC"
fullName: "Packet-Switched Conversational service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psc/"
summary: "Třída QoS definovaná v rámci paketově orientované domény 3GPP pro konverzační služby v reálném čase obousměrné komunikace, jako je Voice over IP (VoIP) a videotelefonie. Je charakterizována přísnými p"
---

PSC je třída kvality služeb (QoS) v paketově orientované síti 3GPP pro konverzační služby v reálném čase, jako je VoIP, charakterizovaná přísnými požadavky na nízké zpoždění, nízký jitter a symetrickou šířku pásma.

## Popis

Služba Packet-Switched Conversational (PSC) je základní třída kvality služeb (QoS) definovaná ve standardech 3GPP, konkrétně v rámci IP Multimedia Subsystem (IMS) a Evolved Packet System (EPS). Představuje třídu provozu s nejvyšší prioritou pro služby reálného času a obousměrné komunikace přenášené přes paketově orientované sítě. Třída PSC je navržena tak, aby napodobovala charakteristiky tradičních hovorů v přepojování okruhů, ale přes infrastrukturu založenou na IP. Mezi klíčové technické parametry definující tuto třídu patří nízké přenosové zpoždění (typicky cílem je méně než 100 ms jednosměrně), nízká variabilita zpoždění (jitter) a nízká, ale nenulová přijatelná míra ztráty paketů. Požadavek na šířku pásma je typicky symetrický, což odráží povahu konverzace, kdy obě strany vysílají i přijímají.

Z architektonického hlediska je třída PSC implementována prostřednictvím interakce několika síťových funkcí. Když uživatel zahájí VoIP nebo video hovor přes IMS, [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function) komunikuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) v jádru sítě. PCRF převádí požadavek na službu na konkrétní parametry QoS (QoS Class Identifier - [QCI](/mobilnisite/slovnik/qci/), Allocation and Retention Priority - [ARP](/mobilnisite/slovnik/arp/), Guaranteed Bit Rate - [GBR](/mobilnisite/slovnik/gbr/)), které jsou vynucovány na úrovni přenosového kanálu. V LTE/EPC a 5G/5GC to znamená vytvoření vyhrazeného přenosového kanálu (v LTE) nebo QoS Flow (v 5G) s QCI 1 (pro konverzační hlas) nebo QCI 2 (pro konverzační video). Tyto přenosové kanály/QoS Flow získávají nejvyšší prioritu plánování na rádiovém rozhraní (např. jsou upřednostňovány plánovačem eNodeB/gNodeB) a preferenční zacházení v transportní síti, aby bylo dosaženo přísného rozpočtu zpoždění.

Třída PSC funguje tak, že poskytuje rezervaci prostředků a řízení přístupu. Před zahájením konverzační relace síť provede kontrolu řízení přístupu, aby zajistila, že jsou k dispozici dostatečné prostředky (rádiové, transportní) pro zaručení požadované GBR. Pokud prostředky nejsou dostatečné, hovor může být blokován, aby byla chráněna kvalita stávajících PSC relací. Během relace značkování paketů (např. pomocí DiffServ Code Points - [DSCP](/mobilnisite/slovnik/dscp/) v IP vrstvě) zajišťuje, že směrovače v transportní síti mohou tyto pakety identifikovat a upřednostnit. Na rádiovém rozhraní plánovač v základnové stanici používá QCI k upřednostnění přenosu dat z PSC přenosových kanálů před provozem s nižší prioritou (jako je streamování nebo dat na pozadí), čímž zajišťuje nízkou latenci i při zatížení buňky.

## K čemu slouží

Třída služby PSC byla vytvořena, aby umožnila migraci tradičních telekomunikačních služeb s přepojováním okruhů (hlasové a video hovory) na plně IP, paketově orientované sítě nové generace (jako 3G, LTE a 5G). Před její definicí měly mobilní sítě oddělené domény s přepojováním okruhů pro hlas a paketově orientované domény pro data. Tento dvoudoménový přístup byl neefektivní a omezoval inovace služeb. Třída PSC řeší problém poskytování kvality hlasu a videa na úrovni operátora přes best-effort IP síť zavedením přísných záruk QoS.

Její motivace vycházela z úsilí průmyslu o konvergenci sítí a ekonomických výhod udržování jediné, na IP založené transportní sítě pro všechny služby. Omezení předchozích přístupů byla zřejmá: bez definované konverzační třídy by VoIP provoz soutěžil na stejné úrovni s prohlížením webu nebo stahováním souborů na paketově orientovaném přenosovém kanálu, což by vedlo k nepřijatelné kvalitě hovorů charakterizované výpadky, vysokou latencí a jitterem. Vytvoření třídy PSC spolu s přidruženou architekturou IMS umožnilo operátorům nabízet Voice over LTE (VoLTE) a později Voice over 5G (VoNR) s kvalitou rovnou nebo lepší než u starších hovorů s přepojováním okruhů, a zároveň umožnilo rozvinuté komunikační služby ([RCS](/mobilnisite/slovnik/rcs/)) a videotelefonii na stejné IP infrastruktuře.

## Klíčové vlastnosti

- Definována přísnými požadavky na nízkou latenci a nízký jitter
- Používá symetrické přenosové kanály/QoS Flow se zaručenou přenosovou rychlostí (GBR)
- Je asociována s hodnotami QCI s vysokou prioritou (1 pro hlas, 2 pro video)
- Vyžaduje řízení přístupu na síťové úrovni pro zaručení prostředků
- Umožňuje kvalitu Voice over IP (VoIP) a videotelefonie na úrovni operátora
- Základní pro konverzační služby založené na IMS

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TR 26.944** (Rel-19) — QoE, ESQoS and SQoS metrics for 3G multimedia services
- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [PSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/psc/)
