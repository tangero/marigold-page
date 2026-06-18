---
slug: "scme"
url: "/mobilnisite/slovnik/scme/"
type: "slovnik"
title: "SCME – Spatial Channel Model Extension"
date: 2025-01-01
abbr: "SCME"
fullName: "Spatial Channel Model Extension"
category: "Physical Layer"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/scme/"
summary: "SCME je pokročilý model rádiového kanálu používaný pro simulace MIMO a víceanténních systémů. Rozšiřuje základní modely, aby přesně reprezentoval prostorové charakteristiky včetně směru příchodu/odcho"
---

SCME je pokročilé rozšíření modelu rádiového kanálu pro MIMO simulace, které přesně reprezentuje prostorové charakteristiky, jako je směr příchodu a polarizace, v realistických podmínkách šíření.

## Popis

Spatial Channel Model Extension (SCME) je standardizovaný model kanálu vyvinutý 3GPP pro linkové a systémové simulace bezdrátových komunikačních systémů, zejména těch využívajících Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)) a pokročilé anténní technologie. Zavedený ve vydání 10 je definován v technických specifikacích 37.976 a 37.977. SCME je geometrický stochastický model kanálu, který rozšiřuje dřívější modely jako Spatial Channel Model ([SCM](/mobilnisite/slovnik/scm/)) poskytnutím vylepšených prostorových parametrů, aby lépe odrážel reálné podmínky šíření rádiového signálu. Modeluje bezdrátový kanál jako sadu diskrétních vícecestných komponent, z nichž každá je charakterizována parametry jako zpoždění, výkon, úhel příchodu (AoA), úhel odchodu (AoD) a polarizace.

Architektonicky SCME funguje generováním impulsních odezev kanálu pro specifikované scénáře, které zahrnují prostředí urban macro, urban micro a rural macro. Model definuje metodologii pro vytváření kanálových koeficientů, které se mění v čase a frekvenci, zachycující efekty jako fading, Dopplerovo rozprostření a prostorová korelace. Klíčové komponenty zahrnují definici klastrů (skupin vícecest) a paprsků v rámci klastrů, každý s přidruženými úhlovými rozprostřeními a poměry křížové polarizace. Model podporuje jak podmínky s přímou viditelností ([LOS](/mobilnisite/slovnik/los/)), tak bez přímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)) a umožňuje konfiguraci geometrií anténních polí na straně vysílače i přijímače.

Jak funguje: Simulace SCME začínají nastavením scénáře se specifickými parametry jako kmitočet nosné, šířka pásma a anténní konfigurace. Model generuje náhodné realizace kanálových cest na základě statistických rozdělení odvozených z měření. Pro každý simulační běh vypočítá komplexní kanálovou matici H pro každý anténní pár, zahrnující prostorové vlastnosti jako azimutální a elevanční úhly. To umožňuje hodnocení MIMO technik jako beamforming, prostorové multiplexování a diverzita. SCME je implementován v softwarových nástrojích a používán výzkumníky a inženýry k posouzení metrik výkonu systému jako propustnost, chybovost a kapacita za realistických kanálových podmínek, což zajišťuje, že konstrukční rozhodnutí jsou validována vůči standardizovaným měřítkům.

## K čemu slouží

SCME byl vytvořen, aby řešil omezení dřívějších modelů kanálu, jako je [SCM](/mobilnisite/slovnik/scm/), kterým chyběly dostatečné detaily pro hodnocení pokročilých [MIMO](/mobilnisite/slovnik/mimo/) a víceanténních systémů vznikajících v LTE-Advanced a novějších. Předchozí modely často příliš zjednodušovaly prostorové charakteristiky, což je činilo nevhodnými pro simulaci technologií jako 3D beamforming, massive MIMO a koordinovaný vícebodový přenos (CoMP). Potřeba přesnější reprezentace reálného šíření, včetně polarizace a elevančních úhlů, se stala kritickou s tím, jak anténní pole rostla na složitosti.

Rozšíření bylo motivováno posunem průmyslu k vyšším kmitočtovým pásmům a hustším sítím, kde prostorové vlastnosti významně ovlivňují výkon. SCME řeší problém nekonzistentních simulačních výsledků mezi různými dodavateli a výzkumnými skupinami poskytnutím společného, detailního rámce. Umožňuje spravedlivé srovnání algoritmů a systémových návrhů a zajišťuje, že tvrzení o výkonu jsou založena na realistických kanálových podmínkách. Tato standardizace je zásadní pro vývoj a certifikaci bezdrátového zařízení od základnových stanic po uživatelská zařízení.

Historicky byly modely kanálu často proprietární nebo omezené na specifické scénáře, což bránilo spolupráci a inovacím. SCME, jako součást standardů 3GPP, nabízí jednotný přístup, který podporuje široké spektrum kmitočtů (až do 6 GHz zpočátku, s rozšířeními pro vyšší pásma) a scénářů nasazení. Byl klíčový pro vývoj 4G a 5G, umožňující inženýrům optimalizovat anténní návrhy, hodnotit nové rádiové funkce a předpovídat reálné chování před nákladnými terénními testy, čímž urychluje adopci technologií a snižuje vývojová rizika.

## Klíčové vlastnosti

- Geometrické stochastické modelování vícecestného šíření
- Podpora simulací MIMO a víceanténních systémů
- Detailní prostorové parametry včetně azimutálních/elevančních úhlů a polarizace
- Definované scénáře: urban macro, urban micro, rural macro (LOS/NLOS)
- Konfigurovatelné geometrie anténních polí a kmitočty nosných
- Standardizovaná metodologie pro reprodukovatelné realizace kanálu

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [SCM – Single-Connection Mode](/mobilnisite/slovnik/scm/)

## Definující specifikace

- **TR 37.976** (Rel-19) — MIMO OTA Test Methodology Study
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology

---

📖 **Anglický originál a plná specifikace:** [SCME na 3GPP Explorer](https://3gpp-explorer.com/glossary/scme/)
