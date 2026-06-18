---
slug: "pani"
url: "/mobilnisite/slovnik/pani/"
type: "slovnik"
title: "PANI – Piggy-backed Ack/Nack Indicator"
date: 2025-01-01
abbr: "PANI"
fullName: "Piggy-backed Ack/Nack Indicator"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pani/"
summary: "Řídicí pole v hlavičce uplink rádiového bloku v GERAN, které signalizuje přítomnost přibalovaného potvrzovacího/negativního potvrzovacího sdělení (PAN) ve stejném bloku. Funguje jako příznak, který in"
---

PANI je řídicí příznak v hlavičce uplinku GERAN, který indikuje přítomnost přibalovaného potvrzovacího sdělení (piggy-backed acknowledgment) ve stejném rádiovém bloku, které má příjemce dekódovat.

## Popis

Piggy-backed Ack/Nack Indicator (PANI) je specifické krátké pole umístěné v hlavičce rádiového bloku řízení spojového spoje/řízení přístupu k médiu ([RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/)) v GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Jeho jedinou funkcí je poskytovat pásmový signalizační údaj (in-band signaling), který indikuje, zda aktuální rádiový blok obsahuje přibalované potvrzovací/negativní potvrzovací sdělení ([PAN](/mobilnisite/slovnik/pan/)) ve své části užitečného zatížení. PANI je typicky jeden bit nebo malá skupina bitů definovaná ve struktuře hlavičky bloku. Když má mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) potvrzovací informaci k odeslání a je jí přidělen uplink zdroj pro přenos dat, nastaví PANI na specifickou hodnotu (např. '1'), aby označila 'PAN přítomen'. Pokud žádné potvrzení není třeba odeslat, je PANI nastaven na opačnou hodnotu (např. '0').

Po odeslání je rádiový blok – skládající se z hlavičky (s PANI), užitečného zatížení (které může obsahovat uživatelská data a/nebo PAN sdělení) a koncových bitů – přenášen přes rozhraní vzduchu. Příjmová část základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) nejprve dekóduje hlavičku bloku. Vrstva MAC v BSS zkontroluje PANI. Pokud je indikátor nastaven, BSS ví, že část užitečného zatížení bloku nejsou uživatelská data, ale je to PAN sdělení. BSS poté provede proces demultiplexování a extrahuje PAN sdělení z předem definované pozice v rámci užitečného zatížení podle pravidel specifikace. Toto extrahované PAN sdělení je pak předáno entitě RLC ke zpracování potvrzení, což spustí retransmise nebo posun okna.

PANI je klíčovým prvkem pro efektivní fungování mechanismu PAN. Bez něj by BSS musela slepě zkoušet dekódovat každý uplink blok jako potenciálně obsahující PAN sdělení nebo používat mimopásmovou signalizaci, což jsou obě neefektivní přístupy. Indikátor umožňuje dynamické a flexibilní využití oblasti užitečného zatížení. Jeho specifikace je těsně svázána s přesnými formáty RLC/MAC bloků pro různé typy kanálů (např. [PDTCH](/mobilnisite/slovnik/pdtch/), PACCH) a kódovací schémata, jak je podrobně popsáno v 3GPP TS 45.003. Přítomnost PANI minimalizuje složitost zpracování a zajišťuje spolehlivou interpretaci struktury bloku.

## K čemu slouží

PANI byl zaveden, aby vyřešil specifický problém rámcování vytvořený konceptem přibalování (piggy-backing). Pouhé vložení PAN sdělení do užitečného zatížení datového bloku by poškodilo data, pokud by příjemce přesně nevěděl, kde PAN data začínají a končí. Účelem PANI je poskytnout tyto informace o rámcování explicitně a efektivně. Funguje jako řídicí signál s nízkou režií uvnitř přenosového pásma (low-overhead, in-band), který dynamicky konfiguruje interpretaci struktury přijatého bloku pro každý přenos.

Před zavedením takového indikátoru systémy mohly používat pevná pole nebo samostatné signalizační kanály, což je méně flexibilní a plýtvá zdroji. PANI umožňuje systému využívat cenný prostor užitečného zatížení pouze pro uživatelská data, když nejsou žádná čekající potvrzení, čímž maximalizuje propustnost. Když jsou potvrzení potřebná, PANI bezproblémově překonfiguruje formát bloku pro tento jediný přenos. Tato dynamická adaptace je klíčová pro zvládání proměnlivé a nárazové povahy datového provozu a s ním spojené zpětné vazby.

Jeho vytvoření bylo motivováno potřebou robustní a jednoznačné signalizační metody v rámci těsně definované protokolové architektury GERAN. Zajišťuje zpětnou kompatibilitu a jasné řízení stavu mezi MS a BSS. PANI, ačkoli jde o malou komponentu, je nezbytný pro spolehlivý provoz mechanismu PAN s vyšší efektivitou, díky čemuž je celý proces ARQ jak efektivní, tak šetrný k prostředkům.

## Klíčové vlastnosti

- Jednobitové nebo malé vícebitové pole v hlavičce uplink RLC/MAC bloku
- Poskytuje binární indikaci přítomnosti PAN sdělení ve stejném rádiovém bloku
- Umožňuje dynamickou interpretaci užitečného zatížení (pouze data vs. data+PAN)
- Pásmový signalizační údaj s nízkou režií, který minimalizuje režii protokolu
- Nezbytný pro správné demultiplexování řídicích a uživatelských dat na straně příjemce
- Podrobně specifikován v dokumentech pro rádiový přenos a příjem (TS 45.003)

## Související pojmy

- [PAN – Piggy-backed Ack/Nack message](/mobilnisite/slovnik/pan/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)

## Definující specifikace

- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE

---

📖 **Anglický originál a plná specifikace:** [PANI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pani/)
