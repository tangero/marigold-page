---
slug: "mt-lr"
url: "/mobilnisite/slovnik/mt-lr/"
type: "slovnik"
title: "MT-LR – Mobile Terminated Location Request"
date: 2026-01-01
abbr: "MT-LR"
fullName: "Mobile Terminated Location Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mt-lr/"
summary: "Mobile Terminated Location Request (MT-LR) je síťový postup, při kterém externí klient lokalizačních služeb (LCS) vyžádá geografickou polohu mobilního účastníka. Umožňuje aplikacím třetích stran, jako"
---

MT-LR je síťový postup, při kterém externí klient lokalizačních služeb (Location Services) vyžádá geografickou polohu mobilního účastníka, což umožňuje aplikacím třetích stran získat polohu uživatele.

## Popis

Mobile Terminated Location Request (MT-LR) je standardizovaný postup v rámci architektury lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP. Umožňuje externímu klientovi LCS (např. tísňovému call centru, logistické aplikaci nebo subjektu pro zákonné odposlechy) vyžádat a obdržet polohu cílového uživatelského zařízení (UE). Architektura zahrnuje několik klíčových entit: klienta LCS, Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE, Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v UMTS nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC a funkce pro určení polohy v rámci rádiové přístupové sítě (RAN) a jádra sítě (např. Enhanced Serving Mobile Location Center - [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, Location Management Function - [LMF](/mobilnisite/slovnik/lmf/) v 5G). Postup je zahájen odesláním žádosti o polohu od klienta LCS do GMLC. GMLC funguje jako brána, provádí autorizaci a kontrolu ochrany soukromí na základě identity klienta a profilu ochrany soukromí účastníka uloženého v HSS. Pokud je žádost autorizována, GMLC dotazuje HSS, aby našel obsluhující uzel (MME/SGSN/AMF) pro cílové UE. Žádost je poté předána tomuto obsluhujícímu uzlu. Obsluhující uzel ve spolupráci s RAN a příslušným lokalizačním serverem (E-SMLC/LMF) spustí proces určení polohy. Ten může zahrnovat různé metody určování polohy, jako je Observed Time Difference of Arrival (OTDOA), Uplink Time Difference of Arrival (UTDOA), Assisted GNSS (A-GNSS) nebo Enhanced Cell ID (E-CID). Vypočtený odhad polohy je poté směrován zpět přes řetězec (obsluhující uzel -> GMLC) k žádajícímu klientovi LCS. Celý proces se řídí přísnými předpisy na ochranu soukromí a vyžaduje souhlas účastníka (buď předem nastavený, nebo v reálném čase), pokud není přepsán zákonnou autoritou (např. pro tísňové služby). Postup MT-LR je definován napříč více protokolovými vrstvami a generacemi sítí, což zajišťuje konzistentní poskytování služeb od GSM po 5G.

## K čemu slouží

MT-LR existuje jako standardizovaný, bezpečný a z hlediska ochrany soukromí vyhovující mechanismus pro autorizované externí subjekty k lokalizaci mobilních účastníků. Řeší problém umožnění hodnotných služeb založených na poloze (např. navigace, vyhledávač přátel, sledování majetku) a kritických služeb (jako je rozšířené tísňové volání Enhanced 911/E112) bez svévolného zpřístupňování polohy účastníka. Před jeho standardizací proprietární řešení nebo omezené síťové možnosti ztěžovaly rozšíření a interoperabilitu lokalizačních služeb. Vytvoření MT-LR bylo motivováno regulatorními požadavky (např. lokalizace tísňového volajícího), komerčními příležitostmi pro služby založené na poloze (LBS) a provozními potřebami (např. správa vozového parku). Odstranil omezení dřívějších nestandardizovaných metod definováním jasných architektonických rolí, rozhraní (např. Le, Lg, SLg, NLs) a postupů kontroly ochrany soukromí. To umožňuje síťovým operátorům nabízet polohu jako řízenou službu poskytovatelům třetích stran při současné ochraně soukromí účastníků. Postup zajišťuje, že získání polohy lze provést bez ohledu na stav UE (nečinné nebo připojené) a napříč různými rádiovými přístupovými technologiemi.

## Klíčové vlastnosti

- Podporuje žádosti o polohu iniciované externím klientem přes referenční bod Le
- Zahrnuje GMLC pro autorizaci, směrování a zprostředkování ochrany soukromí
- Integruje více metod určování polohy (A-GNSS, OTDOA, E-CID atd.)
- Vynucuje ochranu soukromí účastníka prostřednictvím autorizace klienta LCS a souhlasu účastníka
- Funguje napříč všemi generacemi 3GPP (GSM, UMTS, LTE, 5G)
- Definován pro tísňové služby, služby s přidanou hodnotou a zákonné odposlechy

## Související pojmy

- [MO-LR – Mobile Originated Location Request](/mobilnisite/slovnik/mo-lr/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [MT-LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mt-lr/)
