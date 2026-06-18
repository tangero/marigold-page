---
slug: "psap"
url: "/mobilnisite/slovnik/psap/"
type: "slovnik"
title: "PSAP – Public Safety Answering Point"
date: 2026-01-01
abbr: "PSAP"
fullName: "Public Safety Answering Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/psap/"
summary: "Kritické kontaktní centrum záchranných služeb, které přijímá tísňová volání (např. na 112, 911) a vysílá odpovídající zdroje záchranných složek. Standardy 3GPP definují architektury a protokoly pro sm"
---

PSAP je kritické kontaktní centrum záchranných služeb, které přijímá tísňová volání z mobilních sítí a vysílá záchranné složky, přičemž standardy 3GPP definují jeho směrovací architektury a protokoly.

## Popis

Public Safety Answering Point (PSAP) je fyzické nebo logické kontaktní centrum odpovědné za přijímání hovorů na národní nebo regionální tísňové telefonní číslo (např. 112 v Evropě, 911 v Severní Americe). V kontextu standardů 3GPP je důraz kladen na definici síťových architektur, rozhraní a procedur pro úspěšné směrování tísňových hovorů a přidružených dat z uživatelského zařízení (UE) přes mobilní síť na příslušný PSAP. Samotný PSAP je typicky považován za uzel mimo síť 3GPP, ale jeho rozhraní a požadavky významně ovlivňují specifikace 3GPP.

Architektura pro záchranné služby zahrnuje několik klíčových síťových funkcí 3GPP. Když UE zahájí tísňový hovor, rádiová přístupová síť (RAN) a jádrová síť (CN) musí tento hovor rozpoznat jako tísňovou relaci. Centrální roli hraje Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Ty upřednostňují zřízení relace a mohou pro směrování tísňového hovoru vyvolat Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)) v IP Multimedia Subsystem (IMS). Síť musí také poskytnout informace o poloze volajícího. To je zajištěno pomocí Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) a platforem Secure User Plane Location ([SUPL](/mobilnisite/slovnik/supl/)), které získají polohu UE a doručí ji PSAP.

Princip fungování: UE indikuje tísňový požadavek během zřizování relace. Síť autentizuje UE pouze pro záchranné služby (nemusí mít platnou [SIM](/mobilnisite/slovnik/sim/) kartu) a vytvoří prioritní přenos (bearer) nebo QoS tok se specifickými atributy pro tísňový hlas. Současně jsou spuštěny procedury získávání polohy. Signalizace hovoru ([SIP](/mobilnisite/slovnik/sip/) zprávy) je směrována přes IMS jádro, kde E-CSCF dotazuje Location Retrieval Function (LRF), aby na základě polohy volajícího určila správný PSAP. E-CSCF poté směruje hovor na tento PSAP přes Interconnection Border Control Function (IBCF) nebo přímo přes IP síť (např. pomocí ESInet). PSAP přijme hovor a přidružená data o poloze, což operátorovi umožní vyslat policii, hasiče nebo zdravotnickou službu. Úlohou 3GPP je zajistit, aby tento složitý řetězec událostí fungoval spolehlivě napříč různými generacemi sítí a administrativními doménami.

## K čemu slouží

Standardizace rozhraní k PSAP byla motivována kritickým požadavkem veřejné bezpečnosti na spolehlivé připojení mobilních volajících k záchranným službám. Rané celulární systémy měly omezené možnosti pro tísňové hovory, často postrádaly automatickou identifikaci polohy, což představovalo významné riziko pro veřejnou bezpečnost. Jak se mobilní telefony staly primárním zařízením pro uskutečňování tísňových hovorů, regulační orgány po celém světě nařídily vylepšené funkce, jako je automatické doručování polohy.

Práce 3GPP na rozhraních PSAP řeší několik klíčových problémů: Definuje, jak mobilní síť identifikuje pokus o tísňové volání, a to i z neautentizovaného zařízení. Standardizuje mechanismy pro získání a formátování polohy volajícího (cell-ID, assisted-GNSS) tak, aby splňovaly regulační požadavky na přesnost. Definuje také logiku směrování pro připojení volajícího ke geograficky příslušnému PSAP, což u mobilních uživatelů není triviální. Tato práce se vyvinula od základních tísňových hovorů v okruhově komutovaných sítích 2G/3G k sofistikovaným IP záchranným službám v 4G a 5G, zahrnujícím multimediální tísňové služby (např. text a video v reálném čase). Cílem je vytvořit spolehlivý, interoperabilní a funkčně bohatý ekosystém záchranných služeb, který využívá možnosti moderních mobilních sítí k záchraně životů.

## Klíčové vlastnosti

- Koncový bod pro tísňová volání z mobilních sítí
- Přijímá informace o poloze volajícího přes standardizovaná rozhraní (např. od GMLC/LMF)
- Podporuje směrování na základě geografické polohy volajícího
- Lze k němu připojit přes starší okruhově komutované sítě nebo moderní IP-based ESInety
- Podporuje pokročilé záchranné služby, jako jsou multimediální tísňová volání
- Definován jako externí entita, se kterou musí sítě 3GPP interoperovat

## Související pojmy

- [E-CSCF – Emergency – Call Session Control Function](/mobilnisite/slovnik/e-cscf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 22.871** (Rel-11) — Non-Voice Emergency Services (NOVES)
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 23.867** (Rel-7) — IMS Emergency Services Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/psap/)
