---
slug: "ebnf"
url: "/mobilnisite/slovnik/ebnf/"
type: "slovnik"
title: "EBNF – Extended Backus-Naur Form"
date: 2025-01-01
abbr: "EBNF"
fullName: "Extended Backus-Naur Form"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ebnf/"
summary: "Metasyntaktická notace používaná ve specifikacích 3GPP k formálnímu definování syntaxe protokolů, konfiguračních dat a dalších strukturovaných informací. Poskytuje přesnou, jednoznačnou a strojově čit"
---

EBNF je metasyntaktická notace používaná ve specifikacích 3GPP k formálnímu a jednoznačnému definování syntaxe protokolů a strukturovaných informací.

## Popis

Extended Backus-Naur Form (EBNF) je standardizovaný meta-jazyk hojně používaný v technických specifikacích 3GPP k poskytování formálních textových definic syntaxe. Jedná se o rozšíření základní Backus-Naurovy formy (BNF), které začleňuje dodatečné konstrukce pro opakování, volitelnost a seskupování, což ji činí stručnější a čitelnější pro definování složitých gramatik. V 3GPP se EBNF nepoužívá k definování programovacích jazyků, nýbrž k přesné definici struktury protokolových datových jednotek (PDU), formátů zpráv, hodnotových notací Abstract Syntax Notation One (ASN.1), konfiguračních parametrů a dokonce i syntaxe čitelných identifikátorů a řetězců v síťových rozhraních.

Notace se skládá ze souboru produkčních pravidel. Každé pravidlo definuje symbol (neterminál) a způsob, jakým může být rozvinut do sekvence dalších symbolů nebo terminálních znaků. Mezi klíčové operátory EBNF používané v 3GPP patří: '=' pro definici, ';' pro ukončení, '|' pro alternativu, '[]' pro volitelné prvky, '{}' pro opakování (nula nebo vícekrát) a '()' pro seskupení. Například jednoduché pravidlo pro číslici může být definováno jako `digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";`. Složitější pravidla definují přesné pořadí bajtů, oddělovače polí a rozsahy hodnot pro TLV (Type-Length-Value) ve zprávách Diameter nebo [GTP-C](/mobilnisite/slovnik/gtp-c/).

Její role je klíčová pro zajištění interoperability. Poskytnutím jediné autoritativní syntaktické definice EBNF odstraňuje nejednoznačnost, která by mohla vyplynout pouze z textových popisů. Výrobci zařízení a vývojáři softwaru mohou tyto definice EBNF použít k automatickému generování parserů, kodérů a validačních nástrojů pro protokolové zásobníky. Tím se snižují implementační chyby a usnadňuje se testování shody. Použití EBNF je zvláště výrazné ve specifikacích týkajících se správy sítě (např. řada 32 pro OAM), politiky a účtování (např. rozhraní Gx, Rx) a služebních rozhraní v 5G Core, kde musí být [API](/mobilnisite/slovnik/api/) a jejich datové struktury přesně definovány pro více-dodavatelská prostředí.

## K čemu slouží

EBNF byla v 3GPP přijata, aby řešila rostoucí složitost a potřebu přesnosti při definování komunikačních protokolů a datových formátů. Jak se mobilní sítě vyvíjely od okruhově přepínané hlasové služby ke složitým systémům založeným na IP se stovkami konfigurovatelných parametrů a složitými signalizačními zprávami, neformální textové popisy ve specifikacích se staly nedostatečnými. Vedly k rozdílným interpretacím mezi implementátory, což způsobovalo problémy s interoperabilitou při integraci sítí a prodlužovalo čas uvedení nových funkcí na trh.

Primární problém, který EBNF řeší, je nejednoznačnost. Přirozený jazyk může být nepřesný ohledně pořadí prvků, kardinality (kolikrát se něco vyskytuje) nebo přesné množiny povolených znaků. EBNF poskytuje formální, matematický základ pro definici syntaxe, který je zároveň čitelný pro člověka a vhodný pro automatizované zpracování. Tento formalismus byl motivován úspěchem podobných technik v informatice a telekomunikačních standardech, jako je ASN.1. Jeho zařazení do specifikací 3GPP, zejména od verze Rel-8 s nástupem EPS a později služební architektury 5G, odráží vyzrání standardizačního procesu směrem k rigoróznějším inženýrským postupům.

Historicky umožňuje vytváření spolehlivých testovacích sad a vývojových nástrojů. Existence strojově čitelné gramatiky umožňuje standardizačním orgánům a testovacím organizacím vyvíjet referenční parsery pro validaci vzorových zpráv. Dodavatelé mohou používat nástroje typu compiler-compiler (jako YACC nebo ANTLR) k přímému generování částí svého kódu ze specifikace, což zajišťuje věrnost standardu. Tím se snižují náklady na vývoj a zvyšuje se celková kvalita a stabilita nasazených sítí, což je nezbytné pro kritickou infrastrukturu.

## Klíčové vlastnosti

- Formální, jednoznačná definice syntaxe pro protokoly a datové struktury
- Používá produkční pravidla s operátory pro sekvenci, výběr, volitelnost a opakování
- Čitelná pro člověka, ale zároveň strojově parsovatelná notace
- Široce používaná v 3GPP pro definování management dat, parametrů API a formátů zpráv
- Snižuje implementační nejednoznačnost a podporuje více-dodavatelskou interoperabilitu
- Slouží jako základ pro automatizované generování kódu a testování shody

## Související pojmy

- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)

## Definující specifikace

- **TS 29.598** (Rel-19) — UDSF Service Based Interface Stage 3 Protocol
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention

---

📖 **Anglický originál a plná specifikace:** [EBNF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ebnf/)
