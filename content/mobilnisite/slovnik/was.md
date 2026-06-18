---
slug: "was"
url: "/mobilnisite/slovnik/was/"
type: "slovnik"
title: "WAS – Web Application Security"
date: 2026-01-01
abbr: "WAS"
fullName: "Web Application Security"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/was/"
summary: "Pracovní položka a soubor specifikací 3GPP zaměřené na identifikaci, analýzu a poskytování bezpečnostních řešení pro hrozby specifické pro webové aplikace a služby v mobilních sítích. Zabývá se zranit"
---

WAS je bezpečnostní iniciativa 3GPP, která analyzuje hrozby a poskytuje řešení pro webové aplikace v mobilních sítích, zabývající se zranitelnostmi plynoucími z použití webových technologií s využitím telekomunikačních API.

## Popis

Web Application Security (WAS) v 3GPP označuje systematické studium a standardizaci bezpečnostních mechanismů pro webové aplikace, které interagují s prostředím mobilních síťových operátorů nebo jsou v něm hostovány. Tato práce je klíčová, protože síťové funkce a servisní schopnosti jsou stále častěji vystavovány jako webově přívětivá [API](/mobilnisite/slovnik/api/) (např. RESTful API využívající [HTTP](/mobilnisite/slovnik/http/)/[JSON](/mobilnisite/slovnik/json/)) a aplikace samotné jsou budovány pomocí standardních webových technologií. Pracovní položka WAS analyzuje model hrozeb pro takové aplikace, který zahrnuje klasické webové zranitelnosti (jako je Cross-Site Scripting - XSS, Cross-Site Request Forgery - CSRF, injection útoky) i telekomunikačně specifické hrozby plynoucí z přístupu k citlivým síťovým API (např. lokalizace, data účastníků).

Architektonický důraz WAS je kladen na zabezpečení rozhraní mezi webovými aplikacemi a funkcemi pro vystavení sítě, jako je Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) v 5G nebo Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) ve 4G. Definuje bezpečnostní požadavky a směrnice pro API gatewaye, autentizaci, autorizaci a validaci vstupů. Klíčovým aspektem je zajištění, aby webové aplikace, které mohou být vyvíjeny třetími stranami, nemohly zneužít vystavené síťové schopnosti nebo získat přístup k datům mimo svá oprávnění. To zahrnuje definici bezpečných postupů kódování, runtime ochranných mechanismů a metodik bezpečnostního testování uzpůsobených pro webové aplikace využívající síťová API 3GPP.

Jak to funguje, zahrnuje několik úrovní. Na protokolové úrovni ukládá použití [TLS](/mobilnisite/slovnik/tls/) pro veškerou API komunikaci. Na aplikační vrstvě specifikuje použití robustních autentizačních frameworků jako je OAuth 2.0 pro delegovanou autorizaci, což zajišťuje, že webová aplikace jedná jménem uživatele s výslovným souhlasem. Poskytuje také směrnice pro implementaci správných kontrol přístupu na API gatewayi/[NF](/mobilnisite/slovnik/nf/), pro validaci a očištění všech vstupních parametrů z webové aplikace za účelem prevence injection útoků a pro bezpečnou správu API klíčů a tokenů. Specifikace WAS poskytují podrobnou analýzu vektorů útoku a předepisují protiopatření, která mají implementovat jak poskytovatel API (síťový operátor), tak konzument API (vývojář aplikace).

## K čemu slouží

WAS bylo zavedeno, aby řešilo nové bezpečnostní výzvy vzniklé posunem paradigmatu směrem k otevřenému vystavení sítě a webově orientovanému poskytování služeb v mobilních sítích, zejména s příchodem 4G a 5G. Tradiční telekomunikační bezpečnost se soustředila na ochranu uzavřené, signalizačně založené jádrové sítě (např. pomocí MAPsec, zabezpečení Diameter). Avšak když operátoři začali vystavovat síťové schopnosti (jako je kvalita služby, lokalizace, autentizace) prostřednictvím HTTP-based [API](/mobilnisite/slovnik/api/) za účelem podpory inovací a nových servisních ekosystémů, tato rozhraní se stala náchylná k celé nové třídě webových útoků, které byly dříve pro telekomunikace irelevantní.

Primární problém, který WAS řeší, je překlenutí propasti mezi osvědčenými postupy webové bezpečnosti a bezpečností telekomunikačních sítí. Bez takové standardizace by nekonzistentní nebo slabé implementace zabezpečení různými operátory nebo vývojáři aplikací mohly vést k závažným narušením, jako je hromadné sledování polohy, zosobnění účastníka nebo vyčerpání síťových zdrojů. Motivací pro jeho vytvoření ve verzi Rel-14 bylo rostoucí nasazování Network Exposure Functions a potřeba konzistentního, robustního bezpečnostního základu pro ochranu jak aktiv operátora, tak soukromí účastníka v tomto otevřeném prostředí.

Řeší omezení předchozích přístupů, kde byla bezpečnost pro nadstavbové služby často řešena individuálně pro každou službu nebo proprietárně, bez komplexního frameworku řízeného modelem hrozeb. WAS poskytuje standardizovanou, systematickou metodologii pro identifikaci hrozeb (prostřednictvím zpráv analýzy hrozeb) a specifikaci normativních bezpečnostních požadavků v příslušných specifikacích architektury a protokolů (např. pro NEF, CAPIF), což zajišťuje, že bezpečnost je od počátku zabudována do návrhu frameworků pro vystavení.

## Klíčové vlastnosti

- Analýza hrozeb a posouzení rizik specifických pro webové aplikace využívající síťová API 3GPP
- Bezpečnostní požadavky pro rozhraní Network Exposure Function (NEF) a Common API Framework (CAPIF)
- Směrnice pro implementaci OAuth 2.0 a OpenID Connect pro zabezpečenou autorizaci API
- Specifikace pro validaci vstupů, kódování výstupů a zmírnění běžných webových zranitelností (XSS, CSRF, injection)
- Doporučení pro zabezpečenou správu relací a nakládání s tokeny v webových aplikacích
- Směrnice pro bezpečnostní testování a prověření spolehlivosti webových aplikací v telekomunikačních prostředích

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)

## Definující specifikace

- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [WAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/was/)
