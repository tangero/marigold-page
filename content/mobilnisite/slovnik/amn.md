---
slug: "amn"
url: "/mobilnisite/slovnik/amn/"
type: "slovnik"
title: "AMN – Artificial Mains Network"
date: 2025-01-01
abbr: "AMN"
fullName: "Artificial Mains Network"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/amn/"
summary: "Standardizovaná testovací síť, která simuluje charakteristiky impedance reálné elektrické sítě pro testování elektromagnetické kompatibility (EMC) telekomunikačních zařízení. Zajišťuje, že zařízení sp"
---

AMN je standardizovaná testovací síť, která simuluje impedanci reálné elektrické sítě, aby poskytla konzistentní podmínky pro testování elektromagnetické kompatibility (EMC) telekomunikačních zařízení.

## Popis

Umělá síťová impedance (Artificial Mains Network – AMN) je klíčový testovací přístroj specifikovaný ve standardech 3GPP pro testování shody v oblasti elektromagnetické kompatibility ([EMC](/mobilnisite/slovnik/emc/)) telekomunikačních zařízení. Slouží jako rozhraní mezi testovaným zařízením ([EUT](/mobilnisite/slovnik/eut/)) a elektrickou sítí, poskytuje standardizovanou impedanční síť, která simuluje typické charakteristiky elektrického vedení, a zároveň izoluje EUT od skutečné elektrické sítě. Tato izolace zabraňuje ovlivnění výsledků testů vnějšími rušivými vlivy a zajišťuje, že emise z EUT jsou měřeny přesně, bez interference ze strany skutečné elektrické sítě.

Architektura AMN se skládá z pečlivě navržených pasivních součástek včetně cívek, kondenzátorů a rezistorů uspořádaných do specifických konfigurací, které vytvářejí definované charakteristiky impedance v různých frekvenčních pásmech. Tyto sítě jsou kalibrovány tak, aby splňovaly přesné specifikace uvedené v technických specifikacích 3GPP, přičemž různé typy AMN jsou specifikovány pro různé úrovně napětí a proudové zatížení. Zařízení obsahuje měřicí porty pro připojení testovacích přístrojů, jako jsou spektrální analyzátory a přijímače EMI, což inženýrům umožňuje kvantifikovat vedené emise ve frekvenčních pásmech relevantních pro telekomunikační zařízení.

Během testování AMN současně plní více funkcí. Poskytuje napájení testovanému zařízení a zároveň představuje známou, stabilní impedanci reprezentující typické podmínky elektrické sítě. To umožňuje reprodukovatelná měření vedených rušivých vlivů, které může zařízení vnášet do elektrické sítě. AMN také slouží jako vazební zařízení pro testování odolnosti, kdy jsou rušivé vlivy vnášeny do elektrického vedení za účelem vyhodnocení odolnosti zařízení vůči vnější interferenci. Pro různé aplikace jsou specifikovány různé konfigurace AMN, včetně návrhů V-sítí pro symetrická měření a konfigurací delta-sítí pro asymetrická měření.

Role AMN v rámci standardizace 3GPP zajišťuje, že všichni výrobci telekomunikačních zařízení dodržují identické testovací metodologie, což umožňuje spravedlivé srovnání výkonu v oblasti EMC mezi různými produkty a dodavateli. Poskytnutím kontrolovaného testovacího prostředí, které eliminuje proměnné spojené se skutečnými elektrickými sítěmi, AMN umožňuje konzistentní vyhodnocení shody zařízení s mezinárodními předpisy pro EMC. Tato standardizace je obzvláště důležitá pro globální telekomunikační trhy, kde zařízení musí splňovat více regionálních regulatorních požadavků a zároveň zachovávat interoperabilitu a spolehlivost v různých scénářích nasazení.

## K čemu slouží

Umělá síťová impedance (AMN) byla vyvinuta, aby řešila kritickou potřebu standardizovaného, opakovatelného testování elektromagnetické kompatibility v telekomunikačním průmyslu. Před standardizací AMN používali různí výrobci a testovací laboratoře různá testovací uspořádání s nekonzistentními charakteristikami impedance, což vedlo k nesrovnatelným výsledkům testů a problémům s regulatorní shodou. Tato nekonzistence vytvářela překážky pro globální certifikaci zařízení a ztěžovala zajištění, že telekomunikační zařízení budou spolehlivě fungovat, aniž by způsobovala nebo byla ovlivňována elektromagnetickým rušením v reálném nasazení.

AMN tyto problémy řeší tím, že poskytuje přesně definované rozhraní mezi zařízením a elektrickou sítí během testování. Zajišťuje, že všechna měření vedených emisí jsou prováděna za identických impedančních podmínek bez ohledu na skutečné charakteristiky elektrické sítě laboratoře. Tato standardizace umožňuje výrobcům navrhovat zařízení, která splňují globální požadavky na [EMC](/mobilnisite/slovnik/emc/), s jistotou, že výsledky testů budou akceptovány regulatorními orgány po celém světě. AMN také řeší bezpečnostní obavy tím, že poskytuje izolaci mezi testovacím zařízením a živou elektrickou sítí, čímž chrání jak testovací personál, tak i drahé měřicí přístroje.

Historicky byl vývoj specifikací AMN v rámci 3GPP hnán rostoucí složitostí telekomunikačních zařízení a rostoucím významem shody v oblasti EMC, protože zařízení se stávala sofistikovanějšími a pracovala na vyšších frekvencích. Jak se bezdrátové technologie vyvíjely prostřednictvím postupných releasů 3GPP, potřeba konzistentního testování EMC se stávala kritičtější, aby bylo zajištěno, že nové generace zařízení nebudou interferovat se stávajícími systémy ani nebudou náchylné k interferenci od jiných zařízení. AMN poskytuje základ pro tuto testovací metodologii a umožňuje telekomunikačnímu průmyslu udržovat elektromagnetickou kompatibilitu v čím dál více zaplněných frekvenčních spektrech a komplexních síťových nasazeních.

## Klíčové vlastnosti

- Standardizovaná impedanční síť simulující charakteristiky reálné elektrické sítě
- Izolace mezi testovaným zařízením a skutečnou elektrickou sítí
- Více konfigurací pro různé úrovně napětí a proudové zatížení
- Měřicí porty pro testování vedených emisí
- Schopnost vazby pro testování odolnosti
- Požadavky na kalibraci zajišťující konzistenci měření

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 36.113** (Rel-19) — EMC Requirements for E-UTRA Base Stations
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.114** (Rel-19) — EMC Requirements for NR Repeaters and NCR
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes

---

📖 **Anglický originál a plná specifikace:** [AMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/amn/)
