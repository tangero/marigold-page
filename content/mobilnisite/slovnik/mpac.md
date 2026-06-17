---
slug: "mpac"
url: "/mobilnisite/slovnik/mpac/"
type: "slovnik"
title: "MPAC – Multi-Probe Anechoic Chamber"
date: 2025-01-01
abbr: "MPAC"
fullName: "Multi-Probe Anechoic Chamber"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/mpac/"
summary: "MPAC je sofistikovaný Over-the-Air (OTA) testovací systém používaný k vyhodnocení vyzařovacího výkonu bezdrátových zařízení, zejména MIMO antén v mobilních terminálech. Vytváří řízené, opakovatelné si"
---

MPAC je sofistikovaný Over-the-Air (OTA) testovací systém, který využívá více prostorových sond v řízené komoře k vyhodnocení vyzařovacího výkonu, jako je TRP a TIS, bezdrátových zařízení, například MIMO antén.

## Popis

Multi-Probe Anechoic Chamber (MPAC) je pokročilé měřicí uspořádání určené pro Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)) testování bezdrátových zařízení, jako jsou chytré telefony, tablety a IoT moduly. Jeho hlavní funkcí je charakterizace vyzařovacího výkonu testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)) v řízeném, izolovaném prostředí, které simuluje reálné podmínky šíření rádiového signálu. Jádrem MPAC je stíněná anechoická komora vyložená materiálem pohlcujícím rádiové vlny (RAM), která eliminuje vnější rušení a vnitřní odrazy a vytváří 'klidovou zónu' s rovnoměrnými elektromagnetickými poli. Charakteristickým rysem je soustava více pevných anténních sond (často 8, 16 nebo více) uspořádaných na kruhovém nebo kulovém povrchu kolem pozice DUT. Každá sonda může být individuálně aktivována pro vysílání nebo příjem signálů, čímž simuluje příchozí rádiové vlny z různých směrů příchodu.

Testovací postup zahrnuje umístění DUT na pozicionovací systém ve středu komory. Vektorový generátor a analyzátor signálu jsou připojeny k soustavě sond přes spínací matici. Pro měření celkového vyzařovaného výkonu (TRP) DUT vysílá signál a systém postupně aktivuje každou sondu, aby změřil přijímaný výkon ze všech směrů. Výsledky se integrují přes sféru pro výpočet celkového vyzařovaného výkonu. Opačně, pro celkovou izotropní citlivost (TIS), každá sonda vysílá známý signál do DUT a měří se citlivost přijímače DUT pro každý směr; výsledky se integrují pro zjištění průměrné citlivosti. Soustava více sond umožňuje rychlé sekvenční vzorkování prostorové sféry bez nutnosti fyzického otáčení DUT pro každý úhel, což výrazně urychluje testy složitých víceanténních systémů.

Systémy MPAC jsou klíčové pro vyhodnocení výkonu Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)) a beamformingu, které jsou základem 4G LTE a 5G NR. Mohou vytvářet dynamické fadingové prostředí aplikací komplexních vah na signály z různých sond, čímž simulují specifické kanálové modely definované v 3GPP (např. TDL, [CDL](/mobilnisite/slovnik/cdl/)). To umožňuje testování výkonu přijímače za realistických vícecestných podmínek a validaci účinnosti anténní diverzity a schémat MIMO prostorového multiplexování. Specifikace pro MPAC testovací metodologie, včetně kalibrace komory, konfigurace sond a nejistoty měření, jsou podrobně popsány v 3GPP TS 37.544 a souvisejících specifikacích pracovní skupiny 3GPP Radio Access Network (RAN). To zajišťuje, že výkonnostní testy jsou standardizované, opakovatelné a korelují s reálným výkonem sítě, což poskytuje spolehlivý etalon pro certifikaci zařízení a výzkum a vývoj.

## K čemu slouží

MPAC byl vyvinut pro řešení významných výzev při testování moderních bezdrátových zařízení, jejichž výkon je stále více definován jejich integrovanými anténami a [MIMO](/mobilnisite/slovnik/mimo/) schopnostmi. Tradiční konduktivní testování, kdy je kabel připojen přímo k anténnímu portu, se stalo nedostatečným, protože obchází anténní systém – právě tu komponentu, která definuje vyzařovaný výkon, citlivost a prostorové charakteristiky. Jak se zařízení zmenšovala a používala více integrovaných, neodnímatelných antén, [OTA](/mobilnisite/slovnik/ota/) testování se stalo nezbytným. Rané OTA metody používaly jednu sondu a rotační pozicionér, což bylo časově náročné a nedokázalo přesně simulovat rychlé fadingové, vícecestné prostředí MIMO.

Omezení systémů s jednou sondou motivovalo vytvoření MPAC. Pro přesnou validaci MIMO a beamformingu je nutné stimulovat zařízení signály přicházejícími z více prostorových směrů současně nebo v rychlém sledu za sebou, což emuluje realistický prostorový kanál. Systém s jednou sondou a mechanickým pozicionérem je příliš pomalý na to, aby zachytil časové koherenční vlastnosti kanálu. MPAC to řeší použitím pevné soustavy sond, což umožňuje rychlé přepínání mezi prostorovými úhly a aplikaci komplexní emulace kanálu. To umožňuje efektivní testování klíčových ukazatelů výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)), jako je MIMO propustnost za standardizovaných fadingových podmínek.

3GPP standardizovalo metodologii MPAC, aby zajistilo konzistenci a spravedlnost při hodnocení výkonu zařízení, zejména pro přijetí operátorem a regulační shodu. Poskytuje řízenou a opakovatelnou alternativu k nákladnému a proměnlivému terénnímu testování. Definováním přesných testovacích uspořádání ve specifikacích jako TS 37.544 umožňuje 3GPP výrobcům zařízení, testovacím laboratořím a síťovým operátorům mít společné, přesné porozumění reálnému vyzařovacímu výkonu zařízení, což pohání zlepšení v anténním designu a celkovém uživatelském zážitku v celulárních sítích.

## Klíčové vlastnosti

- Skládá se z anechoické komory s více pevnými anténními sondami prostorově uspořádanými kolem testovaného zařízení (DUT)
- Umožňuje rychlé sekvenční měření vyzařovaného výkonu a citlivosti ze všech směrů bez mechanické rotace DUT pro každý úhel
- Podporuje vytváření realistických prostorových kanálových modelů (např. 3GPP TDL/CDL) pro testování výkonu MIMO a beamformingu
- Měří klíčové OTA metriky: Celkový vyzařovaný výkon (TRP), Celková izotropní citlivost (TIS) a MIMO propustnost
- Poskytuje stíněné, bezodrazové prostředí pro přesné a opakovatelné testování vyzařovacího výkonu
- Standardizovaná metodologie ve specifikacích 3GPP pro konzistentní testování shody a certifikaci zařízení

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology

---

📖 **Anglický originál a plná specifikace:** [MPAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpac/)
