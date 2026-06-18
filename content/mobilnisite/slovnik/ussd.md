---
slug: "ussd"
url: "/mobilnisite/slovnik/ussd/"
type: "slovnik"
title: "USSD – Unstructured Supplementary Services Data"
date: 2025-01-01
abbr: "USSD"
fullName: "Unstructured Supplementary Services Data"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ussd/"
summary: "Zastaralý mechanismus GSM/UMTS pro textovou komunikaci v reálném čase mezi mobilním telefonem a aplikací v síti. Umožňuje interaktivní služby řízené nabídkou, jako jsou kontroly zůstatku, doplňování k"
---

USSD je zastaralý mechanismus GSM/UMTS pro komunikaci v reálném čase založenou na textu, probíhající signalizačními kanály mezi mobilním telefonem a síťovou aplikací, který umožňuje interaktivní služby bez datového připojení.

## Popis

Unstructured Supplementary Services Data (USSD) je relací řízený komunikační protokol fungující v reálném čase, používaný v sítích GSM, UMTS a příbuzných mobilních sítích. Na rozdíl od [SMS](/mobilnisite/slovnik/sms/), která funguje na principu ulož a předej (store-and-forward), USSD navazuje přechodný interaktivní dialog mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) uživatele a aplikací v síti, typicky USSD Gateway nebo služebním uzlem. Uživatel relaci zahájí vytočením USSD řetězce, který začíná hvězdičkou (*) a končí křížkem (#), například *123#. Tento řetězec je přenášen z MS na ústřednu mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) přes signalizační kanály (např. protokol [DTAP](/mobilnisite/slovnik/dtap/) na rádiovém rozhraní). MSC/SGSN směruje USSD zprávu na příslušný USSD handler na základě vytočeného kódu.

Klíčovým síťovým prvkem pro USSD je USSD Gateway nebo USSD Service Center. Funguje jako interpret a směrovač pro USSD zprávy. Po přijetí USSD řetězce může brána zprávu zpracovat lokálně pomocí vlastní služební logiky nebo ji přeposlat externímu aplikačnímu serveru (např. systému předplacených služeb, platformě péče o zákazníky) přes protokoly jako [MAP](/mobilnisite/slovnik/map/) nebo [SMPP](/mobilnisite/slovnik/smpp/). Aplikace vygeneruje textovou odpověď, která je odeslána zpět přes bránu a MSC na uživatelův telefon, kde se zobrazí na obrazovce. USSD relace zůstává otevřená, dokud ji uživatel explicitně neukončí (např. odesláním dalšího #) nebo nedojde k síťovému timeoutu, což umožňuje výměnu více zpráv v rámci jedné relace pro podporu navigace v nabídkách.

USSD funguje nezávisle na přepojování okruhů (circuit-switched) nebo paketů (packet-switched); používá signalizační cestu nespojenou s hovorem. To znamená, že funguje i když je uživatel ve hovoru nebo v oblasti bez pokrytí daty GPRS/EDGE/3G, což zajišťuje téměř univerzální dostupnost. Zprávy jsou přenášeny v rámci operací protokolu MAP (Mobile Application Part), konkrétně MAP PROCESS-UNSTRUCTURED-SS-REQUEST a MAP UNSTRUCTURED-SS-REQUEST. Z architektonického hlediska využívá stávající infrastrukturu SS7 nebo SIGTRAN pro přenos mezi MSC a USSD Gateway. Jeho úlohou je poskytovat odlehčené rozhraní s nízkou latencí pro jednoduché, ale klíčové služby pro účastníky, zejména na trzích, kde nejsou chytré telefony a mobilní data všudypřítomné.

## K čemu slouží

USSD bylo vytvořeno, aby poskytlo jednoduchou, efektivní a interaktivní metodu, jak mohou mobilní účastníci přistupovat k síťovým službám přímo z volací klávesnice svého telefonu, aniž by potřebovali datový tarif nebo instalaci konkrétní aplikace. V počátcích sítí GSM operátoři potřebovali způsob, jak umožnit zákazníkům spravovat své služby (např. kontrolovat zůstatek u předplacených služeb, aktivovat přesměrování hovorů) bez nutnosti volat na zákaznickou linku nebo používat složité telefonní menu. USSD tento problém vyřešilo poskytnutím standardizovaného textového rozhraní typu stroj-stroj, které může být spuštěno uživatelem a zpracováno v reálném čase síťovými aplikacemi.

Řešilo významná omezení alternativních metod. Systémy interaktivní hlasové odpovědi (IVR) vyžadovaly hovor, který byl zpoplatněn a obsazoval hovorový kanál. Služby založené na SMS trpěly latencí kvůli principu ulož a předej a vyžadovaly, aby si uživatel pamatoval specifickou syntaxi. USSD naproti tomu využívá signalizační kanály, je relací řízené pro rychlou interakci a používá jednoduchou, zapamatovatelnou strukturu kódu (*XXX#). To jej učinilo ideálním pro systémy předplacených služeb, kde je reálná kontrola zůstatku a doplnění kreditu kritická, a pro přidané služby jako mobilní bankovnictví (m-banking) v rozvojových regionech.

Historický kontext je ukotven ve specifikacích GSM Phase 2+, kde byly rozšiřovány doplňkové služby. USSD poskytlo 'nestrukturovanou' (unstructured) protiváhu vysoce strukturovaným doplňkovým službám, jako je přesměrování hovorů. Jeho flexibilita umožnila operátorům a třetím stranám rychle nasazovat nové textové služby. Jeho trvajícím účelem, zejména na rozvíjejících se trzích, je překlenout digitální propast tím, že doručuje základní finanční a informační služby na základní a feature telefony, a zajišťuje tak dostupnost služeb pro celou základnu účastníků bez ohledu na schopnosti jejich telefonu.

## Klíčové vlastnosti

- Textový dialog v reálném čase, řízený relací (nikoli principem ulož a předej)
- Funguje přes signalizační kanály, nezávisle na hlasových nebo datových přenosech
- Zahájeno uživatelem vytočením kódu (*XXX#) z klávesnice telefonu
- Podporuje interaktivní navigaci v nabídkách v rámci jedné relace
- Pro přenos mezi MSC a USSD Gateway využívá protokol MAP
- Široce používáno pro předplacené služby, kontroly zůstatku a mobilní bankovnictví

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.090** (Rel-19) — USSD Stage 2 Specification
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.294** (Rel-19) — IMS Centralized Services (ICS) I1 Interface Protocol
- **TS 24.390** (Rel-19) — USSD over IMS Procedures
- **TS 24.391** (Rel-19) — USSD over IMS Management Object Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [USSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ussd/)
