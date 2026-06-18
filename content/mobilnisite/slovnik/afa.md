---
slug: "afa"
url: "/mobilnisite/slovnik/afa/"
type: "slovnik"
title: "AFA – Adaptive Frequency Allocation"
date: 2025-01-01
abbr: "AFA"
fullName: "Adaptive Frequency Allocation"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/afa/"
summary: "AFA je dynamická technika správy spektra v sítích GSM/EDGE, která optimalizuje přiřazení frekvencí na základě aktuálních podmínek interference a provozu. Zvyšuje kapacitu sítě a kvalitu snížením ko-ka"
---

AFA je dynamická technika správy spektra v sítích GSM/EDGE, která optimalizuje přiřazení frekvencí na základě aktuálních podmínek interference a provozu za účelem zvýšení kapacity a kvality.

## Popis

Adaptive Frequency Allocation (AFA) je sofistikovaný algoritmus implementovaný v řadiči základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) v systémech GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Jeho primární funkcí je dynamicky přiřazovat rádiové frekvence buňkám a mobilním stanicím, což představuje posun oproti statickým, předem naplánovaným frekvenčním plánům. Systém průběžně sleduje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je úroveň přijímaného signálu, chybovost a míra vymazání rámců, jak v uplinku, tak v downlinku. Na základě těchto aktuálních měření spolu s informacemi o zatížení provozem AFA využívá heuristické nebo optimalizační algoritmy k výpočtu interferenční matice, která reprezentuje elektromagnetickou kompatibilitu mezi různými buňkami a frekvencemi. Na základě této matice může spustit přerozdělení frekvencí, ať už pro jednotlivá volání prostřednictvím předávání hovorů (handover), nebo pro celé buňky, aby se minimalizovala ko-kanálová interference (když je stejná frekvence použita v geograficky blízkých buňkách) a sousední-kanálová interference (když sousední frekvence navzájem přeslechnou). Proces je řízen parametry nastavenými operátorem sítě, které vyvažují četnost změn oproti možným ziskům v kvalitě. Z architektonického hlediska je AFA integrována s funkcemi správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) BSC a spoléhá na měřicí hlášení od mobilních stanic ([MS](/mobilnisite/slovnik/ms/)) a základnových stanic ([BTS](/mobilnisite/slovnik/bts/)). Její role je klíčová pro udržení kvality hovorů a maximalizaci přenosové kapacity omezeného GSM spektra, zejména v městském prostředí s komplexními podmínkami šíření a vysokou hustotou uživatelů.

## K čemu slouží

AFA byla zavedena, aby řešila významná omezení statického frekvenčního plánování v raných sítích GSM. Statické plány vytvořené při zavádění sítě se nedokázaly přizpůsobit měnícím se podmínkám, jako jsou hotspoty provozu, nově nasazené buňky nebo sezónní změny v šíření signálu. To vedlo k suboptimálnímu využití spektra, přetrvávajícím problémům s interferencí v určitých oblastech a v konečném důsledku k přerušeným hovorům a špatné kvalitě hlasu. Pevná povaha těchto plánů také činila optimalizaci sítě pomalým, manuálním a nákladným procesem. Motivací pro AFA byla potřeba větší spektrální účinnosti a provozní automatizace. Tím, že umožňuje síti samo-optimalizovat své využití frekvencí v reálném čase, řeší problém rigidního přidělování spektra v dynamickém rádiovém prostředí. Umožňuje síti proaktivně zmírňovat interferenci, zlepšovat celkovou třídu služby (GoS) a zvyšovat kapacitu bez nutnosti získání dalšího spektra – což byla klíčová výhoda s rostoucím počtem účastníků. Historicky představovala klíčový krok k autonomnějším a inteligentnějším rádiovým sítím a připravila cestu pro pozdější koncepty samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) v 3GPP.

## Klíčové vlastnosti

- Dynamické přiřazování frekvencí na základě měření interference v reálném čase
- Průběžná optimalizace ko-kanálové a sousední-kanálové interference
- Integrace s algoritmy správy rádiových zdrojů (RRM) v BSC
- Podpora jak přerozdělení frekvencí na úrovni buňky, tak předávání hovorů (handover) pro optimalizaci
- Využití měřicích hlášení z mobilních a základnových stanic (RXLEV, RXQUAL, FER)
- Konfigurovatelné parametry pro řízení agresivity a stability změn přidělení

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface
- **TS 45.056** (Rel-19) — GSM CTS-FP Radio Requirements

---

📖 **Anglický originál a plná specifikace:** [AFA na 3GPP Explorer](https://3gpp-explorer.com/glossary/afa/)
