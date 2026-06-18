---
slug: "dn"
url: "/mobilnisite/slovnik/dn/"
type: "slovnik"
title: "DN – Distinguished Name"
date: 2026-01-01
abbr: "DN"
fullName: "Distinguished Name"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/dn/"
summary: "Strukturovaný, hierarchický identifikátor používaný v rámci systémů správy 3GPP pro jednoznačné pojmenování a lokalizaci spravovaných objektů, jako jsou síťové prvky, konfigurační parametry nebo výkon"
---

DN (Distinguished Name) je strukturovaný, hierarchický identifikátor používaný v rámci systémů správy 3GPP pro jednoznačné pojmenování a lokalizaci spravovaných objektů, jako jsou síťové prvky nebo konfigurační parametry.

## Popis

Distinguished Name (DN) je klíčový koncept v architektuře Telekomunikační správní sítě ([TMN](/mobilnisite/slovnik/tmn/)) a správy sítě ([NM](/mobilnisite/slovnik/nm/)) podle 3GPP, silně založený na modelu adresáře [OSI](/mobilnisite/slovnik/osi/) X.500. Poskytuje globálně jednoznačnou hierarchickou cestu k identifikaci jakékoli instance spravovaného objektu ve stromu správních informací. DN je konstruován jako sekvence Relativních Distinguished Names ([RDN](/mobilnisite/slovnik/rdn/)), kde každý RDN je pár atribut-hodnota (např. `SubNetwork=PLMN-PLMN`, `ManagedElement=ME123`). Tato sekvence začíná od kořene správního stromu a postupuje dolů ke konkrétnímu objektu, čímž vytváří jednoznačnou adresu, například `SubNetwork=PLMN-PLMN/ManagedElement=ME123/Equipment=1`. Tato struktura odráží fyzickou nebo logickou hierarchii sítě, jako je Network, SubNetwork, Managed Element a Equipment.

V provozu je DN primárním klíčem používaným na všech správních rozhraních, zejména na Itf-N (northbound rozhraní) a v rámci frameworku Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)) definovaného ve specifikacích řady 32. Když Network Manager (NM) nebo Element Manager ([EM](/mobilnisite/slovnik/em/)) potřebuje získat výkonnostní měření, nakonfigurovat parametr nebo přijmout notifikaci o poruše, použije DN k určení přesného cílového objektu. Informační služba ([IS](/mobilnisite/slovnik/is/)) správního systému používá tyto DN k organizaci a získávání dat ze svých úložišť spravovaných objektů. Hierarchická povaha umožňuje efektivní vymezení rozsahu operací; například správce může požadovat všechny alarmy pro konkrétní `SubNetwork` použitím jeho DN jako filtru rozsahu.

Role DN je klíčová pro zajištění konzistence, sledovatelnosti a automatizace v síťové správě. Odděluje logickou identitu zdroje od jeho fyzické IP adresy nebo jiných přechodných identifikátorů. To je zásadní pro více-dodavatelská prostředí a pro úlohy správy životního cyklu, jako jsou softwarové aktualizace nebo rozšiřování kapacity, kdy mohou být objekty překonfigurovány nebo nahrazeny. Komplexní soubor konvencí pojmenování a pravidel pro konstrukci DN je podrobně definován v 3GPP TS 32.300, což zajišťuje interoperabilitu mezi různými správními systémy a síťovými prvky od různých dodavatelů.

## K čemu slouží

Distinguished Name byl zaveden k řešení základního problému jednoznačné a konzistentní identifikace milionů konfigurovatelných a monitorovatelných entit v komplexní, více-dodavatelské telekomunikační síti. Před standardizovaným hierarchickým pojmenováním správní systémy spoléhaly na proprietární nebo ploché adresní schémata, což vedlo k problémům s integrací, nejednoznačným referencím a neschopnosti automatizovat rozsáhlé operace. DN poskytuje jednotný 'adresář' pro celou síť.

Jeho vytvoření bylo motivováno frameworkem správy systémů [OSI](/mobilnisite/slovnik/osi/) a potřebou robustní Telekomunikační správní sítě (TMN) s rostoucím rozsahem a složitostí sítí. Hierarchická struktura přímo modeluje vlastní architekturu sítě, což ji činí intuitivní pro inženýry a škálovatelnou pro software. Řeší omezení jednoduchých jmen nebo indexů vložením relačního kontextu; DN objektu implicitně ukazuje jeho začlenění do konkrétní lokality, síťového řezu nebo domény dodavatele.

Tato schopnost je základem pro automatizované zřizování, korelaci poruch a správu výkonnosti. Poskytnutím stabilního, logického identifikátoru umožňuje správním aplikacím spolehlivě odkazovat na síťový zdroj po celou dobu jeho životního cyklu, i když se mění jeho fyzické charakteristiky nebo připojení. To je nezbytné pro moderní, softwarem řízené operace.

## Klíčové vlastnosti

- Globálně jednoznačná identifikace instancí spravovaných objektů
- Hierarchická struktura odrážející organizaci sítě nebo zdrojů
- Skládá se z sekvence Relativních Distinguished Names (RDN)
- Základ pro vymezení rozsahu a filtrování v správních operacích
- Standardizovaná syntaxe a pravidla definovaná v 3GPP TS 32.300
- Odděluje logickou správní identitu od fyzické adresace

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.791** (Rel-16) — NWDAF Data Collection & Analytics Framework
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.502** (Rel-19) — 5G Multicast-Broadcast User Services Architecture
- … a dalších 114 specifikací

---

📖 **Anglický originál a plná specifikace:** [DN na 3GPP Explorer](https://3gpp-explorer.com/glossary/dn/)
