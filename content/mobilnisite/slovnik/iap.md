---
slug: "iap"
url: "/mobilnisite/slovnik/iap/"
type: "slovnik"
title: "IAP – Interception Access Point"
date: 2025-01-01
abbr: "IAP"
fullName: "Interception Access Point"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iap/"
summary: "Funkční entita v síti 3GPP, která poskytuje zákonně autorizované odposlechové (LI) schopnosti. Je to bod, kde je odposlechnutý komunikační obsah (CC) a odposlechové související informace (IRI) dupliko"
---

IAP je funkční entita v síti 3GPP, kde je zákonně odposlechnutý komunikační obsah a související informace duplikován a doručen zařízení pro monitorování orgánů činných v trestním řízení.

## Popis

Interception Access Point (IAP) je standardizovaná síťová funkce definovaná 3GPP pro účely zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)). Slouží jako technické rozhraní v síti operátora, kde dochází k samotnému odposlechu telekomunikací. IAP je zodpovědný za duplikaci jak Komunikačního obsahu ([CC](/mobilnisite/slovnik/cc/)) – hovoru, SMS nebo datové relace – tak Odposlechových souvisejících informací ([IRI](/mobilnisite/slovnik/iri/)) – dat spojených s hovorem, jako jsou čísla, čas, lokalita – cíleného účastníka. Tyto duplikované informace jsou následně naformátovány a bezpečně přeneseny do zařízení pro monitorování orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)) přes standardizovaná rozhraní ([HI2](/mobilnisite/slovnik/hi2/) pro IRI, [HI3](/mobilnisite/slovnik/hi3/) pro CC).

Z architektonického hlediska není IAP jediným fyzickým uzlem, ale funkční rolí, která může být implementována v různých síťových prvcích v závislosti na odposlouchávané službě. Například v síti 5G může být funkce IAP pro odposlech datových paketů umístěna ve funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), kde může duplikovat pakety uživatelské roviny. Pro hlasové hovory přes IMS by mohla být funkce IAP v Media Gateway nebo specifické Media Resource Function. IAP přijímá aktivační příkazy od interní administrativní funkce ([ADMF](/mobilnisite/slovnik/admf/)), která je spuštěna na základě zákonného příkazu. Po aktivaci IAP tiše začne duplikovat cílený provoz bez dopadu na službu účastníka.

IAP spolupracuje s dalšími entitami LI: Administrativní funkcí (ADMF), která spravuje odposlechové příkazy a skrývá existenci více současných odposlechů před sítí; Doručovací funkcí (DF), která zajišťuje bezpečné doručení do LEMF; a Sbírkovou funkcí (CF) na straně LEMF. Činnost IAP je podrobně definována v 3GPP TS 33.108, která specifikuje předávací rozhraní (HI1, HI2, HI3), datové formáty a bezpečnostní požadavky. IAP musí zajistit integritu, důvěrnost a spolehlivost odposlechnutých dat a poskytovat silné záruky, že probíhají pouze autorizované odposlechy a že data jsou přesně doručena příslušnému orgánu.

## K čemu slouží

IAP existuje za účelem plnění zákonných povinností ukládaných telekomunikačním poskytovatelům národními zákony, které vyžadují, aby operátoři pomáhali orgánům činným v trestním řízení a bezpečnostním složkám se zákonným odposlechem komunikací. Jeho vytvoření bylo motivováno potřebou standardizovaného, bezpečného a spolehlivého technického mechanismu, který funguje napříč různými zařízeními výrobců a generacemi sítí (2G až 5G). Bez standardizovaného IAP by každý operátor a výrobce implementoval proprietární odposlechová řešení, což by orgánům činným v trestním řízení ztěžovalo a prodražovalo konzistentní přístup k odposlechnutým datům a potenciálně brzdilo vyšetřování.

Problém, který řeší, je dvojí: technická implementace a soulad s regulacemi. Technicky poskytuje dobře definovaný bod a postup pro přístup k síťovému provozu v reálném čase bez degradace služby pro ostatní uživatele. Z pohledu souladu zajišťuje, že odposlech je prováděn v souladu s přísnými zákonnými a procesními zárukami, při zachování jasné auditní stopy. Historický kontext zahrnuje vývoj telekomunikací od jednoduchých okruhově přepínaných hlasových služeb ke komplexním IP multimediálním službám, což vyžadovalo odpovídající vývoj odposlechových schopností. Standardy LI od 3GPP, včetně konceptu IAP, řeší omezení dřívějších nestandardizovaných odposlechových metod tím, že poskytují budoucím vývoji odolný, na technologii nezávislý rámec, který chrání soukromí uživatelů mimo zákonné mandáty a zajišťuje interoperabilitu mezi síťovými operátory a orgány činnými v trestním řízení.

## Klíčové vlastnosti

- Duplikuje Komunikační obsah (CC) a Odposlechové související informace (IRI)
- Spolupracuje s interní Administrativní funkcí (ADMF) pro aktivaci
- Využívá standardizovaná Předávací rozhraní (HI2, HI3) pro doručení do LEMF
- Může být implementován v různých síťových funkcích (např. UPF, MSC, IMS uzly)
- Funguje utajeně bez upozornění odposlouchávaného účastníka
- Podporuje bezpečnostní funkce pro integritu a důvěrnost dat

## Související pojmy

- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)
- [LEMF – Law Enforcement Monitoring Facility](/mobilnisite/slovnik/lemf/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [IAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/iap/)
