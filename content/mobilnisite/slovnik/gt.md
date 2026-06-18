---
slug: "gt"
url: "/mobilnisite/slovnik/gt/"
type: "slovnik"
title: "GT – Global Title"
date: 2025-01-01
abbr: "GT"
fullName: "Global Title"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gt/"
summary: "Adresa používaná v signalizaci SS7 pro směrování zpráv mezi síťovými uzly, pokud není znám point code konečného cíle. Je klíčovým identifikátorem pro entity jako HLR, SMSC a SCP a umožňuje globální ro"
---

GT (Global Title, globální číslo) je směrovací adresa používaná v signalizaci SS7 pro doručování zpráv síťovým entitám, jako jsou HLR nebo SMSC, pokud není znám jejich přímý point code, což umožňuje globální roaming a poskytování služeb.

## Popis

Global Title (GT, globální číslo) je klíčový adresní mechanismus v rámci sady protokolů Signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), který tvoří signalizační páteř tradičních telekomunikačních sítí včetně 2G, 3G a propojovacích funkcí 4G/5G. Na rozdíl od Point Code ([PC](/mobilnisite/slovnik/pc/)), což je lokální adresa signalizačního uzlu v rámci sítě, je GT globálně jednoznačná, volitelná adresa, která neobsahuje explicitní směrovací informace. Point Code si lze představit jako [PS](/mobilnisite/slovnik/ps/)Č pro signalizační přenosový bod ([STP](/mobilnisite/slovnik/stp/)), zatímco Global Title je jméno a adresa ulice příjemce. GT se používá, když odesílající signalizační bod nezná point code cíle. Zpráva je odeslána na STP, který provede Global Title Translation ([GTT](/mobilnisite/slovnik/gtt/)) a určí příslušný cílový point code a číslo subsystému pro konečné směrování.

Z architektonického hlediska je Global Title přenášen v poli Called Party Address zprávy Signalizační spojové řídicí části ([SCCP](/mobilnisite/slovnik/sccp/)). Struktura GT je definována standardy [ITU-T](/mobilnisite/slovnik/itu-t/) a [ANSI](/mobilnisite/slovnik/ansi/) a může být různých typů. V mobilních sítích je nejběžnější formát E.164, což je v podstatě mezinárodní telefonní číslo (např. MSISDN HLR). GT může také zahrnovat typ překladu, číslovací plán a kódovací schéma. Mezi klíčové síťové prvky adresované pomocí GT patří Home Location Register (HLR), Visitor Location Register (VLR), Mobile Switching Center (MSC), Short Message Service Center (SMSC) a Service Control Points (SCP) pro služby inteligentní sítě. Tyto prvky jsou často odkazovány svými čísly E.164, která fungují jako jejich GT.

Jak to funguje: Když uzel (např. MSC) potřebuje odeslat signalizační zprávu na HLR, ale zná pouze E.164 GT tohoto HLR (odvozené z IMSI/MSISDN účastníka), adresuje SCCP zprávu tímto GT. Zpráva je směrována na STP na základě směrovacích tabulek. STP zkontroluje GT a provede vyhledání ve své GTT databázi. Tento překlad mapuje GT na kombinaci Destination Point Code (DPC) a případně Subsystem Number (SSN). STP poté nahradí adresu pro směrování GT za DPC/SSN a přepošle zprávu do sítě SS7 pro konečné doručení skutečnému HLR. Tento proces umožňuje decentralizované, škálovatelné směrování bez nutnosti, aby každý uzel znal point codes všech možných cílových entit po celém světě, což je zásadní pro funkce jako roaming, doručování SMS a vyvolávání služeb.

## K čemu slouží

Global Title byl vytvořen, aby vyřešil zásadní problém škálovatelného, nepřímého směrování ve velkých, propojených signalizačních sítích, jako je SS7. Síť nemůže prakticky vyžadovat, aby každý signalizační bod znal přesný point code každé možné cílové entity na světě, zejména když sítě rostly a roaming se stal všudypřítomným. GT poskytuje úroveň nepřímosti a abstrakce. Umožňuje uzlům adresovat zprávy pomocí známého, logického identifikátoru (jako je číslo E.164), který zůstává stabilní, i když se změní fyzická topologie sítě nebo přiřazení point codes.

Historicky, před rozšířeným používáním GT, bylo směrování založeno výhradně na point codes, což omezovalo flexibilitu a škálovatelnost. Zavedení GT a doprovodné funkce GTT na STP revolučně změnilo signalizační architekturu. Umožnilo vývoj hierarchické, inteligentní směrovací vrstvy. To bylo obzvláště klíčové pro globální systém mobilních telekomunikací (GSM a následující generace), kde účastníci roamují mezi sítěmi a služby jako SMS nebo Camel vyžadují lokalizaci HLR účastníka nebo konkrétního servisního uzlu v cizí síti. GT je klíč, který tuto schopnost odemyká. Řeší omezení statického směrování založeného na point codes, které je závislé na topologii, tím, že poskytuje logickou, na službu orientovanou adresu, která může být překládána dynamicky, což usnadňuje globální interoperabilitu a komplexní servisní logiku moderních telekomunikačních sítí.

## Klíčové vlastnosti

- Globálně jednoznačná, logická adresa nezávislá na topologii sítě
- Běžně formátována jako číslo E.164 (mezinárodní telefonní číslo)
- Přenášena v poli SCCP Called Party Address
- Umožňuje nepřímé směrování prostřednictvím Global Title Translation (GTT) na STP
- Zásadní pro adresování HLR, SMSC a SCP v mobilních sítích
- Podporuje více číslovacích plánů a kódovacích schémat

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [GT na 3GPP Explorer](https://3gpp-explorer.com/glossary/gt/)
