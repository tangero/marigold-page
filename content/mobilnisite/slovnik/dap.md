---
slug: "dap"
url: "/mobilnisite/slovnik/dap/"
type: "slovnik"
title: "DAP – Data Authentication Pattern"
date: 2026-01-01
abbr: "DAP"
fullName: "Data Authentication Pattern"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dap/"
summary: "Bezpečnostní mechanismus definovaný ve specifikacích 3GPP pro ověřování integrity a původu dat v telekomunikačních sítích. Poskytuje kryptografickou záruku, že data nebyla pozměněna a pocházejí z legi"
---

DAP je bezpečnostní mechanismus 3GPP, který kryptograficky ověřuje integritu a původ dat, aby zajistil, že data nejsou pozměněna a pocházejí z legitimního zdroje pro bezpečnou výměnu v síti.

## Popis

Data Authentication Pattern (DAP, vzor pro autentizaci dat) je standardizovaný bezpečnostní konstrukt v systémech 3GPP, který implementuje autentizaci zpráv. Nejde o samostatný protokol, ale o definovaný vzor či rámec pro aplikaci kryptografické ochrany integrity a autentizace původu dat na protokolové datové jednotky (PDU) vyměňované mezi síťovými entitami. Tento vzor specifikuje, jak generovat a ověřit autentizační značku (často Message Authentication Code – [MAC](/mobilnisite/slovnik/mac/)) pro sadu datových polí, čímž zajišťuje integritu dat a potvrzuje identitu odesílatele. Tím se zabraňuje neoprávněné modifikaci, replay útokům a falšování během přenosu dat.

Architektonicky DAP funguje na vrstvě nad základním transportem, typicky v rámci aplikační nebo signalizační protokolové vrstvy. Jeho implementace zahrnuje odesílatele a příjemce sdílející tajný kryptografický klíč (K), který je navázán předchozími bezpečnostními procedurami, jako je Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Pro vygenerování DAP vybere odesílatel konkrétní datová pole, která mají být chráněna („autentizovaná data“), což mohou být kritické parametry jako identifikátory, časová razítka nebo kódy příkazů. Pomocí sdíleného klíče K a určeného kryptografického algoritmu (historicky byly běžné algoritmy ze sady 3GPP MILENAGE) odesílatel vypočte MAC nad těmito autentizovanými daty. Tento MAC, který je samotným DAP, je následně připojen ke zprávě před odesláním.

Po přijetí přijímající entita extrahuje DAP a přijatá autentizovaná data. Nezávisle přepočte očekávaný MAC pomocí své kopie sdíleného klíče K a stejného algoritmu. Porovnáním vypočteného MAC s přijatým DAP může příjemce s vysokou kryptografickou jistotou ověřit, že data jsou neporušená a pocházejí od entity disponující správným klíčem. Přesný rozsah autentizovaných dat, kryptografický algoritmus a správa klíčů jsou definovány v konkrétní technické specifikaci 3GPP (TS), která implementuje DAP pro dané rozhraní nebo službu, jako jsou specifikace pro Legal Interception ([LI](/mobilnisite/slovnik/li/)) nebo správu dat účastníků.

Role DAP je zásadní pro zabezpečení citlivých operací, zejména v síťovém managementu a regulačních funkcích. Například v systémech Legal Interception specifikovaných v TS 33.108 DAP autentizuje veškerou komunikaci na Handover Interface ([HI](/mobilnisite/slovnik/hi/)) mezi Lawful Enforcement Monitoring Facility ([LEMF](/mobilnisite/slovnik/lemf/)) a Mediation Function ([MF](/mobilnisite/slovnik/mf/)) operátora. Tím se zajišťuje, že příkazy k odposlechu a odposlechnutý obsah jsou pravé a nezměněné, což je kritický zákonný požadavek. Podobně mechanismy DAP zabezpečují komunikaci v Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)) a dalších síťových prvcích zpracovávajících citlivá data účastníků nebo zařízení, jak je uvedeno ve specifikacích jako TS 23.048.

## K čemu slouží

DAP byl vytvořen, aby řešil základní bezpečnostní požadavek na autentizaci původu dat a ochranu integrity v sítích 3GPP. Jak se mobilní sítě vyvíjely a nabízely sofistikovanější služby a zpracovávaly stále citlivější uživatelská data, rostlo riziko, že škodliví aktéři vloží falešné příkazy, pozmění data managementu nebo budou falšovat síťové entity. Předchozí přístupy často spoléhaly na implicitní důvěru v uzavřených síťových doménách nebo na slabší, nestandardizované bezpečnostní mechanismy, které byly nedostatečné pro splnění regulatorních požadavků a robustní ochranu sítě.

Primární problém, který DAP řeší, je poskytnutí standardizované, kryptograficky silné metody, která zajistí, že kritické výměny dat – zejména pro síťový management, legal interception a správu dat účastníků – jsou důvěryhodné. Bez DAP by mohly být padělány příkazy k aktivaci legal interception nebo aktualizaci černých listin zařízení, což by vedlo k porušování soukromí, narušení služeb nebo nedodržení zákonů. Jeho vytvoření bylo motivováno potřebou konzistentního bezpečnostního vzoru, který by mohl být vyžadován napříč různými rozhraními 3GPP, a zajištění interoperability mezi zařízeními různých výrobců při současném splnění přísných bezpečnostních a legislativních požadavků síťových operátorů a regulátorů.

Historicky jeho zavedení v Release 5 časově souviselo s dozráním bezpečnostní architektury 3G a formalizací systémů jako Legal Interception. DAP poskytl potřebný technický mechanismus pro splnění požadavku na „autentizaci“ komunikace na Handover Interface, jak požadují donucovací orgány po celém světě. Vyřešil tak omezení spočívající v absenci standardizovaného, na algoritmu nezávislého rámce pro takovou autentizaci a umožnil integraci silných kryptografických algoritmů, jako jsou ty ze sady MILENAGE definované pro 3G/UMTS [AKA](/mobilnisite/slovnik/aka/).

## Klíčové vlastnosti

- Poskytuje kryptografickou autentizaci původu dat
- Zajišťuje ochranu integrity pro vybraná pole zprávy
- Používá sdílené tajné klíče navázané přes síťové bezpečnostní procedury
- Využívá se v kritických regulačních funkcích, jako je Legal Interception
- Definuje znovupoužitelný vzor aplikovatelný napříč různými rozhraními 3GPP
- Rámec nezávislý na algoritmu podporující specifikované kryptografické funkce

## Definující specifikace

- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [DAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dap/)
