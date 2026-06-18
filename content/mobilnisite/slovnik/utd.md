---
slug: "utd"
url: "/mobilnisite/slovnik/utd/"
type: "slovnik"
title: "UTD – Uniform Theory of Diffraction"
date: 2025-01-01
abbr: "UTD"
fullName: "Uniform Theory of Diffraction"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/utd/"
summary: "Model šíření vysokofrekvenčních elektromagnetických vln používaný v modelování kanálů 3GPP. Poskytuje rigorózní matematický rámec pro predikci rozptylu a difrakce rádiových vln na překážkách, jako jso"
---

UTD je model šíření vysokofrekvenčních elektromagnetických vln používaný v modelování kanálů 3GPP pro predikci rozptylu a difrakce rádiových vln na překážkách za účelem přesné simulace bezdrátového kanálu.

## Popis

Uniformní teorie difrakce (UTD) je asymptotická vysokofrekvenční technika pro řešení problémů elektromagnetického rozptylu, zejména difrakce rádiových vln na hranách, rozích a zakřivených površích. V kontextu norem 3GPP, konkrétně v rámci specifikací modelu kanálu (např. TR 38.900, TR 38.901), je UTD používána jako základní složka pro deterministické nebo semideterministické paprskové modelování kanálu. Tyto modely jsou klíčové pro simulaci a charakterizaci prostředí šíření rádiových vln ve scénářích definovaných pro 5G NR a novější systémy, jako je Urban Microcell (UMi), Urban Macrocell (UMa) a Indoor Hotspot (InH). Na rozdíl od jednodušších statistických modelů umožňuje paprskové trasování rozšířené o UTD přesný výpočet útlumu na dráze, rozprostření zpoždění, úhlu příchodu a odchodu tím, že bere v úvahu geometrii prostředí a fyzickou interakci elektromagnetických vln s objekty.

Základní princip UTD je rozšířením geometrické optiky (GO). Zatímco GO přesně modeluje přímé (přímé viditelnosti) a odražené paprsky, selhává v zastíněných oblastech za překážkami. UTD zavádí difraktované paprsky, které vznikají na hranách, hranolech nebo rozích konstrukcí, a poskytuje tak spojité a uniformní řešení pole i v těchto přechodových zónách. Teorie poskytuje 'difrakční koeficienty' – komplexní vzorce závislé na geometrii difrakční hrany, polarizaci dopadající vlny a pozorovacím úhlu. Při integraci do simulačního enginu pro 'ray-launching' nebo 'ray-tracing' simulátor identifikuje potenciální difrakční body (např. střechy a rohy budov). Pro každou dráhu paprsku zahrnující difrakci se vypočítají UTD koeficienty pro určení amplitudy, fáze a stavu polarizace difraktované složky pole.

V rámci prostorového modelu kanálu 3GPP přispívá UTD k vytváření realistických impulsních odezev kanálu. Typická simulace může vyslat tisíce paprsků z vysílače. Dráha každého paprsku je sledována a jeho interakce (přímá, odražená, difraktovaná) s databází prostředí je vypočítána pomocí GO pro odraz a UTD pro difrakci. Součet všech těchto příspěvků paprsků v místě přijímače tvoří úplný kanál. Tato metoda je výpočetně náročná, ale poskytuje vysokou přesnost pro místně specifické plánování a pro generování referenčních modelů kanálů, které ověřují výkon systémů massive [MIMO](/mobilnisite/slovnik/mimo/), beamformingových a vysokofrekvenčních mmWave systémů. Její přesnost je prvořadá pro návrh sítí spoléhajících na přesné prostorové zpracování a pro vyhodnocení pokrytí v komplexních podmínkách bez přímé viditelnosti.

## K čemu slouží

UTD byla začleněna do modelování kanálů 3GPP, aby řešila omezení čistě statistických modelů šíření, zejména když se buněčné systémy vyvíjely směrem k vyšším frekvencím (jako mmWave v 5G) a složitějším anténním systémům (jako massive [MIMO](/mobilnisite/slovnik/mimo/)). Statistické modely, ač výpočetně efektivní, často postrádají prostorovou konzistenci a fyzikální přesnost potřebnou pro vyhodnocení pokročilých technologií, které jsou vysoce citlivé na konkrétní geometrii prostředí, jako je beamforming a multi-user MIMO. Účelem použití UTD je poskytnout fyzikálně podložený, deterministický základ pro predikci charakteristik kanálu v realistických, heterogenních scénářích nasazení.

Historická motivace vychází z potřeby standardizovaných, reprodukovatelných a důvěryhodných modelů kanálů pro ověřování výkonu nových rozhraní. Před jejím formálním zahrnutím používaly proprietární nástroje pro paprskové trasování různé aproximace. Standardizací na rigorózní teorii, jako je UTD, zajišťuje 3GPP, že různí výrobci zařízení a výzkumné instituce mohou dosáhnout srovnatelných simulačních výsledků, což vede ke spravedlivému a konzistentnímu hodnocení návrhů technologie 5G NR. Řeší problém přesného modelování šíření v hustých městských kaňonech, vnitřních kancelářských prostorech a kolem nepravidelného terénu, kde je difrakce dominantním mechanismem pro pronikání signálu do zastíněných oblastí.

Navíc, jak se nástroje pro plánování sítě vyvíjely pro podporu 3D prostředí digitálních dvojčat, vzrostla poptávka po predikci založené na fyzice. UTD poskytuje potřebný teoretický základ pro převod 3D databáze budov na kvantifikovatelný rádiový kanál, což umožňuje plánovačům sítí předpovídat díry v pokrytí, optimalizovat sklon a umístění antén a vyhodnocovat scénáře interference před fyzickým nasazením. Tato schopnost je klíčová pro nákladově efektivní zavádění 5G sítí s vysokou šířkou pásma a vysokou spolehlivostí.

## Klíčové vlastnosti

- Poskytuje uniformní asymptotické řešení pro problémy elektromagnetické difrakce
- Umožňuje přesné modelování šíření rádiových vln v zastíněných oblastech za překážkami
- Integruje se s geometrickou optikou (GO) pro úplný paprskový model kanálu
- Podporuje výpočet komplexních difrakčních koeficientů pro hrany, hranoly a rohy
- Usnadňuje generování prostorově konzistentní impulsní odezvy kanálu
- Nezbytná pro simulaci vysokofrekvenčních (mmWave) scénářů šíření a scénářů pro massive MIMO

## Definující specifikace

- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [UTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/utd/)
