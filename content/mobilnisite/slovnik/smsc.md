---
slug: "smsc"
url: "/mobilnisite/slovnik/smsc/"
type: "slovnik"
title: "SMSC – Short Message Service Centre"
date: 2025-01-01
abbr: "SMSC"
fullName: "Short Message Service Centre"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smsc/"
summary: "SMSC je základní síťová entita zodpovědná za ukládání, předávání a doručování SMS zpráv mezi mobilními účastníky. Funguje jako systém typu „ulož a předej“ (store-and-forward), který zajišťuje doručení"
---

SMSC je základní síťová entita zodpovědná za standardizovanou operaci typu „ulož a předej“ (store-and-forward), která doručuje SMS zprávy mezi mobilními účastníky a zajišťuje doručení i v případě, kdy je příjemce nedostupný.

## Popis

Short Message Service Centre (SMSC) je kritický síťový prvek v architektuře GSM a UMTS, určený speciálně pro službu krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)). Funguje jako systém typu „ulož a předej“ (store-and-forward), což znamená, že přijímá zprávy od odesílající entity, dočasně je ukládá a následně se pokouší doručit je zamýšlenému příjemci. Primární rolí SMSC je zajistit spolehlivé doručování SMS, včetně zpracování scénářů, kdy je zařízení příjemce vypnuté nebo mimo dosah sítě, opakovanými pokusy o doručení po konfigurovatelnou dobu. SMSC komunikuje s různými dalšími síťovými komponentami, včetně Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) pro SMS v přepojování okruhů a IP Short Message Gateway ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)) pro SMS přes IP sítě, aby zprávy správně směroval.

Z architektonického hlediska se SMSC skládá z několika funkčních komponent. Jádrem je úložiště zpráv, které uchovává zprávy čekající na doručení nebo vyzvednutí. Obsahuje směrovací logiku pro určení cílové sítě a vhodné signalizační cesty, například přes [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) nad [SS7](/mobilnisite/slovnik/ss7/) nebo Diameter nad IP. SMSC také spravuje účastnická data relevantní pro SMS, jako jsou nastavení služby nebo informace o tom, zda je účastník ze služby vyloučen. Generuje záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro účely fakturace a implementuje protokoly definované v technických specifikacích, jako je 3GPP TS 23.040 (technická realizace) a TS 23.078 (uživatelské aplikace).

Během provozu, když je odeslána mobilně iniciovaná ([MO](/mobilnisite/slovnik/mo/)) SMS, přenese ji mobilní zařízení přes rádiový přístup a základní síť do SMSC. SMSC potvrdí příjem a následně zahájí proceduru doručení mobilně terminované ([MT](/mobilnisite/slovnik/mt/)) zprávy. Dotazuje se Home Location Register (HLR) nebo Home Subscriber Server (HSS), aby získala aktuální směrovací informace (např. adresu obsluhujícího MSC nebo SGSN/MME) pro příjemce. Zpráva je poté předána této síťové entitě pro doručení do mobilního zařízení. Pokud se doručení nezdaří, SMSC naplánuje opakované pokusy na základě své konfigurace. Tento oddělený, asynchronní model je klíčový pro spolehlivost SMS.

Role SMSC se rozšířila se zavedením SMS přes IP a IMS. V pozdějších vydáních standardů komunikuje s IP-SM-GW, které funguje jako propojovací funkce mezi starší SMS založenou na MAP a SIP-based zasíláním zpráv v IMS, jak je definováno v TS 23.204. To umožňuje plynulé pokračování služeb SMS při vývoji sítí směrem k plně IP základním sítím. Dále SMSC podporuje nadstandardní služby prostřednictvím rozhraní k externím aplikačním serverům (např. SMS brány pro doručování obsahu) a umožňuje funkce jako rozesílání SMS (broadcasting) nebo zpoplatněné zprávy, což z něj činí univerzální platformu pro zasílání zpráv jak mezi osobami, tak z aplikací k osobám.

## K čemu slouží

SMSC byl vytvořen pro umožnění služby krátkých textových zpráv (SMS), což je základní služba mobilních dat specifikovaná v raných standardech GSM. Jeho primárním účelem je poskytnout spolehlivý mechanismus zasílání zpráv typu „ulož a předej“, který funguje nezávisle na spojení pro hlasové hovory. Před rozšířením mobilních dat nabízela SMS jednoduchý a efektivní způsob odesílání krátkých textových zpráv využívající nevyužitou kapacitu signalizačních kanálů používaných pro řízení sítě (Stand-alone Dedicated Control Channel, SDCCH). SMSC řeší problém doručování zpráv do mobilních zařízení, která mohou být dočasně nedostupná, a zajišťuje, aby žádná zpráva nebyla trvale ztracena kvůli stavu sítě nebo zařízení.

Historicky byla motivací využít stávající síťovou signalizační infrastrukturu pro novou, ziskovou službu bez nutnosti zásadních síťových upgradů. Model „ulož a předej“ byl zvolen namísto pokusů o doručení v reálném čase, protože zohledňoval omezení raných mobilních sítí, kde byla zařízení často vypnutá nebo mimo dosah. Tento návrh také umožnil funkce jako odložené doručení nebo indikátor čekající zprávy. SMSC standardizoval centrální bod pro směrování SMS, propojení mezi operátory a účtování, což bylo klíčové pro interoperabilitu, jež učinila SMS celosvětovým úspěchem.

S vývojem sítí se účel SMSC rozšířil o udržení kontinuity služby SMS během přechodu na sítě s přepojováním paketů a sítě založené na IMS. Řešil výzvu podpory starších SMS v nových architekturách založených na IP, čímž zajistil zpětnou kompatibilitu pro miliardy účastníků. Jeho trvalou rolí je poskytovat osvědčenou a spolehlivou přepravu zpráv, která podporuje nejen textování mezi uživateli, ale také kritickou komunikaci mezi stroji (M2M), dvoufázové ověřování a různé systémy výstrah, což z něj činí nepostradatelnou součást mobilní telekomunikace.

## Klíčové vlastnosti

- Zpracování zpráv typu „ulož a předej“ s konfigurovatelnou dobou platnosti a plánem opakovaných pokusů
- Rozhraní s HLR/HSS pro dotazování na polohu a stav účastníka pomocí MAP nebo Diameter
- Generuje záznamy o účtování (CDR) pro fakturaci transakcí SMS
- Podporuje procedury mobilně iniciovaných (MO-SM) i mobilně terminovaných (MT-SM) zpráv
- Spolupracuje s IP-SM-GW pro doručování SMS přes IMS a IP sítě
- Umožňuje nadstandardní služby prostřednictvím rozhraní k externím aplikacím (např. pro hromadné rozesílání zpráv nebo prémiový obsah)

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [SMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/smsc/)
