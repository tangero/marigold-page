---
slug: "naf"
url: "/mobilnisite/slovnik/naf/"
type: "slovnik"
title: "NAF – Network Application Function"
date: 2025-01-01
abbr: "NAF"
fullName: "Network Application Function"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/naf/"
summary: "Network Application Function (NAF) je klíčovou součástí architektury Generic Authentication Architecture (GAA). Funguje jako aplikační server poskytovatele služeb, který využívá mechanismy ověřování a"
---

NAF je aplikační server poskytovatele služeb v architektuře Generic Authentication Architecture (GAA), který využívá mechanismy GAA k bezpečnému ověření uživatelů a navázání zabezpečených kanálů pro síťové služby.

## Popis

Network Application Function (NAF) funguje v rámci architektury definované standardy Generic Authentication Architecture ([GAA](/mobilnisite/slovnik/gaa/)). Jedná se o aplikačně specifický server, který vyžaduje ověření svých uživatelů (uživatelských zařízení - UE) a navázání sdílených relaních klíčů pro zabezpečení následné komunikace. NAF samotné ověřování neprovádí; namísto toho k tomuto účelu využívá funkci Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když se UE pokusí o přístup ke službě poskytované NAF, NAF přesměruje UE k BSF pro tzv. bootstrapping ověření.

Během bootstrapovací procedury se UE a BSF vzájemně ověří pomocí přihlašovacích údajů uložených v HSS (obvykle na základě protokolu Authentication and Key Agreement - [AKA](/mobilnisite/slovnik/aka/)). Po úspěšném ověření odvodí BSF a UE sdílený klíčový materiál, konkrétně Bootstrapping Transaction Identifier ([B-TID](/mobilnisite/slovnik/b-tid/)) a relaní klíč (Ks). BSF poskytne B-TID UE. UE následně znovu kontaktuje NAF a předloží tento B-TID.

NAF po přijetí B-TID dotazuje BSF (přes rozhraní Zn), aby získal odpovídající klíčový materiál (aplikačně specifický klíč Ks_NAF odvozený z Ks). To umožňuje NAF ověřit UE (nepřímo přes BSF) a sdílet Ks_NAF s UE, což jim umožní navázat zabezpečený kanál. Role NAF tedy spočívá v tom, že funguje jako tzv. relying party, která důvěřuje ověření provedenému BSF a používá odvozené klíče pro zabezpečení na aplikační vrstvě. Z architektonického hlediska je NAF odděleno od infrastruktury ověřování základní sítě, což umožňuje poskytovatelům služeb implementovat zabezpečené služby nezávisle.

Klíčové komponenty fungování NAF zahrnují jeho rozhraní: rozhraní Zn s BSF pro získání klíčů a aplikačně specifické rozhraní (často přes [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/) nebo jiné protokoly) s UE. NAF je definováno tak, aby podporovalo různé scénáře služeb, což z něj činí univerzální prvek pro zajištění bezpečnosti v sítích 3GPP. Jeho návrh umožňuje opakované využití robustní infrastruktury 3GPP AKA pro širokou škálu služeb, podporuje konzistenci zabezpečení a snižuje složitost implementace pro poskytovatele aplikací.

## K čemu slouží

NAF bylo zavedeno za účelem řešení problému poskytování standardizovaného a robustního ověřování a dohody o klíčích pro přidané služby a aplikace nad rámec základního síťového přístupu. Před architekturou [GAA](/mobilnisite/slovnik/gaa/) a konceptem NAF by každá aplikace nebo služba (jako MBMS, služby založené na poloze nebo správa zařízení) musela implementovat vlastní mechanismus ověřování, což vedlo k fragmentaci zabezpečení, zvýšené složitosti pro výrobce UE a potenciálním zranitelnostem z nestandardních přístupů.

Vytvoření NAF bylo motivováno potřebou obecného bezpečnostního rámce, který by mohly využívat jakékoli síťové aplikace. Architektura Generic Authentication Architecture (GAA), zavedená ve vydání 3GPP Release 6, tento rámec vytvořila. NAF slouží jako aplikační koncový bod v rámci GAA, což umožňuje poskytovatelům služeb outsourcovat složitý proces ověřování k prověřené infrastruktuře mobilního operátora (BSF/HSS). Toto oddělení odpovědností umožňuje inovace ve službách při zachování vysoké a konzistentní úrovně zabezpečení odvozené od mobilního předplatného.

Historicky to řešilo omezení, kdy bylo zabezpečení aplikací buď slabé (např. jednoduché uživatelské jméno/heslo), nebo vyžadovalo složitou, službě specifickou integraci se sítí operátora. Model NAF poskytuje škálovatelný a standardizovaný způsob, jak dosáhnout silného dvoufaktorového ověřování (něco, co máte – SIM/USIM, a něco, co znáte – PIN) pro množství služeb, a podporuje tak bezpečný ekosystém pro mobilní aplikace.

## Klíčové vlastnosti

- Funguje jako tzv. relying party v rámci architektury Generic Authentication Architecture (GAA)
- Využívá bootstrapovaný klíčový materiál (Ks_NAF) od BSF pro zabezpečení na aplikační vrstvě
- Komunikuje s funkcí Bootstrapping Server Function (BSF) přes standardizovaný referenční bod Zn
- Podporuje vzájemné ověření mezi uživatelským zařízením (UE) a aplikačním serverem
- Umožňuje zabezpečený přístup ke službám pro různé aplikace jako MBMS, GBA a ochrana integrity uživatelské roviny
- Odděluje zabezpečení aplikace od ověřování přístupu k základní síti, což umožňuje nezávislé nasazení služeb

## Definující specifikace

- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.423** (Rel-8) — PSTN/ISDN Simulation Services XCAP Protocol
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 29.309** (Rel-19) — Nbsp Service Based Interface for GBA BSF
- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TR 31.822** (Rel-18) — Technical Report on GBA_U based APIs
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.110** (Rel-19) — UICC-Terminal Key Establishment
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.185** (Rel-19) — V2X Security in LTE
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [NAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/naf/)
