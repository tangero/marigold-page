---
slug: "sntp"
url: "/mobilnisite/slovnik/sntp/"
type: "slovnik"
title: "SNTP – Simple Network Time Protocol"
date: 2025-01-01
abbr: "SNTP"
fullName: "Simple Network Time Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sntp/"
summary: "Zjednodušená verze protokolu NTP používaná pro synchronizaci hodin v sítích 3GPP. Poskytuje přesné rozvádění času pro síťové prvky a uživatelská zařízení, což je klíčové pro časově citlivé aplikace, ú"
---

SNTP je zjednodušená verze protokolu Network Time Protocol (NTP) používaná pro přesnou synchronizaci hodin síťových prvků a uživatelských zařízení v sítích 3GPP.

## Popis

Simple Network Time Protocol (SNTP) je protokol pro synchronizaci času definovaný ve standardech 3GPP, který poskytuje odlehčenou metodu pro rozvádění koordinovaného světového času ([UTC](/mobilnisite/slovnik/utc/)) napříč síťovými prvky a uživatelskými zařízeními (UE). Funguje jako podmnožina plnohodnotného protokolu Network Time Protocol ([NTP](/mobilnisite/slovnik/ntp/)), který zjednodušuje implementaci na straně klienta odstraněním složitých algoritmů používaných pro výběr serveru a disciplínu hodin, což jej činí vhodným pro zařízení s omezenými prostředky. V architektuře 3GPP typicky SNTP funguje v modelu klient-server, kde síťový prvek, jako je UE nebo síťový uzel, funguje jako klient SNTP a žádá o časové informace od serveru SNTP, který je často integrován nebo asociován s funkcí Network Time Server v jádru sítě.

Protokol funguje tak, že klient odešle požadavek na server, který obsahuje časovou značku odeslání z klienta. Server odpoví paketem obsahujícím své vlastní časové značky přijetí a odeslání. Pomocí těchto časových značek může klient vypočítat zpoždění na trase a odchylku mezi svými hodinami a hodinami serveru, což mu umožní upravit svůj místní čas. Tento proces je klíčový pro sladění vnitřních hodin různých síťových komponent na společný časový referenční bod. Mezi klíčové komponenty patří klientský software SNTP umístěný v UE nebo síťovém uzlu, server SNTP poskytující autoritativní zdroj času a podkladová IP přenosová vrstva (často přes User Datagram Protocol, [UDP](/mobilnisite/slovnik/udp/)) používaná pro výměnu zpráv.

Jeho role v síti je zásadní pro řadu funkcí. Přesná synchronizace času je nezbytná pro správný provoz duplexování s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)) v rádiové přístupové síti (RAN), pro časové označování záznamů o účtování v jádru sítě za účelem zajištění přesného účtování a pro bezpečnostní mechanismy spoléhající na časová razítka, jako je ověřování bezpečnostních certifikátů. Pro služby jako jsou služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)), multimediální vysílání a služby kritické pro misi zajišťuje synchronizovaný čas správné zaznamenávání a koordinaci událostí napříč různými síťovými entitami, což umožňuje bezproblémové poskytování služeb a interoperabilitu.

## K čemu slouží

SNTP byl zaveden, aby řešil základní potřebu přesné a spolehlivé synchronizace času napříč všemi prvky mobilní sítě 3GPP. Před jeho standardizací mohly síťové prvky spoléhat na různorodé, proprietární nebo méně přesné metody měření času, což vedlo k nekonzistencím, které mohly narušit provoz sítě, přesnost účtování a kvalitu služeb. Rozšíření IP služeb a rostoucí požadavky na přesnost nových rádiových technologií si vyžádaly standardizovaný, odlehčený protokol, který by mohl být široce implementován, od výkonných serverů jádra sítě až po uživatelská zařízení napájená bateriemi.

Vytvoření SNTP v rámci 3GPP bylo motivováno omezeními použití plné implementace [NTP](/mobilnisite/slovnik/ntp/) v prostředích s omezenými prostředky. Plný NTP zahrnuje sofistikované algoritmy pro správu více časových zdrojů, filtrování a disciplínu hodin, které jsou výpočetně náročné a vyžadují významnou paměť. Pro mnohé implementace UE a specifické síťové funkce je tato složitost zbytečná. SNTP poskytuje zjednodušený režim 'pouze klient', který splňuje základní požadavek na získání času z důvěryhodného serveru bez této režie, což jej činí ideálním pro integraci do široké škály zařízení. Řeší problém poskytnutí všudypřítomné, standardy založené metody pro rozvádění času, která je dostatečně přesná pro telekomunikační aplikace a zároveň dostatečně efektivní pro hromadné nasazení, čímž zajišťuje celosíťovou časovou koherenci, která je předpokladem pro pokročilé služby, správu sítě a zabezpečení.

## Klíčové vlastnosti

- Odlehčená klientská implementace odvozená od NTP
- Funguje přes UDP/IP pro efektivní přenos
- Poskytuje synchronizaci hodin s primárním časovým zdrojem (např. UTC)
- Vypočítává síťové zpoždění a odchylku hodin pomocí výměny časových značek
- Podporuje unicastový režim klient-server pro časové požadavky
- Umožňuje přesnost synchronizace vhodnou pro telekomunikační aplikace (např. účtování, zabezpečení)

## Související pojmy

- [NTP – Network Time Protocol](/mobilnisite/slovnik/ntp/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [UTC – Coordinated Universal Time](/mobilnisite/slovnik/utc/)

## Definující specifikace

- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming

---

📖 **Anglický originál a plná specifikace:** [SNTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sntp/)
