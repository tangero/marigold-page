---
slug: "oid"
url: "/mobilnisite/slovnik/oid/"
type: "slovnik"
title: "OID – Organisation Identifier"
date: 2025-01-01
abbr: "OID"
fullName: "Organisation Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oid/"
summary: "Globálně jednoznačný identifikátor přidělený organizaci, jako je normalizační orgán (např. ITU-T, 3GPP) nebo výrobce. Používá se v rámci řídicích protokolů a informačních modelů k jednoznačné identifi"
---

OID je globálně jednoznačný identifikátor přidělený organizaci, který umožňuje nedvojznačně identifikovat definující autoritu pro spravované objekty v rámci protokolů pro správu sítě.

## Popis

Organisation Identifier (OID) je hierarchický, globálně jednoznačný identifikátor hojně využívaný v telekomunikacích a informačních technologiích pro pojmenovávání a identifikaci objektů. V kontextu norem 3GPP se OID používají v rámci řídicích rámců, datových jednotek protokolů a informačních modelů, aby poskytly jednoznačný způsob odkazování na organizaci, která definovala konkrétní informaci, třídu spravovaného objektu, atribut nebo celou podstromovou část stromu řídicích informací. OID je reprezentován jako posloupnost celých čísel oddělených tečkami (např. 0.0.0.0.0.0).

Struktura OID se řídí normami [ITU-T](/mobilnisite/slovnik/itu-t/) X.660 a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 9834-1. Tvoří stromovou hierarchii, kde každý oblouk (číslo) představuje uzel. Kořen má tři oblouky: 0 (ITU-T), 1 (ISO) a 2 (joint-iso-itu-t). Odtud přidělují podřízené identifikátory příslušné registrační autority. Například 3GPP bylo přiděleno konkrétní OID pod větví joint-iso-itu-t(2). Tento hierarchický systém zaručuje, že žádné dvě nezávisle registrované entity nikdy nebudou mít stejný OID, čímž předchází kolizím v pojmenování v prostředích s více výrobci a standardy.

V rámci systémů pro správu 3GPP mají OID několik klíčových aplikací. Za prvé se používají v Common Management Information Protocol ([CMIP](/mobilnisite/slovnik/cmip/)) a jeho nástupci Simple Network Management Protocol ([SNMP](/mobilnisite/slovnik/snmp/)) k identifikaci modulů Management Information Base ([MIB](/mobilnisite/slovnik/mib/)) definovaných 3GPP nebo jednotlivými výrobci zařízení. Když systém pro správu sítě přijme trap nebo čte objekt, předpona OID mu určí, které definice MIB od které organizace má použít pro interpretaci. Za druhé se OID používají v protokolu Diameter, klíčovém protokolu pro autentizaci, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/)). V Diametru mohou OID identifikovat konkrétní výrobce (Vendor-Id) nebo být použity v rámci Attribute-Value Pairs ([AVP](/mobilnisite/slovnik/avp/)) pro kvalifikaci výrobcem specifických atributů.

Proces přidělování a registrace OID je formální. 3GPP jako organizace spravuje svou vlastní podstromovou část OID a přiděluje podoblouky pro své vlastní technické specifikace (např. pro různá vydání nebo pracovní skupiny) a v některých případech i pro registrované výrobce. Tím vzniká strukturovaný jmenný prostor, kde může být každý spravovaný objekt, od výkonnostního čítače pro 5G gNB po výrobcem specifický příznak funkce v HSS, přesně a jednoznačně pojmenován. Tato přesnost je nezbytná pro interoperabilitu, automatizovanou provizi a správu sítí s více výrobci, kde musí být zdroj a sémantika každého kusu řídicích dat naprosto jasné.

## K čemu slouží

Organisation Identifier byl vytvořen k řešení základního problému jednoznačné identifikace a pojmenování v distribuovaných systémech s více organizacemi. Před rozšířeným přijetím OID používaly různé normalizační orgány, společnosti a konsorcia své vlastní ad-hoc systémy pojmenování, což vedlo ke konfliktům, nejednoznačnosti a závažným problémům s interoperabilitou při integraci systémů z různých zdrojů. Hierarchie OID, standardizovaná ITU a ISO, poskytuje univerzální 'telefonní seznam' pro přidělování globálně jednoznačných jmen čemukoliv, co je potřebuje.

V konkrétní oblasti správy sítí 3GPP bylo použití OID motivováno potřebou výrobně neutrálních, ale rozšiřitelných rámců pro správu. Jelikož jsou sítě 3GPP budovány integrací zařízení a softwaru od četných výrobců, byl společný jazyk pro správu nezbytný. Informační modely pro správu definované 3GPP používají OID k deklarování vlastnictví svých definic objektů. Současně architektura umožňuje výrobcem specifická rozšíření – výrobce si může zaregistrovat vlastní podstromovou část OID a definovat pod ní proprietární spravované objekty. Tím se řeší napětí mezi standardizací (pro interoperabilitu) a inovacemi (pro diferenciaci výrobců).

OID navíc poskytují ochranu do budoucna a škálovatelnost. Hierarchický strom je v podstatě nekonečný, což umožňuje delegování registrační autority. 3GPP může delegovat podoblouk výrobci a ten může dále delegovat jeho části, čímž vzniká škálovatelný jmenný prostor. Tato struktura podporuje dlouhodobý vývoj sítí, kde jsou neustále zaváděny nové typy uzlů, nové protokoly a nové řídicí parametry. Použitím OID zajišťuje 3GPP, že každá nová spravovaná entita, bez ohledu na její původ, může být integrována do ekosystému správy bez kolizí v pojmenování, čímž vytváří robustní základnu pro OAM vrstvu, která spravuje celý životní cyklus sítě.

## Klíčové vlastnosti

- Globálně jednoznačný, hierarchický identifikátor podle ITU-T X.660/ISO 9834-1
- Reprezentován jako tečkami oddělený řetězec celých čísel (např. 1.3.6.1.4.1.3GPP)
- Jednoznačně identifikuje definující autoritu (organizaci) spravovaného objektu
- Používá se jako kořen pro definice Management Information Base (MIB) od 3GPP a od výrobců
- Využívá se v řídicích protokolech jako SNMP a CMIP pro pojmenování objektů
- Používá se v protokolu Diameter pro Vendor-Id a výrobcem specifická AVP

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [SNMP – Simple Network Management Protocol](/mobilnisite/slovnik/snmp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [OID na 3GPP Explorer](https://3gpp-explorer.com/glossary/oid/)
