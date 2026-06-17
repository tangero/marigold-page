---
slug: "crr"
url: "/mobilnisite/slovnik/crr/"
type: "slovnik"
title: "CRR – Conformance Requirements Reference"
date: 2025-01-01
abbr: "CRR"
fullName: "Conformance Requirements Reference"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/crr/"
summary: "CRR je standardizovaný referenční rámec v 3GPP, který definuje požadavky shody pro testování uživatelských zařízení (UE). Poskytuje normativní specifikace, vůči nimž jsou implementace UE ověřovány, ab"
---

CRR je standardizovaný referenční rámec 3GPP, který definuje normativní požadavky shody pro testování uživatelských zařízení (UE) za účelem zajištění interoperability a souladu se standardy.

## Popis

Conformance Requirements Reference (CRR) je komplexní testovací rámec specifikovaný v technických specifikacích 3GPP 31.213 a 51.013. Stanovuje kompletní soubor normativních požadavků, které musí uživatelské zařízení splňovat, aby bylo považováno za shodné se standardy 3GPP. Rámec CRR pokrývá více vrstev protokolového zásobníku, včetně procedur fyzické vrstvy, správy rádiových prostředků, správy mobility a signalizačních protokolů vyšších vrstev.

Architektura testování CRR zahrnuje standardizované testovací případy, které simulují reálné síťové podmínky a procedury. Tyto testovací případy jsou navrženy tak, aby ověřily, že implementace UE správně zpracovávají různé scénáře definované ve specifikacích 3GPP, včetně navázání hovoru, procedur předávání, řízení výkonu, hlášení měření a přechodů stavů protokolu. Testovací rámec zahrnuje jak povinné, tak volitelné testovací požadavky, se specifickými kritérii úspěchu/neúspěchu pro každý testovací případ.

Klíčové součásti rámce CRR zahrnují účely testů, konfigurace testů, procedury testů a specifikace očekávaného chování UE. Účely testů definují, jaký konkrétní aspekt funkčnosti UE je ověřován, zatímco konfigurace testů specifikují síťové parametry a podmínky, za kterých je test prováděn. Procedury testů poskytují podrobné pokyny pro provedení testu, včetně signalizačních sekvencí a časových požadavků. Očekávané chování UE zahrnuje scénáře normálního provozu i případy zpracování chyb.

CRR hraje klíčovou roli v procesu certifikace UE, slouží jako závazná reference pro testovací laboratoře a certifikační orgány. Zajišťuje, že všechny implementace UE procházejí konzistentním testováním vůči stejným požadavkům, bez ohledu na testovací zařízení nebo geografickou polohu. Tato standardizace je nezbytná pro udržení globální interoperability a prevenci síťových problémů způsobených nevyhovujícími zařízeními. Rámec se také vyvíjí s každou verzí 3GPP, aby zahrnoval nové funkce a technologie, a zajistil tak, že testování zůstává relevantní a komplexní.

## K čemu slouží

Conformance Requirements Reference byl vytvořen, aby řešil kritickou potřebu standardizovaného testování UE v odvětví mobilní telekomunikace. Před jeho zavedením různí výrobci a testovací laboratoře často používali odlišné interpretace specifikací 3GPP, což vedlo k nekonzistentním výsledkům testů a potenciálním problémům s interoperabilitou. Tento nedostatek standardizace mohl mít za následek zařízení, která správně fungovala v některých sítích, ale v jiných selhávala, což způsobovalo výpadky služeb a špatný uživatelský zážitek.

CRR tyto problémy řeší tím, že poskytuje jedinou, autoritativní referenci pro všechny požadavky testování shody. Zajišťuje, že každá implementace UE je testována vůči stejné sadě požadavků pomocí standardizovaných metodologií. Tento přístup eliminuje nejednoznačnost v interpretaci specifikací a poskytuje jasná kritéria úspěchu/neúspěchu pro každý testovací případ. Rámec také usnadňuje certifikační proces tím, že poskytuje společný jazyk a strukturu, na které se mohou všichni zúčastnění odvolávat.

Historicky byl vývoj CRR motivován rostoucí složitostí mobilních sítí a rostoucím počtem výrobců UE vstupujících na trh. Jak se specifikace 3GPP vyvíjely, aby zahrnovaly pokročilejší funkce a schopnosti, potřeba komplexního a standardizovaného testování byla stále zjevnější. CRR poskytuje základ pro certifikační procesy Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB, což umožňuje výrobcům prokázat soulad se standardy 3GPP a získat přístup na trhy po celém světě.

## Klíčové vlastnosti

- Standardizované definice testovacích případů pro všechny požadavky 3GPP na UE
- Komplexní pokrytí protokolových vrstev od fyzické vrstvy po aplikační vrstvu
- Jasná kritéria úspěchu/neúspěchu pro každý testovací scénář
- Podpora povinných i volitelných testovacích požadavků
- Integrace s certifikačními procesy (GCF, PTCRB)
- Pravidelné aktualizace sladěné s cykly vydání 3GPP

## Definující specifikace

- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [CRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/crr/)
