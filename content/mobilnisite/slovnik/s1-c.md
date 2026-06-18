---
slug: "s1-c"
url: "/mobilnisite/slovnik/s1-c/"
type: "slovnik"
title: "S1-C – S1 Control Plane"
date: 2025-01-01
abbr: "S1-C"
fullName: "S1 Control Plane"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s1-c/"
summary: "S1-C je rozhraní řídicí roviny mezi eNodeB (základnovou stanicí) a entitou Mobility Management Entity (MME) v sítích LTE/EPC. Přenáší signalizační zprávy pro funkce jako zřizování přenosových kanálů,"
---

S1-C je rozhraní řídicí roviny mezi eNodeB a entitou Mobility Management Entity v sítích LTE, přenášející signalizaci pro funkce jako zřizování přenosových kanálů (bearer) a předávání spojení (handover).

## Popis

Rozhraní S1-C je klíčovou součástí architektury Evolved Packet System (EPS), definovanou 3GPP jako spojení řídicí roviny mezi Evolved NodeB (eNodeB) v Evolved Universal Terrestrial Radio Access Network ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a entitou Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v Evolved Packet Core (EPC). Funguje nad IP transportní sítí, typicky využívá jako transportní protokol [SCTP](/mobilnisite/slovnik/sctp/) (Stream Control Transmission Protocol) k zajištění spolehlivé, spojově orientované signalizace s funkcemi jako multi-homing a multi-streaming, které zvyšují robustnost a výkon. Rozhraní využívá protokol S1 Application Protocol ([S1AP](/mobilnisite/slovnik/s1ap/)), který definuje signalizační procedury a zprávy vyměňované mezi eNodeB a MME.

Klíčové procedury řízené přes S1-C zahrnují počáteční připojení UE (Initial UE Attachment), kdy eNodeB přeposílá počáteční [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) zprávu UE k MME za účelem vytvoření kontextu; správu [E-RAB](/mobilnisite/slovnik/e-rab/) (Evolved Radio Access Bearer), kdy MME žádá o zřízení, modifikaci nebo uvolnění přenosových kanálů pro přenos uživatelských dat; přípravu a provedení předání spojení (Handover Preparation and Execution), umožňující plynulou mobilitu mezi eNodeB nebo k jiným 3GPP rádiovým přístupovým technologiím; a vyhledávání (Paging), kdy MME iniciuje žádosti o vyhledání pro lokalizaci UE v režimu nečinnosti (idle mode). Rozhraní také podporuje funkce jako přenos NAS (NAS Transport), který transparentně přenáší signalizaci vyšší vrstvy mezi UE a MME skrze eNodeB, a vyrovnávání zatížení (Load Balancing), kdy MME může nasměrovat eNodeB k redistribuci UE pro optimální výkon sítě.

Architektonicky je S1-C logické bod-bod rozhraní, což znamená, že každé eNodeB má vyhrazené S1-C spojení k jedné nebo více MME pro redundanci a sdílení zátěže, což umožňuje funkce S1-flex. To dovoluje, aby bylo eNodeB připojeno k více MME v oblasti poolu, čímž se zvyšuje spolehlivost a škálovatelnost sítě. Rozhraní je navrženo odděleně od uživatelské roviny (kterou zajišťuje [S1-U](/mobilnisite/slovnik/s1-u/)), v souladu s principem oddělení řídicí a uživatelské roviny (CUPS), což zjednodušuje vývoj sítě a umožňuje nezávislé škálování prostředků pro zpracování signalizace a dat. V provozu je signalizace S1-C klíčová pro udržování stavů mobility UE, správu kontextů relací a zajišťování kvality služby (QoS) koordinací rádiových a jádrových síťových prostředků, což z ní činí základní prvek plně IP, ploché architektury LTE, která ve srovnání s předchozími 3G systémy snižuje latenci a zvyšuje efektivitu.

## K čemu slouží

Rozhraní S1-C bylo zavedeno ve 3GPP Release 8 jako součást standardizace LTE/EPC, aby řešilo omezení dřívějších 3GPP architektur, jako je UMTS, které používaly hierarchičtější a složitější rozhraní jako Iu-CS a Iu-PS mezi Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a jádrem sítě. V UMTS byly funkce řídicí a uživatelské roviny často propleteny, což vedlo k problémům se škálovatelností a vyšší latencí. S1-C bylo vytvořeno pro umožnění plošší síťové architektury přímým propojením základnové stanice (eNodeB) s řídicí entitou jádra sítě (MME), čímž odpadla potřeba mezilehlého RNC. Tento návrh snižuje signalizační režii, zkracuje délku cest pro řídicí zprávy a podporuje rychlejší předávání spojení a správu relací, což je kritické pro vysokorychlostní datové služby a aplikace v reálném čase jako VoIP a video streamování.

Historicky vycházela motivace pro S1-C z potřeby podporovat plně IP sítě a uspokojit rostoucí požadavky na mobilní broadband, poháněné nástupem chytrých telefonů a datově náročných aplikací. Oddělením řídicí roviny (S1-C) od uživatelské roviny (S1-U) umožnilo 3GPP nezávislý vývoj a optimalizaci signalizace a přenosu dat. Například toto oddělení umožňuje funkce jako sdílení sítě a flexibilní scénáře nasazení, kde řídicí funkce mohou být centralizovány, zatímco funkce uživatelské roviny jsou distribuovány. Rozhraní také usnadňuje zavádění nových služeb a technologií, jako je LTE-Advanced a později propojení s 5G, tím, že poskytuje stabilní signalizační základnu, kterou lze rozšiřovat bez nutnosti přestavby celé síťové architektury.

Dále S1-C řeší problémy související se spolehlivostí a efektivitou sítě prostřednictvím mechanismů jako S1-flex a MME pooling, které distribuují řídicí provoz přes více MME, aby se předešlo jediným bodům selhání a vyrovnalo zatížení. To byl významný pokrok oproti předchozím systémům, kde selhání uzlu mohlo vést k rozsáhlému přerušení služeb. Standardizací S1-C napříč releasy zajistilo 3GPP zpětnou kompatibilitu a hladké migrační cesty, což operátorům umožnilo postupně nasazovat LTE sítě při zachování interoperability s legacy 3GPP systémy. Celkově je účelem S1-C poskytnout robustní, škálovatelné a nízkolatenční rozhraní řídicí roviny, které tvoří operační inteligenci sítí LTE a umožňuje pokročilé řízení mobility, zabezpečení a možnosti QoS.

## Klíčové vlastnosti

- Používá SCTP pro spolehlivý, spojově orientovaný přenos signalizace
- Podporuje protokol S1 Application Protocol (S1AP) pro výměnu zpráv mezi eNodeB a MME
- Umožňuje správu E-RAB pro zřizování, modifikaci a uvolňování přenosových kanálů
- Usnadňuje procedury předání spojení (handover), včetně mezi eNodeB a mezi různými RAT
- Poskytuje přenos NAS pro signalizaci mezi UE a MME prostřednictvím eNodeB
- Podporuje S1-flex pro připojení k více MME pro redundanci

## Související pojmy

- [S1-MME – S1 Control Plane Interface to the Mobility Management Entity](/mobilnisite/slovnik/s1-mme/)
- [S1-U – S1 User Plane Interface](/mobilnisite/slovnik/s1-u/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [S1AP – S1 Application Protocol](/mobilnisite/slovnik/s1ap/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [S1-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/s1-c/)
