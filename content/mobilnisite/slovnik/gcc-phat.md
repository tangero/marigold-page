---
slug: "gcc-phat"
url: "/mobilnisite/slovnik/gcc-phat/"
type: "slovnik"
title: "GCC-PHAT – Generalized Cross-Correlation with Phase Transform"
date: 2025-01-01
abbr: "GCC-PHAT"
fullName: "Generalized Cross-Correlation with Phase Transform"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gcc-phat/"
summary: "GCC-PHAT je algoritmus pro odhad časového rozdílu příchodu (TDoA) s vysokým rozlišením používaný pro lokalizaci akustického zdroje. V 3GPP je specifikován pro vylepšení určování polohy, zejména pro lo"
---

GCC-PHAT je algoritmus pro odhad časového rozdílu příchodu (TDoA) s vysokým rozlišením, specifikovaný v 3GPP pro určování polohy UE, který bělí fázové spektrum za účelem zvýšení přesnosti v dozvukovém prostředí.

## Popis

Generalized Cross-Correlation with Phase Transform (GCC-PHAT) je pokročilý algoritmus zpracování signálu používaný k odhadu časového rozdílu příchodu (TDoA) signálu přijatého dvěma nebo více mikrofony či senzory. V kontextu 3GPP je standardizován v TS 26.253 jako součást rámce pro určování polohy, konkrétně pro použití v akustických lokalizačních systémech, kde může uživatelské zařízení (UE) určit svou polohu nasloucháním zvukovým signálům z pevných reproduktorů se známou polohou (např. v nákupním centru nebo na letišti). Algoritmus funguje tak, že vypočítá vzájemnou korelaci mezi signály přijatými dvěma senzory a aplikuje specifickou váhovou funkci na reprezentaci ve frekvenční oblasti, aby zvýraznil vrchol TDoA.

Z architektonického hlediska pro určování polohy v 3GPP systém zahrnuje Akustický lokalizační server (APS), který spravuje akustické majákové vysílače (reproduktory), a UE s mikrofonem. Reproduktory vysílají známé, neslyšitelné akustické signály (často pískoty nebo kódované sekvence). Mikrofon UE tyto signály zachytí. Lokalizační software v UE následně zpracuje zachycený zvuk aplikací algoritmu GCC-PHAT po dvojicích mezi referenčním signálem (známá vyslaná sekvence) a přijatým signálem, nebo mezi signály přijatými v různých časech, pokud má UE pouze jeden mikrofon a pohybuje se. Základními výpočetními komponentami jsou rychlá Fourierova transformace ([FFT](/mobilnisite/slovnik/fft/)), výpočet fázové vzájemné výkonové spektrální hustoty, inverzní FFT a detekce vrcholu.

Jak funguje: Nejprve jsou přijaté zvukové signály z mikrofonu(ů) digitalizovány a předzpracovány (např. filtrovány, okenovány). Pro dvojici signálů (nebo přijatý signál a referenční signál) se vypočítá jejich vzájemná výkonová spektrální hustota. Klíčovým krokem PHAT je vážení této vzájemné výkonové spektrální hustoty převrácenou hodnotou její velikosti, čímž se efektivně zachová pouze fázová informace – to je 'fázová transformace'. Tento proces bělení potlačuje vliv amplitudového spektra signálu, což je výhodné, protože činí korelační vrchol ostřejším a odolnějším vůči akustice prostředí, jako je dozvuk a šum, které ovlivňují amplitudu signálu. Inverzní FFT tohoto váženého spektra dává funkci zobecněné vzájemné korelace. Časové zpoždění odpovídající maximálnímu vrcholu této funkce je odhadnutý TDoA. S odhady TDoA z více dvojic majáků lze polohu UE vypočítat pomocí hyperbolické laterace.

Její role v ekosystému 3GPP spočívá v tom, že je vysoce přesnou komponentou pro doplňkové lokalizační technologie, zejména pro vnitřní scénáře, kde jsou signály [GNSS](/mobilnisite/slovnik/gnss/) slabé nebo nedostupné. Specifikací GCC-PHAT ve standardu 3GPP zajišťuje konzistentní a vysoce výkonné implementace akustického určování polohy napříč různými UE a infrastrukturou, což umožňuje služby založené na poloze, navigaci a určení polohy volajícího v nouzi i uvnitř složitých budov. Představuje integraci pokročilých technik [DSP](/mobilnisite/slovnik/dsp/) do standardů mobilních sítí za účelem splnění přísných požadavků na určování polohy pro 5G a další generace.

## K čemu slouží

GCC-PHAT byl začleněn do standardů 3GPP, aby řešil kritickou výzvu přesného určování polohy uvnitř budov. Tradiční metody určování polohy založené na mobilních sítích, jako je [OTDOA](/mobilnisite/slovnik/otdoa/) využívající rádiové signály, mohou uvnitř budov selhávat kvůli vícecestnému šíření a útlumu signálu. Podobně je [GNSS](/mobilnisite/slovnik/gnss/) často uvnitř budov nedostupný. Byla zde zřejmá motivace standardizovat doplňkové vysoce přesné technologie a akustické určování polohy se ukázalo jako slibné řešení díky všudypřítomnosti mikrofonů a reproduktorů v UE a infrastruktuře.

Hlavním problémem, který GCC-PHAT řeší, je spolehlivý odhad časových zpoždění v akusticky náročném prostředí. Jednoduché metody vzájemné korelace jsou vysoce náchylné k dozvuku a šumu v pozadí, což může rozmazat nebo vytvořit falešné korelační vrcholy, což vede k velkým chybám TDoA. Váhování PHAT tyto efekty specificky zmírňuje tím, že zdůrazňuje fázovou informaci, která je v dozvukových podmínkách stabilnější než amplituda. Výsledkem je ostřejší, jednoznačnější korelační vrchol, který umožňuje přesnost odhadu TDoA na úrovni centimetrů až decimetrů, což přímo vede k vyšší přesnosti určení polohy.

Historicky byl GCC-PHAT po desetiletí známým algoritmem ve výzkumu zpracování zvukového signálu a akustické lokalizace. Jeho standardizace v 3GPP Release 18 odráží snahu průmyslu splnit regulatorní (např. E911) a komerční požadavky na přesnou vnitřní lokalizaci. Řeší omezení předchozích nestandardizovaných nebo proprietárních akustických metod tím, že poskytuje definovaný, vysoce výkonný základní algoritmus. To zajišťuje interoperabilitu, umožňuje srovnávání výkonu a dává výrobcům zařízení a síťovým operátorům společný technický základ, na kterém mohou budovat škálovatelné služby vnitřního určování polohy jako součást plánu vývoje pro 5G Advanced a 6G.

## Klíčové vlastnosti

- Používá váhování fázovou transformací (PHAT) k bílení vzájemného výkonového spektra
- Poskytuje odhad časového rozdílu příchodu (TDoA) s vysokým rozlišením
- Odolný výkon v dozvukovém a hlučném akustickém prostředí
- Standardizovaný algoritmus zajišťuje interoperabilitu pro akustické určování polohy
- Umožňuje přesnost vnitřního určování polohy na úrovni centimetrů až decimetrů
- Může pracovat s jedním mikrofonem na pohybujícím se UE nebo s více mikrofony

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [GCC-PHAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/gcc-phat/)
