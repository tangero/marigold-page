---
slug: "ixit"
url: "/mobilnisite/slovnik/ixit/"
type: "slovnik"
title: "IXIT – Implementation eXtra Information for Testing"
date: 2025-01-01
abbr: "IXIT"
fullName: "Implementation eXtra Information for Testing"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/ixit/"
summary: "IXIT je formální dokument specifikující doplňkové informace potřebné k provedení standardizovaných testovacích případů na konkrétní implementaci. Podrobně popisuje parametry, konfigurace a schopnosti"
---

IXIT je formální dokument specifikující doplňkové parametry a konfigurace závislé na konkrétní implementaci, které jsou nezbytné pro přesné provedení standardizovaných testovacích případů, protože tyto podrobnosti nejsou plně definovány v základních testovacích specifikacích.

## Popis

Implementation eXtra Information for Testing (IXIT) je klíčovou součástí testovacího a certifikačního rámce 3GPP. Nejde o protokol ani síťovou funkci, ale o strukturovaný dokument nebo datový soubor, který doprovází konkrétní implementaci standardu 3GPP (např. UE nebo síťový prvek) během formálních testovacích postupů, jako jsou ty prováděné certifikačními orgány, například Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) nebo [PCS](/mobilnisite/slovnik/pcs/) Type Certification Review Board (PTCRB). Hlavním účelem IXIT je překlenout mezeru mezi obecnými požadavky standardizovaného testovacího případu a konkrétními, reálnými charakteristikami testovaného zařízení nebo systému ([SUT](/mobilnisite/slovnik/sut/)). Standardní testovací specifikace (TS) definují testovací postupy, podněty a očekávané odezvy obecným způsobem. Skutečný produkt však může mít funkce závislé na implementaci, volitelné schopnosti nebo konfigurovatelné parametry, které ovlivňují způsob aplikace a interpretace testu. IXIT poskytuje tento chybějící kontext.

Z architektonického hlediska IXIT vystupuje jako vstup pro testovací systém. Prováděč testu (často automatizované testovací zařízení) čte parametry z IXIT, aby správně nakonfiguroval testovací prostředí a upravil testovací sekvenci pro SUT. Například testovací případ pro agregaci nosných může být definován obecně, ale konkrétní pásma a kombinace šířek pásma podporované UE musí být deklarovány v jejím IXIT, aby tester věděl, které přesné konfigurace použít. IXIT je typicky strukturován podle šablon uvedených v příslušných testovacích specifikacích (např. TS 38.523 pro 5G NR). Obsahuje řadu parametrů, z nichž každý má jedinečný identifikátor, popis a hodnotu nebo rozsah hodnot specifický pro danou implementaci. Tyto parametry mohou pokrývat širokou škálu aspektů včetně podporovaných frekvenčních pásem, technologií rádiového přístupu, funkcí protokolů, bezpečnostních algoritmů, QoS schopností a dokonce i podrobností, jako jsou podporované velikosti [PDCP](/mobilnisite/slovnik/pdcp/) [SN](/mobilnisite/slovnik/sn/) nebo režimy [RLC](/mobilnisite/slovnik/rlc/).

Role IXIT v síťovém ekosystému je zásadní pro zajištění kvality a interoperability. Bez něj by bylo testování shody nejednoznačné. Testovací laboratoře by musely činit předpoklady o schopnostech SUT, což by vedlo k nekonzistentnímu provádění testů a potenciálně k falešně pozitivním nebo negativním výsledkům. Vyžadováním přesného IXIT zajišťuje 3GPP, že testování je reprodukovatelné a že výsledek 'prošel' skutečně indikuje, že implementace splňuje standard pro svůj deklarovaný soubor funkcí. Tento proces je nedílnou součástí procesu certifikace terminálů, což je předpoklad pro komerční nasazení. IXIT je tedy klíčovým prostředkem pro přístup na trh, který poskytuje regulatorním orgánům a operátorům jistotu, že zařízení budou v reálných sítích fungovat podle očekávání.

## K čemu slouží

IXIT byl vytvořen, aby vyřešil základní problém standardizovaného testování v telekomunikacích: variabilitu. Jak se standardy 3GPP vyvíjely, zahrnovaly stále více volitelných funkcí a konfigurovatelných parametrů, aby vyhověly různým požadavkům trhu a implementačním volbám. Jedna testovací specifikace nemohla definovat univerzální testovací postup pro každou možnou variantu produktu. Před zavedením formálních procesů IXIT bylo testování často ad-hoc a spoléhalo se na neformální dohody mezi testovacími laboratořemi a výrobci, což vedlo k nekonzistentnostem, delším certifikačním časům a potenciálním problémům s interoperabilitou v praxi.

Primární motivací bylo zavést důkladnost a objektivitu do procesu testování shody. Vyžadováním, aby výrobci formálně deklarovali přesné schopnosti své implementace, získává testovací ekosystém přesnou 'mapu' zařízení. To umožňuje provádět testovací případy kontrolovaným, reprodukovatelným způsobem, který je přizpůsoben skutečnému souboru funkcí zařízení. Řeší to problém testování volitelných funkcí – pokud funkce není v IXIT deklarována, příslušné testy se jednoduše neprovedou a zařízení je certifikováno na základě svého deklarovaného profilu. Tento přístup je mnohem efektivnější než snaha vytvářet a testovat všechny možné kombinace funkcí. Navíc poskytuje jasnou auditní stopu pro certifikaci, protože samotný dokument IXIT se stává součástí certifikačního záznamu a podrobně uvádí, co přesně bylo testováno.

## Klíčové vlastnosti

- Poskytuje implementačně specifické konfigurační parametry pro provedení testu
- Umožňuje přizpůsobení obecných testovacích případů konkrétním schopnostem testovaného systému (SUT)
- Zajišťuje reprodukovatelnost a konzistenci testování shody v různých laboratořích
- Formálně dokumentuje volitelné funkce a implementační volby produktu
- Slouží jako povinný vstup pro certifikační procesy, jako jsou GCF a PTCRB
- Je strukturován podle šablon v testovacích specifikacích 3GPP (např. TS 38.523)

## Definující specifikace

- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TS 34.229** (Rel-19) — IMS SIP/SDP UE Conformance Testing for 5GS
- **TS 36.523** (Rel-19) — UE Conformance Test Spec for Idle Mode
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [IXIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ixit/)
