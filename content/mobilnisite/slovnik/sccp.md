---
slug: "sccp"
url: "/mobilnisite/slovnik/sccp/"
type: "slovnik"
title: "SCCP – Signalling Connection Control Part"
date: 2025-01-01
abbr: "SCCP"
fullName: "Signalling Connection Control Part"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sccp/"
summary: "Protokol síťové vrstvy v rámci signalizačních architektur SS7 a SIGTRAN, poskytující spojované i nespojované služby. Umožňuje směrování signalizačních zpráv mezi síťovými uzly (jako MSC a HLR) na zákl"
---

SCCP je protokol síťové vrstvy v SS7 a SIGTRAN, který poskytuje spojované i nespojované služby pro směrování signalizačních zpráv mezi síťovými uzly s využitím čísel subsystémů a překladu globálního názvu.

## Popis

Signalling Connection Control Part (SCCP) je klíčový protokol vrstvy 4 (transportní vrstvy) v zásobníku protokolů [SS7](/mobilnisite/slovnik/ss7/) (Signalling System No. 7), definovaný [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatý 3GPP pro signalizaci v jádru sítě. Nachází se nad Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)) úrovně 3, která poskytuje základní směrování zpráv na základě směrovacích kódů. SCCP rozšiřuje MTP poskytováním dvou klíčových služeb: nespojované služby (třída 0 a 1) pro signalizaci v režimu datagramů a spojované služby (třída 2 a 3) pro spolehlivý přenos dat v pořadí, analogicky virtuálnímu okruhu.

Z architektonického hlediska zavádí SCCP dva hlavní adresní mechanismy nad rámec cílového směrovacího kódu ([DPC](/mobilnisite/slovnik/dpc/)) MTP. Jsou to čísla subsystémů ([SSN](/mobilnisite/slovnik/ssn/)) a globální názvy ([GT](/mobilnisite/slovnik/gt/)). SSN identifikuje konkrétní aplikaci v rámci uzlu (např. SSN=6 pro [HLR](/mobilnisite/slovnik/hlr/), SSN=8 pro [MSC](/mobilnisite/slovnik/msc/)). Globální název je adresa, jako je E.164 MSISDN nebo IMSI, která se přímo nepřevádí na síťový směrovací kód. Klíčovou funkcí SCCP je překlad globálního názvu (GTT), který spočívá v dotazování databáze za účelem převodu GT na kombinaci DPC a SSN, což umožňuje flexibilní směrování založené na cíli nezávislé na fyzické topologii sítě. To umožňuje směrovat signalizační zprávy ke správné síťové entitě (jako je HLR) na základě čísla účastníka.

Při provozu, například pro nespojovanou transakci jako aktualizace polohy, odešle MSC zprávu SCCP Unitdata obsahující IMSI účastníka jako globální název. Signal Transfer Point (STP) provede GTT, převede IMSI na DPC a SSN příslušného HLR a zprávu přepošle. Pro spojované služby SCCP spravuje navázání spojení, přenos dat s řízením pořadí a uvolnění spojení. To se používá pro transakce vyžadující dialog, například mezi MSC a EIR. V rámci sítí 3GPP slouží SCCP jako transport pro protokoly vyšších vrstev, jako je TCAP (Transaction Capabilities Application Part), který nese zprávy MAP (Mobile Application Part) a CAP (CAMEL Application Part), a tvoří tak páteř veškeré signalizace nesouvisející s okruhy.

## K čemu slouží

SCCP byl vytvořen, aby řešil omezení základního směrování MTP v sítích SS7. Směrování MTP je založeno výhradně na statických směrovacích kódech, které reprezentují fyzické síťové uzly. Tento model je nepružný pro rozsáhlé, distribuované a na účastníka orientované sítě, jako jsou GSM/UMTS, kde je třeba směrovat signalizaci k logické databázi (jako je HLR) na základě identity účastníka, nikoli fyzického umístění dotazujícího se uzlu. Schopnost SCCP pracovat s globálním názvem tento problém vyřešila oddělením logického adresování od fyzického směrování.

Dalším klíčovým problémem, který řešil, byla potřeba jak jednoduché signalizace typu dotaz-odpověď, tak rozšířené signalizace orientované na dialog. MTP poskytuje pouze nespojovanou službu bez řízení pořadí. SCCP zavedl spojované služby s řízením toku a doručováním v pořadí, které jsou nezbytné pro určité složité transakce a pro správu signalizačních spojení v rozvíjejících se síťových architekturách. To poskytlo spolehlivý transport vyžadovaný pro služby pokročilé inteligentní sítě (AIN) a databázové dotazy.

Jeho přijetí 3GPP bylo motivováno potřebou robustního, standardizovaného signalizačního transportu pro protokol Mobile Application Part (MAP), který zajišťuje veškerou správu mobility, směrování hovorů a výměnu dat o účastnících. SCCP umožnil škálovatelné, hierarchické a globálně interoperabilní jádro sítě, které zajistilo úspěch GSM a následných technologií 3GPP, a umožnil účastníkům celosvětový roaming tím, že zajistil, aby signalizační zprávy našly cestu ke správným databázím domovské sítě.

## Klíčové vlastnosti

- Poskytuje jak nespojované (UDT), tak spojované služby
- Umožňuje adresování a směrování pomocí globálního názvu (GTT) pro logické cílové směrování
- Používá čísla subsystémů (SSN) k identifikaci konkrétních aplikací v rámci uzlu
- Podporuje segmentaci a opětovné složení dlouhých signalizačních zpráv
- Nabízí doručování v pořadí a řízení toku pro spojované služby
- Slouží jako transportní vrstva pro protokoly TCAP, MAP a CAP

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sccp/)
