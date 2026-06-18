---
slug: "vcat"
url: "/mobilnisite/slovnik/vcat/"
type: "slovnik"
title: "VCAT – Virtual Concatenation"
date: 2025-01-01
abbr: "VCAT"
fullName: "Virtual Concatenation"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vcat/"
summary: "Virtual Concatenation (VCAT) je technika transportní sítě, která seskupuje více nezávislých virtuálních kontejnerů (např. v SDH/SONET nebo OTN) do jediného logického kanálu za účelem dosažení vyšší ef"
---

VCAT je technika transportní sítě, která seskupuje více nezávislých virtuálních kontejnerů do jediného logického kanálu za účelem dosažení vyšší efektivity využití šířky pásma a flexibilní alokace kapacity.

## Popis

Virtual Concatenation (VCAT) je metoda používaná v synchronní digitální hierarchii ([SDH](/mobilnisite/slovnik/sdh/)), optické transportní síti (OTN) a podobných transportních technologiích k agregaci více virtuálních kontejnerů ([VC](/mobilnisite/slovnik/vc/)) nebo optických kanálových datových jednotek (ODU) do většího logického kanálu s vyšší šířkou pásma. Na rozdíl od tradiční souvislé konkatenace, která vyžaduje fyzicky sousední časové sloty, VCAT umožňuje, aby byly členské kontejnery přenášeny sítí nezávisle, případně po různých cestách, a následně znovu sestaveny v cílovém uzlu. Toho je dosaženo přiřazením společného skupinového identifikátoru, jako je štítek skupiny virtuální konkatenace (VCG), všem členům, spolu s pořadovými čísly pro zajištění správného opětovného sestavení i přes rozdílná zpoždění. V kontextech 3GPP je VCAT specifikováno v transportních specifikacích (např. 28.620 pro správu) a používá se v přenosových sítích mobilních sítí pro efektivní přenos agregovaného provozu ze stanic základnových stanic do jádrových uzlů.

Architektura VCAT zahrnuje tři klíčové komponenty: zdrojový adaptér, který segmentuje vysokorychlostní klientské signály do více členských kontejnerů, transportní síť, která tyto členy přenáší, případně po různých trasách, a cílový adaptér, který je znovu sestaví do původního signálu. Každý členský kontejner pracuje se standardní rychlostí (např. VC-12, VC-3, VC-4 v SDH) a je přepínán a spravován individuálně. Schéma úpravy kapacity spoje (LCAS) se často používá spolu s VCAT pro dynamické přidávání nebo odebírání členů ze skupiny bez přerušení služby, což umožňuje plynulé škálování šířky pásma. Tato dynamická schopnost je klíčová pro přizpůsobení se kolísajícím požadavkům na provoz v mobilních sítích, jako jsou ty způsobené denními vzorci využití nebo speciálními událostmi.

V provozu VCAT funguje tak, že distribuuje klientská data napříč členskými kontejnery pomocí techniky inverzního multiplexování. Ve zdroji jsou data rozdělena do proudů, které jsou namapovány do užitečného zatížení každého kontejneru, přičemž do režijních dat jsou vložena pořadová čísla pro sledování pořadí. Během přenosu síťové prvky zpracovávají každý kontejner nezávisle, což umožňuje flexibilní směrování a odolnost vůči výpadkům. V cíli jsou kontejnery uloženy do vyrovnávací paměti pro kompenzaci rozdílných zpoždění (zkosení), seřazeny podle pořadových čísel a zkombinovány pro rekonstrukci původního datového proudu. Role VCAT v sítích 3GPP spočívá v poskytování škálovatelného a efektivního transportního mechanismu pro přenosové spoje, zejména s rostoucími přenosovými rychlostmi mobilních dat při nasazení LTE a 5G. Umožňuje operátorům přírůstkově navyšovat kapacitu přidáváním dalších kontejnerů namísto výměny celých spojů, čímž snižuje kapitálové výdaje a zlepšuje agilitu sítě.

## K čemu slouží

Virtual Concatenation (VCAT) bylo vyvinuto za účelem překonání neefektivit tradiční konkatenace [SDH](/mobilnisite/slovnik/sdh/)/[SONET](/mobilnisite/slovnik/sonet/), která vyžadovala souvislé časové sloty a rigidní hierarchii šířky pásma (např. pouze násobky pevných rychlostí jako 155 Mbps). Toto omezení vedlo k uvíznuté (nevyužité) šířce pásma a špatnému využití, když požadavky služeb neodpovídaly standardním velikostem kontejnerů. VCAT, zavedené v telekomunikačních standardech a přijaté 3GPP ve verzi 11 pro správu transportu, tento problém vyřešilo tím, že umožnilo flexibilní alokaci šířky pásma prostřednictvím logického seskupování nesouvislých kontejnerů, což operátorům umožnilo 'přizpůsobit velikost' spojů pro různé služby, jako je Ethernetový přenos pro mobilní základnové stanice.

Motivace pro VCAT vycházela z rostoucí poptávky po datových službách a přechodu na paketově přepínané sítě, které vyžadovaly jemnější a přizpůsobitelnější transportní kapacity. Předchozí přístupy, jako je použití více samostatných spojů, byly složité na správu a neefektivní. VCAT v kombinaci s LCAS poskytlo dynamické řešení, které mohlo okamžitě upravovat šířku pásma, čímž řešilo trhaný charakter mobilního provozu a podporovalo cíle správy provozu. To bylo obzvláště důležité pro sítě 3GPP vyvíjející se směrem k LTE a dále, kde přenosová síť potřebovala podporovat vysokopropustná, nízkolatentní spojení pro rozšířené mobilní širokopásmové služby.

Oddělením logické šířky pásma od fyzických omezení VCAT umožnilo lepší využití zdrojů a úsporu nákladů v transportních sítích. Umožnilo síťovým operátorům využít stávající infrastrukturu SDH/OTN a zároveň akomodovat nové služby, čímž vyhladilo migraci na plně paketový transport. Zařazení VCAT do specifikací 3GPP (např. 28.620) standardizovalo jeho správu, zajistilo interoperabilitu mezi různými dodavateli a usnadnilo jeho nasazení v scénářích mobilního přenosu, což nakonec přispělo k efektivnějším a škálovatelnějším síťovým architekturám.

## Klíčové vlastnosti

- Flexibilní agregace šířky pásma kombinací nesouvislých virtuálních kontejnerů
- Podpora inverzního multiplexování pro distribuci provozu přes více cest
- Číslování pořadí a kompenzace zkosení pro přesné opětovné sestavení
- Integrace se schématem úpravy kapacity spoje (LCAS) pro dynamické změny šířky pásma
- Kompatibilita s transportními technologiemi SDH, SONET a OTN
- Vylepšené využití zdrojů a snížení uvízlé (nevyužité) šířky pásma

## Související pojmy

- [SDH – Synchronous Digital Hierarchy](/mobilnisite/slovnik/sdh/)

## Definující specifikace

- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM

---

📖 **Anglický originál a plná specifikace:** [VCAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/vcat/)
