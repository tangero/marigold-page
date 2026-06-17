---
slug: "mrp"
url: "/mobilnisite/slovnik/mrp/"
type: "slovnik"
title: "MRP – Mouth Reference Point"
date: 2025-01-01
abbr: "MRP"
fullName: "Mouth Reference Point"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mrp/"
summary: "Mouth Reference Point (MRP) je standardizovaný referenční bod modelu umělé hlavy používaný v 3GPP pro akustické testování hlasových komunikačních zařízení. Definuje přesný referenční bod pro akustický"
---

MRP je referenční bod standardizovaného modelu umělé hlavy pro akustický výstup simulátoru úst, používaný v 3GPP pro konzistentní akustické testování hlasových komunikačních zařízení.

## Popis

Mouth Reference Point (MRP) je klíčovou součástí standardizovaného akustického testovacího rámce 3GPP, specificky definovanou pro koncová zařízení, jako jsou mobilní telefony a sluchátka. Není fyzickou součástí sítě, ale referenčním modelem používaným v laboratorním prostředí. MRP je součástí simulátoru hlavy a trupu ([HATS](/mobilnisite/slovnik/hats/)), který napodobuje akustické vlastnosti lidského mluvčího. Jeho primární funkcí je poskytnout geometricky a akusticky definovaný bod, ze kterého jsou vysílány testovací řečové signály, simulující pozici a akustické charakteristiky lidských úst. To zajišťuje, že všechna testovaná zařízení přijímají stejný akustický podnět, což umožňuje spravedlivé a srovnatelné hodnocení jejich přenosového výkonu.

Technická implementace MRP je podrobně popsána v několika specifikacích 3GPP, které definují jeho přesnou prostorovou polohu vůči referenčnímu bodu umělé hlavy ([HRP](/mobilnisite/slovnik/hrp/)) a referenčnímu bodu ucha ([ERP](/mobilnisite/slovnik/erp/)). Specifikace, jako jsou TS 26.131 a TS 26.132, stanovují přísné požadavky na akustický zdroj používaný v MRP, včetně jeho frekvenční charakteristiky, směrovosti a hladiny akustického tlaku. Během testování je standardizovaný řečový signál přehráván prostřednictvím reproduktoru nebo simulátoru umístěného v MRP. Testované zařízení, umístěné ve standardizované pozici vůči umělé hlavě, tento signál zachytí. Přijatý zvuk je následně analyzován pro měření klíčových ukazatelů výkonu, jako jsou hodnoty vysílací hlasitosti, frekvenční charakteristiky a přenos šumu na pozadí.

Role MRP přesahuje pouhé generování signálu; je zásadní pro zajištění interoperability a kvality služby (QoS) pro hlasové služby. Poskytnutím řízeného a opakovatelného akustického zdroje umožňuje síťovým operátorům a výrobcům zařízení ověřit, že koncová zařízení splňují přenosové požadavky 3GPP. Tyto požadavky jsou nezbytné pro udržení konzistentní kvality hovoru v síti bez ohledu na model telefonu. MRP se používá ve spojení s dalšími referenčními body, jako je ERP pro testy poslechu, a vytváří tak kompletní koncové akustické testovací uspořádání. Tento holistický přístup ověřuje jak vysílací (mluvčí), tak přijímací (posluchač) cestu hlasového hovoru.

Definice MRP navíc podporuje vývoj hlasových kodeků a pokročilých služeb, jako je Voice over LTE (VoLTE) a Voice over NR (VoNR). Se zaváděním nových kodeků (např. [EVS](/mobilnisite/slovnik/evs/), [AMR-WB](/mobilnisite/slovnik/amr-wb/)) MRP zajišťuje, že akustické testování zůstává konzistentní, což umožňuje hodnocení vylepšených funkcí kvality hlasu. Jeho specifikace jsou pravidelně revidovány a aktualizovány, aby zohlednily nové testovací metodiky a formáty zařízení, jako jsou nositelná zařízení a chytré reproduktory, a zajistily tak, že referenční bod zůstává relevantní pro moderní komunikační scénáře.

## K čemu slouží

Mouth Reference Point byl vytvořen, aby vyřešil základní problém v telekomunikačním testování: nedostatek reprodukovatelnosti a konzistence v akustických měřeních hlasových koncových zařízení. Před jeho standardizací mohli různí výrobci a zkušebny používat odlišná uspořádání pro simulaci lidského mluvčího, což vedlo k nekonzistentním výsledkům testů. To ztěžovalo objektivní srovnání přenosové kvality různých zařízení nebo vynucování standardů kvality sítě. MRP poskytuje jednotný, objektivní referenční bod, který zajišťuje, že všechny strany měří akustický výkon za identických podmínek.

Historicky se potřeba takové standardizace stala naléhavou s rozšířením mobilních telefonů a globalizací telekomunikačního trhu. Síťoví operátoři potřebovali záruky, že jakékoli certifikované zařízení poskytne na jejich síti přijatelný uživatelský zážitek. MRP, zavedený ve 3GPP Release 5, byl součástí širšího úsilí o definování komplexních standardů pro testování koncových zařízení. Vyřešil omezení ad-hoc testování tím, že poskytl vědecky definovaný model akustického výstupu lidského hlasového systému, založený na rozsáhlém výzkumu akustiky řeči a sluchu.

MRP zůstává nezbytný, protože kvalita hlasu zůstává klíčovým ukazatelem výkonu pro mobilní sítě, i přes růst datových služeb. Řeší problém zajištění toho, aby pokroky v designu zařízení (menší mikrofony, potlačení šumu) nezhoršily základní parametry přenosu hlasu. Definováním stabilního referenčního bodu umožňuje vývoj testovacích standardů pro pokrytí nových technologií, jako je širokopásmový zvuk, hands-free provoz a voice over IP, při zachování zpětné kompatibility a konzistentního základu pro hodnocení kvality.

## Klíčové vlastnosti

- Definuje přesný geometrický bod pro akustický zdroj v simulátoru umělé hlavy.
- Specifikuje akustické charakteristiky (např. frekvenční charakteristiku) zdroje v referenčním bodě.
- Zajišťuje reprodukovatelná a srovnatelná akustická měření napříč různými testovacími laboratořemi.
- Podporuje testování klíčových přenosových parametrů, jako je hodnocení vysílací hlasitosti a sidetone.
- Integruje se s referenčním bodem ucha (ERP) pro kompletní koncové testování hlasových koncových zařízení.
- Poskytuje stabilní referenční bod pro testování vyvíjejících se hlasových kodeků a služeb, jako jsou VoLTE a VoNR.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services
- **TS 43.058** (Rel-19) — Handsfree MS Transmission Quality Guidelines

---

📖 **Anglický originál a plná specifikace:** [MRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrp/)
