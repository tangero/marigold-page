---
slug: "ptt"
url: "/mobilnisite/slovnik/ptt/"
type: "slovnik"
title: "PTT – Push-to-Talk"
date: 2026-01-01
abbr: "PTT"
fullName: "Push-to-Talk"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ptt/"
summary: "Poloduplexní hlasová komunikační služba, kde uživatel stiskne tlačítko, aby promluvil ke skupině, a uvolní ho, aby poslouchal. 3GPP ji standardizovalo jako Push-to-talk over Cellular (PoC), což umožňu"
---

PTT je poloduplexní hlasová služba standardizovaná 3GPP jako Push-to-talk over Cellular (PoC), která umožňuje okamžitou, vysílačce podobnou skupinovou komunikaci přes mobilní paketové sítě.

## Popis

Push-to-Talk (PTT) over Cellular (PoC) je standardizovaná služba 3GPP, která poskytuje okamžitou poloduplexní hlasovou skupinovou komunikaci přes IP mobilní sítě. Na rozdíl od plně duplexního telefonního hovoru využívá PTT "mluvící" tlačítko k ovládání práva mluvit (tzv. "právo slova"). Uživatel stiskne a drží tlačítko, aby získal právo slova, jeho hlas je paketizován a přenášen přes jádro IP Multimedia Subsystem (IMS) ke všem členům předdefinované nebo ad-hoc skupiny, a tlačítko uvolní, aby poslouchal. Architektura služby je typu klient-server a zahrnuje PoC klientskou aplikaci na uživatelském zařízení (UE), PoC server v síti a využívá IMS pro řízení relace (pomocí [SIP](/mobilnisite/slovnik/sip/)) a přenos médií (pomocí [RTP](/mobilnisite/slovnik/rtp/) přes [UDP](/mobilnisite/slovnik/udp/)).

Klíčovou síťovou komponentou je PoC Server, který vykonává několik kritických funkcí: spravuje definice skupin a členství, zpracovává zahájení a ukončení relace, řídí právo slova (rozhoduje mezi požadavky více uživatelů snažících se mluvit současně) a distribuuje mediální streamy všem účastníkům. Protokol pro řízení práva slova je klíčovým prvkem, který zajišťuje, že v jeden okamžik vysílá audio pouze jeden účastník, aby nedocházelo ke kolizím. Média jsou typicky přenášena jako Voice over IP (VoIP) pakety. Služba je integrována se základními funkcemi IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro směrování SIP a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro uživatelské profily a autorizaci služby.

Provoz začíná registrací PoC klienta v jádru IMS. Pro zahájení skupinové hovorové relace klient odešle SIP INVITE na PoC server s identifikací cílové skupiny. Server upozorní ostatní členy skupiny (pomocí SIP) a vytvoří jednosměrnou mediální cestu od držitele práva slova ke všem posluchačům. Když chce uživatel mluvit, jeho klient odešle zprávu s žádostí o právo slova. PoC server právo slova přidělí na základě nastavené politiky (např. kdo dřív přijde, ten dřív mele, nebo podle priority) a uživatelův audio stream je pak směrován ke skupině. Tento model poskytuje okamžitou komunikaci s minimálním zpožděním při sestavování, napodobující zkušenost s tradičními obousměrnými radiostanicemi, ale s celoplošným pokrytím a kapacitou mobilní sítě.

## K čemu slouží

PTT bylo standardizováno 3GPP za účelem přenesení okamžitého, jeden-k-více komunikačního paradigmatu tradičních Private Mobile Radio (PMR) a dispečerských systémů do komerčních mobilních sítí. Před PoC se profesionální uživatelé (např. v oblasti veřejné bezpečnosti, stavebnictví, logistiky) spoléhali na samostatné, vyhrazené sítě [LMR](/mobilnisite/slovnik/lmr/), zatímco mobilní sítě nabízely pouze plně duplexní hovory jeden-na-jednoho nebo nestandardizovaná proprietární PTT řešení bez interoperability. Motivací bylo využít všudypřítomné pokrytí a vysokou kapacitu vyvíjejících se paketových sítí 2.5G/3G ([GPRS](/mobilnisite/slovnik/gprs/), UMTS) k nabídnutí přesvědčivé, standardizované skupinové komunikační služby.

Vytvoření 3GPP PTT (PoC) vyřešilo několik problémů: Poskytlo interoperabilitu mezi zařízeními a sítěmi od různých výrobců a operátorů, což proprietární řešení nedokázala. Nabídlo nákladově efektivní alternativu k budování a údržbě samostatných sítí LMR využitím stávající mobilní infrastruktury. Dále řešilo omezení latence u časných skupinových hovorů v přepojovaných okruzích, protože paketový charakter PoC umožnil rychlejší sestavení hovoru a efektivnější využití síťových zdrojů pro přerušovaný hlasový provoz.

Jeho vývoj byl hnacím komerční poptávkou po okamžité komunikaci v obchodních vertikálách a snahou operátorů zvýšit [ARPU](/mobilnisite/slovnik/arpu/) novými službami s přidanou hodnotou. Díky integraci s IMS bylo PoC navrženo jako perspektivní, plně IP služba, která se mohla vyvíjet spolu s jádrem sítě. Řešilo to omezení předchozích přístupů poskytnutím standardizované, škálovatelné a sítí řízené služby, která mohla podporovat velké skupiny, informace o přítomnosti a bezproblémovou mobilitu, čímž překlenulo propast mezi tradičními dispečerskými radiostanicemi a moderní mobilní telefonií.

## Klíčové vlastnosti

- Poloduplexní, jeden-k-více hlasová skupinová komunikace
- Mechanismus řízení práva slova pro arbitráž hovorového práva
- Integrace s jádrem IMS pro řízení relace (SIP) a média (RTP)
- Podpora předem sestavených a ad-hoc okamžitých skupinových relací
- Stav přítomnosti a dostupnosti členů skupiny
- Využívá mobilní paketová data pro celoplošné pokrytí a mobilitu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TS 22.468** (Rel-19) — Group Communication System Enabler Requirements
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.779** (Rel-13) — MCPTT over LTE Stage 2 Study
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 36.868** (Rel-12) — Study on Group Communication for E-UTRA

---

📖 **Anglický originál a plná specifikace:** [PTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptt/)
