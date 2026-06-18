---
slug: "soi"
url: "/mobilnisite/slovnik/soi/"
type: "slovnik"
title: "SOI – Start Of Interception"
date: 2025-01-01
abbr: "SOI"
fullName: "Start Of Interception"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/soi/"
summary: "SOI je standardizovaný referenční bod v sítích 3GPP, který označuje začátek toku dat pro zákonný odposlech. Jedná se o klíčovou architektonickou komponentu, která umožňuje síťovým operátorům plnit zák"
---

SOI je standardizovaný referenční bod v síti 3GPP, který označuje začátek toku dat pro zákonné odposlechy pro oprávněné orgány.

## Popis

Start Of Interception (SOI, začátek odposlechu) je základní architektonický koncept definovaný ve specifikacích 3GPP pro zákonný odposlech ([LI](/mobilnisite/slovnik/li/)). Představuje přesný logický bod v rámci síťového uzlu nebo funkce, kde začíná duplikace informací souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)) pro konkrétní cíl. SOI není fyzické rozhraní, ale standardizované referenční umístění, které zajišťuje konzistentní implementaci napříč různými výrobci a síťovými elementy. Jeho definice je klíčová pro vymezení odpovědností a zajištění, že odposlechnutá data jsou úplná, přesná a právně přípustná.

Architektonicky se SOI nachází v rámci Intercepting Control Element ([ICE](/mobilnisite/slovnik/ice/)), což je síťový uzel (např. [MME](/mobilnisite/slovnik/mme/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/), [AMF](/mobilnisite/slovnik/amf/)), který provádí samotný odposlech. Když je pro cíl aktivováno zákonné povolení, ICE identifikuje příslušné komunikační relace nebo události spojené s tímto cílem. SOI je instanciační bod, kde ICE začíná kopírovat určená IRI (metadata jako záznamy hovorů, poloha) a CC (hlasový, datový, obsah zpráv) ze svých interních zpracovacích cest. Tato zkopírovaná data jsou následně formátována a doručována přes Handover Interface (HI) do Law Enforcement Monitoring Facility (LEMF).

Úlohou SOI je poskytnout jasnou a jednoznačnou technickou definici toho, kde odposlech začíná. To je zásadní pro síťové operátory, aby mohli prokázat soulad s právními rámci, protože definuje rozsah sběru dat. Zajišťuje, že odposlech je aplikován správně až po autorizaci a že všechna požadovaná data od bodu odposlechu dále jsou zachycena bez opomenutí. Specifikace popisující SOI, jako je TS 33.128, poskytují rámec pro jeho implementaci v rámci různých funkcí 5G sítě, včetně User Plane Function (UPF) pro odposlech obsahu a Access and Mobility Management Function (AMF) pro informace související s odposlechem.

## K čemu slouží

SOI byl vytvořen k řešení potřeby standardizovaného, spolehlivého a právně obhajitelného mechanismu pro zahájení zákonného odposlechu v mobilních sítích založených na 3GPP. Jelikož se telekomunikace staly klíčovou infrastrukturou, právní rámce po celém světě nařídily operátorům poskytovat možnosti zákonného odposlechu na podporu trestního vyšetřování a národní bezpečnosti. Bez standardizované definice toho, kde odposlech začíná, by se implementace mohly lišit, což by vedlo k neúplnému zachycení dat, problémům s ověřováním souladu a potenciálním právním sporům o přípustnost důkazů.

Historicky byly odposlechové mechanismy často proprietární a integrované ad-hoc způsobem. Standardizace SOI v rámci 3GPP, zvláště zdůrazněná od Release 16 se systémem 5G, poskytuje společný referenční bod, kterého se musí držet všichni výrobci síťového zařízení a operátoři. Tím se řeší problém interoperability a zajišťuje, že orgány činné v trestním řízení dostávají konzistentní formát a úplný datový tok bez ohledu na podkladového síťového výrobce. Řeší to technický a právní požadavek na přesné definování okamžiku a místa duplikace dat, aby byla zachována integrita procesu odposlechu od začátku do konce.

## Klíčové vlastnosti

- Standardizovaný referenční bod pro zahájení duplikace dat v zákonném odposlechu
- Definován v rámci Intercepting Control Element (ICE) síťové funkce
- Použitelný pro informace související s odposlechem (IRI) i obsah komunikace (CC)
- Zajišťuje úplné zachycení komunikací cíle od definovaného počátečního bodu
- Kritický pro právní soulad a přípustnost důkazů
- Poskytuje jasné vymezení pro implementaci a testování

## Definující specifikace

- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [SOI na 3GPP Explorer](https://3gpp-explorer.com/glossary/soi/)
