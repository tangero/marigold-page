---
slug: "lir"
url: "/mobilnisite/slovnik/lir/"
type: "slovnik"
title: "LIR – Location Information Request"
date: 2025-01-01
abbr: "LIR"
fullName: "Location Information Request"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lir/"
summary: "Location Information Request (LIR) je procedura nebo zpráva používaná entitou (jako aplikační server nebo síťový uzel) k dotazování sítě na geografickou nebo občanskou polohu uživatelského zařízení (U"
---

LIR je žádost (request message) používaná aplikací nebo síťovým uzlem k dotazování sítě na geografickou nebo občanskou (civic) polohu mobilního zařízení, která spouští různé metody určování polohy.

## Popis

Location Information Request (LIR) je klíčový procedurální prvek v architekturách 3GPP pro získání polohy mobilního zařízení. Není to jedna konkrétní protokolová zpráva, ale konceptuální servisní žádost, která je realizována prostřednictvím specifických protokolů a rozhraní, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) přes rozhraní SLs, protokol [OMA](/mobilnisite/slovnik/oma/) SUPL, nebo přes rozhraní core sítě jako Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) používající rozhraní Le nebo SLg. LIR je iniciována klientem služby polohy ([LCS](/mobilnisite/slovnik/lcs/) Client), kterým může být externí aplikace (např. mapová služba), interní síťová služba (např. pro zákonný odposlech) nebo samotné UE. Žádost obsahuje parametry jako identifikátor cílového UE ([MSISDN](/mobilnisite/slovnik/msisdn/), [IMSI](/mobilnisite/slovnik/imsi/)), požadovanou kvalitu služby (QoS) pro polohu (např. přesnost, dobu odezvy) a typ požadované polohové informace (např. geografické souřadnice, občanská adresa).

Po přijetí LIR síťový polohový systém aktivuje příslušné metody určování polohy. Pro síťové určování polohy může síť použít měření z základnových stanic (např. Observed Time Difference of Arrival - [OTDOA](/mobilnisite/slovnik/otdoa/) v LTE, Downlink Time Difference of Arrival - [DL-TDOA](/mobilnisite/slovnik/dl-tdoa/) v 5G). Pro určování polohy založené na UE síť poskytne uživatelskému zařízení asistenční data (např. efemeridy satelitů pro A-GNSS), které si pak samo vypočte svou polohu a může ji nahlásit zpět. Hybridní metody kombinují oba přístupy. Řízení a koordinaci tohoto procesu zajišťují síťové entity jako Evolved Serving Mobile Location Centre (E-SMLC) v LTE nebo Location Management Function (LMF) v 5G. Tyto entity vybírají metodu určování polohy na základě QoS z LIR, možností UE a dostupných síťových měření.

Výsledkem zpracování LIR je odpověď s polohovou informací (Location Information Response), která doručí odhadovaná polohová data žádajícímu klientovi. Celá procedura zahrnuje více síťových domén: core síť pro autorizaci klienta a směrování žádosti, rádiovou přístupovou síť pro sběr měření a potenciálně i UE. Soukromí je kritickým aspektem; síť musí ověřit, že LCS Client je oprávněn žádat o polohu konkrétního cílového UE na základě nastavení soukromí účastníka a regulatorních pravidel. Mechanismus LIR je tedy spouštěcím podnětem pro složitou, standardizovanou sekvenci, která převádí rádiové signály nebo satelitní data na použitelnou geografickou polohu pro služby.

## K čemu slouží

Koncept Location Information Request vznikl za účelem standardizace způsobu, jakým aplikace a služby mohou programově získat polohu mobilního účastníka. Před jeho standardizací byly polohové služby proprietární a fragmentované, což bránilo rozvoji rozšířených aplikací založených na poloze. Hlavní problém, který řeší, je poskytnutí jednotného, bezpečného a spolehlivého rozhraní pro oprávněné entity k žádosti o polohu UE, což je nezbytné pro komerční služby (hledání přátel, reklamu založenou na poloze), nouzové služby (E-911/112) a optimalizaci sítě.

Historicky byla tato potřeba hnána regulatorními požadavky na lokalizaci nouzových volajících a komerčním potenciálem služeb založených na poloze. Rámec LIR, vyvíjející se od 3GPP Release 99, vytvořil jasnou architektonickou separaci mezi entitou žádající o polohu (LCS Client) a polohovými schopnostmi sítě. Tím se vyřešila omezení ad-hoc řešení definováním standardizovaných protokolů (např. LPP, SUPL), rozhraní (např. Le, SLg) a mechanismů kontroly soukromí. Umožnil ekosystém, kde mohli operátoři v kontrolovaném režimu zpřístupnit polohové schopnosti poskytovatelům aplikací třetích stran, což podpořilo inovace v mobilních službách při současném zajištění soukromí účastníků a bezpečnosti sítě.

## Klíčové vlastnosti

- Standardizovaný mechanismus pro spouštění procedur určování polohy UE
- Podpora více metod určování polohy (A-GNSS, OTDOA, E-CID atd.)
- Zahrnuje parametry kvality služby (QoS) jako přesnost a doba odezvy
- Zahrnuje ověření soukromí a autorizační kontroly
- Implementován napříč více rozhraními (LTE: SLs, Le; 5G: NLs, Nlmf)
- Poskytuje polohu ve standardizovaných formátech (např. 3GPP nebo civic shapes)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.572** (Rel-19) — Nlmf Service Based Interface Stage 3
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lir/)
