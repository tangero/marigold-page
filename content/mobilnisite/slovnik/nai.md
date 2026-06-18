---
slug: "nai"
url: "/mobilnisite/slovnik/nai/"
type: "slovnik"
title: "NAI – Network Access Identifier"
date: 2026-01-01
abbr: "NAI"
fullName: "Network Access Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nai/"
summary: "Network Access Identifier (NAI, identifikátor pro přístup k síti) je standardizovaný formát uživatelské identity používaný při autentizaci přístupu k síti, zvláště v roamingu. Má strukturu 'uživatel@d"
---

NAI je standardizovaný formát uživatelské identity se strukturou 'uživatel@doména' (user@realm), používaný pro jednoznačnou identifikaci a směrování žádostí o autentizaci, zejména v roamingu v mobilních sítích.

## Popis

Network Access Identifier (NAI, identifikátor pro přístup k síti) je klíčový identifikátor definovaný v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 7542 a přijatý 3GPP pro použití v přístupové autentizaci. Jeho primární formát je 'uživatelské_jméno@doména' (username@realm). Část 'uživatelské jméno' (username) jednoznačně identifikuje uživatele v rámci dané 'domény' (realm). 'Doména' (realm) je klíčová součást označující administrativní doménu odpovědnou za autentizaci uživatele, typicky domovského poskytovatele služeb (např. operator.com). Tato struktura je zásadní pro roaming.

Při přístupu k síti, když se uživatel (UE) pokouší připojit k navštívené síti (např. při mezinárodním roamingu), UE předloží svůj NAI v přístupové žádosti. Přístupový bod navštívené sítě (např. [PDN](/mobilnisite/slovnik/pdn/) Gateway v 5G nebo [AAA](/mobilnisite/slovnik/aaa/) proxy) prozkoumá část domény (realm) v NAI. Protože doména není lokální, AAA infrastruktura navštívené sítě přepošle žádost o autentizaci, obsahující NAI, na AAA server v domovské doméně uživatele. Toto směrování často probíhá přes hierarchii proxy AAA serverů.

Domovský AAA server (např. [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/) v 3GPP) použije část uživatelského jména (username) z NAI k vyhledání uživatelského profilu předplatného a autentizačních přihlašovacích údajů. Poté zahájí autentizační protokol (jako EAP-AKA') s UE. NAI zůstává během tohoto procesu konstantní, což zajišťuje, že domovská síť přesně ví, který uživatel je autentizován. V systémech 3GPP je NAI často odvozen z International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) uživatele nebo z trvalého identifikátoru předplatného ([SUPI](/mobilnisite/slovnik/supi/)) způsobem chránícím soukromí (např. vytvořením pseudonymu).

Role NAI sahá za počáteční přístup. Používá se v záznamech o účtování (např. v RADIUS Accounting zprávách) ke korelaci dat o využití s konkrétním uživatelem a jeho domovskou doménou pro účely fakturace a vyúčtování mezi roamingovými partnery. Jedná se o identifikátor na úrovni operátora navržený pro škálovatelnost a globální jedinečnost, který tvoří páteř interoperabilní autentizace v heterogenních a roaming podporujících síťových prostředích.

## K čemu slouží

NAI byl vytvořen k vyřešení základního problému jedinečné a jednoznačné identifikace mobilního uživatele ve světě více vzájemně propojených síťových poskytovatelů služeb (roaming). Před standardizací používaly různé sítě různé, často nekompatibilní formáty pro uživatelská ID (např. jednoduchá uživatelská jména, MSISDN), což způsobovalo vážné problémy při směrování žádostí o autentizaci během roamingu a komplikovalo mezioperátorské účtování.

Primární motivací bylo umožnit bezproblémovou a bezpečnou autentizaci přístupu k síti pro roamingové uživatele. Struktura 'uživatel@doména' (user@realm) poskytuje jednoduchý, ale účinný způsob, jak vložit informace pro směrování (doménu) přímo do identity uživatele. To umožňuje jakékoli navštívené síti určit, kam odeslat žádost o autentizaci, aniž by o uživateli předem věděla. Odděluje autentizační infrastrukturu navštívené sítě od databáze uživatelů domovské sítě.

3GPP přijalo NAI k integraci autentizace své jádrové sítě (pomocí Diameter a později protokolů založených na HTTP/2) s širším rámcem internetové autentizace zavedeným IETF. Řeší omezení pouhého použití IMSI nebo MSISDN, které explicitně neobsahují informace pro směrování domény a mohou při přenosu v čistém textu vyvolávat obavy o soukromí. Formát NAI je rozšiřitelný a podporuje vylepšení ochrany soukromí, jako jsou pseudonymní identity nebo identity pro rychlou reautentizaci, což z něj činí univerzální a budoucím potřebám odolný základní kámen pro bezpečný a škálovatelný mobilní přístup.

## Klíčové vlastnosti

- Standardizovaný formát 'uživatelské_jméno@doména' (username@realm) podle IETF RFC 7542
- Komponenta domény (realm) umožňuje směrování žádostí o autentizaci do domény domovské sítě uživatele
- Základní identifikátor používaný v autentizačních a účtovacích protokolech EAP, RADIUS a Diameter
- Často je vytvořen z nebo namapován na IMSI nebo SUPI uživatele pro předplatitele 3GPP
- Podporuje mechanismy ochrany soukromí prostřednictvím použití pseudonymních identit nebo identit pro reautentizaci
- Globálně jedinečný identifikátor nezbytný pro roamingové scénáře a mezioperátorské zúčtování

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [NAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nai/)
