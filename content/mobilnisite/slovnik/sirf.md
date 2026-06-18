---
slug: "sirf"
url: "/mobilnisite/slovnik/sirf/"
type: "slovnik"
title: "SIRF – System Information Retrieval Function"
date: 2025-01-01
abbr: "SIRF"
fullName: "System Information Retrieval Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sirf/"
summary: "Bezpečnostní funkce definovaná v sítích 5G, která umožňuje zabezpečený a efektivní mechanismus pro UE k získání systémových informací (SI) ze sítě. Je součástí bezpečnostní architektury rozhraní založ"
---

SIRF je bezpečnostní funkce v sítích 5G, která poskytuje zabezpečený mechanismus pro UE k získání ověřených a proti neoprávněným změnám chráněných systémových informací prostřednictvím rozhraní založeného na službách (Service-Based Interface) 5G Core.

## Popis

Funkce pro získávání systémových informací (System Information Retrieval Function, SIRF) je síťová funkce v rámci bezpečnostního rámce 5G Core (5GC), standardizovaná od 3GPP Release 16 a novějších. Funguje jako bezpečnostní koncový bod, který usnadňuje zabezpečené získávání systémových informací ([SI](/mobilnisite/slovnik/si/)) uživatelským zařízením (UE). Systémové informace zahrnují zásadní data vysílaná rádiovou přístupovou sítí (např. gNB), která UE potřebují k objevení, výběru a přístupu do sítě, včetně parametrů pro výběr buňky, řízení přístupu a informací o sousedních buňkách. Zatímco některé SI jsou vysílány otevřeně, SIRF řeší potřebu zabezpečeného doručení určitých zpráv SI na vyžádání.

Architektonicky je SIRF logická funkce, která může být umístěna společně s jinými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), jako je Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) nebo specializovaná funkce pro správu SI. Zpřístupňuje rozhraní založené na službách (pravděpodobně využívající [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/), dle konvencí [SBI](/mobilnisite/slovnik/sbi/) pro 5GC), které je zabezpečeno pomocí mechanismů zabezpečení 5G. Když UE potřebuje konkrétní systémové informace, které nejsou vysílány, nebo potřebuje ověřenou kopii, může zahájit zabezpečenou relaci se SIRF. Tato interakce je chráněna bezpečnostním kontextem 5G navázaným během počáteční registrace, což zajišťuje vzájemné ověření mezi UE a sítí, stejně jako důvěrnost a ochranu integrity získaných informací.

SIRF funguje tak, že přijímá ověřené požadavky od UE, validuje je proti bezpečnostnímu kontextu a profilu předplatného UE, a poté načte požadované systémové informace. Tyto informace mohou být čerpány z centrálního úložiště nebo generovány dynamicky. SIRF následně zabalí a vrátí SI k UE chráněným způsobem. Tento mechanismus je obzvláště cenný pro doručování citlivých nebo rozsáhlých bloků SI, které je neefektivní často vysílat, pro poskytování konfigurací SI specifických pro UE nebo pro zajištění autenticity SI ve scénářích, kde by vysílané SI mohlo být falšováno (např. v nesatelitních sítích nebo v zranitelných oblastech pokrytí). Zvyšuje celkovou bezpečnost a efektivitu správy systémových informací v 5G.

## K čemu slouží

SIRF byla vytvořena k řešení specifických bezpečnostních a efektivitních výzev v doručování systémových informací pro pokročilé případy užití 5G definované od Release 16 a dále. Tradiční vysílání všech systémových informací je neefektivní pro parametry, které se mění zřídka, a je zranitelné vůči útokům falšováním, kdy by škodlivý vysílač mohl vysílat falešné síťové parametry k provedení útoků typu denial-of-service nebo man-in-the-middle.

Její zavedení bylo motivováno rozšířením 5G do nových scénářů nasazení, jako jsou Non-Public Networks ([NPN](/mobilnisite/slovnik/npn/)), Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)) a Non-Terrestrial Networks (NTN). V těchto prostředích je zajištění autenticity a integrity systémových informací prvořadé. Například v NPN musí být UE jisté, že získává SI z legitimní privátní sítě a nikoli z falešné buňky. Dále pro SI na vyžádání potřebuje síť zabezpečenou metodu pro doručení potenciálně rozsáhlých nebo specifických datových bloků pro UE bez spoléhání se na nezabezpečené vysílací kanály.

SIRF řeší tyto problémy využitím zavedené bezpečnostní architektury 5G. Poskytuje standardizovanou, zabezpečenou a službami založenou metodu pro získávání SI, což přesahuje čistě vysílací model. To umožňuje síťovým operátorům řídit přístup k určitým SI, ověřovat identitu získávajícího UE a chránit SI před pozměněním během doručení. Představuje vývoj od modelu 'důvěry v rozhraní vzduchu' pro SI k modelu 'zabezpečené služby', což je v souladu se širším principem 5GC, kterým jsou službami založené interakce chráněné robustními bezpečnostními protokoly.

## Klíčové vlastnosti

- Poskytuje zabezpečené rozhraní založené na službách pro získávání systémových informací na vyžádání ze strany UE.
- Integruje se s bezpečnostním rámcem 5G Core, čímž zajišťuje vzájemné ověření a ochranu dat SI.
- Podporuje efektivní doručování rozsáhlých, málo častých nebo specifických bloků systémových informací pro UE.
- Zvyšuje odolnost proti útokům pomocí falešných základnových stanic ověřováním zdroje SI.
- Umožňuje pokročilé scénáře nasazení, jako jsou Non-Public Networks (NPN) a Non-Terrestrial Networks (NTN).
- Funguje jako logická funkce, která může být umístěna společně s jinými síťovými funkcemi 5G Core.

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [SIRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sirf/)
