---
slug: "ts"
url: "/mobilnisite/slovnik/ts/"
type: "slovnik"
title: "TS – Technical Specification"
date: 2025-01-01
abbr: "TS"
fullName: "Technical Specification"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ts/"
summary: "Technická specifikace (TS) je formální, podrobný dokument publikovaný konsorciem 3GPP, který definuje standardy pro systémy mobilní telekomunikace. Specifikuje protokoly, rozhraní, funkce a testovací"
---

TS je formální dokument 3GPP, který definuje standardy pro mobilní sítě, specifikuje protokoly, rozhraní a požadavky pro zajištění globální interoperability od GSM po 5G.

## Popis

Technická specifikace (TS) 3GPP je základním výstupem a stavebním kamenem celého procesu standardizace 3GPP. Jedná se o komplexní, samostatný dokument, který formálně specifikuje konkrétní aspekt mobilního systému. Na rozdíl od technické zprávy (TR), která je informativní, je TS normativní, což znamená, že definuje standardy, které musí výrobci zařízení a operátoři sítí implementovat, aby dosáhli shody a interoperability. Každé TS je přiděleno jedinečné číslo řady (např. 23.501, 38.300), které označuje pracovní skupinu a tematickou oblast.

Struktura TS je vysoce systematická. Typicky zahrnuje rozsah, odkazy, definice, symboly a zkratky, následované podrobnými technickými klauzulemi. Tyto klauzule vyčerpávajícím způsobem popisují architektonické prvky, protokolové zásobníky, formáty zpráv, informační elementy, procedury (např. připojení, předání hovoru, paging), stavové automaty a požadavky na výkon. Například TS 38.300 specifikuje celkovou architekturu a procedury NR a NG-RAN, zatímco TS 38.331 detailně popisuje protokol NR Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Specifikace jsou vrstvené a pokrývají Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), Access Stratum ([AS](/mobilnisite/slovnik/as/)) a fyzickou vrstvu, čímž zajišťují kompletní definici od jádra sítě až po rozhraní rádiového přenosu.

V praxi inženýři používají TS jako konečnou referenci pro návrh čipových sad, vývoj softwaru protokolových zásobníků, plánování sítí a provádění testů shody. Tyto specifikace jsou živé dokumenty, které jsou průběžně aktualizovány prostřednictvím žádostí o změnu ([CR](/mobilnisite/slovnik/cr/)) na zasedáních 3GPP. Jejich tvorba zahrnuje důslednou technickou diskusi, simulace a validaci, aby bylo zajištěno, že splňují systémové požadavky na výkon, bezpečnost a zpětnou kompatibilitu. Zdraví celého ekosystému závisí na přesnosti a jasnosti těchto dokumentů, protože umožňují různým dodavatelům vyrábět interoperabilní síťové prvky a uživatelská zařízení, čímž vytvářejí jednotný globální trh.

## K čemu slouží

Účelem technických specifikací 3GPP je vytvořit jediný, globálně přijímaný technický standard pro systémy mobilní komunikace. To je klíčové pro řešení základního problému interoperability. Bez takových specifikací by každý region nebo dodavatel mohl vyvíjet nekompatibilní technologie, což by vedlo k fragmentaci trhu, vyšším nákladům a špatné uživatelské zkušenosti (např. telefony fungující pouze v jedné zemi). Systém TS poskytuje "pravidla silničního provozu", která umožňují zařízení od libovolného výrobce připojit se k jakékoli kompatibilní síti na celém světě.

Historicky se potřeba takových specifikací jasně projevila při přechodu z analogových (1G) na digitální (2G GSM) systémy. Úspěch GSM, definovaného komplexní sadou specifikací [ETSI](/mobilnisite/slovnik/etsi/) (předchůdce modelu 3GPP TS), demonstroval sílu otevřených standardů založených na konsenzu. Jak se technologie vyvíjela přes 3G UMTS, 4G LTE až po současné 5G NR, rozsah a složitost specifikací prudce vzrostly, aby pokryly nové služby, vyšší přenosové rychlosti, nižší latence a širokou škálu případů užití. Rámec TS řeší omezení proprietárních systémů tím, že podporuje inovace prostřednictvím soutěže v implementaci, nikoli v základních komunikačních protokolech, a zajišťuje tak stabilní základnu, na které může celý průmysl stavět.

## Klíčové vlastnosti

- Normativní dokument definující povinné a volitelné požadavky pro implementaci
- Pokrývá všechny vrstvy systému: architekturu, protokoly, rozhraní a procedury
- Jednoznačně identifikován číslem řady (např. 23.- pro SA2, 38.- pro RAN WG)
- Pravidelně aktualizován prostřednictvím řízeného procesu žádostí o změnu (CR)
- Poskytuje základ pro testy shody a interoperability (např. organizacemi GCF/PTCRB)
- Zajišťuje globální interoperabilitu a úspory z rozsahu v celém průmyslu

## Související pojmy

- [TR – UE delay in receiving direction](/mobilnisite/slovnik/tr/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [TS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ts/)
