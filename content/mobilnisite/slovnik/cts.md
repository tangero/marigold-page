---
slug: "cts"
url: "/mobilnisite/slovnik/cts/"
type: "slovnik"
title: "CTS – Cordless Telephony System"
date: 2025-01-01
abbr: "CTS"
fullName: "Cordless Telephony System"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cts/"
summary: "CTS je standardizovaná služba bezšňůrové telefonie podle 3GPP, která umožňuje mobilním zařízením připojovat se k rezidenčním nebo podnikovým základnovým stanicím pro místní hlasové a datové služby. Po"
---

CTS je standardizovaná služba bezšňůrové telefonie podle 3GPP, která umožňuje mobilním zařízením připojovat se k lokálním základnovým stanicím pro hlas a data, čímž propojuje koncepty buněčných a pevných sítí pro plynulou mobilitu a lepší vnitřní pokrytí.

## Popis

Cordless Telephony System (CTS) je komplexní servisní architektura podle 3GPP, která definuje standardizované mechanismy pro provoz mobilních zařízení jako bezšňůrových telefonů ve vymezených lokálních oblastech. Jádrem CTS je systém, ve kterém se uživatelské zařízení (UE) může připojit k lokálním základnovým stanicím (často nazývaným CTS Fixed Parts nebo rezidenční brány), které poskytují pokrytí v domácnostech, kancelářích nebo areálech. Tyto lokální základnové stanice se připojují k jádrové síti přes širokopásmový nebo jiný pevný přístupový síť, čímž vytvářejí lokalizované prostředí podobné buňkové síti.

Architektura se skládá z několika klíčových komponent: CTS-povoleného UE, CTS Fixed Part ([FP](/mobilnisite/slovnik/fp/)), který funguje jako lokální základnová stanice, a funkcí CTS Core Network, které rozhraní s existující mobilní jádrovou sítí ([MSC](/mobilnisite/slovnik/msc/), [HLR](/mobilnisite/slovnik/hlr/) atd.). CTS FP implementuje podmnožinu funkcí rádiové přístupové sítě optimalizovanou pro provoz na krátkou vzdálenost, typicky využívající licencované buňkové spektrum nebo vyhrazená neregulovaná pásma v závislosti na regionálních předpisech. Zpracovává správu rádiových prostředků, základní mobilitu v rámci lokální oblasti a zabezpečené navázání spojení s autorizovanými UE.

Provoz začíná objevením a registrací UE u CTS FP, což zahrnuje autentizaci proti databázi účastníků domovské sítě. Po registraci může UE uskutečňovat a přijímat hovory přes CTS FP, který směruje hlasový provoz lokálně nebo přes jádrovou síť v závislosti na cíli. Kritickým aspektem je správa mobility: když UE opustí pokrytí CTS, systém podporuje předání spojení do makro buněčné sítě a naopak při návratu do pokrytí CTS. To vyžaduje koordinaci mezi subsystémem CTS a entitami pro správu mobility navštívené mobilní sítě.

Služba podporuje jak hlasovou telefonii, tak základní datové služby, s mechanismy kvality služeb pro zajištění přijatelné kvality hovoru přes potenciálně proměnlivé připojení pevné přístupové sítě. Zabezpečení je implementováno prostřednictvím standardních autentizačních a šifrovacích protokolů 3GPP, přizpůsobených pro scénář lokálního přístupu. Systém také zahrnuje rozhraní pro správu pro zřizování, správu poruch a sledování výkonu CTS FP, což operátorům umožňuje nasazovat a udržovat služby bezšňůrové telefonie ve velkém měřítku pro rezidenční nebo podnikové využití.

## K čemu slouží

CTS byl vyvinut pro řešení několika tržních potřeb v telekomunikačním prostředí počátku 21. století. Za prvé měl poskytnout mobilním operátorům řešení pro zlepšení vnitřního pokrytí – trvalou výzvu pro makro buněčné sítě – prostřednictvím využití lokálních základnových stanic instalovaných zákazníky. To bylo obzvláště cenné, protože se využívání mobilních služeb stále více přesouvalo do interiéru. Za druhé nabídl standardizovanou alternativu k proprietárním bezšňůrovým řešením, což umožnilo interoperabilitu mezi zařízeními od různých výrobců a vytvořilo úspory z rozsahu.

Další klíčovou motivací bylo umožnění konvergence pevných a mobilních sítí před dozráním řešení založených na IMS. CTS umožnil operátorům nabízet balíčkované služby, kde mohly mobilní telefony fungovat jako bezšňůrové sluchátka doma, což potenciálně snížilo využívání pevných linek a vytvořilo pevnější vztahy se zákazníky. Pro spotřebitele sliboval pohodlí jediného zařízení pro mobilní i bezšňůrové použití, s potenciálně nižšími náklady na místní hovory uskutečněné přes pevné širokopásmové připojení namísto buňkového času.

Technologie řešila omezení dřívějších přístupů, jako jsou bezšňůrové systémy [DECT](/mobilnisite/slovnik/dect/), které vyžadovaly samostatná sluchátka a nemohly se bezproblémově integrovat s buněčnými předplatnými. Tím, že CTS vycházel ze standardů 3GPP, zajišťoval kompatibilitu s existujícími mobilními sítěmi a systémy správy účastníků, což operátorům umožnilo nasadit jej jako rozšíření jejich buněčných služeb namísto samostatného systému vyžadujícího duplicitní zřizování a správu.

## Klíčové vlastnosti

- Plynulé předání spojení mezi pokrytím CTS a makro buněčnými sítěmi
- Standardizovaná autentizace a šifrování využívající bezpečnostní mechanismy 3GPP
- Podpora hlasové telefonie a základních služeb paketových dat
- Využití buňkového spektra nebo vyhrazených kmitočtových pásem pro lokální přístup
- Integrace s existujícími prvky mobilní jádrové sítě (HLR, MSC, SGSN)
- Rozhraní pro správu pro nasazení rezidenčních CTS Fixed Parts ve velkém měřítku

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.007** (Rel-19) — GSM Um Interface Layer 3 Architecture
- **TS 28.403** (Rel-19) — WLAN Performance Measurements
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TS 42.056** (Rel-19) — GSM Cordless Telephony System (CTS)
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface
- **TS 45.056** (Rel-19) — GSM CTS-FP Radio Requirements

---

📖 **Anglický originál a plná specifikace:** [CTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cts/)
