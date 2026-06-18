---
slug: "trxua"
url: "/mobilnisite/slovnik/trxua/"
type: "slovnik"
title: "TRXUA – Transceiver Unit Array"
date: 2020-01-01
abbr: "TRXUA"
fullName: "Transceiver Unit Array"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/trxua/"
summary: "Pole jednotek transceiverů (Transceiver Unit Array, TRXUA) je soubor více jednotek transceiverů (TRXU) integrovaných do jednoho modulu nebo subsystému. Umožňuje pokročilé anténní techniky, jako je Mas"
---

TRXUA je soubor více jednotek transceiverů (Transceiver Unit) integrovaných do jednoho modulu, který umožňuje pokročilé anténní techniky, jako je Massive MIMO a beamforming, pro sítě 5G.

## Popis

Pole jednotek transceiverů (Transceiver Unit Array, TRXUA) představuje pokročilou hardwarovou architekturu, ve které je více jednotlivých jednotek transceiverů ([TRXU](/mobilnisite/slovnik/trxu/)) integrováno do souvislé poleové struktury. Toto pole je klíčovým prvkem pro aktivní anténní systémy ([AAS](/mobilnisite/slovnik/aas/)) a zejména pro technologii Massive Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)). Na rozdíl od jedné TRXU obsluhující jeden nebo dva anténní porty integruje TRXUA desítky nebo dokonce stovky TRXU, z nichž každá je připojena ke konkrétnímu anténnímu prvku v rámci většího panelu pole.

Architektura TRXUA je vysoce integrovaná a paralelizovaná. Skládá se z husté agregace základních komponent TRXU – [DAC](/mobilnisite/slovnik/dac/), [ADC](/mobilnisite/slovnik/adc/), [PA](/mobilnisite/slovnik/pa/), [LNA](/mobilnisite/slovnik/lna/), mixérů a filtrů – ale je navržena vysoce miniaturním a synchronizovaným způsobem. Centrální řadič v rámci pole spravuje kalibraci, synchronizaci a řízení zesílení/fáze napříč všemi jednotlivými cestami TRXU. Tato přesná kontrola amplitudy a fáze signálu u každého anténního prvku je tím, co umožňuje digitální beamforming. TRXUA spolupracuje s výkonným procesorem základního pásma, který spouští složité algoritmy pro výpočet optimálních beamformingových vah pro každou TRXU v poli, dynamicky tvaruje a nasměrovává rádiové paprsky ke konkrétním uživatelům.

V síti je TRXUA typicky jádrem rádiové jednotky AAS. Jejím úkolem je poskytnout masivní počet paralelních rádiových řetězců vyžadovaných pro prostorové multiplexování a potlačení interference. Tím, že současně obsluhuje více uživatelů na stejném časově-frekvenčním zdroji (multi-user MIMO) a směrově soustřeďuje energii, TRXUA výrazně zlepšuje kapacitu sítě, pokrytí na okrajích buňky a spektrální účinnost. Pro 5G NR, které primárně pracuje v pásmech středních (např. 3,5 GHz) a vysokých (mmWave) frekvencí, je TRXUA nezbytná kvůli kratším vlnovým délkám, které umožňují umístit mnoho anténních prvků do praktického formátu, čímž se pokročilý beamforming stává nejen výhodným, ale i nutným pro překonání vyšších útlumů na dráze.

## K čemu slouží

TRXUA byla vytvořena k překonání omezení tradičních pasivních anténních systémů a [MIMO](/mobilnisite/slovnik/mimo/) s malým rozsahem. Když se mobilní sítě potýkaly s exponenciálním růstem poptávky po datech, pouhé přidávání dalších makro stanovišť nebo spektra se stalo ekonomicky a fyzicky náročným. Průmysl potřeboval průlom ve spektrální účinnosti. TRXUA to umožňuje tím, že realizuje teoretické výhody Massive MIMO, technologie identifikované jako základní kámen pro 5G.

Motivace vychází z potřeby provádět sofistikované prostorové zpracování signálu. Předchozí hardwarové vybavení RAN, s pouze 2, 4 nebo 8 cestami transceiverů, mohlo podporovat pouze omezený beamforming a prostorové multiplexování. TRXUA to řeší škálováním počtu rádiových řetězců nákladově efektivně a v rámci zvládnutelné spotřeby energie a velikosti. Řeší kritické problémy, jako je poskytování konzistentního pokrytí ve vysokofrekvenčních pásmech (kde signály rychle slábnou), správa interference v ultra-hustých sítích a podpora obrovského počtu připojených zařízení. Její vývoj byl poháněn pokroky v návrhu integrovaných obvodů, technologii RF polovodičů (např. GaN) a digitálním zpracování signálu, což umožnilo integraci celého pole transceiverů do jediné, nasaditelné jednotky.

## Klíčové vlastnosti

- Integruje velký počet jednotlivých TRXU (např. 32, 64, 128+) do jednoho modulu
- Umožňuje digitální beamforming prostřednictvím nezávislé kontroly amplitudy a fáze na prvek
- Základní součást aktivních anténních systémů (AAS) a rádiových jednotek Massive MIMO
- Podporuje multi-user MIMO (MU-MIMO) pro současné prostorové multiplexování
- Obsahuje integrované kalibrační sítě pro synchronizaci a konzistenci pole
- Navržena pro vysokou integraci za účelem minimalizace velikosti, hmotnosti a spotřeby energie (SWaP)

## Související pojmy

- [TRXU – Transceiver Unit](/mobilnisite/slovnik/trxu/)

## Definující specifikace

- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background
- **TS 38.817** — 3GPP TR 38.817
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study

---

📖 **Anglický originál a plná specifikace:** [TRXUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/trxua/)
