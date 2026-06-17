---
slug: "ima"
url: "/mobilnisite/slovnik/ima/"
type: "slovnik"
title: "IMA – Intersection Movement Assist"
date: 2025-01-01
abbr: "IMA"
fullName: "Intersection Movement Assist"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ima/"
summary: "Intersection Movement Assist (IMA) je bezpečnostní služba V2X (Vehicle-to-Everything) navržená k varování řidičů před možnými kolizemi na křižovatkách. Využívá přímou komunikaci mezi vozidly (V2V) a/n"
---

IMA je bezpečnostní služba V2X, která varuje řidiče před možnými kolizemi na křižovatkách využitím komunikace V2V/V2I k výměně kinematických dat v reálném čase a výpočtu rizik kolize.

## Popis

Intersection Movement Assist je standardizovaná služba kooperativního inteligentního dopravního systému (C-ITS) v ekosystému 3GPP, která primárně využívá komunikaci LTE-V2X (rozhraní PC5) a později postranní spoj NR-V2X. Služba funguje tak, že vozidla periodicky vysílají základní bezpečnostní zprávy ([BSM](/mobilnisite/slovnik/bsm/)), známé v Evropě také jako zprávy kooperativního povědomí ([CAM](/mobilnisite/slovnik/cam/)), které obsahují dynamické stavové informace vozidla, jako je zeměpisná šířka a délka, rychlost, směr jízdy, zrychlení a rozměry vozidla.

Když vozidlo vybavené IMA přijíždí ke křižovatce, jeho palubní jednotka (OBU) použije přijaté BSM od jiných blízkých vozidel k provedení lokálního vyhodnocení rizika. Pokročilé algoritmy tato data zpracují, aby předpověděly budoucí trajektorie všech relevantních vozidel v dosahu komunikace. Hlavní funkcí je identifikovat potenciální konflikty, kdy by se předpovězené dráhy dvou nebo více vozidel protnuly v kritickém časovém okně, což signalizuje vysokou pravděpodobnost kolize v křižovatce, například při projetí vozidla na červenou nebo nedání přednosti.

Při detekci bezprostředního ohrožení aplikace IMA spustí varování řidiče. Toto varování může být vizuální (např. ikona na displeji), zvukové (např. pípnutí) nebo haptické (např. vibrace volantu). Služba je navržena tak, aby fungovala i v podmínkách bez přímé viditelnosti, kdy je řidičův výhled zakryt budovami nebo jinými vozidly, což je klíčová výhoda oproti palubním senzorům, jako jsou kamery. Architektura zahrnuje aplikační vrstvu V2X, komunikační zásobník V2X (včetně přístupové vrstvy a síťových/transportních vrstev pro PC5) a palubní rozhraní člověk-stroj ([HMI](/mobilnisite/slovnik/hmi/)). Specifikace jako TS 23.795 definují požadavky na službu a architekturu na vysoké úrovni, zatímco specifikace nižších vrstev (např. TS 25.411) mohou pokrývat související komunikační aspekty.

## K čemu slouží

Intersection Movement Assist byl vytvořen k řešení významného a přetrvávajícího problému bezpečnosti silničního provozu: kolizí souvisejících s křižovatkami. Podle studií bezpečnosti provozu dochází k velkému procentu závažných nehod ve městech právě na křižovatkách z důvodů, jako je chyba řidiče, nepozornost, omezený výhled a porušování světelné signalizace. Tradiční bezpečnostní systémy vozidel (airbagy, deformační zóny) jsou reaktivní a i pokročilé asistenční systémy řidiče (ADAS), jako je varování před kolizí, spoléhají na senzory s přímou viditelností, které jsou na křižovatkách s vizuálními překážkami neúčinné.

Účelem IMA je poskytnout proaktivní, kooperativní bezpečnostní síť. Využívá schopnost komunikace V2X „vidět skrz“ k získávání informací o vozidlech, která řidič fyzicky nevidí. Tím řeší kritické omezení palubních senzorů. Motivací pro standardizaci IMA v rámci 3GPP bylo zajistit interoperabilitu mezi vozidly různých výrobců a využít globálně harmonizovanou technologii cellular-V2X, která nabízí výhody v dosahu, spolehlivosti a výkonu bez přímé viditelnosti ve srovnání se staršími systémy založenými na [IEEE](/mobilnisite/slovnik/ieee/) 802.11p.

Poskytnutím včasného, situačně uvědomělého varování si IMA klade za cíl dát řidičům několik klíčových sekund navíc k reakci a vyhnutí se kolizi, čímž snižuje počty úmrtí, zranění a hmotných škod. Jeho vývoj byl hnán konsorcii automobilového průmyslu a regulačními snahami o zvýšení bezpečnosti vozidel, což vedlo k jeho zařazení do specifikací 3GPP, aby byl v souladu s širším vývojem mobilních sítí směrem k podpoře kritických případů užití IoT a automobilového průmyslu.

## Klíčové vlastnosti

- Využívá periodické vysílání kinematických dat vozidla (BSM/CAM) prostřednictvím postranního spoje PC5
- Provádí lokální, distribuovaný výpočet hrozby v palubní jednotce každého vozidla
- Poskytuje varování před kolizemi v křižovatkách
- Účinně funguje ve scénářích bez přímé viditelnosti a s omezeným výhledem
- Využívá standardizované komunikační protokoly V2X (LTE-V2X, NR-V2X)
- Navržen pro nízkou latenci, aby umožnil včasná varování řidiče

## Související pojmy

- [BSM – Basic Safety Message](/mobilnisite/slovnik/bsm/)
- [CAM – Cooperative Awareness Message](/mobilnisite/slovnik/cam/)
- [ITS – Intelligent Transport Systems](/mobilnisite/slovnik/its/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification

---

📖 **Anglický originál a plná specifikace:** [IMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ima/)
