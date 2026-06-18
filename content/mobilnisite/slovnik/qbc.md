---
slug: "qbc"
url: "/mobilnisite/slovnik/qbc/"
type: "slovnik"
title: "QBC – QoS flow Based Charging"
date: 2026-01-01
abbr: "QBC"
fullName: "QoS flow Based Charging"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/qbc/"
summary: "Mechanismus účtování v systému 5G, kde je fakturace přímo vázána na jednotlivé toky QoS. Umožňuje detailní, na službu orientované účtování tím, že spojuje účtovací data s konkrétními úrovněmi kvality"
---

QBC je mechanismus účtování v systému 5G, kde je fakturace přímo vázána na jednotlivé toky QoS, což umožňuje detailní, na službu orientované účtování založené na konkrétních úrovních kvality služby a instancích síťových řezů.

## Popis

QoS flow Based Charging (QBC) je architektura účtování definovaná v rámci 5G Core sítě dle 3GPP, specifikovaná primárně v řadě specifikací 32-series (Charging). Představuje posun paradigmatu od účtování založeného na přenosových kanálech (bearer) v 4G EPS k detailnějšímu, na tok orientovanému modelu, který je v souladu s architekturou založenou na službách (service-based architecture) a modelem QoS v 5G Core. V 5G je provoz v uživatelské rovině organizován do toků QoS, z nichž každý má jedinečný identifikátor toku QoS ([QFI](/mobilnisite/slovnik/qfi/)) a specifický profil QoS definující parametry jako 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)), Guaranteed Flow Bit Rate (GFBR) a Maximum Flow Bit Rate ([MFBR](/mobilnisite/slovnik/mfbr/)). QBC funguje tak, že generuje záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) nebo účtovací události, které jsou korelovány s těmito jednotlivými toky QoS.

Architektura zahrnuje několik klíčových síťových funkcí. Centrální rolí disponuje Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), která v rámci [PDU](/mobilnisite/slovnik/pdu/) session vytváří, upravuje a uvolňuje toky QoS. SMF komunikuje s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), aby získala pravidla pro řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)). Tato PCC pravidla zahrnují i instrukce pro účtování, které určují, jak má být účtován konkrétní tok služebních dat namapovaný na tok QoS. Když je účtování spuštěno, SMF, která vystupuje jako Charging Trigger Function (CTF), shromažďuje relevantní informace pro účtování, jako jsou identifikátory toků QoS, objemy dat, doba trvání a související informace o síťovém řezu. Tyto informace pak předává funkci Charging Data Function (CDF) nebo Online Charging System (OCS) přes rozhraní založené na službách Nchf.

Fungování QBC je neodmyslitelně spojeno s modelem QoS v 5G. Jedna PDU session může obsahovat více toků QoS – například jeden pro hlasový provoz s vysokou prioritou, jeden pro best-effort prohlížení internetu a další pro službu hraní s nízkou latencí. QBC umožňuje operátorovi aplikovat na každý z těchto toků nezávisle odlišné sazby účtování, kvóty nebo fakturační modely. Záznamy o účtování mohou zachytit nejen objem a čas, ale také konkrétní hodnotu 5QI, instanci síťového řezu (S-NSSAI) obsluhující tok a název datové sítě (DNN). To umožňuje vysoce detailní fakturační reporty a usnadňuje cenové rozlišení podle služby, například účtování prémie za toky se zaručenou nízkou latencí nebo nulové účtování (zero-rating) za toky specifických aplikací.

## K čemu slouží

QBC byl vytvořen, aby řešil omezení modelu účtování založeného na přenosových kanálech (bearer) v EPS, který nebyl dostatečně detailní pro rozmanitou paletu služeb plánovanou pro 5G. V 4G bylo účtování typicky asociováno s EPS bearer, který agregoval provoz s podobnými požadavky na QoS. To ztěžovalo implementaci detailních, na konkrétní službu orientovaných účtovacích politik, zejména když se sítě vyvíjely k podpoře síťových řezů a široké škály služeb pro vertikální odvětví s odlišnými profily QoS.

Hlavním problémem, který QBC řeší, je umožnění zpoplatňovacích modelů odpovídajících technickým schopnostem 5G. S koexistencí síťových řezů, IoT služeb, ultra-spolehlivé komunikace s nízkou latencí (URLLC) a vylepšeného mobilního širokopásmového přístupu (eMBB) na stejné infrastruktuře je jednotný přístup k účtování nedostatečný. QBC poskytuje mechanismus pro účtování založené na skutečné hodnotě nebo nákladech na poskytnutí konkrétní úrovně QoS. To operátorům umožňuje vytvářet inovativní tarify, nabízet fakturaci založenou na smlouvě o úrovni služeb (SLA) podnikovým zákazníkům a implementovat politiky spravedlivého použití, které berou v úvahu spotřebovanou kvalitu služby, nikoli pouze hrubý objem dat. Jeho zavedení bylo motivováno obchodní potřebou zpoplatnit pokročilé schopnosti 5G nad rámec jednoduchých datových balíčků.

## Klíčové vlastnosti

- Detailnost účtování na úrovni jednotlivých 5G toků QoS, identifikovaných pomocí QFI
- Integrace s rámcem 5G Policy and Charging Control (PCC) prostřednictvím PCF
- Podpora offline (založených na CDR) i online (s řízením kreditu) scénářů účtování
- Účtovací data mohou být korelována s instancí síťového řezu (S-NSSAI) a DNN
- Umožňuje cenové modely rozlišené podle služby (např. prémiové sazby za toky se zaručenou přenosovou rychlostí/nízkou latencí)
- Využívá rozhraní založené na službách Nchf mezi CTF (např. SMF) a účtovacími systémy

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification

---

📖 **Anglický originál a plná specifikace:** [QBC na 3GPP Explorer](https://3gpp-explorer.com/glossary/qbc/)
