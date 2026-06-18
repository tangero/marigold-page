---
slug: "b-tid"
url: "/mobilnisite/slovnik/b-tid/"
type: "slovnik"
title: "B-TID – Bootstrapping Transaction Identifier"
date: 2025-01-01
abbr: "B-TID"
fullName: "Bootstrapping Transaction Identifier"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/b-tid/"
summary: "B-TID je jedinečný identifikátor generovaný během procesu autentizace v architektuře GBA (Generic Bootstrapping Architecture). Slouží jako reference k relaci pro následnou aplikační bezpečnost a umožň"
---

B-TID je jedinečný identifikátor transakce generovaný během procesu GBA autentizace, který umožňuje zabezpečený přístup ke službám bez opakované plné autentizace.

## Popis

Bootstrapping Transaction Identifier (B-TID) je základní komponentou architektury [GAA](/mobilnisite/slovnik/gaa/) (Generic Authentication Architecture) specifikované ve standardech 3GPP. Generuje jej funkce [BSF](/mobilnisite/slovnik/bsf/) (Bootstrapping Server Function) během úvodního procedury autentizace a dohody klíčů mezi uživatelským zařízením (UE) a sítí. B-TID je konstruován pomocí specifického formátu: začíná pevnou předponou (typicky doménou BSF), za níž následuje hodnota [RAND](/mobilnisite/slovnik/rand/) (náhodná výzva použitá při autentizaci) zakódovaná v base64 a název serveru BSF. Tento strukturovaný formát zajišťuje globální jedinečnost a umožňuje jakékoli síťové entitě identifikovat konkrétní bootstrapping transakci.

Během procedury [GBA](/mobilnisite/slovnik/gba/), po úspěšné vzájemné autentizaci mezi UE a BSF pomocí protokolu [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement), BSF vygeneruje B-TID a asociuje jej s navázanými relacemi klíčů (konkrétně s klíčem Ks a odvozenými klíči). BSF poté vrátí B-TID uživatelskému zařízení spolu s informací o době platnosti klíče. UE si tento B-TID uloží lokálně spolu s odpovídajícími klíči. Následně, když UE potřebuje přistoupit k aplikační službě (jako je Multimedia Telephony Service nebo jiné [NAF](/mobilnisite/slovnik/naf/)), předloží tento B-TID poskytovateli služby namísto opětovné autentizace od začátku.

B-TID slouží jako bezpečná referenční značka, která umožňuje funkci NAF (Network Application Function) získat příslušný autentizační kontext z BSF. Když NAF obdrží od UE žádost o službu obsahující B-TID, kontaktuje BSF (pomocí rozhraní Zn) a poskytne mu B-TID. BSF ověří platnost B-TID, potvrdí, že relace je stále aktivní v rámci její doby platnosti, a poté poskytne NAF relevantní klíčový materiál (konkrétně odvozený klíč Ks_NAF) potřebný k navázání zabezpečeného kanálu s UE. Tento mechanismus odděluje náročný proces autentizace od přístupu k aplikaci, čímž zvyšuje efektivitu.

Z architektonického pohledu funguje B-TID v rámci třívrstvého modelu GBA: UE, BSF a NAF. Jeho primární rolí je udržovat propojení mezi těmito entitami bez vystavení citlivého klíčového materiálu přes vzdušné rozhraní nebo aplikačním serverům. Samotný B-TID není tajný, ale musí být přenášen zabezpečeně, aby se zabránilo útokům typu hijacking. V síťových nasazeních jsou B-TID spravovány funkcí BSF s odpovídající kontrolou doby platnosti a mechanismy pro odvolání, aby byla zachována bezpečnost. Návrh identifikátoru umožňuje škálovatelnost napříč více BSF a podporuje jak variantu GBA, tak GBA-U (GBA with Ubiquity).

## K čemu slouží

B-TID byl vytvořen, aby vyřešil základní problém opakované autentizace v mobilních sítích, kde uživatelé přistupují k více službám od různých poskytovatelů. Před zavedením [GBA](/mobilnisite/slovnik/gba/) a mechanismu B-TID mohla každá aplikační služba vyžadovat vlastní autentizační proceduru, což vedlo k redundantní signalizaci, zvýšené latenci a špatné uživatelské zkušenosti. Tradiční přístup také znamenal, že uživatelé museli spravovat více přihlašovacích údajů pro různé služby, což vytvářelo bezpečnostní zranitelnosti a problémy s použitelností.

Zavedení B-TID ve vydání Release 6 jako součásti [GAA](/mobilnisite/slovnik/gaa/) poskytlo standardizovaný způsob, jak využít silnou autentizaci již provedenou mobilní sítí (prostřednictvím USIM karet a protokolu AKA) pro zabezpečení na aplikační vrstvě. Vytvořením identifikátoru transakce, který odkazuje na navázaný bezpečnostní kontext, systém umožňuje možnosti jednotného přihlášení napříč různorodými službami. Tím se řeší problém autentizačních izolovaných systémů při zachování úrovně zabezpečení základní autentizace mobilní sítě.

Historicky byl vývoj B-TID motivován rostoucí potřebou zabezpečených mobilních služeb nad rámec základního hlasu a SMS. Když operátoři zaváděli služby jako Multimedia Messaging, Push-to-Talk a později aplikace založené na IMS, potřebovali efektivní způsob, jak rozšířit autentizaci z mobilní sítě na tyto služby s přidanou hodnotou. Mechanismus B-TID umožnil poskytovatelům služeb outsourcovat autentizaci na mobilního operátora, přičemž si zachovali kontrolu nad zabezpečením své aplikace. To vytvořilo nové obchodní modely a umožnilo zabezpečené služby třetích stran bez nutnosti, aby si uživatelé vytvářeli samostatné účty.

## Klíčové vlastnosti

- Jedinečný formát identifikátoru kombinující doménu BSF a zakódovanou hodnotu RAND
- Odkazuje na navázaný bezpečnostní kontext GBA mezi UE a BSF
- Umožňuje odvození klíčů pro více funkcí NAF (Network Application Function)
- Podporuje správu doby platnosti s explicitní kontrolou expirace
- Umožňuje jednotné přihlášení napříč různorodými mobilními službami
- Umožňuje zabezpečené získání kontextu prostřednictvím standardizovaného rozhraní Zn

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.110** (Rel-19) — UICC-Terminal Key Establishment
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 33.222** (Rel-19) — Secure HTTP Access in GAA
- **TS 33.223** (Rel-19) — GBA Push Function Specification
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.259** (Rel-19) — Key Establishment between UICC Hosting & Remote Device
- **TS 33.823** (Rel-12) — GBA Web Browser Integration Study
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [B-TID na 3GPP Explorer](https://3gpp-explorer.com/glossary/b-tid/)
