---
slug: "naa"
url: "/mobilnisite/slovnik/naa/"
type: "slovnik"
title: "NAA – Network Access Application"
date: 2025-01-01
abbr: "NAA"
fullName: "Network Access Application"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/naa/"
summary: "Bezpečnostní aplikace umístěná na univerzální integrované obvodové kartě (UICC) nebo SIM kartě, která spravuje procedury autentizace a dohody o klíčích mezi uživatelským zařízením (UE) a mobilní sítí."
---

NAA je bezpečnostní aplikace na UICC nebo SIM kartě, která spravuje procedury autentizace a dohody o klíčích mezi zařízením uživatele a mobilní sítí prováděním autentizačních algoritmů 3GPP.

## Popis

Aplikace pro přístup k síti (NAA) je klíčová bezpečnostní aplikace, která sídlí v bezpečném výkonném prostředí univerzální integrované obvodové karty (UICC), která zahrnuje karty [SIM](/mobilnisite/slovnik/sim/), [USIM](/mobilnisite/slovnik/usim/) a [ISIM](/mobilnisite/slovnik/isim/). Jejím hlavním úkolem je provádět procedury autentizace a dohody o klíčích ([AKA](/mobilnisite/slovnik/aka/)) definované standardy 3GPP. NAA funguje jako koncový bod v UE pro výzva-odpověď protokol, který ověřuje identitu účastníka vůči síti a stanovuje šifrovací a integritní klíče pro zabezpečenou komunikaci. Každý typ síťového přístupu (GSM, UMTS, LTE, 5G) má odpovídající NAA: aplikace SIM pro GSM, aplikace USIM pro UMTS/LTE a aplikace ISIM pro přístup k IMS.

Architektonicky je NAA apleta Java Card nebo nativní aplikace běžící na mikroprocesoru UICC. Obsahuje jedinečný tajný klíč účastníka (Ki pro GSM, K pro UMTS/5G) a implementované autentizační algoritmy (např. COMP128 pro GSM, Milenage nebo TUAK pro UMTS/5G). Když se UE pokouší připojit k síti, obslužná síť (např. [MME](/mobilnisite/slovnik/mme/), [SGSN](/mobilnisite/slovnik/sgsn/)) přepošle autentizační vektor přijatý z autentizačního centra (AuC) domovské sítě nebo z jednotné správy dat ([UDM](/mobilnisite/slovnik/udm/)). Tento vektor obsahuje náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)) a očekávanou odpověď (XRES) mimo jiné parametry. RAND je odeslán do UE a předán NAA na UICC.

NAA poté použije tajný klíč (K) a přijatý RAND k výpočtu odpovědi (RES) a šifrovacích/integritních klíčů (CK, IK). Vypočítaný RES je odeslán zpět do sítě pro ověření proti XRES. Pokud se shodují, je autentizace úspěšná a síť nařídí UE použít odvozené CK a IK pro zabezpečení rozhraní rádiového přístupu. NAA zajišťuje, že tajný klíč nikdy neopustí bezpečný okruh UICC. Pro 5G NAA (v rámci USIM) také vypočítává kotvící klíč KAUSF, který se používá k odvození dalších klíčů v odolném úložišti UE, což umožňuje vylepšené oddělení hierarchie klíčů. Role NAA je čistě výpočetní a reaktivní; sama procedury nespouští, ale bezpečně provádí algoritmy definované síťovou výzvou.

## K čemu slouží

Aplikace pro přístup k síti (NAA) existuje za účelem poskytnutí standardizované, bezpečné a přenosné metody pro autentizaci účastníka a generování klíčů v mobilních sítích. Její vznik byl motivován potřebou přesunout citlivé kryptografické operace a přihlašovací údaje účastníka z potenciálně méně bezpečného mobilního zařízení do vyhrazeného hardwarového modulu odolného proti neoprávněné manipulaci – UICC. Před modelem UICC/NAA měly rané analogové systémy minimální autentizaci a proprietární řešení byla nebezpečná. Tento koncept zavedla SIM karta GSM a vyvinula se v USIM/NAA pro 3G a novější sítě.

NAA řeší několik klíčových problémů: zajišťuje důvěrnost identity účastníka a bezpečnost sítě tím, že chrání dlouhodobý tajný klíč. Umožňuje interoperabilitu, protože jediná UICC s příslušnou NAA může být použita v jakémkoli kompatibilním zařízení na světě. Poskytuje také jasné oddělení mezi účastníkovým předplatným (na UICC) a samotným zařízením, což usnadňuje snadnou výměnu zařízení. Vývoj od SIM k USIM a ISIM NAA řešil omezení dřívějších algoritmů, jako jsou zranitelnosti v COMP128 pro GSM, zavedením silnější vzájemné autentizace (v UMTS a novějších), delších klíčů a robustnějších kryptografických algoritmů pro ochranu proti novým hrozbám, jako jsou útoky falešnou základnovou stanicí.

## Klíčové vlastnosti

- Sídlí na zabezpečeném hardwaru UICC (SIM/USIM/ISIM)
- Ukládá dlouhodobý tajný autentizační klíč účastníka (K)
- Provádí protokol 3GPP pro autentizaci a dohodu o klíčích (AKA)
- Vypočítává autentizační odpověď (RES) a šifrovací klíče (CK, IK)
- Poskytuje prostředí odolné proti neoprávněné manipulaci pro kryptografické operace
- Umožňuje mobilitu účastníka a nezávislost na zařízení

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API

---

📖 **Anglický originál a plná specifikace:** [NAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/naa/)
