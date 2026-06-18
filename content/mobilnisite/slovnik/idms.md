---
slug: "idms"
url: "/mobilnisite/slovnik/idms/"
type: "slovnik"
title: "IDMS – Inter-destination Multimedia Synchronization"
date: 2025-01-01
abbr: "IDMS"
fullName: "Inter-destination Multimedia Synchronization"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/idms/"
summary: "Služební prvek, který zajišťuje synchronizované přehrávání multimediálního obsahu na více zařízeních nebo v cílových místech. Je klíčový pro poskytování konzistentních vysoce kvalitních zážitků ve sku"
---

IDMS je služební prvek, který zajišťuje synchronizované přehrávání multimediálního obsahu na více zařízeních nebo v cílových místech pro konzistentní zážitek při skupinové komunikaci a ve víceobrazovkových aplikacích.

## Popis

Inter-destination Multimedia Synchronization (IDMS) je služební schopnost definovaná 3GPP pro koordinaci časování prezentace mediálních streamů na více přijímacích koncových bodech, jako jsou chytré telefony, tablety nebo televizory. Funguje v rámci architektury 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)), využívá protokoly aplikační vrstvy a podporu sítě pro dosažení přesné synchronizace. Základní mechanismus zahrnuje Synchronizačního klienta na každém přijímacím zařízení, který si vyměňuje časové informace s centrálním Synchronizačním serverem nebo s ostatními klienty pomocí protokolů jako rozšíření [RTP](/mobilnisite/slovnik/rtp/) a [RTCP](/mobilnisite/slovnik/rtcp/) nebo vyhrazeného signalizace na aplikační vrstvě. Systém měří a kompenzuje síťová zpoždění a rozdíly v hodinách zařízení, aby zarovnal přehrávání a zajistil, aby všichni uživatelé zaznamenali události, jako jsou video snímky nebo zvukové signály, současně.

Architektonicky lze IDMS implementovat centralizovaně, distribuovaně nebo hybridně. V centralizovaném modelu server shromažďuje časové hlášení od všech klientů, vypočítává potřebné úpravy a distribuuje synchronizační příkazy. V distribuovaném nebo peer-to-peer asistovaném modelu si klienti přímo mezi sebou vyměňují časové informace, aby dosáhli shody. Síť 5G může poskytnout vylepšení kvality služeb (QoS) a podporu komunikace s nízkou latencí, aby usnadnila IDMS, ale samotná synchronizační logika je primárně funkcí aplikační vrstvy. Mezi klíčové komponenty patří Synchronizační manažer, který řídí synchronizační strategii, a Mediální přehrávače, které upravují své přehrávací buffery na základě přijatých synchronizačních podnětů.

IDMS hraje klíčovou roli při umožnění imerzivních a sociálních mediálních služeb. Zajišťuje, že uživatelé na různých místech sledující stejný živý přenos zažívají události ve stejný čas, což je zásadní pro aplikace jako živé sportovní přenosy, koncerty nebo interaktivní hraní. Technologie také podporuje synchronizaci napříč heterogenními zařízeními s různými výpočetními schopnostmi a síťovými podmínkami, dynamicky se přizpůsobuje, aby udržela zarovnání. Poskytnutím této synchronizace IDMS zvyšuje zapojení uživatelů a umožňuje nové obchodní modely pro poskytovatele obsahu a provozovatele služeb v ekosystému 5G.

## K čemu slouží

IDMS byl vytvořen, aby řešil rostoucí poptávku po synchronizovaných multimediálních zážitcích na více zařízeních a v různých lokalitách, kterou pohání nárůst sociálního sledování a víceobrazovkových aplikací. Před jeho standardizací byla řešení často proprietární, roztříštěná a nedokázala garantovat konzistentní synchronizaci, zejména v různorodých sítích jako 5G, Wi-Fi nebo pevný broadband. Tento nedostatek interoperability bránil vývoji škálovatelných služeb napříč platformami.

Primární problém, který IDMS řeší, je časové nesoulad přehrávání médií, který může zničit sdílené zážitky. Například při živém sportovním přenosu pro více diváků mohou i malá zpoždění způsobit spoilery nebo narušit sociální interakci. IDMS poskytuje standardizovaný rámec pro měření síťové latence, odchylek hodin zařízení a zpracovatelských zpoždění a následně aplikuje korekce pro synchronizaci přehrávání. To zajišťuje, že všichni uživatelé vnímají mediální události současně, což zvyšuje kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

Motivováno potřebou bohatších mediálních služeb v 5G zavedla 3GPP IDMS ve verzi Release 16 jako součást vylepšení [5GMS](/mobilnisite/slovnik/5gms/). Umožňuje poskytovatelům služeb nabízet synchronizované doručování obsahu jako diferenciovanou funkci, podporující aplikace jako sledovací party, kolaborativní virtuální realitu a synchronizovanou reklamu. Standardizací IDMS 3GPP podporuje interoperabilitu a snižuje vývojové náklady, což umožňuje konzistentní implementaci napříč sítěmi a zařízeními.

## Klíčové vlastnosti

- Synchronizace časování přehrávání na více koncových bodech
- Podpora centralizovaných, distribuovaných a hybridních synchronizačních architektur
- Využití rozšíření RTP/RTCP a signalizace na aplikační vrstvě pro výměnu časových informací
- Kompensace síťové latence, jitteru a rozdílů v hodinách zařízení
- Integrace s architekturou 5G Media Streaming (5GMS) pro vylepšenou podporu QoS
- Dynamické přizpůsobení se měnícím se síťovým podmínkám a schopnostem zařízení

## Související pojmy

- [5GMS – 5G Media Streaming](/mobilnisite/slovnik/5gms/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 28.312** (Rel-19) — Intent Driven Management for Service/Network Mgmt
- **TR 28.914** (Rel-19) — Intent Driven Management Service Study Phase 3

---

📖 **Anglický originál a plná specifikace:** [IDMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/idms/)
