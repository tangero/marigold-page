---
slug: "clas"
url: "/mobilnisite/slovnik/clas/"
type: "slovnik"
title: "CLAS – Centimeter Level Augmentation Service"
date: 2025-01-01
abbr: "CLAS"
fullName: "Centimeter Level Augmentation Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/clas/"
summary: "CLAS je 3GPP polohovací služba, která poskytuje přesnost na úrovni centimetrů uživatelskému zařízení (UE) kombinací měření GNSS s korekčními daty poskytovanými sítí. Umožňuje vysoce přesné lokalizační"
---

CLAS je 3GPP polohovací služba, která poskytuje přesnost na úrovni centimetrů kombinací měření GNSS s korekčními daty poskytovanými sítí přenášenými přes mobilní síť.

## Popis

Centimeter Level Augmentation Service (CLAS) je standardizovaná polohovací služba definovaná v 3GPP, která poskytuje extrémně přesné informace o poloze uživatelskému zařízení (UE) vylepšením měření globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) pomocí korekčních dat založených na síti. Architektura služby zahrnuje více komponent spolupracujících dohromady: UE s GNSS schopnostmi, infrastrukturu mobilní sítě a augmentační servery, které generují a distribuují korekční informace. CLAS funguje porovnáním GNSS signálů přijatých na referenčních stanicích se známými přesnými pozicemi za účelem výpočtu diferenčních korekcí pro různé zdroje chyb včetně chyb satelitní oběžné dráhy a hodin, ionosférických zpoždění a troposférických efektů.

Technická implementace CLAS následuje model klient-server, kde UE funguje jako klient přijímající korekční data ze síťových serverů. Korekční data jsou přenášena přes mobilní rozhraní pomocí standardizovaných protokolů definovaných ve specifikacích 3GPP. UE zpracovává jak surová GNSS měření, tak přijatá korekční data, aby vypočítala svou polohu s přesností na úrovni centimetrů. Služba podporuje více GNSS konstelací včetně [GPS](/mobilnisite/slovnik/gps/), [GLONASS](/mobilnisite/slovnik/glonass/), Galileo a BeiDou a může poskytovat korekce v různých formátech, jako je State Space Representation ([SSR](/mobilnisite/slovnik/ssr/)) nebo Observation Space Representation ([OSR](/mobilnisite/slovnik/osr/)).

Klíčové komponenty v architektuře CLAS zahrnují Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)), která spravuje polohovací relace, Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), která umožňuje vystavení služby, a dedikované augmentační servery, které generují korekční data. Služba komunikuje s existující 5G polohovací architekturou definovanou v 3GPP Release 16 a integruje se s komponentami NG-RAN a 5GC. CLAS podporuje scénáře v reálném čase i následného zpracování, přičemž provoz v reálném čase vyžaduje přenos korekčních dat s nízkou latencí pro zachování přesnosti.

Přenos korekčních dat využívá efektivní kompresní a kódovací techniky pro minimalizaci využití šířky pásma při zachování přesnosti. Služba zahrnuje mechanismy pro monitorování integrity, které zajišťují, že uživatelé mohou důvěřovat přesnosti poskytovaných polohových informací. CLAS funguje v rámci širšího 3GPP polohovacího rámce a doplňuje další polohovací metody jako [OTDOA](/mobilnisite/slovnik/otdoa/), E-CID a polohování založené na senzorech, aby poskytla komplexní portfolio lokalizačních služeb.

## K čemu slouží

CLAS byl vytvořen, aby reagoval na rostoucí poptávku po vysoce přesných polohovacích službách v různých průmyslových odvětvích včetně automobilového, průmyslové automatizace, zemědělství a rozšířené reality. Tradiční GNSS polohování typicky poskytuje přesnost na úrovni metrů, což je nedostatečné pro aplikace vyžadující přesnost na úrovni centimetrů, jako je navigace autonomních vozidel, precizní zemědělství, řízení stavenišť a provoz dronů. Mezi omezení samostatného GNSS patří atmosférické chyby, chyby satelitních hodin a oběžných drah a vícecestné efekty, které snižují přesnost polohování.

Předchozí přístupy k dosažení vysoce přesného polohování spoléhaly na specializované pozemní augmentační systémy jako sítě RTK (Real-Time Kinematic) nebo satelitní augmentační systémy (SBAS), ty však často vyžadovaly dedikovanou infrastrukturu a postrádaly integraci s mobilními sítěmi. CLAS integruje schopnosti vysoce přesného polohování přímo do ekosystému 3GPP a využívá existující mobilní infrastrukturu k efektivní distribuci korekčních dat. Tato integrace umožňuje širokou dostupnost centimetrového polohování bez nutnosti, aby uživatelé nasazovali specializované vybavení nebo se přihlašovali k samostatným augmentačním službám.

Vytvoření CLAS v 3GPP Release 16 bylo motivováno potřebou podporovat vznikající případy užití v 5G sítích, zejména ty definované vertikálními průmyslovými odvětvími. Standardizací služby v rámci 3GPP je zajištěna interoperabilita mezi různými síťovými operátory a výrobci zařízení, čímž vzniká globální ekosystém pro vysoce přesné polohování. CLAS řeší omezení předchozích metod mobilního polohování, které nedokázaly dosáhnout přesnosti na úrovni centimetrů, a staví tak 5G sítě jako platformu pro kritické lokalizační služby založené na poloze.

## Klíčové vlastnosti

- Přesnost polohování na úrovni centimetrů (1–10 cm)
- Podpora více GNSS konstelací (GPS, GLONASS, Galileo, BeiDou)
- Distribuce síťových diferenčních korekcí
- Integrace s 5G polohovací architekturou
- Režimy provozu v reálném čase a následného zpracování
- Efektivní komprese a kódování korekčních dat

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [CLAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/clas/)
