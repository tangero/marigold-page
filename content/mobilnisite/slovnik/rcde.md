---
slug: "rcde"
url: "/mobilnisite/slovnik/rcde/"
type: "slovnik"
title: "RCDE – Relative Code Domain Error"
date: 2025-01-01
abbr: "RCDE"
fullName: "Relative Code Domain Error"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rcde/"
summary: "Klíčový parametr výkonu v systémech WCDMA a TD-SCDMA, který měří přesnost výkonu přenášeného signálu v kódové doméně. Kvantifikuje odchylky od ideálního rozprostíracího kódu, které souvisejí s interfe"
---

RCDE je klíčový parametr výkonu v systémech WCDMA a TD-SCDMA, který měří přesnost výkonu přenášeného signálu v kódové doméně tím, že kvantifikuje odchylky od ideálního rozprostíracího kódu.

## Popis

Relative Code Domain Error (RCDE, relativní chyba kódové domény) je základní měřicí parametr definovaný ve specifikacích 3GPP pro rádiové technologie Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)) a Time Division-Synchronous [CDMA](/mobilnisite/slovnik/cdma/) ([TD-SCDMA](/mobilnisite/slovnik/td-scdma/)). Hodnotí přesnost přenášeného signálu v kódové doméně, což je zásadní v CDMA systémech, kde jsou vícekanály odděleny ortogonálními rozprostíracími kódy. Konkrétně RCDE měří odchylku skutečně vysílaného výkonu v každém kódovém kanálu od zamýšlené úrovně výkonu, a to relativně k celkovému vysílanému výkonu. Vyjadřuje se jako poměr, typicky v decibelech (dB), který porovnává velikost chybového vektoru v kódové doméně s výkonem referenčního signálu. V praxi se RCDE vyhodnocuje při testování vysílače, zejména u uživatelského zařízení (UE) a Node B, aby byla zajištěna kvalita signálu. Měření zahrnuje analýzu vysílaného signálu po desprezování s přiřazenými ortogonálními kódy s proměnným rozprostíracím faktorem ([OVSF](/mobilnisite/slovnik/ovsf/)); jakékoli neortogonální složky nebo nerovnováhy výkonu se projeví jako chyby. Vysoké hodnoty RCDE ukazují na nízkou integritu signálu, což může vést ke zvýšené interferenci, snížené kapacitě a zhoršenému výkonu přijímače na základnové stanici. Metodika testování je podrobně popsána v dokumentech 3GPP TS 25.141 (konformita základnových stanic) a TS 25.142 (konformita UE), kde se RCDE měří za různých podmínek, jako jsou různé úrovně výkonu a frekvenční posuvy. Funguje tak, že porovnává přijaté výkony kódových kanálů s jejich očekávanými hodnotami a zohledňuje zkreslení z nelinearit zesilovačů, deformací filtrů a fázového šumu. RCDE úzce souvisí s dalšími parametry, jako je Error Vector Magnitude ([EVM](/mobilnisite/slovnik/evm/)), ale je specifický pro multiplexování v kódové doméně u CDMA. Jeho role je kritická pro operátory sítí a výrobce při ověřování výkonu zařízení, optimalizaci rádiových parametrů a udržování celkové kvality systému, zejména v hustých nasazeních, kde je ortogonalita kódů zásadní pro minimalizaci vnitrobuněčné interference.

## K čemu slouží

RCDE bylo zavedeno, aby vyhovělo přísným požadavkům [CDMA](/mobilnisite/slovnik/cdma/) systémů 3. generace, ve kterých více uživatelů sdílí stejné frekvenční pásmo prostřednictvím ortogonálních kódů. V takových systémech jakákoli nepřesnost při vysílání přesných výkonů kódových kanálů narušuje ortogonalitu, což způsobuje interferenci, která přímo snižuje kapacitu sítě a kvalitu hovorů. Před jeho standardizací existovala potřeba jednotného parametru pro kvantifikaci těchto zkreslení vysílače během vývoje a testování konformity. Zavedení RCDE vyřešilo problém nekonzistentního hodnocení kvality signálu mezi různými výrobci a zařízeními a zajistilo interoperabilitu a spolehlivý výkon v živých sítích. Je důležité, protože i malé chyby ve výkonu v kódové doméně mohou významně ovlivnit poměr signálu k interferenci, což vede k přerušeným hovorům nebo nižším přenosovým rychlostem. Historicky, jak se [WCDMA](/mobilnisite/slovnik/wcdma/) vyvíjelo z dřívějších CDMA technologií, zvýšené přenosové rychlosti a složité modulace vyžadovaly přísnější kontrolu charakteristik vysílače. RCDE poskytlo standardizovaný způsob, jak tyto chyby měřit a omezovat, což umožnilo výrobcům navrhovat kompatibilní hardware a operátorům nasazovat sítě s předvídatelným výkonem. Také podporuje optimalizaci sítě tím, že identifikuje vadná zařízení nebo neoptimální konfigurace, které degradují rozhraní vzduchu. Bez RCDE by bylo obtížné udržovat vysokou spektrální účinnost a uživatelský komfort slibovaný technologií 3G, protože řízení interference by bylo méně přesné.

## Klíčové vlastnosti

- Měří přesnost výkonu v kódové doméně pro vysílače WCDMA/TD-SCDMA
- Kvantifikuje odchylky od ideálních ortogonálních rozprostíracích kódů
- Vyjadřuje se jako poměr relativní chyby v dB
- Používá se v testech konformity podle 3GPP TS 25.141 a 25.142
- Ukazuje kvalitu signálu a potenciální úrovně interference
- Podporuje optimalizaci sítě a ověřování výkonu UE

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [OVSF – Orthogonal Variable Spreading Factor](/mobilnisite/slovnik/ovsf/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [BER – Basic Encoding Rules](/mobilnisite/slovnik/ber/)

## Definující specifikace

- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements

---

📖 **Anglický originál a plná specifikace:** [RCDE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcde/)
