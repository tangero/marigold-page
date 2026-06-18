---
slug: "sim"
url: "/mobilnisite/slovnik/sim/"
type: "slovnik"
title: "SIM – Subscriber Identity Module / Universal Subscriber Identity Module"
date: 2026-01-01
abbr: "SIM"
fullName: "Subscriber Identity Module / Universal Subscriber Identity Module"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sim/"
summary: "Zabezpečený hardwarový nebo softwarový modul, který uchovává identitu účastníka, autentizační klíče a profily služeb. Umožňuje zabezpečený přístup k síti, autentizaci uživatele a personalizaci služeb"
---

SIM je zabezpečený hardwarový nebo softwarový modul, který uchovává identitu účastníka a autentizační klíče, čímž umožňuje zabezpečený přístup k síti a personalizaci služeb pro mobilní zařízení.

## Popis

Modul účastnické identity (SIM) a jeho evoluce do podoby univerzálního modulu účastnické identity ([USIM](/mobilnisite/slovnik/usim/)) je odolnou hardwarovou součástkou, tradičně v podobě čipové karty ([ICC](/mobilnisite/slovnik/icc/)), nebo softwarovou implementací (eSIM, iSIM). Slouží jako zabezpečený kotvící bod pro účastníka v mobilní síti. Modul obsahuje mikroprocesor a trvalou paměť, která uchovává kritická data včetně mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), jedinečného identifikátoru čipové karty ([ICCID](/mobilnisite/slovnik/iccid/)), souboru autentizačních klíčů (Ki pro GSM, K pro UMTS/5G) a bezpečnostních algoritmů. Uchovává také informace související s účastníkem, jako je telefonní seznam, [SMS](/mobilnisite/slovnik/sms/) zprávy a preference výběru sítě.

Z architektonického hlediska SIM/USIM funguje jako nezávislý zabezpečený prvek uvnitř uživatelského zařízení (UE), které komunikuje s mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) prostřednictvím standardizovaných elektrických a logických rozhraní. Jeho primární rolí je provádět protokol autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) se sítí. Když se UE pokouší připojit k síti, autentizační centrum (AuC) sítě vygeneruje autentizační vektor obsahující náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)), očekávanou odpověď (XRES), šifrovací klíč (CK) a integritní klíč (IK). Tento vektor je odeslán do obslužného síťového uzlu (např. VLR, SGSN, MME, AMF). Síť pošle RAND do UE, které jej předá SIM/USIM. SIM/USIM použije svůj uložený tajný klíč (Ki/K) a přijatý RAND k lokálnímu výpočtu odpovědi (SRES pro GSM, RES pro UMTS/5G) a sezení klíčů (CK, IK). UE odešle vypočítaný RES zpět do sítě k ověření. Shoda autentizuje účastníka a naváže zabezpečenou, šifrovanou komunikaci.

Evoluce ze SIM na USIM představovala významné posílení zabezpečení. Klasický SIM používal pro GSM AKA algoritmus COMP128, který měl známé zranitelnosti. USIM, zavedený pro 3G, podporuje robustnější sadu algoritmů Milenage pro UMTS a později pro 5G AKA. Poskytuje vzájemnou autentizaci (síť autentizuje uživatele a uživatel autentizuje síť), silnější odvozování klíčů a povinnou integritní ochranu signalizace. USIM také spravuje více profilů operátorů a umožňuje zabezpečené služby nad rámec základního přístupu, jako je GBA (Generic Bootstrapping Architecture) pro autentizaci aplikací. V 5G je USIM klíčový pro podporu vylepšeného 5G AKA a primárního autentizačního procesu mezi UE a funkcí autentizačního serveru (AUSF), sloužící jako kotva pro trvalý identifikátor účastníka (SUPI).

## K čemu slouží

SIM byl vytvořen k řešení základního problému zabezpečené identifikace a autentizace účastníka v mobilní síti, oddělením identity účastníka od fyzického telefonního přístroje. Před jeho zavedením byla identita účastníka vázána na mobilní zařízení, což ztěžovalo výměnu přístrojů a představovalo významná bezpečnostní rizika a rizika podvodů. SIM modularizoval identitu, přihlašovací údaje a osobní data účastníka na přenosný, zabezpečený token. To umožnilo globální roaming, protože účastník mohl vložit svůj SIM do jakéhokoli kompatibilního přístroje a okamžitě získat přístup ke svým předplaceným službám a osobním datům.

Primární motivací bylo vytvoření robustního bezpečnostního základu. Ukládáním autentizačních klíčů v odolném prostředí a prováděním kryptografických výpočtů interně SIM zabraňuje extrakci a klonování klíčů, čímž zmírňuje podvody jako podvodné využívání služeb a odposlech. Poskytuje důvěryhodné prostředí pro provádění protokolu AKA. K evoluci na USIM vedla potřeba silnějších kryptografických algoritmů a vzájemné autentizace k řešení bezpečnostních slabin v sítích 2G GSM, kde byl autentizován pouze uživatel vůči síti. 3G a následující generace vyžadovaly ochranu proti útokům falešných základnových stanic, čemuž schopnost USIM autentizovat síť napomáhá.

Kromě toho se platforma SIM/USIM vyvinula v aktivátora služeb. Její schopnosti zabezpečeného úložiště a zpracování byly využity pro služby s přidanou hodnotou, jako jsou zabezpečené platební aplikace (prostřednictvím SIM Toolkit nebo Java Card), zabezpečené úložiště pro řidičské průkazy nebo digitální klíče (v profilech eSIM) a jako kořen důvěry pro síťové aplikace. Řeší problém správy zabezpečených přihlašovacích údajů v ekosystému více operátorů, více služeb a více zařízení a tvoří základ důvěryhodné mobilní identity.

## Klíčové vlastnosti

- Zabezpečené uložení dlouhodobé identity účastníka (IMSI/SUPI) a tajného autentizačního klíče (Ki/K)
- Provádění protokolů autentizace a dohody o klíči (AKA) (GSM AKA, UMTS AKA, 5G AKA)
- Generování sezení bezpečnostních klíčů (CK, IK) pro šifrování a integritní ochranu
- Odolný hardwarový design (nebo ekvivalentní zabezpečené softwarové prostředí pro eSIM)
- Uchovávání dat účastníka (telefonní seznam, SMS, nastavení služeb) a více profilů operátorů
- Podpora služeb s přidanou hodnotou prostřednictvím SIM Application Toolkit (SAT) a platformy Java Card

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

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
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- … a dalších 34 specifikací

---

📖 **Anglický originál a plná specifikace:** [SIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sim/)
