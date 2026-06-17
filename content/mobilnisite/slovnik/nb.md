---
slug: "nb"
url: "/mobilnisite/slovnik/nb/"
type: "slovnik"
title: "NB – Narrowband"
date: 2025-01-01
abbr: "NB"
fullName: "Narrowband"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/nb/"
summary: "Označuje omezenou šířku pásma pro zvuk (typicky kolem 3,1 kHz) používanou pro hlasové služby v telekomunikacích. Je zásadní pro kvalitu tradiční telefonie a slouží jako výchozí bod pro návrh kodeků a"
---

NB (úzkopásmový) je omezená šířka pásma pro zvuk, typicky kolem 3,1 kHz, používaná pro základní hlasové služby telefonie. Slouží jako výchozí bod pro návrh kodeků a plánování sítě, aby byla zajištěna základní interoperabilita.

## Popis

Narrowband (NB) v kontextu 3GPP primárně označuje šířku pásma pro zvuk přibližně 300–3400 Hz, což je standard pro tradiční telefonní hlasové kanály. Tato šířka pásma definuje frekvenční rozsah, který musí hlasové kodeky efektivně kódovat a dekódovat, aby zajistily srozumitelnou řeč. V síťové architektuře parametry NB ovlivňují návrh transportních a rádiových rozhraní, protože stanovují požadavky na vzorkovací frekvence, přenosové rychlosti a filtrování. Například klasická pulzně kódová modulace (PCM) s 64 kbps je založena na této charakteristice NB. V rámci specifikací 3GPP je NB referenčním bodem pro audio výkon, často používaným ve spojení s kodeky jako [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate), aby byla zajištěna zpětná kompatibilita a konzistentní kvalita hlasu napříč generacemi od GSM přes LTE až po 5G.

Operačně je audio NB zpracováváno řečovými kodeky, které komprimují signál v tomto omezeném pásmu pro optimalizaci kapacity sítě. Mezi klíčové komponenty patří enkodér, který digitalizuje a komprimuje analogový hlasový signál, a dekodér, který jej rekonstruuje na přijímací straně. Úzké pásmo umožňuje efektivní multiplexování více hlasových kanálů přes sdílená média, ať už v okruhově nebo paketově spínaných doménách. V rádiovém přístupu úvahy o NB ovlivňují uplink a downlink přenosy, protože hlasové pakety musí být formátovány tak, aby se vešly do přidělených bloků zdrojů, a zároveň byly dodrženy cíle pro zpoždění a kolísání pro komunikaci v reálném čase.

Role NB se rozšiřuje i na testování a certifikaci, kde zařízení musí splňovat specifické metriky kvality zvuku v tomto pásmu. Slouží jako měřítko pro hodnocení metrik kvality hlasu, jako je Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)), a pro definování minimálních požadavků na výkon v testech interoperability. Zatímco moderní systémy podporují širokopásmové (WB) a super-širokopásmové (SWB) audio pro vyšší kvalitu, NB zůstává klíčové pro podporu starších systémů, záložní scénáře a regiony s omezenými zdroji šířky pásma. Jeho přetrvávání napříč vydáními zajišťuje, že jádrové telefonní služby zůstávají dostupné, i když se sítě vyvíjejí pro podporu bohatších médií.

## K čemu slouží

NB existuje za účelem standardizace základní šířky pásma pro zvuk v hlasové komunikaci, čímž zajišťuje interoperabilitu a základní kvalitu služeb napříč různými telekomunikačními sítěmi. Řeší potřebu konzistentního, nízko-náročného audio kanálu, který lze spolehlivě přenášet přes analogové i digitální systémy, sahající až k počátkům telefonie. Historicky byla šířka pásma 3,1 kHz zvolena jako kompromis mezi srozumitelností hlasu a efektivním využitím omezených přenosových zdrojů, jako jsou měděné dráty a rádiové spektrum.

Vznik NB byl motivován požadavkem na vytvoření univerzálního výchozího bodu pro hlasové služby, který by umožnil bezproblémové propojení mezi různými síťovými operátory a technologiemi. Před standardizací mohly různé šířky audio pásma vést k problémům s kompatibilitou a zhoršené kvalitě hovorů. Definováním NB poskytla 3GPP referenci, která vede vývoj kodeků, dimenzování sítí a procesy zajištění kvality. Řeší problémy související se zkreslením hlasového signálu a zajišťuje, že i v omezených prostředích zůstává možná základní komunikace.

NB také slouží jako základ pro evoluční vylepšení audia. Zatímco představuje omezení z hlediska věrnosti zvuku ve srovnání s širšími pásmy, jeho stabilita umožňuje sítím postupně zavádět vylepšení, jako je širokopásmový hlas, aniž by byla narušena podpora starších služeb. Tato zpětná kompatibilita je klíčová pro postupné aktualizace sítí a pro obsluhu uživatelské základny s různorodými možnostmi zařízení.

## Klíčové vlastnosti

- Standardní šířka audio pásma přibližně 300–3400 Hz
- Výchozí bod pro kvalitu tradičního telefonního hlasu a návrh kodeků
- Zajišťuje interoperabilitu mezi staršími a moderními sítěmi
- Podporuje efektivní multiplexování a využití zdrojů
- Používá se jako reference pro testování a certifikaci kvality hlasu
- Umožňuje zpětnou kompatibilitu v sítích více generací

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TR 26.921** (Rel-19) — UE Performance in Ambient Noise
- **TS 28.405** (Rel-19) — QoE Measurement Control & Configuration
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.902** (Rel-19) — OTA TRP/TRS Measurement for LTE Terminals

---

📖 **Anglický originál a plná specifikace:** [NB na 3GPP Explorer](https://3gpp-explorer.com/glossary/nb/)
