---
slug: "ik"
url: "/mobilnisite/slovnik/ik/"
type: "slovnik"
title: "IK – Integrity Key"
date: 2025-01-01
abbr: "IK"
fullName: "Integrity Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ik/"
summary: "Integrity Key (IK) je kryptografický klíč používaný v systémech 3GPP k ověření integrity a autenticity signalizačních zpráv a uživatelských dat. Je generován během procedur autentizace a dohody klíčů"
---

IK je kryptografický klíč používaný v systémech 3GPP k ověření integrity a autenticity signalizačních zpráv a uživatelských dat, čímž brání jejich neoprávněné modifikaci a opakovanému přehrání (replay attacks).

## Popis

Integrity Key (IK) je základní bezpečnostní prvek v rámci frameworku autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)) 3GPP. Jedná se o 128bitový kryptografický klíč odvozený společně s šifrovacím klíčem ([CK](/mobilnisite/slovnik/ck/)) z dlouhodobého tajného klíče (K), který je sdílen mezi modulkem USIM a autentizačním centrem (AuC) v domovské síti. K odvození dochází během procedury AKA, což může být UMTS AKA, EPS AKA nebo 5G AKA. IK je generován konkrétně za účelem poskytnutí ochrany integrity pro signalizační zprávy vyměňované mezi uživatelským zařízením (UE) a sítí a v některých případech i pro data uživatelské roviny.

IK je použit jako vstup do integritních algoritmů (např. algoritmy UIA v UMTS, [EIA](/mobilnisite/slovnik/eia/) v LTE, [NIA](/mobilnisite/slovnik/nia/) v 5G NR). Tyto algoritmy, jako jsou 128-EIA1 (SNOW 3G), 128-EIA2 ([AES](/mobilnisite/slovnik/aes/)) a 128-EIA3 (ZUC), generují pro každou integritně chráněnou protokolovou datovou jednotku (PDU) kód autentizace zprávy ([MAC](/mobilnisite/slovnik/mac/)). Příjemní entita (UE nebo síťový uzel) přepočítá MAC pomocí stejného IK a algoritmu. Pokud se vypočtený MAC shoduje s přijatým MAC, je integrita a autenticita zprávy ověřena, což potvrzuje, že nebyla během přenosu pozměněna a že pochází od legitimního protistrany. IK je typicky uložen v nevolatilní paměti UE a v příslušných síťových uzlech (např. [MME](/mobilnisite/slovnik/mme/) v LTE, [AMF](/mobilnisite/slovnik/amf/) v 5GC) po dobu trvání bezpečnostního kontextu.

V celkové bezpečnostní architektuře IK spolupracuje s CK. Zatímco CK je používán pro důvěrnost (šifrování), IK je vyhrazen pro integritu a autentizaci původu dat. Oddělení funkcí mezi CK a IK je klíčovým bezpečnostním principem, který omezuje dopad potenciálního kompromitování jednoho z klíčů. IK je také používán při odvozování dalších klíčů v rámci hierarchie klíčů, jako je Kenb v LTE nebo KgNB v 5G, které slouží pro ochranu integrity na následných síťových rozhraních (např. mezi eNB a UE). Síla ochrany integrity přímo závisí na utajení IK a na kryptografické odolnosti zvoleného integritního algoritmu.

## K čemu slouží

Integrity Key existuje k řešení kritických bezpečnostních hrozeb v bezdrátové komunikaci, konkrétně modifikace zpráv, jejich vkládání a opakovaného přehrání (replay attacks). Bez ochrany integrity by útočník mohl pozměnit signalizační zprávy (např. příkazy k předání spojení, zprávy správy relace), aby narušil službu, přesměroval provoz nebo se vydával za síť či uživatele. Před standardizovaným použitím IK v systémech 3GPP (od GSM dále) byly bezpečnostní mechanismy slabší; GSM například poskytovalo pouze volitelnou a slabší šifrování pro důvěrnost a nemělo standardizovanou ochranu integrity pro signalizaci, což je činilo zranitelnými vůči některým aktivním útokům.

Vytvoření IK bylo motivováno potřebou silnějšího, povinného bezpečnostního frameworku pro 3G (UMTS) a následné generace. Bezpečnostní skupina 3GPP navrhla nový robustní protokol AKA, který explicitně oddělil funkce integrity a důvěrnosti. To byla přímá reakce na omezení bezpečnosti GSM a vyvíjející se hrozby. IK poskytuje jistotu, že kritická signalizace řídicí roviny nebyla pozměněna, což je základní pro řízení přístupu k síti, správu mobility a správu relací. Jeho odvození z dlouhodobého tajemství prostřednictvím bezpečné jednosměrné funkce zajišťuje, že je pro každou relaci čerstvý a kryptograficky svázaný s identitou účastníka, čímž řeší problém zajištění autenticity zpráv v nedůvěryhodném rádiovém prostředí.

## Klíčové vlastnosti

- 128bitový kryptografický klíč odvozený během procedury AKA
- Používán výhradně pro ochranu integrity a autentizaci původu dat
- Vstup do standardizovaných integritních algoritmů (UIA/EIA/NIA) pro generování MAC
- Uložen lokálně v UE a síťových uzlech po dobu trvání bezpečnostního kontextu
- Oddělen od šifrovacího klíče (CK) za účelem omezení dopadu kompromitace klíče
- Použit jako kořen pro odvozování dalších klíčů v hierarchii klíčů přístupové vrstvy

## Související pojmy

- [CK – Confidentiality Key](/mobilnisite/slovnik/ck/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 33.401** (Rel-19) — EPS Security Architecture
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [IK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ik/)
