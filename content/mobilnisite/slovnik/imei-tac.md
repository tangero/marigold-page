---
slug: "imei-tac"
url: "/mobilnisite/slovnik/imei-tac/"
type: "slovnik"
title: "IMEI-TAC – Type Allocation Code part of an IMEI"
date: 2026-01-01
abbr: "IMEI-TAC"
fullName: "Type Allocation Code part of an IMEI"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/imei-tac/"
summary: "Úvodní osmimístný segment IMEI nebo IMEI-SV, který identifikuje model a výrobce zařízení. Jedná se o globálně jednoznačný kód přidělený k šarži modelu zařízení, používaný pro rozpoznání typu zařízení"
---

IMEI-TAC je úvodní osmimístný segment IMEI, který jednoznačně identifikuje model a výrobce zařízení pro globální rozpoznání typu a regulační schválení.

## Popis

Kód přidělení typu (Type Allocation Code, TAC) je základní součástí jak [IMEI](/mobilnisite/slovnik/imei/), tak [IMEI-SV](/mobilnisite/slovnik/imei-sv/). Tvoří prvních osm číslic těchto identifikátorů. TAC sám o sobě není náhodné číslo; jde o kód oficiálně přidělený centrálním orgánem (historicky BABT, nyní IMEI Allocation Board vedený asociací [GSMA](/mobilnisite/slovnik/gsma/)) výrobci zařízení pro konkrétní model nebo řadu modelů. TAC tedy jednoznačně identifikuje značku, model a často i konkrétní variantu zařízení (např. různé barvy nebo regionální verze).

Provozně je TAC nejčastěji používanou částí IMEI pro vysokou úroveň identifikace zařízení. Když síť přijme celé IMEI, může okamžitě extrahovat TAC a určit typ zařízení bez potřeby jedinečného sériového čísla. Toho se využívá v mnoha síťových funkcích. Například algoritmy rádiového přístupového sítě mohou aplikovat specifické optimalizační parametry na základě modelu zařízení identifikovaného pomocí TAC. Funkce politik v jádru sítě mohou použít TAC k aplikaci specifických QoS politik nebo omezení pro dané zařízení. TAC je také primárním klíčem používaným v databázích zařízení a analytických platformách pro kategorizaci populace zařízení.

Z regulačního a standardizačního hlediska je TAC klíčový pro schvalování typu zařízení. Regulační orgány používají TAC ke sledování, které modely zařízení byly certifikovány pro provoz v jejich jurisdikcích. TAC je také nedílnou součástí ekosystému blokování zařízení založeného na IMEI. Zatímco pro zablokování konkrétního odcizeného zařízení je potřeba celé IMEI, TAC lze použít pro širší akce. Například pokud by byl u konkrétního modelu zařízení zjištěn kritický, neopravitelný rádiový nedostatek, mohli by regulátoři nebo operátoři potenciálně zablokovat přístup všech zařízení s tímto TAC do sítě, což by byl proces využívající možnosti registru identit zařízení (Equipment Identity Register, [EIR](/mobilnisite/slovnik/eir/)). Struktura TAC zajišťuje globální jednoznačnost a zabraňuje kolizím mezi kódy zařízení různých výrobců.

## K čemu slouží

TAC byl zaveden za účelem poskytnutí standardizované hierarchické struktury v rámci [IMEI](/mobilnisite/slovnik/imei/), která umožňuje efektivní kategorizaci a identifikaci modelů zařízení ve velkém měřítku. Před jeho formální definicí vyžadovalo rozpoznání modelu zařízení z jeho sériového čísla proprietární databáze výrobců, což bylo pro síťové operátory a regulátory neefektivní. TAC tento problém řeší tím, že informace o modelu zakóduje přímo do struktury identifikátoru, což umožňuje okamžité rozpoznání.

Jeho vytvoření bylo motivováno potřebami regulačních procesů schvalování typu, analytiky trhu zařízení a optimalizace sítě. Regulátoři potřebovali spolehlivý kód pro asociaci s certifikační dokumentací zařízení. Síťoví operátoři potřebovali rychle identifikovat schopnosti zařízení (např. podporovaná frekvenční pásma, maximální přenosové rychlosti), aby optimalizovali přidělování rádiových zdrojů a řešili problémy specifické pro dané zařízení. TAC, zavedený jako základní část IMEI a později upřesněný, tyto potřeby naplnil tím, že poskytl globálně jednoznačné, operátorem čitelné „číslo modelu“, které každé zařízení konzistentně hlásí. To umožňuje automatizovaným systémům aplikovat konfigurace a politiky specifické pro model v celé mobilní síti.

## Klíčové vlastnosti

- Prvních 8 číslic IMEI a IMEI-SV
- Globálně jednoznačný kód přidělený na model/šarži zařízení
- Identifikuje výrobce zařízení a konkrétní model
- Klíčový pro schválení typu zařízení a regulační shodu
- Umožňuje optimalizaci sítě a řízení politik na základě modelu zařízení
- Používá se jako primární filtr v analytice zařízení a sledování populace

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [IMEI-SV – International Mobile Equipment Identity Software Version](/mobilnisite/slovnik/imei-sv/)
- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)

## Definující specifikace

- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.675** (Rel-19) — UE Radio Capability Provisioning Service
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration

---

📖 **Anglický originál a plná specifikace:** [IMEI-TAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/imei-tac/)
