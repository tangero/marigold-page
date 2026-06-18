---
slug: "tvp"
url: "/mobilnisite/slovnik/tvp/"
type: "slovnik"
title: "TVP – Time Variant Parameter"
date: 2025-01-01
abbr: "TVP"
fullName: "Time Variant Parameter"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tvp/"
summary: "TVP je bezpečnostní parametr definovaný v 3GPP, který se v čase mění a používá se v autentizačních a dohodovacích protokolech klíčů. Zvyšuje bezpečnost zavedením dynamických prvků, které zabraňují rep"
---

TVP je bezpečnostní parametr definovaný v 3GPP, který se v čase mění a používá se v autentizačních protokolech k zabránění replay útoků a zajištění aktuálnosti.

## Popis

Time Variant [Parameter](/mobilnisite/slovnik/parameter/) (TVP) je bezpečnostní koncept specifikovaný v 3GPP TS 33.204, který označuje parametry měnící se v čase a používané v kryptografických protokolech k zajištění aktuálnosti a zabránění replay útokům. V mobilních sítích jsou TVP nedílnou součástí procedur autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)), jako jsou ty definované pro UMTS, LTE a 5G. Typicky zahrnují časová razítka, sekvenční čísla nebo nonces generované sítí nebo uživatelským zařízením (UE) a začleněné do bezpečnostních zpráv. Tím, že se mění s každou transakcí, TVP zaručují, že každý pokus o autentizaci je jedinečný, což útočníkům ztěžuje opětovné použití zachycených zpráv.

Architektonicky se TVP používají v Autentizačním centru (AuC) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jádra sítě, které generují autentizační vektory obsahující TVP jako [RAND](/mobilnisite/slovnik/rand/) (náhodná výzva) a [SQN](/mobilnisite/slovnik/sqn/) (sekvenční číslo). Tyto vektory jsou odesílány do servisní sítě, například [MME](/mobilnisite/slovnik/mme/) v LTE nebo [AMF](/mobilnisite/slovnik/amf/) v 5G, která je použije k výzvě pro UE. UE následně vypočítává odpovědi na základě TVP a ověřuje jejich aktuálnost prostřednictvím synchronizačních mechanismů. Mezi klíčové komponenty patří systém správy SQN, který udržuje čítače pro sledování autentizačních událostí, a generátory založené na čase, které produkují časová razítka, když je to potřeba. TVP také hrají roli v odvozování klíčů, čímž zajišťují, že relakční klíče jsou pro každé spojení jedinečné.

V provozu TVP fungují tak, že vkládají časově citlivé hodnoty do bezpečnostních protokolů, jako je EPS AKA nebo 5G AKA. Například během autentizační žádosti síť odešle UE RAND (TVP), který UE zkombinuje se sdíleným tajným klíčem, aby vytvořila odpověď. UE také kontroluje SQN, aby zajistila, že je v přijatelném rozsahu, a tím zabránila útokům mimo pořadí. Pokud je TVP neplatný nebo zastaralý, autentizace selže a spustí se procedury resynchronizace. TVP zvyšují bezpečnost přidáním prvku nepředvídatelnosti, což je zásadní pro prevenci útoků jako man-in-the-middle nebo hijacking relace. Jejich implementace vyžaduje pečlivou synchronizaci mezi síťovými entitami a UE, aby se předešlo falešným zamítnutím, což je často řízeno prostřednictvím hysterezních oken nebo resynchronizačních protokolů.

## K čemu slouží

TVP byl zaveden, aby řešil bezpečnostní zranitelnosti v raných autentizačních protokolech pro mobilní sítě, kterým chyběly dynamické prvky a byly náchylné k replay útokům. Ve 2G systémech, jako je GSM, autentizace spoléhala na statické výzvy, což útočníkům usnadňovalo zachytit a znovu použít přihlašovací údaje. TVP přidávají do autentizačních zpráv časově proměnné složky, čímž zajišťují, že každá transakce je aktuální a jedinečná. Tím se zvyšuje celková bezpečnost sítí 3GPP, protože chrání proti odposlechu, zneužití identity a dalším hrozbám, které využívají statické parametry.

Vznik TVP byl motivován potřebou silnější bezpečnosti, jak se mobilní sítě vyvíjely, aby podporovaly citlivé aplikace jako mobilní bankovnictví a IoT. Začleněním TVP poskytly standardy 3GPP, jako UMTS [AKA](/mobilnisite/slovnik/aka/) a později EPS AKA, základ pro robustní dohodu klíčů a vzájemnou autentizaci. TVP také podporují funkce ochrany soukromí, jako je skrytí identity uživatele prostřednictvím dočasných identifikátorů, které se v čase mění. Řeší omezení předchozích přístupů tím, že umožňují dopřednou bezpečnost a snižují riziko dlouhodobého kompromitování klíčů, což je v souladu s regulatorními požadavky na ochranu dat a integritu sítě.

## Klíčové vlastnosti

- Zajišťuje aktuálnost autentizačních zpráv, aby zabránil replay útokům
- Integruje se s protokoly AKA v UMTS, LTE a 5G
- Zahrnuje parametry jako RAND, SQN a časová razítka
- Podporuje synchronizační mechanismy mezi sítí a UE
- Zlepšuje odvozování klíčů pro jedinečné relakční klíče
- Usnadňuje ochranu soukromí prostřednictvím časově proměnných identifikátorů

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [SQN – Sequence Number](/mobilnisite/slovnik/sqn/)
- [RAND – RANDom number (authentication parameter)](/mobilnisite/slovnik/rand/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [TVP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tvp/)
