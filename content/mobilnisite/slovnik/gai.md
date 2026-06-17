---
slug: "gai"
url: "/mobilnisite/slovnik/gai/"
type: "slovnik"
title: "GAI – Geographical Area Identifier"
date: 2025-01-01
abbr: "GAI"
fullName: "Geographical Area Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gai/"
summary: "Jedinečný identifikátor přiřazený definované geografické oblasti v síti 3GPP. Používá se k odkazování na konkrétní zóny pro služby založené na poloze, uplatňování politik a správu sítě bez nutnosti př"
---

GAI je jedinečný identifikátor přiřazený definované geografické oblasti v síti 3GPP, používaný k odkazování na konkrétní zóny pro služby založené na poloze, uplatňování politik a správu sítě.

## Popis

Geographical Area Identifier (GAI) je stručný popisek nebo kód reprezentující předem definovanou geografickou oblast v mobilní síti. Na rozdíl od podrobných souřadnic [GAD](/mobilnisite/slovnik/gad/) je GAI zkrácená reference, kterou síťové funkce a uživatelské zařízení (UE) mohou používat k efektivní identifikaci regionu. Je definován ve specifikacích 3GPP jako součást mechanismů pro služby polohy a řízení politik. GAI je typicky mapován na podrobnější geografický popis, například na polygon GAD, v rámci síťových databází.

Z architektonického hlediska se GAI používá na rozhraních mezi uzly jádra sítě, například mezi funkcí pravidel pro politiky a účtování (PCRF) a aplikační funkcí ([AF](/mobilnisite/slovnik/af/)), nebo uvnitř Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Funguje tak, že umožňuje služebním požadavkům nebo pravidlům politik odkazovat na oblast pomocí jejího identifikátoru namísto opakovaného přenosu úplných geografických hranic. Například "zóna prémiové služby" může mít přiřazen konkrétní GAI, a když uživatel tuto zónu vstoupí, síť může na základě GAI uplatnit odpovídající pravidla účtování. Identifikátor je často komunikován v protokolových zprávách, jako jsou ty na rozhraních Gx nebo Rx, za použití protokolu Diameter.

Klíčové komponenty zahrnují samotnou hodnotu GAI, což je řetězec nebo číselný kód, a přidružené mapování na definici geografické oblasti uloženou v síťovém úložišti. Úlohou GAI je snížit signalizační režii a zjednodušit implementaci služeb závislých na poloze. Umožňuje škálovatelné geofencing, kde lze efektivně spravovat velký počet oblastí, a podporuje případy užití jako je řízení přístupu na základě polohy, cílené vysílání a dodržování regulatorních požadavků (např. služby specifické pro danou zemi). V praxi jsou GAIs zřizovány síťovými operátory a mohou odpovídat buňkám, oblastem sledování (tracking areas) nebo uživatelsky definovaným zónám.

## K čemu slouží

GAI byl zaveden, aby řešil neefektivitu opakovaného přenosu podrobných popisů geografických oblastí přes síťová rozhraní. Před jeho standardizací služby založené na poloze často vyžadovaly odesílání kompletních struktur [GAD](/mobilnisite/slovnik/gad/) v každé zprávě, což spotřebovávalo přenosovou kapacitu a výpočetní prostředky. To bylo obzvláště problematické pro služby, které monitorují přítomnost v mnoha oblastech nebo uplatňují politiky na základě častých aktualizací polohy.

Vytvoření GAI ve verzi 8 (Release 8) bylo motivováno rostoucí komplexitou služeb založených na poloze a potřebou optimalizované signalizace. Řešil problém škálovatelnosti v sítích s miliony uživatelů a tisíci geografických zón. Použitím identifikátoru mohly sítě ukládat definice oblastí do mezipaměti a odkazovat se na ně lehkou referencí, což umožnilo rychlejší rozhodování a snížení latence pro služby v reálném čase. Tento přístup také zjednodušil konfiguraci a správu geografických politik, protože operátoři mohli zóny definovat jednou a odkazovat na ně pomocí jednoduchého ID napříč různými síťovými funkcemi a službami.

## Klíčové vlastnosti

- Poskytuje kompaktní referenci na předdefinované geografické oblasti
- Snižuje signalizační režii ve srovnání s přenosem plných struktur GAD
- Umožňuje efektivní uplatňování politik na základě polohy uživatele
- Podporuje mapování na více geografických popisů (např. pro různé úrovně podrobnosti)
- Používá se v rozhraních pro řízení politik (PCRF) a účtování
- Usnadňuje škálovatelný geofencing a spouštění služeb na základě polohy

## Související pojmy

- [GAD – Universal Geographical Area Description](/mobilnisite/slovnik/gad/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [GAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gai/)
