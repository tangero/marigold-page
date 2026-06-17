---
slug: "anbrq"
url: "/mobilnisite/slovnik/anbrq/"
type: "slovnik"
title: "ANBRQ – Access Network Bitrate Recommendation Query"
date: 2025-01-01
abbr: "ANBRQ"
fullName: "Access Network Bitrate Recommendation Query"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/anbrq/"
summary: "Mechanismus v mediálních službách založených na IMS, kdy UE dotazuje přístupovou síť o doporučené přenosové rychlosti. Umožňuje adaptivní mediální streamování tím, že UE může žádat o doporučení přenos"
---

ANBRQ je mechanismus v mediálních službách založených na IMS, kdy uživatelské zařízení (UE) dotazuje přístupovou síť o doporučené přenosové rychlosti, aby umožnilo adaptivní streamování a optimalizovalo kvalitu uživatelského zážitku.

## Popis

Dotaz na doporučení přenosové rychlosti přístupové sítě (ANBRQ) je procedura definovaná v rámci architektury IP Multimedia Subsystem (IMS), konkrétně v kontextu služeb doručování a streamování médií. Funguje jako mechanismus požadavku iniciovaného uživatelským zařízením (UE) směrem k přístupové síti, typicky přes funkci Policy and Charging Rules Function (PCRF) nebo přímo k uzlu přístupové sítě (např. eNodeB v LTE, gNB v 5G NR). Jeho hlavní funkcí je, aby si UE vyžádalo doporučenou přenosovou rychlost nebo sadu přenosových rychlostí, které přístupová síť považuje za optimální vzhledem k aktuálním rádiovým podmínkám, vytížení sítě a parametrům QoS.

Architektonická implementace zahrnuje odeslání zprávy ANBRQ ze strany UE, která je přenášena přes referenční bod Rx při interakci s PCRF nebo přes jiná rozhraní specifická pro přístupovou síť. Tento dotaz obsahuje parametry jako typ média (např. video, audio), požadovanou úroveň kvality a případně aktuální stav vyrovnávací paměti. Přístupová síť tento dotaz zpracuje s ohledem na metriky v reálném čase, jako je dostupná šířka pásma, úroveň zahlcení a kvalita rádiového spoje. Na základě této analýzy formuluje odpověď s doporučením přenosové rychlosti přístupové sítě ([ANBR](/mobilnisite/slovnik/anbr/)), která obsahuje jednu nebo více doporučených hodnot přenosové rychlosti, případně s přidruženou dobou platnosti nebo podmínkami.

Mechanismus ANBRQ je nedílnou součástí adaptivního streamování s proměnnou přenosovou rychlostí ([ABR](/mobilnisite/slovnik/abr/)) v mobilních sítích, zejména pro služby jako Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) nebo HTTP Live Streaming ([HLS](/mobilnisite/slovnik/hls/)). Dotazováním sítě může UE činit informovanější rozhodnutí při výběru vhodné reprezentace média, čímž se snižuje počet zastavení přehrávání, minimalizuje se opětovné načítání a zlepšuje se celková kvalita uživatelského zážitku (QoE). Tento síťově asistovaný přístup kontrastuje s čistě klientskými algoritmy ABR, protože využívá síťovou inteligenci, kterou UE nemůže přímo pozorovat, jako je zahlcení na úrovni buňky nebo provozovatelské politiky.

V praxi se ANBRQ často používá ve spojení s dalšími možnostmi IMS, jako je Service-Based Interface (SBI) a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)). Procedura je definována v dokumentu 3GPP TS 26.114, který specifikuje multimediální telefonní službu IP Multimedia Subsystem (IMS) a doplňkové služby. Interakce zajišťuje, že adaptace médií je v souladu se síťovými podmínkami a řídicími politikami, což usnadňuje efektivní využití zdrojů a konzistentní poskytování služeb v různých síťových prostředích.

## K čemu slouží

ANBRQ byl zaveden, aby řešil výzvy adaptivního mediálního streamování přes mobilní sítě, kde kolísající rádiové podmínky a síťové zahlcení mohou vážně ovlivnit uživatelský zážitek. Před jeho zavedením se adaptivní streamování spoléhalo primárně na heuristiku na straně klienta založenou na pozorované propustnosti a úrovni vyrovnávací paměti, což často vedlo k neoptimálním rozhodnutím kvůli nedostatku přehledu ze strany sítě. To mohlo mít za následek časté přepínání přenosových rychlostí, zastavování videa nebo neefektivní využití síťových zdrojů, což degradovalo kvalitu uživatelského zážitku (QoE).

Motivován potřebou optimalizace streamování za asistence sítě umožňuje ANBRQ přímou komunikaci mezi UE a přístupovou sítí za účelem získání doporučení přenosové rychlosti. To umožňuje síti sdělit svou aktuální kapacitu a omezení daná politikami, čímž pomáhá UE vybrat nejvhodnější přenosovou rychlost média. Tento mechanismus je obzvláště cenný ve spravovaných sítích, kde provozovatelé chtějí prosazovat politiky, zajistit spravedlivé přidělování zdrojů a udržovat konzistentní kvalitu služeb napříč uživateli. Poskytováním doporučení vedených sítí pomáhá ANBRQ snižovat odhadování v klientské adaptaci, což vede k plynulejšímu přehrávání, nižší latenci a lepšímu celkovému řízení zdrojů.

Historicky, jak mobilní video provoz exponenciálně rostl, 3GPP v Release 14 uznalo omezení čistě klientské adaptace a zavedlo ANBRQ jako součást vylepšení pro služby založené na IMS. Řeší propast mezi síťovými podmínkami a vnímáním klienta, což umožňuje citlivější a efektivnější doručování médií. To je v souladu se širším průmyslovým trendem směrem k síťové inteligenci a řízení služeb zohledňujícímu kvalitu, což podporuje pokročilé případy použití, jako je video v ultra vysokém rozlišení, streamování s nízkou latencí a imerzivní média.

## Klíčové vlastnosti

- Umožňuje UE dotazovat přístupovou síť na doporučení přenosových rychlostí
- Podporuje adaptivní streamování s proměnnou přenosovou rychlostí (ABR) v multimediálních službách IMS
- Usnadňuje síťově asistovanou adaptaci médií na základě podmínek v reálném čase
- Integruje se s PCRF a uzly přístupové sítě přes standardizovaná rozhraní
- Zlepšuje kvalitu uživatelského zážitku (QoE) snížením počtu zastavení a optimalizací výběru přenosové rychlosti
- Umožňuje prosazování provozovatelských politik a efektivní využití zdrojů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [ANBRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/anbrq/)
