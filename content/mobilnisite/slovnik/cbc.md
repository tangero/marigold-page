---
slug: "cbc"
url: "/mobilnisite/slovnik/cbc/"
type: "slovnik"
title: "CBC – Cipher Block Chaining (Mode)"
date: 2026-01-01
abbr: "CBC"
fullName: "Cipher Block Chaining (Mode)"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbc/"
summary: "Cipher Block Chaining (CBC) je symetrický šifrovací režim, který řetězí bloky otevřeného textu pomocí operací XOR s předchozími šifrovými bloky před zašifrováním. Tím zajišťuje, že stejné bloky otevře"
---

CBC je symetrický šifrovací režim, který řetězí bloky otevřeného textu pomocí operace XOR s předchozími šifrovými bloky, aby zajistil, že stejné bloky otevřeného textu vytvoří různé šifrové bloky, a tím poskytuje důvěrnost v sítích 3GPP.

## Popis

Cipher Block Chaining (CBC) je režim provozu blokové šifry standardizovaný v rámci 3GPP pro zabezpečení dat uživatelské roviny a signalizace řídicí roviny. Funguje tak, že zprávu v otevřeném textu rozdělí na bloky pevné velikosti (typicky 128 bitů pro [AES](/mobilnisite/slovnik/aes/)). Před zašifrováním je každý blok otevřeného textu podroben operaci XOR se šifrovým textem předchozího bloku. První blok je podroben operaci XOR s inicializačním vektorem ([IV](/mobilnisite/slovnik/iv/)). Tento řetězící mechanismus zavádí závislost mezi bloky, čímž zajišťuje, že stejné sekvence otevřeného textu vedou ke zcela odlišným šifrovým výstupům, a tím odolává útokům analýzou vzorů.

Proces šifrování CBC probíhá v této posloupnosti: Pro první blok (i=1) platí C₁ = Eₖ(P₁ ⊕ IV), kde Eₖ je šifrovací funkce s klíčem K, P₁ je první blok otevřeného textu, IV je inicializační vektor a C₁ je výsledný šifrový blok. Pro následující bloky (i>1) platí Cᵢ = Eₖ(Pᵢ ⊕ Cᵢ₋₁). Dešifrování tento proces obrací: P₁ = Dₖ(C₁) ⊕ IV a Pᵢ = Dₖ(Cᵢ) ⊕ Cᵢ₋₁ pro i>1, kde Dₖ je dešifrovací funkce. Tato struktura znamená, že chyba jednoho bitu v šifrovém bloku Cᵢ znehodnotí dešifrování jak bloku Pᵢ (úplně poškozen), tak bloku Pᵢ₊₁ (chyba jednoho bitu na stejné pozici), ale následující bloky se po průchodu chyby dešifrují správně.

V architekturách 3GPP je režim CBC implementován v kryptografických algoritmech mechanismů ochrany důvěrnosti. Například v LTE a 5G používají algoritmy 128-EEA1 a 128-NEA1 šifru SNOW 3G v určitém režimu proudové šifry, ale základní principy řetězení pro integritu jsou koncepčně příbuzné. Historicky v UMTS používal šifrovací algoritmus f8 pro UTRAN šifru KASUMI v určitém režimu s výstupní zpětnou vazbou. Ačkoli se nejedná o čistý CBC, tyto 3GPP-specifické režimy sdílejí kryptografickou filozofii návrhu využívající zpětnou vazbu k zabránění výskytu vzorů z otevřeného textu v šifrovém textu. Skutečná implementace v 3GPP často používá upravený přístup optimalizovaný pro rádiové rozhraní, jako je generování šifrovacího proudu, který je XORován s otevřeným textem, přičemž samotný šifrovací proud je generován pomocí řetězícího mechanismu závislého na parametru COUNT (parametr aktuálnosti), identitě BEARER, bitu DIRECTION a parametru délky.

Role řetězení podobného CBC v síti je klíčová pro zabezpečení [AS](/mobilnisite/slovnik/as/) (Access Stratum) a [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum). Ve vrstvě PDCP (Packet Data Convergence Protocol) šifrovací funkce přijímá tyto vstupy (KEY, COUNT, BEARER, DIRECTION, LENGTH) k inicializaci šifrovacího algoritmu (jako AES v režimu [CTR](/mobilnisite/slovnik/ctr/) pro 128-EEA2 nebo ZUC pro 128-EEA3). Zatímco se technicky jedná o režimy proudových šifer nebo čítačové režimy, požadavek na kryptografickou synchronizaci a použití stavu (COUNT), který se mění podle paketu, slouží podobnému účelu ochrany proti opětovnému přehrání a zastření vzorů jako IV v CBC. Hlavní poskytovanou bezpečnostní vlastností je důvěrnost, která zajišťuje, že odposlouchávači na rádiovém rozhraní nemohou dešifrovat data uživatele nebo signalizační zprávy.

## K čemu slouží

Režim CBC byl zaveden, aby řešil kritickou zranitelnost režimu Electronic Codebook ([ECB](/mobilnisite/slovnik/ecb/)), ve kterém stejné bloky otevřeného textu vytvářejí stejné šifrové bloky. Tato vada umožňuje útočníkům rozpoznávat vzory, odvozovat informace a potenciálně provádět útoky opětovným přehráním. V telekomunikacích, kde signalizační zprávy a datové pakety uživatelů často obsahují opakující se struktury (hlavičky, odsazení protokolu, běžné příkazy), by režim ECB prozradil významné informace o provozu, čímž by byla ohrožena soukromí uživatelů a bezpečnost sítě.

Zavedení řetězících režimů jako CBC bylo motivováno potřebou robustní důvěrnosti v digitálních celulárních systémech počínaje 3G (UMTS). Jak se mobilní sítě vyvíjely od primárně hlasových (2G GSM, které používalo proudové šifry A5) k paketově přepínaným datovým službám, rozšířil se model hrozeb. Deterministická povaha ECB byla zcela nevhodná pro ochranu IP paketů, SMS dat nebo citlivé signalizace, jako jsou ověřovací výměny. CBC poskytuje sémantickou bezpečnost při útocích s volbou otevřeného textu (IND-CPA), když je použit s bezpečnou blokovou šifrou a náhodným, nepředvídatelným [IV](/mobilnisite/slovnik/iv/) pro každou šifrovací relaci.

V kontextu 3GPP, přestože konkrétní algoritmy (KASUMI, [AES](/mobilnisite/slovnik/aes/), SNOW 3G, ZUC) z výkonnostních důvodů nemusí pracovat v kanonickém režimu CBC (CBC není paralelizovatelný a vyžaduje sekvenční zpracování), jsou kryptografické principy návrhu zapracovány. Specifikace 3GPP definují šifrovací algoritmy důvěrnosti (rodina f8 pro UMTS, rodina 128-EEA pro LTE/5G), které používají základní šifry v režimech zajišťujících, že šifrový text je nedeterministickou funkcí otevřeného textu, klíče a časově proměnného vstupu (COUNT, IV). To přímo řeší omezení předchozích slabších šifrovacích schémat a je zásadní pro splnění přísných požadavků na důvěrnost moderních standardů mobilního broadbandu.

## Klíčové vlastnosti

- Řetězící mechanismus provádí XOR otevřeného textu s předchozím šifrovým blokem před zašifrováním
- Používá inicializační vektor (IV) k náhodnosti zašifrování prvního bloku
- Poskytuje sémantickou bezpečnost: stejné otevřené texty vytvářejí různé šifrové texty
- Šíření chyby je omezeno na dva bloky (poškozený blok a následující)
- Operuje na blocích pevné velikosti (např. 128bitových pro AES)
- Tvoří koncepční základ pro principy návrhu šifrovacích algoritmů 3GPP

## Související pojmy

- [AES – Advanced Encryption Standard](/mobilnisite/slovnik/aes/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.419** (Rel-19) — Service Area Broadcast Protocol (SABP)
- **TS 25.703** (Rel-12) — HNB Emergency Warning Area Study for UTRA
- **TR 26.944** (Rel-19) — QoE, ESQoS and SQoS metrics for 3G multimedia services
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.168** (Rel-19) — SBc-AP Protocol Specification
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [CBC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbc/)
