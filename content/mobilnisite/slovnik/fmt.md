---
slug: "fmt"
url: "/mobilnisite/slovnik/fmt/"
type: "slovnik"
title: "FMT – Feedback Message Type"
date: 2025-01-01
abbr: "FMT"
fullName: "Feedback Message Type"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fmt/"
summary: "Pole v hlášeních zpětné vazby MBMS odesílaných UEs, které udává typ poskytované zpětné vazby, například stav dekódování nebo kvalitu kanálu. Umožňuje efektivní doručování multicastových/broadcastových"
---

FMT je pole v hlášeních zpětné vazby MBMS, které udává typ zpětné vazby, například stav dekódování, což síti umožňuje sbírat data od přijímačů a optimalizovat multicastové/broadcastové přenosy.

## Popis

Feedback Message Type (FMT, typ zprávy zpětné vazby) je parametr v protokolu zpětné vazby služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) používaném v broadcastových systémech LTE a 5G. Je definován v 3GPP TS 26.346 a je součástí popisu uživatelské služby MBMS a mechanismu hlášení zpětné vazby. FMT identifikuje kategorii informací o zpětné vazbě, kterou UE odesílá síti, například zda hlášení obsahuje indikátory úspěšného/neúspěšného dekódování, měření kvality přijímaného signálu nebo jiné metriky specifické pro službu.

Z architektonického hlediska funguje zpětná vazba MBMS v kontextu point-to-multipoint přenosu, kdy jeden zdroj vysílá více UEs. [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Center) a eNodeB/gNB spravují broadcastovou relaci, zatímco UEs službu monitorují. Protokol zpětné vazby umožňuje UEs odesílat hlášení směrem k síti, typicky přes unicastové procedury [RACH](/mobilnisite/slovnik/rach/), aby informovala síť o podmínkách příjmu. Pole FMT je součástí těchto zpráv zpětné vazby a specifikuje jejich obsahovou strukturu a účel, což síti umožňuje správně interpretovat následující informační elementy.

Jak to funguje: UE po splnění spouštěcích podmínek (např. periodické hlášení, při selhání dekódování) sestaví zprávu zpětné vazby. UE nastaví hodnotu FMT podle typu zpětné vazby, kterou potřebuje odeslat – například FMT=1 pro „MBMS Packet Error Rate Report“ nebo FMT=2 pro „MBMS Channel Quality Indicator Report“. Zpráva je následně přenesena přes uplink do eNodeB/gNB, který ji přepošle do BM-SC nebo jiných síťových funkcí. Síť využívá agregovanou zpětnou vazbu od více UEs k vyhodnocení celkového výkonu služby, úpravě modulace a kódovacích schémat nebo k vyvolání retransmisí poškozených dat.

Jeho role v síti spočívá v uzavření zpětné vazby u broadcastových/multicastových služeb, které tradičně kvůli své jednosměrné povaze zpětnou vazbu postrádají. Díky umožnění řízené zpětné vazby FMT usnadňuje adaptivní broadcastový přenos, čímž zlepšuje spolehlivost a efektivitu. Například pokud mnoho UEs hlásí selhání dekódování (indikováno specifickým FMT), síť může přepnout do robustnějšího přenosového režimu. To je klíčové pro služby jako komunikace pro veřejnou bezpečnost nebo živé televizní vysílání přes mobilní sítě, kde je pokrytí a kvalita prvořadé.

## K čemu slouží

FMT byl zaveden, aby řešil výzvu řízení a optimalizace služeb [MBMS](/mobilnisite/slovnik/mbms/), které ze své broadcastové povahy postrádají individuální zpětnou vazbu od přijímačů. Bez zpětné vazby síť funguje naslepo, může přenášet příliš vysokou datovou rychlostí pro okrajové uživatele nebo nemusí detekovat rozšířené problémy s příjmem. FMT poskytuje strukturovaný způsob, jak mohou UEs podávat hlášení, což umožňuje daty řízené síťové úpravy.

Hlavní problém, který řeší, je zvýšení spolehlivosti a efektivity doručování MBMS. Díky kategorizaci typů zpětné vazby umožňuje síti vyžádat si a zpracovat konkrétní informace potřebné pro různé optimalizační úkoly. Například zpětná vazba o kvalitě kanálu (jeden FMT) pomáhá při adaptaci modulace, zatímco zpětná vazba o stavu dekódování (jiný FMT) napomáhá mechanismům obnovy po chybách, jako je aplikace [FEC](/mobilnisite/slovnik/fec/) na aplikační vrstvě nebo plánování retransmisí. To vede k lepšímu využití zdrojů a zlepšenému uživatelskému zážitku, zejména v náročných rádiových podmínkách.

Historicky měly rané verze MBMS v 3GPP omezené možnosti zpětné vazby, což ztěžovalo podporu spolehlivých broadcastových služeb. Zavedení FMT jako součásti rozšířeného rámce MBMS (eMBMS) v Release 8 poskytlo standardizovaný mechanismus zpětné vazby. Řešilo tím omezení jednosměrného vysílání tím, že umožnilo lehký, škálovatelný kanál zpětné vazby, který je klíčový pro komunikace kritické z hlediska mise a efektivní doručování obsahu ve velkém měřítku v systémech LTE a 5G.

## Klíčové vlastnosti

- Identifikuje kategorii hlášení zpětné vazby MBMS (např. stav dekódování, kvalita kanálu)
- Umožňuje strukturovanou zpětnou vazbu od UEs směrem k síti pro broadcastové/multicastové služby
- Podporuje adaptivní přenosová schémata založená na agregovaných datech od přijímačů
- Definován v rámci popisu uživatelské služby MBMS a protokolu zpětné vazby
- Usnadňuje zlepšení spolehlivosti prostřednictvím obnovy po chybách s vědomím stavu sítě
- Integruje se s procedurami MBMS counting a kontinuity služby

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols

---

📖 **Anglický originál a plná specifikace:** [FMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/fmt/)
