---
slug: "dse"
url: "/mobilnisite/slovnik/dse/"
type: "slovnik"
title: "DSE – Data Switching Exchange"
date: 2025-01-01
abbr: "DSE"
fullName: "Data Switching Exchange"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dse/"
summary: "Síťový prvek, který usnadňuje přepínání a směrování dat mezi různými sítěmi nebo službami. Slouží jako přepojovací bod pro datový provoz a umožňuje efektivní propojení a správu datových toků v telekom"
---

DSE je síťový prvek, který slouží jako přepojovací bod pro datový provoz a usnadňuje přepínání a směrování mezi různými sítěmi nebo službami za účelem efektivního propojení a správy datových toků.

## Popis

Data Switching Exchange (DSE) je základní komponenta jádra sítě definovaná ve specifikacích 3GPP, konkrétně v TS 21.905, která pokrývá slovní zásobu a termíny. Slouží jako přepínací uzel, který zajišťuje směrování a výměnu datového provozu mezi různými síťovými segmenty, například mezi okruhově přepínanou a paketově přepínanou doménou nebo mezi sítěmi různých operátorů. DSE funguje v podstatě podobně jako tradiční telefonní ústředna, ale pro datové služby; směruje datové pakety na základě adresních informací a síťových politik. Hraje klíčovou roli při zajišťování, aby data z uživatelských zařízení dorazila na zamýšlené místo určení, ať už v rámci stejné sítě, nebo přes externí sítě jako internet či sítě jiných operátorů.

DSE funguje tak, že zkoumá hlavičky paketů, aplikuje směrovací tabulky a případně provádí konverze protokolů, aby udržela bezproblémové připojení.

Z architektonického hlediska je DSE součástí širší datové roviny v sítích 3GPP a často spolupracuje s prvky jako [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node), GGSN (Gateway GPRS Support Node) v 2G/3G nebo [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) a [PGW](/mobilnisite/slovnik/pgw/) (Packet Data Network Gateway) v 4G/5G. Může zahrnovat přepínací matice, řídicí procesory a rozhraní pro zpracování vysokých objemů datového provozu. Mezi klíčové komponenty patří směrovací enginy, které určují další směr pro pakety, správci kvality služeb (QoS), kteří upřednostňují provoz, a bezpečnostní funkce jako firewally nebo šifrovací moduly. Úlohou DSE je agregovat data z více zdrojů, efektivně je přepínat a přeposílat je ke správnému výstupnímu bodu, čímž minimalizuje latenci a maximalizuje propustnost. To je nezbytné pro podporu služeb jako mobilní internet, VoIP a aplikace IoT.

Při provozu DSE přijímá datové pakety ze vstupních rozhraní, analyzuje jejich cílové adresy a konzultuje směrovací protokoly – například BGP (Border Gateway Protocol) pro mezisíťové směrování nebo statické trasy pro interní cesty. Může také provádět tvarování a regulaci provozu, aby vynucovala politiky QoS a zajistila, že kritická data získají přednostní zacházení. Například v mobilní síti může DSE směrovat uživatelská data z základnové stanice přes jádro sítě do externí paketové datové sítě ([PDN](/mobilnisite/slovnik/pdn/)). Jeho funkce se vyvíjí s generacemi sítí; v dřívějších vydáních se zaměřoval na přepínání dat GPRS a [EDGE](/mobilnisite/slovnik/edge/), zatímco v pozdějších vydáních se integruje s IP architekturami pro LTE a 5G. Centralizací přepínacích funkcí DSE zjednodušuje správu sítě a zvyšuje škálovatelnost, což operátorům umožňuje efektivně zvládat rostoucí datové nároky.

## K čemu slouží

DSE byl vytvořen, aby řešil potřebu efektivní správy datového provozu při přechodu mobilních sítí od služeb orientovaných na hlas ke službám orientovaným na data. V raných buněčných systémech bylo přepínání primárně okruhově přepínané pro hlas, ale s nástupem [GPRS](/mobilnisite/slovnik/gprs/) a paketových dat v 2G/3G vzrostl požadavek na specializovanou infrastrukturu pro přepínání dat. Před zavedením DSE se směrování dat často spoléhalo na ad-hoc řešení nebo jej zajišťovaly hlasové ústředny, což vedlo k neefektivitě a omezené škálovatelnosti. Zavedení DSE ve vydání 5 poskytlo standardizovaný prvek specializovaný na výměnu dat, který řešil problémy jako přetížení, špatné směrování a nedostatek interoperability mezi různými datovými sítěmi.

Historicky vycházela motivace z exploze využívání mobilních dat a rozšíření internetových služeb. Operátoři potřebovali způsob, jak bezproblémově připojovat účastníky k externím datovým sítím, a zároveň udržovat kontrolu nad tokem provozu a jeho kvalitou. DSE nabídl centralizovaný bod pro vynucování politik, účtování a zabezpečení, čímž řešil omezení dřívějších přístupů, které s daty zacházely jako s druhořadou službou. Umožnil lepší využití zdrojů oddělením přepínání dat od přepínání hlasu, což dovolilo optimalizovat hardware a software pro zpracování paketů. To bylo zásadní pro podporu vznikajících aplikací, jako je e-mail, prohlížení webu a později streamování médií.

Dále DSE usnadnil vývoj sítě tím, že poskytl základ pro pokročilé datové služby. Jak se sítě vyvíjely směrem k LTE a 5G, principy přepínání dat zůstaly relevantní a koncepty DSE ovlivnily prvky jako [PGW](/mobilnisite/slovnik/pgw/) a UPF (User Plane Function). Řešil problémy spojené s roamingem mezi více sítěmi a vzájemným propojením, čímž zajišťoval plynulý tok dat přes hranice operátorů. Standardizací DSE zajistil 3GPP, že operátoři mohou nasazovat interoperabilní zařízení, což snižuje náklady a zlepšuje spolehlivost služeb pro koncové uživatele.

## Klíčové vlastnosti

- Směruje a přepíná datové pakety mezi síťovými doménami
- Podporuje propojení s externími paketovými datovými sítěmi
- Integruje se s prvky jádra sítě, jako jsou SGSN, GGSN a PGW
- Vynucuje politiky QoS pro upřednostňování provozu
- Poskytuje škálovatelnost pro zpracování vysokých objemů datového provozu
- Usnadňuje konverze protokolů a síťovou interoperabilitu

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [DSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dse/)
