---
slug: "rms"
url: "/mobilnisite/slovnik/rms/"
type: "slovnik"
title: "RMS – Root Mean Square"
date: 2025-01-01
abbr: "RMS"
fullName: "Root Mean Square"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rms/"
summary: "Základní statistická míra hojně používaná napříč specifikacemi 3GPP ke kvantifikaci velikosti proměnné veličiny, jako je výkon signálu, velikost chybového vektoru (EVM) nebo fázový šum. Poskytuje stan"
---

RMS je základní statistická míra používaná napříč specifikacemi 3GPP ke kvantifikaci velikosti proměnných veličin, jako je výkon signálu, pro standardizované požadavky na výkon a testování shody.

## Popis

Střední kvadratická hodnota (Root Mean Square, RMS) je matematický a statistický koncept všudypřítomně používaný v technických specifikacích 3GPP pro definici a měření výkonnostních parametrů. Není to protokol ani síťová entita, ale metoda výpočtu používaná k určení požadavků na konzistenci a přesnost. RMS hodnota souboru hodnot (nebo spojitého průběhu) je druhá odmocnina z aritmetického průměru druhých mocnin těchto hodnot. Pro střídavý signál s nulovou střední hodnotou odpovídá RMS hodnota jeho efektivní stejnosměrné ekvivalentní hodnotě nebo jeho směrodatné odchylce, což poskytuje robustní jednociferné vyjádření jeho velikosti nebo rozptylu.

Ve specifikacích 3GPP se RMS používá v mnoha klíčových kontextech. Při testování rádiového výkonu (specifikace jako 38.141 pro základnové stanice nebo 38.521 pro UE) se používá k definování požadované přesnosti měření, například RMS úrovně referenčního signálu nebo RMS chyby měření výkonu. Pro kvalitu signálu se velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) často specifikuje jako procentuální RMS hodnota, která kvantifikuje přesnost modulace vysílače. V kontextu [RF](/mobilnisite/slovnik/rf/) zkreslení se fázový šum nebo únik lokálního oscilátoru specifikuje jako RMS hodnota integrovaná přes určitou šířku pásma odstupu. Dále jsou požadavky na nežádoucí emise, jako je poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)), založeny na měření RMS výkonu v rámci definované měřicí šířky pásma.

Použití RMS zajišťuje technickou přísnost a opakovatelnost. Když specifikace uvádí maximální přípustnou RMS hodnotu EVM, například 8 %, znamená to, že střední kvadratická hodnota velikosti chybového vektoru napříč velkým počtem symbolů nesmí tuto hodnotu překročit. Jedná se o statisticky významnější a přísnější požadavek než limit špičkové hodnoty, protože průměruje příležitostné anomálie a odráží celkové zkreslení signálu. Rozsáhlý seznam specifikací odkazujících na RMS (od základní slovní zásoby v 21.905 po podrobné testovací postupy v 38.141 a 38.521) podtrhuje jeho roli jako univerzálního jazyka pro definování kvantitativních výkonnostních mezí. Testovací zařízení používaná pro testování shody a přijetí jsou naprogramována tak, aby prováděla RMS výpočty podle metodologií definovaných 3GPP, což zajišťuje, že všichni výrobci a operátoři posuzují výkon podle stejného objektivního metrika.

## K čemu slouží

Použití metriky střední kvadratické hodnoty (RMS) ve specifikacích 3GPP slouží základnímu účelu stanovení jasných, jednoznačných a statisticky robustních výkonnostních kritérií pro všechny prvky buněčného systému. V počátcích standardizace mobilních sítí bylo klíčové definovat, jak měřit klíčové parametry jako výkon, šum a chybu, aby byla zajištěna interoperabilita. Samotná měření špičkových hodnot jsou nedostatečná, protože mohou být zkreslena přechodovými špičkami a nereprezentují průměrný výkon. RMS poskytuje standardizovaný matematický rámec, který poskytuje konzistentní hodnotu reprezentující celkovou "velikost" proměnlivého signálu nebo chyby.

Jeho přijetí řeší problém specifikace požadavků způsobem, který přímo koreluje s výkonem systému a lze jej spolehlivě měřit. Například RMS úroveň přijímaného signálu přímo souvisí s výkonem dostupným pro demodulaci. RMS hodnota fázového šumu ovlivňuje dosažitelný poměr signálu k šumu. Tím, že 3GPP nařizuje měření založená na RMS, zajišťuje, že různé testovací laboratoře, výrobci zařízení a síťoví operátoři získají při hodnocení shody zařízení nebo výkonu sítě srovnatelné výsledky. Tím se eliminuje subjektivní interpretace a je to nezbytné pro zaručení, že UE od jednoho výrobce bude správně fungovat v síti postavené s infrastrukturou od jiného, protože obě jsou navrženy a testovány tak, aby splňovaly stejné prahové hodnoty založené na RMS pro kritické rádiové frekvenční a základní pásmové charakteristiky.

## Klíčové vlastnosti

- Standardní statistická míra pro specifikaci velikosti signálu a chyb
- Poskytuje robustní, průměrované metrikum méně citlivé na odlehlé hodnoty než špičkové hodnoty
- Základní pro definici požadavků na velikost chybového vektoru (EVM)
- Používá se pro specifikaci přesnosti RF měření (např. výkonu, časování)
- Klíčový parametr ve specifikacích fázového šumu a úniku lokálního oscilátoru
- Zajišťuje konzistentní a opakovatelnou metodologii testování shody

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 28.304** (Rel-19) — PEE Parameters Control & Monitoring Requirements
- **TS 28.305** (Rel-19) — PEE Control & Monitoring IRP Information Service
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [RMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rms/)
