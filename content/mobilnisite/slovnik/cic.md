---
slug: "cic"
url: "/mobilnisite/slovnik/cic/"
type: "slovnik"
title: "CIC – Call Identifier Code / Circuit Identifier Code"
date: 2025-01-01
abbr: "CIC"
fullName: "Call Identifier Code / Circuit Identifier Code"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cic/"
summary: "CIC je jedinečný identifikátor používaný v sítích s přepojováním okruhů k rozlišení jednotlivých hovorů nebo fyzických okruhů. Umožňuje přesné směrování hovorů, korelaci pro účtování a správu síťových"
---

CIC (Call Identifier Code / Circuit Identifier Code) je jedinečný identifikátor používaný v sítích s přepojováním okruhů k rozlišení jednotlivých hovorů nebo fyzických okruhů pro účely směrování, účtování a správy zdrojů.

## Popis

Call Identifier Code (CIC) slouží jako základní identifikátor v 3GPP sítích s přepojováním okruhů a poskytuje jednoznačnou identifikaci jednotlivých hovorů nebo fyzických přenosových okruhů. Ve své primární aplikaci jako Call Identifier Code CIC jednoznačně identifikuje konkrétní instanci hovoru napříč více síťovými prvky a rozhraními, což umožňuje různým uzlům (jako [MSC](/mobilnisite/slovnik/msc/), [GMSC](/mobilnisite/slovnik/gmsc/) a [MGW](/mobilnisite/slovnik/mgw/)) konzistentně odkazovat na stejný hovor během procedur jeho zřizování, udržování a ukončování. Tento identifikátor je klíčový pro korelaci hovorů, generování záznamů pro účtování a řešení problémů v distribuovaných síťových architekturách.

Jako Circuit Identifier Code identifikuje CIC konkrétní fyzické nebo logické okruhy v přenosových systémech, zejména v kontextu vzájemného propojení různých síťových domén. Toto použití je zvláště důležité ve scénářích zahrnujících starší sítě s přepojováním okruhů a moderní IP sítě, kde CIC pomáhá mapovat tradiční identifikátory okruhů na odpovídající zdroje v doménách s přepojováním paketů. Kód dodržuje specifické číselné a formátovací konvence definované ve specifikacích 3GPP, aby byla zajištěna interoperabilita mezi zařízeními různých výrobců.

CIC funguje v rámci signalizačních protokolů definovaných ve specifikacích 3GPP, konkrétně v protokolech [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) a BICC (Bearer Independent Call Control). Během zřizování hovoru výchozí ústředna přiřadí hodnotu CIC, která zůstává s hovorem asociována po celou dobu jeho trvání. Tento identifikátor se objevuje v různých signalizačních zprávách, včetně Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)), Answer Message ([ANM](/mobilnisite/slovnik/anm/)) a Release Message (REL), což umožňuje všem zúčastněným uzlům udržovat konzistentní informace o stavu hovoru.

V síťové architektuře hraje CIC klíčovou roli v několika hlavních funkcích: usnadňuje přesné účtování tím, že poskytuje referenční bod pro záznamy o účtování napříč více síťovými prvky; umožňuje efektivní řešení problémů tím, že síťovým operátorům dovoluje trasovat konkrétní hovory sítí; a podporuje požadavky na zákonné odposlechy tím, že poskytuje konzistentní identifikátor pro cílenou komunikaci. Trvalá přítomnost CIC po celý životní cyklus hovoru jej činí nezbytným pro udržení integrity hovoru v komplexních síťových prostředích s více výrobci.

## K čemu slouží

CIC byl vytvořen, aby řešil základní potřebu jednoznačné identifikace hovorů v telekomunikačních sítích. V raných telefonních systémech, jak sítě rostly na složitosti a zahrnovaly více ústředen, neexistovala standardizovaná metoda pro jednoznačnou identifikaci jednotlivých hovorů napříč různými síťovými prvky. Toto omezení činilo trasování hovorů, korelaci pro účtování a izolaci chyb extrémně náročnými, zejména v prostředích s více výrobci, kde různí výrobci zařízení používali proprietární identifikační schémata.

Před standardizovanými identifikátory, jako je CIC, čelili síťoví operátoři významným provozním výzvám: z účtování vznikaly spory kvůli nekonzistentním záznamům o hovorech na různých síťových uzlech; řešení problémů vyžadovalo manuální korelaci více logovacích souborů; a vypořádání mezi operátory bylo komplikováno nekompatibilními identifikačními metodami. Zavedení CIC ve specifikacích 3GPP poskytlo standardizovaný přístup, který umožnil interoperabilitu mezi různými síťovými prvky a mezi sítěmi provozovanými různými poskytovateli služeb.

Historický kontext vývoje CIC zahrnuje přechod od analogového k digitálnímu přepojování a rostoucí potřebu automatizovaných operačních podpůrných systémů. Jak se sítě vyvíjely, aby podporovaly vyšší objemy provozu a složitější služby, manuální metody identifikace hovorů se staly nepraktickými. Specifikace CIC v 3GPP Release 5 formalizovala to, co se v různých formách vyvíjelo v dřívějších telekomunikačních standardech, a vytvořila konzistentní rámec, který mohl růst spolu s expanzí mobilních sítí a podporovat vznikající požadavky, jako je přenositelnost čísel nebo pokročilé účtovací systémy.

## Klíčové vlastnosti

- Jednoznačná identifikace hovorů s přepojováním okruhů napříč síťovými prvky
- Standardizovaný formát pro interoperabilitu mezi zařízeními různých výrobců
- Trvalá asociace s hovorem po celý jeho životní cyklus
- Podpora korelace pro účtování a generování záznamů o účtování
- Umožňuje efektivní postupy trasování hovorů a řešení problémů
- Usnadňuje vzájemné propojení mezi doménami s přepojováním okruhů a paketů

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TR 43.903** (Rel-19) — Feasibility Study for A-interface over IP

---

📖 **Anglický originál a plná specifikace:** [CIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cic/)
