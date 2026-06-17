---
slug: "cug"
url: "/mobilnisite/slovnik/cug/"
type: "slovnik"
title: "CUG – Closed User Group"
date: 2026-01-01
abbr: "CUG"
fullName: "Closed User Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cug/"
summary: "Closed User Group (CUG) je funkce telekomunikační služby, která umožňuje definované skupině účastníků komunikovat výhradně mezi sebou, zatímco komunikaci s uživateli mimo skupinu omezuje nebo řídí. Po"
---

CUG je funkce telekomunikační služby, která umožňuje definované skupině účastníků komunikovat výhradně mezi sebou, zatímco komunikaci s uživateli mimo skupinu omezuje.

## Popis

Closed User Group (CUG) je funkce služby definovaná ve standardech 3GPP, která umožňuje vytvoření soukromé komunikační komunity uvnitř veřejné mobilní sítě. Funguje tak, že definuje konkrétní skupinu účastníků, kteří mají povoleno vzájemně komunikovat, zatímco interakce s uživateli mimo skupinu jsou buď zakázány, nebo podléhají specifickým omezením a kontrolám. Funkcionalita CUG je implementována prostřednictvím síťových mechanismů, které zahrnují předplatitelská data uložená v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), jež obsahují informace o členství v CUG a s tím spojená oprávnění pro každého účastníka.

Z technického hlediska služba CUG závisí na několika klíčových komponentách v rámci síťové architektury. Základní síťové prvky, zejména HLR/HSS, udržují předplatitelská data CUG včetně identifikátorů skupin, seznamů členů a přístupových práv. Když se účastník pokusí zahájit hovor nebo relaci, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) dotazuje HLR/HSS, aby ověřil, zda cílový účastník patří do stejného CUG jako volající účastník. Tento ověřovací proces určuje, zda má být hovor povolen, zamítnut nebo podroben specifickým postupům zpracování, jako je směrování přes vyhrazené brány nebo aplikace speciálních tarifů.

Implementace CUG zahrnuje více protokolových interakcí napříč různými síťovými rozhraními. Během sestavování hovoru si MSC nebo CSCF vyměňují signalizační zprávy s HLR/HSS, aby získaly informace o CUG prostřednictvím protokolů jako [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) nebo Diameter. Síť uplatňuje omezení CUG na základě předdefinovaných pravidel, která mohou zahrnovat úplný zákaz odchozích hovorů na nečleny, omezení příchozích hovorů od externích účastníků nebo speciální zpracování pro komunikaci mezi CUG, pokud účastník patří do více skupin. S funkcí CUG jsou také integrovány systémy účtování, aby aplikovaly diferencované účtování pro komunikaci uvnitř skupiny a mimo skupinu, což podporuje různé obchodní modely pro skupinové služby.

CUG hraje významnou roli při umožňování specializovaných komunikačních služeb uvnitř veřejných sítí. Umožňuje mobilním operátorům nabízet řešení na míru pro podnikové zákazníky, vládní agentury, záchranné služby a další organizace vyžadující řízená komunikační prostředí. Využitím stávající infrastruktury veřejné sítě poskytuje CUG nákladově efektivní alternativu k vyhrazeným privátním sítím při zachování zabezpečení a řízení přístupu prostřednictvím standardizovaných mechanismů 3GPP. Služba podporuje různé konfigurace včetně hierarchických struktur CUG, překrývajícího se členství v několika skupinách a diferencovaných oprávnění v rámci jedné skupiny, což ji činí přizpůsobitelnou různorodým organizačním komunikačním potřebám.

## K čemu slouží

Funkce Closed User Group (CUG) byla vyvinuta k řešení potřeby řízených komunikačních prostředí uvnitř veřejných mobilních sítí. Před její implementací musely organizace vyžadující soukromé komunikační schopnosti vytvářet samostatné vyhrazené sítě, což zahrnovalo významné náklady na infrastrukturu, režii údržby a omezenou flexibilitu. CUG umožňuje těmto organizacím využívat stávající infrastrukturu veřejné sítě při zachování zabezpečení, řízení přístupu a soukromí komunikace prostřednictvím standardizovaných mechanismů definovaných ve specifikacích 3GPP.

CUG řeší několik praktických problémů v poskytování telekomunikačních služeb. Umožňuje mobilním operátorům nabízet přidané služby podnikovým a vládním zákazníkům bez nutnosti samostatné síťové infrastruktury. Definováním jasných hranic mezi členy skupiny a nečleny CUG zajišťuje, že citlivá komunikace zůstává v autorizovaných kruzích, a přitom stále umožňuje nezbytné interakce s externími stranami za řízených podmínek. Tato rovnováha mezi izolací a konektivitou činí CUG zvláště cennou pro organizace, které potřebují jak vnitřní soukromí, tak selektivní externí přístup, jako jsou záchranné služby koordinující s veřejnými agenturami nebo podniková oddělení komunikující s dodavateli při zachování vnitřní důvěrnosti.

Vytvoření CUG bylo motivováno rostoucí poptávkou po specializovaných komunikačních službách na konci 90. let a na počátku 21. století, kdy se mobilní sítě rozšiřovaly za rámec jednotlivých spotřebitelů, aby sloužily organizačním potřebám. 3GPP standardizovalo CUG, aby zajistilo interoperabilitu napříč sítěmi různých operátorů a dodavatelů zařízení, což umožnilo organizacím udržovat konzistentní komunikační politiky napříč více regiony a poskytovateli služeb. Tato standardizace také umožnila vývoj pokročilých funkcí, jako jsou pravidla komunikace mezi CUG, hierarchické skupinové struktury a integrované účtovací mechanismy, což z CUG činí komplexní řešení pro řízené komunikační komunity uvnitř veřejných mobilních sítí.

## Klíčové vlastnosti

- Řízení přístupu na bázi skupiny omezující komunikaci mezi členy a nečleny
- Implementace na síťové bázi využívající předplatitelská data v HLR/HSS
- Podpora vícečetného členství v CUG s pravidly prioritního přístupu
- Integrované systémy účtování aplikující diferencované sazby pro komunikaci uvnitř skupiny a mimo skupinu
- Standardizované protokoly 3GPP zajišťující interoperabilitu napříč operátory a dodavateli
- Flexibilní konfigurace podporující hierarchické skupiny, překrývající se členství a různé úrovně oprávnění

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 23.259** (Rel-19) — Personal Network Management (PNM) Procedures
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- **TS 32.275** (Rel-19) — MMTel Charging Specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [CUG na 3GPP Explorer](https://3gpp-explorer.com/glossary/cug/)
