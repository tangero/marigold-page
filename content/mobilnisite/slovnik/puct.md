---
slug: "puct"
url: "/mobilnisite/slovnik/puct/"
type: "slovnik"
title: "PUCT – Price per Unit Currency Table"
date: 2025-01-01
abbr: "PUCT"
fullName: "Price per Unit Currency Table"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/puct/"
summary: "PUCT je standardizovaná tabulka v rámci 3GPP, která definuje kódy měn a jejich formátování pro účely fakturace. Zajišťuje konzistentní reprezentaci peněžních hodnot mezi různými síťovými prvky a faktu"
---

PUCT je standardizovaná tabulka 3GPP, která definuje kódy měn a jejich formátování za účelem zajištění jednotného zobrazení peněžních částek pro účely účtování, fakturace a finančních vypořádání v mobilních sítích.

## Popis

Price per Unit Currency Table (PUCT) je základní datová struktura pro správu definovaná ve specifikacích 3GPP, zejména v TS 21.905 (Vocabulary for 3GPP Specifications). Nejde o aktivní protokol nebo rozhraní, nýbrž o referenční tabulku, která standardizuje reprezentaci světových měn v kontextu systémů 3GPP. Jejím hlavním úkolem je poskytovat jednoznačné mapování mezi číselným kódem měny, identifikátorem měny (jako '[USD](/mobilnisite/slovnik/usd/)') a přidruženými pravidly formátování, konkrétně počtem vedlejších jednotek (např. centů) na hlavní jednotku.

Tabulka je navržena jako jednoduchý, statický odkaz. Každý záznam v PUCT obsahuje klíčová pole: číselný kód měny (např. 840 pro USD), alfabetický kód měny (např. USD, EUR, JPY), exponent měny (definující počet používaných desetinných míst) a často i název měny. Exponent je klíčový; například USD má exponent 2, což znamená, že na hlavní jednotku (dolar) připadá 100 vedlejších jednotek (centů). Japonský jen (JPY) má exponent 0, protože standardně nepoužívá vedlejší jednotku. Tyto údaje jsou nezbytné pro jakoukoli síťovou funkci, která zpracovává informace o účtování.

PUCT funguje jako kanonický zdroj, na který odkazují všechny další specifikace 3GPP pro účtování a fakturaci. Když síťový uzel (jako GGSN, [PGW](/mobilnisite/slovnik/pgw/) nebo [SMF](/mobilnisite/slovnik/smf/)) vygeneruje záznam o účtování ([CDR](/mobilnisite/slovnik/cdr/)), zahrne do něj pro všechny peněžní pole kód měny. Navazující fakturační systém, zprostředkovací zařízení nebo platforma pro roamingové vypořádání konzultuje PUCT (nebo interní databázi z ní odvozenou), aby tento kód správně interpretoval. Určuje, jak formátovat částku na faktuře a případně jak převádět mezi měnami. Jeho rolí je odstranit nejednoznačnost a zajistit, aby hodnota '100' s kódem měny 840 byla všeobecně chápána jako 1,00 americký dolar, nikoli 100 dolarů nebo 100 centů. Tato konzistence je zásadní pro automatizované zpracování, finanční auditování a interoperabilitu mezi operátory při roamingu.

## K čemu slouží

PUCT existuje k řešení základního problému v telekomunikačním účtování: potřeby standardizované, strojově čitelné reprezentace světových měn. V počátcích mobilních sítí, zejména s nástupem digitálního roamingu v GSM, si operátoři museli vyměňovat záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) za hovory uskutečněné v navštívených sítích. Bez standardizovaného způsobu označení měny mohla být hodnota '100' od jednoho operátora špatně interpretována systémem druhého, což vedlo k závažným fakturačním chybám a složitým finančním sporům.

Vytvoření PUCT bylo motivováno nutností globální interoperability v oblasti účtování. Před jeho standardizací mohli operátoři používat proprietární kódy nebo různé interpretace mezinárodních standardů, jako je [ISO](/mobilnisite/slovnik/iso/) 4217. PUCT definovaný 3GPP poskytl jednotnou, autoritativní tabulku, kterou mohly používat všechny síťové prvky a fakturační systémy vyhovující 3GPP, a tím zajistil konzistenci v celém ekosystému. Řešil tak omezení ad-hoc implementací tím, že přímo zabudoval definici měny do operačního jazyka sítě.

Kromě toho, jak se mobilní služby rozvíjely a zahrnovaly datové služby, účtování obsahu a nakonec služby IMS, rostla i potřeba přesných finančních transakcí. PUCT poskytuje základní datovou integritu pro všechny peněžní hodnoty proudící sítí, od interakcí s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) v reálném čase až po offline fakturaci a vypořádání mezi operátory. Jeho účelem být neměnným referenčním bodem, který zabraňuje finančnímu chaosu v globální síti s více dodavateli a operátory.

## Klíčové vlastnosti

- Definuje číselné a alfabetické kódy pro světové měny.
- Specifikuje exponent (desetinná místa) pro každou měnu.
- Poskytuje standardizovanou referenci pro všechny specifikace 3GPP pro účtování.
- Zajišťuje jednoznačnou interpretaci peněžních hodnot v záznamech CDR.
- Nezbytná pro přesné roamingové účtování a finanční vypořádání.
- Statická tabulka pravidelně aktualizovaná, aby reflektovala nové měny.

## Související pojmy

- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [PUCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/puct/)
