---
slug: "amd"
url: "/mobilnisite/slovnik/amd/"
type: "slovnik"
title: "AMD – Acknowledged Mode Data"
date: 2025-01-01
abbr: "AMD"
fullName: "Acknowledged Mode Data"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/amd/"
summary: "AMD je režim protokolu řízení rádiového spoje (RLC) v sítích 3GPP, který zajišťuje spolehlivé doručování dat prostřednictvím mechanismů automatického opakování (ARQ). Poskytuje opravu chyb, doručování"
---

AMD je režim protokolu řízení rádiového spoje (RLC) v sítích 3GPP, který zajišťuje spolehlivé doručování dat pomocí automatického opakování (ARQ) pro opravu chyb, doručování ve správném pořadí a detekci duplicit.

## Popis

Acknowledged Mode Data (AMD) je základní provozní režim vrstvy řízení rádiového spoje (RLC) v bezdrátových komunikačních systémech 3GPP, specifikovaný napříč standardy UMTS (25.322), LTE (36.322) a 5G NR (38.322). AMD funguje jako stavový protokol, který poskytuje spolehlivé služby přenosu dat mezi uživatelským zařízením (UE) a rádiovou přístupovou sítí (RAN), konkrétně mezi entitami RLC ve vysílači a přijímači. Na rozdíl od nepotvrzovaného režimu (UM), který nabízí doručování metodou "best-effort", AMD implementuje mechanismy automatického opakování ([ARQ](/mobilnisite/slovnik/arq/)), aby garantovalo bezchybné doručování datových jednotek protokolu (PDU) ve správném pořadí.

Architektura protokolu AMD zahrnuje několik klíčových komponent: vysílací a přijímací vyrovnávací paměti pro ukládání servisních datových jednotek (SDU) a datových jednotek protokolu (PDU) RLC, funkci segmentace a konkatenace, která přizpůsobuje SDU dostupným velikostem přenosových bloků, číslování sekvencí pro všechny AMD PDU a postupy ARQ pro správu retransmisí. Každá AMD PDU obsahuje v hlavičce pořadové číslo, což přijímači umožňuje detekovat chybějící PDU, seřadit přijaté PDU a eliminovat duplicity. Vysílač udržuje vysílací okno a retransmisní vyrovnávací paměť, zatímco přijímač udržuje přijímací okno a vyrovnávací paměť pro opětovné řazení, aby zajistil správné pořadí.

Provoz AMD zahrnuje několik koordinovaných procesů: segmentaci/konkatenaci SDU z vyšších vrstev do RLC PDU, přiřazení pořadových čísel, vysílání s řízením časovačů, hlášení stavu od přijímače k vysílači a selektivní retransmise chybějících PDU. Přijímač odesílá STATUS PDU obsahující potvrzení ([ACK](/mobilnisite/slovnik/ack/)) pro úspěšně přijaté PDU a negativní potvrzení ([NACK](/mobilnisite/slovnik/nack/)) pro chybějící PDU. Tato hlášení stavu mohou být vyžádána vysílačem nebo periodicky odesílána přijímačem. Vysílač využívá tuto zpětnou vazbu k retransmisi nepotvrzených PDU a zároveň udržuje řízení toku pomocí mechanismů založených na oknech.

Ve stohu protokolů se AMD nachází mezi vrstvou konvergenčního protokolu paketových dat (PDCP) výše a vrstvou řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) níže. Slouží pro kritické signalizační nosiče (SRB1, SRB2) a datové rádiové nosiče ([DRB](/mobilnisite/slovnik/drb/)) vyžadující spolehlivé doručení, zejména pro provoz TCP/IP a signalizaci řídicí roviny. Konfigurovatelné parametry AMD zahrnují maximální počet pokusů o retransmisi, hodnoty časovačů pro hlášení stavu a velikosti oken, což umožňuje operátorům sítí vyvažovat spolehlivost a latenci podle požadavků služby. Robustnost protokolu jej činí nezbytným pro udržení stability spojení během událostí mobility a v náročných rádiových podmínkách.

## K čemu slouží

AMD bylo vytvořeno, aby řešilo základní výzvu spolehlivého přenosu dat přes náchylné k chybám bezdrátové kanály v celulárních sítích 3GPP. Před standardizovanými mechanismy [ARQ](/mobilnisite/slovnik/arq/) na vrstvě RLC se bezdrátové systémy potýkaly s vysokou chybovostí paketů, která degradovala uživatelský zážitek a efektivitu sítě. AMD poskytuje standardizovaný přístup k obnově po chybě, který funguje nezávisle na protokolech vyšších vrstev, jako je TCP, a nabízí rychlejší obnovu z přenosových chyb díky své bližší pozici k fyzické vrstvě.

Primární motivací pro vývoj AMD byla podpora různorodých služeb s různými požadavky na spolehlivost v rámci jednotného rámce. Zatímco některé aplikace snášejí ztrátu paketů (např. hlas, video streamování), jiné jako prohlížení webu, přenos souborů a signalizační protokoly vyžadují garantované doručení. AMD umožňuje síti poskytovat různé úrovně kvality služby konfigurací parametrů spolehlivosti pro každý rádiový nosič. Tato flexibilita umožňuje operátorům optimalizovat využití zdrojů při současném splnění různorodých požadavků aplikací.

AMD řeší několik konkrétních problémů: zabraňuje zablokování protokolů na vyšších vrstvách tím, že poskytuje lokální retransmise, snižuje end-to-end latenci ve srovnání se spoléháním pouze na retransmise TCP a šetří rádiové zdroje tím, že se vyhýbá zbytečným retransmisím úspěšně doručených paketů. Funkce protokolu pro detekci duplicit a doručování ve správném pořadí zajišťují integritu dat i během předávání spojení a výpadků rádiového spoje. Standardizací těchto mechanismů napříč generacemi 3GPP umožnilo AMD konzistentní správu kvality služby a zjednodušilo interoperabilitu mezi více dodavateli v celulárních sítích.

## Klíčové vlastnosti

- Automatické opakování (ARQ) se selektivní retransmisí
- Doručování servisních datových jednotek (SDU) do vyšších vrstev ve správném pořadí
- Detekce a eliminace duplicit pomocí pořadových čísel
- Segmentace a konkatenace SDU proměnné velikosti
- Konfigurovatelné parametry spolehlivosti pro každý rádiový nosič
- Hlášení stavu prostřednictvím mechanismů vyžádání a periodického odesílání

## Související pojmy

- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)

## Definující specifikace

- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [AMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/amd/)
