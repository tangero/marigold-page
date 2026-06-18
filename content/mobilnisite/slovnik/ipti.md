---
slug: "ipti"
url: "/mobilnisite/slovnik/ipti/"
type: "slovnik"
title: "IPTI – Inter PDU Transmission Interval"
date: 2025-01-01
abbr: "IPTI"
fullName: "Inter PDU Transmission Interval"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ipti/"
summary: "Inter PDU Transmission Interval (IPTI) je časovací parametr, který definuje minimální časový interval mezi vysíláním po sobě jdoucích protokolových datových jednotek (PDU) na rádiovém přenosovém kanál"
---

IPTI je časovací parametr, který definuje minimální interval mezi vysíláním po sobě jdoucích protokolových datových jednotek (PDU) na rádiovém přenosovém kanálu za účelem řízení tempa vysílání ve směru uplink od vrstvy RLC ke vrstvě MAC.

## Popis

Inter [PDU](/mobilnisite/slovnik/pdu/) Transmission Interval (IPTI) je parametr přidružený k rádiovému přenosovému kanálu v systémech 3GPP UMTS a LTE. Stanovuje minimální časovou mezeru, která musí být dodržena mezi vysíláním po sobě jdoucích protokolových datových jednotek (PDU) z vrstvy řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) do vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro daný logický kanál. Tento parametr se primárně využívá ve směru uplink. IPTI funguje tak, že zavádí vynucené zpoždění na vysílači RLC; poté, co vyšle jednotku RLC PDU (např. [AMD](/mobilnisite/slovnik/amd/) PDU v potvrzovaném režimu), musí entita RLC počkat alespoň po dobu trvání IPTI, než smí předat další PDU k vysílání do vrstvy MAC.

Z architektonického hlediska je IPTI konfigurován vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) jako součást procedur zřízení nebo rekonfigurace rádiového přenosového kanálu. Je součástí konfigurace logického kanálu. Klíčovými zapojenými komponentami jsou entita RLC v UE (pro uplink) nebo NodeB/eNodeB (pro downlink, i když méně obvykle), protokol RRC, který parametr nastavuje, a plánovač MAC, na který má tempo předávání PDU z RLC nepřímý vliv. Hodnota IPTI je typicky definována v milisekundách nebo podrámcích.

Jeho úlohou je regulovat tok dat do vrstvy MAC, čímž zabraňuje přenosům v dávkách, které by mohly vést k neefektivnímu plánování, zvýšenému riziku přetečení vyrovnávací paměti nebo nežádoucím interferenčním vzorům. Prostřednictvím rozestavování PDU může síť dosáhnout předvídatelnějšího a plynulejšího provozu, což může být výhodné pro některé služby s nízkou přenosovou rychlostí a tolerancí k zpoždění nebo pro řízení časování uplink přenosů ve vztahu k jiným kanálům. Jedná se o nástroj, který síti umožňuje řídit charakteristiky uplink přenosů na úrovni jednotlivých rádiových přenosových kanálů, což ovlivňuje kompromis mezi latencí a granularitou plánování.

## K čemu slouží

Parametr IPTI byl vytvořen, aby poskytl síti explicitní kontrolu nad tempem přenosu dat na jednotlivých rádiových přenosových kanálech. V raných verzích UMTS, bez takového řízení tempa, mohla vrstva [RLC](/mobilnisite/slovnik/rlc/) doručovat [PDU](/mobilnisite/slovnik/pdu/) do vrstvy [MAC](/mobilnisite/slovnik/mac/) ihned, jak byly k dispozici od vyšších vrstev. U některých aplikací, zejména těch generujících malé periodické datové pakety (jako VoIP nebo určitý herní provoz), to mohlo vést k velmi dávkovým uplink přenosům, které byly suboptimální pro řízení výkonu, přidělování kódů a celkové řízení rádiových zdrojů.

Problém, který řeší, je neefektivní využití uplink zdrojů a potenciální zhoršení kvality pro služby citlivé na zpoždění způsobené nekontrolovanými přenosovými dávkami. Zavedením konfigurovatelného minimálního intervalu může síť 'tvarovat' vzorec provozu tak, aby lépe odpovídal plánovacím příležitostem a interferenčním podmínkám. Motivací byla potřeba optimalizovat kapacitu systému a kvalitu služeb pro mix různých typů provozu. IPTI umožňuje síti vyměnit malé, řízené zvýšení zpoždění paketů za uspořádanější a předvídatelnější plán uplink přenosů, což zlepšuje celkovou stabilitu a výkon systému, zejména v podmínkách zatížené buňky.

## Klíčové vlastnosti

- Definuje minimální časovou mezeru mezi po sobě jdoucími přenosy RLC PDU
- Konfigurován na úrovni rádiového přenosového kanálu prostřednictvím signalizace RRC
- Primárně aplikován ve směru uplink
- Používá se pro tvorbu provozu a řízení tempa na vrstvě RLC
- Ovlivňuje latenci a chování plánování
- Hodnota parametru je specifikována v časových jednotkách (např. ms, TTIs)

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 29.415** (Rel-19) — Nb User Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [IPTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipti/)
