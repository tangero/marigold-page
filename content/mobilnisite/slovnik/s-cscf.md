---
slug: "s-cscf"
url: "/mobilnisite/slovnik/s-cscf/"
type: "slovnik"
title: "S-CSCF – Serving Call Session Control Function"
date: 2026-01-01
abbr: "S-CSCF"
fullName: "Serving Call Session Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/s-cscf/"
summary: "S-CSCF je centrální uzel jádra IMS, odpovědný za řízení relací a poskytování služeb. Autentizuje uživatele, zpracovává signalizaci SIP, vynucuje politiky a komunikuje s aplikačními servery, aby umožni"
---

S-CSCF je centrální uzel jádra IMS, který autentizuje uživatele, zpracovává signalizaci SIP pro řízení relací a umožňuje multimediální služby interakcí s aplikačními servery.

## Popis

Serving Call Session Control Function (S-CSCF) je centrální procesní uzel v architektuře IP Multimedia Subsystem (IMS). Funguje jako [SIP](/mobilnisite/slovnik/sip/) registrátor a SIP proxy server a zpracovává veškeré řízení relací pro uživatele registrované v IMS v rámci své přiřazené domovské sítě. Při registraci uživatele S-CSCF stáhne jeho služební profil ze serveru Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a tyto informace použije k aplikaci služební logiky, spouštění aplikačních serverů a správě služebních relací uživatele. Je odpovědný za směrování SIP zpráv, komunikaci s dalšími [CSCF](/mobilnisite/slovnik/cscf/) ([P-CSCF](/mobilnisite/slovnik/p-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/)) a vynucování politik operátora sítě.

Architektonicky je S-CSCF stavový SIP server, který udržuje stav registrace a stav relací pro své přiřazené uživatele. Provádí procedury navazování, modifikace a ukončování relací. Klíčovou součástí jeho fungování jsou Initial Filter Criteria (iFC), které jsou součástí služebního profilu uživatele. iFC obsahuje sadu pravidel, která určují, kdy a na které aplikační servery ([AS](/mobilnisite/slovnik/as/)) mají být SIP zprávy přesměrovány pro provedení nadstandardních služeb, jako je přesměrování hovorů, hlasová schránka nebo služby přítomnosti.

Jeho role přesahuje základní směrování SIP; je klíčový pro zabezpečení, provádí autentizaci a autorizaci uživatelů ve spolupráci s HSS. Také zajišťuje funkce účtování generováním záznamů o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) a rozhraní s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) pro řízení politik souvisejících s přenosovými prostředky. S-CSCF je kritický prvek pro umožnění pokročilých komunikačních služeb, zajištění interoperability a poskytnutí platformy pro inovace služeb v sítích 4G, 5G a pevných sítích.

## K čemu slouží

S-CSCF byl vytvořen, aby poskytl standardizované, SIP-based jádro pro poskytování multimediálních služeb přes IP sítě, nezávisle na podkladové přístupové technologii (např. LTE, 5G NR, Wi-Fi). Před IMS byly telekomunikační služby pevně svázány s okruhově spínanými sítěmi, což činilo inovace služeb pomalými a závislými na přístupu. S-CSCF tento problém řeší centralizací řízení relací, oddělením služební vrstvy od přenosové vrstvy a umožněním konvergence hlasu, videa a zpráv přes IP.

Jeho vytvoření bylo motivováno potřebou flexibilní, škálovatelné architektury pro podporu vize 'all-IP' sítí. Řeší omezení předchozích izolovaných služebních platforem tím, že poskytuje společný engine pro poskytování služeb. To umožňuje operátorům efektivně nasazovat služby jako Voice over LTE (VoLTE), Rich Communication Services (RCS) a nakonec Voice over New Radio (VoNR) pomocí jediného jádra sítě, které může obsluhovat více typů přístupu a usnadňovat interoperabilitu mezi sítěmi různých operátorů.

## Klíčové vlastnosti

- Funguje jako SIP registrátor a stavový proxy server pro uživatele IMS
- Stahuje a provádí služební profily uživatelů z HSS
- Zpracovává Initial Filter Criteria (iFC) pro spouštění aplikačních serverů
- Provádí autentizaci a autorizaci uživatelů
- Komunikuje s PCRF pro řízení politik a účtování
- Generuje záznamy o účtovacích datech (CDR) pro fakturaci

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- … a dalších 46 specifikací

---

📖 **Anglický originál a plná specifikace:** [S-CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-cscf/)
