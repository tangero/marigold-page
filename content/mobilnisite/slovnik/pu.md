---
slug: "pu"
url: "/mobilnisite/slovnik/pu/"
type: "slovnik"
title: "PU – Payload Unit"
date: 2025-01-01
abbr: "PU"
fullName: "Payload Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pu/"
summary: "Základní datová jednotka v protokolové vrstvě řízení rádiového spoje (RLC). Je to formátovaný blok dat (včetně hlavičky a užitečného zatížení), který se přenáší mezi partnerskými entitami RLC přes log"
---

PU je základní formátovaný datový blok obsahující hlavičku a užitečné zatížení, který se přenáší mezi partnerskými entitami řízení rádiového spoje (RLC) přes logické kanály.

## Popis

Jednotka užitečného zatížení (Payload Unit, PU) je klíčová datová struktura v architektuře systému univerzálních mobilních telekomunikací (UMTS) 3GPP a vyvinutého protokolu řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)). Nachází se ve vrstvě datového spoje (vrstva 2) protokolového zásobníku rozhraní. PU je výstupem vysílající entity RLC a vstupem přijímající entity RLC pro daný logický kanál. Její struktura a zpracování závisí na režimu provozu RLC: transparentním režimu ([TM](/mobilnisite/slovnik/tm/)), nepotvrzovaném režimu ([UM](/mobilnisite/slovnik/um/)) nebo potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)).

Z architektonického hlediska vrstva RLC přijímá servisní datové jednotky ([SDU](/mobilnisite/slovnik/sdu/)) z vyšší vrstvy (např. od protokolu konvergence paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) nebo [RRC](/mobilnisite/slovnik/rrc/)). Entita RLC tyto SDU zpracuje a vytvoří z nich PU pro přenos. Toto zpracování zahrnuje klíčové funkce: Pro AM a UM RLC přidá k SDU (nebo jeho segmentu) hlavičku. Tato hlavička obsahuje klíčové informace, jako je pořadové číslo ([SN](/mobilnisite/slovnik/sn/)), které se používá pro doručování ve správném pořadí a správu retransmisí, a indikátory segmentace. Datové pole obsahuje vlastní SDU nebo jeho segment. Tato kombinace hlavičky a SDU tvoří PU. V transparentním režimu se žádná hlavička nepřidává; PU je v podstatě samotné SDU, které prochází beze změny.

Operační postup je následující: Vysílající entita RLC provede segmentaci a/nebo konkatenaci příchozích SDU, aby je přizpůsobila velikosti dostupných přenosových bloků (TB) indikovaných vrstvou MAC. Poté sestaví PU připojením potřebné hlavičky RLC. Tato PU je doručena vrstvě řízení přístupu k médiu (MAC) jako servisní datová jednotka MAC. Vrstva MAC multiplexuje PU z různých logických kanálů do přenosového bloku pro přenos fyzickou vrstvou. Na přijímací straně je proces obrácený. Vrstva MAC doručí PU příslušné entitě RLC. Entita RLC odstraní hlavičku, použije pořadové číslo pro přeřazení a provede opětovné sestavení SDU z více PU (pokud došlo k segmentaci), než kompletní SDU předá výše.

Role PU je klíčová pro spolehlivostní funkce RLC. V potvrzovaném režimu je PU jednotkou retransmise. Pokud je PU ztracena, přijímající RLC může požadovat její retransmisi pomocí stavových hlášení, která odkazují na pořadové číslo PU. Struktura PU umožňuje partnerským entitám RLC udržovat synchronizovaný pohled na to, jaká data byla úspěšně přenesena. Je to atomová jednotka přenosu dat, pro kterou vrstva RLC poskytuje své charakteristické služby: transparentní přenos, nepotvrzovaný přenos dat nebo potvrzovaný přenos dat s opravou chyb.

## K čemu slouží

Koncept jednotky užitečného zatížení (PU) byl zaveden od nejranějších specifikací UMTS 3GPP (Release 99), aby poskytl strukturovaný a efektivní mechanismus pro přenos dat přes náchylný k chybám rádiový spoj. Hlavní problém, který řeší, je nesoulad mezi velikostí datových paketů z vyšších vrstev (které mohou být velké, např. IP paket) a velikostí přenosových jednotek fyzické vrstvy (přenosových bloků), které jsou omezeny rádiovými podmínkami a přiděleními schedularu.

Před zpracováním v RLC, které PU ztělesňuje, neexistoval standardizovaný způsob, jak spolehlivě zvládnout segmentaci a opětovné sestavení přes rádiové rozhraní pro paketově spínané služby. PU se svou hlavičkou obsahující pořadová čísla a informace o segmentaci tuto schopnost poskytuje. Umožňuje rozložit velké pakety vyšších vrstev pro přenos a spolehlivě je ve správném pořadí znovu sestavit na přijímači, i když jednotlivé segmenty (PU) dorazí mimo pořadí kvůli retransmisím HARQ nebo proměnlivému zpoždění.

Historicky bylo její vytvoření motivováno potřebou podporovat různé služby – od hlasu (pomocí malých, na zpoždění citlivých PU v TM) po paketová data (pomocí větších, spolehlivých PU v AM) – přes jednu flexibilní vrstvu řízení rádiového spoje. PU je ztělesněním služby, kterou vrstva RLC poskytuje vyšším vrstvám, abstrahuje složitosti rádiového spoje. Řeší základní problém přizpůsobení libovolných datových toků vyšších vrstev granularitě, variabilitě a nespolehlivosti prostředku fyzického rádiového kanálu, což umožňuje efektivní a spolehlivý přenos dat, který je základem všech datových služeb 3GPP v buňkových sítích.

## Klíčové vlastnosti

- Formátovaný datový blok přenášený mezi partnerskými entitami RLC
- Obsahuje hlavičku RLC (pro režimy UM/AM) a datové pole
- Datové pole nese servisní datovou jednotku (SDU) vyšší vrstvy nebo segment SDU
- Pořadové číslo v hlavičce umožňuje doručování ve správném pořadí a retransmise
- Slouží jako jednotka pro segmentaci, konkatenaci a opravu chyb
- Struktura se liší mezi transparentním režimem (žádná hlavička), nepotvrzovaným režimem a potvrzovaným režimem

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [SDU – Signalling Data Unit](/mobilnisite/slovnik/sdu/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture

---

📖 **Anglický originál a plná specifikace:** [PU na 3GPP Explorer](https://3gpp-explorer.com/glossary/pu/)
