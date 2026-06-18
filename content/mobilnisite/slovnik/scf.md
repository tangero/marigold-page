---
slug: "scf"
url: "/mobilnisite/slovnik/scf/"
type: "slovnik"
title: "SCF – Service Control Function (IN context), Service Capability Feature (VHE/OSA context)"
date: 2025-01-01
abbr: "SCF"
fullName: "Service Control Function (IN context), Service Capability Feature (VHE/OSA context)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scf/"
summary: "Základní komponenta aplikační vrstvy služeb umožňující funkce řízení hovorů v inteligentní síti (IN) a schopnosti otevřeného přístupu ke službám (OSA). Poskytuje logiku a rozhraní pro vytváření a sprá"
---

SCF je základní komponenta aplikační vrstvy služeb, která poskytuje logiku a rozhraní pro vytváření a správu pokročilých telekomunikačních služeb v kontextech Inteligentní sítě (IN) a Otevřeného přístupu ke službám (OSA).

## Popis

Service Control Function (SCF) je základní entita v architektuře Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)), jak ji definuje 3GPP. Hostí aplikační logiku a provádí programy řízení služeb, například pro předplacené služby, virtuální privátní sítě nebo překlad čísel. V kontextu IN komunikuje SCF s funkcí přepínání služeb ([SSF](/mobilnisite/slovnik/ssf/)) v přepínacích uzlech prostřednictvím protokolu [INAP](/mobilnisite/slovnik/inap/) (Intelligent Network Application Part). Toto oddělení umožňuje vyvíjet a nasazovat služby nezávisle na podkladové přepínací infrastruktuře, což vede k rychlému zavádění služeb a centralizovanému řízení. SCF zpracovává podněty ze SSF, provádí aplikační logiku a vrací instrukce pro manipulaci s hovory, jako je připojení ke specializovaným zdrojům nebo změna směrování.

V kontextu Virtual Home Environment ([VHE](/mobilnisite/slovnik/vhe/)) a Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) znamená SCF Service Capability Feature (funkce schopností služeb). V tomto případě představuje standardizovanou sadu síťových schopností vystavených aplikacím prostřednictvím otevřených [API](/mobilnisite/slovnik/api/), jako jsou rozhraní Parlay/OSA. Tyto SCF abstrahují podkladové síťové funkce – například řízení hovorů, polohu uživatele nebo zasílání zpráv – do znovupoužitelných komponent. Aplikace komunikují s SCF prostřednictvím Service Capability Server ([SCS](/mobilnisite/slovnik/scs/)), který funguje jako brána a zajišťuje zabezpečený a řízený přístup. Tento model usnadňuje vývoj služeb třetích stran bez nutnosti hluboké znalosti telekomunikačních protokolů a podporuje ekosystém inovativních aplikací.

Architektura zahrnuje klíčové komponenty jako SCF samotné, SSF pro spouštění a specializované zdroje (např. pro hlášení) prostřednictvím Specialized Resource Function ([SRF](/mobilnisite/slovnik/srf/)). V OSA zajišťuje Framework autentizaci, objevování a správu SCF. SCF jsou klíčové pro umožnění pokročilých služeb, jako je přizpůsobené směrování hovorů, služby založené na stavu dostupnosti a konvergentní webově-telekomunikační aplikace. Fungují napříč více verzemi, vyvíjejí se pro podporu nových paradigmat služeb při zachování zpětné kompatibility, což zajišťuje stabilní platformu pro nasazování služeb.

## K čemu slouží

SCF bylo vytvořeno, aby řešilo omezení tradičních telekomunikačních sítí, kde byla aplikační logika pevně integrována do přepínacího zařízení, což činilo nasazení služeb pomalým, nákladným a závislým na dodavateli. Zavedením konceptu IN umožnila 3GPP oddělení řízení služeb od základního zpracování hovorů, což operátorům umožnilo rychle nasazovat a spravovat přidané hodnotové služby, jako jsou bezplatná volání, volání na platební kartu nebo televoting. Tento architektonický posun zkrátil dobu uvedení na trh a provozní náklady a podpořil konkurenci a inovace v telekomunikačních službách.

S příchodem VHE a OSA se účel rozšířil o umožnění otevřeného, standardizovaného přístupu k síťovým schopnostem pro vývojáře třetích stran. Dříve vyžadovalo vytváření integrovaných telekomunikačních služeb proprietární rozhraní a hlubokou síťovou integraci, což omezovalo inovace. Model SCF v OSA poskytl zabezpečenou, abstrahovanou vrstvu API, která umožnila aplikacím využívat síťové funkce – jako je zahájení hovoru nebo dotaz na stav uživatele – bez vystavení detailů jádra sítě. To podpořilo trend personalizace služeb a konvergence s IT a vyhovělo požadavkům na dynamičtější a uživatelsky orientovanější služby v rozvíjejících se mobilních ekosystémech.

## Klíčové vlastnosti

- Hostí a provádí programy aplikační logiky Inteligentní sítě
- Komunikuje s funkcí přepínání služeb (SSF) prostřednictvím INAP pro řízení hovorů
- Vystavuje síťové schopnosti jako funkce schopností služeb (Service Capability Features) v OSA
- Podporuje otevřená API (např. Parlay) pro integraci aplikací třetích stran
- Umožňuje rychlé nasazení služeb nezávislé na přepínací infrastruktuře
- Poskytuje centralizované řízení a správu služeb v celé síti

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.297** (Rel-19) — Charging Data Record File Transfer
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/scf/)
