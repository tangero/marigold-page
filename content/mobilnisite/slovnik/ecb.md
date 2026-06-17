---
slug: "ecb"
url: "/mobilnisite/slovnik/ecb/"
type: "slovnik"
title: "ECB – Electronic Code-book (mode)"
date: 2025-01-01
abbr: "ECB"
fullName: "Electronic Code-book (mode)"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecb/"
summary: "ECB je základní režim provozu blokové šifry, kde je každý blok otevřeného textu šifrován nezávisle stejným klíčem. Jde o základní, avšak nezabezpečený režim, protože vzory v otevřeném textu zůstávají"
---

ECB je základní a nezabezpečený režim blokové šifry, kde je každý blok otevřeného textu šifrován nezávisle stejným klíčem, což zachovává vzory otevřeného textu v šifrovém textu.

## Popis

Electronic Code-book (ECB) je režim provozu blokové šifry. V režimu ECB je proces šifrování přímočarý: vstupní zpráva v podobě otevřeného textu je rozdělena na bloky pevné velikosti (např. 128 bitů pro [AES](/mobilnisite/slovnik/aes/)). Každý blok je poté nezávisle zašifrován pomocí stejného symetrického klíče. Výsledný šifrový text je prostým spojením zašifrovaných bloků. Dešifrování následuje stejný princip v opačném pořadí, přičemž každý blok šifrového textu je dešifrován nezávisle, aby se obnovil původní blok otevřeného textu.

Klíčovou charakteristikou ECB je jeho bezstavová a deterministická povaha. Pro daný klíč budou identické bloky otevřeného textu vždy produkovat identické bloky šifrového textu. Tato vlastnost vede k jeho hlavní kryptografické slabině: vzory přítomné v otevřeném textu jsou přímo odhaleny v šifrovém textu. Například obrázek v otevřeném textu zašifrovaný pomocí ECB by v šifrovém textu ukázal nejasný obrys původního obrázku, protože oblasti jednotné barvy produkují jednotné bloky šifrového textu.

Z architektonického hlediska ECB nevyžaduje inicializační vektor ([IV](/mobilnisite/slovnik/iv/)) ani žádný zpětnovazební mechanismus. Funguje přímo na blocích otevřeného textu. V systémech 3GPP je ECB specifikována především jako základní nebo referenční algoritmus v rámci bezpečnostních specifikací. Kvůli svým zranitelnostem se nepoužívá pro ochranu uživatelských dat nebo signalizace v živých sítích. Její role je často didaktická nebo jako součást složitějších kryptografických konstrukcí, kde je nedostatečná difuze řešena jinými prostředky.

Z pohledu implementace je ECB nejjednodušším režimem k implementaci, protože zahrnuje přímou aplikaci šifrovacích a dešifrovacích funkcí blokové šifry bez jakékoli řetězové logiky. Tato jednoduchost je však vykoupena bezpečností. V moderních architekturách 3GPP je ECB explicitně vyhýbáno pro jakoukoli ochranu důvěrnosti. Její zmínka ve specifikacích, jako je 31.113 (bezpečnost UICC), je typicky v kontextu definování algoritmů, kde může být ECB základním režimem pro specifickou funkci s omezeným účelem, nikdy však pro obecné šifrování dat.

## K čemu slouží

Režim ECB existuje jako nejzákladnější a koncepčně nejjednodušší režim provozu blokových šifer. Byl vytvořen k demonstraci základní aplikace blokové šifry na data delší než jeden blok. Historicky byl jedním z prvních definovaných režimů a sloužil jako stavební kámen pro pochopení kryptografie.

Primární problém, který ECB 'řeší', je triviální rozšíření šifrování blokové šifry s pevnou délkou bloku na zprávu libovolné délky. Neřeší však kritický problém poskytování sémantické bezpečnosti. Motivací pro jeho definování ve standardech, jako je 3GPP, je mít kompletní sadu zdokumentovaných algoritmů a režimů pro referenci, testování a interoperabilitu ve velmi omezených scénářích. Jeho zařazení umožňuje specifikaci kryptografických sad, i když některé režimy nejsou doporučeny pro obecné použití.

Omezení ECB jsou závažná a přímo motivovala vytvoření všech ostatních standardních režimů ([CBC](/mobilnisite/slovnik/cbc/), [CTR](/mobilnisite/slovnik/ctr/), GCM atd.). Neposkytuje difuzi; vzory a opakování v otevřeném textu přímo pronikají do šifrového textu. Je také zranitelný vůči replay a manipulačním útokům, protože bloky lze přeskupit, odstranit nebo duplikovat bez ovlivnění dešifrování ostatních bloků. Jeho účelem v současném 3GPP tedy není nasazení, ale úplnost specifikace a role kryptografického primitiva, které může být použito interně jinými, zabezpečenými konstrukcemi.

## Klíčové vlastnosti

- Nezávislé šifrování bloků: Každý blok otevřeného textu je šifrován samostatně bez řetězení.
- Deterministický výstup: Identické bloky otevřeného textu produkují identické bloky šifrového textu pod stejným klíčem.
- Nevyžaduje inicializační vektor (IV): Zjednodušuje provoz, ale snižuje bezpečnost.
- Paralelizovatelné šifrování a dešifrování: Bloky lze zpracovávat současně díky žádným závislostem.
- Chybí šíření chyb: Poškozený blok šifrového textu ovlivní pouze odpovídající blok otevřeného textu.
- Jednoduchá implementace: Přímá aplikace základní funkce blokové šifry.

## Související pojmy

- [AES – Advanced Encryption Standard](/mobilnisite/slovnik/aes/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [ECB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecb/)
