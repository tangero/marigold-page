---
slug: "aka"
url: "/mobilnisite/slovnik/aka/"
type: "slovnik"
title: "AKA – Authentication and Key Agreement"
date: 2026-01-01
abbr: "AKA"
fullName: "Authentication and Key Agreement"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/aka/"
summary: "AKA je základní bezpečnostní protokol používaný v sítích 3GPP pro vzájemné ověření mezi zařízením uživatele (UE) a sítí a pro navázání relacích klíčů. Zajišťuje, že k síti mají přístup pouze autorizov"
---

AKA je základní bezpečnostní protokol 3GPP pro vzájemné ověření mezi zařízením uživatele a sítí a pro navázání relacích klíčů pro šifrování a ochranu komunikace.

## Popis

Protokol Authentication and Key Agreement (AKA) je mechanismus typu challenge-response, který poskytuje vzájemné ověření a odvození kryptografických klíčů v sítích 3GPP. Funguje mezi uživatelským zařízením (UE) a ověřovacím centrem sítě (AuC), které sídlí v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v 4G/5G nebo v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) v 3G. Jádrem AKA je sdílený tajný klíč (K), který je bezpečně uložen jak v univerzální SIM kartě (USIM) v UE, tak v AuC. Tento dlouhodobý klíč se nikdy nepřenáší vzduchem.

Vykonání protokolu začíná, když obsluhovaná síť požádá o ověřovací vektory od HSS/AuC. AuC vygeneruje jeden nebo více ověřovacích vektorů pomocí klíče účastníka K a čísla sekvence (SQN). Každý vektor obsahuje náhodnou výzvu (RAND), očekávanou odpověď (XRES), šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)), integritní klíč ([IK](/mobilnisite/slovnik/ik/)) a ověřovací token ([AUTN](/mobilnisite/slovnik/autn/)). Samotný AUTN obsahuje SQN a kód pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)), což umožňuje UE ověřit pravost sítě. Obsluhovaná síť (např. prostřednictvím [MME](/mobilnisite/slovnik/mme/) v 4G nebo [AMF](/mobilnisite/slovnik/amf/) v 5G) odešle UE RAND a AUTN.

Po přijetí USIM v UE použije svůj uložený klíč K a přijatý RAND k výpočtu vlastní verze očekávané odpovědi (RES), šifrovacího klíče (CK), integritního klíče (IK) a MAC. Nejprve ověří AUTN kontrolou MAC, aby se ujistila, že výzva pochází ze skutečné sítě, a kontrolou SQN, aby zajistila, že je aktuální a nejde o opakování starého ověření. Pokud je úspěšné, UE odešle RES zpět do sítě. Síť porovná přijatý RES s XRES; shoda dokončí vzájemné ověření. Odvozené CK a IK pak používají UE a přístupová vrstva sítě k zajištění důvěrnosti a ochrany integrity veškerého následujícího signalizačního a uživatelského datového provozu.

Konstrukce AKA je robustní a poskytuje oddělení klíčů – pro různé účely (šifrování, integrita) a různé síťové domény (přístupová vrstva, nepřístupová vrstva) se odvozují různé klíče. Podporuje také synchronizační mechanismy pro případy, kdy se čísla sekvence v UE a AuC rozcházejí. V 5G bylo AKA vylepšeno na 5G AKA, které zahrnuje lepší řízení domovskou sítí, odvození kotvícího klíče (KAUSF) pro lepší hierarchii klíčů a zahrnutí názvu obsluhované sítě do odvozování klíčů, aby byly klíče vázány na konkrétní síť, což zmírňuje některé vektory útoků. Vykonání protokolu je pro uživatele transparentní, ale je spuštěno při počátečním připojení k síti, při přechodech mezi různými typy jádra sítě nebo periodicky pro přeověření.

## K čemu slouží

AKA bylo vytvořeno za účelem řešení kritických bezpečnostních nedostatků předchozích buněčných systémů, zejména slabého a jednostranného ověřování v GSM. V GSM pouze síť ověřovala uživatele, což ji činilo zranitelnou vůči útokům falešných základnových stanic (IMSI catchers). Navíc se ukázalo, že šifrovací algoritmy a délky klíčů v GSM jsou kryptograficky slabé. Primárním účelem AKA, zavedeného s 3G (UMTS), bylo navázání silného, vzájemného ověření a generování robustních, relaci specifických kryptografických klíčů pro zajištění důvěrnosti i integrity komunikace.

Protokol řeší problém bezpečného navázání důvěryhodné relace v nepřátelském rádiovém prostředí. Zajišťuje, že se uživatel připojuje k legitimní, autorizované síti a ne k podvodnému napodobiteli, a zároveň dokazuje síti, že je uživatel platným účastníkem. Tato vzájemná důvěra je základním předpokladem pro všechny ostatní bezpečnostní služby. Odvozováním nových, efemérních šifrovacích a integritních klíčů (CK/IK) z dlouhodobého tajemství pro každou instanci ověření AKA omezuje dopad potenciálního kompromitování klíče a poskytuje dopřednou důvěrnost pro uživatelská data v rámci relace.

Historicky byl vývoj AKA motivován potřebou standardizovaného, do budoucna použitelného bezpečnostního základu, který by se mohl vyvíjet s generacemi sítí. Jeho konstrukce zahrnovala poučení z GSM a protokolů pro ověřování v pevných sítích. Použití mechanismu čísla sekvence (SQN), i když přináší složitost pro synchronizaci, bylo záměrnou volbou pro poskytnutí ochrany proti opakování a umožnění domovské síti udržovat stav. Účel AKA se rozšířil od 3G a vytvořil základ architektury bezpečnosti 3GPP, přičemž byl přizpůsobován a vylepšován v každé následující generaci (EPS-AKA pro 4G, 5G AKA pro 5G), aby řešil nové hrozby, jako je možnost spojování účastníků, a podporoval nové architektonické paradigmy, jako je síťové dělení a oddělení řídicí a uživatelské roviny.

## Klíčové vlastnosti

- Poskytuje vzájemné ověření mezi UE a sítí
- Odvozuje relaci specifické šifrovací (CK) a integritní (IK) klíče z dlouhodobého sdíleného tajemství
- Používá číslo sekvence (SQN) pro ochranu proti opakování a synchronizaci
- Umožňuje kryptografické oddělení klíčů pro různé bezpečnostní kontexty a síťové domény
- Podporuje generování více ověřovacích vektorů pro efektivní dávkové zpracování
- Tvoří bezpečnostní základ pro systémy 3G (UMTS), 4G (EPS) a 5G

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.804** (Rel-7) — SMS/MMS over IP Access Support
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [AKA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aka/)
