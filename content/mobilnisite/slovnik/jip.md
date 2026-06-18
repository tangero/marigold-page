---
slug: "jip"
url: "/mobilnisite/slovnik/jip/"
type: "slovnik"
title: "JIP – Jurisdiction Information Parameter"
date: 2025-01-01
abbr: "JIP"
fullName: "Jurisdiction Information Parameter"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/jip/"
summary: "Parametr informace o jurisdikci (Jurisdiction Information Parameter) je datový prvek používaný v účtovacích systémech 3GPP k označení geografické nebo regulační jurisdikce, kde došlo k události teleko"
---

JIP je datový prvek používaný v účtovacích systémech 3GPP k označení geografické nebo regulační jurisdikce, kde došlo k servisní události, za účelem správného účtování, tarifů, daní a poplatků.

## Popis

Parametr informace o jurisdikci (JIP) je pole v záznamech účtovacích dat ([CDR](/mobilnisite/slovnik/cdr/)) a dalších účtovacích zprávách v síti 3GPP. Patří do domény Telekomunikačního managementu, konkrétně do Fakturační domény v rámci Systému podpory provozu ([OSS](/mobilnisite/slovnik/oss/)). JIP nese kódovanou hodnotu, která jednoznačně identifikuje právní, regulační nebo tarifní jurisdikci použitelnou pro událost využití služby, jako je hovor, [SMS](/mobilnisite/slovnik/sms/) nebo datová relace. Tento parametr typicky vkládá síťový uzel generující účtovací událost (např. mobilní ústředna ([MSC](/mobilnisite/slovnik/msc/)) pro hovory v přepojování okruhů nebo Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN)/Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) pro paketová data).

JIP funguje tak, že je naplněn na základě topologie a konfigurace sítě. Síťový operátor definuje mapování mezi konkrétními síťovými prvky, ID buněk nebo geografickými oblastmi (jako jsou Location Area Codes nebo Routing Area Codes) a standardizovanými kódy jurisdikcí. Například při sestavování hovoru MSC určí obsluhující buňku pro účastníka. Na základě předkonfigurovaných dat přiřadí hodnotu JIP odpovídající městu, státu nebo regionu země, kde se tato buňka nachází. Tento JIP je pak zahrnut do počátečních detailních záznamů o hovoru. Později, během procesu generování CDR (např. při uvolnění hovoru), je JIP zapsán do CDR. CDR je pak přenesen do fakturačního systému.

Ve fakturačním systému je JIP klíčovým vstupem pro ratingový engine. Ratingový engine použije JIP spolu s dalšími parametry, jako je volané číslo, denní doba a tarifní plán účastníka, k výběru správné tarifní tabulky. Různé jurisdikce často mají různé sazby za minutu, daňové struktury (např. daň z přidané hodnoty, poplatky za univerzální službu) a regulační příplatky. Přesným označením každé události využití služby její jurisdikcí umožňuje JIP vytváření přesných, právně konformních faktur. Také podporuje složité roamingové scénáře, kdy musí být jurisdikce navštívené sítě sdělena domovské síti pro účely vypořádání. Jeho role je tedy kritická pro monetizaci, dodržování regulatorních požadavků a finanční vypořádání mezi operátory.

## K čemu slouží

JIP byl vytvořen k řešení složitých požadavků na účtování vyplývajících z vícejurisdikční telekomunikační regulace a konkurenčního tarifování. V počátcích mobilní telefonie bylo účtování často zjednodušeno s jednotnými celostátními sazbami. Jak se sítě rozšiřovaly, rostla konkurence a regulace se vyvíjela, operátoři potřebovali zavést podrobné, na lokalitě založené ceny (např. místní vs. dálkové hovory, různé sazby pro různé státy/provincie) a přesně uplatňovat daně a poplatky specifické pro danou lokalitu.

Bez standardizovaného parametru, jako je JIP, museli operátoři vkládat logiku jurisdikce ad-hoc způsobem do síťových prvků nebo provádět složité dodatečné zpracování [CDR](/mobilnisite/slovnik/cdr/) na základě jiných polí, jako jsou volané předvolby nebo ID buněk, což bylo náchylné k chybám a nepružné. JIP poskytuje čistou, standardizovanou abstrakci. Odděluje úkol sítě identifikovat *kde* k události došlo od úkolu fakturačního systému rozhodnout *kolik za ni účtovat*. Toto oddělení zájmů zjednodušuje konfiguraci sítě, činí fakturační pravidla transparentnějšími a udržovatelnějšími a zajišťuje konzistenci napříč různými službami (hlas, data, [SMS](/mobilnisite/slovnik/sms/)). Jeho zavedení bylo motivováno potřebou automatizovaných, spolehlivých a auditovatelných účtovacích procesů, které by dokázaly škálovat s rostoucí složitostí sítě a splnit přísné regulatorní požadavky na přesnost účtování napříč různými právními územími.

## Klíčové vlastnosti

- Standardizované datové pole v účtovacích záznamech 3GPP (např. CDR, EDR) pro označení příslušné jurisdikce
- Hodnota je typicky kód mapovaný na konkrétní geografickou nebo regulační oblast (např. země, stát, město, tarifní zóna)
- Naplněno síťovým prvkem (MSC, SGSN, GGSN, PGW) na základě lokality servisní události
- Kritický vstup pro ratingový engine fakturačního systému k výběru správných tarifů a aplikaci daní/poplatků
- Umožňuje dodržování regionálních telekomunikačních regulací a daňových zákonů
- Usnadňuje přesné účtování a vypořádání mezi operátory v roamingových scénářích

## Definující specifikace

- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [JIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/jip/)
