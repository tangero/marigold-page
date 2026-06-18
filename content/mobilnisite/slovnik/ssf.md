---
slug: "ssf"
url: "/mobilnisite/slovnik/ssf/"
type: "slovnik"
title: "SSF – Service Switching Function"
date: 2026-01-01
abbr: "SSF"
fullName: "Service Switching Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssf/"
summary: "Funkce jádra sítě, původně z architektury Inteligentní sítě (IN), která detekuje spouštěče služeb a komunikuje s Service Control Function (SCF). V systémech 3GPP je integrována do MSC nebo GMSC, aby u"
---

SSF je Service Switching Function, prvek jádra sítě integrovaný do MSC nebo GMSC, který detekuje spouštěče služeb a funguje jako brána mezi zpracováním hovoru a Service Control Function (SCF) pro umožnění přidaných služeb.

## Popis

Service Switching Function (SSF) je základní součást architektury Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)), která byla přijata a přizpůsobena v systémech 3GPP pro služby okruhově komutované ([CS](/mobilnisite/slovnik/cs/)) domény. Je to funkční entita typicky umístěná společně a integrovaná do Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)). Primární role SSF je fungovat jako zprostředkovatel nebo 'přepínač' mezi základními funkcemi řízení hovoru a spojení MSC a pokročilou servisní logikou hostovanou v samostatné entitě zvané Service Control Function ([SCF](/mobilnisite/slovnik/scf/)), která často sídlí v Service Control Point ([SCP](/mobilnisite/slovnik/scp/)). SSF sleduje události a stavy hovoru v rámci MSC vůči sadě nakonfigurovaných detekčních bodů ([DP](/mobilnisite/slovnik/dp/)).

Jak to funguje, zahrnuje kontinuální dialog založený na IN Application Protocol ([INAP](/mobilnisite/slovnik/inap/)). Když událost při sestavování hovoru nebo během hovoru (jako zvednutí volaným účastníkem nebo stisknutí DTMF tónu) odpovídá nakonfigurovanému DP v SSF, SSF se aktivuje a pozastaví základní zpracování hovoru. Poté sestaví zprávu INAP (např. operaci InitialDP) obsahující podrobnosti o hovoru a spouštěcí události a odešle tento dotaz do SCF. SCF, který obsahuje servisní logiku (např. pro předplacenou službu), zpracuje dotaz, učiní rozhodnutí (např. zkontroluje zůstatek, aplikuje směrovací číslo) a odešle zpět odpověď INAP do SSF s instrukcemi. Tyto instrukce, známé jako 'příkazy řízení hovoru', mohou SSF nařídit, aby hovor spojila, přehrála oznámení, sbírala číslice, aplikovala účtování nebo hovor ukončila. SSF tyto příkazy věrně provede v rámci přepínací struktury MSC a poté obnoví základní zpracování hovoru, případně aktivuje další detekční body později během hovoru.

Architektonicky je SSF klíčovou součástí fyzické roviny konceptuálního modelu IN. Její klíčové komponenty zahrnují Call Control Function (CCF) pro základní obsluhu hovoru, samotnou Service Switching Function pro interakci s IN a specializovanou funkci zdrojů (často součást samostatného SRF) pro přehrávání oznámení nebo sběr číslic podle příkazu SCF. V 3GPP je integrace SSF specifikována podrobně, definuje, jak protokoly IN jako INAP (založené na CAMEL pro mobilitu) rozhraní s interním modelem hovoru MSC. Role SSF je klíčová pro oddělení servisní inteligence od přepínacího hardwaru, což operátorům umožňuje zavádět a upravovat služby centrálně na SCP bez nutnosti upgradovat každé MSC v síti. Umožňuje realizaci široké škály standardizovaných a operátorsky specifických CS služeb.

## K čemu slouží

SSF byla vytvořena, aby vyřešila zásadní problém monolitických, nepružných telefonních ústředen. V tradičních telefonních sítích vyžadovaly nové služby (jako přesměrování hovoru nebo bezplatná čísla) softwarové upgrady každé ústředny v síti, což byl pomalý, nákladný proces brzdící inovace. Koncept Inteligentní sítě a následně i SSF byl vyvinut k oddělení servisní logiky od přepínací funkčnosti. Účelem SSF je vložit inteligenci 'přepínání služeb' přímo do ústředny (MSC), aby mohla rozpoznat, kdy hovor vyžaduje pokročilé zpracování, a delegovat toto zpracování na centralizovaný výkonný počítač (SCP).

Tato architektura řešila významná omezení. Umožnila rychlé vytváření a nasazování nových přidaných služeb z jednoho centrálního bodu. Operátoři nyní mohli implementovat služby jako předplacená mobilní služba, virtuální privátní sítě (VPN) pro firmy nebo služby překladu čísel v celé své síti aktualizací servisní logiky na svých SCP, zatímco MSC, vybavené SSF, jednoduše následovaly příkazy. To dramaticky zkrátilo dobu uvedení nových služeb na trh a umožnilo personalizované nabídky. Historický kontext je zakořeněn ve standardech IN pro pevné linky (jako CS-1/CS-2 od ITU-T), které 3GPP přizpůsobilo pro mobilní prostředí, primárně prostřednictvím sady protokolů CAMEL.

V systémech 3GPP SSF vyřešila kritický problém poskytování pokročilých, síťově řízených služeb roamujícím účastníkům. Servisní logika domovské sítě účastníka (na SCP HPMN) mohla řídit hovory pro tohoto účastníka, i když roamoval v navštívené síti, prostřednictvím interakce SSF navštíveného MSC s domovským SCP přes CAMEL. To umožnilo globální služby jako předplacené roamování, což byl před aplikací principů IN na mobilní sítě hlavní obchodní a technický problém. SSF tedy nebyla jen vylepšením, ale zásadním prvkem umožňujícím komerční mobilní služby nad rámec základního hlasového volání.

## Klíčové vlastnosti

- Integrována do MSC/GMSC pro propojení základního řízení hovoru s IN servisní logikou
- Sleduje události hovoru a aktivuje se na základě nakonfigurovaných detekčních bodů (DPs)
- Komunikuje s Service Control Function (SCF) pomocí IN Application Protocol (INAP/CAMEL)
- Provádí příkazy řízení hovoru (spojit, ukončit, přehrát oznámení, sbírat číslice) od SCF
- Umožňuje centralizované vytváření a nasazování služeb nezávislé na přepínacím hardwaru
- Základní pro implementaci standardizovaných okruhově komutovaných služeb, jako je předplacená služba, bezplatné volání a VPN

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [INAP – Intelligent Network Application Protocol](/mobilnisite/slovnik/inap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.827** (Rel-12) — IMS-based Streaming & Download Delivery Enhancements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [SSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssf/)
