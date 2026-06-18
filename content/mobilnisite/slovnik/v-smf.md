---
slug: "v-smf"
url: "/mobilnisite/slovnik/v-smf/"
type: "slovnik"
title: "V-SMF – Visited Session Management Function"
date: 2025-01-01
abbr: "V-SMF"
fullName: "Visited Session Management Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-smf/"
summary: "Funkce správy relací nasazená ve visited veřejné pozemní mobilní síti (VPLMN), která poskytuje služby správy relací roamujícímu uživateli. Je klíčovou součástí architektury roamování 5G, umožňuje loká"
---

V-SMF (funkce správy relací ve visited síti) je funkce správy relací nasazená ve visited PLMN, která poskytuje služby správy relací roamujícímu uživateli v architektuře 5G.

## Popis

Visited Session Management Function (V-SMF) je funkce jádra sítě v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) pro 5G, definovaná speciálně pro roamingové scénáře. Je vytvořena ve visited veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), když uživatelské zařízení (UE) roamuje mimo svou domovskou veřejnou pozemní mobilní síť ([HPLMN](/mobilnisite/slovnik/hplmn/)). V-SMF je zodpovědná za správu [PDU](/mobilnisite/slovnik/pdu/) relací pro roamující UE ve visited síti. Jejím hlavním úkolem je interakce s Visited User Plane Function (V-UPF) za účelem vytváření, modifikace a uvolňování spojení v uživatelské rovině, řeší úkoly jako přidělování IP adres, vynucování QoS a generování údajů pro účtování provozu s lokálním breakoutem.

Architektonicky V-SMF pracuje pod kontrolou Home [SMF](/mobilnisite/slovnik/smf/) ([H-SMF](/mobilnisite/slovnik/h-smf/)), která zůstává v HPLMN. Tato rozdělená architektura je definována ve 3GPP Release 16 a novějších pro vylepšené roamování. V-SMF komunikuje s H-SMF přes rozhraní N16 (pomocí služby Nsmf_PDUSession) a přijímá relací politiky a pokyny. Lokálně spolupracuje s Visited Access and Mobility Management Function (V-AMF) přes rozhraní N11 a řídí V-UPF přes rozhraní N4. To umožňuje V-SMF spravovat cestu uživatelské roviny lokálně a efektivně směrovat data (Local Breakout - [LBO](/mobilnisite/slovnik/lbo/)) pro přístup k internetu nebo k místním službám datové sítě bez nutnosti vést veškerý provoz přes domovskou síť.

Fungování V-SMF je klíčové pro implementaci pokročilých roamingových funkcí, jako jsou Home Routed ([HR](/mobilnisite/slovnik/hr/)) a Local Breakout (LBO) PDU relace. Ve scénáři LBO V-SMF vybere lokální V-UPF a spravuje celou cestu uživatelské roviny v rámci VPLMN, což výrazně snižuje latenci a náklady na přenosovou síť. Zajišťuje udržení režimů kontinuity relace a služby (SSC) a aplikuje politiky QoS přijaté od H-SMF nebo Policy Control Function (PCF). V-SMF také spolupracuje s Visited Charging Function (V-CHF) na generování záznamů pro účtování za část služby využitou ve visited síti, čímž podporuje konvergované systémy účtování.

## K čemu slouží

V-SMF byla zavedena, aby řešila omezení počáteční roamingové architektury 5G Release 15, která primárně podporovala domovsky směrovaný provoz. Při domovsky směrovaném roamingu je veškerý provoz uživatelské roviny tunelován zpět do HPLMN, což vede ke zvýšené latenci, neefektivnímu využití přenosových zdrojů a neschopnosti efektivně přistupovat k místním službám nebo obsahu v navštívené zemi. V-SMF umožňuje roaming s lokálním breakoutem (LBO), což je optimalizovanější metoda směrování vyžadovaná pro samostatná nasazení 5G.

Její zavedení bylo motivováno potřebou flexibilnějšího a efektivnějšího roamingu v 5G, který podporuje případy užití s nízkou latencí a snižuje náklady a složitost mezinárodního přenosu dat. Delegováním kontroly správy relací na funkci ve visited síti tato architektura snižuje signalizační zátěž domovské sítě a umožňuje aplikaci místních síťových politik. To je nezbytné pro umožnění pokročilých služeb, jako je síťové sliceování pro roamující uživatele, kde může být instance slicu ve VPLMN přímo spravována.

## Klíčové vlastnosti

- Umožňuje PDU relace s lokálním breakoutem (LBO) pro efektivní směrování roamujících dat
- Spravuje vytváření, modifikaci a uvolňování relací pro roamující UE v rámci VPLMN
- Spolupracuje s Home SMF (H-SMF) na řízení politik a koordinaci
- Řídí Visited UPF (V-UPF) přes rozhraní N4 pro správu uživatelské roviny
- Podporuje konvergované účtování spoluprací s Visited Charging Function (V-CHF)
- Umožňuje aplikaci a vynucování politik QoS v rámci visited sítě

## Související pojmy

- [H-SMF – Home Session Management Function](/mobilnisite/slovnik/h-smf/)

## Definující specifikace

- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.542** (Rel-19) — SMF NIDD Service Based Interface Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [V-SMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-smf/)
