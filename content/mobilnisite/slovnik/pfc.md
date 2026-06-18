---
slug: "pfc"
url: "/mobilnisite/slovnik/pfc/"
type: "slovnik"
title: "PFC – Packet Flow Context"
date: 2025-01-01
abbr: "PFC"
fullName: "Packet Flow Context"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pfc/"
summary: "Logický kontext v SGSN a GGSN, který spravuje stav a parametry pro konkrétní tok paketových dat uživatele. Je klíčový pro aplikaci správných zásad QoS, účtování a směrování na jednotlivé datové proudy"
---

PFC je logický kontext v SGSN a GGSN, který spravuje stav a parametry pro konkrétní tok paketových dat, aby mohl aplikovat správné zásady QoS, účtování a směrování.

## Popis

Packet Flow Context (PFC) je základní koncept v architektuře paketového jádra [GPRS](/mobilnisite/slovnik/gprs/) a UMTS, konkrétně spravovaný Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Gateway GPRS Support Node (GGSN). Představuje logický stav a přidružené parametry pro konkrétní tok paketových dat patřící do Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) kontextu uživatele. Jeden PDP kontext, který uživateli zřizuje IP relaci, může obsahovat více PFC, z nichž každý odpovídá odlišnému provoznímu toku s jedinečnými požadavky, jako je například VoIP hovor, relace prohlížení webu nebo video stream. PFC obsahuje všechny potřebné informace pro zpracování tohoto konkrétního toku, včetně jeho Traffic Flow Template ([TFT](/mobilnisite/slovnik/tft/)) pro filtrování paketů, přidruženého QoS profilu a identifikátorů účtování.

Provozně je PFC vytvářen, upravován nebo mazán signalizací mezi User Equipment (UE), SGSN a GGSN, obvykle iniciovanou potřebou aplikace pro specifický přenosový kanál. Když dorazí uplink pakety od UE, SGSN použije TFT uložený v PFC k jejich zařazení do správného toku. GGSN provádí podobnou klasifikaci pro downlink pakety přijaté z externí Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)). Po zařazení síť aplikuje parametry QoS (jako garantovaný přenosový výkon, priorita a zpoždění) definované v QoS profilu PFC, aby zajistila, že tok bude mít odpovídající zacházení prostřednictvím mechanismů plánování a řízení přístupu jak v jádře, tak v rádiové přístupové síti.

Role PFC je úzce integrována se systémy účtování. Každý PFC je propojen s konkrétním Charging ID, což síti umožňuje generovat samostatné, podrobné záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro každý služební tok. To umožňuje sofistikované modely účtování, jako je například účtování video streamu odlišně od synchronizace e-mailů na pozadí. PFC tedy funguje jako ústřední kotvící bod pro vynucování zásad, spojující dohromady filtrování paketů (TFT), kvalitu služeb (QoS) a účtování pro jednotlivý datový proud, což umožňuje jemně odstupňovanou diferenciaci služeb, která je charakteristickým znakem paketových sítí 3GPP.

## K čemu slouží

Packet Flow Context byl zaveden, aby odstranil omezení spočívající v tom, že uživatel měl k dispozici pouze jediný, monolitický přenosový kanál ([PDP](/mobilnisite/slovnik/pdp/) kontext) na IP adresu. Rané implementace [GPRS](/mobilnisite/slovnik/gprs/) mohly aplikovat jednotnou politiku QoS a účtování na veškerý provoz uživatele. To bylo nedostatečné pro umožnění více souběžných služeb s odlišnými požadavky, jako je například hlasový hovor vyžadující nízké zpoždění a stahování souboru vyžadující vysokou přenosovou kapacitu, přes stejné IP připojení.

Vytvoření konceptu PFC umožnilo zřídit více vyhrazených logických přenosových kanálů v rámci jednoho PDP kontextu. Tím se vyřešil kritický problém diferenciace služeb. Síťoví operátoři mohli nyní nabízet sofistikované služby se zaručeným výkonem tím, že přidělovali specifické síťové zdroje a tarifní plány jednotlivým aplikačním tokům. Poskytl potřebnou granularitu pro správu provozu a jeho monetizaci, čímž položil základy pro IP Multimedia Subsystem (IMS) a další služby reálného času v sítích 3GPP. Mechanismus PFC byl klíčovým vývojem od datové sítě typu best-effort k řízené, multislužební síti schopné podporovat různorodou kvalitu služeb (QoS).

## Klíčové vlastnosti

- Umožňuje více odlišných paketových toků v rámci jednoho PDP kontextu
- Ukládá Traffic Flow Template (TFT) pro filtrování a klasifikaci uplink a downlink paketů
- Přiřazuje konkrétní QoS profil (např. ARP, GBR, MBR) každému jednotlivému toku
- Propojuje se s jedinečným Charging ID pro účtování a fakturaci specifickou pro daný tok
- Spravován prostřednictvím signalizačních procedur mezi UE, SGSN a GGSN (operace PFC)
- Umožňuje nezávislou aktivaci, modifikaci a deaktivaci toků

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [PFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pfc/)
