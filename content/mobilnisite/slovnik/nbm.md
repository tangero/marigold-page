---
slug: "nbm"
url: "/mobilnisite/slovnik/nbm/"
type: "slovnik"
title: "NBM – Network Based Mobility Management"
date: 2025-01-01
abbr: "NBM"
fullName: "Network Based Mobility Management"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nbm/"
summary: "Architektura správy mobility, ve které síť řídí a spravuje mobilitu uživatelského zařízení (UE). Jde o klíčový koncept v architektuře Evolved Packet Core (EPC) a 5G Core (5GC) dle 3GPP, který umožňuje"
---

NBM je architektura správy mobility, ve které síť řídí mobilitu UE, aby umožnila plynulé předávání spojení a kontinuitu relací v systémech 3GPP, jako je EPC a 5GC.

## Popis

Network Based Mobility Management (NBM) je základní architektonický princip v systémech 3GPP, primárně definovaný pro Evolved Packet System (EPS) a pokračující v 5G System (5GS). V tomto modelu je síťová infrastruktura zodpovědná za sledování polohy uživatelského zařízení (UE) a za správu signalizace související s mobilitou, která je nutná k udržení IP konektivity při pohybu UE. Role UE je zjednodušena; provádí připojení k přístupové síti a může hlásit svou polohu, ale složité úkoly správy kontextů mobility, přenosových drah a rozhodování o předání spojení zajišťují síťové uzly. To kontrastuje s hostitelsky orientovanými protokoly mobility, jako je Mobile IP, kde se UE aktivně podílí na správě vlastního mobility bindingu a vytváření tunelů.

V EPS je NBM implementováno prostřednictvím protokolů jako [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) a varianta Proxy Mobile IP (PMIP). Klíčovými síťovými funkcemi jsou Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro mobilitu v řídicí rovině a Serving Gateway (S-GW) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) pro mobilitu v uživatelské rovině. MME sleduje polohu UE na úrovni sledovací oblasti (Tracking Area) a spravuje signalizaci pro předávání spojení a vytváření přenosových drah. S-GW funguje jako lokální kotva mobility, přepínající dráhu uživatelské roviny při pohybu UE mezi eNodeB. P-GW slouží jako IP kotva, poskytující stabilní IP adresu pro PDN připojení UE bez ohledu na její polohu v síti.

V 5GS princip NBM pokračuje, přičemž role v řídicí rovině přebírají Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) funguje jako kotva mobility pro uživatelskou rovinu, analogicky k S-GW a P-GW. 5GC zavádí vyšší flexibilitu, například možnost vybrat pro různé PDU relace různé UPF (UL [CL](/mobilnisite/slovnik/cl/), BP) pro optimalizaci směrování provozu. NBM umožňuje funkce jako plynulé předávání spojení, správu mobility v režimu nečinnosti (aktualizace sledovacích oblastí) a kontinuitu relací. Jeho síťově orientovaný přístup umožňuje optimalizované směrování, efektivní využití síťových zdrojů a implementaci pokročilých politik (např. QoS, účtování) operátorem, což by bylo složitější, pokud by je přímo spravovalo UE.

## K čemu slouží

NBM bylo vyvinuto za účelem poskytnutí škálovatelné, efektivní a operátorem řízené metody pro správu mobility uživatelů v paketově orientovaných mobilních sítích. Před přijetím jednotného přístupu NBM pro EPS v Release 8 3GPP byla správa mobility často vázána na konkrétní přístupové technologie a mohla zahrnovat hostitelsky orientovaná schémata, která kladla značnou zátěž zpracování a signalizace na mobilní zařízení. Primární motivací bylo navrhnout síťovou architekturu, která by dokázala podporovat plynulou mobilitu pro obrovské množství zařízení s různými schopnostmi, od chytrých telefonů po IoT senzory, při zachování kontinuity IP služeb.

Architektura řeší několik klíčových problémů. Za prvé, centralizuje inteligenci v síti, což operátorům umožňuje optimalizovat rozhodnutí o předání spojení na základě vytížení sítě, zásad pro účastníky a požadavků služeb. Za druhé, zjednodušuje návrh UE a šetří její životnost baterie přesunutím složitých signalizačních procedur do sítě. Za třetí, poskytuje stabilní kotvu pro IP relaci uživatele, což zajišťuje, že probíhající komunikace (jako VoIP hovory nebo video přenosy) nejsou při pohybu přerušeny. To je klíčové pro zajištění konzistentní kvality uživatelského zážitku. NBM je navíc nezbytné pro umožnění funkcí jádra sítě, jako je zákonné odposlouchávání, detailní záznamy pro účtování a aplikace konzistentních politik a vynucování QoS bez ohledu na místo připojení UE.

Historicky bylo NBM v EPS (pomocí GTP) přirozeným vývojem z GPRS jádra sítě, což operátorům poskytlo hladkou migrační cestu. Jeho pokračování a vylepšení v 5GS dokazuje jeho zásadní roli při poskytování spolehlivé mobility jako služby, což je předpokladem pro umožnění pokročilých případů užití, jako je massive IoT, ultra spolehlivá komunikace s nízkou latencí (URLLC) a síťové segmenty (network slicing), kde je předvídatelná a řízená mobilita prvořadá.

## Klíčové vlastnosti

- Řízení signalizace mobility a rozhodování o předání spojení ze strany sítě
- Zjednodušení UE s nižší signalizační zátěží a spotřebou energie
- Kontinuita IP relací díky stabilním síťovým kotvám (S-GW/P-GW v EPS, UPF v 5GS)
- Podpora mobility v uživatelské rovině založené na protokolech GTP i PMIP
- Umožňuje správu mobility v režimu nečinnosti prostřednictvím aktualizací sledovacích/směrovacích oblastí
- Základ pro vynucování politik, účtování a zákonný odposlech v celé síti

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO

---

📖 **Anglický originál a plná specifikace:** [NBM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nbm/)
