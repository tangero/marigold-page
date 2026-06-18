---
slug: "nss"
url: "/mobilnisite/slovnik/nss/"
type: "slovnik"
title: "NSS – Network Sub System"
date: 2025-01-01
abbr: "NSS"
fullName: "Network Sub System"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nss/"
summary: "Jádro okruhově přepínané domény sítě GSM, zodpovědné za řízení hovorů, správu mobility a data účastníků. Skládá se z klíčových uzlů, jako jsou MSC, VLR, HLR a EIR, které společně umožňují hlasové hovo"
---

NSS je jádro okruhově přepínané domény v síti GSM, které zahrnuje uzly jako MSC, VLR, HLR a EIR a poskytuje řízení hovorů, správu mobility a data účastníků pro hlasové služby a SMS.

## Popis

Network Sub System (NSS) je hlavní síťová doména systému GSM (Global System for Mobile communications) a jeho vyvinutých protějšků 2.5G/3G. Představuje okruhově přepínané srdce sítě, zodpovědné za správu hlasových hovorů, služby krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)) a mobilitu účastníků. NSS rozhraní na jedné straně s podsystémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) a na druhé straně s externími sítěmi, jako je telefonní síť veřejné komunikační sítě ([PSTN](/mobilnisite/slovnik/pstn/)). Jeho primární funkcí je navazování, udržování a ukončování okruhově přepínaných spojení a sledování polohy mobilních účastníků za účelem doručování služeb.

Architektonicky se NSS skládá z několika klíčových vzájemně propojených uzlů. Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) je centrální ústředna, která zajišťuje směrování a přepojování hovorů. Propojuje hovory mezi mobilními uživateli a mezi mobilními a pevnými sítěmi. Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) je databáze, často umístěná společně s MSC, která uchovává dočasná data účastníků pro uživatele nacházející se aktuálně v její servisní oblasti. Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) je trvalá hlavní databáze účastníků obsahující všechny uživatelské profily, servisní předplatná a aktuální informace o poloze (odkazující na obsluhující VLR). Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)) je databáze, která eviduje platné, blokované nebo odcizené identity mobilních zařízení ([IMEI](/mobilnisite/slovnik/imei/)). Další prvky, jako SMS Interworking MSC (SMS-IWMSC) a Gateway MSC (GMSC), zajišťují doručování SMS a propojení s jinými sítěmi.

NSS funguje prostřednictvím sofistikovaných signalizačních protokolů, primárně Mobile Application Part (MAP) běžícího nad signalizačním systémem č. 7 (SS7). Když se mobilní telefon registruje v síti, kontaktuje BSS, který registraci předá MSC/VLR. VLR následně dotazuje HLR účastníka (pomocí MAP signalizace) za účelem autentizace uživatele a stažení jeho servisního profilu. Pro příchozí hovor je hovor směrován na GMSC, který dotazem na HLR zjistí, které MSC/VLR účastníka aktuálně obsluhuje. HLR poskytne adresu obsluhujícího MSC a hovor je tam směrován k dokončení. Tento složitý proces signalizace mezi uzly NSS umožňuje plynulou mobilitu a poskytování služeb napříč rozsáhlými geografickými oblastmi.

## K čemu slouží

NSS bylo vytvořeno jako základní jádrová síť pro GSM za účelem umožnění širokoplošné, automatizované mobilní telefonie. Před GSM byly rané mobilní systémy často manuální nebo měly velmi omezené, lokalizované pokrytí. NSS vyřešilo základní problémy správy mobility účastníků a automatického přepojování hovorů v národní nebo mezinárodní síti. Oddělilo trvalou identitu uživatele (uloženou v HLR) od jeho dočasné polohy (spravované VLR), což byl revoluční koncept, který uživatelům umožnil plynulý roaming.

Jeho vytvoření bylo motivováno cílem vytvořit digitální, škálovatelnou a standardizovanou celulární síť. Architektura NSS poskytla přepojovací inteligenci a databáze účastníků nezbytné pro podporu milionů uživatelů a nabídla služby jako přesměrování hovorů, roaming a SMS. Vyřešila omezení předchozích analogových systémů tím, že poskytla robustní, na signalizaci bohaté jádro schopné zvládnout komplexní směrování, zabezpečení (prostřednictvím autentizačních center často integrovaných s HLR) a servisní logiku. NSS vytvořilo vzor pro všechny následující okruhově přepínané mobilní jádrové sítě, včetně těch pro 3G UMTS, předtím než průmysl přešel na plně IP IMS a paketově přepínaná jádra 4G a 5G.

## Klíčové vlastnosti

- Poskytuje funkce okruhově přepínané jádrové sítě pro hlas a SMS
- Je centralizované kolem Mobile Switching Center (MSC) pro řízení hovorů
- Využívá HLR pro trvalá data účastníků a VLR pro dočasná data návštěvníků
- Používá EIR pro validaci identity zařízení a zabezpečení
- Pro komunikaci mezi uzly používá signalizaci SS7/MAP
- Umožňuje národní a mezinárodní roaming účastníků

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [NSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nss/)
