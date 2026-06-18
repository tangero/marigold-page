---
slug: "ck"
url: "/mobilnisite/slovnik/ck/"
type: "slovnik"
title: "CK – Confidentiality Key"
date: 2025-01-01
abbr: "CK"
fullName: "Confidentiality Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ck/"
summary: "Confidentiality Key (CK) je kryptografický klíč používaný v sítích 3GPP k šifrování uživatelských dat a signalizačních zpráv, čímž zajišťuje soukromí na rozhraní vzdušného přenosu. Je základní součást"
---

CK (Confidentiality Key) je kryptografický klíč generovaný během autentizace v sítích 3GPP za účelem šifrování uživatelských dat a signalizačních zpráv, který zajišťuje soukromí a zabraňuje odposlechu na rozhraní vzdušného přenosu.

## Popis

Confidentiality Key (CK) je základním prvkem bezpečnostní architektury 3GPP, konkrétně definovaným jako součást protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Jedná se o 128bitový kryptografický klíč odvozený během procesu vzájemné autentizace mezi uživatelským zařízením (UE) a autentizačním centrem (AuC) v rámci Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). K odvození se používá algoritmus Milenage nebo jiné standardizované algoritmy se vstupy zahrnujícími sdílený tajný klíč (K) uložený na [USIM](/mobilnisite/slovnik/usim/) a v AuC, náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)) generovanou sítí a další parametry. CK je generován současně s Integrity Key ([IK](/mobilnisite/slovnik/ik/)) a tvoří dvojici klíčů pro zabezpečení komunikace.

Po úspěšné autentizaci je CK doručen z HSS/AuC do obsluhujícího síťového uzlu – jako je [SGSN](/mobilnisite/slovnik/sgsn/) v UMTS nebo [MME](/mobilnisite/slovnik/mme/) v LTE/5G – prostřednictvím autentizačních vektorů. Obsluhující uzel následně poskytne CK příslušné entitě rádiového přístupového sítě (např. [RNC](/mobilnisite/slovnik/rnc/) v UMTS, eNB v LTE, gNB v 5G NR) pro použití v šifrovacích algoritmech. CK slouží jako vstup do algoritmu důvěrnosti (f8 v UMTS, 128-EEA v LTE, 128-NEA v 5G) k vytvoření šifrovacího proudu, který šifruje uživatelská data a určité signalizační zprávy na rozhraní vzdušného přenosu. Toto šifrování probíhá na vrstvě Packet Data Convergence Protocol (PDCP) v LTE a 5G a na vrstvách Radio Resource Control (RRC) a uživatelské roviny v UMTS.

Úloha CK je striktně omezena na ochranu důvěrnosti dat přenášených mezi UE a řadičem rádiové sítě/základnovou stanicí. Nikdy není použit pro ochranu integrity, což je samostatná funkce IK. Klíč je specifický pro konkrétní instanci autentizace a je obnovován s každým novým průběhem AKA, což zvyšuje bezpečnost omezením množství dat zašifrovaných pod jedním klíčem. V 5G se paradigma vyvinulo zavedením kotvícího klíče (K_AMF) a odvozováním samostatných šifrovacích klíčů (např. K_RRCenc, K_UPenc) pro různé oblasti ochrany, ale základní koncept klíče určeného pro důvěrnost zůstává. Síla CK a jeho správná správa jsou klíčové pro zmírnění hrozeb, jako je odposlech, analýza provozu a zachycení uživatelských dat.

## K čemu slouží

CK byl zaveden, aby řešil kritickou potřebu soukromí a důvěrnosti v digitálních celulárních komunikacích, což byla významná slabina dřívějších analogových systémů náchylných k odposlechu. Jeho vytvoření bylo motivováno závazkem 3GPP vybudovat robustní, standardizovanou bezpečnost přímo v síťové architektuře, počínaje UMTS (Release 99). Před 3G byly bezpečnostní mechanismy často slabší nebo volitelné. CK poskytuje povinný, algoritmicky silný mechanismus pro šifrování veškerého uživatelského provozu a citlivé signalizace, který zajišťuje, že komunikaci nemohou porozumět neoprávněné strany.

CK řeší problém zabezpečení dat na inherentně zranitelném rádiovém spoji. Tím, že je dynamicky generován z dlouhodobého tajemství a náhodné výzvy pro každou autentizaci, poskytuje dokonalé utajení do budoucna – prolomení jediného CK neodhalí klíče předchozích ani budoucích relací. Tento přístup řeší omezení statických nebo méně často měněných šifrovacích klíčů. Oddělení CK od Integrity Key (IK) také dodržuje princip kryptografického oddělení klíčů, což zvyšuje celkovou bezpečnost omezením dopadu potenciálního prolomení jednoho algoritmu. Jeho integrace do standardizovaného protokolu AKA zajišťuje interoperabilitu mezi různými síťovými zařízeními a výrobci UE, což je nezbytné pro bezpečnost globálních mobilních systémů.

## Klíčové vlastnosti

- 128bitový kryptografický klíč pro silné šifrování
- Dynamicky generován během každého postupu Authentication and Key Agreement (AKA)
- Použit jako vstup do standardizovaných algoritmů důvěrnosti (např. f8, 128-EEA, 128-NEA)
- Chrání uživatelská data a vybrané signalizační zprávy na rozhraní vzdušného přenosu
- Odvozen současně, ale odděleně od Integrity Key (IK) pro kryptografické oddělení
- Doručen od páteřní sítě (HSS/AuC) k obsluhující síti a rádiové přístupové síti pro šifrování

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [CK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ck/)
