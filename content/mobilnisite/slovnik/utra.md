---
slug: "utra"
url: "/mobilnisite/slovnik/utra/"
type: "slovnik"
title: "UTRA – Universal Terrestrial Radio Access"
date: 2025-01-01
abbr: "UTRA"
fullName: "Universal Terrestrial Radio Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/utra/"
summary: "Standardizovaná rádiová přístupová technologie definovaná 3GPP pro sítě 3G, zahrnující jak režim FDD (WCDMA), tak TDD (TD-SCDMA). Tvoří základ rozhraní pro UMTS a poskytuje klíčové specifikace pro mod"
---

UTRA je standardizovaná 3GPP rádiová přístupová technologie pro sítě UMTS, zahrnující režimy WCDMA a TD-SCDMA, které tvoří rozhraní pro vysokorychlostní datové a hlasové služby.

## Popis

Universal Terrestrial Radio Access (UTRA) je souhrnný termín pro kompletní sadu rádiových přístupových technologií specifikovaných 3GPP, které tvoří rozhraní Universal Mobile Telecommunications System (UMTS) a jeho vývoje. Je definována v rozsáhlé sadě technických specifikací pokrývajících všechny vrstvy rádiového protokolového zásobníku. UTRA existuje primárně ve dvou duplexních režimech: UTRA Frequency Division Duplex (UTRA-FDD), který jako základní víceuživatelský přístup používá Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)), a UTRA Time Division Duplex (UTRA-TDD), který zahrnuje jak variantu s nízkou čipovou rychlostí ([LCR](/mobilnisite/slovnik/lcr/), známou také jako [TD-SCDMA](/mobilnisite/slovnik/td-scdma/)), tak variantu s vysokou čipovou rychlostí (HCR).

Jádro architektury UTRA je postaveno na konceptu rozprostření vysílaných signálů pomocí pseudonáhodných kódů přes širokou šířku pásma (např. 5 MHz pro WCDMA). To poskytuje vnitřní odolnost vůči rušení a umožňuje funkce jako měkký předávání spojení. Fyzická vrstva (vrstva 1), detailně popsaná ve specifikacích řady 25.2xx, definuje rádiové charakteristiky, modulaci ([QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/)), kanálové kódování (konvoluční, Turbo), rozprostření, skramblování a strukturu fyzických kanálů (např. [DPCH](/mobilnisite/slovnik/dpch/), [CPICH](/mobilnisite/slovnik/cpich/), PRACH). Linková vrstva (vrstva 2) je rozdělena na podvrstvy Medium Access Control (MAC), Radio Link Control (RLC) a Packet Data Convergence Protocol (PDCP), které jsou zodpovědné za mapování logických kanálů, opravu chyb a kompresi hlaviček. Protokol Radio Resource Control (RRC) (vrstva 3) spravuje navazování spojení, mobilitu a konfiguraci všech parametrů nižších vrstev.

Úlohou UTRA v síti je poskytovat spolehlivé, vysokokapacitní bezdrátové propojení mezi uživatelským zařízením (UE) a rádiovou přístupovou sítí sítě (UTRAN), která se skládá z Node B a řadičů rádiové sítě (RNC). Podporuje přepojování okruhů pro hlas a videohovory i služby přepojování paketů pro data s teoretickými špičkovými rychlostmi, které se od prvních vydání vyvíjely od 384 kbps až po několik Mbps s vylepšeními High-Speed Packet Access (HSPA). Tato technologie zavedla klíčové koncepty 3G, jako jsou vyhrazené a sdílené kanály, proměnné rozprostřovací faktory a rychlý řízení výkonu. Její návrh kladl důraz na plynulou mobilitu, diferenciaci kvality služeb (QoS) a zpětnou kompatibilitu se sítěmi 2G GSM/GPRS, čímž vytvořila kritický most mezi druhou generací a skutečným širokopásmovým mobilním internetem.

## K čemu slouží

UTRA byla vytvořena za účelem stanovení globálního, jednotného standardu pro mobilní komunikace třetí generace (3G), což znamenalo posun za hlasově orientované a fragmentované prostředí 2G. Jejím primárním účelem bylo poskytnout výrazně vyšší datové rychlosti (původně cíleno na 2 Mbps pro vnitřní prostředí/nízkou mobilitu) pro podporu nových multimediálních aplikací, jako je videotelefonie, prohlížení mobilního internetu a e-mail. 'Universal' v jejím názvu odráží ambici vytvořit jediné rádiové rozhraní schopné celosvětového nasazení, které by nahradilo množství nekompatibilních technologií 2G a tehdejší konkurenční návrhy 3G.

Vývoj UTRA řešil klíčová omezení předchozích systémů 2G, jako je GSM. GSM používalo úzkopásmový Time Division Multiple Access (TDMA), což omezovalo spektrální účinnost a špičkové datové rychlosti. Přijetí WCDMA v UTRA poskytlo větší kapacitu prostřednictvím statistického multiplexování, inherentní frekvenční diverzity a schopnosti podporovat proměnné přenosové rychlosti na jediném spojení. Také efektivně vyřešilo výzvu podpory jak symetrického (hlas), tak asymetrického (data) provozu prostřednictvím svých režimů FDD a TDD. UTRA byla navíc od základu navržena tak, aby podporovala sofistikované řízení QoS, což umožnilo operátorům nabízet diferencované služby.

Historicky začala specifikace UTRA koncem 90. let pod záštitou 3GPP, přičemž první kompletní sada specifikací byla zmražena jako Release 99 (R99). Šlo o monumentální úsilí o harmonizaci evropsky vedeného WCDMA a japonsky vedených návrhů do jediného standardu. Vytvoření UTRA bylo motivováno vizí IMT-2000 Mezinárodní telekomunikační unie (ITU) pro 3G. Poskytla technologický základ, který umožnil explozivní růst mobilních dat, a připravila cestu pro vývoj HSPA a nakonec přechod k 4G LTE a 5G NR, s nimiž si po mnoho let udržovala interoperabilitu.

## Klíčové vlastnosti

- Wideband Code Division Multiple Access (WCDMA) pro provoz FDD
- Podpora obou duplexních režimů: FDD i TDD (včetně TD-SCDMA)
- Nominální šířka kanálu 5 MHz s proměnnými rozprostřovacími faktory
- Rychlé řízení výkonu (1500 Hz) a schopnosti měkkého/měkkého předávání spojení
- Integrovaná podpora služeb s přepojováním okruhů i paketů
- Vývoj prostřednictvím HSPA (HSDPA/HSUPA) pro vylepšený výkon paketových dat

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- … a dalších 62 specifikací

---

📖 **Anglický originál a plná specifikace:** [UTRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/utra/)
