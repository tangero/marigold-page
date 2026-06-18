---
slug: "sfr"
url: "/mobilnisite/slovnik/sfr/"
type: "slovnik"
title: "SFR – Security Functional Requirements"
date: 2025-01-01
abbr: "SFR"
fullName: "Security Functional Requirements"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sfr/"
summary: "SFR definuje povinné bezpečnostní funkce a schopnosti, které musí síťové prvky a uživatelská zařízení implementovat pro zajištění bezpečného systému 3GPP. Poskytuje standardizovaný základní rámec pro"
---

SFR je soubor povinných bezpečnostních funkcí a schopností, které musí síťové prvky a uživatelská zařízení implementovat, aby byl zajištěn bezpečný a interoperabilní systém 3GPP.

## Popis

Požadavky na bezpečnostní funkce (Security Functional Requirements, SFR) představují základní soubor specifikací v rámci bezpečnostní architektury 3GPP. Nejde o jeden konkrétní protokol nebo rozhraní, ale o komplexní soubor povinných bezpečnostních schopností. Tyto požadavky jsou definovány v různých technických specifikacích (TS) a jsou aplikovány na síťové funkce, uživatelská zařízení (UE) a rozhraní mezi nimi. Rámec SFR zajišťuje, že všechny kompatibilní implementace poskytují minimální, ověřitelnou úroveň zabezpečení, která pokrývá aspekty jako autentizace, ochrana integrity, důvěrnost a dostupnost. Požadavky jsou v principu nezávislé na konkrétní technologii, ale jsou podrobně rozpracovány pro konkrétní systémové architektury, jako jsou GSM, UMTS, LTE a 5G.

SFR fungují tak, že jsou integrovány do normativních specifikací pro každý síťový prvek a protokol. Například specifikace pro protokoly přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) a ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) obsahují klauzule odkazující na SFR, které ukládají povinnost používat konkrétní šifrovací algoritmy (jako 128-EEA3) nebo integritní algoritmy (jako 128-EIA3) pro 5G. Podobně specifikace pro síťové funkce jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) nebo [UPF](/mobilnisite/slovnik/upf/) obsahují SFR podrobně popisující požadavky na bezpečné ukládání klíčů, ochranu proti replay útokům a bezpečné logování. Soulad je ověřován prostřednictvím konformních testů, kde je zařízení testováno vůči těmto povinným funkcím.

Klíčové součásti rámce SFR zahrnují požadavky na důvěrnost identity uživatele, autentizaci entit, důvěrnost dat, integritu dat a nepopiratelnost. Ty jsou dále rozčleněny na konkrétní technické povinnosti. Například požadavky na autentizaci entit podrobně popisují potřebu vzájemného ověření mezi UE a sítí pomocí sady protokolů [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement). Požadavky na důvěrnost dat specifikují potřebu šifrování provozu uživatelské a řídicí roviny přes rozhraní rádiového přístupu a uvnitř core sítě. Úlohou SFR je poskytovat soudržný základní bezpečnostní rámec, který brání dodavatelům nebo operátorům v nasazování systémů s kritickými bezpečnostními mezerami a zajišťuje, že se bezpečnost vyvíjí současně s novými síťovými funkcemi a hrozbami.

## K čemu slouží

Účelem požadavků na bezpečnostní funkce (SFR) je stanovit povinný, standardizovaný bezpečnostní základ pro všechny systémy 3GPP. Před jejich formalizací mohly být implementace zabezpečení nekonzistentní, přičemž dodavatelé mohli z důvodu nákladů nebo výkonu vynechat určité ochrany, což vedlo ke zranitelnostem a problémům s interoperabilitou. Rámec SFR byl vytvořen, aby tento problém vyřešil definováním nezbytné sady bezpečnostních funkcí, které musí každý kompatibilní produkt implementovat. Tím je zajištěna základní úroveň důvěry a zabezpečení v celém ekosystému, od čipových sad v telefonech po servery core sítě.

Historicky, jak se mobilní technologie vyvíjela od 2G (GSM) k 3G (UMTS), se bezpečnost stala složitější a kritičtější. Zabezpečení GSM mělo známé slabiny, jako je jednosměrná autentizace a slabé šifrovací algoritmy. Zavedení SFR v rámci 3GPP, zejména od Release 9 dále, poskytlo strukturovaný způsob, jak zavést povinnost silnější, vzájemné autentizace a robustnějších kryptografických algoritmů. Řešilo to omezení ad-hoc bezpečnostních implementací tím, že poskytlo jasný, specifikacemi řízený kontrolní seznam. Motivací pro to byla rostoucí hodnota mobilních dat, nástup mobilního obchodu a rostoucí sofistikovanost útoků na telekomunikační infrastrukturu.

SFR dále umožňují dodržování regulatorních požadavků a certifikaci (např. pro vládní nebo kritickou infrastrukturu) tím, že poskytují jasnou sadu technických kritérií, vůči kterým lze systémy hodnotit. Zajišťují, že nové funkce zaváděné v pozdějších releasech, jako je síťové dělení (network slicing) v 5G nebo služby blízkosti ([ProSe](/mobilnisite/slovnik/prose/)), jsou od počátku budovány na bezpečném základu, přičemž pro tyto nové schopnosti jsou definovány konkrétní SFR, aby se zabránilo tomu, že bude bezpečnost řešena až dodatečně.

## Klíčové vlastnosti

- Ukládá povinnost vzájemné autentizace mezi UE a sítí pomocí protokolů AKA
- Specifikuje požadavky na šifrovací algoritmy pro zajištění důvěrnosti dat na uživatelské a řídicí rovině
- Definuje mechanismy ochrany integrity pro zabránění manipulaci se signalizačními zprávami
- Zahrnuje požadavky na důvěrnost identity uživatele (např. skrytí SUCI v 5G)
- Ukládá povinnost bezpečné správy a ukládání klíčů uvnitř síťových funkcí a UE
- Poskytuje rámec pro zajištění bezpečnosti a konformní testování

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 26.150** (Rel-19) — Syndicated Feed Reception (SFR) Specification
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [SFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfr/)
