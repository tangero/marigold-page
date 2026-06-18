---
slug: "atcf"
url: "/mobilnisite/slovnik/atcf/"
type: "slovnik"
title: "ATCF – Access Transfer Control Function"
date: 2025-01-01
abbr: "ATCF"
fullName: "Access Transfer Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/atcf/"
summary: "Access Transfer Control Function (ATCF) je síťový prvek 3GPP, který řídí plynulý přenos přístupu při zachování kontinuity hlasového hovoru mezi různými přístupovými sítěmi. Slouží jako kotvicí bod v s"
---

ATCF je síťový prvek 3GPP, který v IMS kotví hovor za účelem řízení plynulého přenosu přístupu mezi různými sítěmi, například mezi okruhově spínanou a paketově spínanou doménou.

## Popis

Access Transfer Control Function (ATCF) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS) dle 3GPP, konkrétně navržená pro usnadnění operací Voice Call Continuity ([VCC](/mobilnisite/slovnik/vcc/)) a Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)). Funkčně je umístěna jako Session Border Controller (SBC) uvnitř jádra IMS, ATCF slouží jako kotvicí bod pro média a signalizaci během aktivních hlasových relací. Když uživatelské zařízení (UE) zahájí nebo přijme hlasový hovor, ATCF se stane pevným bodem v síti IMS, který zpracovává všechny následné přenosy přístupu, a zajišťuje, že vzdálená strana nezaznamená žádné změny v podkladové síti.

Architektonicky se ATCF skládá ze dvou hlavních komponent: samotné Access Transfer Control Function a Access Transfer Gateway ([ATGW](/mobilnisite/slovnik/atgw/)). ATCF zpracovává signalizační rovinu, řídí řízení [SIP](/mobilnisite/slovnik/sip/) relací a koordinuje s dalšími prvky IMS, jako je Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Access Transfer Signaling Function (ATSF). ATGW funguje v rovině médií, kotví přenosovou cestu médií a provádí potřebné funkce pro vzájemné propojení médií. Toto oddělení umožňuje efektivní zpracování operací řídicí i uživatelské roviny během složitých scénářů předávání.

Během provozu ATCF implementuje několik klíčových procedur. Když se UE zaregistruje v síti IMS, S-CSCF identifikuje potřebu funkce SRVCC a vybere vhodnou ATCF. ATCF se poté vloží do signalizační cesty a zřídí ATGW v přenosové cestě médií. Během aktivního hlasového hovoru, pokud UE detekuje zhoršující se pokrytí LTE a potřebuje předat spojení do okruhově spínané sítě 2G/3G, ATCF koordinuje s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) provedení procedury SRVCC. Řídí přenos relace, aktualizuje přenosovou cestu médií vzdálené strany tak, aby směřovala k ATGW, a zajišťuje, že během přechodu nedojde k přerušení médií.

ATCF je propojena s mnoha síťovými prvky prostřednictvím standardizovaných referenčních bodů. Klíčová rozhraní zahrnují rozhraní Mw se S-CSCF pro SIP signalizaci, rozhraní [I2](/mobilnisite/slovnik/i2/) s MSC Server pro koordinaci SRVCC a interní rozhraní mezi komponentami ATCF a ATGW. Interaguje také s Policy and Charging Rules Function (PCRF) pro správu kvality služeb a s Home Subscriber Server (HSS) pro data účastníka. Tato komplexní integrace umožňuje ATCF udržovat kontinuitu relace při zachování bezpečnosti, účtování a vynucování politik napříč různými přístupovými technologiemi.

## K čemu slouží

ATCF byla vytvořena, aby vyřešila kritický problém udržení kontinuity hlasového hovoru během předávání mezi různými technologiemi rádiového přístupu, zejména když operátoři začali nasazovat sítě LTE vedle stávající infrastruktury 2G a 3G. Před standardizací SRVCC a ATCF by se hlasové hovory na LTE (pomocí VoLTE) při pohybu uživatelů mimo oblasti pokrytí LTE jednoduše přerušily, což vedlo ke špatné uživatelské zkušenosti a omezovalo schopnost operátorů migrovat hlasové služby na paketově spínané sítě. ATCF poskytuje potřebnou funkci kotvení pro umožnění plynulých přechodů bez přerušení hovoru.

Historicky byl vývoj ATCF motivován přechodem odvětví na plně IP sítě a potřebou zachovat kvalitu hlasových služeb během této migrace. Raná nasazení LTE postrádala možnosti přepojení do okruhově spínané sítě, což činilo hlasové služby nespolehlivými v oblastech s nerovnoměrným pokrytím LTE. ATCF, zavedená ve verzi 3GPP Release 10 jako součást vylepšeného řešení SRVCC (eSRVCC), to vyřešila poskytnutím stabilního kotvicího bodu v jádru IMS, který dokáže řídit složitou signalizaci a aktualizace přenosových cest médií vyžadované během přenosů přístupu.

ATCF řeší několik omezení předchozích přístupů. Počáteční implementace SRVCC v Release 8 měly delší doby přerušení během předávání, protože vyžadovaly signalizaci až zpět do sítě vzdálené strany. ATCF tuto signalizaci lokalizuje tím, že kotví relaci blíže uživateli, což výrazně snižuje doby přerušení při předávání z potenciálně stovek milisekund na méně než 300 milisekund. Toto zlepšení učinilo SRVCC prakticky použitelným pro udržení kvality hlasu během síťových přechodů, což operátorům umožnilo s důvěrou nasazovat služby VoLTE a zároveň využívat své stávající okruhově spínané sítě pro pokrytí.

## Klíčové vlastnosti

- Kotvicí bod signalizace IMS pro hlasové relace
- Kotvení médií prostřednictvím integrované Access Transfer Gateway
- Koordinace procedur SRVCC a eSRVCC
- Plynulé předávání mezi LTE a okruhově spínanými sítěmi 2G/3G
- Udržování kontinuity relace během přenosů přístupu
- Integrace s MSC Server pro předávání do okruhově spínané domény

## Související pojmy

- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ATGW – Access Transfer Gateway](/mobilnisite/slovnik/atgw/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [ATCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/atcf/)
