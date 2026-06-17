---
slug: "mdst"
url: "/mobilnisite/slovnik/mdst/"
type: "slovnik"
title: "MDST – Modified Discrete Sine Transform"
date: 2025-01-01
abbr: "MDST"
fullName: "Modified Discrete Sine Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mdst/"
summary: "Transformace pro zpracování signálu používaná ve studijních položkách 5G Advanced a 6G pro efektivní kompresi a reprezentaci dat. Jedná se o variantu diskrétní sinusové transformace (DST) optimalizova"
---

MDST je varianta diskrétní sinusové transformace optimalizovaná pro efektivní kompresi a reprezentaci dat v aplikacích 5G Advanced a 6G, jako je společná komunikace a snímání.

## Popis

Modifikovaná diskrétní sinusová transformace (MDST) je matematická transformace studovaná v rámci 3GPP pro potenciální použití v pokročilém zpracování signálů na fyzické vrstvě. Definována v 3GPP TS 26.253 v kontextu práce na kodecích a médiích představuje adaptaci klasické diskrétní sinusové transformace ([DST](/mobilnisite/slovnik/dst/)). DST úzce souvisí s diskrétní kosinovou transformací ([DCT](/mobilnisite/slovnik/dct/)) a používá se k reprezentaci konečné sekvence datových bodů jako součtu sinusových funkcí kmitajících na různých frekvencích. Aspekt „modifikované“ obvykle odkazuje na specifické úpravy bázových funkcí transformace nebo jejího aplikačního kontextu, aby byla optimalizována pro konkrétní případy použití, jako je komprese dat, extrakce příznaků nebo jako součást předzpracovacího řetězce pro modely strojového učení v RAN.

Z hlediska architektury a fungování by byla MDST implementována v rámci řetězců digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) vysílače nebo přijímače. Funguje tak, že vezme blok vzorků v časové nebo prostorové oblasti a převede je do reprezentace ve frekvenční nebo transformační oblasti, kde je energie koncentrována do menšího počtu koeficientů. Tato vlastnost je cenná pro kompresi, protože umožňuje odstranění méně významných koeficientů s minimální percepční nebo informační ztrátou. Specifické modifikace standardní DST mohou mít za cíl zlepšit koncentraci energie, snížit výpočetní složitost nebo přizpůsobit transformaci statistickým vlastnostem bezdrátových signálů nebo kódovaných médií.

Její role v síti, jako předmět studia ve verzi 18 a dalších, je průzkumná. Mohla by být použita ve scénářích, jako je efektivní hlášení zpětné vazby v massive [MIMO](/mobilnisite/slovnik/mimo/) (kde jsou informace o stavu kanálu komprimovány), integrované snímání a komunikace (ISAC) pro reprezentaci radarových signálů, nebo v rámci modelů [AI/ML](/mobilnisite/slovnik/ai-ml/) pracujících v RAN pro predikci kanálu nebo detekci anomálií. Samotná transformace je nástrojem pro efektivní matematickou reprezentaci a její integrace by byla v rámci větších funkčních bloků definovaných specifikacemi 3GPP pro konkrétní funkce, jako jsou nové mediální kodeky nebo rádiová rozhraní s podporou AI/ML.

## K čemu slouží

MDST existuje jako položka výzkumu a studia pro zkoumání efektivnějších technik reprezentace a zpracování signálu pro budoucí bezdrátové systémy nad rámec 5G. Motivace vychází z neustálého úsilí o vyšší spektrální účinnost, nižší latenci a podporu nových služeb, jako je společná komunikace a snímání, které mohou těžit z optimalizovaných transformačních domén. Předchozí přístupy mohly spoléhat na standardní [DCT](/mobilnisite/slovnik/dct/) nebo [DFT](/mobilnisite/slovnik/dft/), které, ač efektivní, nemusí být optimální pro všechny typy signálů nebo pro specifická omezení pracovních postupů [AI/ML](/mobilnisite/slovnik/ai-ml/) v RAN.

Problém, který řeší, je potřeba vysoce efektivní komprese dat a extrakce příznaků v kontextech, kde je omezena šířka pásma nebo výpočetní výkon. Například v AI/ML pro RAN vyžaduje komprese velkého množství dat měření kanálu pro hlášení nebo vstup modelu transformace, které minimalizují ztrátu informací. Modifikovaná transformace může být přizpůsobena statistickým vlastnostem dat bezdrátového kanálu nebo specifických typů médií a potenciálně nabídnout lepší výkon než obecně dostupné transformace.

Její vznik je motivován vývojem směrem k 6G, kde extrémní požadavky na výkon a nové případy použití vyžadují inovace na základní úrovni zpracování signálu. Studium MDST umožňuje 3GPP vyhodnotit, zda vlastní, optimalizované transformace poskytují hmatatelné výhody, které stojí za standardizaci, a zajistit interoperabilitu při současném posouvání hranic možného z hlediska efektivity reprezentace dat.

## Klíčové vlastnosti

- Varianta diskrétní sinusové transformace s optimalizovanými bázovými funkcemi
- Cílí na vysokou koncentraci energie pro efektivní kompresi dat
- Potenciál snížení výpočetní složitosti ve srovnání se standardními transformacemi
- Přizpůsobitelná specifické statistice signálu (např. bezdrátové kanály, data senzorů)
- Užitečná pro extrakci příznaků v modelech AI/ML pro RAN
- Předmět studia pro pokročilé aplikace, jako je integrované snímání a komunikace

## Související pojmy

- [DCT – Discrete Cosine Transformation](/mobilnisite/slovnik/dct/)
- [DFT – Discrete Fourier Transform](/mobilnisite/slovnik/dft/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [MDST na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdst/)
