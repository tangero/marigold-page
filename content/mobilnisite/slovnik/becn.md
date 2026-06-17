---
slug: "becn"
url: "/mobilnisite/slovnik/becn/"
type: "slovnik"
title: "BECN – Backward Explicit Congestion Notification"
date: 2025-01-01
abbr: "BECN"
fullName: "Backward Explicit Congestion Notification"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/becn/"
summary: "BECN je mechanismus signalizace zahlcení na rozhraní Gb dle 3GPP, který informuje SGSN o zahlcení sítě ve směru downlink. Umožňuje síti proaktivně řídit tok provozu a předcházet ztrátám paketů tím, že"
---

BECN je mechanismus signalizace zahlcení na rozhraní Gb, který zpětně signalizuje zahlcení v downlinku ze strany BSS směrem k SGSN za účelem proaktivního řízení provozu a předcházení ztrátám paketů v sítích 2G/3G.

## Popis

Backward Explicit Congestion Notification (BECN) je mechanismus řízení zahlcení specifikovaný v 3GPP TS 48.016 pro rozhraní Gb, které spojuje Base Station System ([BSS](/mobilnisite/slovnik/bss/)) se Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v mobilních sítích 2G a 3G. Rozhraní Gb přenáší signalizaci i uživatelská data pro služby GPRS a [EDGE](/mobilnisite/slovnik/edge/) a BECN funguje konkrétně v transportní vrstvě tohoto rozhraní založené na Frame Relay. Když dojde k zahlcení ve směru downlink (od SGSN k BSS), BECN poskytuje standardizovanou metodu, jak BSS může notifikovat SGSN o stavu zahlcení, což umožňuje koordinované řízení provozu mezi síťovými prvky.

Mechanismus BECN funguje prostřednictvím bitů pro signalizaci zahlcení v hlavičce protokolu Frame Relay. Když BSS detekuje zahlcení ve svých vyrovnávacích pamětech nebo přenosových frontách pro downlinkový provoz, nastaví bit Backward Explicit Congestion Notification v hlavičce Frame Relay rámců putujících v opačném směru (z BSS do SGSN). Tento zpětný způsob notifikace je zásadní, protože zahlcení typicky nastává na přijímací straně (BSS), ale řízení provozu musí být implementováno na straně odesílající (SGSN). Bit BECN je přenášen v poli Data Link Connection Identifier ([DLCI](/mobilnisite/slovnik/dlci/)) hlavičky Frame Relay, konkrétně v adresním poli, kde jsou bity pro řízení zahlcení definovány podle standardů Frame Relay.

Při přijetí rámců s nastaveným bitem BECN SGSN tuto informaci interpretuje jako indikaci zahlcení na downlinkové cestě k BSS. SGSN pak může implementovat různé mechanismy reakce na zahlcení, typicky zahrnující snížení přenosové rychlosti nebo tvarování provozu pro postižená spojení. Konkrétní reakční algoritmy závisí na implementaci, ale obecně se řídí principy postupného snižování rychlosti, aby se zahlcení zmírnilo bez náhlého přerušení služby. SGSN může snížit přenosovou rychlost pro konkrétní Packet Data Protocol (PDP) kontexty nebo aplikovat obecnější omezení provozu pro veškerý provoz směřující do zahlceného BSS.

BECN funguje ve spojení s Forward Explicit Congestion Notification ([FECN](/mobilnisite/slovnik/fecn/)), která poskytuje signalizaci zahlcení ve směru dopředném. Zatímco FECN informuje přijímací stranu (BSS) o zahlcení ve směru uplink, BECN se specificky zabývá kritičtějším scénářem zahlcení v downlinku, kde tok provozu řídí SGSN. Kombinace BECN a FECN vytváří obousměrný systém řízení zahlcení pro rozhraní Gb. Účinnost BECN závisí na správné implementaci reakčních mechanismů v SGSN a vhodných algoritmech detekce zahlcení v BSS, což z něj činí kooperativní schéma řízení zahlcení spíše než povinný mechanismus regulace provozu.

Architektura podporující BECN zahrnuje více vrstev protokolů: na fyzické vrstvě rozhraní Gb typicky využívá linky E1/T1; na spojové vrstvě Frame Relay poskytuje možnosti signalizace zahlcení; a na síťové vrstvě [BSSGP](/mobilnisite/slovnik/bssgp/) (BSS GPRS Protocol) spravuje vlastní GPRS provoz. BECN funguje na vrstvě Frame Relay, což jej činí transparentním pro vyšší protokolové vrstvy, ale zároveň je nezbytný pro udržení efektivity transportu. Mezi klíčové komponenty patří Frame Relay přepínače v přenosové síti, mechanismy detekce zahlcení v BSS a funkce řízení provozu v SGSN. BECN hraje klíčovou roli v předcházení přetečení vyrovnávacích pamětí v BSS, snižování ztrátovosti paketů a udržování kvality služeb pro uživatele mobilních dat.

## K čemu slouží

BECN byl vytvořen, aby řešil základní výzvu řízení zahlcení v paketových mobilních sítích, konkrétně pro rozhraní Gb v systémech 2G a 3G. Před standardizovanými mechanismy signalizace zahlcení měly síťové prvky omezený přehled o podmínkách zahlcení na sousedních uzlech, což vedlo k neefektivnímu zacházení s provozem, zvýšeným ztrátám paketů a zhoršenému uživatelskému zážitku. Transport Frame Relay na rozhraní Gb představoval specifické výzvy, protože postrádal vlastní mechanismy řízení zahlcení, a vyžadoval tedy explicitní signalizační schémata pro koordinaci řízení provozu mezi SGSN a [BSS](/mobilnisite/slovnik/bss/).

Primární problém, který BECN řeší, je asymetrická povaha detekce a řízení zahlcení v mobilních sítích. Zahlcení typicky nastává na přijímacím uzlu (BSS), když downlinkový provoz překročí jeho kapacitu zpracování nebo přenosu, ale řízení provozu musí být implementováno na vysílacím uzlu (SGSN). Bez BECN by SGSN nemělo přímou indikaci zahlcení na straně BSS a mohlo by potenciálně pokračovat v přenosu dat, která by byla zahozena, což by plýtvalo síťovými zdroji a degradovalo kvalitu služby. BECN poskytuje nezbytný zpětnovazební mechanismus, který umožňuje uzavřenou smyčku řízení zahlcení.

Historický kontext ukazuje, že rané implementace [GPRS](/mobilnisite/slovnik/gprs/) trpěly neefektivním zvládáním zahlcení, což vedlo k suboptimálnímu využití zdrojů a špatnému uživatelskému zážitku během špičkového provozu. Technologie Frame Relay používaná pro transport rozhraní Gb zahrnovala ve své specifikaci možnosti signalizace zahlcení, ale 3GPP potřebovalo definovat, jak budou tyto možnosti využity v kontextu mobilní sítě. BECN spolu s FECN představovaly standardizaci osvědčených postupů pro řízení zahlcení, což zajišťovalo interoperabilitu mezi zařízeními různých výrobců a konzistentní výkon sítě. Tento mechanismus řešil omezení předchozích přístupů, které se spoléhaly pouze na správu vyrovnávacích pamětí nebo prosté zahazování paketů, a poskytoval sofistikovanější systém řízení zahlcení s přehledem o síti.

## Klíčové vlastnosti

- Signalizace zahlcení založená na Frame Relay využívající vyhrazené bity v hlavičce
- Zpětný směr notifikace (z BSS do SGSN) pro řízení zahlcení v downlinku
- Integrace s mechanismy tvarování provozu a řízení rychlosti v SGSN
- Spolupráce s Forward Explicit Congestion Notification (FECN)
- Transparentnost pro vyšší protokolové vrstvy jako BSSGP a IP
- Reakční algoritmy závislé na implementaci umožňující optimalizaci výrobcem

## Související pojmy

- [FECN – Forward Explicit Congestion Notification](/mobilnisite/slovnik/fecn/)
- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [BECN na 3GPP Explorer](https://3gpp-explorer.com/glossary/becn/)
