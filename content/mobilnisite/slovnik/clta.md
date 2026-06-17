---
slug: "clta"
url: "/mobilnisite/slovnik/clta/"
type: "slovnik"
title: "CLTA – Co-Location Test Antenna"
date: 2025-01-01
abbr: "CLTA"
fullName: "Co-Location Test Antenna"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/clta/"
summary: "Standardizovaná testovací anténa používaná během testování shody základnových stanic k ověření, že více rádiových jednotek nebo transceiverů může správně fungovat při jejich fyzické společné lokalizac"
---

CLTA (zkontrolovací anténa pro společnou lokalizaci) je standardizovaná testovací anténa používaná při testování shody základnových stanic, která slouží k ověření, že společně lokalizované rádiové jednotky fungují správně bez způsobení nepřijatelného rušení.

## Popis

Co-Location Test Antenna (CLTA, zkontrolovací anténa pro společnou lokalizaci) je kritická součást konformního testovacího rámce 3GPP pro základnové stanice, konkrétně definovaná v 3GPP specifikacích TS 37.141 ([E-UTRA](/mobilnisite/slovnik/e-utra/), UTRA a GSM/[EDGE](/mobilnisite/slovnik/edge/) Multi-Standard Radio ([MSR](/mobilnisite/slovnik/msr/)) Base Station ([BS](/mobilnisite/slovnik/bs/)) conformance testing) a TS 38.141 (NR Base Station (BS) conformance testing). Nejde o anténu používanou v provozních sítích, nýbrž o standardizovanou testovací přípravku navrženou k simulaci podmínek nejhorší možné vazby mezi více rádiovými vysílači a přijímači, když jsou instalovány v těsné fyzické blízkosti uvnitř stejného krytu základnové stanice nebo na stejném anténním stožáru. Primární funkcí CLTA je vytvořit řízené, opakovatelné elektromagnetické prostředí, které testovacím laboratořím umožňuje ověřit, zda mohou více rádiové jednotky základnové stanice fungovat současně, aniž by si navzájem způsobovaly nepřijatelnou úroveň rušení, které by degradovalo citlivost přijímačů a celkový výkon systému.

CLTA funguje tak, že je během testování umístěna v určené, standardizované vzdálenosti a orientaci vůči provozním anténám základnové stanice. Její elektromagnetické charakteristiky – včetně vyzařovacího diagramu, polarizace a impedance – jsou v 3GPP specifikacích přesně definovány, aby byla zajištěna konzistence napříč různými testovacími domy a výrobci zařízení. Během testování společné lokalizace testovaná základnová stanice provozuje více transceiverů současně na různých kmitočtových pásmech nebo různých technologiích rádiového přístupu (jako například LTE a NR v Multi-Standard Radio). CLTA zachycuje vysílané signály a přivádí je zpět do přijímačů základnové stanice přes kalibrované cesty vazby, čímž simuluje scénář, kdy energie z jednoho vysílače proniká do sousedního přijímače. Testovací zařízení následně měří klíčové parametry, jako je Adjacent Channel Leakage Ratio ([ACLR](/mobilnisite/slovnik/aclr/)), blokování přijímače a intermodulace přijímače, aby zajistilo, že zůstávají v přísných mezích definovaných 3GPP.

Z architektonického hlediska je CLTA součástí většího testovacího uspořádání, které zahrnuje systémový simulátor, generátory signálů, spektrální analyzátory a RF spínače. Testovací postupy definované v 3GPP specifikacích podrobně popisují, jak musí být CLTA do tohoto uspořádání integrována. Testy mohou například zahrnovat vysílání vysokovýkonového signálu na jednom nosném kmitočtu při současném pokusu o příjem nízkovýkonového signálu na sousedním nosném kmitočtu, přičemž CLTA zajišťuje, že vazba mezi těmito cestami je reprezentativní pro reálné scénáře společné lokalizace. Samotná CLTA může být fyzickou anténou, nebo může být (v některých uspořádáních pro testování vedením) reprezentována kalibrovanými kabely a tlumiči, které emulují její vazební charakteristiky. Jejím úkolem je poskytnout referenční bod, který eliminuje variabilitu při testování a umožňuje tak spravedlivé a srovnatelné hodnocení zařízení základnových stanic od různých dodavatelů.

Klíčové součásti konceptu CLTA zahrnují standardizované specifikace antény, definované testovací geometrie (vzdálenosti a úhly vůči testovanému zařízení) a komplexní testovací případy pokrývající různé scénáře společné lokalizace. Tyto scénáře zahrnují intrapásmovou společnou lokalizaci (více nosných kmitočtů v rámci stejného kmitočtového pásma), interpásmovou společnou lokalizaci (nosné kmitočty v různých kmitočtových pásmech) a společnou lokalizaci více RAT (např. nosné kmitočty LTE a 5G NR). CLTA umožňuje ověření, že filtrování, stínění a techniky digitálního potlačení rušení základnové stanice jsou dostačující pro zachování výkonu. To je zvláště důležité pro moderní základnové stanice, které podporují agregaci nosných kmitočtů, massive [MIMO](/mobilnisite/slovnik/mimo/) a vícepásmový provoz, kde je více transceiverů hustě umístěno do jedné jednotky. Bez takového standardizovaného testování by operátoři mohli nasadit zařízení trpící vnitřním rušením, což by vedlo k přerušeným hovorům, sníženým datovým rychlostem a celkové nestabilitě sítě.

## K čemu slouží

CLTA byla vytvořena, aby řešila rostoucí výzvu densifikace základnových stanic a nasazení více pásem a více RAT v mobilních sítích. Když operátoři přidávali do svých sítí více kmitočtových pásem a technologií rádiového přístupu, stále častěji potřebovali instalovat více rádiových jednotek na stejném fyzickém místě – ať už uvnitř jednoho skříně základnové stanice nebo na stejném anténním stožáru. Tato společná lokalizace vytváří riziko elektromagnetického rušení mezi vysílači a přijímači těchto různých jednotek. I při pečlivém návrhu může energie z vysoko výkonného vysílače pronikat do sousedního přijímače, což jej desenzibilizuje a znemožňuje mu detekovat slabé signály od vzdáleného uživatelského zařízení. Tento problém je obzvláště palčivý u základnových stanic podporujících agregaci nosných kmitočtů a provoz Multi-Standard Radio ([MSR](/mobilnisite/slovnik/msr/)), kde více transceiverů pracuje současně v těsné blízkosti.

Historicky, před standardizovaným testováním společné lokalizace, používali dodavatelé zařízení a operátoři k posouzení rušení v těchto scénářích ad-hoc metody. Tyto metody byly často nekonzistentní, což ztěžovalo porovnávání zařízení od různých dodavatelů nebo záruku výkonu v reálných nasazeních. Nedostatek standardizace mohl vést k situacím, kdy základnové stanice prošly laboratorními testy, ale v terénu selhaly kvůli neočekávaným charakteristikám rušení. To mělo za následek nákladné přestavby lokalit, degradaci výkonu a výpadky služeb. 3GPP zavedlo koncept CLTA, aby poskytlo jednotnou, rigorózní testovací metodologii, která zajišťuje, že základnové stanice mohou spolehlivě fungovat v reálných podmínkách společné lokalizace.

CLTA tyto problémy řeší definováním scénáře nejhorší možné vazby, proti kterému musí být všechny základnové stanice testovány. To zajišťuje, že jakákoli základnová stanice vyhovující specifikacím 3GPP bude mít dostatečnou izolaci mezi svými vnitřními komponentami, aby zabránila degradaci výkonu. Pro síťové operátory to znamená větší jistotu při nasazování vícepásmových základnových stanic s vědomím, že zařízení bylo validováno za standardizovaných, opakovatelných podmínek. Pro dodavatele zařízení poskytuje jasné cíle pro návrh filtrování, stínění a linearity. CLTA nakonec přispívá k síťové spolehlivosti, spektrální efektivitě a uživatelskému zážitku tím, že zajišťuje, aby rostoucí složitost hardwaru základnových stanic nevedla ke zvýšenému rušení a sníženému výkonu.

## Klíčové vlastnosti

- Standardizované charakteristiky antény pro konzistentní testování napříč laboratořemi
- Definuje scénáře nejhorší možné vazby pro intrapásmovou a interpásmovou společnou lokalizaci
- Podporuje testování shody pro základnové stanice Multi-Standard Radio (MSR)
- Umožňuje ověření citlivosti přijímače při rušení od spolu lokalizovaného vysílače
- Validuje výkon základnové stanice pro nasazení s agregací nosných kmitočtů
- Poskytuje referenci pro testování pokročilých funkcí, jako je massive MIMO a více RAT

## Definující specifikace

- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1

---

📖 **Anglický originál a plná specifikace:** [CLTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/clta/)
