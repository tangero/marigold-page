---
slug: "osi"
url: "/mobilnisite/slovnik/osi/"
type: "slovnik"
title: "OSI – Open Systems Interconnection"
date: 2025-01-01
abbr: "OSI"
fullName: "Open Systems Interconnection"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/osi/"
summary: "Základní sedmivrstvý konceptuální model (ISO/IEC 7498-1) pro standardizaci komunikačních funkcí telekomunikačního nebo výpočetního systému. Standardy 3GPP často odkazují na model OSI pro popis zásobní"
---

OSI je základní sedmivrstvý konceptuální model, který 3GPP používá pro standardizaci a popis komunikačních funkcí a zásobníků protokolů v telekomunikačních systémech.

## Popis

Model Open Systems Interconnection (OSI) je univerzální, abstraktní rámec vyvinutý organizací International Organization for Standardization ([ISO](/mobilnisite/slovnik/iso/)) pro standardizaci funkcí komunikačního systému do sedmi samostatných vrstev. Ačkoli sám o sobě není sadou protokolů, poskytuje klíčový referenční model, který 3GPP a další normalizační orgány používají k popisu, návrhu a vysvětlení složitých protokolových architektur. Každá vrstva v modelu OSI vykonává specifickou sadu funkcí, poskytuje služby vrstvě nad sebou a spoléhá na služby vrstvy pod sebou, čímž vytváří jasné oddělení odpovědností. Tento vrstvený přístup zjednodušuje návrh sítí, umožňuje interoperabilitu mezi produkty různých výrobců a usnadňuje řešení problémů izolací funkcí.

Sedm vrstev, od nejnižší po nejvyšší, je: 1) Fyzická vrstva (vrstva 1): Definuje elektrické, mechanické a procedurální rozhraní pro přenosové médium (např. rádiové vlny, vlákno). Zpracovává přenos a příjem bitů. 2) Linková vrstva (vrstva 2): Zajišťuje přenos dat mezi uzly, detekci/opravu chyb a řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Formátuje data do rámců a spravuje přístup ke sdílenému médiu. 3) Síťová vrstva (vrstva 3): Poskytuje funkční a procedurální prostředky pro přenos datových sekvencí proměnné délky (paketů) ze zdrojového do cílového uzlu přes jednu nebo více sítí, včetně směrování a adresování. 4) Transportní vrstva (vrstva 4): Zajišťuje transparentní přenos dat mezi koncovými systémy s možností spolehlivého či nespolehlivého doručení, řízením toku a obnovou po chybě. 5) Relační vrstva (vrstva 5): Spravuje řízení dialogu a synchronizaci mezi aplikacemi. 6) Prezentační vrstva (vrstva 6): Překládá mezi aplikačními a síťovými formáty, poskytuje šifrování, kompresi a transformaci dat. 7) Aplikační vrstva (vrstva 7): Rozhraní pro uživatelské aplikace pro přístup k síťovým službám.

Ve specifikacích 3GPP je na model OSI často odkazováno pro mapování složitých zásobníků protokolů v celulárních systémech. Například v rádiové protokolové architektuře odpovídá vrstva [PHY](/mobilnisite/slovnik/phy/) vrstvě OSI 1, podsoubory MAC a [RLC](/mobilnisite/slovnik/rlc/) odpovídají vrstvě OSI 2 a vrstva [RRC](/mobilnisite/slovnik/rrc/) je často považována za část vrstvy 3 řídicí roviny. Zásobník protokolů uživatelské roviny (např. [PDCP](/mobilnisite/slovnik/pdcp/), [GTP-U](/mobilnisite/slovnik/gtp-u/)) je také popsán ve vztahu k těmto vrstvám. Toto mapování je klíčové pro inženýry, aby pochopili, jak data proudí z aplikace na UE přes různé síťové uzly (gNB, [UPF](/mobilnisite/slovnik/upf/)) do externí paketové datové sítě, přičemž každá vrstva přidává nebo odstraňuje své specifické hlavičky a vykonává své určené funkce.

## K čemu slouží

Model OSI byl vytvořen na konci 70. a začátku 80. let 20. století, aby vyřešil kritický problém nekompatibility mezi proprietárními, na výrobce specifickými síťovými architekturami (např. IBM SNA, DEC DECnet). V té době bylo propojení počítačů od různých výrobců extrémně obtížné nebo nemožné, což dusilo růst síťových výpočetních technologií. Účelem modelu OSI bylo poskytnout univerzální standard, který by umožnil komunikaci různorodých systémů rozdělením komunikačního procesu na standardizované, interoperabilní vrstvy. To by umožnilo výrobcům vyvíjet produkty pro konkrétní vrstvy a zároveň zajistit kompatibilitu s produkty jiných výrobců implementujících stejné služby dané vrstvy.

Zatímco model TCP/IP, který se vyvinul z ARPANETu, se nakonec stal praktickým základem internetu, přísný teoretický rámec modelu OSI měl trvalý dopad jako výukový a referenční nástroj. 3GPP přijalo jeho principy, aby vneslo strukturu a jasnost do nesmírně složitého systému celulární telekomunikace. Řeší omezení ad-hoc návrhu protokolů vynucením modulární architektury, kde se vrstvy mohou vyvíjet nezávisle (např. vylepšení fyzické vrstvy pro 5G NR bez nutnosti přepracování celé síťové vrstvy). Toto oddělení je klíčové pro řízení životního cyklu globálního standardu, jako je 3GPP, kde jsou zaváděny nové technologie rádiového přístupu (od GSM po 5G NR) a architektury jádra sítě (od přepojování okruhů po architekturu založenou na službách), a to při zachování zpětné kompatibility a jasných funkčních hranic.

Model OSI navíc poskytuje společný jazyk pro inženýry napříč různými doménami (jádro sítě, RAN, přenosová síť) k diskusi o rozhraních a odpovědnostech. Když specifikace 3GPP uvádí, že protokol funguje na 'vrstvě 2', okamžitě tím sděluje sadu očekávaných funkcionalit (adresování, rámcování, řízení chyb) bez nutnosti dalšího rozsáhlého vysvětlování. Tento konceptuální rámec je nezbytný pro návrh, implementaci, testování a řešení problémů systémů 3GPP, neboť zajišťuje, že nesčetné množství protokolů spolupracuje koherentním a předvídatelným způsobem k poskytování koncových služeb.

## Klíčové vlastnosti

- Sedmivrstvý abstraktní referenční model pro komunikační systémy
- Jasné oddělení funkcí: Fyzická, Linková, Síťová, Transportní, Relační, Prezentační, Aplikační
- Definuje služby, které každá vrstva poskytuje vrstvě nad sebou
- Umožňuje modulární návrh a interoperabilitu více výrobců
- Slouží jako univerzální nástroj pro výuku a řešení problémů
- Poskytuje základní jazyk pro popis zásobníků protokolů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 31.112** (Rel-8) — USAT Interpreter System Architecture
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.404** (Rel-19) — Performance Management Definitions & Template
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 32.407** (Rel-19) — PM; CN CS Domain; UMTS/GSM measurements
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [OSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/osi/)
