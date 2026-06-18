---
slug: "utc"
url: "/mobilnisite/slovnik/utc/"
type: "slovnik"
title: "UTC – Coordinated Universal Time"
date: 2026-01-01
abbr: "UTC"
fullName: "Coordinated Universal Time"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/utc/"
summary: "Coordinated Universal Time (UTC, koordinovaný světový čas) je primární celosvětový časový standard, založený na mezinárodním atomovém čase (TAI) s přidávanými přestupnými sekundami pro soulad s univer"
---

UTC je primární celosvětový časový standard používaný v 3GPP pro synchronizaci sítě, časové značkování a zajištění konzistentního měření času v globálních telekomunikačních systémech.

## Popis

Coordinated Universal Time (UTC, koordinovaný světový čas) je globální časový standard spravovaný Mezinárodním úřadem pro míry a váhy (BIPM), který kombinuje stabilitu atomového času s úpravami pro soulad s rotací Země. Je odvozen od mezinárodního atomového času ([TAI](/mobilnisite/slovnik/tai/)), který je generován souborem atomových hodin po celém světě, ale zahrnuje periodicky vkládané nebo vynechávané přestupné sekundy, aby se udržel v rozmezí 0,9 sekundy od univerzálního času [UT1](/mobilnisite/slovnik/ut1/). Tento hybridní přístup zajišťuje, že UTC slouží jak vědeckým potřebám pro jednotný čas, tak praktickým požadavkům na sladění se slunečním časem. Ve specifikacích 3GPP je UTC hojně používán pro synchronizaci sítě, časování protokolů a časové značkování napříč různými rozhraními a funkcemi. Je odkazováno v mnoha specifikacích, jako je 22.261 pro požadavky na služby, 36.331 pro řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a 29.345 pro systémy účtování, což zdůrazňuje jeho všudypřítomnou roli. UTC umožňuje přesnou koordinaci mezi síťovými prvky, jako jsou základnové stanice (např. gNB) a uzly jádra (např. [AMF](/mobilnisite/slovnik/amf/)), tím, že poskytuje společný časový referenční bod, který zabraňuje časovému úniku (driftu) a zajišťuje plynulé předávání spojení a konzistenci dat. Šíření UTC v telekomunikačních sítích často závisí na protokolech jako Network Time Protocol ([NTP](/mobilnisite/slovnik/ntp/)) nebo Precision Time Protocol ([PTP](/mobilnisite/slovnik/ptp/)), synchronizovaných z primárních referenčních zdrojů, jako je [GNSS](/mobilnisite/slovnik/gnss/) nebo národní časové laboratoře. To zajišťuje, že všechny síťové komponenty, od uživatelského zařízení (UE) po datová centra, pracují na synchronizované časové ose, což je klíčové pro aplikace jako účtování, bezpečnostní logování a služby v reálném čase. Integrace UTC do standardů 3GPP podporuje interoperabilitu mezi různými operátory a regiony, usnadňuje globální roaming a konzistentní poskytování služeb.

## K čemu slouží

UTC existuje za účelem poskytnutí globálně přijímaného časového standardu, který vyvažuje přesnost atomových hodin s časem rotace Země, a řeší tak potřebu konzistentního měření času v mezinárodní telekomunikaci. Řeší problém časového úniku (driftu) mezi atomovým časem a slunečním časem začleněním přestupných sekund, čímž zajišťuje, že síťové operace zůstávají sladěny s lidskými aktivitami a astronomickými jevy. Historicky byl UTC zaveden v 60. letech 20. století jako náhrada za Greenwich Mean Time ([GMT](/mobilnisite/slovnik/gmt/)), nabízející přesnější a vědecky robustnější referenci pro celosvětovou koordinaci. V 3GPP, počínaje Release 4, byl UTC přijat jako základní časová reference pro synchronizaci sítě, což umožnilo přesné časové značkování pro protokoly, záznamy o účtování a bezpečnostní funkce. Tato motivace vychází z rostoucí složitosti mobilních sítí, které vyžadují harmonizovaný čas napříč různými prvky pro podporu funkcí, jako je zákonné odposlouchávání, správa kvality služeb (QoS) a lokalizační služby. Použitím UTC mohou systémy 3GPP dosáhnout časové konzistence, snížit chyby při předávání spojení, nesrovnalosti v účtování a výpadky služeb, čímž se zvyšuje celková spolehlivost sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Globální časový standard založený na atomovém čase s přestupnými sekundami
- Zajišťuje synchronizaci sítě napříč systémy 3GPP
- Používá se pro časové značkování v protokolech a účtování
- Podporuje interoperabilitu a globální roaming
- Šířen v sítích prostřednictvím NTP, PTP nebo GNSS
- Kritický pro bezpečnostní logování a zákonné odposlouchávání

## Související pojmy

- [UT – Universal Time](/mobilnisite/slovnik/ut/)
- [UT1 – Universal Time No.1](/mobilnisite/slovnik/ut1/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [UTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/utc/)
