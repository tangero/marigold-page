---
slug: "camel"
url: "/mobilnisite/slovnik/camel/"
type: "slovnik"
title: "CAMEL – Customised Applications for Mobile network Enhanced Logic"
date: 2025-01-01
abbr: "CAMEL"
fullName: "Customised Applications for Mobile network Enhanced Logic"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/camel/"
summary: "CAMEL je standard 3GPP pro služby inteligentních sítí (IN) v sítích GSM, UMTS a LTE. Umožňuje služby v reálném čase definované operátorem, jako je předplacené účtování, překlad čísel a řízení hovorů p"
---

CAMEL je standard inteligentních sítí (IN) 3GPP, který umožňuje poskytovat v reálném čase operátorsky definované služby, jako je předplacené účtování a řízení hovorů pro roamující účastníky v sítích GSM, UMTS a LTE.

## Popis

CAMEL (Customised Applications for Mobile network Enhanced Logic) je standard 3GPP, který rozšiřuje koncepty inteligentních sítí ([IN](/mobilnisite/slovnik/in/)) na mobilní sítě, konkrétně GSM, [GPRS](/mobilnisite/slovnik/gprs/), UMTS a IMS. Poskytuje standardizovaný mechanismus pro síťové operátory, aby nabízeli účastníkům operátorské, přidané služby, a to i při roamování mimo jejich domovskou síť. Základním principem je oddělení služební logiky od základních funkcí řízení hovorů a relací síťových ústředen ([MSC](/mobilnisite/slovnik/msc/)/VLR, SGSN, GGSN). Toto oddělení umožňuje centralizované vytváření, nasazování a správu složitých služeb bez nutnosti aktualizací každého síťového uzlu.

Architektura CAMEL je postavena na interakci mezi síťovými entitami pomocí protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)), který je rozšířením SS7/SIGTRAN. Klíčové funkční komponenty zahrnují CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) neboli Service Control Function (SCF), který hostuje služební logiku, a Service Switching Function (SSF) integrovanou do síťových ústředen jako MSC/VLR nebo [GMSC](/mobilnisite/slovnik/gmsc/). SSF detekuje spouštěcí body (Detection Points) během zpracování hovoru nebo relace a pozastaví lokální zpracování, aby požádal o instrukce od vzdáleného SCF přes CAP. SCF následně vrátí instrukce (např. connect, continue, play announcement, apply charging) SSF, který je vykoná, což umožňuje řízení služeb v reálném čase na základě událostí.

CAMEL funguje prostřednictvím řady fází a spouštěcích detekčních bodů definovaných pro různé typy hovorů a relací, jako jsou Mobile Originated, Mobile Terminated a Forwarded hovory. Podporuje více fází, jako je navázání hovoru, vyzvánění, odpověď a ukončení. Pro paketově orientovanou doménu zavedly CAMEL Phase 3 a novější verze řízení pro GPRS relace a SMS, což umožnilo služby jako předplacené účtování dat. Protokol definuje bohatou sadu operací a parametrů pro řízení účtování, notifikace událostí a manipulaci s hovory, což z něj činí komplexní nástroj pro služby ve stylu IN.

Jeho role v síti je zásadní pro monetizaci a diferenciaci služeb. Je základní technologií umožňující předplacené účtování v reálném čase, které je klíčové pro mnoho trhů. Také podporuje pokročilé služby řízení hovorů, jako jsou Freephone, Premium Rate, Virtual Private Networks (VPN) a služby založené na poloze. Poskytnutím standardizovaného rozhraní zajišťuje CAMEL interoperabilitu mezi zařízeními různých dodavatelů a mezi různými síťovými operátory, což je nezbytné pro bezproblémový roaming a konzistentní poskytování služeb.

## K čemu slouží

CAMEL byl vytvořen, aby odstranil omezení tradičního, na ústřednách založeného poskytování služeb v mobilních sítích. Před CAMELem byly pokročilé telefonní služby implementovány přímo v softwaru Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)), což je činilo závislými na dodavateli, obtížně vytvářitelnými a nákladnými na jednotné nasazení v celé síti. Tento přístup také zcela selhával pro roamující účastníky, protože ústředny navštívené sítě neznaly vlastní služby domovského operátora. Existovala jasná potřeba standardizované, síťově široké platformy pro vývoj a provádění vlastní služební logiky nezávisle na základní infrastruktuře ústředen.

Hlavní problém, který CAMEL řeší, je umožnění služebního řízení v reálném čase specifického pro operátora bez ohledu na polohu účastníka. To bylo hnací silou komerční potřeby předplacených služeb, které vyžadují okamžitou kontrolu a odečet kreditu během hovoru nebo datové relace. Bez systému jako je CAMEL bylo téměř nemožné implementovat předplacené služby v síti s více dodavateli a pro roamující uživatele. CAMEL poskytl architektonický rámec a protokol ([CAP](/mobilnisite/slovnik/cap/)) k oddělení služební logiky (hostované v centralizovaném SCF) od funkcí přepojování hovorů, což umožnilo centralizované vytváření služeb a konzistentní provádění doma i v zahraničí.

Historicky CAMEL navázal na standardy inteligentních sítí (IN) pro pevné linky, jako je ITU-T CS-1, ale přizpůsobil je jedinečným požadavkům mobilních sítí, jako je správa mobility, předávání hovorů a roaming. Jeho zavedení v 3GPP Release 99 (CAMEL Phase 3) představovalo významný vývoj, který rozšířil podporu na paketově orientovanou doménu (GPRS) a SMS, čímž standard připravil na budoucnost datových služeb. CAMEL odstranil omezení předchozích proprietárních řešení IN vytvořením jednotného rozhraní specifikovaného 3GPP, což podpořilo interoperabilitu a urychlilo globální nasazení pokročilých služeb generujících příjmy.

## Klíčové vlastnosti

- Řízení služeb v reálném čase pro obsluhu hovorů a relací
- Podpora předplaceného/postplaceného účtování prostřednictvím standardizovaných účtovacích operací
- Transparentnost roamingu pro služby domovského operátora
- Protokol (CAP) pro komunikaci mezi Service Control a Switching Functions
- Spouštěcí detekční body (Trigger Detection Points) pro vyvolání logiky řízené událostmi
- Podpora služeb pro okruhově přepínané (hlas), paketově přepínané (GPRS) a IMS domény

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [CAMEL na 3GPP Explorer](https://3gpp-explorer.com/glossary/camel/)
