---
slug: "hateoas"
url: "/mobilnisite/slovnik/hateoas/"
type: "slovnik"
title: "HATEOAS – Hypermedia As The Engine Of Application State"
date: 2025-01-01
abbr: "HATEOAS"
fullName: "Hypermedia As The Engine Of Application State"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hateoas/"
summary: "Omezení architektonického stylu REST, kdy klient komunikuje se síťovou aplikací výhradně prostřednictvím hypermédií (odkazů) dynamicky poskytovaných serverem. V 3GPP řídí návrh rozhraní založených na"
---

HATEOAS je architektonické omezení REST pro rozhraní 3GPP založená na službách, při němž klient komunikuje výhradně prostřednictvím hypermediálních odkazů dynamicky poskytovaných serverem, což umožňuje volné spojení a možnost objevování mezi síťovými funkcemi.

## Popis

Hypermedia As The Engine Of Application State (HATEOAS) je základní princip architektonického stylu Representational State Transfer (REST) uplatňovaný v architektuře 5G Core Network založené na službách (SBA). Stanovuje, že klient (konzument síťové funkce, [NF](/mobilnisite/slovnik/nf/)) by měl komunikovat se serverem (producentem NF) prostřednictvím hypermediálních odkazů a formulářů vložených do přijímaných reprezentací prostředků, namísto spoléhání se na mimopásmové znalosti [API](/mobilnisite/slovnik/api/) nebo natvrdo zakódované URL. V praxi, když konzument NF (např. [AMF](/mobilnisite/slovnik/amf/)) požaduje prostředek od producenta NF (např. [NRF](/mobilnisite/slovnik/nrf/)), odpověď (typicky ve formátu [JSON](/mobilnisite/slovnik/json/)) obsahuje nejen požadovaná data, ale také sadu `_links`.

Tyto `_links` jsou Uniform Resource Identifiers (URI), které označují možné další akce nebo související prostředky, ke kterým se klient může dostat, jako `self`, `update`, `delete` nebo odkazy na další související služby NF. Stav aplikace klienta je řízen navigací podle těchto odkazů. Například po objevení instance funkce Správy relací ([SMF](/mobilnisite/slovnik/smf/)) prostřednictvím NRF by AMF následoval odkaz poskytnutý pro tuto instanci SMF, aby zahájil komunikaci založenou na službách (např. použitím API `nsmf-pdusession`). Server určuje dostupné přechody stavu podle toho, které odkazy zahrne, což umožňuje vývoj API serveru bez porušení klientů, kteří pouze následují odkazy.

V rámci specifikací 3GPP (např. TS 29.501, TS 23.502) je HATEOAS implementováno v rozhraních založených na službách používajících [HTTP](/mobilnisite/slovnik/http/)/2, jako jsou Nnrf (NF Repository Function), Nnef (Network Exposure Function) a Namf (Access and Mobility Management Function). Definice OpenAPI pro tato rozhraní zahrnují schéma pro objekty `Links` a `ProblemDetails`. Tento architektonický přístup odděluje konzumenty služeb NF od konkrétní topologie nasazení a struktury URI, což umožňuje dynamické objevování služeb, vyrovnávání zátěže a pozvolný vývoj sítě. Funkce NRF (Network Repository Function) funguje jako centrální hypermediální engine, poskytující počáteční odkazy, které inicializují interakci mezi ostatními NF.

## K čemu slouží

HATEOAS bylo přijato v 3GPP 5G SBA, aby řešilo kritické problémy škálovatelnosti, flexibility a udržovatelnosti v jádrové síti. Tradiční telekomunikační rozhraní byla založena na statických protokolech typu bod-bod (např. Diameter) s pevnými vztahy. Přidání nové síťové funkce nebo změna verze [API](/mobilnisite/slovnik/api/) vyžadovala koordinované aktualizace na více uzlech, což brzdilo inovace a síťové segmenty (slicing). Účelem aplikace HATEOAS je vytvořit systém s volným spojením, kde se síťové funkce dynamicky objevují a vzájemně komunikují.

Tím se řeší omezení pevně zakódovaných závislostí. Klient NF potřebuje znát pouze způsob interakce s bootstrapovým koncovým bodem (jako je NRF) a způsob interpretace hypermediálních odkazů. Server NF řídí dostupné interakce. To umožňuje bezproblémové zavádění nových služeb, verzování API (poskytnutím různých odkazů pro různé verze) a podporu síťových segmentů (slicing), kde různé segmenty mohou mít různé instance stejného typu NF. Umožňuje to uplatňovat principy cloud-nativní architektury v 5G Core, jako je automatické škálování, samoopravování a průběžné nasazování, protože nové instance se mohou zaregistrovat u NRF a okamžitě se stanou objevitelné prostřednictvím hypermediálních odkazů, které NRF poskytuje, aniž by vyžadovaly rekonfiguraci všech potenciálních konzumentů NF.

## Klíčové vlastnosti

- Interakce klienta jsou řízeny hypermediálními odkazy poskytovanými v odpovědích serveru
- Odděluje klienta a server, což umožňuje nezávislý vývoj struktury URI a verzí API
- Klíčové pro dynamické objevování služeb zprostředkované funkcí NRF (Network Repository Function)
- Implementováno pomocí objektů `_links` v reprezentacích JSON přes HTTP/2
- Umožňuje podporu síťových segmentů (slicing) a cloud-nativních modelů nasazení
- Snižuje potřebu mimopásmové koordinace a konfigurace mezi síťovými funkcemi

## Související pojmy

- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [HATEOAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hateoas/)
