---
slug: "ccr"
url: "/mobilnisite/slovnik/ccr/"
type: "slovnik"
title: "CCR – Credit-Control-Request"
date: 2025-01-01
abbr: "CCR"
fullName: "Credit-Control-Request"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ccr/"
summary: "CCR je zpráva založená na protokolu Diameter používaná v rámci Policy and Charging Control (PCC) pro žádost o kreditní autorizaci pro datovou relaci uživatele. Jedná se o klíčovou součást pro účtování"
---

CCR je zpráva založená na protokolu Diameter používaná v rámci 3GPP Policy and Charging Control pro žádost o kreditní autorizaci pro datovou relaci uživatele, což umožňuje reálný čas účtování a vymáhání politik.

## Popis

Credit-Control-Request (CCR) je základní příkaz protokolu Diameter v architektuře 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), konkrétně definovaný v Diameter Credit-Control Application ([DCCA](/mobilnisite/slovnik/dcca/)) podle [RFC](/mobilnisite/slovnik/rfc/) 4006 a přizpůsobený ve specifikacích 3GPP. Jde o request zprávu odesílanou funkcí Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) nebo Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)) k funkci Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) za účelem zahájení, aktualizace nebo ukončení kreditní řídicí relace. Zpráva CCR nese základní informace, jako je identita účastníka (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), informace o služebním datovém toku, požadované parametry QoS a hlášení o využití, což PCRF umožňuje činit informovaná rozhodnutí o pravidlech politik a účtování.

V provozu, když uživatel zahájí datovou relaci, PCEF (typicky umístěná v PDN Gateway nebo GGSN) odešle úvodní CCR (CCR-Initial) PCRF s žádostí o pravidla pro politiky a účtování. PCRF, případně komunikující s Online Charging System (OCS) přes referenční bod Sy, vyhodnotí žádost vůči profilům účastníka a síťovým politikám. Následně odpoví Credit-Control-Answer (CCA) obsahující autorizovaná pravidla pro politiky a účtování, která mohou zahrnovat přidělené QoS, rozhodnutí o propouštění (gating) a informace o účtování, jako jsou přidělené kvóty. Během relace PCEF odesílá aktualizační CCR (CCR-Update) k nahlášení využití (např. objemu nebo spotřebovaného času) a k žádosti o další autorizaci a ukončovací CCR (CCR-Terminate) při skončení relace, aby dokončila proces účtování.

Struktura zprávy CCR zahrnuje atributy typu AVP (Attribute-Value Pairs), které přenášejí podrobné parametry relace. Mezi klíčové AVP patří CC-Request-Type (určující INITIAL_REQUEST, UPDATE_REQUEST nebo TERMINATION_REQUEST), CC-Request-Number pro sekvencování, Subscription-Id pro identifikaci uživatele, QoS-Information pro charakteristiky přenosového spoje a více instancí Used-Service-Unit AVP pro hlášení objemového, časového nebo služebně specifického využití. Tato detailní data umožňují modely účtování v reálném čase, které jsou citlivé na služby, jako je účtování podle objemu, času nebo události, a podporují pokročilé vymáhání politik, jako je tvarování provozu (traffic shaping) a zvýšení priority služeb.

Role CCR přesahuje základní účtování; je nedílnou součástí dynamického řízení politik. Hlášením detekce služebního datového toku a využití v reálném čase umožňuje CCR, aby PCRF přizpůsoboval politiky na základě síťových podmínek, úrovně účastníka nebo typu aplikace. To usnadňuje funkce jako sponzorovaná data, zero-rating a poskytování šířky pásma na požádání. V nasazeních s offline účtováním (Offline Charging) může být CCR použito k hlášení využití do Offline Charging System (OFCS) přes referenční bod Ga, i když jeho primární návrh je pro online interakce. Zpráva je přenášena přes protokol Diameter na referenčním bodu Gx (mezi PCEF a PCRF) nebo Sd (mezi TDF a PCRF), což zajišťuje spolehlivou, bezpečnou a standardizovanou komunikaci pro operace PCC.

## K čemu slouží

CCR bylo zavedeno, aby řešilo omezení statických, dávkově orientovaných systémů účtování v dřívějších mobilních sítích (např. 2G/3G), které nedokázaly podporovat řízení služeb v reálném čase a flexibilní modely účtování vyžadované pro rozvíjející se datové služby. Předchozí přístupy, jako ty založené na CAMEL pro předplacené služby, se často zaměřovaly na přepojování okruhů a postrádaly integraci s dynamickým vymáháním politik. Vzestup služeb s přepojováním paketů a rozmanitých datových aplikací vyžadoval mechanismus pro kreditní autorizaci v reálném čase a rozhodování o politikách, aby se zabránilo únikům příjmů, umožnily předplacené datové balíčky a operátoři mohli nabízet diferencované služby.

Vytvoření CCR v rámci PCC frameworku v 3GPP Release 8 bylo motivováno potřebou standardizovaného online rozhraní pro účtování, které by mohlo bezproblémově interagovat s řízením politik. Řeší problém řízení kvót účastníků v reálném čase, zajišťuje, aby uživatelé nepřekročili své kreditní limity, a zároveň umožňuje nepřetržitý provoz služeb. Oddělením účtování od vymáhání politik umožňuje CCR operátorům implementovat složité obchodní modely, jako jsou vrstvené ceny, účtování specifické pro aplikace a propagační nabídky, bez výpadků sítě. Také podporuje konvergenci předplacených a postpaid systémů poskytováním jednotného rozhraní pro online řízení kreditů.

Historicky, bez mechanismů typu CCR, se operátoři potýkali se spory o účtování po skončení relace a nedokázali dynamicky upravovat služby na základě kreditního stavu. Zavedení CCR jako součásti architektury PCC založené na Diameter poskytlo škálovatelné a interoperabilní řešení, které je základem moderních sítí LTE a 5G. Řeší kritickou potřebu okamžité zpětné vazby o využívání zdrojů, což usnadňuje nejen účtování, ale také optimalizaci síťových zdrojů a zlepšený uživatelský zážitek díky úpravám politik v reálném čase.

## Klíčové vlastnosti

- Příkaz založený na Diameter pro kreditní autorizaci v reálném čase
- Podporuje tři typy requestů: INITIAL, UPDATE a TERMINATION pro správu životního cyklu relace
- Nese detailní AVP pro identitu účastníka, parametry QoS a hlášení o využití
- Umožňuje integraci mezi PCEF/TDF a PCRF přes rozhraní Gx/Sd
- Umožňuje dynamické vymáhání politik a řízení online účtování
- Podporuje více modelů účtování: objemové, časové a založené na událostech

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [CCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccr/)
