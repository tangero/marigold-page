---
slug: "bsf"
url: "/mobilnisite/slovnik/bsf/"
type: "slovnik"
title: "BSF – Bootstrapping Server Function"
date: 2026-01-01
abbr: "BSF"
fullName: "Bootstrapping Server Function"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/bsf/"
summary: "Bootstrapping Server Function (BSF) je síťová funkce jádra v rámci architektury Generic Authentication Architecture (GAA). Poskytuje bezpečnou metodu pro aplikace a síťové funkce, aby dynamicky získáv"
---

BSF je Bootstrapping Server Function, prvek jádra sítě, který poskytuje aplikacím a síťovým funkcím bezpečné, dynamicky generované autentizační údaje a kryptografické klíče.

## Popis

Bootstrapping Server Function (BSF) je ústřední komponenta architektury Generic Authentication Architecture ([GAA](/mobilnisite/slovnik/gaa/)) konsorcia 3GPP, definovaná jako bezpečnostní rámec pro autentizaci a dohodu klíčů. Funguje jako samostatná síťová funkce, která komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) za účelem provádění bootstrapping procedur. Základní princip spočívá ve využití existujícího silného ověření mezi uživatelským zařízením (UE) a mobilní sítí (prostřednictvím protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/))) k odvození specifických bezpečnostních přihlašovacích údajů pro aplikace. Tento proces, známý jako 'bootstrapping', vytváří sdílené tajemství mezi UE a Network Application Function ([NAF](/mobilnisite/slovnik/naf/)) bez nutnosti předchozí přímé bezpečnostní asociace.

Architektonicky je BSF entita na straně serveru, která komunikuje s UE (vystupující jako klient GAA) a s NAF. Procedura začíná, když UE kontaktuje BSF k zahájení bootstrappingu. BSF následně komunikuje s HSS/UDM, aby získala autentizační vektory (např. kvintety pro UMTS AKA nebo vektory pro EPS AKA/5G AKA). Pomocí těchto vektorů vyzve UE k ověření. Po úspěšné vzájemné autentizaci nezávisle vypočítají jak BSF, tak UE sdílený, na relaci specifický kořenový klíč nazývaný Bootstrapping Transaction Identifier ([B-TID](/mobilnisite/slovnik/b-tid/)) a související klíčový materiál (Ks). Toto Ks je dlouhodobý klíč odvozený z AKA relace.

Role BSF spočívá v tom, že funguje jako důvěryhodný generátor a distributor klíčů. Po bootstrappingu, když UE potřebuje přístup ke službě poskytované konkrétní NAF (např. serveru Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), službě založené na poloze nebo aplikačnímu serveru 3GPP), předá UE NAF identifikátor B-TID. NAF následně dotazuje BSF pomocí B-TID, aby získala příslušný klíčový materiál (NAF-specifický klíč, Ks_NAF, odvozený z Ks) pro danou služební relaci. To umožňuje NAF a UE navázat zabezpečený kanál. BSF tedy odděluje autentizaci v jádru sítě od zabezpečení na aplikační vrstvě, což umožňuje širokému spektru služeb využívat robustní infrastrukturu buněčné autentizace.

Klíčová rozhraní BSF zahrnují rozhraní Ub směrem k UE pro bootstrapping proceduru, rozhraní Zn směrem k NAF pro distribuci klíčů a rozhraní Zh směrem k HSS nebo UDM pro získávání autentizačních dat. V systémech 5G se BSF přizpůsobuje servisně orientované architektuře a potenciálně vystavuje své schopnosti jako služba síťové funkce ([NF](/mobilnisite/slovnik/nf/)). Její implementace je klíčová pro umožnění bezpečné, standardizované a škálovatelné autentizace pro přidané služby napříč sítěmi 3GPP, 4G a 5G a tvoří základ mnoha bezpečnostních řešení založených na GAA.

## K čemu slouží

BSF byla vytvořena, aby vyřešila základní problém, jak bezpečně autentizovat uživatele a zařízení vůči mnoha aplikačním serverům (NAF), aniž by každá aplikace musela spravovat vlastní samostatnou databázi přihlašovacích údajů nebo navazovat přímý vztah důvěry s jádrem mobilní sítě. Před GAA aplikace používaly buď slabá, aplikací specifická hesla, nebo vyžadovaly složitou, mimopásmovou provizi certifikátů nebo sdílených klíčů, což nebylo škálovatelné a bylo náchylné k útokům. BSF poskytuje standardizovanou metodu řízenou operátorem sítě pro opětovné využití silné, na předplatném založené autentizace mobilní sítě.

Primární motivací bylo umožnit nové, bezpečné mobilní služby – jako je ochrana vysílání/vícevysílání obsahu (MBMS), zabezpečená správa zařízení, finanční transakce a zákonné odposlechy – tím, že jim poskytla spolehlivý zdroj kryptografických klíčů odvozených z autentizace SIM/USIM uživatele. BSF řeší problém distribuce klíčů škálovatelným způsobem. Umožňuje mobilnímu operátorovi vystupovat jako důvěryhodná třetí strana, která generuje a poskytuje relakční klíče autorizovaným poskytovatelům aplikací, čímž vytváří obchodně-obchodní bezpečnostní rámec. To usnadnilo bezpečnou komercializaci mobilních služeb přesahujících základní hlas a data.

Historicky zavedená v 3GPP Release 6 jako součást GAA, BSF řešila bezpečnostní potřeby vznikajících služeb IP Multimedia Subsystem (IMS) a dalších síťových aplikací. Poskytla architekturu připravenou na budoucnost, která se vyvinula přes 4G až do 5G, kde její role zůstává nezbytná pro servisně orientované zabezpečení, zejména ve scénářích vystavení sítě. Řeší omezení statického, předem nakonfigurovaného zabezpečení tím, že umožňuje dynamické, na požadavek založené vytváření klíčů, které je vázáno na aktuální stav síťové autentizace uživatele.

## Klíčové vlastnosti

- Poskytuje dynamické, na požadavek odvození aplikačně specifických kryptografických klíčů (Ks_NAF) z autentizace jádra sítě (AKA).
- Umožňuje vzájemnou autentizaci mezi uživatelským zařízením (UE) a Bootstrapping Server Function.
- Funguje jako důvěryhodné centrum distribuce klíčů pro Network Application Functions (NAF) prostřednictvím rozhraní Zn.
- Podporuje autentizační vektory pro 3G (UMTS), 4G (EPS) i 5G prostřednictvím rozhraní s HSS a UDM.
- Odděluje zabezpečení na aplikační vrstvě od zabezpečení přístupu k jádru sítě, což podporuje inovace služeb.
- Tvoří základní prvek architektury Generic Authentication Architecture (GAA) pro zabezpečení širokého spektra služeb.

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 29.309** (Rel-19) — Nbsp Service Based Interface for GBA BSF
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.810** (Rel-13) — Diameter Load Control Study
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.110** (Rel-19) — UICC-Terminal Key Establishment
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.185** (Rel-19) — V2X Security in LTE
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [BSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsf/)
