---
slug: "ocb"
url: "/mobilnisite/slovnik/ocb/"
type: "slovnik"
title: "OCB – Outgoing Calls Barred within the CUG"
date: 2026-01-01
abbr: "OCB"
fullName: "Outgoing Calls Barred within the CUG"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ocb/"
summary: "Funkce doplňkové služby ve skupině uzavřených účastníků (CUG), která účastníkovi znemožňuje uskutečňovat odchozí hovory na čísla mimo jeho určenou skupinu. Vynucuje omezení služeb a kontrolu účtování"
---

OCB je doplňková služba skupiny uzavřených účastníků (CUG), která účastníkovi znemožňuje uskutečňovat odchozí hovory na čísla mimo jeho určenou skupinu.

## Popis

Outgoing Calls Barred (OCB) je doplňková služba definovaná v rámci standardů 3GPP, která funguje jako specifické omezení v rámci širší služby Closed User Group ([CUG](/mobilnisite/slovnik/cug/)). CUG je možnost předplatného, která definuje skupinu účastníků, kteří mohou komunikovat pouze mezi sebou, čímž vytváří logickou privátní síť nad veřejnou mobilní infrastrukturou. Funkce OCB je specifická podmínka zákazu aplikovaná na člena CUG, která tomuto členovi zakazuje iniciovat (tj. uskutečňovat) hovory na cíle mimo hranice jeho přiřazené CUG. Vynucení tohoto zákazu je řízeno jádrovou sítí, konkrétně v rámci Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)). Když se účastník s aktivním omezením OCB pokusí uskutečnit hovor, zdrojový MSC nebo CSCF dotazuje profil účastníka z HLR/HSS. Po identifikaci příznaku OCB a ověření, že volané číslo není členem povolené CUG účastníka, síť zamítne žádost o sestavení hovoru, obvykle vrátí tón nebo hlášení volajícímu. Služba je vysoce konfigurovatelná na úrovni jednotlivých účastníků, což umožňuje operátorům definovat více CUG s různými charakteristikami zákazu, včetně kombinací s Incoming Calls Barred ([ICB](/mobilnisite/slovnik/icb/)) a dalšími kódy propojení CUG. Tato architektura zajišťuje, že servisní logika a data účastníka jsou centralizovány v domovské síti, což umožňuje konzistentní aplikaci pravidel zákazu i při roamingu účastníka. OCB je základním nástrojem pro implementaci řízených komunikačních prostředí, který přímo ovlivňuje řízení hovorů, účtování (zamezením zpoplatněných hovorů na externí čísla) a diferenciaci služeb.

## K čemu slouží

Primárním účelem OCB je poskytnout mechanismus pro vytváření řízených, privátních komunikačních skupin ve veřejné mobilní síti. Řeší problém nekontrolovaných komunikačních nákladů a neautorizovaných externích hovorů pro specifické skupiny účastníků, jako jsou zaměstnanci společnosti, členové vládní agentury nebo zařízení v machine-to-machine (M2M) flotile. Před standardizací těchto funkcí musely organizace spoléhat na fyzické privátní sítě nebo základní služby zákazu, kterým chyběla podrobnost skupinové logiky. Vytvoření služeb [CUG](/mobilnisite/slovnik/cug/) s možnostmi OCB a [ICB](/mobilnisite/slovnik/icb/) bylo motivováno komerčními požadavky podnikových zákazníků, kteří potřebovali kontrolu nákladů a soukromí podobnou Private Branch Exchange (PBX), ale s mobilitou a pokrytím veřejné mobilní sítě. Umožňuje operátorům nabízet nadstandardní služby pro podnikový segment, což vytváří další zdroje příjmů nad rámec individuálních tarifů pro spotřebitele. Historicky tento koncept vznikl v pevné telefonii a byl adaptován do GSM a následných systémů 3GPP, čímž se stal jedním ze základních kamenů doplňkových služeb založených na inteligentní síti (IN). Řeší omezení jednoduchého zákazu (jako je zákaz všech odchozích hovorů) tím, že poskytuje sofistikovanější, skupinově orientované omezení, které stále umožňuje nezbytnou interní komunikaci.

## Klíčové vlastnosti

- Omezuje odchozí hovory na čísla mimo určenou skupinu uzavřených účastníků (CUG) účastníka.
- Vynucováno sítí při sestavování hovoru MSC nebo CSCF na základě profilových dat z HLR/HSS.
- Funguje nezávisle nebo v kombinaci s Incoming Calls Barred (ICB) v rámci CUG.
- Podporuje více předplatných CUG s různými kódy propojení pro složité skupinové struktury.
- Aplikovatelné jak v okruhově spínané (CS), tak v IP Multimedia Subsystem (IMS) doméně.
- Zůstává účinné při roamingu díky interakci mezi navštívenou a domovskou sítí.

## Související pojmy

- [CUG – Closed User Group](/mobilnisite/slovnik/cug/)
- [ICB – Incoming Calls Barred (within the CUG)](/mobilnisite/slovnik/icb/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.529** (Rel-8) — Explicit Communication Transfer (ECT) Simulation Service
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.611** (Rel-19) — Anonymous Communication Rejection & Barring
- **TS 24.629** (Rel-19) — Explicit Communication Transfer (ECT) Protocol
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [OCB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ocb/)
