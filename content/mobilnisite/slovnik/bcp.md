---
slug: "bcp"
url: "/mobilnisite/slovnik/bcp/"
type: "slovnik"
title: "BCP – Basic Communication Part"
date: 2025-01-01
abbr: "BCP"
fullName: "Basic Communication Part"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/bcp/"
summary: "BCP je protokolová komponenta ve službě Mission Critical Push to Talk (MCPTT) společnosti 3GPP, standardizovaná v TS 24.275. Poskytuje základní komunikační mechanismy pro zřizování, udržování a ukončo"
---

BCP je protokolová komponenta ve službě Mission Critical Push to Talk společnosti 3GPP, která poskytuje základní mechanismy pro zřizování, udržování a ukončování skupinových nebo privátních hovorů.

## Popis

Základní komunikační část (Basic Communication Part, BCP) je jádrová protokolová entita definovaná v architektuře služeb Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) společnosti 3GPP, konkrétně pro službu Mission Critical Push to Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Funguje na aplikační vrstvě a je odpovědná za správu základní signalizace a toků médií pro relace MCPTT. BCP je implementována jak v klientovi MCPTT (v uživatelském zařízení, UE), tak na serveru MCPTT (v síti). Jejím primárním účelem je řízení procedur řízení hovoru pro skupinové hovory, privátní hovory a nouzové hovory, které jsou základními komunikačními režimy pro personál veřejné bezpečnosti.

Z architektonického hlediska BCP interaguje s dalšími funkčními komponentami MCPTT, jako je aplikační server MCPTT a část řízení práva mluvit (Floor Control Part, [FCP](/mobilnisite/slovnik/fcp/)). Zatímco BCP spravuje celkové zřizování relace (např. zvaní účastníků, vyjednávání kodeků), FCP spravuje rozhodování o tom, kdo má právo mluvit (tzv. "floor") během relace. BCP využívá jako podpůrný signalizační protokol [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), jak je definováno ve 3GPP TS 24.229, a pro přenos médií [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/). Definuje specifické SIP metody, hlavičky a těla zpráv pro přenos informací specifických pro MCPTT, jako jsou identifikátory skupin, priority uživatelů a typy hovorů.

Protokol funguje tak, že zpracovává SIP požadavky INVITE pro zahájení hovorů, BYE pro ukončení hovorů a různé požadavky během relace. Pro skupinový hovor vyšle BCP v iniciujícím klientovi SIP INVITE obsahující cílové ID skupiny na server MCPTT v síti. BCP na serveru tento požadavek zpracuje, případně provede autorizační kontroly, a je odpovědná za rozeslání pozvánky všem členům skupiny nebo za správu předem zřízené skupinové relace. Zpracovává odpovědi, spravuje časovače relace a koordinuje se s funkcemi přenosové roviny médií, aby zajistila správné směrování hlasových paketů ke všem autorizovaným účastníkům.

Klíčovými součástmi specifikace BCP jsou detailní stavové automaty pro klienta a server, definice parametrů a hlavičkových polí SIP specifických pro MCPTT a procedury pro řešení abnormálních událostí, jako je přerušení (když vyšší prioritní uživatel získá právo mluvit) nebo odpojení od sítě. Její role je fundamentální; bez BCP by základní hovorová konektivita pro MCPTT neexistovala. Poskytuje standardizované "navázání spojení" (handshake), které umožňuje interoperabilitu mezi MCPTT klienty a servery různých dodavatelů, což je kritický požadavek pro sítě veřejné bezpečnosti, kde zařízení od více dodavatelů musí během mimořádných událostí bezproblémově spolupracovat.

## K čemu slouží

BCP byla vytvořena, aby vyřešila kritickou potřebu standardizovaného, interoperabilního protokolu pro hlasovou komunikaci push-to-talk v sítích LTE a 5G pro uživatele veřejné bezpečnosti a systémy s požadavkem na vysokou spolehlivost (mission-critical). Před standardizací 3GPP poskytovaly podobnou funkčnost profesionální mobilní radiové systémy (PMR), jako jsou [TETRA](/mobilnisite/slovnik/tetra/) a [P25](/mobilnisite/slovnik/p25/), které však byly založeny na úzkopásmových, okruhově spínaných technologiích s omezenými datovými schopnostmi a často proprietárními implementacemi. Motivací bylo využít vysokou přenosovou rychlost, nízkou latenci a úspory z rozsahu komerčních sítí 3GPP (LTE/5G NR) k poskytování pokročilých služeb s požadavkem na vysokou spolehlivost a přitom zajistit garantovanou spolehlivost, bezpečnost a funkčnost.

Konkrétním problémem, který BCP řeší, je absence jednotného protokolu řízení hovoru pro MCPTT. Bez standardu, jako je BCP, by každý dodavatel implementoval vlastní signalizační metody pro nastavování skupinových hovorů, což by vedlo k fragmentaci a neschopnosti různých agentur nebo organizací komunikovat během společných operací. BCP jako součást širšího standardu 3GPP MCPTT poskytuje tento společný jazyk. Definuje přesně, jak je hovor zahájen, jak jsou přidáváni účastníci a jak je relace spravována, což zajišťuje, že MCPTT klient od dodavatele A může úspěšně navázat skupinový hovor prostřednictvím serveru MCPTT od dodavatele B.

Dále BCP umožňuje integraci pokročilých funkcí telefonie založené na IP (zděděných z SIP) do oblasti s požadavky na vysokou spolehlivost, jako je přítomnost (presence), okamžité zprávy a integrace polohy, a přidává potřebná rozšíření pro veřejnou bezpečnost, jako je priorizace uživatelů, možnost přerušení a inherentní zabezpečení. Byla klíčovým prostředníkem pro přechod od starších systémů pozemní mobilní rádiové komunikace (LMR) k širokopásmovým službám Mission Critical Communications přes LTE/5G, často označovaným jako MCX (Mission Critical Services).

## Klíčové vlastnosti

- Standardizované řízení hovoru založené na SIP pro skupinové, privátní a nouzové hovory MCPTT
- Definuje specifické SIP metody, hlavičky a těla zpráv pro parametry MCPTT (např. ID skupiny, typ služby MCPTT)
- Spravuje procedury zřizování, modifikace a ukončení relace mezi klientem a serverem MCPTT
- Spolupracuje s částí řízení práva mluvit (Floor Control Part, FCP) pro koordinovanou správu hovoru a práva mluvit
- Podporuje základní funkce pro systémy s požadavky na vysokou spolehlivost (mission-critical), jako je přerušení (pre-emption), priorita a hovory signalizující bezprostřední nebezpečí
- Poskytuje stavové automaty a procedury pro řešení abnormálních stavů sítě a klienta

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.275** (Rel-19) — MO for MMTEL Basic Communication Part

---

📖 **Anglický originál a plná specifikace:** [BCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcp/)
