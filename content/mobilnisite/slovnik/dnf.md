---
slug: "dnf"
url: "/mobilnisite/slovnik/dnf/"
type: "slovnik"
title: "DNF – Disjunctive Normal Form"
date: 2025-01-01
abbr: "DNF"
fullName: "Disjunctive Normal Form"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/dnf/"
summary: "Standardizovaný formát logických výrazů používaný v 3GPP pro reprezentaci složitých podmínek, zejména pro vystavení funkcí sítě a řízení politik. Umožňuje přesné, strojově čitelné definice požadavků n"
---

DNF je standardizovaný formát logických výrazů používaný v 3GPP pro reprezentaci složitých podmínek, který umožňuje přesné, strojově čitelné definice pro automatizované rozhodování sítě v oblasti vystavení funkcí a řízení politik.

## Popis

Disjunktivní normální forma (DNF) je kanonický tvar logického vzorce skládající se z disjunkce (operace [OR](/mobilnisite/slovnik/or/)) jedné nebo více konjunkcí (operací [AND](/mobilnisite/slovnik/and/)) literálů. V normách 3GPP je DNF přijata jako strukturovaný datový model pro standardizovanou a jednoznačnou reprezentaci složitých podmínek nebo predikátů. To je klíčové pro scénáře, kdy síťové funkce potřebují vyhodnocovat více kritérií vůči sadě pravidel, jako je řízení politik, vystavení funkcí sítě nebo poskytování parametrů služeb.

V rámci architektury 3GPP je DNF specifikována pro použití v [API](/mobilnisite/slovnik/api/) a informačních modelech, zejména v Common API Framework ([CAPIF](/mobilnisite/slovnik/capif/)) a Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)). Poskytuje formální metodu pro zakódování podmínek jako "(Podmínka A A Podmínka B) NEBO (Podmínka C A Podmínka D A [NE](/mobilnisite/slovnik/ne/) Podmínka E)". Každý literál v konjunkci může reprezentovat konkrétní síťový parametr, atribut uživatele, polohu, čas nebo charakteristiku služby. Celý DNF výraz se vyhodnotí jako PRAVDA, pokud alespoň jedna z jeho konstitučních konjunkcí vyhodnotí jako PRAVDA.

Úlohou DNF je umožnit dynamické a flexibilní vynucování politik. Například poskytovatel služeb může definovat politiku pro novou aplikaci, kde je zvýšená QoS přidělena pouze tehdy, pokud je uživatel na konkrétní poloze (literál 1) A je přihlášen k prémiovému tarifu (literál 2) A je dostupný síťový řez (literál 3). Tato celá konjunkce tvoří jednu klauzuli. Alternativní klauzule může být pro scénáře roamingu. Použitím DNF může síť tyto vícerozměrné podmínky programově parsovat a vyhodnocovat bez nejednoznačnosti, což je zásadní pro automatizaci v sítích 5G a dalších generací.

## K čemu slouží

Účelem standardizace Disjunktivní normální formy v 3GPP je řešit rostoucí složitost síťových politik a požadavků služeb v systémech 5G. Předchozí přístupy se často spoléhaly na proprietární nebo ad-hoc reprezentace podmínek uvnitř síťových funkcí, což bránilo interoperabilitě a ztěžovalo automatizovanou správu politik. Jak se sítě vyvíjely, aby podporovaly síťové řezy, edge computing a rozmanité IoT služby, potřeba robustního, formálního jazyka pro vyjádření složité servisní logiky se stala prvořadou.

DNF byla zavedena, aby poskytla společný, matematicky podložený základ pro vyjadřování podmínek napříč různými doménami 3GPP. Řeší problém nejednoznačnosti v pravidlech politik, zajišťuje, že podmínka definovaná jednou síťovou funkcí (např. Policy Control Function) je interpretována shodně jinou funkcí (např. Session Management Function). To je kritické pro zajištění služeb end-to-end a pro vystavení síťových schopností aplikacím třetích stran předvídatelným způsobem prostřednictvím [API](/mobilnisite/slovnik/api/), jako jsou ta poskytovaná [NEF](/mobilnisite/slovnik/nef/).

Historicky byly podmínky politik často pevně zakódované nebo popsané přirozeným jazykem ve specifikacích, což vedlo k rozdílům v implementaci. Přijetí DNF, počínaje Release 15, je v souladu s širším posunem 3GPP k architekturám založeným na službách a principům softwarově definovaných sítí, kde je klíčová dynamická, daty řízená konfigurace. Poskytuje potřebný formalismus pro umožnění komunikace složitých obchodních a provozních pravidel mezi stroji.

## Klíčové vlastnosti

- Standardizovaný formát logických výrazů pro jednoznačnou reprezentaci podmínek
- Podporuje složité kombinace operací AND, OR a NOT
- Umožňuje strojově čitelné definice politik a požadavků služeb
- Usnadňuje interoperabilitu mezi různými síťovými funkcemi a externími aplikacemi
- Používá se v 3GPP API pro vystavení funkcí sítě a řízení politik (např. NEF, CAPIF)
- Poskytuje základ pro dynamické, automatizované rozhodování sítě a poskytování služeb

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.884** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [DNF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dnf/)
