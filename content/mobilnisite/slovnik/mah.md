---
slug: "mah"
url: "/mobilnisite/slovnik/mah/"
type: "slovnik"
title: "MAH – Mobile Access Hunting supplementary service"
date: 2025-01-01
abbr: "MAH"
fullName: "Mobile Access Hunting supplementary service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mah/"
summary: "Doplňková telefonní služba, která umožňuje, aby příchozí hovor na zaneprázdněného nebo neodpovídajícího účastníka postupně prohledával předdefinovaný seznam alternativních cílů. Zvyšuje míru dokončení"
---

MAH je doplňková telefonní služba, která umožňuje, aby příchozí hovor na zaneprázdněného nebo neodpovídajícího účastníka postupně prohledával předdefinovaný seznam alternativních cílů za účelem zvýšení úspěšnosti dokončení hovoru.

## Popis

Mobile Access Hunting (MAH) je standardizovaná doplňková služba v sítích 3GPP, která automatizuje proces přesměrování příchozího hovoru, když je primární cíl zaneprázdněn nebo neodpovídá. Služba je implementována v rámci řídicí logiky služeb v jádru sítě, typicky spojené s Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo aplikačním serverem v IMS. Když je uskutečněn hovor na účastníka, který má MAH aktivovanou a jehož linka je zaneprázdněna nebo neodpovídá po konfigurovatelném počtu zvonění či časovém intervalu, je služba spuštěna. Síť následně konzultuje seznam prohledávání definovaný účastníkem nebo operátorem, což je uspořádaná sekvence alternativních cílů. Tyto cíle mohou zahrnovat jiná telefonní čísla spojená se stejným účastníkem (např. mobilní telefon, pracovní telefon nebo domácí telefon) nebo systém hlasové schránky. Síť postupně pokouší navázat hovor na každý cíl v seznamu podle definovaného pořadí, dokud není hovor úspěšně spojen nebo není seznam vyčerpán. Logika služby zajišťuje přesměrování hovoru, spravuje časovače pro podmínky neodpovědi a poskytuje volající straně během procesu prohledávání odpovídající tóny nebo hlášení. Mezi klíčové komponenty patří profil služby účastníka uložený v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), který obsahuje seznam prohledávání a stav aktivace, a prostředí pro provádění služby v MSC nebo call session control function. MAH zvyšuje efektivitu sítě automatizací přesměrování hovorů, snižuje počet neúspěšných pokusů o hovor a poskytuje plynulý zážitek jak pro volajícího, tak pro volaného.

## K čemu slouží

Služba MAH byla vyvinuta k řešení běžného telefonního problému zmeškaných hovorů a obsazovacích tónů, čímž zvyšuje míru dokončení hovorů a dostupnost účastníků v mobilních sítích. Před existencí takových automatizovaných služeb museli volající ručně znovu vytáčet nebo zkoušet alternativní čísla, pokud byl účastník nedostupný, což vedlo k frustraci a neefektivnímu využití síťových zdrojů. MAH tento proces automatizuje a napodobuje funkci 'hunt group' běžnou v podnikových ústřednách ([PBX](/mobilnisite/slovnik/pbx/)), ale pro jednotlivé mobilní účastníky. Její vytvoření bylo motivováno snahou vylepšit základní nabídku telefonních služeb, poskytnout uživatelům větší kontrolu nad jejich dostupností a zajistit, aby se důležité hovory k nim mohly dostat alternativními prostředky. Standardizací MAH v rámci 3GPP bylo zajištěno konzistentní chování napříč různými sítěmi a zařízeními, což operátorům umožnilo nabízet spolehlivou a hodnotnou funkci, která zvyšuje spokojenost účastníků a využití sítě. Vyřešila omezení statického přesměrování hovorů tím, že poskytla dynamický, sekvenční vyhledávací mechanismus, který byl obzvláště užitečný v éře, kdy jednotlivci začali používat více komunikačních zařízení.

## Klíčové vlastnosti

- Postupně prohledává předdefinovaný seznam alternativních cílů
- Spouští se při podmínce obsazení nebo vypršení časového limitu pro neodpověď
- Seznam prohledávání a stav aktivace konfigurovatelné účastníkem
- Integruje se s řízením hovorů v jádru sítě a databázemi účastníků
- Zajišťuje dokončení hovoru na hlasovou schránku nebo jiná přidružená čísla
- Standardizované chování napříč sítěmi 3GPP pro interoperabilitu

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MAH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mah/)
