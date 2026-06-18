---
slug: "s-nssai"
url: "/mobilnisite/slovnik/s-nssai/"
type: "slovnik"
title: "S-NSSAI – Single Network Slice Selection Assistance Information"
date: 2026-01-01
abbr: "S-NSSAI"
fullName: "Single Network Slice Selection Assistance Information"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s-nssai/"
summary: "S-NSSAI (Single Network Slice Selection Assistance Information) je klíčový identifikátor v řezech 5G sítě, používaný k výběru konkrétní instance síťového řezu pro uživatelské zařízení (UE). Skládá se"
---

S-NSSAI je klíčový identifikátor v řezech 5G sítě, který se skládá z typu řezu/služby (SST) a volitelného diferenciátoru řezu (SD) a používá se k výběru konkrétní instance síťového řezu pro uživatelské zařízení (UE).

## Popis

Single Network Slice Selection Assistance Information (S-NSSAI) je základní konstrukcí v systému 5G (5GS), která jednoznačně identifikuje síťový řez. Síťový řez je logická, koncová síť přizpůsobená tak, aby splňovala specifické požadavky služby nebo zákazníka. S-NSSAI používá uživatelské zařízení (UE) a síť k výběru a přiřazení UE ke správné instanci síťového řezu během procedur registrace a vytváření relace. Je to kritický parametr přenášený v signalizačních zprávách ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) mezi UE a funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)).

S-NSSAI se skládá ze dvou částí: povinného typu řezu/služby ([SST](/mobilnisite/slovnik/sst/)) a volitelného diferenciátoru řezu ([SD](/mobilnisite/slovnik/sd/)). SST je 8bitová hodnota, která udává očekávané chování síťového řezu z hlediska vlastností a služeb. Standardizované hodnoty SST zahrnují 1 pro rozšířené mobilní širokopásmové připojení (eMBB), 2 pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a 3 pro hromadný internet věcí (mIoT). SD je 24bitový volitelný identifikátor používaný k rozlišení mezi více síťovými řezy stejného SST, což operátorům umožňuje vytvářet další specializované řezy v rámci široké kategorie (např. různé eMBB řezy pro podnikové a spotřebitelské služby). Kombinace SST a SD umožňuje jemně odstupňovaný výběr řezu.

Během počáteční registrace poskytne UE požadovanou sadu [NSSAI](/mobilnisite/slovnik/nssai/) (Requested NSSAI), což je seznam S-NSSAI odpovídajících řezům, ke kterým si přeje získat přístup. Síť tyto požadavky ověřuje proti předplaceným S-NSSAI (Subscribed S-NSSAIs) účastníka uloženým ve funkci jednotné správy dat ([UDM](/mobilnisite/slovnik/udm/)). AMF ve spolupráci s funkcí výběru síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)) vybere příslušné instance síťových řezů a vrátí UE povolenou sadu NSSAI (Allowed NSSAI) pro použití v aktuální registrační oblasti. Tato povolená NSSAI se pak používá pro následné vytváření relací s funkcí správy relací (SMF). S-NSSAI ovlivňuje výběr všech ostatních funkcí jádra sítě (SMF, PCF, UPF) a může být použito k aplikaci specifických síťových politik, profilů kvality služeb (QoS) a tarifních pravidel, což umožňuje skutečnou koncovou logickou izolaci a přizpůsobení sítě.

## K čemu slouží

S-NSSAI bylo zavedeno ve specifikaci 3GPP Release 15 jako klíčový prvek umožňující řezy 5G sítě, což je revoluční koncept, který umožňuje rozdělení jedné fyzické síťové infrastruktury na více virtuálních, nezávislých logických sítí. Před 5G sítě poskytovaly převážně monolitické služby; přizpůsobení sítě pro různé typy služeb (např. streamování videa, autonomní řízení, senzorové sítě) bylo složité a neefektivní. S-NSSAI to řeší tím, že poskytuje jednoduchý, standardizovaný identifikátor, který umožňuje jak zařízení, tak síti dynamicky vybrat předem nakonfigurovaný řez se specifickými charakteristikami.

Vytvoření S-NSSAI bylo motivováno rozmanitými a přísnými požadavky 5G případů užití, které sahají od vysoké šířky pásma a nízké latence až po masivní hustotu připojení. Řeší problém, jak efektivně směrovat provoz a aplikovat přizpůsobené prostředky bez nutnosti budovat samostatné fyzické sítě. Zahrnutím S-NSSAI do signalizace může systém 5G pro každou relaci vytvořit správnou sadu síťových funkcí a politik. To operátorům umožňuje nabízet síť jako službu (NaaS), podporovat podnikové privátní sítě a optimalizovat využití prostředků, čímž se odemykají nové zdroje příjmů a jsou splněny výkonnostní požadavky moderních aplikací.

## Klíčové vlastnosti

- Jednoznačně identifikuje síťový řez pomocí SST a volitelného SD
- Přenáší se v NAS signalizaci pro výběr řezu během registrace UE
- Umožňuje síti vybrat instance AMF, SMF, PCF a UPF specifické pro řez
- Podporuje standardizované typy řezů/služeb (eMBB, URLLC, MIoT)
- Umožňuje operátorům definovat více diferencovaných řezů na jeden SST
- Integruje se s údaji účastníka (UDM) pro autorizaci řezu

## Související pojmy

- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)
- [SST – Spectral Smoothing Technique](/mobilnisite/slovnik/sst/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 24.575** (Rel-19) — UE Pre-configuration for MBS
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- … a dalších 42 specifikací

---

📖 **Anglický originál a plná specifikace:** [S-NSSAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-nssai/)
