---
slug: "ni-lr"
url: "/mobilnisite/slovnik/ni-lr/"
type: "slovnik"
title: "NI-LR – Network Induced Location Request"
date: 2026-01-01
abbr: "NI-LR"
fullName: "Network Induced Location Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ni-lr/"
summary: "Procedura, při níž síť (jádrová síť nebo důvěryhodný externí klient) iniciuje požadavek na lokalizaci cílového uživatelského zařízení (UE) bez explicitního požadavku od samotného UE. Používá se pro tí"
---

NI-LR je procedura požadavku na polohu iniciovaná sítí, při níž jádrová síť nebo důvěryhodný klient nařídí cílovému UE nebo rádiové síti poskytnout polohovací měření bez explicitního požadavku od UE.

## Popis

Network Induced Location Request (NI-LR) je procedura řízená jádrovou sítí v rámci architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP. Umožňuje autorizované entitě, známé jako LCS klient, požadovat zeměpisnou polohu cílového UE. Klíčovou charakteristikou NI-LR je, že požadavek na polohu je spuštěn sítí nebo externím aplikačním serverem, nikoli UE (což by byl Mobile Originated Location Request, [MO-LR](/mobilnisite/slovnik/mo-lr/)). Požadující LCS klient může sídlit v doméně operátora sítě (např. pro tísňové služby, zákonné odposlechy) nebo může být externím, důvěryhodným poskytovatelem služeb třetí strany (např. pro logistiku nebo sledování majetku). Požadavek je předán do Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), které slouží jako brána a autorizátor ochrany soukromí pro všechny požadavky na polohu.

Po přijetí ověřeného NI-LR směruje GMLC požadavek na příslušný obslužný uzel v jádrové síti – Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) pro přístup s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) pro přístup s přepojováním paketů (PS) v 2G/3G, nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro přístup v 4G/5G. Tento obslužný uzel pak iniciuje polohovací proceduru s cílovým UE a rádiovou přístupovou sítí (RAN). Konkrétní metoda určování polohy (např. Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/), UTDOA, A-GNSS) je určena sítí na základě požadované kvality služby (QoS), jako je přesnost a doba odezvy. RAN a/nebo UE provedou potřebná měření (např. časová měření pro OTDOA, signály satelitů pro A-GNSS) a nahlásí je vyhrazenému síťovému uzlu, Enhanced Serving Mobile Location Centre (E-SMLC) v LTE nebo Location Management Function (LMF) v 5G. Tento uzel vypočítá konečný odhad polohy.

Vypočtený odhad polohy je pak směrován zpět v řetězci: z E-SMLC/LMF do obslužného uzlu (MME/SGSN/MSC), poté do GMLC a nakonec doručen požadujícímu LCS klientovi. V celém tomto procesu je prvořadá ochrana soukromí. Síť musí ověřit, že LCS klient je autorizován pro konkrétní typ požadavku a že nastavení ochrany soukromí cílového účastníka, uložená v Home Subscriber Server (HSS) nebo Home Location Register (HLR), takové zveřejnění polohy iniciované sítí povolují. Procedura NI-LR je tedy komplexní orchestrací autorizace, signalizace, rádiového měření a výpočtu napříč více síťovými entitami.

## K čemu slouží

NI-LR byl vyvinut pro splnění kritických regulatorních, bezpečnostních a komerčních potřeb, které vyžadují, aby síť mohla lokalizovat účastníka bez jeho aktivní účasti. Nejvýznamnějším hnacím motorem byly regulatorní požadavky na určení polohy tísňového volajícího. Když uživatel uskuteční tísňové volání (např. 112, 911), síť musí automaticky určit polohu volajícího, aby mohla vyslat pomoc, i když volající není schopen ji poskytnout nebo si není vědom své polohy. NI-LR poskytuje standardizovaný mechanismus pro tuto automatickou lokalizaci iniciovanou sítí.

Kromě tísňových případů řeší NI-LR požadavky na zákonné odposlechy a polohově závislé služby. Orgány činné v trestním řízení, s příslušným právním povolením, vyžadují možnost lokalizovat účastníka pro bezpečnostní účely. Komerčně umožňuje širokou škálu přidaných služeb. Například logistická společnost může sledovat svůj vozový park, operátor sítě může zavést polohově závislé účtování (např. různé sazby doma vs. v zahraničí) nebo poskytovatel služeb může zasílat cílené reklamy na základě oblasti uživatele. Před standardizovanými LCS by takové schopnosti vyžadovaly proprietární, neinteroperabilní řešení. NI-LR jako součást širšího rámce 3GPP LCS vytvořil jednotnou, bezpečnou a ochranu soukromí respektující metodu pro určování polohy iniciované sítí, což umožnilo globální interoperabilitu pro bezpečnostní a komerční aplikace.

## Klíčové vlastnosti

- Umožňuje síti nebo externí aplikaci požadovat polohu UE bez iniciování ze strany UE
- Klíčová pro tísňové služby (E911, eCall) pro automatické určení polohy volajícího
- Podporuje zákonné odposlechy a bezpečnostní požadavky vládních orgánů
- Využívá různé metody určování polohy (Cell-ID, OTDOA, A-GNSS) na základě požadované QoS
- Zahrnuje uzly jádrové sítě GMLC, MME/SGSN/MSC a polohovací uzel (E-SMLC/LMF)
- Zahrnuje kontrolu ochrany soukromí účastníka a autorizaci LCS klienta

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [MO-LR – Mobile Originated Location Request](/mobilnisite/slovnik/mo-lr/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [NI-LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ni-lr/)
