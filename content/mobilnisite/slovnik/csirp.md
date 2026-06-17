---
slug: "csirp"
url: "/mobilnisite/slovnik/csirp/"
type: "slovnik"
title: "CSIRP – Communication Surveillance Integration Reference Point"
date: 2025-01-01
abbr: "CSIRP"
fullName: "Communication Surveillance Integration Reference Point"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/csirp/"
summary: "CSIRP je standardizované rozhraní definované 3GPP pro zákonné odposlechy (LI) a sledování komunikací. Umožňuje oprávněným orgánům činným v trestním řízení (LEA) zabezpečeně a spolehlivě zachytávat obs"
---

CSIRP je standardizované rozhraní 3GPP, které umožňuje zákonné odposlechy tím, že poskytuje oprávněným orgánům zabezpečený přístup k obsahu komunikací a datům z telekomunikačních sítí.

## Popis

Communication Surveillance Integration Reference Point (CSIRP) je klíčová součást architektury pro zákonné odposlechy ([LI](/mobilnisite/slovnik/li/)) definované 3GPP, specifikovaná v technických specifikacích (TS) řady 32. Slouží jako standardizovaný, na dodavateli nezávislý referenční bod, který definuje rozhraní mezi funkcí zákonného odposlechu ([LIF](/mobilnisite/slovnik/lif/)) síťového operátora a monitorovacím zařízením orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)), které provozují oprávněné orgány. CSIRP není jediné fyzické rozhraní, ale komplexní logická a protokolová specifikace, která zajišťuje zabezpečené, spolehlivé a standardizované doručování zachyceného obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)) a informací souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) ze sítě k příslušnému orgánu.

Architektonicky CSIRP funguje v rámci předávacího rozhraní ([HI](/mobilnisite/slovnik/hi/)) modelu LI dle 3GPP. Doména síťového operátora obsahuje mediační funkci ([MF](/mobilnisite/slovnik/mf/)) a administrační funkci ([ADMF](/mobilnisite/slovnik/admf/)), které spravují příkazy k odposlechu a shromažďují data z různých síťových prvků, jako jsou MSC, SGSN, MME nebo P-GW. CSIRP definuje, jak jsou tato shromážděná data formátována, zabalena a přenesena přes HI do LEMF. Specifikuje protokoly, datové formáty, bezpečnostní mechanismy a provozní postupy. Mezi klíčové součásti specifikace CSIRP patří definice sad zpráv pro aktivaci, deaktivaci a dotazování na odposlechy, stejně jako strukturované kódování IRI (metadata jako podrobnosti o volání, lokalizace) a CC (samotný hlasový nebo datový přenos).

Z technického hlediska CSIRP zajišťuje interoperabilitu. Umožňuje, aby se systém LEMF orgánu činného v trestním řízení, potenciálně dodaný jedním výrobcem, bezproblémově připojil k systému LI operátora od jiného výrobce, pokud oba implementují standardy 3GPP CSIRP. Specifikace (např. TS 32.351, 32.352) detailně popisují protokoly aplikační vrstvy, které jsou často založeny na standardizované IP přenosové vrstvě. Definují přesná XML schémata nebo ASN.1 kódování pro data odposlechu, což zajišťuje konzistentní prezentaci informací, jako je číslo volané strany, časová razítka a identifikátory obsahu. Bezpečnost je prvořadá; specifikace CSIRP ukládají použití robustních mechanismů pro autentizaci, integritu a důvěrnost přenášených zachycených dat, čímž je chrání před neoprávněným přístupem nebo manipulací.

V praxi, když je prostřednictvím ADMF aktivován příkaz k zákonnému odposlechu, příslušné síťové prvky (např. Gateway GPRS Support Node pro paketová data) začnou duplikovat provoz cílového účastníka. MF tato data naformátuje podle pravidel CSIRP a vytvoří standardizované hlášení IRI a CC. Tato hlášení jsou následně doručena přes zabezpečené HI, implementované podle CSIRP, do LEMF. LEMF používá vlastní interní rozhraní (nedefinovaná 3GPP) k prezentaci těchto informací vyšetřovatelům. Úlohou CSIRP je tedy být kritickým, standardizovaným 'předávacím bodem', který spojuje interní síťové funkce operátora a externí doménu orgánů činných v trestním řízení, a zajišťuje tak technickou proveditelnost splnění zákonných požadavků v prostředí s více dodavateli a více sítěmi.

## K čemu slouží

CSIRP byl vytvořen, aby řešil základní výzvu v telekomunikační regulaci a činnosti orgánů činných v trestním řízení: umožnit legální sledování při zvládání komplexnosti moderních mobilních sítí s více dodavateli. Před jeho standardizací síťoví operátoři a výrobci zařízení implementovali proprietární rozhraní pro předávání zachycených dat orgánům činným v trestním řízení. To vytvářelo významné problémy s interoperabilitou, zvyšovalo náklady operátorů, kteří museli podporovat více rozhraní LEMF, a komplikovalo práci orgánům, které potřebovaly různé systémy pro různé operátory nebo země. Nedostatek společného standardu bránil efektivní mezistátní spolupráci a činil plnění národních zákonů o zákonných odposleších technicky náročným a nekonzistentním.

Primární problém, který CSIRP řeší, je tento nedostatek interoperability a standardizace. Definováním univerzálního referenčního bodu umožnilo 3GPP jasné oddělení kompetencí. Výrobci síťového vybavení (např. Ericsson, Nokia) mohli stavět své mediační funkce tak, aby výstupní data byla ve formátu CSIRP, a výrobci řešení pro orgány činné v trestním řízení mohli stavět systémy LEMF, které tento stejný formát přijímají. Tím se oddělují vývojové cykly síťového a LEMF vybavení, což podporuje konkurenční trh pro obě strany. Pro síťové operátory to zjednodušuje plnění povinností, protože mohou pořizovat řešení LI s vědomím, že budou fungovat se systémy jejich národních LEA, pokud jsou tyto systémy také kompatibilní s CSIRP.

Historicky jeho zavedení v Release 8 časově souviselo s úplnou definicí Evolved Packet System (EPS) pro LTE. Jak se sítě vyvíjely od okruhově přepínaných 2G/3G k plně IP 4G sítím, potřebovaly odpovídající vývoj i metody pro zachytávání komunikací. CSIRP jako součást širší architektury LI 3GPP poskytl perspektivní, na IP založený rámec pro sledování, který dokáže zpracovávat nejen hlasová volání, ale také paketové datové relace, IMS služby a nakonec i aplikace pro zasílání zpráv. Byl motivován potřebou technicky robustního, právně obhajitelného a škálovatelného mechanismu odposlechu, který by dokázal držet krok s rychlým technologickým vývojem, a zároveň zachovávat právní stát a ochranu soukromí požadovanou národními regulacemi.

## Klíčové vlastnosti

- Standardizovaný protokol a datový formát pro předání dat zákonného odposlechu
- Definuje rozhraní mezi mediační funkcí síťového operátora a monitorovacím zařízením orgánů činných v trestním řízení
- Specifikuje zabezpečený přenos informací souvisejících s odposlechem (IRI) a obsahu komunikace (CC)
- Zajišťuje interoperabilitu mezi systémy sítí a orgánů činných v trestním řízení od různých dodavatelů
- Podporuje aktivaci, deaktivaci a dotazování na odposlechy prostřednictvím standardizovaných zpráv
- Poskytuje rámec pro zpracování různých služeb (okruhově přepínané, paketově přepínané, IMS)

## Definující specifikace

- **TS 32.351** (Rel-19) — Communication Surveillance IRP Requirements
- **TS 32.352** (Rel-19) — Communication Surveillance IRP Information Service
- **TS 32.353** (Rel-9) — Communication Surveillance IRP CORBA Solution Set
- **TS 32.355** (Rel-9) — Communication Surveillance IRP XML Definitions
- **TS 32.356** (Rel-19) — Communication Surveillance IRP Solution Set
- **TS 32.357** (Rel-9) — Communication Surveillance IRP SOAP Solution Set

---

📖 **Anglický originál a plná specifikace:** [CSIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/csirp/)
