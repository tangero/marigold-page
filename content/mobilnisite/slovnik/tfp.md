---
slug: "tfp"
url: "/mobilnisite/slovnik/tfp/"
type: "slovnik"
title: "TFP – Transfer Prohibited"
date: 2025-01-01
abbr: "TFP"
fullName: "Transfer Prohibited"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tfp/"
summary: "TFP je signalizační zpráva používaná v jádrové síti založené na SS7/SIGTRAN, konkrétně ve vrstvě SCCP. Označuje, že signalizační bod nemůže přeposílat zprávy pro konkrétní cíl, spouští přeusměrování a"
---

TFP je signalizační zpráva na vrstvě SCCP, která označuje, že signalizační bod nemůže přeposílat zprávy ke konkrétnímu cíli, čímž spouští přeusměrování za účelem zachování spolehlivosti sítě a řízení zahlcení.

## Popis

Transfer Prohibited (TFP) je základní zpráva v rámci Signalizační spojové řídicí části ([SCCP](/mobilnisite/slovnik/sccp/)) systému [SS7](/mobilnisite/slovnik/ss7/) (Signalizační systém č. 7) a jeho IP evoluce SIGTRAN. Jedná se o zprávu správy sítě používanou mezi signalizačními přenosovými body ([STP](/mobilnisite/slovnik/stp/)) a dalšími signalizačními body. Když signalizační bod (např. STP) zjistí, že již nemůže směrovat zprávy ke konkrétnímu cílovému kódu bodu ([DPC](/mobilnisite/slovnik/dpc/)), odešle zprávu TFP svým sousedním signalizačním bodům. Toto prohlášení znamená, že výchozí bod je 'zakázán' přenášet zprávy k tomuto konkrétnímu DPC. Přijetí TFP způsobí, že přijímající signalizační bod aktualizuje své směrovací tabulky a označí cestu přes odesílatele jako nedostupnou. Musí poté hledat alternativní cesty (pokud jsou dostupné), aby dosáhl zakázaného cíle. Zpráva TFP je klíčovou součástí správy sítě SS7, která umožňuje dynamické přeusměrování v případě poruch nebo zahlcení. Proces zahrnuje neustálé sledování stavu signalizačních cest. Když se cesta opět stane dostupnou, odešle se zpráva Transfer Allowed ([TFA](/mobilnisite/slovnik/tfa/)), aby zákaz zrušila. Tento mechanismus zajišťuje, že signalizační síť, která přenáší klíčové informace pro řízení hovorů a správu mobility, zůstává robustní a dokáže se přizpůsobit poruchám, čímž udržuje kontinuitu služeb pro hlasové a datové relace.

## K čemu slouží

Zpráva TFP byla vytvořena, aby řešila kritickou potřebu spolehlivosti a odolnosti proti poruchám v globálních telekomunikačních signalizačních sítích. V architektuře [SS7](/mobilnisite/slovnik/ss7/) musí mít signalizační body schopnost dynamicky se přizpůsobovat síťovým poruchám, zahlcení nebo událostem údržby. Bez mechanismu, jako je TFP, by porucha jednoho [STP](/mobilnisite/slovnik/stp/) mohla vést ke ztrátě signalizačních zpráv, selhání navazování hovorů nebo výpadkům služeb. TFP poskytuje standardizovaný způsob, jak signalizační bod informuje své sousedy, že nemůže sloužit jako cesta ke konkrétnímu cíli, a tím okamžitě spustí přeusměrování. Tím se řeší problém statických směrovacích tabulek, které nereagují na stav sítě v reálném čase. Umožňuje signalizační síti být samoléčící, přeusměrovávat provoz mimo místa poruch, aby byla zachována koncová signalizační konektivita, což je zásadní pro základní telefonní služby, správu mobility (např. předávání hovorů) a doplňkové služby. Jeho zavedení formalizovalo distribuovanou schopnost správy sítě, která je základním kamenem robustnosti veřejných telefonních sítí ([PSTN](/mobilnisite/slovnik/pstn/)) a jejich integrace s mobilními sítěmi.

## Klíčové vlastnosti

- Zpráva správy sítě SS7/SIGTRAN SCCP
- Označuje neschopnost směrovat ke konkrétnímu cílovému kódu bodu (DPC)
- Spouští dynamickou aktualizaci směrovacích tabulek v sousedních signalizačních bodech
- Umožňuje přeusměrování signalizačního provozu v případě poruch nebo zahlcení
- Spolupracuje se zprávou Transfer Allowed (TFA) pro obnovení cest
- Základní prvek pro spolehlivost signalizační sítě a správu poruch

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TFP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfp/)
