---
slug: "wae"
url: "/mobilnisite/slovnik/wae/"
type: "slovnik"
title: "WAE – Wireless Application Environment"
date: 2025-01-01
abbr: "WAE"
fullName: "Wireless Application Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wae/"
summary: "Wireless Application Environment (WAE) je aplikační rámec ve vrstvě protokolu Wireless Application Protocol (WAP). Definuje základní programovací model, značkovací jazyk (WML), skriptovací jazyk (WMLS"
---

WAE je aplikační rámec WAP, který definuje základní programovací model, značkovací a skriptovací jazyky a formáty obsahu pro poskytování interaktivních služeb mobilním zařízením s omezenými schopnostmi.

## Popis

Wireless Application Environment (WAE) je komplexní aplikační rámec tvořící nejvyšší vrstvu architektury Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)). Jeho hlavní úlohou je poskytovat interoperabilní prostředí pro vývoj a provádění aplikací na mobilních zařízeních s omezenými prostředky, jako byly například rané feature telefony. WAE je v podstatě fúzí konceptů World Wide Web a mobilní telefonie, optimalizovanou pro úzkopásmové sítě a zařízení s malými displeji, omezenou pamětí a jednoduchými vstupními metodami. Jádro WAE tvoří definice Wireless Markup Language ([WML](/mobilnisite/slovnik/wml/)), značkovacího jazyka založeného na [XML](/mobilnisite/slovnik/xml/) podobného zjednodušenému [HTML](/mobilnisite/slovnik/html/), navrženého pro vytváření 'balíčků' (decks) 'karet' (cards, stránek), které jsou efektivně kódovány v binárním formátu pro přenos. WML doplňuje WMLScript, odlehčený klientský skriptovací jazyk podobný JavaScriptu, který umožňuje procedurální logiku, validaci dat a lokální řízení dialogů bez nutnosti zpětných dotazů na server. Uživatelský agent WAE, typicky mikroprohlížeč v telefonu, je zodpovědný za interpretaci WML, provádění WMLScript a vykreslování obsahu. WAE také specifikuje sadu definovaných formátů obsahu pro obrázky (WBMP), kalendářní události (vCalendar) a vizitky (vCard), což zajišťuje konzistentní zpracování napříč zařízeními. Rámec zahrnuje WAE Push framework, umožňující serverům asynchronně odesílat obsah na zařízení, což byl předchůdce moderních push notifikací. Architektonicky se WAE nachází nad WAP Session Protocol ([WSP](/mobilnisite/slovnik/wsp/)), Transaction Protocol ([WTP](/mobilnisite/slovnik/wtp/)), Security Layer ([WTLS](/mobilnisite/slovnik/wtls/)) a Transport Layer ([WDP](/mobilnisite/slovnik/wdp/)), a spoléhá na ně pro správu relace, spolehlivé transakce, zabezpečení a adaptaci na přenosovou vrstvu.

## K čemu slouží

WAE bylo vytvořeno za účelem řešení kritického problému přinášení interaktivních datových služeb masovému trhu mobilních telefonů na konci 90. let a počátku 21. století, v období dominovaném sítěmi s přepojováním okruhů (jako GSM CSD) a zařízeními neschopnými provozovat plnohodnotný webový prohlížeč. Motivací bylo definovat univerzální otevřený standard, který by prolomil fragmentaci proprietárních platforem mobilních služeb. Před WAP/WAE byly služby s přidanou hodnotou často specifické pro výrobce, což omezovalo dostupnost obsahu a interoperabilitu. WAE si kladlo za cíl replikovat úspěch otevřených standardů World Wide Web (HTML, HTTP), avšak v rámci přísných omezení mobilních sítí (nízká šířka pásma, vysoká latence) a zařízení (malé obrazovky, omezený výkon CPU). Vyřešilo problém adaptace obsahu zavedením WML, který byl navržen pro efektivní kompresi a navigaci pomocí telefonní klávesnice, nikoli myši. WMLScript poskytl nezbytnou vrstvu interaktivity bez nutnosti spoléhat se na zpracování na serveru pro každou akci, čímž zlepšil uživatelský zážitek při pomalém připojení. Ačkoli byl WAE a WAP nakonec nahrazen plnohodnotnými HTML prohlížeči a vysokorychlostními paketovými sítěmi (3G/4G), sehrály klíčovou roli v demonstraci poptávky po mobilních datech, ustavení obchodních modelů pro mobilní obsah a přípravě cesty pro moderní ekosystém mobilního internetu.

## Klíčové vlastnosti

- Definuje Wireless Markup Language (WML) pro vytváření navigovatelných balíčků obsahu optimalizovaných pro malé obrazovky
- Specifikuje WMLScript, odlehčený klientský skriptovací jazyk pro přidání logiky a interaktivity do stránek WML
- Zahrnuje model uživatelského agenta založený na mikroprohlížeči pro vykreslování WML a provádění WMLScript na zařízení
- Specifikuje standardní formáty obsahu jako Wireless Bitmap (WBMP) pro obrázky, vCalendar a vCard
- Poskytuje Push framework pro serverem iniciované doručování obsahu a servisních indikací
- Nabízí schéma URL a integraci s telefonními funkcemi (WTAI) pro přístup k funkcím zařízení, jako je volání přímo z WML

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/wae/)
