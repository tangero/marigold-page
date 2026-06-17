---
slug: "ftam"
url: "/mobilnisite/slovnik/ftam/"
type: "slovnik"
title: "FTAM – File Transfer, Access and Management"
date: 2025-01-01
abbr: "FTAM"
fullName: "File Transfer, Access and Management"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ftam/"
summary: "Standardizovaná sada protokolů pro přenos a správu souborů v rámci síťových prvků 3GPP. Umožňuje spolehlivé, automatizované zacházení se soubory pro konfiguraci, softwarové aktualizace a sběr logů, co"
---

FTAM je standardizovaná sada protokolů pro přenos a správu souborů v rámci síťových prvků 3GPP, která umožňuje automatizované zacházení se soubory pro konfiguraci, aktualizace a logy nezbytné pro provoz a údržbu sítě.

## Popis

File Transfer, Access and Management (FTAM) je komplexní protokolový rámec definovaný 3GPP pro provádění operací se soubory napříč síťovými prvky. Vychází ze standardu [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 8571 a je přizpůsoben pro telekomunikační prostředí. Architektura následuje model klient-server, kde systém správy (iniciátor) interaguje se spravovaným síťovým prvkem (responder) za účelem provádění operací se soubory. Mezi klíčové komponenty patří FTAM protokolový stroj, který zajišťuje komunikační dialog, a virtuální úložiště souborů (virtual filestore), což je abstraktní reprezentace souborového systému na spravované entitě, s nímž FTAM pracuje.

Protokol funguje prostřednictvím řady fázových aktivit: navázání spojení, výběr souboru, přenos dat a uvolnění. Podporuje širokou škálu služeb včetně vytváření, mazání, čtení, zápisu souborů a správy jejich atributů. Přenos dat může probíhat hromadně nebo orientovaně na záznamy, což poskytuje flexibilitu pro různé typy souborů. FTAM zajišťuje spolehlivost pomocí mechanismů kontrolních bodů a restartu, což umožňuje pokračovat v přerušených přenosech. Zahrnuje také bezpečnostní funkce pro autentizaci a řízení přístupu.

V rámci ekosystému 3GPP se FTAM primárně používá pro úkoly správy, provozu a údržby (OAM). Je základním kamenem pro přenos softwarových balíčků (např. pro aktualizace [eNB](/mobilnisite/slovnik/enb/) nebo uzlů core sítě), konfiguračních souborů a výkonnostních reportů. Jeho standardizovaná povaha zajišťuje interoperabilitu mezi více-dodavatelskými systémy správy a síťovými prvky, což je klíčové pro rozsáhlá, heterogenní nasazení sítí. Podrobné stavové automaty a definice služeb protokolu poskytují robustní základ pro automatizovanou a odolnou správu souborů v telekomunikačních sítích.

## K čemu slouží

FTAM byl zaveden, aby vyřešil kritickou potřebu standardizované, spolehlivé a bezpečné metody správy souborů na distribuovaných síťových prvcích. Před jeho přijetím se pro softwarové aktualizace a správu konfigurace používaly proprietární skripty a protokoly, což vedlo k problémům s interoperabilitou, zvýšené provozní složitosti a vyšším nákladům v sítích s více dodavateli. Vytvoření FTAM bylo motivováno rostoucí složitostí sítí 3G a požadavkem na automatizované zřizování a údržbu.

Tato technologie řeší omezení ad-hoc metod přenosu souborů tím, že poskytuje formalizovaný protokol s explicitními definicemi služeb, postupy pro obnovu po chybách a bezpečnostními kontexty. To umožňuje síťovým operátorům automatizovat klíčové pracovní postupy OAM, jako je hromadné nasazování softwaru, centralizovaná správa konfigurace a sběr fakturačních nebo výkonnostních dat ze síťových prvků. Standardizací tohoto rozhraní 3GPP umožnilo oddělení systému správy od dodavatelsky specifické implementace síťového prvku, což podpořilo konkurenceschopnější a flexibilnější ekosystém.

Historicky integrace FTAM do standardů 3GPP položila základy pro Telecommunications Management Network (TMN) a později pro rozhraní Network Management ([NM](/mobilnisite/slovnik/nm/)). Vyřešila problém, jak spolehlivě doručovat velké soubory (jako jsou celé obrazy operačního systému pro základnové stanice) přes potenciálně nespolehlivé managementové spoje, čímž zajistila integritu sítě a snížila potřebu manuálního zásahu během cyklů aktualizací.

## Klíčové vlastnosti

- Standardizovaný protokol založený na ISO pro interoperabilitu mezi dodavateli
- Komplexní operace se soubory (čtení, zápis, mazání, vytváření, správa atributů)
- Spolehlivý přenos s mechanismy obnovy pomocí kontrolních bodů a restartu
- Podpora jak hromadného, tak orientovaného režimu přenosu dat na záznamy
- Abstrakce virtuálního úložiště souborů pro konzistentní interakci se souborovým systémem
- Integrované bezpečnostní služby pro autentizaci a řízení přístupu

## Související pojmy

- [NM – Network Management](/mobilnisite/slovnik/nm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 41.033** (Rel-14) — GSM Lawful Interception Interface Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [FTAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftam/)
