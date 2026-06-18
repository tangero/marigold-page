---
slug: "sscm"
url: "/mobilnisite/slovnik/sscm/"
type: "slovnik"
title: "SSCM – Statistical Spatial Channel Model"
date: 2025-01-01
abbr: "SSCM"
fullName: "Statistical Spatial Channel Model"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sscm/"
summary: "Standardizovaný kanálový model pro simulaci a hodnocení pokročilých anténních technologií v 5G NR a novějších systémech. Statisticky reprezentuje šíření rádiových vln v různých prostředích (např. UMi,"
---

SSCM je standardizovaný statistický kanálový model pro 5G NR, který simuluje šíření rádiového signálu v různých prostředích modelováním parametrů, jako je rozprostření zpoždění a útlum na dráze, a je nezbytný pro hodnocení systémů Massive MIMO a beamforming.

## Popis

Statistical Spatial Channel Model (SSCM) je komplexní, geometrií založený stochastický kanálový model (GSCM) standardizovaný organizací 3GPP pro návrh, testování a hodnocení výkonu technologií rozhraní New Radio (NR), zejména těch zahrnujících pokročilé víceanténní systémy. Definovaný ve specifikacích jako TR 38.900 a TR 38.901 poskytuje matematický rámec pro statisticky přesnou simulaci rádiového přenosového kanálu mezi vysílačem (např. gNB) a přijímačem (např. UE). Model zachycuje prostorové charakteristiky kanálu, které jsou klíčové pro technologie jako Massive [MIMO](/mobilnisite/slovnik/mimo/), beamforming a multi-user MIMO.

SSCM funguje tak, že modeluje přenosovou dráhu jako kombinaci více clusterů. Každý cluster představuje skupinu vícecestných složek s podobnými vlastnostmi zpoždění a úhlu. Nejprve jsou ze statistických rozdělení specifických pro daný scénář (např. Urban Microcell (UMi), Urban Macrocell (UMa), Rural Macrocell (RMa), Indoor Office) vygenerovány klíčové parametry velkého rozsahu ([LSP](/mobilnisite/slovnik/lsp/)), jako je rozprostření zpoždění, úhlové rozprostření (azimutální a zenitové na straně příjmu i vysílání), stínování a útlum na dráze. Tyto LSP jsou na základě reálných měření vzájemně korelovány. Uvnitř každého clusteru jsou následně generovány parametry malého rozsahu, jako je zpoždění clusteru, výkon clusteru a úhly. Nakonec je impulsní odezva kanálu ([CIR](/mobilnisite/slovnik/cir/)) nebo kanálová matice H sestavena sečtením příspěvků všech clusterů a drah, přičemž zahrnuje anténní diagramy a geometrie anténních polí na obou stranách.

Model podporuje široký frekvenční rozsah od pásem pod 6 GHz až po milimetrové vlny (mmWave), jako je 52,6 GHz a výše. Zahrnuje klíčové vlastnosti, jako jsou podmínky přímé viditelnosti ([LOS](/mobilnisite/slovnik/los/)) a nepřímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)), modely zastínění pro mmWave a prostorovou konzistenci. Prostorová konzistence zajišťuje, že se charakteristiky kanálu pro pohybující se UE plynule vyvíjejí v čase a prostoru, což je zásadní pro hodnocení výkonu mobility a algoritmů sledování paprsku. Tím, že poskytuje společný realistický referenční model, umožňuje SSCM spravedlivé srovnání různých anténních schémat, simulace na úrovni spoje a systému a odvození klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)) pro systémy 5G NR.

## K čemu slouží

Vývoj SSCM byl motivován omezeními předchozích kanálových modelů (jako modely [SCM](/mobilnisite/slovnik/scm/)/[SCME](/mobilnisite/slovnik/scme/) pro 3G/4G) v řešení nových výzev 5G. Předchozí modely nebyly navrženy pro vyšší frekvence (mmWave), rozsáhlé použití beamformingu nebo masivní měřítko anténních polí plánovaných pro 5G. Byla zde potřeba jednotného modelu, který by dokázal přesně zachytit prostorové vlastnosti kanálu v širokém rozsahu frekvencí, šířek pásma a scénářů nasazení.

Jeho primárním účelem je sloužit jako spolehlivý nástroj pro standardizaci a vývoj technik fyzické vrstvy 5G NR. Použitím společného, dohodnutého kanálového modelu mohou různé společnosti a výzkumníci simulovat a porovnávat výkon navrhovaných technologií (např. nových kódovacích schémat, referenčních signálů, procedur správy paprsků) za konzistentních a realistických podmínek. To je klíčové pro dosažení konsenzu během zasedání standardizace 3GPP. Dále pomáhá výrobcům síťových zařízení a mobilním operátorům navrhovat a optimalizovat své produkty a nasazení tím, že umožňuje pochopit, jak budou pokročilé funkce jako Massive MIMO fungovat v reálných prostředích, jako jsou husté městské oblasti nebo vnitřní továrny. SSCM řeší specifické výzvy šíření mmWave, jako je vysoký útlum na dráze a citlivost na zastínění, což byla mezera v předchozích modelech.

## Klíčové vlastnosti

- Geometrií založený stochastický model podporující frekvence od 0,5 GHz do 100 GHz
- Definuje více scénářů nasazení: UMi, UMa, RMa, Indoor Hotspot apod., se stavy LOS/NLOS
- Modeluje parametry velkého rozsahu (rozprostření zpoždění, úhlové rozprostření, stínování) s korelací mezi parametry
- Generuje clustery vícecestných složek s únikem malého rozsahu a prostorovou konzistencí
- Zahrnuje podporu pro 3D anténní diagramy a libovolné geometrie anténních polí (ULA, UPA)
- Obsahuje modely zastínění a útlumu průnikem, klíčové pro simulace v milimetrových vlnových pásmech

## Definující specifikace

- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [SSCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sscm/)
