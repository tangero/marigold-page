---
slug: "hi"
url: "/mobilnisite/slovnik/hi/"
type: "slovnik"
title: "HI – Handover Interface"
date: 2025-01-01
abbr: "HI"
fullName: "Handover Interface"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hi/"
summary: "Rozhraní předávání (HI) je standardizované rozhraní definované 3GPP pro výměnu informací mezi orgány činnými v trestním řízení (LEA) a telekomunikačními sítěmi. Umožňuje zákonné odposlechy, což pověře"
---

HI je standardizované rozhraní 3GPP mezi telekomunikačními sítěmi a orgány činnými v trestním řízení pro výměnu informací umožňující zákonné odposlechy.

## Popis

Rozhraní předávání (HI) je klíčovou součástí architektury zákonných odposlechů 3GPP. Slouží jako standardizovaný komunikační spoj mezi infrastrukturou pro odposlech provozovatele sítě a monitorovacím zařízením orgánu činného v trestním řízení ([LEA](/mobilnisite/slovnik/lea/)). HI není jediným fyzickým portem, ale logickým rozhraním zahrnujícím sadu protokolů, datových formátů a mechanismů doručení definovaných v technických specifikacích, jako jsou TS 33.107 a TS 33.108. Jeho hlavní funkcí je přenos zachyceného komunikačního obsahu ([CC](/mobilnisite/slovnik/cc/)) a informací souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) z mediační funkce ([MF](/mobilnisite/slovnik/mf/)) sítě do sběrné funkce ([CF](/mobilnisite/slovnik/cf/)) LEA.

HI funguje na základě modelu požadavek-odpověď iniciovaného LEA. Po zákonném pověření LEA odešle prostřednictvím rozhraní [HI1](/mobilnisite/slovnik/hi1/) (administrativní rozhraní) provozovateli sítě žádost o odposlech. Po aktivaci začne cílový uzel sítě (např. [MSC](/mobilnisite/slovnik/msc/), [SGSN](/mobilnisite/slovnik/sgsn/) nebo PGW) generovat data IRI a CC. Tato data jsou mediační funkcí zpracována a naformátována podle specifikací HI. Samotné doručení zachycených dat k LEA probíhá přes rozhraní HI2 a HI3. HI2 je určeno pro doručování IRI, které zahrnuje metadata, jako jsou časy navázání hovoru, identity účastníků a informace o poloze. HI3 je určeno pro doručování CC, což je skutečný hlasový, datový nebo zprávový obsah.

Architektura HI zajišťuje bezpečné, spolehlivé a standardizované doručení. Definuje požadavky na kódování dat, jejich řazení a časové značky pro zachování důkazní integrity. Jsou vyžadována bezpečnostní opatření včetně šifrování a zabezpečených transportních protokolů, aby byla chráněna citlivá zachycená data během přenosu. Role HI je klíčová pro oddělení odposlechových schopností sítě od sběrných systémů LEA, poskytuje jasný demarkační bod, který zajišťuje soulad s právními rámci při zachování bezpečnosti sítě a provozní nezávislosti.

## K čemu slouží

HI bylo vytvořeno, aby řešilo rostoucí potřebu standardizované, bezpečné a právně konformní metody pro zákonné odposlechy v globálních telekomunikačních sítích. Před jeho standardizací byly odposlechové mechanismy často proprietární, specifické pro danou zemi nebo neexistovaly, což vytvářelo výzvy pro orgány činné v trestním řízení působící přes hranice a pro provozovatele sítí spravující více-dodavatelská prostředí. Nedostatek standardizace bránil interoperabilitě a zvyšoval náklady a složitost implementace odposlechových schopností.

Zavedení HI ve 3GPP Release 8 poskytlo jednotný rámec. Řeší problém, jak spolehlivě a bezpečně doručit zachycená data z jakékoli kompatibilní sítě 3GPP (od 3G UMTS dále) do jakéhokoli kompatibilního systému LEA. Jeho vytvoření bylo motivováno právními požadavky v mnoha jurisdikcích, které ukládají telekomunikačním poskytovatelům povinnost pomáhat při zákonných odposleších pro národní bezpečnost, trestní vyšetřování a nouzové situace. HI zajišťuje, že tato pomoc může být poskytována efektivně bez ohrožení základní funkčnosti nebo bezpečnosti sítě a že shromážděné důkazy jsou formátovány a doručovány konzistentním a přijatelným způsobem.

## Klíčové vlastnosti

- Standardizované logické rozhraní pro doručování dat zákonných odposlechů
- Odděluje doručování komunikačního obsahu (HI3) a informací souvisejících s odposlechem (HI2)
- Definuje zabezpečené transportní protokoly a požadavky na šifrování dat
- Specifikuje formátování dat, jejich řazení a časové značky pro důkazní integritu
- Poskytuje jasnou demarkaci mezi systémy provozovatele sítě a orgánů činných v trestním řízení
- Podporuje interoperabilitu mezi různými dodavateli sítí a zařízeními LEA

## Související pojmy

- [HI1 – Handover Interface Port 1 (for Administrative Information)](/mobilnisite/slovnik/hi1/)
- [HI2 – Handover Interface Port 2](/mobilnisite/slovnik/hi2/)
- [HI3 – Handover Interface Port 3](/mobilnisite/slovnik/hi3/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [HI na 3GPP Explorer](https://3gpp-explorer.com/glossary/hi/)
