---
slug: "sdars"
url: "/mobilnisite/slovnik/sdars/"
type: "slovnik"
title: "SDARS – Satellite Digital Audio Radio System"
date: 2025-01-01
abbr: "SDARS"
fullName: "Satellite Digital Audio Radio System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdars/"
summary: "SDARS označuje satelitní systémy digitálního rozhlasového vysílání, jako je SiriusXM, které poskytují širokoplošné pokrytí pro multimediální obsah. 3GPP studovala jejich integraci s pozemními mobilním"
---

SDARS je satelitní systém digitálního rozhlasového vysílání, který 3GPP studuje pro integraci s mobilními sítěmi za účelem umožnění hybridních služeb typu broadcast-broadband.

## Popis

Satellite Digital Audio Radio System (SDARS) je termín používaný v rámci 3GPP pro označení existujících komerčních satelitních vysílacích systémů, jako je SiriusXM v Severní Americe, které doručují digitální audio a přidružené datové služby přímo do mobilních a pevných přijímačů v rozsáhlé geografické oblasti. V kontextu 3GPP není SDARS technologií definovanou 3GPP, ale externím systémem, který byl studován pro potenciální integraci a spolupráci s pozemními mobilními sítěmi 3GPP. Technický důraz je kladen na vytvoření hybridní síťové architektury, kde lze vysílací obsah doručovaný přes satelit doplnit nebo spravovat pomocí možností mobilní sítě.

Z architektonického pohledu se síť SDARS skládá z geostacionárních ([GEO](/mobilnisite/slovnik/geo/)) nebo satelitů na vysoce eliptické dráze ([HEO](/mobilnisite/slovnik/heo/)), pozemních sítí opakovačů pro zajištění pokrytí v městských kaňonech a uživatelských přijímačů. Studie 3GPP, zejména v kontextu evolved Multimedia Broadcast Multicast Service (eMBMS) a později 5G broadcastu, zkoumají, jak by mohla jádrová síť (např. Broadcast/Multicast Service Center – [BM-SC](/mobilnisite/slovnik/bm-sc/)) interagovat s poskytovatelem obsahu SDARS. To by mohlo zahrnovat využití mobilní sítě pro oznamování služeb, správu předplatného, distribuci klíčů pro ochranu služeb nebo pro doručování doplňkového obsahu na vyžádání nebo interaktivního obsahu („clipcasting“), který obohacuje lineární satelitní vysílací proud.

Z provozního hlediska zkoumané modely integrace zahrnují kooperativní a komplementární přístupy. V kooperativním modelu může být stejný obsah doručován současně jak přes satelitní spoj SDARS, tak přes pozemní mobilní spoj pro multicast/broadcast (např. přes LTE eMBMS nebo 5G NR multicast), přičemž zařízení plynule vybere nejlepší dostupný signál. V komplementárním modelu primární audio proud přichází přes satelit, zatímco mobilní spoj poskytuje zpětný kanál pro interaktivitu, metadata, aktualizace softwaru nebo cílené vkládání reklam. Práce 3GPP zahrnuje definování potřebných rozhraní, protokolů a adaptací na vrstvě služeb, aby bylo možné takový hybridní provoz umožnit, a zajištění kontinuity služeb a jednotného uživatelského zážitku.

## K čemu slouží

Studium SDARS v rámci 3GPP bylo motivováno trendem konvergence v odvětví a snahou najít efektivní způsoby doručování kvalitního vysílacího a multicastového obsahu, zejména do vozidel. Tradiční systémy SDARS nabízejí vynikající širokoplošné pokrytí a pokrytí dálnic, ale mají omezenou šířku pásma a jsou ze své podstaty jednosměrné vysílací systémy bez inherentní zpětné cesty nebo možnosti personalizace. Mobilní sítě nabízejí všudypřítomnou obousměrnou konektivitu, ale mohou být neefektivní a nákladné pro doručování oblíbeného živého obsahu masivním současným divákům, jako je tomu u unicastového streamování.

Prozkoumáním integrace se 3GPP snaží vyřešit několik problémů. Snaží se zvýšit efektivitu vysílacích služeb potenciálním přesunem oblíbeného lineárního obsahu z unicastového mobilního provozu na vyhrazenou vysílací vrstvu (satelitní nebo pozemní broadcast), čímž uvolní mobilní spektrum pro interaktivní služby. Také si klade za cíl obohatit uživatelský zážitek u stávajících služeb satelitního rádia přidáním interaktivity, personalizace a doplňkového vizuálního obsahu doručovaného přes mobilní spoj. Tím se řeší omezení čistě vysílacích systémů. Tato práce, zvláště aktivní v éře LTE Advanced Pro a 5G, je hnána případy použití v automobilové infotainmentové oblasti, kde je spolehlivá celokontinentální audio služba kombinovaná s lokálními interaktivními funkcemi velmi žádoucí.

## Klíčové vlastnosti

- Širokoplošné satelitní vysílací pokrytí
- Integrace s jádrovou sítí 3GPP (např. BM-SC)
- Podpora hybridních modelů služeb typu broadcast-broadband
- Oznamování služeb a správa předplatného přes mobilní síť
- Doručování komplementárního obsahu (Clipcasting)
- Studijní položka pro automobilové a multimediální služby

## Související pojmy

- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 36.846** (Rel-12) — LTE WCS Band Specification
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR

---

📖 **Anglický originál a plná specifikace:** [SDARS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdars/)
