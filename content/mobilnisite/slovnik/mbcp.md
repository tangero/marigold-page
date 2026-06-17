---
slug: "mbcp"
url: "/mobilnisite/slovnik/mbcp/"
type: "slovnik"
title: "MBCP – Media Burst Control Protocol"
date: 2026-01-01
abbr: "MBCP"
fullName: "Media Burst Control Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mbcp/"
summary: "Řídicí protokol používaný ve službách Mission Critical Push-To-Talk (MCPTT) přes sítě 3GPP. Spravuje přidělování práva k vysílání (floor control) pro skupinovou komunikaci a rozhoduje, který uživatel"
---

MBCP (Media Burst Control Protocol) je řídicí protokol pro mediální přenosy používaný ve službách Mission Critical Push-To-Talk (MCPTT) ke správě přidělování práva k vysílání (floor control) a k rozhodování o tom, který uživatel v mluvčí skupině má oprávnění přenášet média.

## Popis

Media Burst Control Protocol (MBCP) je klíčový signalizační protokol v rámci architektury 3GPP Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně definovaný pro službu Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Jeho primární funkcí je poskytovat řízení přidělování práva k vysílání (floor control) pro poloduplexní skupinové komunikační relace. Floor control je mechanismus, který uděluje výhradní oprávnění – tzv. 'právo k vysílání' – jedinému účastníkovi v mluvčí skupině k odesílání médií (hlasu, videa nebo dat) v daném okamžiku, čímž předchází kolizím a zajišťuje uspořádanou komunikaci. MBCP funguje jako aplikační protokol, typicky běžící nad spolehlivými transportními protokoly, jako je TCP nebo TLS.

Z architektonického hlediska jsou zprávy MBCP vyměňovány mezi klientem MCPTT (na zařízení uživatele) a serverem MCPTT (v síti). Protokol definuje stavový automat pro entity řízení práva k vysílání. Mezi klíčové typy zpráv patří Požadavek na právo k vysílání (Floor Request, odeslaný uživatelem, který chce mluvit), Udělení práva k vysílání (Floor Granted, odeslané serverem oprávněnému uživateli), Uvolnění práva k vysílání (Floor Release, odeslané uživatelem po dokončení vysílání) a Zamítnutí práva k vysílání (Floor Deny, odeslané serverem, pokud je požadavek odmítnut). Server MCPTT funguje jako centrální rozhodčí, který zpracovává konkurenční požadavky na základě nastavených priorit, pravidel přednostního přerušení (pre-emption) a aktuálního stavu práva k vysílání.

MBCP spolupracuje s protokoly pro přenos médií (jako je RTP) a protokoly pro řízení relace (jako je SIP). Když uživatel stiskne tlačítko pro vysílání (push-to-talk), klient MCPTT odešle na server zprávu MBCP Floor Request. Server vyhodnotí požadavek podle politik – jako je priorita uživatele, nastavení skupiny a to, zda probíhá nouzové volání – a rozhodne o udělení nebo zamítnutí práva k vysílání. Pokud je právo uděleno, server odešle zprávu Floor Granted žádajícímu klientovi a zprávu Floor Taken všem ostatním účastníkům ve skupině, čímž je informuje, že právo k vysílání je obsazeno. Udělený klient pak může začít streamovat média. Po uvolnění server odešle zprávy Floor Idle. Toto přesné řízení je klíčové pro efektivní a disciplinovanou komunikaci ve scénářích veřejné bezpečnosti a kritických misí, kde může být jasný a nepřerušovaný projev otázkou života a smrti.

## K čemu slouží

MBCP byl vytvořen k řešení základního problému správy soutěžení o médium v poloduplexní skupinové hlasové komunikaci přes IP-based mobilní sítě. Tradiční systémy pozemní mobilní rádiové komunikace (Land Mobile Radio, [LMR](/mobilnisite/slovnik/lmr/)) měly vestavěné, často hardwarové, mechanismy řízení práva k vysílání. Když organizace veřejné bezpečnosti usilovaly o migraci na širokopásmové sítě LTE a 5G v rámci iniciativy 3GPP Mission Critical Services, byl standardizovaný, robustní a funkčně bohatý protokol pro řízení práva k vysílání nezbytný. Jednoduché konferenční protokoly pro hlas přes IP (VoIP) postrádaly specifické požadavky na prioritní, přednostně přerušitelné a spolehlivé rozhodování o mluvčím, které potřebují záchranáři.

Protokol řeší omezení ad-hoc nebo nestandardizovaných přístupů tím, že poskytuje jednotný způsob správy práva k vysílání napříč zařízeními různých výrobců a síťovými nasazeními. Umožňuje pokročilé funkce klíčové pro operace kritické pro plnění mise: udělování práva k vysílání na základě priority (aby hovor velitele mohl přerušit hovor běžného důstojníka), frontu požadavků, přednostní přerušení (pre-emption) mluvčích s nižší prioritou a explicitní zamítnutí s uvedením důvodu. Vytvoření MBCP ve verzi Release 13 bylo základním kamenem standardizace [MCPTT](/mobilnisite/slovnik/mcptt/), které zajišťuje interoperabilitu a garantuje, že skupinová komunikace přes komerční mobilní sítě může splňovat přísné požadavky na spolehlivost, řízení a latenci kladené uživateli z oblasti veřejné bezpečnosti a průmyslu.

## Klíčové vlastnosti

- Rozhodování o výhradních přenosových právech (právo k vysílání) v mluvčí skupině
- Podpora fronty požadavků na právo k vysílání a jeho udělování na základě priority
- Schopnost přednostního přerušení (pre-emption) pro uživatele s vyšší prioritou nebo nouzové hovory
- Spolehlivé doručování zpráv pro kritickou řídicí signalizaci
- Integrace s řízením volání MCPTT a mediální rovinou 3GPP
- Oznámení stavu práva k vysílání (obsazeno, volné, uděleno) všem členům skupiny

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [MBCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbcp/)
