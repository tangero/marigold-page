---
slug: "pia"
url: "/mobilnisite/slovnik/pia/"
type: "slovnik"
title: "PIA – Point In Association"
date: 2025-01-01
abbr: "PIA"
fullName: "Point In Association"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pia/"
summary: "Referenční bod nebo logická asociace v rámci jádra sítě, často používaná v kontextech CAMEL nebo servisní vrstvy. Definuje konkrétní interakční body pro provádění servisní logiky, což umožňuje přizpůs"
---

PIA je referenční bod nebo logická asociace v rámci jádra sítě, která definuje konkrétní interakční body pro provádění servisní logiky, což umožňuje přizpůsobené řízení hovorů a služeb.

## Popis

Point In Association (PIA, bod v asociaci) je koncept v architektuře jádra sítě 3GPP, primárně spojovaný s protokolem [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile network Enhanced Logic) a protokoly pro řízení služeb. Představuje logický bod nebo fázi v asociaci mezi síťovými entitami, například mezi Service Control Point ([SCP](/mobilnisite/slovnik/scp/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), kde může být vyvolána specifická servisní logika. PIA definuje přesný okamžik nebo podmínku během sestavování, modifikace nebo ukončování hovoru či relace, kdy dochází k CAMEL triggerům nebo jiným akcím souvisejícím se službami, což umožňuje přesné řízení provádění služeb. Tento mechanismus je klíčový pro implementaci pokročilých telefonních služeb, jako je předplacené účtování, přesměrování hovorů nebo překlad čísel, standardizovaným způsobem napříč různými síťovými operátory a regiony.

Architektonicky je PIA implementován v rámci protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)), který funguje nad signalizací Signaling System No. 7 ([SS7](/mobilnisite/slovnik/ss7/)) nebo IP-based. Zahrnuje klíčové komponenty jako gsmSCF (Service Control Function), která obsahuje servisní logiku, a gsmSSF (Service Switching Function) v MSC nebo [GMSC](/mobilnisite/slovnik/gmsc/), která detekuje body v hovoru a spouští akce na základě definic PIA. PIA je specifikováno v dokumentu 3GPP TS 23.078 a souvisejících dokumentech, které detailně popisují různé body, jako jsou typy [DP](/mobilnisite/slovnik/dp/) (Detection Point) – např. DP Collected_Info nebo DP Route_Select_Failure – odpovídající konkrétním fázím zpracování hovoru. Když hovor dosáhne definovaného PIA, gsmSSF odešle notifikaci gsmSCF, která pak může ovlivnit průběh hovoru odesláním instrukcí zpět, například připojením k určitému číslu nebo aplikací účtování.

Fungování PIA zahrnuje sekvenci detekčních bodů a triggerů nakonfigurovaných v síti. Například během hovoru iniciovaného mobilním zařízením může MSC narazit na PIA jako DP Collected_Info po načtení vytočených číslic, což vyvolá CAMEL dotaz na předplacený server pro kontrolu kreditu. Server odpoví příkazy continue nebo apply charging, které určí, zda hovor pokračuje. To umožňuje interakci se službami v reálném čase bez nutnosti modifikace základních funkcí přepojování hovorů. Role PIA sahá mimo hlasové služby i do datových služeb v pozdějších verzích, podporuje prostředí [GPRS](/mobilnisite/slovnik/gprs/) a IMS, kde pomáhá řídit datové relace, QoS (Quality of Service) a hodnotově přidané služby prostřednictvím standardizovaných rozhraní, čímž zajišťuje interoperabilitu a flexibilní nasazení služeb v rozvíjejících se jádrových sítích.

## K čemu slouží

Point In Association byl vytvořen, aby řešil potřebu flexibilní, operátorsky specifické servisní logiky v mobilních sítích bez nutnosti změn standardních protokolů pro řízení hovorů. Před zavedením CAMEL a PIA implementace vlastních služeb, jako jsou předplacené služby nebo virtuální privátní sítě, často vyžadovala proprietární rozšíření ústředen, což vedlo k problémům s interoperabilitou a vysokým nákladům. Zavedeno ve verzi 3GPP R99, PIA poskytlo standardizovaný způsob definice interakčních bodů, kde může být vloženo externí řízení služeb, čímž vyřešilo problém rigidních síťových architektur a umožnilo rychlou inovaci služeb napříč více-dodavatelským prostředím.

Historicky, jak se sítě GSM globálně rozšiřovaly, operátoři usilovali o diferenciaci prostřednictvím hodnotově přidaných služeb při zachování kompatibility. PIA jako součást CAMEL umožnilo umístit servisní logiku do samostatných uzlů (SCP), čímž oddělilo tvorbu služeb od základních přepojovacích funkcí. Tím se vyřešila omezení dřívějších přístupů IN (Intelligent Network) specifikací přesných bodů v asociacích hovorů, což zajistilo spolehlivé spouštění a snížilo složitost nasazení služeb. Umožnilo to růst předplacených mobilních služeb na konci 90. let a v letech 2000, které byly závislé na účtování a řídicích bodech v reálném čase definovaných pomocí PIA.

V pozdějších verzích se PIA vyvinulo, aby podporovalo paketově přepínané domény a IMS, čímž rozšířilo svůj účel na datové a multimediální služby. Vyřešilo to výzvy v integraci legacy IN s IP-based sítěmi a umožnilo bezproblémovou kontinuitu služeb. Bez PIA by sítě postrádaly standardizovaný mechanismus pro integraci služeb třetích stran, což by brzdilo vývoj pokročilých mobilních aplikací a personalizovaných uživatelských zkušeností v éře digitálních služeb.

## Klíčové vlastnosti

- Definuje logické body pro vyvolání servisní logiky v toku hovoru/relace
- Integruje se s protokolem CAMEL Application Part (CAP)
- Podporuje různé typy Detection Point (DP) pro přesné spouštění
- Umožňuje řízení služeb v reálném čase, jako je předplacené účtování a směrování hovorů
- Usnadňuje interoperabilitu mezi síťovými elementy od různých dodavatelů
- Rozšiřitelné na paketově přepínané domény a domény IMS v pozdějších verzích

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [PIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pia/)
