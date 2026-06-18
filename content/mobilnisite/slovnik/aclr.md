---
slug: "aclr"
url: "/mobilnisite/slovnik/aclr/"
type: "slovnik"
title: "ACLR – Adjacent Channel Leakage Power Ratio"
date: 2025-01-01
abbr: "ACLR"
fullName: "Adjacent Channel Leakage Power Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aclr/"
summary: "ACLR měří poměr vysílaného výkonu v přiděleném kanálu k výkonu, který uniká do sousedních kanálů. Jde o klíčový parametr výkonu vysílače, který zajišťuje, aby signál jednoho uživatele nerušil sousední"
---

ACLR je poměr vysílaného výkonu v přiděleném kanálu k výkonu, který uniká do sousedních kanálů. Jde o klíčový parametr vysílače pro prevenci rušení a udržení kvality sítě.

## Popis

Adjacent Channel Leakage Power Ratio (ACLR, poměr výkonu úniku do sousedního kanálu) je základním parametrem výkonu vysílače v bezdrátových systémech 3GPP, který kvantifikuje, kolik výkonu z vysílaného signálu uniká do frekvenčně sousedících kanálů. Je definován jako poměr filtrovaného středního výkonu vystředěného na frekvenci přiděleného kanálu k filtrovanému střednímu výkonu vystředěnému na frekvenci sousedního kanálu. Měření se provádí pomocí měřicího filtru, který odpovídá charakteristikám přijímacího filtru v sousedním kanálu, což zajišťuje realistické posouzení potenciálního rušení.

Měření ACLR zahrnuje sofistikované techniky zpracování signálu, kdy je vysílaný signál nejprve převeden na nižší frekvenci a filtrován pomocí specifických měřicích šířek pásma definovaných standardem. Pro systémy [WCDMA](/mobilnisite/slovnik/wcdma/) je měřicí šířka pásma typicky 3,84 MHz, zatímco pro LTE se liší v závislosti na šířce kanálu (1,4 MHz až 20 MHz). Výkon se měří jak v hlavním kanálu, tak v sousedních kanálech, přičemž poměr je vyjádřen v decibelech (dB). Vyšší hodnoty ACLR znamenají lepší výkon vysílače, tedy menší rušení sousedních kanálů.

Tento parametr je klíčový, protože reálné vysílače nemohou dosáhnout dokonalého spektrálního omezení kvůli nelinearitám ve výkonových zesilovačích, nedokonalostem modulátoru a omezením převodníků z digitálního na analogový signál. Tyto nedokonalosti způsobují spektrální obnovu, která přesahuje přidělenou šířku pásma. Specifikace ACLR se liší v závislosti na technologii radiového přístupu ([UTRA](/mobilnisite/slovnik/utra/), [E-UTRA](/mobilnisite/slovnik/e-utra/), NR), frekvenčním pásmu a výkonové třídě zařízení. Základnové stanice mají zpravidla přísnější požadavky na ACLR než uživatelská zařízení kvůli jejich vyššímu vysílacímu výkonu a většímu potenciálu způsobit rušení.

Při nasazení sítě ACLR přímo ovlivňuje kapacitu systému a kvalitu služeb. Špatný výkon ACLR vede k rušení sousedního kanálu, což snižuje poměr signálu k šumu a rušení ([SINR](/mobilnisite/slovnik/sinr/)) pro uživatele v sousedních kanálech. Toto rušení je obzvláště problematické v systémech s frekvenčním duplexem ([FDD](/mobilnisite/slovnik/fdd/)), kde se vysílání v uplinku a downlinku uskutečňuje současně v sousedních frekvenčních blocích. Specifikace 3GPP definují požadavky na ACLR jak pro vedené, tak pro zářené měření, s testovacími metodikami specifikovanými v dokumentech pro testování shody, aby byla zajištěna interoperabilita mezi zařízeními různých výrobců.

Moderní systémy implementují různé techniky pro zlepšení výkonu ACLR, včetně digitálního předkompenzačního zkreslení, redukce činitele špičkovosti a pokročilé linearizace výkonového zesilovače. Tyto techniky pomáhají splnit stále přísnější požadavky na ACLR v novějších vydáních standardů při zachování účinnosti výkonového zesilovače. Vývoj od 3G k 5G přinesl složitější požadavky na ACLR se zavedením agregace nosných, doplňkového uplinku a dynamického sdílení spektra, což vyžaduje sofistikovanější metodiky měření a ověřování shody.

## K čemu slouží

ACLR byl zaveden, aby řešil základní problém spektrální účinnosti v celulárních sítích. Jak se bezdrátové systémy vyvíjely, aby podporovaly více uživatelů a vyšší datové rychlosti v rámci omezených přidělení spektra, stala se kontrola rušení mezi sousedními kanály klíčovou. Bez specifikací ACLR by vysílače jednoho operátora mohly rušit přijímače jiného operátora pracujícího v sousedních frekvenčních pásmech, což by snižovalo celkovou kapacitu sítě a degradovalo uživatelský zážitek.

Vytvoření metriky ACLR bylo motivováno přechodem z analogových na digitální celulární systémy, kde více uživatelů sdílí sousední frekvenční kanály. V raných celulárních systémech byly ochranná pásma mezi kanály široká, aby se zabránilo rušení, ale tento přístup plýtval cenným spektrem. ACLR umožnil zúžení ochranných pásem tím, že zajistil kontrolu a kvantifikaci nedokonalostí vysílače. To umožnilo efektivnější využití spektra při zachování přijatelné úrovně rušení mezi sousedními kanály.

ACLR řeší technickou výzvu nelineárního chování vysílače, zejména ve výkonových zesilovačích pracujících blízko saturace kvůli účinnosti. Tyto nelinearity způsobují spektrální obnovu, která přesahuje přidělenou šířku pásma kanálu. Stanovením standardizovaných požadavků na ACLR zajišťuje 3GPP interoperabilitu mezi zařízeními různých výrobců a zároveň optimalizuje kompromis mezi účinností vysílače a spektrální čistotou. Tato rovnováha je zásadní pro komerční nasazení, kde jsou kritickými faktory jak výkon sítě, tak výdrž baterie zařízení.

## Klíčové vlastnosti

- Kvantifikuje spektrální únik vysílače do sousedních kanálů
- Používá měřicí filtry odpovídající charakteristikám přijímače
- Specifikováno pro vedená i zářená měření
- Liší se podle technologie radiového přístupu a frekvenčního pásma
- Klíčové pro správu rušení v systémech FDD
- Ovlivňuje kapacitu sítě a spektrální účinnost

## Související pojmy

- [ACP – Accelerated H.245 Procedures](/mobilnisite/slovnik/acp/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [SEM – Spectrum Emissions Mask](/mobilnisite/slovnik/sem/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.942** (Rel-19) — UTRA RF System Scenarios Specification
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- … a dalších 66 specifikací

---

📖 **Anglický originál a plná specifikace:** [ACLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/aclr/)
