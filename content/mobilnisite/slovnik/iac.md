---
slug: "iac"
url: "/mobilnisite/slovnik/iac/"
type: "slovnik"
title: "IAC – Indoor Anechoic Chamber"
date: 2025-01-01
abbr: "IAC"
fullName: "Indoor Anechoic Chamber"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iac/"
summary: "Stíněná komora pro rádiové frekvence s absorpční výstelkou, používaná k vytvoření prostředí bez odrazů. Je nezbytná pro přesné a opakovatelné bezdrátové testování (Over-the-Air, OTA) bezdrátových zaří"
---

IAC je stíněná komora pro rádiové frekvence s absorpční výstelkou, používaná k vytvoření prostředí bez odrazů pro přesné bezdrátové testování (Over-the-Air) bezdrátových zařízení.

## Popis

Indoor Anechoic Chamber (IAC) je specializované elektromagnetické testovací zařízení definované ve specifikacích 3GPP pro testování shody a výkonu rádiových zařízení. Jejím hlavním účelem je poskytnout řízené, izolované prostředí bez vnějšího rádiového rušení (RFI) a vnitřních odrazů signálu. Komora je konstruována s kovovým stíněním (často měď nebo ocel) na všech stěnách, stropě a podlaze, aby blokovala vnější RF signály. Vnitřní povrchy jsou obloženy materiálem pohlcujícím RF energii, typicky pyramidální nebo klínovou pěnou napuštěnou uhlíkem, která minimalizuje odrazy pohlcováním dopadajících elektromagnetických vln v širokém frekvenčním pásmu. Tím vzniká přiblížení podmínek volného prostoru, umožňující přesné měření vyzařovacích charakteristik zařízení.

Komora je vybavena přesnými polohovacími systémy, jako jsou otočné stoly a robotická ramena, pro otáčení testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)). Měřící anténa, připojená k vektorovému analyzátoru nebo jiné testovací aparatuře, je umístěna na pevném místě. Otáčením DUT a měřením signálu přijímaného měřící anténou mohou inženýři charakterizovat vyzařovací diagram DUT, včetně metrik jako Celkový vyzářený výkon (TRP), Celková izotropní citlivost (TIS) a paprskové diagramy pro anténní pole. Komora musí být dostatečně velká, aby splňovala podmínku měření ve vzdálené zóně, kde je vzdálenost mezi DUT a měřící anténou dostatečně velká, aby čelo vlny bylo přibližně rovinné. Pro vyšší frekvence (jako mmWave) jsou často do IAC integrovány kompaktní anténní testovací tratě ([CATR](/mobilnisite/slovnik/catr/)) využívající parabolické reflektory k vytvoření kolimovaného svazku, což efektivně simuluje podmínky vzdálené zóny v menším prostoru.

V kontextu 3GPP je IAC klíčová pro metodologie bezdrátového testování ([OTA](/mobilnisite/slovnik/ota/)) specifikované pro zařízení 5G NR a LTE. Specifikace jako 37.941 definují testovací sestavy a postupy pro vyhodnocování metrik vyzařovaného výkonu. IAC umožňuje opakovatelné a srovnatelné testy v různých laboratořích a mezi různými výrobci. Používá se pro jak pro vedené, tak pro vyzařované testování, ale její hodnota je zásadní pro vyzařované testování, kde je anténa nedílnou, neodnímatelnou součástí zařízení, jak je běžné u moderních smartphonů a základnových stanic. Kvalita komory, určená její účinností stínění a úrovní odrazivosti (výkon v tiché zóně), přímo ovlivňuje přesnost měření, což z ní činí základní kámen certifikace a výzkumu a vývoje bezdrátových zařízení.

## K čemu slouží

Indoor Anechoic Chamber existuje proto, aby řešila základní problém přesného měření vyzařovaného výkonu bezdrátových zařízení řízeným a reprodukovatelným způsobem. V otevřeném prostředí nebo běžné místnosti se rádiové vlny odrážejí od stěn, podlah a předmětů, což vytváří scénář vícecestného šíření, který znemožňuje izolovat přímé vyzařovací charakteristiky testovaného zařízení. Vnější RF šum od jiných vysílačů měření dále narušuje. IAC poskytuje čistou, odrazuprostou 'elektromagnetickou tichou zónu', která napodobuje ideální podmínky volného prostoru.

Historicky, jak se bezdrátové technologie vyvíjely od jednoduchých antén ke komplexním systémům [MIMO](/mobilnisite/slovnik/mimo/) a beamforming v 4G a 5G, potřeba přesného [OTA](/mobilnisite/slovnik/ota/) testování exponenciálně rostla. Dřívější testování se často spoléhalo na vedené testy prostřednictvím kabelových spojů, které se staly nedostačujícími pro hodnocení aktivních anténních systémů a výkonu zařízení, jak jej zažívá koncový uživatel. IAC byla přijata jako standardní prostředí pro umožnění těchto pokročilých OTA testů. Její vznik byl motivován požadavkem průmyslu na společnou, spolehlivou testovací metodologii, která by zajišťovala interoperabilitu zařízení, shodu s předpisy (např. [FCC](/mobilnisite/slovnik/fcc/), normy [ETSI](/mobilnisite/slovnik/etsi/)), a ověřování výkonnostních tvrzení za ekvivalentních podmínek globálně. Odstraňuje omezení otevřených testovacích prostorů (OATS), které jsou náchylné k počasí a okolnímu rušení, tím, že poskytuje konzistentní, vnitřní a bezpečné testovací zařízení.

## Klíčové vlastnosti

- Elektromagnetické stínění pro blokování vnějšího RF rušení
- Interiér obložený RF absorbérem pro minimalizaci odrazů signálu
- Umožňuje sestavy pro OTA měření ve vzdálené zóně nebo s kompaktním dosahem (CATR)
- Přesné polohovací systémy pro rotaci a orientaci DUT
- Podporuje testování v širokém frekvenčním rozsahu (včetně mmWave)
- Poskytuje řízené prostředí pro opakovatelné a standardizované testování dle 3GPP

## Definující specifikace

- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements

---

📖 **Anglický originál a plná specifikace:** [IAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/iac/)
