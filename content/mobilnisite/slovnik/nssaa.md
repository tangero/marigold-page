---
slug: "nssaa"
url: "/mobilnisite/slovnik/nssaa/"
type: "slovnik"
title: "NSSAA – Network Slice-Specific Authentication and Authorization"
date: 2026-01-01
abbr: "NSSAA"
fullName: "Network Slice-Specific Authentication and Authorization"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nssaa/"
summary: "NSSAA je bezpečnostní architektura v rámci 5G, která provádí kontrolu autentizace a autorizace specifickou pro požadovaný síťový řez. Zajišťuje, že UE není pouze autentizována pro základní síť, ale je"
---

NSSAA je bezpečnostní architektura 5G, která provádí autentizaci a autorizaci specifickou pro síťový řez a zajišťuje, že uživatelskému zařízení je výslovně povolen přístup ke konkrétnímu síťovému řezu nad rámec obecného přístupu k síti.

## Popis

Network Slice-Specific Authentication and Authorization (NSSAA) je klíčový bezpečnostní mechanismus zavedený ve specifikaci 3GPP Release 16, který doplňuje primární autentizaci a autorizaci prováděnou funkcí Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). Zatímco primární autentizace ověřuje identitu UE pro celou 5G Core Network (5GC), NSSAA poskytuje dodatečnou, granulární vrstvu zabezpečení pro jednotlivé síťové řezy. To je nezbytné, protože různé řezy mohou mít výrazně odlišné bezpečnostní požadavky, obchodní modely a domény důvěry. Například řez pro hromadné IoT senzory může mít jiné bezpečnostní nastavení než řez pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) v průmyslové automatizaci. NSSAA zajišťuje, že přístup k vysoce zabezpečenému řezu není udělen pouze na základě pověření platných pro řez s nižší úrovní zabezpečení.

Procedura NSSAA je typicky spuštěna po úspěšné primární autentizaci, když UE požádá o síťový řez vyžadující autentizaci specifickou pro daný řez, což je indikováno informací Subscribed Network Slice Selection Assistance Information ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)). Proceduru řídí funkce Network Slice-Specific Authentication and Authorization Function ([NSSAAF](/mobilnisite/slovnik/nssaaf/)), která funguje jako zprostředkovatel. NSSAAF přijímá žádost o autentizaci od funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a komunikuje s externími, na řez specifickými servery Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)). Tyto externí AAA servery jsou považovány za součást domény tenanta řezu a jsou zodpovědné za vyhodnocení pověření UE vůči politikám specifickým pro daný řez. Komunikace mezi NSSAAF a externím AAA serverem může využívat protokoly jako Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)), což umožňuje širokou škálu autentizačních metod (EAP-AKA', EAP-TLS atd.), jak je definováno poskytovatelem řezu.

Architektura zahrnuje několik síťových funkcí 5GC. AMF je hlavním kontaktním bodem, který proceduru iniciuje na základě žádosti o řez. NSSAAF, dedikovaná logická funkce, může být nasazena jako samostatná síťová funkce ([NF](/mobilnisite/slovnik/nf/)) nebo společně s jinou NF, například s AUSF. Rozhraní s externím AAA serverem zprostředkovává referenční bod N33. Funkce Unified Data Management (UDM) může uchovávat indikace, které S-NSSAI vyžadují NSSAA pro daného účastníka. Výsledek procedury (úspěch, selhání nebo průběh) je předán zpět AMF, která následně povolí nebo zamítne registraci UE pro požadovaný řez. Klíčovým aspektem je, že NSSAA může běžet paralelně pro více řezů a její selhání pro jeden řez nemusí nutně ovlivnit registraci UE pro jiné, již autorizované řezy. To poskytuje flexibilitu a zachovává kontinuitu služeb tam, kde je to možné.

## K čemu slouží

NSSAA byla vytvořena, aby řešila bezpečnostní výzvy a výzvy obchodních modelů inherentní síťovému krájení. Před jejím zavedením v Release 16 bylo řízení přístupu k síťovým řezům primárně založeno na předplatitelských datech uložených v UDM, která mohla indikovat, zda je účastníkovi použití řezu povoleno. Šlo však o jednoduchou binární kontrolu, která nepodporovala dynamická, reálná rozhodnutí o autentizaci a autorizaci, jež by mohla zahrnovat externí pověření nebo politiky specifické pro tenanta. Toto omezení bylo významnou překážkou pro podniky a vertikální odvětví, která si přála provozovat vlastní řezy s vlastními systémy správy identit.

Hlavním problémem, který NSSAA řeší, je potřeba zvýšené bezpečnostní izolace mezi řezy. Ve sdílené fyzické infrastruktuře je prvořadé zajistit, aby kompromitace nebo slabá autentizace v jednom řezu nestala vektorem pro přístup k citlivějšímu řezu. Delegováním finálního rozhodnutí o autorizaci na externí AAA server řízený tenantem řezu umožňuje NSSAA silnou, na doménu specifickou autentizaci. To je zásadní pro obchodní modely, kdy mobilní operátor (MNO) poskytuje síť jako službu třetím stranám, například podnikům. Podnik si může zachovat kontrolu nad tím, která jeho zařízení nebo uživatelé jsou povoleni na jeho dedikovaný řez, a to za použití stávajících podnikových přihlašovacích údajů a bezpečnostních politik, aniž by MNO musel tyto identity spravovat přímo. Toto oddělení zodpovědností usnadňuje komercializaci síťového krájení.

## Klíčové vlastnosti

- Poskytuje sekundární, na síťový řez specifickou autentizaci po primární autentizaci v 5G jádře
- Využívá externí AAA servery pro autorizační rozhodnutí řízená tenantem
- Podporuje protokol Extensible Authentication Protocol (EAP) pro flexibilní autentizační metody
- Umožňuje paralelní autentizační procedury pro více síťových řezů
- Umožňuje přísnou bezpečnostní izolaci mezi síťovými řezy s různou úrovní důvěry
- Umožňuje vlastnictví řezů podnikům a vertikálním odvětvím s nezávislou správou identit

## Související pojmy

- [NSSAAF – Network Slice-specific Authentication and Authorization Function](/mobilnisite/slovnik/nssaaf/)
- [NSSAI – Network Slice Selection Assistance Information](/mobilnisite/slovnik/nssai/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 28.204** (Rel-18) — Charging management
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.526** (Rel-19) — Nnssaaf Service Based Interface Stage 3
- **TS 29.571** (Rel-19) — Common Data Types for 5G Service Based Interfaces
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application
- **TR 31.826** (Rel-18) — Technical Report
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TR 32.847** (Rel-18) — Technical Report
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.700** — 3GPP TR 33.700

---

📖 **Anglický originál a plná specifikace:** [NSSAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssaa/)
