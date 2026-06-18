---
slug: "rrb"
url: "/mobilnisite/slovnik/rrb/"
type: "slovnik"
title: "RRB – Request Report BCSM Event"
date: 2025-01-01
abbr: "RRB"
fullName: "Request Report BCSM Event"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rrb/"
summary: "Request Report BCSM Event (RRB) je operace CAMEL (Customized Applications for Mobile Network Enhanced Logic) používaná k vyžádání monitorování a hlášení konkrétních událostí v modelu základního stavu"
---

RRB je operace CAMEL, která žádá o monitorování a hlášení konkrétních událostí v modelu základního stavu hovoru (BCSM) za účelem umožnění řízení služeb v reálném čase.

## Popis

Request Report [BCSM](/mobilnisite/slovnik/bcsm/) Event (RRB) je klíčová operace v rámci protokolu [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile Network Enhanced Logic), který poskytuje schopnosti Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) v sítích GSM, UMTS a IMS. BCSM (Basic Call State Model) je konečný automat, který abstraktně reprezentuje fáze hovoru (např. zahájení hovoru, vyzvánění, odpověď, odpojení). Operace RRB je odeslána z řídicí funkce služby (gsmSCF) na spínací funkci služby (gsmSSF nebo [MSC](/mobilnisite/slovnik/msc/)/[SSP](/mobilnisite/slovnik/ssp/)), aby jí nařídila monitorovat jednu nebo více konkrétních událostí BCSM vyskytujících se v dané instanci hovoru.

Z architektonického hlediska, když je nastavován hovor spouštěný CAMEL, může gsmSCF odeslat počáteční RRB jako součást operace Connect nebo Continue. RRB obsahuje seznam identifikátorů událostí BCSM (např. „O_Answer“ pro odpověď na straně volajícího, „O_Disconnect“ pro odpojení na straně volajícího, „Route_Select_Failure“). gsmSSF v rámci MSC poté aktivuje tyto detekční body. Jak hovor postupuje a aktivovaná událost nastane, gsmSSF přeruší základní zpracování hovoru a odešle operaci Event Report BCSM (ERB) zpět na gsmSCF. Tato zpráva obsahuje podrobnosti o události, jako je časové razítko. Po přijetí ERB může gsmSCF následně uplatnit servisní logiku – například spustit nebo zastavit časovač účtování, přehrát oznámení nebo upravit směrování hovoru.

Mechanismus RRB je způsob, jakým CAMEL dosahuje řízení v reálném čase řízeného událostmi. Funguje prostřednictvím série dialogů žádost-hlášení. Jeden CAMEL dialog pro hovor může zahrnovat více výměn RRB a ERB. Například počáteční RRB může aktivovat události „O_Answer“ a „O_Disconnect“ pro předplacený hovor. Když je nahlášena událost „O_Answer“, gsmSCF začne odečítat kredit. Když je nahlášena událost „O_Disconnect“, zastaví odečítání a dokončí účtování. To umožňuje servisní logice sídlící v síti (nikoli v koncovém zařízení) interagovat s průběhem hovoru a řídit jej na základě jeho vývoje, což umožňuje komplexní přidané služby, které jsou transparentní pro koncového uživatele a nezávislé na dodavateli ústředny.

## K čemu slouží

Operace RRB byla vytvořena, aby splnila základní slib Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a [CAMEL](/mobilnisite/slovnik/camel/): oddělit servisní logiku od spínací funkčnosti. Před IN byly služby jako předplacené účtování nebo filtrování hovorů pevně zakódovány do softwaru ústředny, což je činilo nákladnými na vývoj, pomalými na nasazení a závislými na dodavateli. CAMEL s operacemi jako RRB zavedl standardizovaný způsob, jak může externí servisní platforma ([SCP](/mobilnisite/slovnik/scp/)) řídit hovory v reálném čase tím, že je informována o klíčových událostech.

Řeší problém pasivního řízení služeb. Bez RRB by SCP mohlo nařídit ústředně sestavit hovor, ale nemělo by přehled o tom, zda byl hovor přijat, jak dlouho trval nebo proč selhal. RRB tuto transparentnost poskytuje tím, že umožňuje SCP vyžádat si hlášení právě o těchto událostech. To umožňuje přesné účtování založené na událostech (klíčové pro předplacené služby), sofistikované řízení hovorů (např. směrování podle denní doby, monitorování podvodů detekcí neobvyklých vzorců hovorů) a bezproblémovou přenositelnost služeb mezi sítěmi.

Historickým motivem byl rychlý růst předplacených mobilních služeb na konci 90. let 20. století. Operátoři potřebovali spolehlivou, standardizovanou metodu pro implementaci účtování a řízení v reálném čase. CAMEL a mechanismus RRB/ERB se staly globálním standardem 3GPP pro tento účel, což překonalo omezení proprietárních řešení IN. Umožnilo operátorům rychle a konzistentně zavádět pokročilé telefonní služby v síťových prostředích s více dodavateli a vytvořilo páteř mnoha komerčních mobilních služeb po desetiletí.

## Klíčové vlastnosti

- Operace CAMEL odeslaná z gsmSCF na gsmSSF k aktivaci konkrétních detekčních bodů BCSM
- Umožňuje hlášení událostí zpět servisní logice prostřednictvím operace Event Report BCSM (ERB)
- Klíčová pro aplikace řízení služeb v reálném čase, jako je předplacené účtování
- Monitoruje události průběhu hovoru (např. odpověď, odpojení, obsazeno, neodpovězeno)
- Umožňuje servisní logice dynamicky reagovat na změny stavu hovoru
- Standardizována napříč vydáními 3GPP pro konzistentní implementaci služeb v sítích GSM, UMTS a IMS

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [RRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrb/)
