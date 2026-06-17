---
slug: "asti"
url: "/mobilnisite/slovnik/asti/"
type: "slovnik"
title: "ASTI – Access Stratum Time distribution"
date: 2025-01-01
abbr: "ASTI"
fullName: "Access Stratum Time distribution"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/asti/"
summary: "ASTI je mechanismus 3GPP pro distribuci přesných informací o časové synchronizaci ze sítě k uživatelskému zařízení (UE) prostřednictvím přístupové vrstvy (AS). Umožňuje aplikace vyžadující přesné časo"
---

ASTI je mechanismus 3GPP pro distribuci přesných informací o časové synchronizaci ze sítě k uživatelskému zařízení (UE) prostřednictvím přístupové vrstvy (Access Stratum) za účelem umožnění aplikací vyžadujících přesnost na úrovni submikrosekund.

## Popis

Access Stratum Time distribution (ASTI, distribuce času přístupové vrstvy) je standardizovaný rámec zavedený ve specifikaci 3GPP Release 17, který umožňuje distribuci přesných časových informací ze sítě k uživatelskému zařízení (UE) prostřednictvím buněčného rádiového rozhraní. Na rozdíl od tradičních synchronizačních metod, které spoléhají na externí systémy jako [GNSS](/mobilnisite/slovnik/gnss/) nebo Network Time Protocol (NTP), ASTI využívá stávající buněčnou infrastrukturu k doručování časových referencí s vysokou přesností a spolehlivostí. Systém funguje v rámci přístupové vrstvy (Access Stratum), která zajišťuje veškerou rádiovou komunikaci mezi UE a rádiovou přístupovou sítí (RAN), čímž se časové informace stávají nedílnou součástí buněčného připojení.

Architektura ASTI zahrnuje několik klíčových síťových prvků pracujících v koordinaci. Primárním zdrojem je přesný časový zdroj typu Precision Time Protocol (PTP) grandmaster nebo jiný vysoce přesný časový zdroj připojený k jádru sítě. Tato časová reference je distribuována prostřednictvím architektury 5G System (5GS) k gNodeB (gNB) v RAN. gNB následně začlení časové informace do specifických zpráv řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) nebo bloků systémových informací (SIB), které jsou vysílány všem UE. Modem v UE tyto zprávy zpracuje, aby extrahoval a aplikoval časové korekce, přičemž kompenzuje zpoždění šíření a zpracování pomocí sofistikovaných algoritmů.

Implementace ASTI zahrnuje více technických komponent, včetně časového značkování v bodech vysílání a příjmu, odhadu zpoždění šíření a kompenzačních mechanismů. gNB označuje časy vysílání s vysokou přesností, zatímco UE zaznamenávají časy příjmu a vypočítávají měření doby oběhu. Tato měření zohledňují faktory jako šíření signálu různými médii, zpoždění zpracování hardwaru a atmosférické podmínky. Systém podporuje jak periodické vysílání časových informací pro obecnou synchronizaci, tak i doručování na vyžádání (unicast) pro konkrétní UE vyžadující vyšší přesnost nebo další časové parametry.

Z pohledu protokolů funguje ASTI napříč více vrstvami zásobníku 3GPP. Na vrstvě RRC nesou vyhrazené zprávy časové informace a konfigurační parametry. Fyzická vrstva poskytuje přesné časové referenční body prostřednictvím synchronizačních signálů a referenčních symbolů. Vyšší vrstvy v UE, včetně aplikační vrstvy, mohou k synchronizovanému času přistupovat prostřednictvím standardizovaných aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)). Tento vícevrstvý přístup zajišťuje, že časové informace si zachovávají přesnost v celém přenosovém řetězci a zároveň jsou dostupné různým aplikacím běžícím na UE.

Systém podporuje různé úrovně přesnosti od mikrosekund po nanosekundy v závislosti na scénářích nasazení a možnostech UE. Pro aplikace průmyslového IoT může ASTI poskytnout synchronizaci lepší než 1 mikrosekunda, zatímco pro méně náročné aplikace může poskytovat přesnost na úrovni milisekund. Rámec zahrnuje mechanismy pro detekci chyb, indikaci kvality a záložní procedury, když kvalita časování klesne pod požadované prahové hodnoty. To zajišťuje, že aplikace dostávají spolehlivé časové informace i v náročných rádiových podmínkách nebo během přechodů v síti.

## K čemu slouží

ASTI byl vyvinut, aby řešil rostoucí potřebu přesné časové synchronizace v buněčných sítích bez nutnosti spoléhat se na externí časové zdroje na úrovni zařízení. Mnoho nově vznikajících aplikací v průmyslové automatizaci, chytrých sítích, finančních službách a distribuci multimédií vyžaduje vysoce přesné a spolehlivé časové reference. Tradiční přístupy, jako jsou přijímače [GNSS](/mobilnisite/slovnik/gnss/) v každém zařízení, jsou drahé, energeticky náročné a nespolehlivé v prostředích uvnitř budov nebo městských kaňonech. ASTI poskytuje alternativu, která využívá inherentní časové schopnosti buněčné sítě.

Vytvoření ASTI bylo motivováno několika průmyslovými trendy, včetně Průmyslu 4.0, modernizace chytrých sítí a rozšíření aplikací citlivých na čas v sítích. V průmyslových prostředích potřebují stroje a roboti přesnou koordinaci pro synchronizované operace. Ochranné systémy energetických sítí vyžadují synchronizaci na mikrosekundové úrovni pro detekci a izolaci poruch. Platformy pro finanční obchodování potřebují přesná časová razítka pro řazení transakcí. Předchozí buněčné systémy nemohly poskytnout požadovanou časovou přesnost prostřednictvím rádiového rozhraní, což nutilo podniky nasazovat vedle svých buněčných sítí samostatnou časovou infrastrukturu.

ASTI řeší omezení předchozích přístupů integrací přesné distribuce času do zásobníku protokolů buněčné sítě. Odstraňuje potřebu dodatečného hardwaru na straně UE, snižuje náklady na nasazení a zlepšuje spolehlivost prostřednictvím síťové redundance. Systém také řeší bezpečnostní obavy poskytováním ověřených časových informací chráněných proti útokům typu spoofing a manipulaci. Tím, že z přesného časování činí nativní službu buněčné sítě, ASTI umožňuje nové obchodní modely a aplikace, které byly dříve nepraktické nebo příliš drahé pro nasazení ve velkém měřítku.

## Klíčové vlastnosti

- Distribuuje přesné časové informace prostřednictvím buněčného rádiového rozhraní s přesností na submikrosekundové úrovni
- Podporuje jak vysílací (broadcast), tak i individuální (unicast) režimy doručování časových informací
- Zahrnuje kompenzační mechanismy pro zpoždění šíření za účelem zlepšení přesnosti
- Poskytuje indikátory kvality časování a schopnosti detekce chyb
- Integruje se se stávajícími protokoly 3GPP včetně RRC a systémových informací
- Podporuje více úrovní přesnosti od nanosekund po milisekundy na základě požadavků aplikace

## Definující specifikace

- **TR 28.839** (Rel-18) — Technical Report
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.565** (Rel-19) — Time Synchronization Function Services
- **TS 32.282** (Rel-18) — Charging management; Time Sensitive Networking

---

📖 **Anglický originál a plná specifikace:** [ASTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/asti/)
