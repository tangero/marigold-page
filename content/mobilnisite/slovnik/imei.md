---
slug: "imei"
url: "/mobilnisite/slovnik/imei/"
type: "slovnik"
title: "IMEI – International Mobile Station Equipment Identities"
date: 2025-01-01
abbr: "IMEI"
fullName: "International Mobile Station Equipment Identities"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/imei/"
summary: "Globálně unikátní 15místné číslo, které trvale identifikuje mobilní zařízení (telefon, tablet, modem). Používají jej sítě pro identifikaci zařízení, jeho ověření a bezpečnostní funkce, jako je bloková"
---

IMEI je globálně unikátní 15místné číslo, které trvale identifikuje mobilní zařízení a používá se sítěmi pro identifikaci, ověřování a bezpečnostní funkce, jako je například zařazování na černou listinu.

## Popis

International Mobile Equipment Identity (IMEI) je klíčový identifikátor v mobilních telekomunikacích, který slouží jako trvalé, výrobcem přiřazené sériové číslo mobilní stanice ([MS](/mobilnisite/slovnik/ms/)). Jedná se o 15místné dekadické číslo strukturované do několika částí. Prvních osm číslic tvoří Type Allocation Code (TAC), který identifikuje model zařízení a jeho výrobce. Následujících šest číslic je unikátní sériové číslo (SNR) přiřazené výrobcem. Poslední číslice je kontrolní číslice ([CD](/mobilnisite/slovnik/cd/)) vypočtená pomocí Luhnova algoritmu, která slouží k ověření správnosti předchozích 14 číslic. IMEI je naprogramováno do firmware nebo hardwaru zařízení během výroby a není určeno ke změně uživatelem.

Z pohledu provozu sítě zařízení IMEI hlásí síti během počátečních procedur registrace a připojení. Síť může IMEI vyžádat pomocí specifických signalizačních zpráv, například Identity Request v [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) procedurách. Obsluhující síťová entita, typicky [MME](/mobilnisite/slovnik/mme/) v LTE nebo [AMF](/mobilnisite/slovnik/amf/) v 5G, pak může toto IMEI předat do Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)) nebo podobné síťové funkce. EIR obsahuje seznamy (bílý, šedý, černý), vůči kterým je nahlášené IMEI kontrolováno. Tento proces umožňuje operátorovi síťovou službu povolit, monitorovat nebo odepřít na základě stavu zařízení, například zablokovat službu zařízením nahlášeným jako odcizená.

Role IMEI přesahuje pouhou identifikaci. Je základním kamenem pro zákonné odposlechy, prevenci podvodů a analýzu zařízení. Pro zákonné odposlechy mohou orgány použít IMEI k jednoznačné identifikaci cílového zařízení pro sledování. V prevenci podvodů operátoři používají černé listiny IMEI k znepřístupnění odcizených telefonů v jejich sítích, což významně snižuje prodejní hodnotu odcizeného majetku a odrazuje od krádeží. Dále agregovaná data IMEI pomáhají výrobcům a operátorům analyzovat populaci zařízení, penetraci modelů a plánovat podporu síťových technologií (např. odhad počtu zařízení s podporou 5G v síti). Jeho standardizovaný formát zajišťuje globální interoperabilitu, což umožňuje, aby byla identita zařízení konzistentně rozpoznávána a zpracovávána různými operátory a v různých zemích.

## K čemu slouží

IMEI bylo vytvořeno k řešení základního problému jednoznačné a trvalé identifikace samotného fyzického mobilního zařízení, nezávisle na uživatelském předplatném (které je identifikováno [IMSI](/mobilnisite/slovnik/imsi/) na SIM/USIM). Před jeho standardizací neexistovala spolehlivá globální metoda, jak sítě identifikovaly typy zařízení nebo sledovaly jednotlivé hardwarové jednotky. Toto omezení ztěžovalo boj proti krádežím mobilních telefonů, protože odcizený telefon mohl být jednoduše používán s jinou SIM kartou. Také bránilo přesné analýze zařízení a téměř znemožňovalo zavádění politik nebo omezení specifických pro dané zařízení.

Zavedení IMEI ve 3GPP Release 99 poskytlo standardizovaný, proti manipulaci odolný identifikátor, který je pevně zakódován v zařízení. To umožnilo vytvoření centralizovaných Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)), kde si operátoři mohli sdílet seznamy odcizených zařízení. Klíčovou motivací byla ochrana zákazníků a operátorů snížením motivace ke krádežím telefonů, čímž se zvýšila celková bezpečnost sítě. Dále umožnilo splnění regulatorních požadavků pro schvalování typu zařízení a poskytlo mechanismus síťovým operátorům pro správu přístupu zařízení, například zákazem zařízení, která nejsou pro jejich síť typově schválena nebo která představují bezpečnostní riziko.

## Klíčové vlastnosti

- Globálně unikátní 15místný dekadický identifikátor
- Trvale přiřazen během výroby zařízení
- Skládá se z Type Allocation Code (TAC), Serial Number (SNR) a Check Digit (CD)
- Používá se k ověření zařízení vůči černým listinám v Equipment Identity Register (EIR)
- Základní prvek pro prevenci podvodů a blokování odcizených zařízení
- Podporuje analýzu zařízení a plánování sítě

## Související pojmy

- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [IMEI-SV – International Mobile Equipment Identity Software Version](/mobilnisite/slovnik/imei-sv/)
- [IMEI-TAC – Type Allocation Code part of an IMEI](/mobilnisite/slovnik/imei-tac/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.172** (Rel-19) — EPC LCS Protocol (ELP) specification
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [IMEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/imei/)
