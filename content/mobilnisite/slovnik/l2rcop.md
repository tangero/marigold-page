---
slug: "l2rcop"
url: "/mobilnisite/slovnik/l2rcop/"
type: "slovnik"
title: "L2RCOP – Layer 2 Relay Character Oriented Protocol"
date: 2025-01-01
abbr: "L2RCOP"
fullName: "Layer 2 Relay Character Oriented Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/l2rcop/"
summary: "Protokol pro přenos rámců datové spojové vrstvy orientovaných na znaky, umožňující rozšíření nebo propojení spojů vrstvy 2. Funguje tak, že přijímá, případně zpracovává a přeposílá L2R rámce, a tím um"
---

L2RCOP je protokol vrstvy 2 pro přenos rámců datového spoje orientovaných na znaky za účelem rozšíření nebo propojení spojů, což umožňuje síťové topologie přesahující bod-bod pro řídicí a správní provoz.

## Popis

Layer 2 Relay Character Oriented Protocol (L2RCOP) je protokol definovaný 3GPP, který funguje jako přenosový agent pro rámce Character Orientated Protocol ([L2R](/mobilnisite/slovnik/l2r/)). Jeho hlavní úlohou je přijímat L2R rámce na jednom rozhraní, zpracovat je podle přenosových pravidel a přeposlat je na jiném rozhraní, čímž efektivně rozšiřuje dosah L2R spoje nebo propojuje více L2R segmentů. To umožňuje vytváření složitějších síťových topologií, jako je bod–více bodů nebo řetězová spojení, s využitím jednoduchého bod-bod L2R protokolu jako stavebního bloku.

Architektonicky je entita L2RCOP umístěna mezi dva nebo více L2R spoji. Ukončuje L2R protokol na svých příchozích rozhraních a extrahuje přenášená data (informační pole). Přeposílací logika poté určí příslušné odchozí rozhraní na základě adresních informací obsažených v rámci nebo předem nastaveného směrování. Protokol může provádět minimální zpracování, například kontrolu sekvence pro kontrolu rámce ([FCS](/mobilnisite/slovnik/fcs/)) před chybou před přeposláním, nebo může fungovat v transparentnějším 'drátovém' režimu. Po zpracování znovu zapouzdří přenášená data do nového L2R rámce s příslušnými oddělovači a přepočítaným FCS pro přenos na odchozím spoji. Tento proces činí přenosovou funkci z velké části neviditelnou pro koncové body původního L2R spojení.

V praxi L2RCOP umožňuje scénáře, kdy centrální řídicí systém potřebuje komunikovat s více vzdálenými síťovými prvky přes sdílenou nebo kaskádovanou fyzickou infrastrukturu. Například může být použit pro agregaci správních spojů z několika základnových stanic na jeden přenosový spoj směrem k síťovému řadiči. Protokol zajišťuje multiplexování a demultiplexování L2R toků. Klíčové pro jeho funkci je zachování integrity a posloupnosti přenášených správních zpráv. Standardizací této přenosové funkce 3GPP zajistilo, že síťoví návrháři mohou vytvářet škálovatelné správní sítě s využitím standardizovaných L2R spojů, aniž by každý uzel musel podporovat složitější síťové protokoly, čímž zachovávají jednoduchost a spolehlivost základního L2R protokolu a zároveň přidávají topologickou flexibilitu.

## K čemu slouží

L2RCOP byl vytvořen, aby překonal topologické omezení základního [L2R](/mobilnisite/slovnik/l2r/) protokolu, který je inherentně bod-bod protokolem. V praktických síťových nasazeních, zejména v přístupových sítích, často existuje potřeba připojit centrální místo k více vzdáleným místům přes společnou infrastrukturu (jako řetězová nebo stromová topologie). Nasazení individuálních bod-bod L2R spojů z centra ke každému vzdálenému místu by bylo neefektivní a nákladné. L2RCOP to řeší zavedením standardizované přenosové funkce.

Protokol umožňuje síťovým operátorům používat nákladově efektivní řetězová nebo hvězdicová fyzická uspořádání a přitom stále využívat jednoduchý, spolehlivý L2R protokol pro správní provoz. Řešil tak ekonomická a praktická omezení při budování správních sítí pro základnové stanice 2G a 3G. Bez takového přenosu by alternativou byla implementace složitějšího směrování na síťové vrstvě (IP) v každém uzlu, což bylo pro jednoduchý úkol přenosu OAM příkazů často zbytečně složité a náročné na zdroje. L2RCOP poskytl elegantní řešení na vrstvě 2, které rozšířilo využitelnost L2R, umožnilo škálovatelné a ekonomické návrhy správních sítí a zároveň zachovalo výhody interoperability standardizovaného základního protokolu.

## Klíčové vlastnosti

- Přeposílá L2R (Character Orientated Protocol) rámce mezi spoji
- Umožňuje topologie bod–více bodů a kaskádové topologie pro L2R
- Ukončuje a znovu generuje L2R rámce s novými oddělovači a FCS
- Může fungovat na základě adresování uvnitř přenášených rámců
- Rozšiřuje dosah a škálovatelnost spojů pro správu a řízení
- Zachovává jednoduchost a spolehlivost základního L2R protokolu

## Související pojmy

- [L2R – COP L2R Character Orientated Protocol](/mobilnisite/slovnik/l2r/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [L2RCOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/l2rcop/)
