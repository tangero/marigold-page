---
slug: "msisdn"
url: "/mobilnisite/slovnik/msisdn/"
type: "slovnik"
title: "MSISDN – Mobile Station International Subscriber Directory Number"
date: 2026-01-01
abbr: "MSISDN"
fullName: "Mobile Station International Subscriber Directory Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msisdn/"
summary: "MSISDN je veřejné telefonní číslo používané k volání mobilního účastníka. Jde o globálně jednoznačné číslo E.164 uložené v HLR/HSS a je zásadní pro směrování hovorů a SMS v přepojování okruhů a v sítí"
---

MSISDN je globálně jednoznačné veřejné telefonní číslo, které se řídí formátem E.164 a používá se k volání mobilního účastníka a k směrování hovorů a SMS zpráv.

## Popis

Mobile Station International Subscriber Directory Number (MSISDN) je primární, mezinárodně standardizovaný identifikátor mobilního účastníka ve veřejné telefonní síti (PSTN) a v digitální síti s integrovanými službami ([ISDN](/mobilnisite/slovnik/isdn/)). Řídí se číslovacím plánem [ITU-T](/mobilnisite/slovnik/itu-t/) E.164 a skládá se z kódu země ([CC](/mobilnisite/slovnik/cc/)), z národního směrovacího čísla ([NDC](/mobilnisite/slovnik/ndc/)), které často identifikuje operátora mobilní sítě, a z čísla účastníka (SN). Toto číslo není uloženo na samotné SIM kartě, ale je klíčovým datovým prvkem v profilu účastníka v registru domácích účastníků ([HLR](/mobilnisite/slovnik/hlr/)) v sítích GSM/UMTS nebo na serveru domácích účastníků ([HSS](/mobilnisite/slovnik/hss/)) v sítích LTE/5G. MSISDN je odděleno od hardwarové identity zařízení ([IMEI](/mobilnisite/slovnik/imei/)) a identity SIM karty ([IMSI](/mobilnisite/slovnik/imsi/)), což umožňuje účastníkovi měnit zařízení při zachování čísla a umožňuje přenosnost čísel mezi operátory.

V síťových operacích je MSISDN hlavní adresou používanou pro směrování příchozích hlasových hovorů a SMS zpráv. Když je uskutečněno volání na MSISDN, volající síť dotazuje příslušnou databázi přenosnosti čísel a poté směruje hovor do domácí sítě účastníka. Gateway MSC (GMSC) domácí sítě používá MSISDN k dotazování HLR/HSS za účelem získání aktuálních směrovacích informací, konkrétně Mobile Station Roaming Number (MSRN) nebo IP adresy obsluhujícího MSC nebo SMSC. Tento proces umožňuje doručení hovoru nebo zprávy na aktuální polohu účastníka, ať už je v domácí síti nebo v roamingu.

Role MSISDN přesahuje základní služby s přepojováním okruhů. V IP Multimedia Subsystem (IMS) může být MSISDN použito jako veřejná uživatelská identita (IMPU) pro služby založené na SIP, jako je VoLTE a ViLTE, což umožňuje interoperabilitu s uživateli starších sítí PSTN/PLMN. Je také klíčovým prvkem pro správu účastníků, účtování a zákonné odposlechy. Oddělení MSISDN od IMSI poskytuje provozní flexibilitu; například jediné IMSI (a tedy jediné předplatné) může být spojeno s více MSISDN pro služby jako hlas a fax nebo pro firemní linky. Jeho standardizovaný, globálně směrovatelný formát je základem pro globální mobilní telekomunikace.

## K čemu slouží

MSISDN bylo vytvořeno za účelem poskytnutí standardizovaného, uživatelsky přívětivého a globálně jednoznačného adresovacího schématu pro mobilní účastníky, analogického telefonním číslům ve fixní síti. Před standardizací v celulárních sítích používaly různé nekompatibilní rádiové systémy odlišné metody identifikace, což bránilo interoperabilitě a mezinárodnímu roamingu. Zavedení MSISDN založeného na E.164 v rámci GSM a následných technologií 3GPP tento problém vyřešilo tím, že poskytlo konzistentní číslo, které mohli uživatelé sdílet a které sítě mohly používat pro směrování hovorů po celém světě.

Jeho návrh odděluje veřejnou identitu účastníka (MSISDN) od jeho privátní síťové identity (IMSI) a identity zařízení (IMEI). Toto oddělení je klíčové pro bezpečnost, soukromí a provozní flexibilitu. Umožňuje mobilitu účastníka a přenosnost čísel bez změny fyzické SIM karty nebo zařízení. MSISDN umožňuje mobilní síti bezproblémově komunikovat s globální sítí PSTN/ISDN, čímž se mobilní telefon stal skutečným rozšířením celosvětového telefonního systému. Vyřešilo základní problém, jak najít a směrovat hovor k mobilnímu účastníkovi, jehož poloha není pevná, tím, že jej používá jako stabilní klíč pro dotazování na dynamické směrovací informace z HLR.

## Klíčové vlastnosti

- Řídí se mezinárodním číslovacím plánem ITU-T E.164
- Globálně jednoznačný veřejný identifikátor účastníka pro směrování hovorů a SMS
- Oddělen od IMSI a IMEI pro provozní flexibilitu
- Uložen v HLR/HSS jako součást profilu účastníka
- Může sloužit jako veřejná uživatelská identita (IMPU) v IMS
- Umožňuje přenosnost mobilních čísel (MNP) mezi operátory

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 22.085** (Rel-19) — Closed User Group (CUG) Supplementary Service
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.863** (Rel-12) — SMS over IMS for MSISDN-less UEs
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [MSISDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/msisdn/)
