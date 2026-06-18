---
slug: "wgw"
url: "/mobilnisite/slovnik/wgw/"
type: "slovnik"
title: "WGW – WAP Gateway"
date: 2005-01-01
abbr: "WGW"
fullName: "WAP Gateway"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wgw/"
summary: "Síťový prvek, který zprostředkovává služby Wireless Application Protocol (WAP) tím, že funguje jako prostředník mezi mobilními zařízeními a internetovými servery. Překládá protokoly WAP (např. WSP, WT"
---

WGW je síťový prvek, který funguje jako prostředník a překládá protokoly WAP na standardní webové protokoly, aby umožnil časným mobilním zařízením přístup k internetovým službám.

## Popis

[WAP](/mobilnisite/slovnik/wap/) Gateway (WGW) je klíčová síťová komponenta specifikovaná v 3GPP pro zajištění služeb založených na Wireless Application Protocol (WAP) v sítích 2G a 3G. Funguje jako brána pro překlad protokolů, která stojí mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelským zařízením (UE) a původními servery na internetu nebo v operátorově intranetu. WGW primárně převádí požadavky a odpovědi mezi zásobníkem protokolů WAP používaným přes rozhraní rádiové komunikace a standardní sadou internetových protokolů používanou v drátových sítích. Zásobník WAP zahrnuje protokoly jako Wireless Session Protocol ([WSP](/mobilnisite/slovnik/wsp/)) pro správu relací, Wireless Transaction Protocol ([WTP](/mobilnisite/slovnik/wtp/)) pro zpracování transakcí a Wireless Transport Layer Security ([WTLS](/mobilnisite/slovnik/wtls/)) pro šifrování, zatímco internetová strana typicky používá [HTTP](/mobilnisite/slovnik/http/), [TCP/IP](/mobilnisite/slovnik/tcp-ip/) a [TLS](/mobilnisite/slovnik/tls/).

Architektonicky WGW rozhraní s více síťovými prvky. Na mobilní straně se připojuje přes paketově přepínanou páteřní síť, jako je síť GPRS v 2G/3G, a přijímá data přes GGSN (Gateway GPRS Support Node). Na straně internetu komunikuje s webovými servery nebo aplikačními servery. WGW vykonává kritické funkce, jako je převod protokolů, kódování/dekódování obsahu a ukládání do mezipaměti. Například když mobilní uživatel požaduje WAP stránku, UE odešle požadavek WSP přes rádiové rozhraní; WGW jej přijme, přeloží na HTTP požadavek, přepošle jej webovému serveru, obdrží HTTP odpověď, zakóduje obsah (např. do kompaktního binárního formátu WML) a odešle jej zpět k UE přes WSP. Tento proces optimalizuje data pro rádiové spoje s omezenou přenosovou kapacitou.

Klíčové komponenty uvnitř WGW zahrnují překladače protokolů, adaptéry obsahu a bezpečnostní moduly. Brána často obsahuje kodér WML (Wireless Markup Language) pro převod HTML nebo jiného webového obsahu do WML, což je odlehčený značkovací jazyk navržený pro malé obrazovky. Může také obsahovat mechanismus ukládání do mezipaměti pro ukládání často přistupovaného obsahu, čímž se snižuje latence a zatížení sítě. Z hlediska své role WGW umožňuje základní mobilní internetové služby, jako je prohlížení, e-mail a stahování na zařízeních před érou smartphoneů. Funguje jako centrální bod pro implementaci operátorově specifických služeb, jako je účtování na základě využití WAP nebo filtrování obsahu. Přestože je WGW v moderních sítích 4G/5G z velké části zastaralý kvůli přímému prohlížení založenému na IP, byl zásadní pro raný ekosystém mobilních dat, který překlenul propast mezi omezenými mobilními zařízeními a plnohodnotným internetem.

## K čemu slouží

WAP Gateway byl vytvořen, aby řešil omezení časných mobilních zařízení, která měla omezený výpočetní výkon, paměť a možnosti zobrazení a fungovala v pomalých sítích s vysokou latencí. Před nástupem smartphoneů s plnohodnotnými HTML prohlížeči byl přímý přístup k internetovému obsahu nepraktický kvůli robustní povaze webových protokolů a obsahu. WAP poskytoval optimalizovanou alternativu, ale vyžadoval bránu pro překlad mezi optimalizovanými bezdrátovými protokoly a standardní internetovou infrastrukturou.

Motivace pro WGW vycházela z potřeby přinést webové služby na masový trh feature phoneů na konci 90. let a počátku 21. století. Operátoři chtěli nabízet služby s přidanou hodnotou, jako jsou zprávy, počasí a jednoduché transakce, aniž by museli měnit stávající webové servery. WGW tento problém vyřešil tím, že fungoval jako transparentní prostředník schopný přizpůsobit obsah a protokoly. Také umožnil operátorům kontrolovat a zpoplatňovat datový provoz, protože brána mohla implementovat systémy účtování, uzavřené zahrady (walled gardens) a filtrování obsahu. Toto byl klíčový obchodní model během vzestupu mobilních dat.

Dále WGW řešil technické výzvy, jako je vysoká latence a ztráta paketů na rádiových spojích. Použitím binárního kódování a zjednodušených transakčních protokolů snížil režii ve srovnání s TCP/HTTP. Jeho omezení, včetně přístupu 'uzavřené zahrady' a horší uživatelské zkušenosti ve srovnání s plnohodnotným webem, však nakonec vedly k jeho úpadku. Vývoj směrem k plně IP sítím v 3GPP Rel-5 a novějších, s přímým HTTP prohlížením na výkonnějších zařízeních, učinil WGW zastaralým, ale sehrál klíčovou historickou roli v průkopnictví mobilního přístupu k internetu.

## Klíčové vlastnosti

- Překlad protokolů mezi zásobníkem WAP (WSP/WTP) a internetovými protokoly (HTTP/TCP/IP)
- Adaptace a kódování obsahu, např. převod HTML na Wireless Markup Language (WML)
- Ukládání často přistupovaného WAP obsahu do mezipaměti pro zlepšení výkonu a snížení latence
- Podpora Wireless Transport Layer Security (WTLS) pro zajištění šifrování přes rádiové rozhraní
- Integrace s operátorovými systémy účtování pro zpoplatnění služeb WAP
- Funguje jako prostředník pro implementaci uzavřených zahrad (walled gardens) a filtrování obsahu

## Související pojmy

- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [VHE – Virtual Home Environment](/mobilnisite/slovnik/vhe/)
- [WML – Wireless Mark-up Language](/mobilnisite/slovnik/wml/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [WGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/wgw/)
