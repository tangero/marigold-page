---
slug: "um"
url: "/mobilnisite/slovnik/um/"
type: "slovnik"
title: "UM – Unacknowledged Mode"
date: 2026-01-01
abbr: "UM"
fullName: "Unacknowledged Mode"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/um/"
summary: "Unacknowledged Mode (UM) je režim protokolu řízení rádiového spoje (RLC), který poskytuje službu nepotvrzovaného přenosu dat. Zajišťuje doručení protokolových datových jednotek (PDU) vyšší vrstvy ve s"
---

UM je režim protokolu RLC pro nepotvrzovaný přenos dat, který zajišťuje doručení ve správném pořadí, nikoli však zaručené doručení, což jej činí vhodným pro provoz citlivý na zpoždění, jako je hlas nebo video.

## Popis

Unacknowledged Mode (UM) je jeden ze tří provozních režimů vrstvy řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) v bezdrátových systémech 3GPP, vedle Acknowledged Mode ([AM](/mobilnisite/slovnik/am/)) a Transparent Mode ([TM](/mobilnisite/slovnik/tm/)). Vrstva RLC se nachází jak v uživatelském zařízení (UE), tak v uzlu rádiové přístupové sítě (RAN) (např. NodeB, eNodeB, gNB) a je zodpovědná za přenos protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) vyšších vrstev. V UM je hlavní funkcí nepotvrzovaný přenos dat. To znamená, že vysílající RLC entita odesílá RLC PDU bez očekávání kladného nebo záporného potvrzení od přijímače. Následně v tomto režimu na úrovni RLC neexistuje mechanismus automatického opakovaného dotazu ([ARQ](/mobilnisite/slovnik/arq/)) pro opravu chyb. Protokol provádí segmentaci a konkatenaci RLC servisních datových jednotek ([SDU](/mobilnisite/slovnik/sdu/)) z vyšších vrstev do RLC PDU pro přenos a na straně přijímače opětovné sestavení těchto PDU zpět na SDU.

Z architektonického hlediska má RLC entita nakonfigurovaná v UM vysílací a přijímací stranu. Vysílací strana obsahuje vysílací buffer a funkce pro segmentaci/konkatenaci a konstrukci PDU. Klíčovou součástí je číslování sekvence. Každému RLC PDU je přiřazeno pořadové číslo v konečném rozsahu, které je zahrnuto v hlavičce PDU. Toto pořadové číslo je zásadní pro činnost přijímače. Přijímací strana využívá buffer pro opětovné sestavení. Používá pořadová čísla k detekci chybějících PDU (způsobených chybami nebo ztrátou na rozhraní vzduchu) a k zajištění doručení RLC SDU vyšší vrstvě ve správném pořadí. Protože doručení není zaručeno, detekovaná chybějící PDU nejsou vyžadována k retransmisi; místo toho může RLC doručit částečně sestavené SDU nebo indikovat chybu, v závislosti na konfiguraci a povaze služby vyšší vrstvy.

Úloha UM v síti je podporovat služby citlivé na zpoždění a kolísání zpoždění (jitter), které však snášejí určitou úroveň ztráty paketů. Nepřítomnost ARQ retransmisí se vyhýbá zavedení proměnlivého a potenciálně velkého zpoždění, které přichází s čekáním na potvrzení a prováděním retransmisí. To činí UM ideálním pro služby reálného času přenášené přes paketově spínané sítě, jako je Voice over IP (VoIP) využívající IP Multimedia Subsystem (IMS) nebo streamované video. Funkce doručení ve správném pořadí je stále důležitá pro zachování pořadí paketů, protože doručení mimo pořadí by mohlo vážně degradovat kvalitu těchto aplikací reálného času. Konfigurace UM (např. velikost pole pořadového čísla) je určena vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) na základě požadavků zřízeného rádiového nosiče.

## K čemu slouží

Unacknowledged Mode byl vytvořen pro efektivní podporu služeb reálného času, streamování a vysílání/multicastu přes paketově spínané sítě 3GPP. Před rozšířením paketových dat měla okruhově spínaná hlasová služba garantované kanály s konstantní přenosovou rychlostí. S přechodem na služby založené na IP byl potřebný mechanismus pro přenos IP paketů citlivých na zpoždění přes nespolehlivý bezdrátový spoj bez zavedení režie latence protokolů s retransmisemi. Čisté, nespojované IP doručení by mohlo vést k paketům mimo pořadí, což způsobuje špatný výkon aplikace. UM to řeší poskytnutím odlehčené, spojované služby spojové vrstvy, která přidává číslování sekvence pro doručení ve správném pořadí, ale záměrně vynechává potvrzení a retransmise, aby byla latence minimální.

Problém, který řeší, je základní kompromis mezi spolehlivostí a latencí. Acknowledged Mode ([AM](/mobilnisite/slovnik/am/)) s ARQ poskytuje vysokou spolehlivost, ale proměnlivou, potenciálně vysokou latenci, což je vhodné pro datový provoz, jako je prohlížení webu nebo přenos souborů. Pro konverzační provoz reálného času nebo streamování je tato latence nepřijatelná. Transparent Mode (TM) nabízí ještě nižší režii zpracování, ale neposkytuje segmentaci ani doručení ve správném pořadí, což omezuje jeho použití. UM zaujímá kritickou střední pozici, přidává nezbytné funkce sekvencování a opětovného sestavení pro paketové služby reálného času a zároveň se vyhýbá penalizaci zpoždění mechanismů spolehlivosti. Jeho vytvoření bylo motivováno potřebou definovat diferenciaci kvality služeb (QoS) na vrstvě RLC, což umožňuje síti optimalizovat přenos pro různé typy provozu, což je základním kamenem architektury Universal Mobile Telecommunications System (UMTS) a následných architektur 4G a 5G.

## Klíčové vlastnosti

- Poskytuje službu nepotvrzovaného přenosu dat bez ARQ retransmisí
- Zajišťuje doručení PDU vyšší vrstvy ve správném pořadí pomocí pořadových čísel
- Provádí segmentaci a konkatenaci RLC SDU pro efektivní přenos
- Detekuje chybějící PDU na přijímači, ale nevyžaduje jejich retransmisi
- Používá konfigurovatelnou velikost pole pořadového čísla (např. 5, 10 bitů pro LTE)
- Optimalizováno pro provoz citlivý na zpoždění a tolerantní k chybám, jako je VoIP a streamování

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [VOIP – Voice over IP](/mobilnisite/slovnik/voip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TR 24.980** (Rel-16) — MCPTT IMS Profile for Gm Reference Point
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [UM na 3GPP Explorer](https://3gpp-explorer.com/glossary/um/)
