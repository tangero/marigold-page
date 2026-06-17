---
slug: "nes"
url: "/mobilnisite/slovnik/nes/"
type: "slovnik"
title: "NES – Network Energy Savings"
date: 2025-01-01
abbr: "NES"
fullName: "Network Energy Savings"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nes/"
summary: "Soubor funkcí a mechanismů v 5G NR navržený ke snížení spotřeby energie rádiové přístupové sítě. Umožňuje dynamické přizpůsobení síťových zdrojů, jako je vypínání buněk a úpravy částí šířky pásma, na"
---

NES je soubor funkcí 5G NR navržený ke snížení spotřeby energie v rádiové přístupové síti dynamickým přizpůsobováním zdrojů, jako jsou buňky a šířka pásma, na základě vytížení provozu.

## Popis

Network Energy Savings (NES) je komplexní rámec v rámci specifikací 3GPP 5G New Radio (NR) zaměřený na optimalizaci energetické účinnosti gNB a celé RAN. Funguje inteligentním řízením provozního stavu síťových zdrojů v reakci na aktuální a predikované podmínky provozu. Základní princip spočívá v přechodu síťových prvků nebo specifických rádiových zdrojů do stavů s nízkou spotřebou během období nízké poptávky, čímž se snižuje spotřeba energie bez významného dopadu na uživatelský zážitek nebo dostupnost sítě.

Architektura NES je integrována do funkcí správy rádiových zdrojů (RRM) gNB a řídí se politikami, které vyvažují úspory energie s klíčovými výkonnostními ukazateli ([KPI](/mobilnisite/slovnik/kpi/)), jako je latence, propustnost a pokrytí. Mezi klíčové provozní mechanismy patří Cell [DTX](/mobilnisite/slovnik/dtx/) (Discontinuous Transmission), kdy buňka může dočasně ztlumit své vysílací signály, a Carrier Shutdown, který zahrnuje vypnutí celých nosných komponent. Dále NES využívá pokročilé režimy spánku pro rádiové jednotky a podporuje dynamické přizpůsobení částí šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), což umožňuje gNB pracovat s užším aktivním pásmem, když není vyžadována plná kapacita.

Implementace závisí na koordinaci mezi gNB-Central Unit (gNB-CU) a gNB-Distributed Unit (gNB-DU), jak je specifikováno v rozhraní F1. gNB-CU činí centralizovaná rozhodnutí na základě agregovaných informací o vytížení a může nařídit konkrétním [DU](/mobilnisite/slovnik/du/), aby přešly do stavů úspory energie. Tyto akce jsou často synchronizovány s funkcemi Self-Organizing Network (SON) pro automatizovanou optimalizaci. NES také definuje specifické signalizační a měřicí procedury, jako jsou zprávy Energy Saving Indication a Energy Saving Assistance Information, které usnadňují koordinaci mezi sousedními gNB a zajišťují, že při snížení aktivity buňky nevzniknou díry v pokrytí.

## K čemu slouží

NES byl zaveden, aby řešil rostoucí energetické náklady a environmentální dopady nasazování a provozu hustých 5G sítí. Protože 5G NR využívá širší šířky pásma, massive [MIMO](/mobilnisite/slovnik/mimo/) a vyšší hustotu buněk k dosažení svých výkonnostních cílů, spotřeba energie RAN se stala hlavním problémem pro operátory. Tradiční sítě často fungovaly s pevnými, trvale zapnutými přenosovými vzory, což vedlo k významnému plýtvání energií během období nízkého provozu, například přes noc. NES poskytuje nástroje, aby spotřeba energie sítě byla více úměrná její skutečné služební zátěži.

Vznik NES byl motivován ekonomickými i regulačními tlaky. Operátoři se snaží snížit provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)), jejichž podstatnou část tvoří náklady na energii. Zároveň roste společenská a vládní poptávka po ekologičtější telekomunikaci. NES to řeší tím, že umožňuje pružnější síťovou infrastrukturu. Překračuje jednoduché, statické režimy úspory energie a vytváří dynamický systém citlivý na provoz, který může provádět jemně odstupňované úpravy. To operátorům umožňuje zachovat kvalitu služeb a pokrytí při dosažení podstatného snížení spotřeby energie, což je klíčové pro udržitelné zavádění sítí 5G a budoucích sítí 6G.

## Klíčové vlastnosti

- Dynamická aktivace/deaktivace buněk (Cell Sleep) na základě vytížení provozu
- Diskontinuální vysílání (DTX) pro řídicí a referenční signály
- Vypnutí nosné (Carrier shutdown) pro sekundární komponentní nosné
- Adaptivní přepínání části šířky pásma (BWP) na užší a účinnější konfigurace
- Koordinace mezi gNB pro zajištění pokrytí během akcí úspory energie
- Integrace se SON pro automatizované řízení energie založené na politikách

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [NES na 3GPP Explorer](https://3gpp-explorer.com/glossary/nes/)
