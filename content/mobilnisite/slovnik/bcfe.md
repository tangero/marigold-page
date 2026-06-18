---
slug: "bcfe"
url: "/mobilnisite/slovnik/bcfe/"
type: "slovnik"
title: "BCFE – Broadcast Control Functional Entity"
date: 2025-01-01
abbr: "BCFE"
fullName: "Broadcast Control Functional Entity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bcfe/"
summary: "Broadcast Control Functional Entity (BCFE) je logická entita v rámci UMTS Radio Network Controller (RNC) odpovědná za správu vysílacích služeb. Zpracovává vysílání systémových informací a zpráv cell b"
---

BCFE je logická entita v UMTS RNC (radiovém síťovém řadiči) odpovědná za správu vysílacích služeb, včetně vysílání systémových informací a zpráv cell broadcast všem UE v buňce nebo skupině buněk.

## Popis

Broadcast Control Functional Entity (BCFE) je základní logická komponenta v architektuře Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) sítě UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), jak je definována ve specifikacích 3GPP Release 99 a následujících. Nachází se v řídicí rovině (Control Plane) RNC a je odpovědná za centralizovanou správu a distribuci vysílacích informací napříč jednou či více buňkami. Primární funkcí BCFE je zajistit, aby všechna uživatelská zařízení (UE) v její pokryté oblasti obdržela konzistentní a včasné systémové informace a zprávy služby cell broadcast ([CBS](/mobilnisite/slovnik/cbs/)). Funguje tak, že komunikuje s dalšími funkčními entitami RNC a jádrem sítě, aby přijímala obsah k vysílání, který následně zpracovává a plánuje pro přenos přes rozhraní vzduchu prostřednictvím Node B.

Z architektonického hlediska je BCFE součástí funkcionality vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) v rámci RNC. Spolupracuje s entitami Paging and Notification Control Functional Entity ([PNFE](/mobilnisite/slovnik/pnfe/)) a Dedicated Control Functional Entity ([DCFE](/mobilnisite/slovnik/dcfe/)). BCFE generuje bloky systémových informací (System Information Blocks – SIBy), které obsahují klíčové parametry pro výběr buňky, převýběr buňky a přístup k síti. Také zpracovává zprávy Cell Broadcast, což jsou krátké textové zprávy vysílané všem UE v definované geografické oblasti, například pro systémy veřejného varování (např. varování před zemětřesením a tsunami) nebo pro lokalizační komerční služby. Entita spravuje plánování, opakování a segmentaci těchto vysílacích zpráv, aby zajistila spolehlivý příjem i pro UE ve špatných rádiových podmínkách.

Z procedurálního hlediska zahrnuje činnost BCFE několik klíčových procesů. Pro vysílání systémových informací kompiluje SIBy na základě konfiguračních dat a stavu sítě. Tyto SIBy jsou pak namapovány na logické kanály Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) a následně na Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)) a Secondary Common Control Physical Channel (S-CCPCH) pro fyzický přenos. Pro službu Cell Broadcast Service přijímá BCFE zprávy CBS z Cell Broadcast Centre (CBC) v jádru sítě přes rozhraní Iu-BC. Zpracovává tyto zprávy, které mohou obsahovat informace o geografickém cílení, a určuje vhodné buňky pro vysílání. BCFE je odpovědná za spolehlivé doručení těchto zpráv, implementuje mechanismy pro opakování zpráv a spravuje vysílací plán, aby se předešlo zahlcení rádiového rozhraní.

BCFE hraje klíčovou roli v efektivitě sítě a veřejné bezpečnosti. Centralizací vysílací kontroly minimalizuje redundantní zpracování na jednotlivých Node B a zajišťuje konzistentní doručování informací v celé síti. Její návrh umožňuje flexibilní konfiguraci vysílacích oblastí, od jedné buňky po více buněk nebo dokonce celou síť. Tato schopnost je nezbytná jak pro rutinní síťové operace (prostřednictvím SIBů), tak pro nouzovou komunikaci (prostřednictvím CBS). Funkcionalita entity je podrobně specifikována v mnoha technických specifikacích 3GPP, včetně TS 25.331 (protokol RRC) a TS 25.931 (funkce UTRAN).

## K čemu slouží

Broadcast Control Functional Entity (BCFE) byla zavedena ve 3GPP Release 99, aby vyřešila potřebu standardizovaného, efektivního a spolehlivého mechanismu pro vysílání řídicích informací a zpráv veřejných služeb v sítích UMTS. Před standardizací 3GPP byla vysílací funkcionalita v celulárních sítích často implementována proprietárními způsoby, což vedlo k problémům s interoperabilitou a neefektivnímu využití rádiových prostředků. BCFE byla vytvořena, aby poskytla centralizovanou, síťově řízenou entitu, která by mohla koordinovaně spravovat veškerý vysílací provoz, a zajistila tak, že nezbytné systémové informace a nouzové výstrahy dorazí ke všem uživatelským zařízením v cílové oblasti bez nutnosti individuální signalizace ke každému zařízení.

Primární problém, který BCFE řeší, je efektivní šíření společných informací k velkému počtu UE. Bez vyhrazené vysílací řídicí entity by sítě musely stejné informace odesílat individuálně každému UE, což by spotřebovávalo nadměrné signalizační prostředky a způsobovalo zahlcení sítě. BCFE umožňuje komunikaci typu jeden–k–mnoha přes rádiové rozhraní, což je pro distribuci parametrů potřebných pro výběr buňky, přístup k síti a veřejná varování mnohem efektivnější. Tento návrh byl obzvláště důležitý pro UMTS, které zavedlo složitější struktury systémových informací a podporovalo nové služby, jako je Cell Broadcast Service (CBS) pro systémy veřejného varování a lokalizační informace.

Historicky motivace pro vytvoření BCFE vycházela z vývoje mobilních sítí směrem k sofistikovanějším službám a rostoucího uznání mobilních sítí jako platformy pro komunikaci v oblasti veřejné bezpečnosti. Omezení předchozích přístupů v systémech 2G, kde byla vysílací funkcionalita méně standardizovaná a integrovaná, zdůraznila potřebu robustního a škálovatelného vysílacího rámce v 3G. Vytvoření BCFE bylo hnáno požadavky na lepší efektivitu sítě, podporu povinných systémů veřejného varování (které se v mnoha zemích staly regulatorní požadavkem) a potřebou flexibilní architektury, která by mohla podporovat budoucí vysílací služby. Centralizací vysílací kontroly v RNC poskytla BCFE základ pro spolehlivé vysílací služby, které zůstávají nezbytné v moderních celulárních sítích.

## Klíčové vlastnosti

- Centralizovaná správa generování a vysílání bloků systémových informací (System Information Blocks – SIB)
- Zpracování a plánování zpráv služby Cell Broadcast Service (CBS) přijatých z jádra sítě
- Mapování vysílacích informací na příslušné logické kanály (BCCH, CTCH) a transportní kanály (FACH)
- Správa geografické oblasti pro cílenou distribuci vysílacích zpráv
- Podpora segmentace a opakování zpráv pro zajištění spolehlivého příjmu ve špatných rádiových podmínkách
- Koordinace s dalšími funkčními entitami RNC (PNFE, DCFE) pro integrovaný provoz řídicí roviny

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [BCFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcfe/)
