---
slug: "ngsi"
url: "/mobilnisite/slovnik/ngsi/"
type: "slovnik"
title: "NGSI – Next Generation Service Interfaces"
date: 2025-01-01
abbr: "NGSI"
fullName: "Next Generation Service Interfaces"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ngsi/"
summary: "NGSI je soubor standardizovaných northbound API, které umožňují externím aplikacím objevovat, vyžadovat a interagovat s možnostmi a daty sítě 3GPP. Poskytuje jednotné, zabezpečené a programovatelné ro"
---

NGSI je soubor standardizovaných northbound API, které umožňují externím aplikacím objevovat, vyžadovat a interagovat s možnostmi a daty sítě 3GPP pro vystavení služeb.

## Popis

Rozhraní příští generace pro služby (Next Generation Service Interfaces, NGSI) jsou klíčovým prvkem architektury založené na službách (Service-Based Architecture, SBA) dle 3GPP, definovaným primárně pro 5G jádro sítě (5G Core, 5GC). Představují standardizovaná aplikační programová rozhraní (Application Programming Interfaces, [API](/mobilnisite/slovnik/api/)), která síťové funkce (Network Functions, NFs) používají pro vzájemnou interní komunikaci (southbound) a, což je důležitější, pro vystavení síťových schopností a informací autorizovaným externím aplikačním funkcím (Application Functions, AFs) směrem ven ze sítě (northbound). Tato rozhraní jsou založena na [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/), využívají principy RESTful nebo asynchronní notifikace, což je činí vstřícnými k webu a snadno použitelnými vývojáři třetích stran. Specifikace, jako jsou TS 23.222 a TS 23.722, podrobně popisují procedury, datové modely a bezpečnostní mechanismy pro tyto interakce.

Z architektonického hlediska NGSI funguje prostřednictvím klíčové síťové funkce zvané Funkce pro vystavení sítě (Network Exposure Function, [NEF](/mobilnisite/slovnik/nef/)). NEF funguje jako zabezpečená brána a bod vynucování politik mezi sítí 3GPP a externími [AF](/mobilnisite/slovnik/af/). Když aplikace potřebuje přístup k síťovým datům (např. poloha uživatele, stav sítě) nebo požaduje specifické síťové chování (např. ovlivnění směrování provozu, konfigurace QoS), nekomunikuje přímo s jádrovými [NF](/mobilnisite/slovnik/nf/), jako je [PCF](/mobilnisite/slovnik/pcf/) nebo [SMF](/mobilnisite/slovnik/smf/). Místo toho odešle požadavky API k NEF. NEF požadavek ověří a autorizuje, přeloží externí volání API na interní signalizaci 3GPP (pomocí rozhraní založených na službách, jako jsou Npcf nebo Nsmf), a poté vrátí odpověď zpět k AF. Tato abstraktní vrstva chrání jádro sítě a poskytuje konzistentní, verzované API bez ohledu na interní změny v síti.

Fungování NGSI zahrnuje několik klíčových procedur. Pro vystavení schopností si může AF přihlásit odběr konkrétních událostí (např. změna stavu dosažitelnosti UE) a přijímat notifikace při jejich výskytu. Pro poskytování parametrů služby může AF předat síti očekávané parametry služby, které rámec politik (PCF) může použít k přijetí vhodných rozhodnutí o QoS. Rozhraní podporují jak model požadavek-odpověď, tak model přihlášení-oznámení. Mezi klíčová NGSI API patří Nnef (pro interakci externích AF s NEF) a interní SBI API jako Nnrf (objevování NF), Npcf (řízení politik) a Nudm (sjednocená správa dat). Poskytnutím těchto standardizovaných rozhraní NGSI umožňuje případy užití jako koordinaci edge computingu, vylepšenou kvalitu uživatelského zážitku pro aplikace a správu zařízení IoT.

## K čemu slouží

NGSI bylo vytvořeno k vyřešení kritického problému 'zahrad s vysokou zdí' (walled garden), kde byly cenné síťové schopnosti a data nedostupné poskytovatelům služeb třetích stran. V před-5G sítích bylo vystavování síťových funkcí často realizováno prostřednictvím proprietárních, nestandardizovaných bran, což omezovalo inovace, zpomalovalo nasazování služeb a vytvářelo bezpečnostní rizika. Vzestup aplikací pro vertikální odvětví (např. automobilový průmysl, Průmysl 4.0, rozšířená realita) si vyžádal přímý, programovatelný přístup k síťové inteligenci, jako je poloha, šířka pásma na vyžádání a záruky latence.

Motivace pro NGSI vychází z potřeby přechodu od monolitické sítě nabízející pouze konektivitu k otevřené platformě umožňující 'síť jako službu'. Předchozí přístupy postrádaly jednotný, bezpečný a škálovatelný mechanismus vystavení. NGSI, postavené na cloud-nativním principu API, tento problém přímo řeší. Umožňuje operátorům mobilních sítí zpeněžit jejich síťová aktiva tím, že je nabízejí jako programovatelné služby prostřednictvím otevřených API. To podporuje ekosystém, ve kterém mohou vývojáři aplikací vytvářet služby, které jsou hluboce integrovány s podkladovou sítí a jí optimalizovány.

NGSI je navíc nezbytné pro naplnění slibu 5G podporovat různorodá vertikální odvětví. Automobilová společnost může například použít NGSI API k vyžádání řezů sítě s ultra-spolehlivou nízkou latencí (URLLC) pro své připojené vozy nebo k získání údajů o poloze vozidel v reálném čase pro řízení dopravy. Bez standardizovaného rámce pro vystavení, jako je NGSI, by každé vertikální odvětví vyžadovalo nákladné, vlastní integrační projekty. NGSI poskytuje společnou, znovupoužitelnou a bezpečnou rozhranovou vrstvu, která činí takové integrace efektivní a škálovatelné, což umožňuje nové zdroje příjmů a inovativní služby.

## Klíčové vlastnosti

- Standardizovaná RESTful API založená na HTTP/2 a JSON pro přístup externích aplikací
- Centralizované vystavení a zabezpečení prostřednictvím Funkce pro vystavení sítě (Network Exposure Function, NEF)
- Podpora jak modelu interakce požadavek-odpověď, tak modelu přihlášení-oznámení
- Vystavení síťových schopností včetně řízení QoS, monitorování událostí a analytiky
- Zabezpečený přístup prostřednictvím mechanismů ověřování, autorizace a řízení provozu
- Soulad se specifikacemi OpenAPI pro vývojářsky vstřícnou definici API

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)
- [AF – Authentication Framework](/mobilnisite/slovnik/af/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs

---

📖 **Anglický originál a plná specifikace:** [NGSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngsi/)
