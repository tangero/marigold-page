---
slug: "sg"
url: "/mobilnisite/slovnik/sg/"
type: "slovnik"
title: "SG – Signal Generator"
date: 2025-01-01
abbr: "SG"
fullName: "Signal Generator"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sg/"
summary: "Testovací a měřicí komponenta používaná k vytváření řízených rádiových signálů pro hodnocení výkonu přijímače uživatelského zařízení (UE). Simuluje síťové přenosy za účelem ověření metrik demodulace,"
---

SG (Signal Generator) je testovací komponenta používaná k vytváření řízených rádiových signálů pro hodnocení výkonu přijímače uživatelského zařízení (UE) simulací síťových přenosů za účelem ověření metrik demodulace, synchronizace a chybovosti.

## Popis

Signal Generator (SG) je klíčová součást testovacího vybavení definovaná ve specifikacích 3GPP pro testování shody přijímačů uživatelského zařízení (UE). Funguje tak, že generuje přesně řízené vysokofrekvenční signály napodobující přenosy základnové stanice, včetně specifických modulačních schémat, podmínek na kanálu a scénářů rušení požadovaných testovacími případy. SG pracuje ve spojení se systémovým simulátorem za účelem vytváření reprodukovatelných testovacích prostředí, což umožňuje hodnocení metrik výkonu UE, jako je bitová chybovost ([BER](/mobilnisite/slovnik/ber/)), bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) a citlivost přijímače.

Z architektonického hlediska je SG integrován do testovacích sestav, jako je Radio Frequency Conformance Test System. S testovaným UE komunikuje prostřednictvím rádiového rozhraní, často v provedení s vedeným nebo vyzařovaným signálem. Mezi klíčové vnitřní komponenty patří procesor základnového pásma pro generování rámců fyzické vrstvy (např. podle 25.101 pro [UTRA](/mobilnisite/slovnik/utra/) [FDD](/mobilnisite/slovnik/fdd/)), převodník na vysokofrekvenční pásmo a moduly řízení výkonu. Výstup SG musí splňovat přísné požadavky na spektrální a časovou přesnost, aby byla zajištěna platnost testu.

Jeho úlohou je aplikovat standardizované testovací signály definované ve specifikacích jako 25.101 (rádiový přenos a příjem UE), 25.309 (testování shody FDD opakovačů) a 25.319 (požadavky na testování vylepšeného uplinku). Například může generovat vyhrazené fyzické kanály se specificnými rozprostíracími kódy, úrovněmi výkonu a aditivním bílým Gaussovským šumem ([AWGN](/mobilnisite/slovnik/awgn/)) pro zatížení přijímače UE. SG umožňuje ověřit, že UE splňují minimální výkonnostní charakteristiky, což zajišťuje spolehlivý provoz v reálných sítích.

V pozdějších vydáních se schopnosti SG rozšířily o podporu nových technologií. Specifikace jako 38.762 pro NR definují testovací signály pro testy přijímačů 5G NR UE, včetně složitých scénářů s více nosnými a massive [MIMO](/mobilnisite/slovnik/mimo/). SG musí generovat signály s flexibilní numerologií, širokou šířkou pásma a beamformingovými charakteristikami. Tento vývoj zajišťuje, že testování drží krok s pokročilými rádiovými funkcemi, a udržuje tak kvalitu sítě a interoperabilitu.

## K čemu slouží

SG existuje za účelem poskytnutí standardizované, opakovatelné metody pro testování výkonu přijímače UE v laboratorních podmínkách. Před jeho formalizací mohlo být testování přijímačů nekonzistentní, protože spoléhalo na proprietární vybavení a metody, což vedlo k problémům s interoperabilitou a různému výkonu v terénu. SG tento problém řeší definicí jednotného rámce pro generování signálů, což zajišťuje, že všechna UE jsou hodnocena podle stejných přísných kritérií.

Historicky, jak se mobilní technologie vyvíjely od GSM přes UMTS až po LTE, rostla složitost přijímačů s pokročilou modulací (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/)) a technikami rozprostřeného spektra. To si vyžádalo přesné testovací signály pro ověření výkonu při útlumu, rušení a vysokorychlostních scénářích. SG, specifikovaný od vydání 6 dále, tyto potřeby řešil tím, že poskytoval řízenou referenci pro testování shody, které je povinné pro regulační schválení a přijetí operátorem.

Jeho vytvoření bylo motivováno potřebou zaručit kvalitu služeb a spektrální účinnost v živých sítích. Tím, že SG pomáhá odhalit nedostatky přijímačů včas, pomáhá předcházet přerušeným hovorům, nízké datové propustnosti a nadměrnému vybíjení baterie. Také podporuje vývoj robustních přijímačů schopných zvládat reálné rušivé vlivy, což v konečném důsledku zlepšuje uživatelský zážitek a spolehlivost sítě v různých podmínkách nasazení.

## Klíčové vlastnosti

- Generuje standardizované RF signály pro testování shody přijímače UE
- Podporuje více technologií rádiového přístupu (UTRA, E-UTRA, NR) napříč vydáními
- Emuluje realistické podmínky na kanálu včetně AWGN a profilů útlumu
- Poskytuje přesné řízení výkonu signálu, modulace a časování
- Integruje se se systémovými simulátory pro automatizované provádění testů
- Umožňuje měření klíčových ukazatelů výkonu, jako je BLER a citlivost

## Související pojmy

- [AWGN – Additive White Gaussian Noise](/mobilnisite/slovnik/awgn/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1

---

📖 **Anglický originál a plná specifikace:** [SG na 3GPP Explorer](https://3gpp-explorer.com/glossary/sg/)
