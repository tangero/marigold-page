---
slug: "lrn"
url: "/mobilnisite/slovnik/lrn/"
type: "slovnik"
title: "LRN – Location Routing Number"
date: 2025-01-01
abbr: "LRN"
fullName: "Location Routing Number"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lrn/"
summary: "Jedinečné číslo používané v severoamerické telekomunikační síti pro směrování hovorů na konkrétní geografickou lokalitu nebo přenesené číslo. Umožňuje přenositelnost čísel oddělením volaného čísla od"
---

LRN je jedinečné severoamerické směrovací číslo, které umožňuje přenositelnost čísel tím, že zajišťuje, aby hovory na přenesené číslo dorazily do sítě správného poskytovatele služeb.

## Popis

Location Routing Number (LRN, číslo pro směrování podle umístění) je klíčový identifikátor v rámci ekosystému Severoamerického číslovacího plánu ([NANP](/mobilnisite/slovnik/nanp/)), standardizovaný 3GPP pro podporu místní přenositelnosti čísel (LNP). Jedná se o desetimístné číslo, strukturálně shodné se standardním telefonním číslem, které jednoznačně identifikuje konkrétní ústřednu nebo síťový bod vzájemného propojení (POI) v síti operátora. Když účastník přenese své telefonní číslo od jednoho poskytovatele služeb k druhému, volané telefonní číslo ([DN](/mobilnisite/slovnik/dn/)) zůstává pro volajícího stejné, ale základní směrování se musí změnit, aby byl hovor směrován do sítě nového operátora. LRN slouží jako tato nová směrovací adresa.

Z architektonického hlediska je funkce LRN integrována do jádra sítě, primárně v rámci signalizačních systémů jako je Signalizační systém č. 7 (SS7) a jeho nástupci založené na IP (např. SIGTRAN). Když je uskutečněn hovor na přenesené číslo, ústředna volajícího operátora provede dotaz na centralizovanou databázi přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)), obvykle prostřednictvím služby dotazu na přenositelnost čísel (NPQ). Tento dotaz používá volané DN jako klíč. NPDB vrátí odpovídající LRN pro dané DN, který identifikuje ústřednu příjemce-operátora, která nyní hostuje účastníka. Ústředna volajícího poté použije toto LRN, namísto volaného DN, jako směrovací adresu v rámci zprávy [IAM](/mobilnisite/slovnik/iam/) (Initial Address Message) pro zřízení hovoru přes telefonní veřejnou komutovanou síť (PSTN) nebo IP propojení.

Jeho role přesahuje pouhé směrování hovorů. LRN je zásadní pro účtování a vyúčtování mezi operátory, protože přesně identifikuje síť, která hovor ukončuje. Ve specifikacích 3GPP, konkrétně v řadě 32 o účtování a řízení, je LRN klíčovým parametrem pro záznamy o účetnictví (např. záznamy o podrobnostech hovoru nebo záznamy o účtovacích datech). Zajišťuje, aby byl příjem správně přidělen, když hovory procházejí více sítěmi. Mechanismus LRN dále podporuje různé typy přenositelnosti, včetně přenosu z pevné sítě do mobilní, z mobilní do pevné a přenosů uvnitř jednoho operátora, čímž poskytuje flexibilní a škálovatelné řešení pro konkurenční telekomunikační trh.

## K čemu slouží

LRN bylo vytvořeno, aby vyřešilo základní výzvu zavedenou místní přenositelností čísel (LNP): umožnit účastníkům zachovat si svá telefonní čísla při změně poskytovatele služeb, aniž by došlo k narušení infrastruktury směrování hovorů v PSTN. Před LNP byla telefonní čísla neoddělitelně spjata s konkrétní ústřednou operátora a geografickou tarifní oblastí. Samotné číslo obsahovalo prefix NPA-NXX, který identifikoval obsluhující ústřednu, což činilo směrování přímočarým. Tento rigidní systém se však stal překážkou konkurence, protože zákazníci se nechtěli vzdát svého zavedeného telefonního čísla.

LNP, nařízená regulačními orgány, toto přímé propojení zrušila a vytvořila problém: jak směrovat hovor na číslo, které již nepatří k původně přiřazené ústředně? LRN poskytuje řešení zavedením nepřímé směrovací vrstvy. Odděluje volatelný identifikátor účastníka (telefonní číslo, [DN](/mobilnisite/slovnik/dn/)) od síťové směrovací adresy. To umožňuje, aby volané číslo zůstalo pro koncové uživatele konstantní, zatímco síť používá samostatný, operátorem přiřazený identifikátor (LRN) k fyzickému směrování hovoru na správnou cílovou ústřednu. Tato inovace zachovala jednoduchost uživatelského volání a efektivitu stávající hierarchie směrování SS7, a zároveň umožnila plnou mobilitu čísel.

Zavedení LRN bylo motivováno potřebou standardizované, interoperabilní a efektivní metody pro implementaci LNP napříč všemi severoamerickými operátory. Řešilo omezení alternativních, složitějších směrovacích schémat, která by vyžadovala masivní změny v překladech ústředen nebo zaváděla významnou latenci. Díky využití stávajících mechanismů databázových dotazů umožnilo řešení LRN relativně elegantní integraci přenositelnosti do starších sítí a vytvořilo páteř pro konkurenční telekomunikační prostředí.

## Klíčové vlastnosti

- Desetimístný číselný identifikátor odpovídající formátu NANP
- Jednoznačně identifikuje konkrétní přepínací entitu nebo bod vzájemného propojení
- Umožňuje směrování hovorů pro přenesená telefonní čísla nezávisle na volaném DN
- Získává se pomocí dotazů na centralizovanou databázi přenositelnosti čísel (NPDB)
- Používá se jako směrovací adresa ve zprávách IAM (Initial Address Message) SS7/SIGTRAN
- Klíčový parametr pro záznamy o účtování a vyúčtování mezi operátory

## Definující specifikace

- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [LRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/lrn/)
