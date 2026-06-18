---
slug: "sdk"
url: "/mobilnisite/slovnik/sdk/"
type: "slovnik"
title: "SDK – Software Development Kit"
date: 2025-01-01
abbr: "SDK"
fullName: "Software Development Kit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sdk/"
summary: "Software Development Kit (SDK) v kontextu 3GPP poskytuje vývojářům knihovny, nástroje a API pro tvorbu aplikací, které komunikují se síťovými schopnostmi. Abstrahuje složité síťové funkce, což umožňuj"
---

SDK (Software Development Kit) je sada knihoven, nástrojů a API, která vývojářům umožňuje vytvářet aplikace abstrakcí složitých funkcí sítě 3GPP, jako je QoS, lokalizace a autentizace.

## Popis

V ekosystému 3GPP se termín Software Development Kit (SDK) vztahuje k sadě softwarových nástrojů a knihoven poskytovaných vývojářům aplikací za účelem usnadnění tvorby služeb, které mohou komunikovat s mobilní sítí a využívat její schopnosti. Na rozdíl od obecných SDK konkrétně 3GPP SDK zpřístupňuje aplikační programová rozhraní ([API](/mobilnisite/slovnik/api/)), která abstrahují podkladové síťové funkce definované ve specifikacích 3GPP. Tato API umožňují aplikacím vyžádat síťové prostředky, přistupovat k informacím o účastníkovi (s jeho souhlasem) nebo využívat služby, jako je kvalita služeb (QoS), lokalizace zařízení nebo platební služby, aniž by vyžadovala hluboké znalosti protokolů jádra sítě. SDK typicky zahrnuje knihovny kódu, dokumentaci, ukázkové aplikace a někdy i simulátory nebo testovací nástroje.

Architektura pro zpřístupnění sítě, ke které se SDK připojuje, je v jádru sítě 5G (5G Core) založena na funkci Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a v jádru sítě 4G (4G EPC) na funkci Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)). SDK poskytuje klientskou knihovnu, která s těmito expozičními funkcemi komunikuje prostřednictvím standardizovaných API, nejčastěji založených na RESTful principech přes [HTTPS](/mobilnisite/slovnik/https/). Například aplikace využívající SDK může vyvolat metodu pro vyžádání garantované přenosové rychlosti pro video stream. Klientská knihovna SDK by tento požadavek naformátovala do příslušného volání API (např. pomocí severozápadního API 3GPP, N33) a bezpečně jej odeslala do NEF. NEF pak tento externí požadavek API přeloží na interní síťové příkazy a ve spolupráci s funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) nastaví příslušnou politiku QoS.

Klíčové komponenty 3GPP SDK zahrnují moduly pro autentizaci a zabezpečení, které zajišťují bezpečnou registraci a přístup založený na tokenech (pomocí OAuth 2.0), klientské knihovny API pro všechny podporované síťové schopnosti (např. QoS na vyžádání, lokalizace zařízení, notifikace o stavu sítě) a datové modelové objekty odpovídající informačním prvkům definovaným v 3GPP. Úlohou SDK je výrazně snížit vstupní bariéru pro vývojáře služeb a umožnit jim inovovat začleněním telekomunikačních funkcí do aplikací pro vertikály, jako jsou hry, rozšířená realita, IoT a podniková komunikace. SDK funguje jako klíčový most mezi aplikační vrstvou a řídicí rovinou sítě a podporuje ekosystém aplikací s povědomím o síti.

## K čemu slouží

Standardizace SDK a expozičních [API](/mobilnisite/slovnik/api/) v rámci 3GPP, zejména od vydání Release 17, řeší historický problém: 'uzavřenou zahradu' (walled garden) telekomunikačních sítí. Tradičně byly síťové schopnosti izolované a přístupné pouze vlastním službám operátora, což brzdilo inovace od vývojářů třetích stran. To omezovalo tvorbu nových, diferencovaných služeb, které by mohly využívat jedinečné atributy mobilních sítí, jako je nízká latence, přesná lokalizace nebo garantované připojení.

Motivace pro vytváření standardizovaných 3GPP SDK spočívá v otevření sítě bezpečným, řízeným a zpoplatnitelným způsobem. Řeší problém složité integrace poskytnutím jednoduchého, dobře zdokumentovaného a jednotného rozhraní pro vývojáře, které abstrahuje podkladovou síťovou složitost. To umožňuje operátorům monetizovat jejich síťové prostředky nad rámec pouhé konektivity a podnikům a poskytovatelům aplikací dynamicky přizpůsobovat chování sítě jejich specifickým potřebám. Zavedení SDK je klíčovým prvkem pro naplnění vize 5G o síťových řezech (network slicing) a služebně orientované architektuře, protože umožňuje automatizované, na vyžádání poskytování síťových prostředků pro množství nových případů užití.

## Klíčové vlastnosti

- Abstrakce složitých síťových API 3GPP do jednoduchých programových rozhraní
- Integrovaná autentizace a autorizace (např. klient OAuth 2.0)
- Klientské knihovny pro schopnosti jako správa QoS, lokalizace zařízení a monitorování
- Zahrnuje dokumentaci, ukázky kódu a návody osvědčených postupů
- Často obsahuje lokální simulátor pro vývoj a testování bez živé sítě
- Zajišťuje bezpečnou, standardizovanou komunikaci s vrstvou pro zpřístupnění sítě (NEF/SCEF)

## Související pojmy

- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)

## Definující specifikace

- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [SDK na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdk/)
