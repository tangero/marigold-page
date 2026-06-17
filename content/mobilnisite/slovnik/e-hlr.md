---
slug: "e-hlr"
url: "/mobilnisite/slovnik/e-hlr/"
type: "slovnik"
title: "E-HLR – Enhanced Home Location Register"
date: 2025-01-01
abbr: "E-HLR"
fullName: "Enhanced Home Location Register"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-hlr/"
summary: "Vylepšená verze HLR, což je centrální databáze v mobilních sítích 2G/3G. Ukládá a spravuje trvalá data účastníka včetně identity, profilů služeb, autentizačních informací a aktuální polohy. Je klíčová"
---

E-HLR je vylepšená verze centrální databáze HLR v sítích 2G/3G, která ukládá trvalá data účastníka pro autentizaci, směrování hovorů a poskytování služeb.

## Popis

Enhanced Home Location Register (E-HLR) je kritický síťový prvek a databáze v doménách jádrové sítě s přepojováním okruhů a paketů systémů 2G (GSM) a 3G (UMTS) podle definice 3GPP. Slouží jako primární, trvalé úložiště informací o účastnících. Z architektonického hlediska jde o samostatný síťový uzel, který komunikuje s různými dalšími entitami jádrové sítě prostřednictvím standardizovaných signalizačních protokolů, především Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) přes SS7 nebo SIGTRAN. E-HLR ukládá komplexní soubor dat účastníka, známý jako profil účastníka. To zahrnuje International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), což je jedinečný trvalý identifikátor, Mobile Station [ISDN](/mobilnisite/slovnik/isdn/) Number ([MSISDN](/mobilnisite/slovnik/msisdn/)) neboli telefonní číslo, informace o předplacených službách (např. nastavení přesměrování hovorů, zákazové služby, oprávnění k roamingu) a autentizační data, jako je Authentication Key (Ki), používaná k generování bezpečnostních trojic (RAND, SRES, Kc) nebo kvintetů pro UMTS. Když se User Equipment (UE) připojí k síti, Visitor Location Register (VLR) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) dotazuje E-HLR, aby autentizoval účastníka a získal jeho profil služeb. E-HLR také udržuje dynamické informace o aktuální poloze účastníka, konkrétně adresu VLR nebo SGSN, který UE aktuálně obsluhuje. To je klíčové pro směrování hovorů a relací; když dorazí hovor směrovaný na mobil, Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) se dotáže E-HLR, aby získal adresu aktuálního obslužného uzlu a hovor správně směroval. Aspekt 'Enhanced' (vylepšený) typicky odkazuje na vylepšení v kapacitě, spolehlivosti, schématu databáze a rozhraních pro podporu širšího spektra služeb a integraci s vyvíjejícími se síťovými architekturami, jako je IP Multimedia Subsystem (IMS), kde může komunikovat s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)).

## K čemu slouží

E-HLR byl vyvinut, aby řešil rostoucí rozsah a složitost mobilních sítí přesahující možnosti původního HLR definovaného v raných standardech GSM. Jak se sítě globálně rozšiřovaly, báze účastníků narostla na desítky milionů a nabídka služeb (SMS, GPRS, předplacené služby, CAMEL) se rozšířila, bylo třeba HLR významně vylepšit. E-HLR byl navržen k řešení problémů souvisejících se škálovatelností, výkonem při vysoké zátěži dotazů a správou komplexních profilů účastníků s více službami. Poskytl robustnější a funkčně bohatší platformu pro podporu přechodu od čistě okruhově přepínaných hlasových služeb k integrovaným hlasovým a paketovým datovým službám v sítích 2.5G a 3G. Jeho vznik byl motivován potřebou centralizované, vysoce dostupné databáze účastníků, která by mohla podporovat pokročilou servisní logiku, bezproblémový roaming a přísné požadavky na spolehlivost veřejných telekomunikačních sítí. Řešil omezení dřívějších HLR z hlediska rychlosti transakcí, redundance databáze a flexibility při přidávání nových parametrů služeb, čímž vytvořil spolehlivou páteř pro správu účastníků a mobilitu v sítích před 4G.

## Klíčové vlastnosti

- Centralizované úložiště trvalé identity účastníka (IMSI) a profilů služeb
- Autentizační funkce, generující bezpečnostní vektory (trojice/kvintety) pro ověření UE
- Udržuje dynamické informace o poloze (aktuální adresa VLR/SGSN) pro každého účastníka
- Podporuje širokou škálu doplňkových služeb (přesměrování hovorů, zákazy atd.)
- Konfigurace vysoké dostupnosti a redundance pro spolehlivost sítě
- Komunikuje s MSC, VLR, SGSN, GMSC a SMS centry prostřednictvím signalizace MAP

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [E-HLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-hlr/)
