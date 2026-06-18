---
slug: "ehplmn"
url: "/mobilnisite/slovnik/ehplmn/"
type: "slovnik"
title: "EHPLMN – Equivalent Home Public Land Mobile Network"
date: 2025-01-01
abbr: "EHPLMN"
fullName: "Equivalent Home Public Land Mobile Network"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ehplmn/"
summary: "EHPLMN je seznam identifikátorů sítí (PLMN ID) považovaných za ekvivalentní domovské PLMN (HPLMN) uživatele pro výběr sítě a roamování. Umožňuje bezproblémový přístup ke službám napříč partnerskými sí"
---

EHPLMN je seznam identifikátorů sítí považovaných za ekvivalentní domovské PLMN uživatele pro výběr sítě, umožňující bezproblémový přístup ke službám napříč partnerskými sítěmi bez toho, aby byl považován za roamování.

## Popis

Equivalent Home Public Land Mobile Network (EHPLMN) je koncept v 3GPP, který definuje sadu jednoho či více identifikátorů veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/) ID), které jsou považovány za ekvivalentní domovské PLMN ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka. HPLMN je síť provozovaná poskytovatelem služeb účastníka, identifikovaná Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) na jeho [SIM](/mobilnisite/slovnik/sim/)/[USIM](/mobilnisite/slovnik/usim/). Seznam EHPLMN je uložen na SIM/USIM a používá jej uživatelské zařízení (UE) během procedur výběru sítě a registrace. Když UE vyhledává dostupné sítě, upřednostňuje sítě, jejichž PLMN ID odpovídá buď jeho HPLMN, nebo jakémukoli PLMN v seznamu EHPLMN. Pokud je taková síť nalezena, UE se s ní pokusí zaregistrovat, jako by šlo o domovskou síť, často s výhodami služeb jako v domovské síti a potenciálně bez roamovacích poplatků v závislosti na dohodách operátorů.

Z architektonického hlediska je seznam EHPLMN zřízen operátorem domovské sítě na SIM kartu. Používají jej vrstvy správy mobility ([MM](/mobilnisite/slovnik/mm/)) a správy spojení ([CM](/mobilnisite/slovnik/cm/)) v UE. Během počátečního výběru buňky nebo po ztrátě pokrytí UE skenuje rádiové frekvence a dekóduje PLMN ID vysílané buňkami. Výběrový algoritmus, definovaný ve specifikacích jako TS 23.122, nařizuje, že UE se musí pokusit zaregistrovat na EHPLMN s vyšší prioritou než na navštívené PLMN (VPLMN). Jádrová síť, konkrétně Home Subscriber Server (HSS) nebo Unified Data Management (UDM), může tento koncept také používat k aplikaci specifických zásad předplatného, když je uživatel na EHPLMN.

EHPLMN funguje ve spojení s dalšími seznamy PLMN, jako je seznam zakázaných PLMN (FPLMN) a uživatelsky řízený selektor PLMN. Jeho role je klíčová pro umožnění národního roamingu, dohod o sdílení sítí a multi-operator core networks (MOCN). Například ve scénáři sdílení sítě, kde dva operátoři sdílejí infrastrukturu rádiového přístupu, ale mají oddělené jádrové sítě, může každý operátor nakonfigurovat PLMN druhého jako EHPLMN pro své účastníky. To umožňuje účastníkům automaticky se připojit ke sdílené síti bez manuálního výběru a přijímat služby, jako by byli ve své domovské síti, což zajišťuje bezproblémovou mobilitu a kontinuitu služeb.

## K čemu slouží

EHPLMN byl zaveden k řešení problému bezproblémového přístupu k síti ve scénářích zahrnujících více spolupracujících operátorů, jako jsou dohody o národním roamingu, sdílení sítí (např. MORAN, MOCN) a fúze/akvizice. Před jeho definicí by UE považovalo jakoukoli PLMN odlišnou od své HPLMN za navštívenou síť, což vedlo k potenciálním indikátorům roamingu, odlišnému zacházení se službami a nutnosti manuálního výběru sítě uživatelem. To zhoršovalo uživatelský zážitek a komplikovalo provozní modely, kde operátoři chtěli prezentovat jednotnou síťovou stopu.

Koncept, zavedený ve 3GPP Release 7, byl motivován rostoucí složitostí partnerských vztahů operátorů a potřebou flexibilnější správy účastníků. Umožňuje operátorovi transparentně rozšířit zážitek 'domovské sítě' na partnerské sítě. Tím řeší omezení základní dichotomie HPLMN/VPLMN tím, že poskytuje standardizovaný způsob definice sady 'ekvivalentních domovských' sítí. To umožňuje provozní efektivitu, zlepšený zákaznický zážitek skrytím hranic sítí a podporuje regulatorní požadavky na povinnosti pokrytí prostřednictvím partnerství.

## Klíčové vlastnosti

- Seznam PLMN ID uložených na USIM/SIM považovaných za ekvivalentní HPLMN
- Používán UE pro automatický výběr sítě s vyšší prioritou než VPLMN
- Umožňuje bezproblémový přístup ke službám ve scénářích sdílení sítí a národního roamingu
- Zřizován operátorem domovské sítě
- Integruje se s předplatitelskými daty v jádrové síti pro vynucování zásad
- Podporuje kontinuitu služeb a zacházení jako v domovské síti na partnerských sítích

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.391** (Rel-19) — USSD over IMS Management Object Specification
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures

---

📖 **Anglický originál a plná specifikace:** [EHPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ehplmn/)
