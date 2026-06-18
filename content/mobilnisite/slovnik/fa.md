---
slug: "fa"
url: "/mobilnisite/slovnik/fa/"
type: "slovnik"
title: "FA – Flexible Alerting"
date: 2026-01-01
abbr: "FA"
fullName: "Flexible Alerting"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fa/"
summary: "Flexible Alerting (FA) je doplňková služba, která umožňuje, aby jeden příchozí hovor vyvolal upozornění na více terminálech nebo uživatelských identitách současně nebo postupně. Je klíčová pro firemní"
---

FA (Flexible Alerting) je doplňková služba, která umožňuje, aby jeden příchozí hovor vyvolal upozornění na více terminálech nebo uživatelských identitách současně nebo postupně.

## Popis

Flexible Alerting (FA) je sofistikovaná doplňková služba definovaná v rámci standardů 3GPP, navržená pro správu distribuce hovorů do předem definované skupiny cílů. Služba funguje tak, že spojuje jednu veřejnou uživatelskou identitu, známou jako Flexible Alerting Group Number (FAGN), s více identitami účastníků nebo terminály, označovanými jako Alerting Addresses. Když je uskutečněn hovor na FAGN, síť zahájí upozorňovací procedury na těchto adresách na základě nakonfigurovaného režimu upozornění. Klíčovým architektonickým prvkem umožňujícím FA je Flexible Alerting Server (FAS), typicky integrovaný v rámci IP Multimedia Subsystem (IMS) nebo v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v okruhově přepínaných doménách. Tento server spravuje data účastníka FA, včetně seznamu Alerting Addresses a servisní logiky pro obsluhu hovorů.

Služba podporuje několik klíčových provozních režimů. V režimu současného upozornění se síť pokouší upozornit všechny nakonfigurované terminály současně. První terminál, který zvedne, hovor přijme a upozorňování pro ostatní se ukončí. V režimu postupného upozornění síť upozorňuje cíle jeden po druhém podle předem definovaného pořadí a časování a pokračuje k dalšímu pouze v případě, že je aktuální obsazený nebo neodpovídá. Servisní logika také řeší scénáře jako přesměrování hovoru při obsazení nebo při neodpovědi, které mohou být integrovány s procedurami FA. Dále služba FA interaguje s dalšími síťovými funkcemi pro správu předplatitelských dat, účtování a procedury mobility, aby zajistila bezproblémový provoz při pohybu uživatelů.

Z pohledu signalizace FA zahrnuje specifické protokoly a procedury. V IMS využívají zahájení a ukončení relace pro skupiny FA metody [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), přičemž FAS funguje jako aplikační SIP server. Přijímá počáteční požadavek INVITE určený pro FAGN, rozšíří skupinu a rozdělí (fork) požadavek registrovaným kontaktům pro Alerting Addresses. V legacy okruhově přepínaných sítích používá MSC protokoly [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) a [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) pro správu sestavení hovoru a načítání dat účastníka. Generují se záznamy pro účtování, aby bylo možné účtovat skupinový hovor, často se specifickými tarify. Úlohou služby je skrýt před volajícím složitost skupinové komunikace a poskytnout jednoduché kontaktní číslo s jedním bodem, které dynamicky spojí s nejvhodnějším členem skupiny, čímž optimalizuje úspěšnost dokončení hovoru a uživatelský zážitek.

## K čemu slouží

Flexible Alerting byl vytvořen, aby řešil kritickou podnikovou potřebu efektivní skupinové a týmové komunikace. Před jeho standardizací vyžadovalo spojení s konkrétním oddělením nebo pohotovostním týmem buď manuálního operátora, primitivní loveckou skupinu (hunt group) na ústředně [PBX](/mobilnisite/slovnik/pbx/), nebo jednotlivé hovory na každého člena – procesy, které byly pomalé, nespolehlivé a zvyšovaly pravděpodobnost zmeškání důležitých hovorů. FA to řeší automatizací distribuce hovorů a zajišťuje, že příchozí hovor na sdílené číslo spolehlivě dojde k dostupné osobě.

Historický kontext spočívá ve vývoji telekomunikačních služeb od základního hlasu k službám inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a později k službám založeným na IMS. FA, zavedená ve 3GPP Release 4, byla součástí sady standardizovaných doplňkových služeb navržených k poskytnutí funkční parity a vylepšení oproti starším službám IN v nové architektuře jádra sítě typu all-IP. Řešila omezení statických loveckých skupin tím, že nabízela dynamičtější, účastníkem konfigurovatelné vzorce upozorňování a bezproblémově se integrovala s mobilitou mobilních uživatelů a multimediálními schopnostmi.

K jejímu vytvoření motivovala poptávka po provozní efektivitě v podnicích, záchranných službách a zákaznických podpůrných centrech. Tím, že garantuje, že hovor na servisní číslo bude přijat, zvyšuje spokojenost zákazníků a vnitřní koordinaci. Technologie řeší problém sdružování zdrojů, což umožňuje skupině sdílet zátěž příchozí komunikace bez nutnosti vyhrazeného dispečera, čímž optimalizuje lidské zdroje a snižuje míru opuštění hovorů.

## Klíčové vlastnosti

- Podporuje současné upozornění všech členů skupiny pro nejrychlejší odpověď
- Podporuje postupné upozornění na základě konfigurovatelného pořadí a časovačů
- Spravována prostřednictvím jedné veřejné identity (Flexible Alerting Group Number – FAGN)
- Integruje se s doplňkovými službami přesměrování hovorů (CFB, CFNRy)
- Poskytuje podrobné záznamy pro účtování událostí skupinového hovoru
- Funguje jak v okruhově přepínaných (na bázi MSC), tak paketově přepínaných (na bázi IMS) doménách

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TR 22.899** (Rel-14) — Study on Enhanced User Location Reporting
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.239** (Rel-19) — Flexible Alerting Protocol for IMS
- **TS 24.304** (Rel-19) — MIPv4 FA Mode Mobility Management in EPC
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.279** (Rel-19) — MIPv4 Mobility Protocol over S2a
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [FA na 3GPP Explorer](https://3gpp-explorer.com/glossary/fa/)
