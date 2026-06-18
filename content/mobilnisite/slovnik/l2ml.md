---
slug: "l2ml"
url: "/mobilnisite/slovnik/l2ml/"
type: "slovnik"
title: "L2ML – Layer 2 Management Link"
date: 2025-01-01
abbr: "L2ML"
fullName: "Layer 2 Management Link"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/l2ml/"
summary: "Standardizovaný managementový spoj pracující na spojové vrstvě modelu OSI (vrstva 2), používaný pro správu sítě a komunikaci řídicí roviny mezi síťovými prvky. Poskytuje spolehlivý transportní mechani"
---

L2ML je standardizovaný managementový spoj pracující na spojové vrstvě modelu OSI, používaný pro správu sítě a komunikaci řídicí roviny mezi síťovými prvky.

## Popis

Layer 2 Management Link (L2ML) je základní managementové rozhraní definované ve standardech 3GPP, které je speciálně navrženo pro provoz na spojové vrstvě modelu [OSI](/mobilnisite/slovnik/osi/). Vytváří vyhrazený logický nebo fyzický kanál pro výměnu managementových a řídicích informací mezi síťovými entitami, například mezi základnovou stanicí (NodeB, eNodeB, gNB) a jejím řídicím systémem správy sítě nebo radiovým síťovým řadičem. Protokolový zásobník pro L2ML je minimální, zaměřuje se na funkce spojové vrstvy, jako je rámování, detekce chyb a případně řízení toku, čímž zajišťuje spolehlivé doručení managementových paketů přes podkladové fyzické médium. Toto přímé spojení na vrstvě 2 izoluje kritický managementový provoz od dat uživatelské roviny a poskytuje stabilní a předvídatelnou cestu pro příkazy provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)), a to i během zahlcení sítě nebo selhání protokolů vyšších vrstev.

Z architektonického hlediska je L2ML často implementován přes point-to-point spoje, jako jsou linky T1/E1 nebo vyhrazená ethernetová připojení, které propojují síťové prvky v rámci radiové přístupové sítě (RAN) a s doménami správy jádra sítě. Slouží jako přenašeč pro managementové protokoly, přenáší datovou část protokolů vyšších vrstev, jako je [SNMP](/mobilnisite/slovnik/snmp/) nebo proprietární OAM protokoly. Samotný spoj je charakterizován svou jednoduchostí a spolehlivostí, vyhýbá se složitostem směrování na síťové vrstvě (IP) a relacím na transportní vrstvě (TCP/[UDP](/mobilnisite/slovnik/udp/)), aby poskytl přímý kanál. Tento návrh je klíčový pro počáteční bootstrap konfiguraci, obnovu po poruše a out-of-band management, kdy IP konektivita ještě nemusí být navázána nebo selhala.

Během provozu L2ML zajišťuje zapouzdření datových jednotek managementových protokolů ([PDU](/mobilnisite/slovnik/pdu/)) do rámců vhodných pro konkrétní používanou technologii fyzické vrstvy. Provádí řízení přístupu k médiu, zajišťuje uspořádaný přístup ke sdílenému nebo vyhrazenému médiu a implementuje kontrolní součet cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)) nebo jiné mechanismy pro detekci chyb, aby garantoval integritu dat. Ačkoli se nejedná o rozhraní orientované na služby, jeho role je pro zdraví sítě klíčová; umožňuje vzdálené aktualizace softwaru, monitorování výkonu, hlášení alarmů a změny konfigurace. Konzistentní specifikace L2ML napříč mnoha vydáními 3GPP podtrhuje jeho trvalý význam jako nízké, důvěryhodné managementové kanálu v architekturách sítí 3G UMTS i 4G LTE, tvořící základ pro spolehlivost a automatizaci sítě.

## K čemu slouží

L2ML byl vytvořen, aby vyřešil základní potřebu robustního, vždy dostupného managementového kanálu v telekomunikačních sítích, který je nezávislý na datových rovinách přenášejících služby. Před jeho standardizací byla managementová rozhraní často proprietární nebo spoléhala na stejné transportní cesty jako uživatelská data, což vytvářelo jediný bod selhání. Pokud selhalo směrování uživatelské roviny nebo došlo k jejímu zahlcení, mohli operátoři sítí ztratit schopnost problém vzdáleně diagnostikovat a napravit. L2ML poskytuje out-of-band managementovou cestu, která zajišťuje, že se operátoři mohou vždy dostat k síťovým prvkům pro kritické [OAM](/mobilnisite/slovnik/oam/) funkce.

Motivace vycházela z rostoucí složitosti a automatizace sítí 2G a raných 3G, které vyžadovaly spolehlivější a standardizovanější možnosti vzdálené správy. Tím, že pracuje na vrstvě 2, odstraňuje závislosti na IP zásobníku, který může být chybně nakonfigurován nebo kompromitován. To je obzvláště důležité během počátečního nasazení a instalace síťového prvku nebo ve scénářích obnovy po závažné poruše. L2ML zajišťuje, že k zařízení existuje 'záchranné lano' založené na jednoduchých, dobře pochopených principech spojové vrstvy, což usnadňuje spolehlivé zprovoznění sítě, nepřetržitý dohled a odolné řízení poruch, což jsou nezbytné požadavky na sítě úrovně operátora.

## Klíčové vlastnosti

- Pracuje nezávisle na spojové vrstvě modelu OSI (vrstva 2)
- Poskytuje vyhrazený kanál pro managementový a řídicí provoz
- Zajišťuje spolehlivý transport pomocí mechanismů rámování a detekce chyb
- Podporuje out-of-band management pro vysokou dostupnost a obnovu po poruše
- Slouží jako přenašeč pro OAM protokoly vyšších vrstev (např. SNMP)
- Využívá se pro počáteční bootstrap konfiguraci a aktualizace softwaru

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [L2ML na 3GPP Explorer](https://3gpp-explorer.com/glossary/l2ml/)
