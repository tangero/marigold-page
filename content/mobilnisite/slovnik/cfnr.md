---
slug: "cfnr"
url: "/mobilnisite/slovnik/cfnr/"
type: "slovnik"
title: "CFNR – Communication Forwarding No Reply"
date: 2026-01-01
abbr: "CFNR"
fullName: "Communication Forwarding No Reply"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cfnr/"
summary: "Doplňková služba, která automaticky přesměruje příchozí hlasový nebo multimediální hovor na předem definované alternativní číslo, pokud volaná strana neodpoví. Jde o základní funkci správy hovorů pro"
---

CFNR je doplňková služba, která přesměruje nezodpovězený hlasový nebo multimediální hovor na předem definované alternativní číslo za účelem zvýšení úspěšnosti dokončení hovoru v mobilních sítích.

## Popis

Communication Forwarding No Reply (CFNR) je standardizovaná doplňková služba v rámci standardů 3GPP, která funguje v doméně IP Multimedia Subsystem (IMS) nebo v doméně přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)). Když je uskutečněn hovor na účastníka, který má aktivovanou službu CFNR, síť se normálně pokusí hovor zřídit. Pokud zařízení volané strany zvoní, ale hovor není v konfigurovatelném časovém intervalu (obvykle 15–30 sekund) přijat, síť zachytí tento pokus o spojení. Následně automaticky přesměruje signalizaci a média na jiné cílové číslo, známé jako forward-to číslo, které si účastník nastavil ve svém služebním profilu. Toto rozhodnutí o přesměrování a jeho provedení provádí síťové prvky, jako je Serving Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v IMS nebo Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v CS, které konzultují služební data účastníka uložená v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)).

Službu si účastník zřizuje, aktivuje, deaktivuje a dotazuje pomocí specifických procedur, často prostřednictvím kódů Unstructured Supplementary Service Data ([USSD](/mobilnisite/slovnik/ussd/)) nebo přes rozhraní pro správu služeb. Síť udržuje stav CFNR účastníka (aktivní/neaktivní) a přidružené forward-to číslo jako součást jeho účastnických dat. Klíčovým provozním aspektem je interakce s dalšími službami přesměrování hovorů, jako je Communication Forwarding Busy ([CFB](/mobilnisite/slovnik/cfb/)) a Communication Forwarding Unconditional ([CFU](/mobilnisite/slovnik/cfu/)). Tyto služby jsou typicky vyhodnocovány v určitém pořadí priority definovaném síťovým operátorem (např. nejprve CFU, poté CFB, poté CFNR), aby se určila konečná přesměrovací akce pro příchozí hovor.

Z pohledu signalizace, když je CFNR spuštěna, síť vygeneruje novou signalizaci pro zřízení hovoru (např. SIP INVITE v IMS nebo ISUP IAM v CS) směrem k forward-to číslu. Pro původního volajícího je tento proces obecně transparentní; jednoduše zaznamená, že se hovor po vypršení časového limitu pro neodpověď spojil na přesměrované místo určení. Služba je nedílnou součástí poskytování uživatelské kontroly nad dostupností komunikace a zajišťuje, že důležité hovory nejsou zmeškány, i když jsou uživatelé dočasně nedostupní pro odpověď na své primární zařízení. Její implementace musí zvládat různé scénáře, včetně přesměrování na mezinárodní čísla (podle pravidel operátora), interakcí se službami zákazu hovorů a udržování správných záznamů o účtování jak pro přesměrovanou část, tak pro původní pokus o hovor.

## K čemu slouží

CFNR byla vytvořena k řešení základního problému zmeškaných hovorů a neefektivní komunikace v telefonních sítích. Před existencí takových funkcí, pokud volaná strana neodpověděla, hovor prostě selhal, což potenciálně vyžadovalo opakované pokusy a způsobovalo zpoždění. To bylo obzvláště problematické v mobilním prostředí, kde uživatelé mohli být vzdáleni od svého telefonu, na schůzce nebo jinak neschopni okamžitě odpovědět. CFNR poskytuje mechanismus pro zajištění dokončení hovoru přesměrováním komunikačního pokusu na alternativní kontaktní místo, jako je hlasová schránka, sekretářka nebo jiné osobní zařízení.

Služba řeší omezení základního zřizování hovorů přidáním inteligence a uživatelsky konfigurovatelné logiky do sítě. Posiluje postavení účastníků tím, že jim dává přímou kontrolu nad tím, jak jsou jejich příchozí komunikace zpracovány během období nedostupnosti, a přesahuje tak jednoduchý binární model přijetí/nepřijetí hovoru. Historicky byly takové přesměrovací služby poprvé definovány ve sítích pevné linky a byly klíčové pro obchodní komunikaci. Jejich standardizace v 3GPP již od nejranějších vydání zajistila bezproblémovou kontinuitu služeb a konzistentní uživatelský zážitek při vývoji telefonie od přepojování okruhů v GSM k hlasu přes LTE (VoLTE) a 5G Voice založenému na přepojování paketů v IMS.

CFNR dále podporuje provozní efektivitu síťových operátorů. Standardizací chování umožňuje interoperabilitu mezi síťovými prvky různých výrobců a napříč sítěmi různých operátorů. Také vytváří základ pro pokročilejší, ziskové služby, jako je centralizovaná hlasová schránka nebo řešení inteligentního směrování hovorů. Služba řeší problém uživatelského zážitku ze zmeškaných spojení a zároveň poskytuje stavební kámen pro složité pracovní postupy zpracování hovorů.

## Klíčové vlastnosti

- Automatické přesměrování hovoru po neodpovědi po uplynutí konfigurovatelného časovače
- Zřízení a aktivace služby uživatelem prostřednictvím síťové signalizace (např. USSD)
- Uložení a správa cílového čísla pro přesměrování v profilu účastníka
- Definované přednostní pořadí a interakce s ostatními službami přesměrování hovorů (CFU, CFB)
- Provedení na straně sítě pomocí řídicích funkcí jádra sítě (MSC, S-CSCF)
- Podpora jak v doméně přepojování okruhů (CS), tak v IP Multimedia Subsystem (IMS)

## Související pojmy

- [CFB – Call Forwarding on mobile subscriber Busy](/mobilnisite/slovnik/cfb/)
- [CFU – Communication Forwarding Unconditional](/mobilnisite/slovnik/cfu/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.616** (Rel-19) — Malicious Call Identification (MCID) Protocol
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [CFNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfnr/)
