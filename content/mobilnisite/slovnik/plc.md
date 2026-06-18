---
slug: "plc"
url: "/mobilnisite/slovnik/plc/"
type: "slovnik"
title: "PLC – Programmable Logic Controller"
date: 2025-01-01
abbr: "PLC"
fullName: "Programmable Logic Controller"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/plc/"
summary: "Průmyslový digitální počítač přizpůsobený pro řízení výrobních procesů nebo strojů. V kontextu 3GPP se jedná o zařízení v průmyslové automatizaci využívající pro komunikaci mobilní sítě (např. 5G), co"
---

PLC (Programovatelný logický řadič) je průmyslový digitální počítač používaný v automatizaci, který se připojuje prostřednictvím mobilních sítí jako je 5G, aby umožnil vysoce spolehlivou komunikaci s nízkou latencí pro řízení strojů.

## Popis

Programovatelný logický řadič (PLC) je odolný průmyslový počítačový systém navržený pro řízení průmyslových elektromechanických procesů v reálném čase, jako jsou montážní linky, robotická zařízení nebo stroje. V kontextu norem 3GPP jsou PLC identifikovány jako klíčový případ užití a koncové zařízení pro mobilní komunikaci, zejména s nástupem 5G a jeho podporou vysoce spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a integrace s časově citlivými sítěmi ([TSN](/mobilnisite/slovnik/tsn/)). Typický systém PLC se skládá z centrální procesorové jednotky, vstupních/výstupních modulů pro rozhraní se senzory a aktuátory, zdroje napájení a komunikačního rozhraní. Jeho hlavní funkcí je nepřetržité monitorování stavu vstupních zařízení, provádění uživatelem naprogramované řídicí logiky (často pomocí logiky kontaktů – ladder logic – nebo strukturovaného textu) a rozhodování pro řízení stavu výstupních zařízení.

Při připojení prostřednictvím sítě 3GPP umožňuje komunikační modul PLC (např. 5G modem) komunikaci s dalšími PLC, systémy SCADA nebo cloudovými výrobními provozními systémy ([MES](/mobilnisite/slovnik/mes/)). To umožňuje distribuované řídicí architektury, kde řídicí smyčky mohou překlenout velké vzdálenosti. Síť 3GPP poskytuje „drát“, který nahrazuje tradiční sběrnicové nebo drátové připojení Ethernet. Aby to fungovalo, musí síť poskytovat deterministickou latenci, extrémně vysokou spolehlivost (např. 99,9999 %) a přesnou časovou synchronizaci, což řeší funkce 5G NR, jako je přístup do uplinku bez přidělení (grant-free uplink), plánování v mini-slotech a vylepšený návrh fyzické vrstvy.

Úloha PLC v průmyslovém IoT (IIoT) ekosystému podporovaném 3GPP je transformační. Přesouvá průmyslové řízení z izolovaných, drátových sítí na flexibilní bezdrátové systémy, které podporují pokročilé aplikace jako mobilní roboti, rozšířená realita pro údržbu a adaptivní výrobní linky. Specifikace 3GPP studují a definují požadavky (např. v TS 22.804, TS 22.832) pro tyto komunikační služby, aby zajistily, že rádiové rozhraní a základní síť mohou splnit přísné požadavky uzavřených řídicích smyček, kde by zpožděný nebo ztracený paket mohl způsobit výrobní závadu nebo bezpečnostní incident.

## K čemu slouží

Tradiční PLC pracovaly na izolovaných, drátových sítích (např. PROFIBUS, Modbus), které nabízely spolehlivost a determinismus, ale postrádaly flexibilitu, byly nákladné na instalaci a přeconfiguraci a bránily adopci agilních výrobních konceptů, jako je Průmysl 4.0. Účelem integrace PLC se sítěmi 3GPP je odemknout bezdrátovou konektivitu pro průmyslovou automatizaci, což umožní škálovatelné, rekonfigurovatelné a mobilní aplikace.

Práce 3GPP na PLC řeší omezení předchozích bezdrátových technologií (jako je Wi-Fi), které nemohly garantovat vysoce spolehlivou, nízkolatentní a časově synchronizovanou komunikaci potřebnou pro tvrdé řízení v reálném čase. Motivace vychází z požadavků průmyslu na bezdrátový přístup k pohyblivým částem (např. na robotických ramenech), zjednodušení kabeláže ve složitých provozech a možnosti rychlého převedení výrobních linek. Definováním PLC jako klíčového případu užití od verze Rel-15 výše zajišťuje 3GPP, že se mobilní technologie vyvíjí pro podporu těchto aplikací s vysokou mírou kritičnosti, usnadňuje konvergenci provozních technologií ([OT](/mobilnisite/slovnik/ot/)) a informačních technologií ([IT](/mobilnisite/slovnik/it/)) a připravuje cestu pro plně flexibilní chytré továrny.

## Klíčové vlastnosti

- Deterministické řízení průmyslových procesů v tvrdém reálném čase
- Podpora programovacích standardů logiky kontaktů (ladder logic) a IEC 61131-3
- Odolný návrh pro náročné průmyslové prostředí
- Integrace se sítěmi 3GPP pro schopnosti URLLC a TSN
- Rozsáhlá podpora digitálních a analogových I/O modulů
- Umožňuje mobilní automatizaci a bezdrátové řízení v uzavřené smyčce

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.447** (Rel-19) — EVS Frame Loss Concealment Procedure
- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification
- **TR 26.865** (Rel-18) — Technical Report
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TR 28.865** (Rel-18) — Technical Report on Deterministic Communication Service Assurance
- **TR 28.907** (Rel-19) — Enhanced Management of Non-Public Networks
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [PLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/plc/)
