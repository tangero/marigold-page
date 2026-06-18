---
slug: "ffn"
url: "/mobilnisite/slovnik/ffn/"
type: "slovnik"
title: "FFN – Follow Me function node"
date: 2025-01-01
abbr: "FFN"
fullName: "Follow Me function node"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ffn/"
summary: "Síťová funkce definovaná ve 3GPP Release 4 pro podporu služby Follow Me, která uživateli umožňuje mít jediné, na poloze nezávislé číslo. Spravuje směrování hovorů a servisní logiku pro přesměrování ko"
---

FFN je síťová funkce podporující službu Follow Me tím, že spravuje směrování hovorů a servisní logiku pro přesměrování komunikace na aktuální polohu uživatele, čímž poskytuje jediné, na poloze nezávislé číslo.

## Popis

Follow Me function node (FFN) je entita řízení služeb specifikovaná v 3GPP TS 23.094. Jedná se o klíčovou komponentu doplňkové služby Follow Me ([FM](/mobilnisite/slovnik/fm/)), která poskytuje osobní mobilitu tím, že umožňuje účastníkovi být dosažitelný prostřednictvím jediného, trvalého čísla bez ohledu na jeho fyzickou polohu nebo používaný terminál. Z architektonického hlediska se FFN nachází ve služební vrstvě sítě, typicky komunikuje s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro data účastníka a s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC pro řízení hovorů. Jeho primární rolí je provádět servisní logiku pro příchozí hovory určené pro účastníka služby FM.

Když je uskutečněn hovor na Follow Me číslo účastníka, je hovor nejprve směrován na určený síťový uzel, často na konkrétní MSC. Tento uzel následně požádá FFN o instrukce pro směrování. FFN konzultuje svou interní databázi nebo propojený profil účastníka, který obsahuje uživatelovo aktuální aktivní kontaktní číslo nebo adresu. Tento profil je dynamicky aktualizován účastníkem, například pomocí [USSD](/mobilnisite/slovnik/ussd/) kódů nebo webového rozhraní, aby odrážel jeho aktuální preferovaný cíl (např. kancelářský telefon, mobilní telefon nebo hlasovou schránku). Na základě těchto informací FFN instruuje MSC, aby hovor přesměroval na specifikovanou kontaktní adresu.

Fungování FFN je zásadní pro realizaci plynulé osobní mobility. Zajišťuje překlad mezi logickým, na uživatele zaměřeným Follow Me číslem a fyzickou, sítí směrovatelnou adresou. Tím odděluje identitu uživatele od konkrétního zařízení nebo linky. Tento uzel také spravuje servisní triggery, komunikuje s účtovacími systémy pro účtování specifické pro službu a zajišťuje, že logika přesměrování odpovídá předdefinovaným pravidlům účastníka, jako je směrování podle denní doby nebo filtrování na základě volajícího. Ačkoli je konceptuálně samostatnou funkcí, její schopnosti byly později začleněny a rozšířeny širšími architekturami služeb IP Multimedia Subsystem (IMS) a funkcemi Voice Call Continuity ([VCC](/mobilnisite/slovnik/vcc/)), které nabízejí flexibilnější řešení osobní mobility založená na IP.

## K čemu slouží

FFN byl vytvořen, aby řešil rostoucí potřebu osobní mobility v raných sítích 3GPP, konkrétně v okruhově přepínané doméně. Před existencí takových služeb bylo telefonní číslo uživatele neodmyslitelně svázáno s konkrétní fyzickou linkou nebo [SIM](/mobilnisite/slovnik/sim/) kartou, což ztěžovalo udržení konzistentního kontaktního bodu při přesunu mezi lokalitami nebo zařízeními. Služba Follow Me, umožněná FFN, toto vyřešila zavedením vrstvy indirekce, která uživatelům umožnila definovat jedinou, trvalou identitu.

Motivace vycházela z obchodních a profesionálních potřeb, kdy jednotlivci vyžadovali stálé, dosažitelné číslo. FFN poskytl síťovou inteligenci, která to umožnila, aniž by bylo nutné měnit chování volající strany nebo základní směrovací protokoly jádrové sítě pro základní hovory. Představoval raný krok k oddělení uživatelské identity od topologie sítě, což je koncept, který se stal zásadním pro pozdější komunikační služby zcela na bázi IP. Ačkoli byla jeho implementace specifická pro konkrétní doplňkovou službu, položil konceptuální základy pro pokročilejší funkce jednotné komunikace a přenositelnosti čísel.

## Klíčové vlastnosti

- Spravuje servisní logiku pro doplňkovou službu Follow Me
- Komunikuje s HLR pro data účastníka a s MSC pro řízení hovorů
- Dynamicky překládá trvalé Follow Me číslo na aktuální směrovatelnou kontaktní adresu
- Podporuje aktualizace profilu řízené účastníkem prostřednictvím síťové signalizace (např. USSD)
- Umožňuje přesměrování hovorů na základě uživatelem definovaných pravidel a preferencí
- Integruje se s účtovacími systémy pro účtování specifické pro službu

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)

## Definující specifikace

- **TS 23.094** (Rel-19) — Follow Me (FM) Feature Stage 2

---

📖 **Anglický originál a plná specifikace:** [FFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ffn/)
