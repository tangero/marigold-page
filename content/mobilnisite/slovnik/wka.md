---
slug: "wka"
url: "/mobilnisite/slovnik/wka/"
type: "slovnik"
title: "WKA – Well Known Abbreviation"
date: 2026-01-01
abbr: "WKA"
fullName: "Well Known Abbreviation"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/wka/"
summary: "Well Known Abbreviation (WKA, standardizovaná zkratka) je koncept správy v rámci 3GPP pro standardizaci pojmenování a identifikace běžných síťových prvků, funkcí a parametrů. Poskytuje konzistentní sl"
---

WKA je koncept správy v rámci 3GPP pro standardizaci pojmenování a identifikace běžných síťových prvků za účelem zajištění interoperability v systémech pro správu a orchestraci sítě.

## Popis

Well Known Abbreviation (WKA, standardizovaná zkratka) je formalizovaný mechanismus v rámci specifikací 3GPP pro definování a registraci standardizovaných zkratek běžně používaných entit, atributů a parametrů síťového managementu. Je součástí širšího úsilí o umožnění automatizované správy sítě, samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) a Managementu a orchestrace ([MANO](/mobilnisite/slovnik/mano/)) tím, že zajišťuje jednotnou, strojově čitelnou konvenci pojmenování. Systém je dokumentován ve specifikacích jako 28.821 (Management and orchestration; Abbreviations and symbols) a 32.156 (Telecommunication management; Study of Management Aspects of Self-Organizing Networks).

Z architektonického hlediska jsou WKA definovány v rámci řízeného jmenného prostoru a jsou určeny pro použití v rozhraních pro správu, datových modelech a specifikacích informačních služeb. Fungují tak, že poskytují kanonický, krátký identifikátor pro koncept, který by jinak mohl být popsán dlouhými, proměnlivými názvy. Například konkrétní čítač výkonnostních měření nebo konfigurační parametr funkce základnové stanice by měl registrovanou WKA. To umožňuje systémům správy, systémům pro správu sítě ([NMS](/mobilnisite/slovnik/nms/)), správcům prvků ([EM](/mobilnisite/slovnik/em/)) a orchestračním platformám odkazovat na stejnou entitu jednoznačně při výměně dat nebo vydávání příkazů.

Klíčové komponenty zahrnují registr nebo seznam definovaných zkratek, pravidla pro jejich vytváření a použití a jejich integraci do YANG datových modelů, [XML](/mobilnisite/slovnik/xml/) schémat nebo jiných jazyků pro definici rozhraní používaných v managementu 3GPP. Jeho role je klíčová pro umožnění automatizace bez zásahu operátora (zero-touch), protože softwarové algoritmy a politiky musí být schopny spolehlivě identifikovat a manipulovat se specifickými síťovými prostředky a metrikami napříč nasazeními více dodavatelů. Bez WKA by automatizační skripty a rozhraní směrem na sever (northbound APIs) mohly trpět nekonzistencemi, které narušují automatizované procesy.

## K čemu slouží

WKA byla zavedena k řešení problému nekonzistence a nejednoznačnosti terminologie při správě složitých sítí 3GPP od více dodavatelů, zejména s nástupem [SON](/mobilnisite/slovnik/son/) a virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)). Před jejím formalizováním mohly různé specifikace nebo dodavatelé používat mírně odlišné zkratky nebo názvy pro stejný spravovaný objekt, což vedlo k problémům s integrací, chybám v automatizačních skriptech a zvýšeným provozním nákladům. Motivací bylo vytvořit jediný zdroj pravdy pro terminologii managementu.

Historický kontext představuje tlak na autonomní sítě v 3GPP Release 11 a novějších. Jak se sítě stávaly více řízené softwarem a automatizované, potřeba standardizovaných, strojově interpretovatelných identifikátorů se stala prvořadou. WKA řeší omezení ad-hoc pojmenování tím, že poskytuje rámec, který podporuje interoperabilní výměnu dat správy, usnadňuje vývoj znovupoužitelných SON funkcí a tvoří základ datových modelů používaných pro automatizaci s uzavřenou smyčkou a správu sítě založenou na politikách.

## Klíčové vlastnosti

- Standardizovaný registr zkratek pro objekty správy
- Podporuje automatizovanou správu sítě a funkce SON
- Zajišťuje jednoznačnou identifikaci napříč rozhraními více dodavatelů
- Integrováno do datových modelů správy 3GPP (např. YANG)
- Usnadňuje komunikaci mezi stroji (M2M) pro orchestraci
- Snižuje chyby integrace v systémech správy

## Definující specifikace

- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.156** (Rel-20) — UML Modeling for Network Management Systems

---

📖 **Anglický originál a plná specifikace:** [WKA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wka/)
