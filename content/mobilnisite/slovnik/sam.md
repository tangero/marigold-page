---
slug: "sam"
url: "/mobilnisite/slovnik/sam/"
type: "slovnik"
title: "SAM – Specific Anthropomorphic Mannequin"
date: 2025-01-01
abbr: "SAM"
fullName: "Specific Anthropomorphic Mannequin"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sam/"
summary: "Specific Anthropomorphic Mannequin (SAM) je standardizovaný softwarový model lidského těla používaný v 3GPP pro simulaci expozice radiofrekvenčnímu (RF) elektromagnetickému poli z bezdrátových zařízen"
---

SAM je standardizovaný softwarový model lidského těla používaný v 3GPP pro simulaci expozice radiofrekvenčnímu záření z bezdrátových zařízení za účelem vyhodnocení shody s bezpečnostními limity, jako je Specifická míra absorpce (SAR).

## Popis

Specific Anthropomorphic Mannequin je výpočetní model představující lidskou hlavu nebo tělo, používaný v elektromagnetických simulacích k posouzení interakce mezi zářícím zařízením (jako je mobilní telefon nebo základnová stanice) a lidskou tkání. Je definován podrobnou geometrickou sítí (mesh), která zahrnuje různé typy tkání, jako je kůže, tuk, svaly, kosti a mozek, přičemž každé jsou přiřazeny komplexní permitivity (dielektrické vlastnosti) pro konkrétní kmitočtová pásma. Tento model je implementován v simulačním softwaru pro řešení Maxwellových rovnic, obvykle pomocí metody Finite-Difference Time-Domain (FDTD), za účelem výpočtu rozložení absorbované [RF](/mobilnisite/slovnik/rf/) energie.

Hlavním výstupem simulace SAM je Specifická míra absorpce ([SAR](/mobilnisite/slovnik/sar/)), měřená ve wattech na kilogram (W/kg). SAR je míra rychlosti, jakou tělo absorbuje energii při vystavení RF elektromagnetickému poli. U ručních zařízení simulace umisťují SAM do standardizovaných poloh u hlavy (tvářová a skloněná poloha) nebo vedle těla pro stanovení prostorově průměrovaného špičkového SAR. U základnových stanic nebo jiného zařízení se SAM používá k vyhodnocení expozice výkonové hustoty v blízkosti antény. Standardizovaná geometrie a tkáňové parametry SAM zajišťují, že různé laboratoře a výrobci získají srovnatelné a reprodukovatelné výsledky, což je klíčové pro regulační certifikaci.

Specifikace 3GPP, zejména ty vyvinuté skupinou RAN4 (Radio Access Network Working Group 4), odkazují na modely SAM pro testování shody uživatelského zařízení (UE) a základnových stanic z hlediska RF expozice. Specifikace podrobně popisují přesné rozlišení sítě, vlastnosti tkání pro kmitočtová pásma od 300 MHz do 6 GHz a simulační metodologii. Použitím SAM poskytuje 3GPP jasný technický základ pro prokázání, že bezdrátová zařízení fungující v rámci jejích standardů splňují mezinárodní bezpečnostní směrnice stanovené orgány, jako je Mezinárodní komise pro ochranu před neionizujícím zářením (ICNIRP) a Institut inženýrů elektrotechniky a elektroniky ([IEEE](/mobilnisite/slovnik/ieee/)).

## K čemu slouží

SAM byl vyvinut za účelem vytvoření jednotného, vědecky rigorózního přístupu pro hodnocení shody s limity [RF](/mobilnisite/slovnik/rf/) expozice v celosvětovém telekomunikačním průmyslu. Před standardizací používali výrobci a testovací laboratoře různé proprietární fantomy a metodologie, což vedlo k nesrovnalostem v měření [SAR](/mobilnisite/slovnik/sar/) a obtížím při porovnávání výsledků. Tento nedostatek harmonizace představoval výzvy pro regulační schvalování a vyvolával obavy ohledně spolehlivosti bezpečnostních hodnocení.

Zavedení SAM ve standardech 3GPP řeší tyto problémy tím, že poskytuje společný referenční model. Jeho účelem je zajistit, aby všechna zařízení testovaná na shodu s rádiovými standardy 3GPP byla hodnocena vůči stejnému benchmarku, což podporuje spravedlnost, reprodukovatelnost a technickou přesnost. To je obzvláště důležité, protože formfaktory zařízení se stávají složitějšími (např. skládací telefony, nositelná zařízení) a sítě používají vyšší kmitočtová pásma (jako mmWave v 5G), kde se charakteristiky expozice mění. SAM umožňuje průmyslu proaktivně hodnotit bezpečnost pomocí výpočetního modelování, které je často flexibilnější a komplexnější než samotná fyzická měření, a tím podporuje rychlý vývoj a certifikaci nových bezdrátových technologií.

## Klíčové vlastnosti

- Standardizovaný geometrický model: Podrobná 3D síť (mesh) představující lidskou hlavu a/nebo tělo s rozlišením 1 mm x 1 mm x 1,5 mm pro hlavu.
- Dielektrické vlastnosti více tkání: Zahrnuje definované hodnoty komplexní permitivity pro tkáně kůže, tuku, svalů, kostí, chrupavky a mozku napříč více kmitočtovými pásmy.
- Nástroj pro výpočetní simulaci: Navržen pro použití s FDTD a dalšími softwary pro elektromagnetickou simulaci k výpočtu rozložení SAR.
- Standardizované testovací polohy: Definuje konkrétní polohy zařízení vůči fantomu (např. tvářová, skloněná, nošená u těla) pro konzistentní testování.
- Soulad s regulacemi: Podporuje hodnocení shody s hlavními mezinárodními bezpečnostními směrnicemi pro RF expozici (ICNIRP, IEEE, FCC).
- Pokrytí kmitočtového rozsahu: Použitelný pro simulace od 300 MHz až do alespoň 6 GHz, pokrývající tradiční i moderní buněčná pásma.

## Definující specifikace

- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.902** (Rel-19) — OTA TRP/TRS Measurement for LTE Terminals

---

📖 **Anglický originál a plná specifikace:** [SAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sam/)
