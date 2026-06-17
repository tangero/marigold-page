---
slug: "cspdn"
url: "/mobilnisite/slovnik/cspdn/"
type: "slovnik"
title: "CSPDN – Circuit Switched Public Data Network"
date: 2025-01-01
abbr: "CSPDN"
fullName: "Circuit Switched Public Data Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cspdn/"
summary: "Veřejná datová síť využívající technologii přepojování okruhů pro vytváření vyhrazených spojovacích cest mezi koncovými body. Poskytuje spolehlivý přenos dat s konstantní přenosovou rychlostí pro apli"
---

CSPDN (veřejná datová síť s přepojováním okruhů) je veřejná datová síť, která využívá technologii přepojování okruhů k vytvoření vyhrazených spojovacích cest a poskytuje spolehlivý přenos dat s konstantní přenosovou rychlostí pro aplikace vyžadující garantovanou šířku pásma a nízkou latenci.

## Popis

CSPDN (veřejná datová síť s přepojováním okruhů) je telekomunikační síťová architektura, která pro dobu trvání datové relace vytváří mezi komunikujícími koncovými body vyhrazené fyzické nebo logické okruhy. Na rozdíl od sítí s přepojováním paketů, kde jsou data rozdělena na pakety putující nezávisle, CSPDN vytváří nepřetržité koncové spojení s rezervovanou šířkou pásma, což zajišťuje konzistentní přenosové charakteristiky po celou dobu spojení. Tato architektura funguje podobně jako tradiční telefonní sítě, ale je optimalizována pro přenos dat namísto hlasu, využívá digitální signalizaci a datově specifické protokoly pro správu spojení a přenos informací mezi datovými koncovými zařízeními.

Technické fungování CSPDN zahrnuje tři odlišné fáze: navázání spojení, přenos dat a uvolnění spojení. Během navazování signalizační protokoly vyjednají a rezervují síťové prostředky podél celé cesty mezi zdrojem a cílem, čímž vytvoří vyhrazený okruh přes přepojovací uzly. Tento okruh zůstává výhradně alokován pro danou relaci, což zabraňuje souběhu s jinými uživateli. Přenos dat probíhá konstantní přenosovou rychlostí s minimální variací zpoždění, což jej činí vhodným pro časově citlivé aplikace. Síť využívá signalizační systémy asociované s kanálem nebo společný signalizační kanál pro správu sestavení, dohled a uvolnění hovoru, přičemž protokoly jako X.21 nebo X.25 poskytují rozhraní mezi datovým koncovým zařízením a sítí.

Mezi klíčové architektonické komponenty patří ústředny s přepojováním okruhů (podobné telefonním ústřednám, ale optimalizované pro data), přenosové systémy (digitální přenosové cesty jako E1/T1) a adaptéry datových koncových zařízení, které propojují uživatelské zařízení se sítí. Síť používá časový multiplex (TDM) pro sdílení fyzického média mezi více okruhy, přičemž každému okruhu jsou přiděleny specifické časové sloty v opakujících se rámcích. Řídicí signalizace může být buď v pásmu (používající stejný kanál jako data), nebo mimo pásmo (používající samostatné signalizační kanály), přičemž moderní implementace upřednostňují společný signalizační kanál pro vyšší efektivitu. Řízení chyb typicky zajišťuje vrstva spojení pomocí protokolů jako [LAPB](/mobilnisite/slovnik/lapb/), zatímco síťová adresace se řídí standardizovanými číslovacími plány pro směrování hovorů hierarchií přepojování.

Role CSPDN ve vývoji telekomunikací byla významná, neboť poskytla první rozšířenou infrastrukturu pro digitální datové služby předtím, než se přepojování paketů stalo dominantním. Umožnila spolehlivou obchodní datovou komunikaci, raný přístup k internetu a specializované aplikace vyžadující garantovanou kvalitu služby. I když byla v podstatě vytlačena technologiemi s přepojováním paketů ve veřejných sítích, paradigma přepojování okruhů stále ovlivňuje určité specializované aplikace a porozumění jejím principům zůstává klíčové pro pochopení historického vývoje a základních kompromisů v síťovém designu mezi garantovanou službou a efektivitou statistického multiplexování.

## K čemu slouží

CSPDN byla vytvořena za účelem poskytování spolehlivých a předvídatelných služeb datové komunikace přes veřejnou telekomunikační infrastrukturu v době, kdy se datové sítě vyvíjely z proprietárních systémů ke standardizované veřejné nabídce. Řešila problém, jak rozšířít prověřenou spolehlivost a kvalitativní záruky hlasových sítí s přepojováním okruhů na rostoucí poptávku po přenosu dat, a nabídla tak firmám a institucím spravovanou alternativu k raným paketovým sítím, které trpěly proměnlivým výkonem a omezenými kvalitativními zárukami. Tato technologie reagovala na potřeby aplikací, jako je zpracování transakcí, vzdálený přístup k terminálům a raná telemetrie, které vyžadovaly konzistentní latenci a garantovanou dostupnost šířky pásma.

Historicky se CSPDN objevila v 70. a 80. letech 20. století, kdy telekomunikační operátoři hledali způsob, jak využít svou stávající infrastrukturu s přepojováním okruhů (navrženou pro hlas) k nabízení datových služeb, čímž vytvořili přirozenou vývojovou cestu od analogových modemů přes hlasové okruhy k vyhrazeným digitálním datovým okruhům. Tento přístup umožnil operátorům využít svých značných investic do přepojovacích a přenosových systémů a zároveň uspokojit rostoucí korporátní poptávku po datové konektivitě. Před CSPDN datová komunikace typicky spoléhala na pronajaté linky (trvalé okruhy) nebo modemová spojení v hlasovém pásmu, které byly buď nákladné pro nepřetržité používání, nebo nabízely omezenou rychlost a spolehlivost pro datové aplikace.

Vznik CSPDN byl motivován několika konkrétními omezeními předchozích přístupů: pronajaté linky byly cenově neúnosné pro občasné použití, modemová spojení přes hlasové sítě poskytovala nekonzistentní kvalitu a vyžadovala dlouhou dobu sestavování, a rané paketové sítě postrádaly kvalitativní záruky potřebné pro kritické aplikace. CSPDN nabídla kompromis – poskytovala sestavování okruhů na vyžádání s předvídatelnými výkonnostními charakteristikami, lepší využití síťových prostředků než trvalé okruhy a standardizovaná rozhraní umožňující interoperabilitu mezi různými dodavateli. To učinilo digitální datové služby dostupnějšími pro širší okruh uživatelů a aplikací a překlenulo mezeru mezi vyhrazenými privátními sítěmi a veřejnými datovými službami typu 'best-effort'.

## Klíčové vlastnosti

- Vytváření vyhrazených koncových okruhů pro garantované přidělení šířky pásma
- Přenos s konstantní přenosovou rychlostí a předvídatelnými charakteristikami latence
- Spojově orientovaný provoz s explicitními fázemi sestavení a uvolnění
- Digitální přenos využívající techniky časového multiplexu (TDM)
- Standardizovaná uživatelsko-síťová rozhraní (doporučení řady X)
- Garance kvality služby prostřednictvím rezervace prostředků během sestavování hovoru

## Související pojmy

- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CSPDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cspdn/)
