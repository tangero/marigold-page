---
slug: "vin"
url: "/mobilnisite/slovnik/vin/"
type: "slovnik"
title: "VIN – Vehicle Identity Number"
date: 2025-01-01
abbr: "VIN"
fullName: "Vehicle Identity Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vin/"
summary: "Globálně jednoznačný, standardizovaný 17místný identifikátor pro jednotlivá motorová vozidla, definovaný normou ISO 3779. V kontextu 3GPP se používá pro identifikaci vozidel v telematických a V2X služ"
---

VIN (Vehicle Identity Number) je globálně jednoznačný, standardizovaný 17místný identifikátor vozidla používaný v 3GPP pro identifikaci vozidel v telematických a V2X službách.

## Popis

Vehicle Identity Number (VIN) je klíčový identifikátor v automobilovém a telekomunikačním průmyslu, který slouží jako jedinečný otisk každého motorového vozidla. Definovaný normou [ISO](/mobilnisite/slovnik/iso/) 3779 se jedná o 17místný alfanumerický kód poskytující globálně jednoznačnou identitu. Struktura VIN je přesně definována: první tři znaky představují World Manufacturer Identifier (WMI), který identifikuje výrobce vozidla a zemi původu. Znaky 4 až 9 tvoří Vehicle Descriptor Section (VDS), která podrobně popisuje atributy jako model, typ karoserie, typ motoru a bezpečnostní systémy. Posledních osm znaků tvoří Vehicle Identifier Section (VIS), která zahrnuje kód modelového roku, kód výrobního závodu a sériové výrobní číslo, čímž zajišťuje jedinečnost každého vozidla.

Ve standardech 3GPP je VIN integrován jako klíčový identifikátor pro telematické služby a komunikaci Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). Je odkazován ve specifikacích jako 22.967 pro požadavky na služby. VIN používají síťové funkce k jednoznačné identifikaci palubní jednotky vozidla (OBU) nebo uživatelského zařízení (UE) spojeného s vozidlem. Tato identifikace je zásadní pro služby jako nouzové volání (eCall), sledování odcizených vozidel, dálková diagnostika, správa vozového parku a různé V2X aplikace. Síť může korelovat VIN s dalšími identifikátory, jako je International Mobile Equipment Identity ([IMEI](/mobilnisite/slovnik/imei/)) nebo identifikátory předplatného, aby vytvořila komplexní profil vozidla.

Technická role VIN v architekturách 3GPP zahrnuje jeho uložení a zpracování. Může být uložen v OBU vozidla nebo v embedded UICC (eUICC) a přenášen přes mobilní síť na aplikační servery nebo specifické síťové funkce. Ve scénářích V2X lze VIN použít pro autorizační a bezpečnostní účely, což zajišťuje, že zprávy pocházejí z legitimních, identifikovatelných vozidel. Jeho standardizovaný formát umožňuje interoperabilitu mezi různými výrobci, síťovými operátory a poskytovateli služeb, čímž tvoří základnu pro škálovatelné, globální telematické ekosystémy a ekosystémy připojených vozidel.

## K čemu slouží

VIN existuje k vyřešení základního problému jednoznačné a nedvojznačné identifikace jednotlivých motorových vozidel v globálním měřítku. Před jeho standardizací byla identifikace vozidel roztříštěná, často se spoléhala na výrobcem specifická schémata, která bránila interoperabilitě pro registraci, pojištění, orgány činné v trestním řízení a vznikající telematické služby. Vytvoření normy [ISO](/mobilnisite/slovnik/iso/) 3779 poskytlo univerzální jazyk pro identitu vozidla, který se stal nepostradatelným, když se vozidla vyvinula z čistě mechanických zařízení na připojené entity.

Začlenění VIN do standardů 3GPP bylo motivováno vzestupem telematických služeb a služeb připojených vozidel založených na mobilních sítích. Pro aplikace jako automatické nouzové volání (eCall) je zásadní, aby záchranné služby obdržely přesný identifikátor vozidla, aby mohly vyslat odpovídající pomoc a získat podrobnosti o vozidle (např. model, typ paliva) z národních databází. Pro komerční telematiku potřebují manažeři vozového parku spolehlivý klíč ke sledování polohy, využití a stavu vozidla. V komunikaci [V2X](/mobilnisite/slovnik/v2x/) poskytuje VIN vrstvu identity pro správu bezpečnostních přihlašovacích údajů a přiřazení zpráv, čímž řeší potřebu důvěry a odpovědnosti v bezpečnostně kritických vozidlových sítích. VIN tedy propojuje svět automobilový a telekomunikační a umožňuje novou třídu síťově orientovaných vozidlových služeb.

## Klíčové vlastnosti

- Globálně jednoznačný 17místný alfanumerický identifikátor
- Standardizovaná struktura dle ISO 3779 (sekce WMI, VDS, VIS)
- Umožňuje jednoznačnou identifikaci vozidla pro síťové služby
- Nezbytný pro telematické aplikace jako eCall a sledování odcizených vozidel
- Podporuje identitu vozidla v bezpečnostních rámcích komunikace V2X
- Poskytuje interoperabilitu mezi automobilovými výrobci (OEM) a poskytovateli telekomunikačních služeb

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission

---

📖 **Anglický originál a plná specifikace:** [VIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/vin/)
