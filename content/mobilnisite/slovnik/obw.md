---
slug: "obw"
url: "/mobilnisite/slovnik/obw/"
type: "slovnik"
title: "OBW – Occupied Bandwidth"
date: 2025-01-01
abbr: "OBW"
fullName: "Occupied Bandwidth"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/obw/"
summary: "Obsazená šířka pásma (Occupied Bandwidth) je míra šířky frekvenčního spektra, které obsahuje stanovené procento (typicky 99 %) celkového skutečného středního výkonu vysílaného rádiového signálu. Jde o"
---

OBW je šířka frekvenčního spektra obsahujícího stanovené procento, typicky 99 %, celkového středního výkonu vysílaného rádiového signálu, což definuje jeho skutečné využití spektra.

## Popis

Obsazená šířka pásma (OBW) je standardizovaná metoda pro kvantifikaci spektrální stopy vysílaného rádiového signálu. Je definována jako šířka pásma mezi dvěma frekvenčními body, nad a pod nosnou frekvencí, které obsahují definované procento celkového integrovaného výkonu emise. Standard 3GPP, v souladu s doporučeními [ITU-R](/mobilnisite/slovnik/itu-r/), typicky používá definici 99% kontejnmentu výkonu. Měření se provádí pomocí spektrálního analyzátoru nebo specializovaného testovacího zařízení. Proces zahrnuje centrování měření na přidělený kanál, zachycení spektrální hustoty výkonu ([PSD](/mobilnisite/slovnik/psd/)) vysílaného signálu a následnou integraci výkonu od střední frekvence směrem ven, dokud není na každé straně nalezeno 0,5 % celkového výkonu; frekvenční rozdíl mezi těmito dvěma body -26 dB (neboli 0,5 %) je 99% OBW. U komplexně modulovaných signálů, jako jsou ty v LTE a 5G NR, je OBW úzce spojena, ale ne totožná, s šířkou kanálu nebo konfigurací přenosové šířky pásma. Je ovlivněna faktory jako modulační schéma (např. [QPSK](/mobilnisite/slovnik/qpsk/) vs. 256-QAM), spektrální tvarovací filtr (např. činitel sklonu filtru pro tvarování impulsu) a přítomnost jakéhokoli dodatečného spektrálního rozprostření. OBW je kritický parametr pro plánování sítě a regulační shodu. Zajišťuje, že vysílač zůstává v rámci přiděleného frekvenčního bloku a nepřelévá se do přilehlých alokací, což by mohlo způsobit rušení. Pro certifikaci zařízení musí být naměřená OBW menší nebo rovna deklarované šířce kanálu, aby byly splněny regulační požadavky.

## K čemu slouží

Koncept obsazené šířky pásma existuje proto, aby poskytl objektivní, měřitelnou definici toho, kolik spektra rádiová emise skutečně zabírá, což je zásadní pro efektivní a spravedlivou správu spektra. Rané rádiové předpisy potřebovaly způsob, jak zajistit, aby přenosy zůstávaly v rámci svých licencovaných pásem. Jednoduché definice založené na nosné frekvenci byly nedostačující pro moderní komplexní modulace se širokými spektrálními okraji. OBW poskytuje konzistentní metriku založenou na výkonu, kterou mohou regulátoři po celém světě (jako [FCC](/mobilnisite/slovnik/fcc/) a [ETSI](/mobilnisite/slovnik/etsi/)) používat k nastavení pravidel. Řeší problém definování praktického 'okraje' signálu, jehož výkon klesá postupně, nikoli náhle. To umožňuje správcům spektra umísťovat kanály blíže k sobě (minimalizace ochranných pásem) a přitom stále kontrolovat rušení, čímž maximalizují využití vzácných spektrálních zdrojů. Její formalizace v 3GPP již od nejstarších vydání LTE (Rel-8) byla nezbytná pro charakterizaci nových signálů založených na [OFDMA](/mobilnisite/slovnik/ofdma/), které mají odlišný spektrální tvar definovaný rozestupem subnosných a cyklickou předponou. Přesná definice OBW byla zásadní pro spektrální koexistenci LTE s legacy systémy (jako UMTS) a pro následné zavedení agregace nosných, kde se kombinuje více komponentních nosných s definovanými OBW.

## Klíčové vlastnosti

- Měří šířku pásma obsahující stanovené procento (např. 99 %) celkového výkonu signálu
- Poskytuje objektivní, regulačně konformní definici spektrální stopy signálu
- Měření je založeno na integraci spektrální hustoty výkonu
- Přímo ovlivňuje požadovaná ochranná pásma mezi sousedními kanály
- Klíčový parametr pro testování shody vysílače a schvalování typu
- Použitelná pro všechny 3GPP rádiové technologie (GSM, UMTS, LTE, NR)

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements

---

📖 **Anglický originál a plná specifikace:** [OBW na 3GPP Explorer](https://3gpp-explorer.com/glossary/obw/)
