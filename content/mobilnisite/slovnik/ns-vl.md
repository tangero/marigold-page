---
slug: "ns-vl"
url: "/mobilnisite/slovnik/ns-vl/"
type: "slovnik"
title: "NS-VL – Network Service Virtual Link"
date: 2025-01-01
abbr: "NS-VL"
fullName: "Network Service Virtual Link"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ns-vl/"
summary: "Logické spojení, které agreguje více spojení typu Network Service Virtual Connection (NS-VC) mezi BSC a serverem BSS Network Synchronization Server (NSS) přes rozhraní Iur-g. Představuje vyšší transpo"
---

NS-VL je logické spojení, které agreguje více spojení typu Network Service Virtual Connection (NS-VC) přes rozhraní Iur-g a vytváří tak vyšší transportní cestu pro synchronizační data mezi BSC a serverem BSS Network Synchronization Server.

## Popis

Network Service Virtual Link (NS-VL) je logická agregační entita definovaná v dokumentu 3GPP TS 48.016 pro rozhraní Iur-g, které propojuje řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) se serverem [BSS](/mobilnisite/slovnik/bss/) Network Synchronization Server ([NSS](/mobilnisite/slovnik/nss/)). Slouží jako kontejner nebo virtuální potrubí, které sdružuje více spojení typu Network Service Virtual Connection ([NS-VC](/mobilnisite/slovnik/ns-vc/)) a poskytuje jim společnou transportní cestu pro synchronizační informace. Samotný NS-VL funguje nad podkladovou fyzickou nebo virtuální transportní sítí (např. [ATM](/mobilnisite/slovnik/atm/) nebo IP) a je zodpovědný za správu společných zdrojů a kvality služeb pro přenášená NS-VC spojení. Představuje vyšší vrstvu abstrakce ve srovnání s jednotlivými NS-VC, což zjednodušuje konfiguraci sítě a její škálovatelnost.

Z architektonického hlediska je NS-VL zřízen mezi BSC a NSS pro podporu synchronizačních potřeb daného BSC. V rámci tohoto spojení lze vytvořit více NS-VC, z nichž každé je identifikováno jedinečným [NS-VCI](/mobilnisite/slovnik/ns-vci/), pro přenos různých typů synchronizačních dat nebo pro různé účely, jako jsou primární a záložní časové reference. NS-VL zajišťuje, že agregovaný provoz je zpracováván konzistentně z hlediska směrování, priority a spolehlivosti. Řídicí rovina protokolů zajišťuje zřizování, modifikaci a uvolňování NS-VL, stejně jako NS-VC v jeho rámci, což umožňuje dynamickou adaptaci na síťové podmínky nebo synchronizační požadavky.

V síti hraje NS-VL klíčovou roli při optimalizaci distribuce synchronizace. Agregací spojení snižuje signalizační režii a zjednodušuje správu, protože operátoři mohou konfigurovat a monitorovat NS-VL jako jedinou entitu namísto jednotlivých NS-VC. To je zvláště výhodné v rozsáhlých sítích s mnoha BSC, protože umožňuje centralizovaným synchronizačním serverům efektivně obsluhovat více koncových bodů. NS-VL také podporuje diferenciaci kvality služeb, což umožňuje upřednostnit kritické synchronizační toky v rámci spojení. Jeho návrh odráží vývoj směrem k virtualizovaným síťovým funkcím, kde logické konstrukce nahrazují fyzické propojení za účelem zvýšení flexibility a snížení nákladů na synchronizaci v rádiové přístupové síti.

## K čemu slouží

NS-VL byl zaveden pro řešení potřeby efektivní agregace a správy více synchronizačních spojení v rozvíjejících se mobilních sítích. S expanzí sítí a růstem počtu základnových stanic se správa jednotlivých synchronizačních spojení pro každý [BSC](/mobilnisite/slovnik/bsc/) stala složitou a náročnou na zdroje. NS-VL poskytuje strukturovaný způsob, jak tato spojení svázat, čímž zjednodušuje síťovou architekturu a zlepšuje škálovatelnost. Řeší problém koordinace a alokace zdrojů pro synchronizační provoz a zajišťuje spolehlivé doručování časových informací bez zahlcení transportní sítě množstvím samostatných spojení.

Jeho vytvoření bylo motivováno přechodem na paketový transport a virtualizované síťové funkce ve standardech 3GPP. Definováním vrstvy virtuálního spojení mohli operátoři efektivněji využívat statistické multiplexování a sdílené zdroje, čímž se snížily náklady a složitost synchronizační infrastruktury. NS-VL umožňuje flexibilnější modely nasazení, jako jsou centralizované synchronizační servery obsluhující více BSC přes společnou páteřní síť, což je klíčové pro moderní, husté rádiové přístupové sítě. Také umožňuje pokročilé funkce, jako je redundance a vyrovnávání zátěže, tím, že v rámci jednoho NS-VL umožňuje existenci více [NS-VC](/mobilnisite/slovnik/ns-vc/) poskytujících záložní nebo alternativní časové cesty.

Historicky se koncept NS-VL objevil ve 3GPP Release 8 jako součást rozšířených specifikací rozhraní Iur-g, navazujících na dřívější synchronizační metody, které takové agregační schopnosti postrádaly. Odstranil omezení bod-bod synchronizačních přístupů tím, že poskytl rámec pro řízenou a škálovatelnou distribuci synchronizace, čímž podpořil trend odvětví směrem k efektivnějším a interoperabilnějším síťovým návrhům v éře GSM a UMTS.

## Klíčové vlastnosti

- Logické spojení agregující více NS-VC na rozhraní Iur-g
- Poskytuje společnou transportní cestu pro synchronizační data mezi BSC a NSS
- Zjednodušuje správu sítě seskupením spojení do jedné entity
- Podporuje alokaci zdrojů a QoS pro agregovaný synchronizační provoz
- Umožňuje škálovatelnou distribuci synchronizace v rozsáhlých sítích
- Umožňuje dynamické zřizování a modifikaci prostřednictvím protokolů řídicí roviny

## Související pojmy

- [NS-VC – Network Service Virtual Connection](/mobilnisite/slovnik/ns-vc/)
- [NS-VCI – Network Service Virtual Connection Identifier](/mobilnisite/slovnik/ns-vci/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [NS-VL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns-vl/)
