---
slug: "wcdma"
url: "/mobilnisite/slovnik/wcdma/"
type: "slovnik"
title: "WCDMA – Wideband Code Division Multiple Access"
date: 2025-01-01
abbr: "WCDMA"
fullName: "Wideband Code Division Multiple Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/wcdma/"
summary: "WCDMA je primární technologií rádiového rozhraní pro sítě 3G UMTS, která využívá přímou sekvenci rozprostřeného spektra s šířkou pásma 5 MHz. Umožňuje vysokorychlostní datové a hlasové služby tím, že"
---

WCDMA je primární technologií rádiového rozhraní pro sítě 3G UMTS, která využívá přímou sekvenci rozprostřeného spektra s šířkou pásma 5 MHz pro zajištění vysokorychlostních datových a hlasových služeb.

## Popis

Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (WCDMA) je technika mnohonásobného přístupu s rozprostřeným spektrem, která tvoří jádro pozemního rádiového přístupu UMTS ([UTRA](/mobilnisite/slovnik/utra/)) pro sítě 3G. Pracuje s čipovou rychlostí 3,84 Mcps v nominální šířce pásma 5 MHz, což je výrazně širší než 200 kHz nosné používané v GSM. Tato větší šířka pásma podporuje vyšší datové rychlosti a poskytuje lepší rozlišení vícecestného šíření. WCDMA využívá přímou sekvenci rozprostření, kde je datový signál každého uživatele násoben vysokorychlostním pseudonáhodným rozprostíracím kódem, čímž je signál rozprostřen přes celou šířku pásma. Různí uživatelé jsou odděleni přiřazením unikátních ortogonálních kódů s proměnným rozprostíracím faktorem ([OVSF](/mobilnisite/slovnik/ovsf/)) pro kanalizaci a skramblovacích kódů pro identifikaci buňky a uživatele.

Fyzická vrstva WCDMA podporuje jak režim duplexu s frekvenčním dělením ([FDD](/mobilnisite/slovnik/fdd/)), tak duplex s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)). V režimu FDD používají uplink a downlink samostatná frekvenční pásma, zatímco TDD využívá stejné frekvenční pásmo s časovými sloty přidělenými pro každý směr. Mezi klíčové fyzické kanály patří vyhrazený fyzický kanál ([DPCH](/mobilnisite/slovnik/dpch/)) pro uživatelská data a řídicí informace, společný pilotní kanál ([CPICH](/mobilnisite/slovnik/cpich/)) pro odhad kanálu a synchronizační kanál ([SCH](/mobilnisite/slovnik/sch/)) pro vyhledávání buněk. Technologie využívá výkonné konvoluční a turbokódování spolu s modulací QPSK pro downlink a BPSK pro uplink v raných vydáních. Řízení výkonu je klíčové, přičemž rychlé uzavřené řízení výkonu pracující na 1500 Hz bojuje proti problému blízko-daleko a udržuje kvalitu spoje.

Z pohledu síťové architektury je WCDMA implementována v uživatelském zařízení (UE) a v Node B (základnové stanici), která se připojuje k řadiči rádiové sítě (RNC) v rádiové přístupové síti UMTS (UTRAN). RNC spravuje rádiové zdroje, předávání hovorů a připojení k jádru sítě. WCDMA podporuje měkké předání hovoru, při kterém může UE komunikovat současně s více Node B, čímž se zlepšuje spolehlivost na okrajích buněk. Technologie se vyvinula tak, aby podporovala vylepšení High-Speed Packet Access (HSPA), což dramaticky zvýšilo špičkové datové rychlosti. Její konstrukční principy širokého pásma a kódového dělení kanálů položily základy pro pozdější technologie 4G a 5G.

## K čemu slouží

WCDMA byla vyvinuta za účelem splnění požadavků Mezinárodní telekomunikační unie (ITU) IMT-2000 pro systémy mobilních sítí třetí generace (3G), které vyžadovaly vyšší datové rychlosti (zpočátku až 2 Mbps), podporu multimediálních služeb a vyšší spektrální účinnost ve srovnání s technologiemi 2G, jako je GSM. Hlavní motivací bylo vytvořit globální standard pro 3G, který by mohl podporovat rychlosti podobné přístupu k internetu, videohovory a mobilní širokopásmový přístup. WCDMA jako zvolená technologie pro UMTS poskytla evoluční cestu ze sítí GSM/GPRS, umožňující operátorům znovu využít infrastrukturu jádra sítě při nasazování nové rádiové přístupové sítě.

Řešila omezení systémů 2G založených na TDMA, které měly omezenou kapacitu a datové rychlosti. Použitím CDMA s šířkou pásma 5 MHz nabídla WCDMA díky statistickému multiplexování, inherentní frekvenční diverzitě a robustnímu chování v prostředí s vícecestným šířením vyšší kapacitu. Technologie byla od počátku navržena tak, aby podporovala asymetrický datový provoz a diferenciaci kvality služeb (QoS), což bylo nezbytné pro kombinované hlasové, video a datové služby. Její standardizace v rámci 3GPP od Release 99 dále zajišťovala celosvětovou interoperabilitu a úspory z rozsahu, což pohánělo úspěch mobilního širokopásmového přístupu 3G.

## Klíčové vlastnosti

- Šířka kanálu 5 MHz s čipovou rychlostí 3,84 Mcps pro vysokou datovou kapacitu
- Přímá sekvence rozprostřeného spektra využívající OVSF kódy pro kanalizaci a skramblovací kódy pro oddělení
- Podpora obou duplexních režimů FDD a TDD
- Rychlé řízení výkonu (1500 Hz) pro zvládání interference a problému blízko-daleko
- Schopnosti měkkého a měkčího předání hovoru pro plynulou mobilitu
- Podpora pokročilých služeb na fyzické vrstvě prostřednictvím vyhrazených a společných kanálů

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [OVSF – Orthogonal Variable Spreading Factor](/mobilnisite/slovnik/ovsf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [WCDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wcdma/)
