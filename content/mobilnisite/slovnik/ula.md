---
slug: "ula"
url: "/mobilnisite/slovnik/ula/"
type: "slovnik"
title: "ULA – Uniform Linear Array"
date: 2025-01-01
abbr: "ULA"
fullName: "Uniform Linear Array"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ula/"
summary: "Základní konfigurace anténního pole, ve které jsou vyzařovací prvky uspořádány v přímce se stejnými rozestupy. Je klíčová pro formování svazku a prostorové filtrování v MIMO systémech, umožňuje přesný"
---

ULA je základní konfigurace anténního pole, ve které jsou vyzařovací prvky uspořádány v přímce se stejnými rozestupy, což umožňuje formování svazku pro směrový přenos a příjem signálu v MIMO systémech.

## Popis

Uniform Linear Array (ULA) je specifický typ architektury anténního pole, který je zásadní pro moderní systémy bezdrátové komunikace, zejména v aplikacích [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) a formování svazku. V ULA je více anténních prvků uspořádáno podél jedné přímky (osy) s konstantním, rovnoměrným rozestupem mezi prvky, typicky zlomkem vlnové délky (např. polovina vlnové délky). Tato pravidelná geometrická struktura je matematicky dobře zpracovatelná a tvoří základ mnoha algoritmů digitálního zpracování signálu používaných pro prostorové zpracování signálu. Primární funkcí ULA je poskytnout směrové řízení vysílaných nebo přijímaných rádiových vln. Aplikací specifických komplexních vah (amplitudových a fázových posunů) na signál u každého anténního prvku může pole konstruktivně kombinovat signály v požadovaném směru a destruktivně v jiných směrech, čímž vytváří řiditelný svazek. Tento proces, známý jako formování svazku nebo prostorové filtrování, umožňuje základnové stanici (gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v 4G) soustředit energii směrem ke konkrétnímu uživatelskému zařízení (UE), čímž se zvýší síla signálu pro tohoto uživatele a sníží se rušení pro ostatní.

Fungování ULA silně závisí na konceptu činitele pole, což je matematická funkce popisující vyzařovací charakteristiku pole na základě počtu prvků, jejich rozestupu a aplikovaného buzení (vah). Rovnoměrný rozestup je klíčový; zajišťuje předvídatelnou odezvu pole a zjednodušuje výpočet úhlů natočení svazku. S ULA se běžně používá digitální formování svazku (DBF), kde se vážení aplikuje v digitální základnové oblasti, což nabízí vysokou flexibilitu. Svazek lze elektronicky natáčet úpravou fázového posunu napříč prvky bez fyzického pohybu antény. Schopnost natáčení je definována geometrií pole; pro ULA s rozestupem polovina vlnové délky lze svazky typicky natáčet v sektoru 120 stupňů před polem. Čím více prvků ULA obsahuje, tím užší a směrovější se hlavní svazek stává, což vede k vyššímu anténnímu zisku a lepšímu prostorovému rozlišení, což je nezbytné pro podporu víceuživatelského MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)), kde základnová stanice obsluhuje více uživatelů současně na stejném časově-frekvenčním zdroji.

V rámci architektury 3GPP jsou ULA detailem implementace fyzické vrstvy pro Radio Access Network (RAN). Jsou základní součástí anténního systému na gNB. Jejich výkon přímo ovlivňuje klíčové funkce správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), jako je odhad kanálu, předkódování pro downlinkové přenosy a kombinování pro uplinkové příjmy. Specifikace jako 3GPP TS 37.840 a 38.878 definují požadavky a testovací metodologie pro aktivní anténní systémy ([AAS](/mobilnisite/slovnik/aas/)), které využívají pole jako ULA, a zajišťují tak interoperabilitu a výkon. V nasazeních massive MIMO může panel základnové stanice sestávat z více podpolí nebo většího dvourozměrného pole, ale princip ULA je často stavebním kamenem těchto složitějších struktur. Jeho úlohou je umožnit prostorové multiplexování, které je klíčové pro dosažení vysokých datových rychlostí, kapacity a spolehlivosti spoje slibovaných standardy 4G LTE-Advanced a 5G NR.

## K čemu slouží

ULA existuje, aby poskytla praktický a účinný prostředek pro manipulaci s prostorovými vlastnostmi rádiových vln pro vylepšenou bezdrátovou komunikaci. Základní problém, který řeší, je omezení tradičních všesměrových nebo sektorových antén, které vyzařují energii široce, plýtvají výkonem a vytvářejí rušení napříč buňkou. Umožněním elektronického formování svazku umožňuje ULA operátorům sítí přesně směrovat rádiovou energii tam, kde je potřeba – k uživateli – a pryč od míst, kde škodí. Toto prostorové zaměření řeší kritické problémy omezeného spektra a rušení, které jsou hlavními překážkami pro kapacitu sítě a uživatelský zážitek.

Historicky se směrového zisku dosahovalo pomocí velkých, mechanicky natáčených parabolických antén nebo pasivních anténních polí s pevnými charakteristikami. Ta byla nepružná, pomalá v přizpůsobování a nevhodná pro dynamická mobilní prostředí. Přechod na digitální systémy a technologii [MIMO](/mobilnisite/slovnik/mimo/) vytvořil potřebu agilních, softwarem řízených anténních systémů. ULA se svou jednoduchou lineární geometrií poskytla ideální model pro počáteční vývoj a nasazení adaptivních algoritmů formování svazku. Její matematická jednoduchost umožňuje efektivní výpočet vah pro formování svazku v reálném čase, což umožňuje její implementaci v komerčních základnových jednotkách. Rovnoměrný rozestup zajišťuje, že pro široký rozsah úhlů natočení jsou při rozestupu menším než vlnová délka (což je klíčový konstrukční požadavek) potlačeny parazitní laloky (nežádoucí vedlejší svazky).

Motivací pro standardizaci aspektů výkonu ULA v 3GPP, zejména od Release 12 s prací na Active Antenna Systems ([AAS](/mobilnisite/slovnik/aas/)), bylo zajistit, aby teoretické výhody formování svazku mohly být realizovány v interoperabilních, více-dodavatelských sítích. Jak se sítě vyvíjely směrem k 5G a využívaly vyšší kmitočtová pásma (jako mmWave), kde signály trpí větším útlumem na dráze, se zisk z formování svazku poskytovaný poli jako ULA stal nejen vylepšením, ale nutností pro udržení životaschopného pokrytí. ULA je tedy základní technologií, která umožňuje spektrální účinnost a řízení mobility založené na svazcích, jež jsou charakteristickými rysy pokročilých systémů 4G a 5G.

## Klíčové vlastnosti

- Lineární uspořádání anténních prvků s konstantním rozestupem mezi prvky
- Umožňuje elektronické formování svazku a natáčení nul pomocí úpravy komplexních vah
- Poskytuje vysokou směrovost a anténní zisk úměrný počtu prvků
- Zjednodušuje výpočet činitele pole a algoritmy digitálního zpracování signálu
- Základní stavební blok pro složitější planární (2D) a massive MIMO pole
- Podporuje techniky prostorového multiplexování, jako je MU-MIMO, pro zvýšení kapacity buňky

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [AAS – Active Antenna System](/mobilnisite/slovnik/aas/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO

---

📖 **Anglický originál a plná specifikace:** [ULA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ula/)
