---
slug: "asa"
url: "/mobilnisite/slovnik/asa/"
type: "slovnik"
title: "ASA – Azimuth Spread of Arrival"
date: 2025-01-01
abbr: "ASA"
fullName: "Azimuth Spread of Arrival"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/asa/"
summary: "ASA měří úhlový rozptyl příchozích rádiových signálů na přijímači v horizontální rovině. Kvantifikuje prostorovou disperzi kanálu, což je klíčové pro výkon MIMO, přesnost beamformingu a modelování kan"
---

ASA (Azimuth Spread of Arrival) je azimutální rozptyl příchodu, parametr, který měří úhlový rozptyl příchozích rádiových signálů na přijímači v horizontální rovině za účelem charakterizace vícecestného šíření.

## Popis

Azimuth Spread of Arrival (ASA) je základní parametr kanálu definovaný ve specifikacích 3GPP, který charakterizuje úhlovou disperzi vícecestných složek přicházejících k přijímací anténní soustavě v azimutové (horizontální) rovině. Matematicky je definován jako odmocnina ze střední kvadratické hodnoty (RMS) úhlového rozdělení příchozího výkonu signálu, typicky měřená ve stupních. ASA kvantifikuje, jak je energie signálu rozprostřena napříč různými azimutovými úhly, což přímo ovlivňuje prostorovou korelaci mezi anténními prvky a účinnost prostorových zpracovatelských technik, jako je beamforming a prostorové multiplexování.

V praktické implementaci se ASA odhaduje z měření kanálu získaných pomocí referenčních signálů nebo sondovacích procedur. Přijímač vypočítá výkonové úhlové spektrum (PAS) analýzou prostorové kovarianční matice přijímaných signálů napříč anténními prvky. Z tohoto PAS se ASA spočítá jako směrodatná odchylka úhlového rozdělení, často vážená výkonem každé vícecestné složky. Tento odhad vyžaduje přesné informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a správnou kalibraci antén, protože chyby ve fázovém sladění mezi anténními prvky mohou zkreslit měření ASA.

ASA hraje klíčovou roli v návrhu a optimalizaci [MIMO](/mobilnisite/slovnik/mimo/) systémů. V prostředích s nízkou ASA (typicky pod 10 stupni) vykazují kanály vysokou prostorovou korelaci, což je činí vhodnými pro beamforming, ale omezuje zisky prostorového multiplexování. Naopak prostředí s vysokou ASA (typicky nad 30 stupni) poskytují bohaté rozptylování, které umožňuje efektivní prostorové multiplexování a vyšší řády MIMO. Síťové zařízení používá měření ASA k dynamickému výběru mezi přenosovými režimy – přepíná mezi beamformingem pro rozšíření pokrytí a prostorovým multiplexováním pro zvýšení kapacity na základě aktuálních podmínek kanálu.

Parametr je nedílnou součástí kanálových modelů 3GPP, zejména prostorového kanálového modelu (SCM) a jeho vývojových verzí. Tyto modely používají ASA jako klíčový vstupní parametr pro generování realistických realizací kanálu pro simulace systémů a hodnocení výkonu. Různé scénáře nasazení (urban macro, urban micro, rural atd.) mají charakteristická rozdělení ASA, která musí být přesně modelována pro predikci reálného výkonu systému. ASA také ovlivňuje rozhodování o předávání hovoru (handover) v systémech založených na beamforming, protože rychlé změny ASA mohou naznačovat, že se uživatel pohybuje do jiného prostředí šíření, které vyžaduje jiné strategie správy beamů.

## K čemu slouží

ASA byl zaveden, aby poskytl standardizovanou metriku pro kvantifikaci prostorových charakteristik rádiových kanálů, což se stalo stále důležitějším s přijetím [MIMO](/mobilnisite/slovnik/mimo/) technologie v systémech 3GPP. Před formální definicí ASA projektanti systémů postrádali konzistentní metody pro charakterizaci úhlové disperze, což vedlo k nekompatibilním kanálovým modelům a suboptimálním návrhům anténních systémů napříč různými dodavateli a nasazeními. Parametr řeší základní potřebu porozumět tomu, jak vícecestné složky přicházejí k přijímači, za účelem optimalizace prostorových zpracovatelských algoritmů.

S vývojem od jednoanténních k víceanténním systémům ve 3GPP Release 8 a novějších se přesná prostorová charakterizace kanálu stala nezbytnou pro dosažení slibovaných zisků MIMO technologie. ASA umožňuje síťovému zařízení přizpůsobit přenosové strategie na základě rozptylového prostředí – používat beamforming ve scénářích s nízkou disperzí pro zlepšení pokrytí a prostorové multiplexování ve scénářích s vysokou disperzí pro zvýšení kapacity. Tento adaptivní přístup maximalizuje spektrální účinnost napříč různými scénáři nasazení.

Parametr také podporuje plánování a optimalizaci sítě tím, že poskytuje kvantitativní metriky pro klasifikaci prostředí šíření. Operátoři mohou použít měření ASA z terénních zkoušek nebo drive testů ke kategorizaci buněčných stanic do různých tříd šíření, což umožňuje přesnější plánování kapacity a konfiguraci anténních systémů. V systémech massive MIMO a beamformingu zavedených v pozdějších releasech se ASA stala ještě kritičtější pro určení vhodné šířky beamu a strategií správy beamů k udržení spolehlivého připojení pro mobilní uživatele.

## Klíčové vlastnosti

- Kvantifikuje horizontální úhlovou disperzi příchozích vícecestných signálů
- Měřen jako odmocnina ze střední kvadratické hodnoty (RMS) výkonového úhlového spektra ve stupních
- Kritický vstupní parametr pro prostorové kanálové modely 3GPP
- Umožňuje adaptivní výběr mezi režimy beamformingu a prostorového multiplexování
- Podporuje odhad anténní korelace pro predikci výkonu MIMO
- Používá se při správě beamů a rozhodování o předávání hovoru v systémech založených na beamforming

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [ASA na 3GPP Explorer](https://3gpp-explorer.com/glossary/asa/)
