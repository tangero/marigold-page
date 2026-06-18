---
slug: "ea"
url: "/mobilnisite/slovnik/ea/"
type: "slovnik"
title: "EA – External Alarms"
date: 2025-01-01
abbr: "EA"
fullName: "External Alarms"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ea/"
summary: "Externí alarmy (EA) jsou signály generované externím zařízením nebo senzory a hlášené systému správy telekomunikační sítě. Indikují fyzické nebo environmentální podmínky ovlivňující síťovou infrastruk"
---

EA (External Alarms) je externí alarmový signál hlášený systému správy sítě, který indikuje fyzické nebo environmentální podmínky, jako je výpadek napájení nebo požár, které ovlivňují telekomunikační infrastrukturu.

## Popis

Externí alarmy (EA) v 3GPP odkazují na rozhraní a informační model správy, který umožňuje zařízením externím vůči jádru telekomunikační sítě – jako jsou napájecí systémy, chladicí jednotky, systémy detekce požáru nebo senzory fyzické bezpečnosti – hlásit svůj stav a alarmové podmínky systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systému správy prvku ([EMS](/mobilnisite/slovnik/ems/)). Tyto alarmy reprezentují fyzické nebo environmentální události, které mohou ovlivnit provoz a integritu síťových prvků, jako jsou základnové stanice, uzly jádrové sítě nebo datová centra. Rámec EA standardizuje způsob, jakým jsou tyto heterogenní externí události zachyceny, formátovány a integrovány do celkových procesů správy poruch telekomunikačního operátora.

Z architektonického hlediska jsou externí alarmy typicky hlášeny prostřednictvím standardizovaného rozhraní, často založeného na protokolech jako [SNMP](/mobilnisite/slovnik/snmp/) nebo [CORBA](/mobilnisite/slovnik/corba/), jak je definováno ve specifikacích správy 3GPP. Síťový prvek (např. NodeB, [eNB](/mobilnisite/slovnik/enb/) nebo gNB) nebo vyhrazená jednotka pro sběr alarmů funguje jako zprostředkující zařízení. Má fyzické nebo logické vstupní porty (např. suché kontakty, digitální vstupy), které se připojují k externím senzorům. Když je senzor aktivován (např. otevření dveří, překročení teplotního prahu, selhání usměrňovače), změní stav tohoto vstupu. Síťový prvek pak tuto změnu stavu namapuje na konkrétní typ a závažnost alarmu definované v jeho bázi informací pro správu ([MIB](/mobilnisite/slovnik/mib/)). Následně vygeneruje standardizované alarmové oznámení a odešle jej nadřazenému systému správy.

Proces zahrnuje několik klíčových komponent: externí senzor nebo zařízení generující nezpracovaný signál, alarmové vstupní rozhraní na telekomunikačním zařízení, logiku zpracování alarmů v rámci agenta správy zařízení a severní rozhraní směrem k NMS. Alarmové oznámení obsahuje kritické informace, jako je typ alarmu (např. 'selhání napájecího zdroje', 'narušení skříně'), vnímaná závažnost (kritický, závažný, menší, varování), pravděpodobná příčina, identifikátor konkrétní instance a čas výskytu. NMS konsoliduje tyto externí alarmy s interními alarmy ze softwaru a hardwaru síťového prvku a poskytuje jednotný pohled. To umožňuje operátorovi v centru provozu sítě vidět, že lokalita zažívá výpadek napájení spolu s následnými výpadky rádiového spoje.

Role externích alarmů v síti spočívá v proaktivní a preventivní údržbě. Monitorováním environmentálních podmínek mohou operátoři řešit problémy dříve, než způsobí výpadky služeb. Například alarm rostoucí teploty v skříni základnové stanice může podnítit servisní zásah k vyčištění ventilátorů nebo opravě klimatizace, čímž se předejde přehřátí a selhání hardwaru. Podobně alarm selhání napájecího zdroje umožňuje rychlé nasazení záložních generátorů. Tato integrace je klíčová pro dosažení cílů vysoké dostupnosti a spolehlivosti sítě, zejména u lokalit bez obsluhy. Transformuje NMS z čistě logického monitoru sítě na komplexní nástroj pro správu fyzické infrastruktury.

## K čemu slouží

Standardizace externích alarmů (EA) v 3GPP, sahající až k Release 5, byla hnána provozní potřebou spravovat kompletní fyzický ekosystém podporující mobilní síť. Rané mobilní sítě primárně spravovaly logické a hardwarové poruchy interní pro síťové zařízení samotné. Významná část výpadků služeb však pramenila z fyzických problémů: výpadků napájení, extrémních environmentálních podmínek, krádeží nebo požárů. Tyto události pocházely ze zařízení mimo tradiční telekomunikační doménu (např. systémy HVAC, komerční rozvodné sítě, bezpečnostní systémy) a byly často pro systém správy sítě neviditelné, dokud nenastaly sekundární poruchy.

Primární problém, který EA řeší, je izolovaná správa fyzické infrastruktury. Před standardizací, pokud lokalita ztratila komerční napájení, mohla síť hlásit pouze to, že vysílače-přijímače základnové stanice přestaly být dostupné po vyčerpání záložních baterií. Tento reaktivní přístup vedl k delšímu průměrnému času k opravě. Definováním standardního způsobu, jak síťové prvky přijímají a hlásí signály z externích senzorů, umožnilo 3GPP proaktivní a integrovanou správu poruch. Operátoři nyní mohli okamžitě přijímat alarm 'výpadek síťového napájení', což jim umožnilo vyslat zdroje dříve, než se baterie vybily a lokalita zcela zkolabovala.

Historicky, jak se sítě rozšiřovaly na desetitisíce často vzdálených a neobsluhovaných lokalit, se náklady na manuální návštěvy lokalit za účelem kontroly staly neúnosnými. EA poskytla nástroj pro vzdálené monitorování zdraví celé lokality. Motivací byly také ekonomické důvody a souvislost se smlouvami o úrovni služeb; předcházení výpadkům je levnější než jejich oprava a vyhýbá se pokutám za nesplnění [SLA](/mobilnisite/slovnik/sla/). Dále, s nástupem sdílení sítí a více-dodavatelského prostředí, standardizovaný model EA zajistil, že alarmy ze senzorů různých dodavatelů mohou být pochopeny jakýmkoli kompatibilním systémem správy, což zjednodušuje provozní a údržbové pracovní postupy.

## Klíčové vlastnosti

- Standardizované rozhraní pro integraci alarmů z netelekomunikačního zařízení do NMS
- Podpora různých typů alarmů: selhání napájecího systému, překročení teploty/vlhkosti, požár, narušení, zaplavení
- Definuje úrovně závažnosti alarmu (kritický, závažný, menší, varování) pro stanovení priorit
- Umožňuje korelaci mezi fyzickými alarmy a následným zhoršením síťových služeb
- Umožňuje proaktivní údržbu k prevenci hardwarových selhání a výpadků služeb
- Používá standardní protokoly správy (např. SNMP) pro oznamování a mazání alarmů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [EA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ea/)
