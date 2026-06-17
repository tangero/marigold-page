---
slug: "hspa"
url: "/mobilnisite/slovnik/hspa/"
type: "slovnik"
title: "HSPA – High Speed Packet Access"
date: 2025-01-01
abbr: "HSPA"
fullName: "High Speed Packet Access"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hspa/"
summary: "Významné 3GPP vylepšení standardu UMTS/WCDMA, které výrazně zvyšuje rychlost paketových dat v downlinku a uplinku. Kombinuje HSDPA (High Speed Downlink Packet Access) a HSUPA (High Speed Uplink Packet"
---

HSPA je významné 3GPP vylepšení standardu UMTS/WCDMA, které kombinuje HSDPA a HSUPA a výrazně zvyšuje rychlost paketových dat v downlinku a uplinku pro mobilní širokopásmový přístup.

## Popis

High Speed Packet Access (HSPA) je soubor protokolů a technologií 3GPP pro rádiový přístupový síť, které dramaticky zvyšují datové schopnosti sítí UMTS (Universal Mobile Telecommunications System). Není to jedna technologie, ale zastřešující termín zahrnující [HSDPA](/mobilnisite/slovnik/hsdpa/) (High Speed Downlink Packet Access), představené ve verzi 5, a [HSUPA](/mobilnisite/slovnik/hsupa/) (High Speed Uplink Packet Access), představené ve verzi 6. HSPA pracuje na stávajících kmitočtových pásmech WCDMA, ale zavádí zásadní změny ve fyzické vrstvě a vrstvě řízení přístupu k médiu (Medium Access Control - [MAC](/mobilnisite/slovnik/mac/)), aby snížila latenci, zvýšila špičkové datové rychlosti a zlepšila spektrální účinnost pro paketově přepínané služby.

V jádru HSPA nahrazuje vyhrazený kanál (Dedicated Channel - [DCH](/mobilnisite/slovnik/dch/)) z verze 99 používaný pro datové služby přenosem na sdíleném kanálu. V downlinku (HSDPA) je používán High Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)), který je sdílen mezi více uživateli v časové a kódové doméně. Mezi klíčové umožňující technologie patří adaptivní modulace a kódování (Adaptive Modulation and Coding - [AMC](/mobilnisite/slovnik/amc/)), kde jsou modulační schéma (QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)) a kódovací rychlost dynamicky přizpůsobovány na základě kvality kanálu; hybridní automatické opakování (Hybrid Automatic Repeat Request - HARQ) s měkkým kombinováním pro rychlé retransmise na fyzické vrstvě; a rychlé plánování založené na Node B (základnové stanici), které činí rozhodnutí o plánování každý 2ms přenosový časový interval (Transmission Time Interval - TTI) namísto na RNC. Uplink (HSUPA) používá Enhanced Dedicated Channel (E-DCH) s podobnými vylepšeními, jako jsou kratší TTI, HARQ a plánování řízené Node B (pro povolení).

Z architektonického hlediska přesouvá HSPA klíčové zpracovatelské funkce z řadiče rádiové sítě (Radio Network Controller - RNC) do Node B. Pro HSDPA je nová entita MAC, MAC-hs, umístěna v Node B, aby zvládla rychlé plánování a HARQ. Tím se snižuje doba odezvy a umožňuje rychlejší reakce na měnící se rádiové podmínky. Evoluce HSPA (HSPA+) v pozdějších verzích zavedla další vylepšení, jako je MIMO (Multiple Input Multiple Output), modulace vyššího řádu (64QAM v uplinku, 64QAM/256QAM v downlinku), dvoukanálový a vícekanálový provoz a kontinuální paketová konektivita. Jejím úkolem bylo poskytnout nákladově efektivní, vysokovýkonnou platformu pro mobilní širokopásmový přístup, často popisovanou jako 3.5G, která prodloužila životní cyklus sítí UMTS a sloužila jako široce nasazený globální standard pro mobilní přístup k internetu před plným rozšířením 4G LTE.

## K čemu slouží

HSPA bylo vyvinuto, aby řešilo kritické nedostatky původní specifikace UMTS verze 99 pro paketové datové služby. Zatímco verze 99 zavedla paketové přepínání, její datové rychlosti byly omezené, latence byla vysoká kvůli centralizovanému plánování na RNC a bylo neefektivní pro přerušovaný, asymetrický internetový provoz. Rychlý růst využívání mobilního internetu na počátku 21. století vytvořil naléhavou potřebu vylepšení UMTS, které by mohlo poskytnout skutečný širokopásmový zážitek, konkurovat vznikajícím technologiím, jako je EV-DO, a položit základy pro budoucí mobilní aplikace.

Tato technologie tyto problémy vyřešila zásadní přestavbou rádiového rozhraní pro účinnost a rychlost. Zavedením přidělování zdrojů na sdíleném kanálu, rychlého plánování na Node B, AMC a HARQ výrazně zvýšila spektrální účinnost, propustnost pro uživatele a kapacitu sítě. Snížila latenci z více než 100 ms na desítky milisekund, což umožnilo responzivní interaktivní služby. Tato evoluce umožnila operátorům využít jejich stávající investice do spektra a infrastruktury WCDMA k nabídce konkurenceschopných vysokorychlostních datových služeb, jako je mobilní video, e-mail a prohlížení webu, bez nutnosti okamžité a nákladné migrace na novou technologii rádiového přístupu. Úspěch HSPA prokázal životaschopnost mobilního širokopásmového přístupu a poháněl poptávku, která nakonec vedla k vývoji LTE.

## Klíčové vlastnosti

- Provoz na sdíleném kanálu (HS-DSCH pro downlink, E-DCH pro uplink)
- Rychlé plánování na Node B s 2ms TTI
- Adaptivní modulace a kódování (QPSK, 16QAM, 64QAM)
- Hybridní ARQ (HARQ) s měkkým kombinováním na fyzické vrstvě
- Architektonický přesun funkcí MAC z RNC do Node B
- Evoluce na HSPA+ s MIMO, vícekanálovým provozem a modulací vyššího řádu

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.824** (Rel-8) — HSPA Evolution for 1.28Mcps TDD Study
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- **TR 37.976** (Rel-19) — MIMO OTA Test Methodology Study
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology
- **TS 48.008** (Rel-19) — BSS-MSC Interface Layer 3 Procedures

---

📖 **Anglický originál a plná specifikace:** [HSPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/hspa/)
