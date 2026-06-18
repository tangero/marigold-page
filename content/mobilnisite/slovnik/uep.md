---
slug: "uep"
url: "/mobilnisite/slovnik/uep/"
type: "slovnik"
title: "UEP – Unequal Error Protection"
date: 2025-01-01
abbr: "UEP"
fullName: "Unequal Error Protection"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uep/"
summary: "Unequal Error Protection (nerovnoměrná ochrana proti chybám) je technika kódování kanálu, která aplikuje různé úrovně opravy chyb na různé části datového toku na základě jejich důležitosti. Optimalizu"
---

UEP je technika kódování kanálu, která aplikuje různé úrovně opravy chyb na různé části datového toku na základě jejich důležitosti, aby optimalizovala využití šířky pásma a zlepšila celkovou kvalitu.

## Popis

Unequal Error Protection (UEP) je sofistikovaná strategie dopředné korekce chyb používaná primárně v hlasových a video kodecích v systémech 3GPP. Funguje na principu, že ne všechny bity v komprimovaném mediálním rámci mají stejný význam pro percepční kvalitu rekonstruovaného výstupu. Například v řečovém kodeku Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) jsou bity reprezentující koeficienty filtru lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)) mnohem kritičtější než bity reprezentující excitační signál. UEP přizpůsobuje schéma kódování kanálu – jako jsou konvoluční nebo turbo kódy – tak, aby poskytovalo vyšší kódovou rychlost (méně redundance, slabší ochranu) pro méně důležité bity a nižší kódovou rychlost (více redundance, silnější ochranu) pro nejdůležitější bity.

Implementace UEP zahrnuje detailní proces klasifikace bitů ve zdrojovém kodéru. Výstupní bitový tok kodéru je segmentován do více tříd (např. třída A, B a C pro AMR), přičemž každé je přiřazen percepční význam. Vrstva rádiového protokolu, typicky Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) nebo samotná fyzická vrstva, aplikuje specifické rychlosti kódování kanálu na každou třídu. To je často řízeno pomocí algoritmů Rate Matching, které provádějí punkturaci nebo opakování bitů z různých tříd, aby se vešly do přidělené velikosti transportního bloku. Příjímač musí být této klasifikace vědom, aby mohl správně dekódovat a upřednostnit skrytí chyb, pokud jsou části toku poškozeny.

UEP je těsně integrována s procesy Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)). Různé úrovně ochrany znamenají, že kritické bity mají vyšší pravděpodobnost přežití počátečního přenosu, což snižuje potřebu retransmisí, které by mohly zvýšit latenci. U video služeb, jako je [MBMS](/mobilnisite/slovnik/mbms/) nebo evolved Multimedia Broadcast Multicast Service (eMBMS), je UEP klíčová pro doručení přijatelné kvality na okraji buňky, kde jsou podmínky kanálu špatné. Strategickou alokací zdrojů pro kódování kanálu poskytuje UEP významné zlepšení v end-to-end percepční kvalitě ve srovnání se schématy Equal Error Protection ([EEP](/mobilnisite/slovnik/eep/)) při stejném celkovém vysílacím výkonu a šířce pásma.

## K čemu slouží

UEP byla vytvořena, aby řešila základní výzvu doručení přijatelné hlasové a video kvality přes náchylné bezdrátové kanály s omezenými zdroji šířky pásma a výkonu. Tradiční schémata Equal Error Protection plýtvají kapacitou aplikací stejného robustního kódování na všechny bity, včetně těch, jejichž poškození způsobuje minimální percepční zkreslení. U nízkobitových kodeků, které jsou klíčové v mobilních komunikacích, se tato neefektivita přímo promítá do nižší hlasové kvality nebo zmenšeného pokrytí buňky.

Primární problém, který UEP řeší, je optimalizace end-to-end percepční kvality při omezené kapacitě kanálu. Sladěním síly ochrany proti chybám s citlivostí zdrojových bitů zajišťuje, že nejškodlivější chyby jsou s vysokou pravděpodobností prevenovány, zatímco je akceptována vyšší chybovost u méně důležitých komponent. To je obzvláště zásadní pro služby jako Voice over LTE (VoLTE) a streamování videa, kde je šířka pásma cenná a uživatelský zážitek je citlivý na artefakty.

Její vývoj byl motivován evolucí od okruhově spínaného hlasu k paketově spínanému multimédiu v systémech 3G a 4G. Jak se kodeky stávaly komplexnějšími a komprese efektivnější, rozdíl v důležitosti bitů rostl, čímž se UEP stávala stále přínosnější. Umožňuje síťovým operátorům udržovat kvalitu služby při maximalizaci spektrální efektivity, což je klíčový ekonomický faktor. Standardy jako TS 26.904 pro kodek Extended Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)+) specifikují schémata UEP, aby zajistily interoperabilitu a konzistentní kvalitu napříč zařízeními a sítěmi.

## Klíčové vlastnosti

- Klasifikace důležitosti bitů ve zdrojově kódovaných rámcích (např. třída A/B/C)
- Aplikace různých rychlostí kódování kanálu (např. 1/3, 1/2,我们发现了一个错误。在原始文本中，'2/3' 是作为示例给出的，但在翻译中它被遗漏了。让我们纠正这一点。
- Integrace s procesy Rate Matching fyzické vrstvy a HARQ
- Optimalizace pro percepční kvalitu spíše než pro čistou bitovou chybovost
- Kritická pro robustní výkon hlasových kodeků (AMR, EVS) a video kodeků
- Umožňuje udržení kvality na okraji buňky nebo za špatných rádiových podmínek

## Související pojmy

- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS

---

📖 **Anglický originál a plná specifikace:** [UEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/uep/)
