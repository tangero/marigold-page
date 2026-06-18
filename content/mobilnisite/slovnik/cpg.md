---
slug: "cpg"
url: "/mobilnisite/slovnik/cpg/"
type: "slovnik"
title: "CPG – Call Progress message"
date: 2025-01-01
abbr: "CPG"
fullName: "Call Progress message"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpg/"
summary: "Signalizační zpráva používaná v sítích 3GPP pro sdělení stavu procedury sestavení nebo modifikace hovoru mezi síťovými entitami. Poskytuje standardizované informace o událostech průběhu hovoru, jako j"
---

CPG je signalizační zpráva používaná v sítích 3GPP pro sdělení stavu sestavování nebo modifikace hovoru, která poskytuje standardizované informace o událostech, jako je vyzvánění, spojení nebo rozpojení.

## Popis

Zpráva o průběhu hovoru (Call Progress – CPG) je základní součástí signalizačního rámce pro řízení hovorů v sítích 3GPP, definovaná primárně pro doménu IP multimediální podsystému (IMS) a doménu s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Funguje jako součást signalizačních protokolů Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) nebo [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) v závislosti na síťové doméně. Zprávu generuje síť (např. funkce [S-CSCF](/mobilnisite/slovnik/s-cscf/) v IMS nebo [MSC](/mobilnisite/slovnik/msc/) v CS), aby informovala terminál volající strany nebo síťovou entitu o průběžných událostech během sestavování nebo ukončování hovoru. To zahrnuje indikace, že se volaná strana vyzvání (zvonění), že se hovor spojuje nebo že se uvolňují prostředky související s hovorem.

Z architektonického hlediska se zpráva CPG přenáší v rámci signalizační cesty zavedené mezi uživatelským zařízením (UE) a sítí nebo mezi síťovými uzly, jako je [MGCF](/mobilnisite/slovnik/mgcf/) a MSC. V IMS je přenášena jako zpráva SIP (např. SIP [INFO](/mobilnisite/slovnik/info/) nebo re-INVITE se specifickými hlavičkami) a může obsahovat aktualizace Session Description Protocol (SDP) pro vyjednávání médií. V sítích CS je mapována na signalizační zprávy ISUP, jako je Call Progress (CPG) nebo Address Complete (ACM), což zajišťuje interoperabilitu mezi staršími a IP systémy. Klíčové parametry uvnitř zprávy CPG zahrnují příčinný kód (udávající důvod události), indikátory průběhu (určující typ průběhu, např. informace v pásmu nebo zahlcení sítě) a časová razítka pro synchronizaci.

Role zprávy CPG je klíčová pro udržení konzistence stavu hovoru a poskytování zpětné vazby uživatelům v reálném čase. Například při uskutečnění hovoru síť odešle zprávu CPG s indikací 'vyzvánění' do UE volajícího, což spustí místní zpětný tón vyzvánění. Tím se zabrání tichu na straně volajícího a zlepší se uživatelský zážitek. Dále zpráva podporuje pokročilé služby, jako je přesměrování hovorů, kde CPG může indikovat události přesměrování, nebo multimediální relace, kde sděluje modifikace mediálních proudů. Její standardizovaný formát napříč vydáními 3GPP zajišťuje bezproblémový provoz více-dodavatelských sítí a roamingových scénářů, což snižuje selhání hovorů a zvyšuje spolehlivost služeb.

## K čemu slouží

Zpráva CPG byla zavedena, aby vyřešila potřebu standardizovaného, spolehlivého mechanismu pro komunikaci událostí průběhu hovoru v telekomunikačních sítích, zejména s vývojem sítí od čistého přepojování okruhů k hybridním a IP architekturám, jako je IMS. Před jejím formalizováním v 3GPP bylo signalizování průběhu hovoru často řešeno proprietárními nebo doménově specifickými metodami, což vedlo k problémům s interoperabilitou mezi různými dodavateli síťového vybavení a mezi staršími CS a nově vznikajícími IP sítěmi. Tato roztříštěnost mohla vést k nekonzistentnímu uživatelskému zážitku, jako je chybějící zpětný tón vyzvánění nebo zpožděné spojení hovoru, zejména v prostředích s více operátory.

Historicky se v raných vydáních GSM a UMTS řízení hovorů silně opíralo o CS signalizační protokoly jako ISUP, které obsahovaly základní indikátory průběhu, ale postrádaly flexibilitu pro multimediální služby. Se zavedením IMS ve vydání 5 vznikla potřeba sjednotit řízení hovorů napříč CS a IP doménami, což vyžadovalo zprávu jako CPG pro propojení těchto technologií. Zpráva CPG to řeší tím, že poskytuje společnou abstrakci pro události hovoru, což umožňuje hladkou vzájemnou spolupráci mezi SIP hovory v IMS a tradiční telefonii. Také řeší omezení dřívějších přístupů tím, že podporuje bohatší informační prvky, jako jsou příčinné kódy pro podrobné hlášení chyb a deskriptory průběhu pro oznámení v pásmu/mimo pásmo, které jsou nezbytné pro odstraňování problémů a diferenciaci služeb.

Dále zpráva CPG umožňuje rozšířené služby, jako je videohovor, kde sestavení hovoru zahrnuje více mediálních proudů, a regulační funkce, jako je zákonné odposlouchávání, kde je třeba zaznamenávat události průběhu. Jejím standardizováním napříč vydáními 3GPP zajistilo zpětnou kompatibilitu a budoucí škálovatelnost, což umožnilo sítím vyvíjet se při zachování konzistentní sémantiky řízení hovorů. To bylo klíčové pro globální přijetí služeb VoLTE, VoNR a dalších služeb komunikace v reálném čase, kde je předvídatelné chování hovoru klíčovým metrikou kvality.

## Klíčové vlastnosti

- Sděluje standardizované události průběhu hovoru, jako je vyzvánění, spojení a rozpojení
- Podporuje signalizaci založenou na SIP v IMS i signalizaci založenou na ISUP v CS
- Obsahuje příčinné kódy a indikátory průběhu pro podrobné hlášení událostí
- Umožňuje vzájemnou spolupráci mezi doménami s přepojováním okruhů a IP multimédií
- Spouští mechanismy zpětné vazby pro uživatele, jako jsou zpětné tóny vyzvánění v UE
- Umožňuje pokročilé služby, jako je přesměrování hovorů a vyjednávání médií

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.505** (Rel-8) — Protocol Description of the Conference Service
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [CPG na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpg/)
