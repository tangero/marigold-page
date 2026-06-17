---
slug: "mtp3-b"
url: "/mobilnisite/slovnik/mtp3-b/"
type: "slovnik"
title: "MTP3-B – Message Transfer Part level 3 (for Q.2140)"
date: 2025-01-01
abbr: "MTP3-B"
fullName: "Message Transfer Part level 3 (for Q.2140)"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mtp3-b/"
summary: "MTP3-B je protokolová vrstva v signalizačním systému 3GPP, specificky přizpůsobená pro adaptační vrstvu Q.2140 používanou ve signalizaci B-ISDN User Part (B-ISUP). Poskytuje spolehlivý, nespojový přen"
---

MTP3-B je protokol Message Transfer Part úrovně 3 přizpůsobený pro Q.2140, který zajišťuje nespojové směrování a spolehlivý přenos signalizačních zpráv přes ATM přenos v jádrových sítích 3GPP.

## Popis

MTP3-B (Message Transfer Part level 3 Broadband) je klíčový protokol v signalizační architektuře 3GPP, definovaný pro použití přes přenosové sítě [ATM](/mobilnisite/slovnik/atm/) (Asynchronous Transfer Mode). Funguje jako síťová vrstva v rámci Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)) signalizačního systému, nachází se nad [MTP2](/mobilnisite/slovnik/mtp2/) (vrstvou datového spoje) a pod adaptační vrstvou Q.2140. Jeho primární funkcí je zajišťovat směrování, rozlišování a distribuci signalizačních zpráv mezi různými síťovými uzly, jako jsou Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)) a Gateway MSC. Na rozdíl od své úzkopásmové varianty ([MTP3](/mobilnisite/slovnik/mtp3/)) je MTP3-B optimalizován pro vysokorychlostní, spojově orientovanou povahu ATM a podporuje Signalizační adaptační vrstvu ATM (SAAL), která zahrnuje Q.2140 a [AAL5](/mobilnisite/slovnik/aal5/).

Architektonicky rozhraní MTP3-B komunikuje s vrstvou Q.2140, která adaptuje služby MTP3-B na podkladovou ATM síť. Klíčové komponenty MTP3-B zahrnují funkci zpracování signalizačních zpráv, zodpovědnou za směrování zpráv na základě cílových a zdrojových kódů bodů, a funkci správy signalizační sítě, která řeší řízení zahlcení, správu tras a obnovu po poruše, aby byla zajištěna spolehlivost signalizační sítě. Spravuje signalizační spoje, sady signalizačních spojů a signalizační trasy a poskytuje mechanismy pro sdílení zátěže a přesměrování v případě poruchy spoje.

Během provozu přijímá MTP3-B signalizační zprávy od aplikací vyšších vrstev (jako je B-ISUP) přes servisní rozhraní Q.2140. Zkoumá směrovací pole uvnitř každé zprávy, které obsahuje cílový kód bodu ([DPC](/mobilnisite/slovnik/dpc/)), zdrojový kód bodu (OPC) a pole výběru signalizačního spoje (SLS). Na základě tohoto pole MTP3-B určí příslušný signalizační spoj nebo sadu spojů, přes kterou má zprávu předat k cíli. Zajišťuje doručování zpráv ve stejném pořadí na stejném signalizačním spoji a poskytuje základní detekci chyb prostřednictvím sekvenčních čísel. Jeho schopnosti správy sítě průběžně monitorují stav signalizačních tras a spojů a v případě zjištění poruchy iniciují procedury přechodu na alternativní cesty, čímž udržují kontinuitu služeb.

Role MTP3-B v síti 3GPP, zejména ve verzi Release 99 a raných verzích, byla zásadní pro signalizaci jádrové sítě přes ATM, což byla primární přenosová technologie pro rané sítě UMTS. Umožňoval kritické procedury, jako je navazování hovorů, předávání a uvolňování, spolehlivým přenosem zpráv B-ISUP mezi síťovými elementy. I když jeho význam poklesl s přechodem odvětví na IP přenos (např. SIGTRAN), představoval MTP3-B klíčový evoluční krok v přizpůsobení telekomunikační signalizace širokopásmovým přenosovým technologiím.

## K čemu slouží

MTP3-B byl vytvořen, aby rozšířil tradiční signalizaci SS7/C7 na širokopásmové [ATM](/mobilnisite/slovnik/atm/) sítě, které tvořily přenosovou páteř raných jádrových sítí UMTS 3G. Předchozí úzkopásmová signalizace (MTP3 přes TDM spoje) byla nedostatečná pro vysokou přenosovou kapacitu a spojově orientované požadavky ATM. Motivací bylo využít efektivitu ATM pro hlasové a datové služby při zachování robustního, spolehlivého signalizačního rámce SS7. MTP3-B spolu s Q.2140 poskytly standardizovanou adaptační vrstvu, která umožnila stávajícím signalizačním aplikacím (jako je ISUP) bezproblémově fungovat nad infrastrukturou ATM.

Tato technologie řešila problém integrace spojově orientované signalizace s paketově orientovaným přenosem, což byla klíčová výzva při přechodu na 3G. Odstraňovala omezení úzkopásmového MTP3, které bylo navrženo pro 64 kbps časové sloty a postrádalo nativní podporu pro virtuální spojení a buňkový přenos ATM. Definováním širokopásmové varianty umožnilo 3GPP operátorům nasadit signalizační spoje s vysokou kapacitou, které zvládly zvýšený signalizační provoz z nových služeb 3G, a podpořilo tak funkce jako videohovory a vysokorychlostní datová připojení.

Historicky byl MTP3-B součástí širší standardizace ITU-T pro signalizaci B-ISDN, kterou 3GPP přijalo pro jádrovou síť UMTS. Jeho vytvoření bylo motivováno potřebou budoucně odolného signalizačního systému, který by mohl škálovat s požadavky sítě. I když byl nakonec nahrazen IP protokoly SIGTRAN (jako M3UA) s přechodem odvětví na plně IP sítě, sehrál MTP3-B zásadní roli v počátečním nasazení a provozu služeb 3G, zajišťujíc zpětnou kompatibilitu a hladkou migrační cestu ze sítí 2G na 3G.

## Klíčové vlastnosti

- Nespojový přenos zpráv přes spojově orientovaný ATM přenos
- Směrování signalizačních zpráv na základě cílových a zdrojových kódů bodů
- Správa signalizační sítě pro řízení zahlcení a obnovu po poruše
- Podpora sdílení zátěže přes více signalizačních spojů
- Rozhraní s adaptační vrstvou Q.2140 pro mapování služeb ATM
- Zajištění doručování zpráv ve stejném pořadí na stejném signalizačním spoji

## Související pojmy

- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface

---

📖 **Anglický originál a plná specifikace:** [MTP3-B na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtp3-b/)
