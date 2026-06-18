---
slug: "ncrt"
url: "/mobilnisite/slovnik/ncrt/"
type: "slovnik"
title: "NCRT – Neighbour Cell Relation Table"
date: 2025-01-01
abbr: "NCRT"
fullName: "Neighbour Cell Relation Table"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ncrt/"
summary: "Databáze v síťovém uzlu, jako je gNB nebo eNB, která ukládá informace o sousedních buňkách. Je klíčová pro optimalizaci rozhodnutí o předání spojení, vyrovnávání zatížení a výkonu sítě tím, že udržuje"
---

NCRT je databáze v síťovém uzlu, která ukládá informace o sousedních buňkách za účelem optimalizace rozhodnutí o předání spojení, vyrovnávání zatížení a výkonu sítě.

## Popis

Tabulka vztahů se sousedními buňkami (Neighbour Cell Relation Table, NCRT) je základní řídicí entitou v rádiové přístupové síti (RAN), která se nachází konkrétně v síťových uzlech, jako je gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE. Funguje jako strukturovaná databáze, která eviduje topologické a provozní vztahy mezi obsluhující buňkou a jejími okolními sousedními buňkami. Tabulka není statická; je dynamicky naplňována a aktualizována automatizovanými procesy, jako jsou funkce automatického určování sousedních vztahů ([ANR](/mobilnisite/slovnik/anr/)), a manuální konfigurací od provozovatelů sítě. Ukládané informace typicky zahrnují identifikátory buněk (jako Physical Cell Identity ([PCI](/mobilnisite/slovnik/pci/)) a Cell Global Identity ([CGI](/mobilnisite/slovnik/cgi/))), údaje o frekvenci a šířce pásma a klíčové ukazatele výkonu související s kvalitou rádiového spoje a úspěšností předání spojení mezi dvojicemi buněk.

Z architektonického hlediska je NCRT logická komponenta integrovaná do softwaru řídicí a managementové roviny uzlu RAN. Rozhraní má k mechanismům hlášení měření od uživatelského zařízení (UE) a k signalizačním protokolům mezi uzly, jako je [X2](/mobilnisite/slovnik/x2/) (v LTE) nebo Xn (v 5G NR). Když UE hlásí měření detekovaných sousedních buněk, funkce ANR tato data použije k objevení neznámých sousedů a aktualizaci NCRT. Záznamy v tabulce definují povahu vztahu, například zda je předání spojení na konkrétního souseda povoleno, zakázáno nebo podmíněno, a tvoří základ pro seznam vztahů se sousedy (Neighbour Relation List, NRL) buňky.

Její role v síti je klíčová pro správu mobility. NCRT poskytuje nezbytná data pro algoritmus předání spojení k vyhodnocení kandidátských cílových buněk. Udržováním historických dat o úspěšnosti/neúspěšnosti předání spojení a relativní síle signálu může síť činit informovanější, robustnější a efektivnější rozhodnutí o předání spojení, což snižuje počet přerušených hovorů a selhání rádiového spoje. Dále podporuje pokročilé funkce RAN, jako je optimalizace robustnosti mobility ([MRO](/mobilnisite/slovnik/mro/)) a vyrovnávání zatížení, kde je pochopení vztahů mezi buňkami klíčové pro přerozdělování provozu a optimalizaci využití prostředků v topologii sítě.

## K čemu slouží

NCRT byla vytvořena, aby řešila kritickou potřebu automatizované, přesné a efektivní správy vztahů mezi sousedními buňkami v moderních mobilních sítích. V raných sítích byly seznamy sousedů konfigurovány zcela manuálně inženýry, což byl časově náročný proces náchylný k lidské chybě a obtížně udržitelný, jak sítě houstly a stávaly se složitějšími s přidáváním malých buněk a heterogenních nasazení. Manuální chyby, jako je opomenutí vztahu se sousedem nebo chybná konfigurace parametru buňky, mohly přímo vést k neúspěšným předáním spojení, přerušeným hovorům a špatnému uživatelskému zážitku.

Zavedení NCRT spolu s funkcí [ANR](/mobilnisite/slovnik/anr/) automatizovalo objevování a správu těchto vztahů. Tím byl vyřešen problém škálovatelnosti, což umožnilo sítím samokonfiguraci a samoptimalizaci při nasazování nových buněk. NCRT poskytuje centralizované, dynamické úložiště, které odráží rádiové prostředí v reálném čase, a umožňuje síti přizpůsobit se změnám, jako jsou výpadky buněk nebo nasazení nové infrastruktury. Její účel přesahuje základní konektivitu; je základním prvkem pro funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), které jsou nezbytné pro snížení provozních nákladů (OPEX) a udržení kvality služeb ve velkých a vyvíjejících se sítích.

## Klíčové vlastnosti

- Dynamické naplňování prostřednictvím funkce automatického určování sousedních vztahů (ANR)
- Ukládá identifikátory sousedních buněk (PCI, CGI), frekvence a duplexní režimy
- Udržuje metriky výkonu související s předáním spojení a atributy vztahu (např. No Handover, No Remove)
- Poskytuje základní data pro vytvoření seznamu vztahů se sousedy (NRL) používaného při řízení předání spojení
- Podporuje vztahy se sousedy mezi různými rádiovými přístupovými technologiemi (inter-RAT) (např. mezi buňkami NR a LTE)
- Umožňuje algoritmy optimalizace robustnosti mobility (MRO) a vyrovnávání zatížení

## Definující specifikace

- **TS 32.511** (Rel-19) — ANR Management Concepts & Requirements
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [NCRT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncrt/)
