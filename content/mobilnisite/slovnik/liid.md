---
slug: "liid"
url: "/mobilnisite/slovnik/liid/"
type: "slovnik"
title: "LIID – Lawful Interception Identifier"
date: 2025-01-01
abbr: "LIID"
fullName: "Lawful Interception Identifier"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/liid/"
summary: "Jedinečný identifikátor přiřazený cíli (např. účastníkovi, IP adrese) pro účely zákonného odposlechu. Umožňuje orgánům činným v trestním řízení jednoznačně a nepřijatelně požadovat odposlech specifick"
---

LIID je jedinečný identifikátor přiřazený cíli, jako je účastník nebo IP adresa, který umožňuje orgánům činným v trestním řízení jednoznačně požadovat a auditovat odposlech specifických komunikací od síťového operátora.

## Popis

Lawful Interception Identifier (LIID) je klíčový parametr v architektuře zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) podle 3GPP, definovaný ve specifikacích rozhraní Handover Interface ([HI](/mobilnisite/slovnik/hi/)). Slouží jako jedinečný a trvalý odkaz na konkrétní úlohu odposlechu nebo cíl v doméně síťového operátora. Když orgán činný v trestním řízení ([LEA](/mobilnisite/slovnik/lea/)) vydá příkaz k zákonnému odposlechu, obsahuje LIID, který je následně používán ve veškeré komunikaci mezi monitorovacím zařízením ([MF](/mobilnisite/slovnik/mf/)) LEA a správní funkcí ([ADMF](/mobilnisite/slovnik/admf/)) a doručovacími funkcemi ([DF](/mobilnisite/slovnik/df/)) síťového operátora. LIID je generován LEA nebo síťovým operátorem (dle národních předpisů) a je zahrnut v každé zprávě o informacích souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)) odeslané LEA. To umožňuje LEA korelovat všechna odposlechnutá data – metadata hovorů, podrobnosti SMS, informace o IP sezeních a samotný hlasový/datový obsah – s původním příkazem a konkrétním cílem. Technicky je LIID přenášen v rámci standardizovaných rozhraní HI2 a HI3 pomocí protokolů jako X.500/X.509 a IP transportu. Jeho přítomnost zajišťuje, že i když cíl během období odposlechu změní svůj IMSI, MSISDN nebo IP adresu, všechna odposlechnutá data mohou být stále správně přiřazena ke stejnému příkazu a instanci cíle, čímž se zachovává integrita a kontinuita odposlechové operace.

## K čemu slouží

LIID byl zaveden, aby řešil významné provozní výzvy v systémech zákonného odposlechu před 3GPP Release 8. Dřívější implementace se často spoléhaly výhradně na dynamické identifikátory, jako je IMSI nebo MSISDN, k identifikaci cíle v rámci odposlechových hlášení. Tyto identifikátory se však mohou změnit (např. výměna SIM karty, přenos čísla) nebo být dočasně nedostupné, což způsobuje chybné přiřazení nebo ztrátu odposlechnutých dat a může ohrozit vyšetřování. Dále, bez jedinečného identifikátoru specifického pro příkaz bylo pro orgány činné v trestním řízení obtížné spravovat více souběžných odposlechů pro stejný cíl pod různými příkazy nebo přesně auditovat, která data patří ke kterému právnímu pověření. LIID tyto problémy řeší tím, že poskytuje stabilní identifikátor na úrovni příkazu, který přetrvává po dobu trvání příkazu k odposlechu, nezávisle na síťových identifikátorech cíle. To bylo motivováno rostoucí složitostí telekomunikací, včetně nárůstu IP služeb (VoIP, messagingové aplikace) a uživatelů s více zařízeními, což činilo sledování cílů pouze na základě tradičních identifikátorů nedostatečným. LIID tak zvyšuje přesnost, spolehlivost a právní obhajitelnost operací zákonného odposlechu v moderních sítích.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní příkaz k zákonnému odposlechu a cíl v systému operátora
- Přetrvává po dobu trvání příkazu k odposlechu, nezávisle na změnách identifikátorů účastníka
- Je zahrnut ve všech hlášeních o informacích souvisejících s odposlechem (IRI) a obsahu komunikace (CC)
- Zajišťuje korelaci všech odposlechnutých dat napříč více relacemi a typy komunikace
- Podporuje auditní stopy propojením odposlechnutých dat s konkrétním právním pověřením
- Usnadňuje zpracování více souběžných odposlechů pro stejný cíl

## Související pojmy

- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)
- [DF2 – Delivery Function 2](/mobilnisite/slovnik/df2/)
- [DF3 – Delivery Function 3](/mobilnisite/slovnik/df3/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [HI2 – Handover Interface Port 2](/mobilnisite/slovnik/hi2/)
- [HI3 – Handover Interface Port 3](/mobilnisite/slovnik/hi3/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [LIID na 3GPP Explorer](https://3gpp-explorer.com/glossary/liid/)
