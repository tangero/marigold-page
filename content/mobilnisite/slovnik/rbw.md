---
slug: "rbw"
url: "/mobilnisite/slovnik/rbw/"
type: "slovnik"
title: "RBW – Resolution Bandwidth"
date: 2025-01-01
abbr: "RBW"
fullName: "Resolution Bandwidth"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rbw/"
summary: "Rozlišovací šířka pásma (RBW) je klíčový parametr v rádiové frekvenční testovací a měřicí technice, který definuje šířku pásma mezifrekvenčního (IF) filtru používaného ve spektrálních analyzátorech. U"
---

RBW je nastavení šířky pásma mezifrekvenčního filtru ve spektrálním analyzátoru, které určuje jeho schopnost rozlišit těsně sousedící rádiové frekvenční signály pro přesné testování shody podle 3GPP.

## Popis

Rozlišovací šířka pásma (RBW) je základním nastavením ve spektrálních analyzátorech a dalších [RF](/mobilnisite/slovnik/rf/) testovacích zařízeních používaných pro charakterizaci 3GPP rádiových zařízení a sítí. Technicky RBW definuje šířku pásma nejužšího filtru v mezifrekvenčním ([IF](/mobilnisite/slovnik/if/)) stupni analyzátoru, kterým signál prochází během průchodu. Obvykle se udává v Hertzech (Hz) nebo kilohertzech (kHz). Filtr RBW je obvykle Gaussův nebo tvarovaný filtr, který určuje kmitočtovou selektivitu měření. Když analyzátor prochází kmitočtovým rozsahem, šířka pásma filtru RBW určuje, jak jemně dokáže rozlišit jednotlivé spektrální složky; užší RBW poskytuje lepší kmitočtové rozlišení, ale vyžaduje delší dobu průchodu kvůli pomalejší odezvě filtru.

Volba RBW přímo ovlivňuje několik charakteristik měření. Za prvé definuje minimální kmitočtovou vzdálenost, při které lze dvě sinusové vlny stejné amplitudy rozlišit jako dva samostatné vrcholy (obvykle je vyžadována vzdálenost větší než RBW). Za druhé RBW ovlivňuje zobrazenou průměrnou úroveň šumu (DANL); protože výkon šumu je úměrný šířce pásma, zmenšení RBW o faktor 10 sníží zobrazenou úroveň šumu o 10 dB, čímž se zlepší citlivost pro detekci nízkých signálů. To však probíhá na úkor prodloužení doby průchodu, protože užší filtr má delší ustalovací čas. Pro měření modulovaných signálů, jako jsou signály 3GPP nosných, musí být RBW nastavena dostatečně široká, aby zachytila podstatnou šířku pásma signálu bez zkreslení, ale zároveň optimalizovaná pro konkrétní požadavek testu (např. měření úniku do sousedního kanálu vyžaduje RBW menší než rozestup kanálů).

Ve specifikacích pro testování shody 3GPP (např. TS 25.141 pro testování základnových stanic, TS 36.791 pro [E-UTRA](/mobilnisite/slovnik/e-utra/)) testovací požadavky explicitně definují nastavení RBW pro různá měření, jako je maska spektrálních emisí, nežádoucí emise a obsazená šířka pásma. Automatizované testovací systémy konfigurují RBW podle těchto standardů, aby zajistily reprodukovatelné a kompatibilní výsledky. Moderní spektrální analyzátory často nabízejí automaticky propojená nastavení RBW, která spojují RBW s rozsahem nebo referenční úrovní, ale pro přesné testování podle standardů je povinné ruční nastavení podle specifikace 3GPP. Porozumění a správné použití RBW je tedy nezbytné pro RF inženýry provádějící validaci návrhu, předběžné testování shody a formální certifikaci 3GPP rádiového zařízení.

## K čemu slouží

Rozlišovací šířka pásma existuje jako klíčový řídicí parametr ve spektrální analýze pro zvládnutí základního kompromisu mezi kmitočtovým rozlišením, rychlostí měření a úrovní šumu. Rané spektrální analyzátory měly pevné [IF](/mobilnisite/slovnik/if/) šířky pásma, což omezovalo jejich univerzálnost. Zavedení nastavitelné RBW umožnilo inženýrům optimalizovat přístroj pro různé měřicí úlohy: úzká RBW pro detailní spektrální analýzu těsně sousedících signálů a široká RBW pro rychlé průchody nebo zachycení širokopásmových modulovaných signálů. Tato flexibilita vyřešila problém potřeby více specializovaných přístrojů pro různé scénáře [RF](/mobilnisite/slovnik/rf/) měření.

V kontextu norem 3GPP jsou konkrétní nastavení RBW nařízena v testovacích specifikacích, aby byla zajištěna konzistentní a srovnatelná měření napříč různými laboratořemi a dodavateli zařízení. Tím se řeší historický problém variability měření, kdy různá nastavení RBW mohla vést k různým výsledkům pro stejné testované zařízení, což komplikovalo certifikaci a způsobovalo problémy s interoperability. Formalizace RBW ve specifikacích 3GPP (počínaje 3G UMTS) byla motivována potřebou důsledného a opakovatelného testování RF shody, jak se buněčné technologie stávaly složitějšími s širšími šířkami pásma a přísnějšími emisními limity. Správná konfigurace RBW je nezbytná pro přesné měření kritických parametrů, jako jsou mimopásmové emise, které přímo ovlivňují koexistenci sítí a soulad s předpisy.

## Klíčové vlastnosti

- Definuje kmitočtovou selektivitu mezifrekvenčního filtru spektrálního analyzátoru
- Určuje schopnost rozlišit těsně sousedící spektrální složky
- Ovlivňuje zobrazenou průměrnou úroveň šumu (užší RBW snižuje úroveň šumu)
- Ovlivňuje dobu průchodu měření (užší RBW prodlužuje dobu průchodu)
- Specifikováno v normách pro testování shody 3GPP pro reprodukovatelné výsledky
- Často propojeno s šířkou pásma videa (VBW) pro vyhlazení signálu

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 37.806** (Rel-11) — Harmonized Frequency Variant Study for 806-894 MHz

---

📖 **Anglický originál a plná specifikace:** [RBW na 3GPP Explorer](https://3gpp-explorer.com/glossary/rbw/)
