---
slug: "nadu"
url: "/mobilnisite/slovnik/nadu/"
type: "slovnik"
title: "NADU – Next Application Data Unit"
date: 2025-01-01
abbr: "NADU"
fullName: "Next Application Data Unit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nadu/"
summary: "Koncept v rámci streamovacích služeb 3GPP, zejména v paketové streamovací službě (PSS), odkazující na následující datovou jednotku, kterou aplikace očekává zpracovat. Napomáhá synchronizaci, správě vy"
---

NADU (další aplikační datová jednotka) je koncept v rámci streamovacích služeb 3GPP pro následující datovou jednotku, kterou aplikace očekává, což napomáhá synchronizaci a správě vyrovnávací paměti pro doručování multimedií v reálném čase.

## Popis

Next Application Data Unit (NADU) je termín definovaný ve specifikacích 3GPP pro streamovací služby, především v TS 26.234 pro paketovou streamovací službu ([PSS](/mobilnisite/slovnik/pss/)). Představuje nadcházející datovou jednotku, kterou má streamovací klientská aplikace (např. mediální přehrávač) naplánovanou dekódovat a vykreslit na základě časové osy prezentace. Technicky NADU není pole hlavičky protokolu, ale logická entita používaná streamovacím klientem a serverem ke správě toku dat a synchronizace. Úzce souvisí s datovými částmi protokolu [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) nebo jinými formátovanými mediálními bloky, které tvoří streamovací relaci.

Při provozu klient udržuje přehrávací vyrovnávací paměť, která ukládá příchozí mediální datové jednotky. NADU je další jednotka v pořadí, která bude z této paměti spotřebována pro přehrávání. Klient využívá znalost NADU ke generování zpětných hlášení, např. v [RTCP](/mobilnisite/slovnik/rtcp/) (RTP Control Protocol) nebo prostřednictvím signalizace specifické pro 3GPP, aby informoval server o svém aktuálním stavu příjmu a předpokládaných potřebách. To může ovlivnit chování serveru, jako je úprava přenosových rychlostí, upřednostnění určitých paketů nebo spuštění retransmisí v případě ztráty před termínem přehrání. Koncept NADU je nedílnou součástí mechanismů adaptivního streamování, kde server může přepínat mezi různými reprezentacemi datového toku na základě stavu vyrovnávací paměti klienta a síťových podmínek.

Z architektonického hlediska NADU interaguje s komponentami, jako je správce vyrovnávací paměti streamovacího klienta, plánovač dekodéru a modul správy QoS. Pomáhá implementovat funkce jako rychlý posun vpřed, zpět a trikové režimy tím, že umožňuje klientovi signalizovat, kterou datovou jednotku potřebuje jako další při přeskočení na novou pozici na časové ose. V kontextu PSS a služby [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast/Multicast Service) 3GPP zajišťuje správná správa NADU plynulé přehrávání, minimalizuje události opětovného načítání do vyrovnávací paměti a optimalizuje využití rádiových prostředků tím, že umožňuje síti přednačítat nebo upřednostňovat doručení nejnaléhavěji potřebných dat.

## K čemu slouží

Koncept NADU byl zaveden, aby řešil výzvy při doručování streamovacích služeb v reálném čase přes nespolehlivé a v šířce pásma proměnlivé paketové mobilní sítě. Raná streamovací řešení často trpěla přerušeními přehrávání kvůli kolísání zpoždění, ztrátě paketů a kolísavé propustnosti, což vedlo ke špatnému uživatelskému zážitku. NADU poskytuje jasný referenční bod pro klienta i server, aby koordinovali doručování dat v souladu s požadavky aplikace v reálném čase.

Řeší problém neefektivní správy vyrovnávací paměti a nedostatku plánování v síti s ohledem na aplikaci. Identifikací další požadované datové jednotky může systém upřednostnit její přenos před méně kritickými daty, selektivně aplikovat korekci chyb vpřed nebo retransmise a proaktivně přizpůsobovat rychlost kódování média. To je obzvláště důležité v mobilním prostředí, kde se rádiové podmínky rychle mění a prostředky jsou sdíleny mezi mnoha uživateli.

Historicky byla jeho specifikace v Release 8 jako součást vylepšení [PSS](/mobilnisite/slovnik/pss/) motivována rostoucí popularitou mobilního streamování videa a potřebou standardizovaných mechanismů pro zlepšení kvality služeb. Koncept NADU umožnil sofistikovanější interakce klient-server nad rámec základního [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/), což umožnilo streamovacím službám 3GPP konkurovat internetovým streamovacím platformám díky robustnímu doručování s ohledem na síť. I když pozdější technologie, jako je Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) (DASH), zavedly odlišné paradigma, základní princip sledování dalšího potřebného datového segmentu zůstává relevantní pro optimalizaci streamování v reálném čase.

## Klíčové vlastnosti

- Logický identifikátor pro nadcházející mediální datovou jednotku při streamovacím přehrávání
- Používá se pro správu vyrovnávací paměti klienta a synchronizaci přehrávání
- Umožňuje QoS s ohledem na aplikaci a upřednostňování v síti
- Podporuje adaptivní streamování a rozhodování o přepínání datového toku
- Umožňuje operace trikových režimů (rychlé posuny vpřed/zpět) ve streamovacích službách
- Integruje se s doručovacími mechanismy PSS a MBMS 3GPP

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [NADU na 3GPP Explorer](https://3gpp-explorer.com/glossary/nadu/)
