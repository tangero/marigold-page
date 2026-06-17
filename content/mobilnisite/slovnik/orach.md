---
slug: "orach"
url: "/mobilnisite/slovnik/orach/"
type: "slovnik"
title: "ORACH – ODMA Random Access Channel"
date: 2025-01-01
abbr: "ORACH"
fullName: "ODMA Random Access Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/orach/"
summary: "Fyzický kanál v konceptu ODMA (Opportunity Driven Multiple Access) pro UTRA TDD, který mobilní stanice používají k zahájení komunikace odesláním náhodných přístupových burstů. Umožňuje decentralizovan"
---

ORACH je ODMA Random Access Channel v UTRA TDD, který mobilní stanice používají k zahájení decentralizované, ad-hoc komunikace typu peer-to-peer odesíláním náhodných přístupových burstů.

## Popis

[ODMA](/mobilnisite/slovnik/odma/) Random Access Channel (ORACH) je specifický typ kanálu definovaný ve specifikacích 3GPP pro režim UTRA TDD (Time Division Duplex) v rámci konceptu Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/) (ODMA). ODMA byl koncept zkoumající ad-hoc vícekaskádové přenosy v sítích UMTS. ORACH slouží jako primární kanál pro mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) k zahájení přenosové žádosti nebo navázání spojení v ODMA buňce nebo ve scénáři peer-to-peer přenosu. Funguje na fyzické vrstvě, využívaje definované časové sloty a kódy v rámci struktury TDD rámce.

V architektuře UTRA TDD je fyzická vrstva rozdělena na rámce a časové sloty. ORACH je v této struktuře alokován. Když potřebuje MS komunikovat – například k vyžádání přenosového spojení k jiné MS nebo k přístupu do sítě prostřednictvím peer zařízení – odešle na ORACH náhodný přístupový burst. Tento burst obsahuje preambulovou informaci a případně krátkou zprávu. Přenos je „náhodný“ v tom smyslu, že není předem naplánován sítí; MS si zvolí vhodný časový slot a kód na základě naslouchání kanálu (princip listen-before-talk), aby minimalizovala kolize. To je klíčové pro decentralizovanou povahu ODMA.

Fungování ORACH zahrnuje vícekrokový proces. MS nejprve monitoruje ORACH (a související kanály), aby vyhodnotila aktivitu. Poté vybere volnou přístupovou příležitost, definovanou konkrétním časovým slotem a kanalizačním kódem v rámci tohoto slotu. MS odešle svůj náhodný přístupový burst, který zahrnuje power ramping, aby umožnil přijímači detekovat začátek burstu. Přijímající entita – jiná MS fungující jako přenosový uzel nebo základnová stanice – tento burst detekuje a může na něj odpovědět, čímž zahájí navázání spojení. ORACH je úzce propojen s dalšími ODMA kanály, jako je ODMA Access Indicator Channel (OAICH), který poskytuje zpětnou vazbu o pokusu o přístup. Jeho úlohou je umožnit počáteční kontakt v dynamické, ad-hoc topologii sítě, což podporuje vizi ODMA o rozšíření pokrytí a kapacity prostřednictvím přenosů mezi uživatelskými zařízeními.

## K čemu slouží

ORACH byl vytvořen jako součást studijního bodu [ODMA](/mobilnisite/slovnik/odma/) a následných specifikací k řešení výzev v rozšíření pokrytí a zvýšení kapacity pro sítě UTRA TDD. Tradiční buněčný přístup spoléhá na přímé spojení mezi UE a pevnou základnovou stanicí, což omezuje pokrytí v odlehlých oblastech a může vytvářet kapacitní úzká místa. ODMA navrhlo používat jiná UE jako přenosové uzly k vytvoření vícekaskádových cest k síti. ORACH poskytuje základní mechanismus pro UE, aby spontánně zahájilo takovou žádost o přenosové spojení bez centralizované, plánované kontroly ze strany základnové stanice.

Historický kontext představuje zkoumání alternativních přístupových metod v 3GPP, zejména pro režim TDD. ODMA bylo zamýšleno pro scénáře jako vnitřní pokrytí nebo skupinová komunikace. Omezení předchozích přístupů byla potřeba, aby veškerý přístup koordinovala NodeB. ORACH to řeší tím, že umožňuje oportunistický, decentralizovaný přístup, což UE umožňuje vzájemně se objevovat a přímo se spojovat. To podpořilo výzkum peer-to-peer sítí v rámci buněčné architektury s cílem zlepšit využití zdrojů a uživatelský komfort v hustých nebo nerovnoměrně pokrytých prostředích.

## Klíčové vlastnosti

- Definován v rámci struktury rámce a časových slotů fyzické vrstvy UTRA TDD
- Používá se pro přenos náhodných přístupových burstů k zahájení komunikace
- Funguje na principu listen-before-talk k minimalizaci kolizí
- Podporuje power ramping v rámci burstu pro spolehlivou detekci
- Integruje se s kanálem ODMA Access Indicator Channel (OAICH) pro odezvu na přístup
- Umožňuje decentralizované, ad-hoc navázání spojení ve scénářích vícekaskádového přenosu ODMA

## Související pojmy

- [ODMA – Opportunity Driven Multiple Access](/mobilnisite/slovnik/odma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [ORACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/orach/)
