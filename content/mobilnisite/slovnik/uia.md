---
slug: "uia"
url: "/mobilnisite/slovnik/uia/"
type: "slovnik"
title: "UIA – User Identity Authentication"
date: 2026-01-01
abbr: "UIA"
fullName: "User Identity Authentication"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/uia/"
summary: "User Identity Authentication (UIA) je základní bezpečnostní proces v sítích 3GPP, který ověřuje identitu uživatele (nebo User Equipment) pokoušejícího se o přístup k síťovým službám. Chrání před neopr"
---

UIA je bezpečnostní proces 3GPP, který ověřuje identitu uživatele pro přístup k síti validací přihlašovacích údajů prostřednictvím výzva-odpověď mechanismu mezi SIM/USIM a Autentizačním centrem (AuC).

## Popis

User Identity Authentication (UIA) je klíčový postup definovaný 3GPP, který zajišťuje, že uživatel nebo zařízení jsou tím, za koho se vydávají, ještě před udělením přístupu ke službám mobilní sítě. Je primární funkcí protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Architektura zahrnuje několik klíčových síťových funkcí: User Equipment (UE) obsahující [SIM](/mobilnisite/slovnik/sim/) nebo [USIM](/mobilnisite/slovnik/usim/), obsluhující síť (např. [VLR](/mobilnisite/slovnik/vlr/)/[SGSN](/mobilnisite/slovnik/sgsn/)/[MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/)) a Autentizační centrum (AuC) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) domovské sítě. Proces začíná, když obsluhující síť vyžádá autentizační vektory od HSS/AuC. AuC tyto vektory generuje pomocí tajného klíče (K) jedinečného pro identitu účastníka (IMSI) a pořadového čísla (SQN). Každý vektor obsahuje náhodnou výzvu (RAND), očekávanou odpověď (XRES), šifrovací klíč (CK), integritní klíč (IK) a autentizační token (AUTN). Obsluhující síť odešle RAND a AUTN do UE. USIM v UE, který disponuje stejným tajným klíčem (K), zpracuje AUTN, aby ověřil, že pochází z legitimní sítě (autentizace sítě vůči uživateli), a zkontroluje aktuálnost SQN, aby zabránil replay útokům. Následně vypočte odpověď (RES) pomocí RAND a K. UE odešle RES zpět obsluhující síti, která jej porovná s XRES. Shoda autentizuje uživatele. Úspěšná UIA také vede k odvození stejného CK a IK jak v UE, tak v síti, což umožňuje následné šifrování a integritní ochranu komunikace. Tato vzájemná autentizace (síť autentizuje uživatele, uživatel autentizuje síť) je klíčovou bezpečnostní funkcí.

## K čemu slouží

UIA existuje za účelem zajištění bezpečného a důvěryhodného přístupu k prostředkům mobilní sítě a řeší základní bezpečnostní problém zneužití identity a neoprávněného použití. Před standardizovanou autentizací měly rané mobilní systémy slabou nebo žádnou autentizaci, což je činilo zranitelnými vůči klonování a podvodům. Motivací pro vývoj robustní UIA v GSM (a jejího vývoje přes 3G, 4G a 5G) byla ochrana síťových operátorů před ztrátou příjmů z důvodu podvodů a ochrana soukromí uživatelů a integrity služeb. Řeší omezení jednoduchých systémů založených na hesle použitím sdíleného tajemství uloženého v modulu odolném proti manipulaci (SIM) a kryptografických výzva-odpověď mechanismů, které nikdy nepřenášejí tajný klíč vzduchem. Vytvoření protokolu AKA s UIA v jeho jádru bylo hnáno potřebou škálovatelné, efektivní autentizační metody vhodné pro miliony zařízení, schopné podporovat roaming mezi různými síťovými operátory a poskytující základ pro generování sezení klíčů pro důvěrnost a integritu. Její kontinuální vývoj napříč releasy řeší nově vznikající hrozby, zlepšuje délky klíčů a algoritmy a přizpůsobuje se novým síťovým architekturám (např. EPS AKA v LTE, 5G AKA v 5G SA) při zachování zpětné kompatibility a globální interoperability.

## Klíčové vlastnosti

- Vzájemná autentizace mezi uživatelem a sítí
- Založeno na sdíleném tajném klíči (K) uloženém v USIM a AuC
- Používá mechanismus výzva-odpověď (RAND, RES/XRES)
- Generuje šifrovací klíč (CK) a integritní klíč (IK) pro zabezpečení relace
- Obsahuje pořadové číslo (SQN) pro prevenci replay útoků
- Základ pro protokol 3GPP Authentication and Key Agreement (AKA)

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.700** — 3GPP TR 33.700
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [UIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/uia/)
