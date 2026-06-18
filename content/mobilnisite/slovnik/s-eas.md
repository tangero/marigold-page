---
slug: "s-eas"
url: "/mobilnisite/slovnik/s-eas/"
type: "slovnik"
title: "S-EAS – Source Edge Application Server"
date: 2026-01-01
abbr: "S-EAS"
fullName: "Source Edge Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/s-eas/"
summary: "Edge Application Server (EAS) v síti 5G, který hostuje instanci aplikace, kterou uživatelské zařízení (UE) aktuálně používá nebo z níž se migruje. Jedná se o klíčovou funkční entitu v architektuře Edg"
---

S-EAS je Edge Application Server (hraniční aplikační server) v architektuře edge computingu 5G, který aktuálně hostuje instanci aplikace používanou uživatelským zařízením nebo z níž se migruje, a tím zajišťuje kontinuitu služby.

## Popis

Source Edge Application Server (S-EAS) je klíčová funkční entita v rámci 3GPP frameworku pro objevování a mobilitu Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)) definovaného pro integraci 5G systému s edge computingem. Nachází se v datové síti ([DN](/mobilnisite/slovnik/dn/)), typicky na konkrétní hraniční lokalitě (např. na hostiteli Multi-access Edge Computing ([MEC](/mobilnisite/slovnik/mec/))). S-EAS je definován svým stavem vzhledem k aplikační relaci uživatelského zařízení (UE): je to EAS, který aktuálně poskytuje aplikační službu UE před tím, než je spuštěna potenciální migrace. Jeho architektura je součástí širšího ekosystému EAS, který zahrnuje cílový EAS ([T-EAS](/mobilnisite/slovnik/t-eas/)), Edge Enabler Server ([EES](/mobilnisite/slovnik/ees/)) a Edge Enabler Client ([EEC](/mobilnisite/slovnik/eec/)) v UE.

S-EAS spolupracuje s dalšími hraničními entitami na podpoře mobility aplikačního kontextu. Když podmínky vyžadují migraci (např. pohyb UE, vyrovnávání zátěže nebo optimalizace zdrojů), systém zahájí proceduru přenosu aplikační relace ze S-EAS na T-EAS. Klíčovou rolí S-EAS je poskytnout aplikační kontext T-EAS. Tento kontext zahrnuje vnitřní stav aplikační relace nezbytný pro plynulou kontinuitu, jako jsou data uživatelské relace, stavy transakcí nebo mediální buffery. Přesný obsah tohoto kontextu je závislý na aplikaci a je definován mimo 3GPP, ale architektura 3GPP poskytuje signalizační framework umožňující jeho přenos.

Jak migrace funguje, zahrnuje několik kroků. EEC nebo síť spustí vyhledání vhodnějšího T-EAS prostřednictvím EES. Jakmile je T-EAS vybrán, je provedena procedura přenosu kontextu. S-EAS obdrží požadavek (předaný prostřednictvím EES) na poskytnutí aplikačního kontextu. Ten následně zabalí a bezpečně odešle T-EAS. Po úspěšném přenosu a potvrzení je provoz UE přesměrován na T-EAS a S-EAS může nakonec ukončit starou relaci. S-EAS komunikuje s EES pomocí referenčního bodu EDGE-9 (mezi EES a EAS) a přenos kontextu může využívat referenční bod EDGE-10 (EAS-to-EAS), jak je definováno v TS 23.558.

Jeho role je klíčová pro naplnění slibu edge computingu: služeb s nízkou latencí a vysokou propustností, které následují uživatele. Formální definicí S-EAS a procedur pro předání z něj umožňuje 3GPP stavovou mobilitu aplikací napříč hraničními uzly. Jedná se o významný pokrok oproti prostému přesměrování spojení, protože zachovává interaktivní stav aplikace, což je zásadní pro imerzivní služby jako rozšířená realita, cloudové hraní nebo průmyslové řízení, kde je přerušení relace nepřijatelné.

## K čemu slouží

Koncept S-EAS byl vytvořen k řešení základní výzvy v mobilním edge computingu: jak přesunout běžící, stavovou instanci aplikace spolu s pohyblivým uživatelem bez přerušení služby. Před jeho standardizací byly nasazení edge computingu často považovány aplikační servery za statické koncové body. Pokud se uživatel přesunul, odpojil se od jednoho serveru a připojil se k jinému, čímž ztratil veškerý stav relace – přístup typu 'break-before-make', nevhodný pro interaktivní služby v reálném čase. Motivací pro model S-EAS/[T-EAS](/mobilnisite/slovnik/t-eas/) bylo umožnit mobilitu aplikací typu 'make-before-break'.

To bylo hnací silou požadavků nových vertikál 5G nastíněných v Rel-16 a Rel-17, jako je komunikace vozidlo-vše ([V2X](/mobilnisite/slovnik/v2x/)), průmyslový IoT a imerzivní média. Tyto aplikace vyžadují ultra-nízkou latenci a vysokou spolehlivost, což edge computing poskytuje, ale také předpokládají mobilitu uživatele. Stávající síťová mobilita (předání spojení) spravuje pouze spojení na IP vrstvě, nikoli stav aplikační vrstvy. Entita S-EAS formalizuje 'zdroj' aplikačního stavu a poskytuje jasný bod kotvení, ze kterého lze kontext migrovat.

Řeší tak omezení bezstavových hraničních služeb zavedením standardizované procedury pro přenos stavu. To umožňuje poskytovatelům aplikací implementovat hraniční aplikace s podporou mobility, které mohou svůj kontext vystavit prostřednictvím definovaného rozhraní. Vytvoření role S-EAS v rámci architektury 3GPP zajišťuje, že edge computing není jen o blízkosti, ale také o kontinuitě, čímž se z hraničního prostředí stává plynulé a dynamické rozšíření cloudu, které následuje uživatele, což je klíčový diferenciátor pro služby využívající 5G.

## Klíčové vlastnosti

- Hostuje aktivní instanci hraniční aplikace pro konkrétní relaci UE
- Ukládá a poskytuje aplikačně specifický kontext pro mobilitu
- Podílí se na standardizovaných procedurách přenosu aplikačního kontextu
- Komunikuje s Edge Enabler Serverem (EES) přes referenční bod EDGE-9
- Komunikuje s cílovým EAS (T-EAS) pro přímý přenos kontextu
- Umožňuje kontinuitu služeb pro stavové aplikace během mobility UE

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [S-EAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-eas/)
