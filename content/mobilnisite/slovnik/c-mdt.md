---
slug: "c-mdt"
url: "/mobilnisite/slovnik/c-mdt/"
type: "slovnik"
title: "C-MDT – Continuous Management-Based Minimization of Drive Tests"
date: 2026-01-01
abbr: "C-MDT"
fullName: "Continuous Management-Based Minimization of Drive Tests"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/c-mdt/"
summary: "C-MDT je funkce 3GPP umožňující nepřetržité, operátorem iniciované shromažďování měření z UE a sítě pro monitorování výkonu a optimalizaci bez fyzických drive testů. Poskytuje trvalé, automatizované s"
---

C-MDT je funkce 3GPP pro nepřetržité, automatizované shromažďování měření z UE a sítě za účelem monitorování výkonu a optimalizace RAN bez nutnosti fyzických drive testů.

## Popis

Continuous Management-Based Minimization of Drive Tests (C-MDT, nepřetržité minimalizace drive testů založená na řízení) je pokročilá funkce pro správu a optimalizaci sítě standardizovaná ve 3GPP Release 19. Rozšiřuje tradiční rámec [MDT](/mobilnisite/slovnik/mdt/) tím, že umožňuje operátorům konfigurovat a aktivovat relace sběru měření, které běží nepřetržitě po delší období, namísto omezení na okamžité nebo zaznamenané (logged) relace MDT spouštěné konkrétními událostmi nebo lokacemi. Architektura zahrnuje řídicí systém (typicky Network Management System nebo Element Management System) jako iniciující entitu, která posílá konfigurační příkazy MDT do uzlů RAN (gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v LTE) přes rozhraní Itf-N nebo do Core Network pro konfigurace založené na UE. RAN následně aktivuje specifikovaná měření na cílových UE nebo buňkách.

C-MDT funguje tak, že vytváří trvalý měřicí úkol definovaný operátorem přes management plane. Tento úkol zahrnuje parametry jako cílovou oblast (seznam buněk nebo tracking areas), typy měření (např. Reference Signal Received Power (RSRP), Reference Signal Received Quality (RSRQ), Timing Advance, hlášení o selhání rádiového spoje, úspěšnost handoverů), kritéria reportování (periodické nebo spouštěné událostí) a časovač platnosti, který lze nastavit na dny, týdny nebo i měsíce. RAN nakonfiguruje vybraná UE – která mohou být v idle nebo connected módu – aby tato měření prováděla. Pro UE podporující MDT jsou měření a související informace o poloze (pokud jsou dostupné a autorizované) shromažďovány a ukládány buď v RAN, nebo reportovány přímo, v závislosti na konfiguraci.

Shromážděná data jsou následně agregována a reportována zpět do řídicího systému. Reportování může probíhat téměř v reálném čase pro připojená UE nebo být zaznamenáno a reportováno později, když UE naváže spojení. RAN používá funkci Trace k asociaci měření s konkrétními UE a relacemi. Klíčové komponenty zahrnují Trace Function v RAN a Core Network, funkce konfigurace a sběru MDT v uzlech RAN a funkce zpracování a analýzy dat MDT v řídicím systému. Rozhraní mezi řídicím systémem a síťovými funkcemi je standardizováno v 3GPP TS 28.622 a TS 32.422, což zajišťuje interoperabilitu.

Role C-MDT v síti je klíčová pro provozní automatizaci a inteligenci. Mění optimalizaci sítě z reaktivního, manuálního procesu založeného na sporadických drive testech a stížnostech zákazníků na proaktivní, nepřetržitý proces datové analytiky. Shromažďováním obrovského množství dat z terénu ze skutečných uživatelských zařízení za reálných podmínek použití mohou operátoři vytvářet vysoce přesné mapy rádiového spektra, přesně lokalizovat a charakterizovat problémy s pokrytím (jako oblasti se slabým signálem nebo pilot pollution), analyzovat výkon mobility (selhání handoveru, ping-pong efekty) a porozumět metrikám kvality uživatelského prožitku (QoE) korelovaným s polohou a rádiovými podmínkami. Tato data jsou zásadní pro plánování rozšíření sítě, ladění parametrů antén, optimalizaci seznamů sousedních buněk a ověřování dopadu optimalizačních změn.

## K čemu slouží

C-MDT byl vytvořen, aby řešil významná omezení a rostoucí náklady spojené s tradičními drive testy pro optimalizaci a monitorování mobilních sítí. Fyzické drive testy jsou pracné, časově náročné, drahé a poskytují pouze snímek výkonu sítě v konkrétním čase a na konkrétních trasách. Nemohou zachytit dynamický, na uživatele zaměřený výkon napříč celou stopou sítě 24/7, zejména ve vnitřních prostorech nebo soukromých areálech, kde jsou drive testy neproveditelné. Navíc, jak se sítě vyvíjely k 5G se zvýšenou hustotou (small cells), širšími šířkami pásma a složitějšími funkcemi jako carrier aggregation a beamforming, stala se potřeba detailních, nepřetržitých dat o výkonu kritickou.

Historický kontext vychází z původního rámce [MDT](/mobilnisite/slovnik/mdt/) zavedeného ve 3GPP Release 10, který umožňoval Immediate MDT (spouštěný řídicím příkazem pro připojená UE) a Logged MDT (kde idle UE ukládají měření pro pozdější reportování). Ačkoli revoluční, tyto módy byly často kampaněmi – aktivované na krátkou dobu pro vyšetření konkrétního problému. C-MDT řeší potřebu trvalého monitorování, což operátorům umožňuje vytvořit 'vždy zapnutou' vrstvu měření pro klíčové ukazatele výkonu. To je motivováno posunem odvětví k zero-touch network and service management (ZSM), daty řízeným operacím a umělé inteligenci pro automatizaci sítí (AINA).

Řešením problému nespojitého sběru dat umožňuje C-MDT operátorům detekovat a diagnostikovat přerušované nebo lokálně specifické problémy, které by krátkodobé kampaně MDT mohly minout. Poskytuje základní datový kanál pro modely strojového učení, které předpovídají selhání sítě, optimalizují alokaci zdrojů a zajišťují konzistentní kvalitu služeb. Nakonec C-MDT snižuje provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)) automatizací sběru dat, urychluje optimalizační cykly a zlepšuje kvalitu sítě a uživatelský prožitek tím, že umožňuje důkazně podloženou, nepřetržitou optimalizaci.

## Klíčové vlastnosti

- Trvalé, operátorem konfigurované měřicí úkoly s dlouhými časovači platnosti (dny až měsíce)
- Podpora měření z UE v idle módu i connected módu
- Sběr komplexních rádiových měření (RSRP, RSRQ, SINR) s volitelnými informacemi o poloze
- Aktivace založená na řízení přes standardizovaná rozhraní Itf-N (TS 28.622/32.422)
- Sběr dat cílený na geografickou oblast (seznam buněk, tracking area) nebo specifické skupiny UE
- Flexibilní reportování: jak okamžité reportování, tak zaznamenané (logged) reportování s pozdějším načtením

## Související pojmy

- [MDT – Minimization of Drive Tests](/mobilnisite/slovnik/mdt/)

## Definující specifikace

- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration

---

📖 **Anglický originál a plná specifikace:** [C-MDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-mdt/)
