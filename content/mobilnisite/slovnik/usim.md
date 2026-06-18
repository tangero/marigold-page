---
slug: "usim"
url: "/mobilnisite/slovnik/usim/"
type: "slovnik"
title: "USIM – Universal Subscriber Identity Module"
date: 2026-01-01
abbr: "USIM"
fullName: "Universal Subscriber Identity Module"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/usim/"
summary: "Universal Subscriber Identity Module (USIM) je zabezpečená, proti manipulaci odolná aplikace čipové karty umístěná na UICC (Universal Integrated Circuit Card) v zařízeních 3GPP. Ukládá klíčová data úč"
---

USIM je bezpečná aplikace čipové karty na UICC, která ukládá data účastníka, provádí autentizaci v síti a poskytuje zabezpečené prostředí pro správu identity a přístup ke službám v systémech 3G, 4G a 5G.

## Popis

Universal Subscriber Identity Module (USIM) je základním kamenem zabezpečení účastníka a správy identity v sítích 3GPP počínaje UMTS (3G). Není to fyzická karta samotná (tou je UICC), ale specializovaná aplikace běžící na zabezpečeném mikroprocesoru UICC. Hlavní funkce USIM jsou bezpečné uložení jedinečné identity účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), autentizace účastníka vůči síti, generování sezení klíčů pro šifrování a ochranu integrity a správa dat souvisejících s účastníkem, jako je telefonní seznam a [SMS](/mobilnisite/slovnik/sms/).

Z architektonického hlediska USIM komunikuje s mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) prostřednictvím standardizovaného rozhraní ([ETSI](/mobilnisite/slovnik/etsi/)/3GPP TS 31.101). Když se zařízení zapne nebo vstoupí do nové síťové oblasti, ME vyžádá od USIM mezinárodní identifikaci mobilního účastníka (IMSI). Tato IMSI je odeslána do sítě k zahájení autentizační procedury. Autentizační centrum (AuC) sítě vygeneruje autentizační vektor obsahující náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)), očekávanou odpověď ([XRES](/mobilnisite/slovnik/xres/)), šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)) a integritní klíč ([IK](/mobilnisite/slovnik/ik/)). RAND je odeslán USIM.

USIM, pomocí tajného klíče (K) bezpečně uloženého uvnitř něj a kryptografického algoritmu (MILENAGE pro 3G/4G/5G), vypočítá odpověď (RES) a stejné CK a IK. ME odešle RES zpět do sítě k ověření. Pokud se RES shoduje s XRES, je autentizace úspěšná. CK a IK jsou poté použity zařízením a sítí k šifrování a ochraně integrity veškeré následné komunikace. Tento proces, známý jako Authentication and Key Agreement (AKA), zajišťuje, že pouze legitimní účastník se správnou USIM může přistupovat k síti a že komunikace je zabezpečená.

Kromě základní autentizace USIM poskytuje zabezpečenou úložnou oblast pro data účastníka, preference výběru sítě a aplikace poskytovatele služeb (jako OTA provisioning). V 5G se role USIM vyvíjí k podpoře protokolu 5G AKA a ukládání nových identifikátorů, jako je Subscription Concealed Identifier (SUCI) pro zvýšené soukromí. Funguje jako kořen důvěry, umožňující zabezpečené inicializace dalších služeb a slouží jako zabezpečený prvek pro aplikace mobilního obchodu a digitální identity.

## K čemu slouží

USIM bylo zavedeno s 3G UMTS, aby řešilo bezpečnostní slabiny 2G SIM (Subscriber Identity Module). 2G SIM používalo algoritmus COMP128, který měl známé zranitelnosti, a autentizace GSM byla jednostranná (síť autentizuje účastníka) se slabšími šifrovacími algoritmy. Přechod na 3G vyžadoval silnější mechanismus vzájemné autentizace a vylepšené kryptografické schopnosti k ochraně nových datových a multimediálních služeb.

Vytvoření USIM poskytlo standardizovanou, do budoucna připravenou platformu pro identitu účastníka. Oddělilo zabezpečenou aplikaci (USIM) od fyzické karty (UICC), což umožnilo koexistenci více aplikací (jako ISIM pro IMS). Tato modularita byla klíčová pro konvergenci služeb. Zabezpečené výkonové prostředí a úložiště USIM chrání dlouhodobý tajný klíč (K) před extrakcí, čímž vytváří neměnný kořen důvěry pro celý mobilní ekosystém.

Jeho pokračující vývoj je hnána potřebou silnějšího soukromí (např. SUCI v 5G k ochraně IMSI), podpory nových autentizačních rámců (EAP-AKA', 5G AKA) a umožnění nových případů užití, jako je identifikace síťového řezání a zabezpečené služby pro IoT. USIM řeší základní problém bezpečného a přenosného spojení identity účastníka s předplatným, což umožňuje globální roaming, zabezpečený přístup ke službám a důvěryhodné transakční schopnosti.

## Klíčové vlastnosti

- Zabezpečené uložení dlouhodobého klíče účastníka (K) a IMSI
- Provádění algoritmů Authentication and Key Agreement (AKA)
- Generování sezení šifrovacích (CK) a integritních klíčů (IK)
- Zabezpečené úložiště pro telefonní seznam, SMS a nastavení služeb
- Podpora Over-The-Air (OTA) provizioningu a správy
- Platforma pro hostování dalších zabezpečených aplikací (např. ISIM)

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [ISIM – IMS Subscriber Identity Module](/mobilnisite/slovnik/isim/)
- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- … a dalších 76 specifikací

---

📖 **Anglický originál a plná specifikace:** [USIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/usim/)
