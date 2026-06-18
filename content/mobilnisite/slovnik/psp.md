---
slug: "psp"
url: "/mobilnisite/slovnik/psp/"
type: "slovnik"
title: "PSP – PAS Similarity Percentage"
date: 2025-01-01
abbr: "PSP"
fullName: "PAS Similarity Percentage"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psp/"
summary: "Metrika používaná v 3GPP pro kvantifikaci podobnosti mezi dvěma modely výkonového úhlového spektra (PAS), které charakterizují prostorové vlastnosti rádiových kanálů. Je klíčová pro hodnocení a porovn"
---

PSP je metrika používaná v 3GPP pro kvantifikaci podobnosti mezi dvěma modely výkonového úhlového spektra (Power Angular Spectrum), které charakterizují prostorové vlastnosti rádiových kanálů pro systémy MIMO a beamforming.

## Popis

Procento podobnosti výkonového úhlového spektra (PSP) je kvantitativní míra definovaná ve specifikacích 3GPP pro posouzení podobnosti mezi dvěma modely výkonového úhlového spektra ([PAS](/mobilnisite/slovnik/pas/)). Model PAS popisuje, jak je přijímaný výkon signálu rozložen mezi různé úhly příchodu nebo odchodu u anténního pole, což je zásadní pro charakterizaci prostorových vlastností rádiového přenosového kanálu. V kontextu 3GPP, zejména pro NR (New Radio), jsou tyto modely nezbytné pro návrh a hodnocení pokročilých anténních systémů, včetně Massive [MIMO](/mobilnisite/slovnik/mimo/) a technik beamformingu. PSP poskytuje standardizovanou numerickou metodu pro porovnání kandidátního modelu PAS s referenčním modelem PAS, kterým je typicky model definovaný ve specifikaci 3GPP. Toto porovnání je klíčové pro validaci nových kanálových modelů navrhovaných pro simulace sítí, testování výkonu a standardizační činnosti.

Výpočet PSP zahrnuje matematické porovnání dvou PAS funkcí v úhlové doméně. Proces typicky zahrnuje normalizaci PAS funkcí, aby bylo zajištěno spravedlivé porovnání jejich tvarů spíše než absolutních úrovní výkonu. Běžnou metodou je výpočet korelačního koeficientu nebo metriky podobnosti mezi dvěma normalizovanými PAS distribucemi v definovaném úhlovém rozsahu (např. -180 až 180 stupňů). Vyšší hodnota PSP značí vyšší stupeň podobnosti mezi dvěma modely. Konkrétní metodika výpočtu a akceptační kritéria (např. minimální práh PSP) jsou podrobně popsána v příslušných technických specifikacích 3GPP, jako jsou ty pokrývající požadavky na rádiovou frekvenci ([RF](/mobilnisite/slovnik/rf/)) a kanálové modely.

PSP hraje klíčovou roli v ekosystému návrhu a validace bezdrátových systémů. Pro výrobce zařízení a operátory sítí zajišťuje, že kanálové modely používané v simulacích, testech shody a nástrojích pro plánování sítí jsou konzistentní se standardizovanými referenčními modely. Tato konzistence je zásadní pro přesné predikce výkonu systému, zejména pro funkce jako správa paprsků, prostorové multiplexování a koordinace interference. Poskytnutím objektivní metriky podobnosti PSP pomáhá předcházet nesrovnalostem v hodnocení výkonu, které by mohly vzniknout použitím mírně odlišných interpretací kanálového modelu, a tím podporuje spolehlivější a srovnatelnější hodnocení různých technologií a implementací dodavatelů.

## K čemu slouží

Procento podobnosti výkonového úhlového spektra (PSP) bylo zavedeno, aby řešilo potřebu objektivní, kvantitativní validace kanálových modelů v éře stále složitějších anténních systémů. S vývojem od 4G k 5G NR se použití rozsáhlých anténních polí (Massive [MIMO](/mobilnisite/slovnik/mimo/)) a sofistikovaného beamformingu stalo klíčovým pro dosažení vysokých přenosových rychlostí a kapacity. Výkon těchto systémů je vysoce závislý na přesnosti podkladových prostorových kanálových modelů, konkrétně na výkonovém úhlovém spektru ([PAS](/mobilnisite/slovnik/pas/)). Před zavedením PSP bylo porovnávání kanálových modelů často kvalitativním nebo subjektivním procesem, což mohlo vést k nekonzistencím ve výsledcích simulací, tvrzeních o výkonu a standardizačních debatách.

Vytvoření PSP bylo motivováno požadavkem na zajištění spravedlnosti a přesnosti při hodnocení nových technologických návrhů a při testech shody. Například při zavádění nového scénáře nasazení nebo frekvenčního pásma mohou být navrženy nové kanálové modely. Metrika PSP poskytuje jasný, opakovatelný standard pro určení, zda je navrhovaný model 'dostatečně podobný' existujícímu, dohodnutému referenčnímu modelu. Tím řeší problém divergence modelů, kdy mírně odlišné implementace konceptu kanálového modelu mohly vést k výrazně odlišným predikcím výkonu systému, což komplikovalo standardizační proces a interoperabilitu zařízení.

## Klíčové vlastnosti

- Kvantifikuje podobnost mezi modely výkonového úhlového spektra (PAS)
- Standardizovaná metrika definovaná ve specifikacích 3GPP pro NR
- Zásadní pro validaci kanálových modelů v simulacích MIMO/beamformingu
- Podporuje konzistentní hodnocení výkonu a plánování sítí
- Používá se v testech shody a specifikacích RF požadavků
- Umožňuje objektivní porovnání navrhovaných a referenčních prostorových charakteristik kanálu

## Související pojmy

- [PAS – Publicly Available Specification](/mobilnisite/slovnik/pas/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TR 33.882** (Rel-18) — Technical Report on 5G Security for Personal IoT Networks
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology

---

📖 **Anglický originál a plná specifikace:** [PSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/psp/)
