---
slug: "peaq"
url: "/mobilnisite/slovnik/peaq/"
type: "slovnik"
title: "PEAQ – Perceptual Evaluation of Audio Quality"
date: 2025-01-01
abbr: "PEAQ"
fullName: "Perceptual Evaluation of Audio Quality"
category: "Services"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/peaq/"
summary: "PEAQ je objektivní, standardizovaná metoda pro predikci vnímané kvality zvuku řečových a audio kodeků, založená na modelech lidského sluchového vnímání. Je klíčová pro hodnocení a srovnávání výkonu ko"
---

PEAQ je objektivní, standardizovaná metoda pro predikci vnímané kvality zvuku řečových a audio kodeků v systémech 3GPP, založená na modelech lidského sluchového vnímání.

## Popis

Perceptual Evaluation of Audio Quality (PEAQ) je standardizovaný algoritmus definovaný doporučením [ITU-R](/mobilnisite/slovnik/itu-r/) [BS](/mobilnisite/slovnik/bs/).1387 a přijatý 3GPP pro objektivní měření kvality zpracovaných audio signálů. Funguje porovnáním zpracovaného (degradovaného) audio signálu s původním referenčním signálem. Jádrem PEAQ je psychoakustický model napodobující lidský sluchový systém, který analyzuje signály z hlediska hlasitosti, maskovacích efektů a kritických pásem. Algoritmus extrahuje specifické percepční charakteristiky, známé jako Model Output Variables (MOVs), z obou signálů. Tyto MOVs zachycují rozdíly v aspektech, jako je hlasitost šumu, modulace a harmonická struktura. Neuronová síť nebo jednodušší kognitivní model pak tyto extrahované percepční rozdíly převede na jediné objektivní skóre kvality, typicky Objective Difference Grade ([ODG](/mobilnisite/slovnik/odg/)), které se pohybuje od -4 (velmi rušivé zhoršení) do 0 (nezaznamenatelné zhoršení). To umožňuje spolehlivou predikci subjektivního Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)). V rámci 3GPP se PEAQ používá v testovacích specifikacích k hodnocení výkonu audio a řečových kodeků (např. [EVS](/mobilnisite/slovnik/evs/), [AMR-WB](/mobilnisite/slovnik/amr-wb/)) za různých síťových podmínek, jako je ztráta paketů nebo jitter. Proces je plně automatizovaný, což umožňuje reprodukovatelná a efektivní hodnocení kvality během vývoje, výběru kodeků a plánování sítě. Jeho integrace do specifikací 3GPP zajišťuje, že metriky kvality zvuku jsou konzistentní a srovnatelné napříč různými implementacemi a dodavateli, a tvoří tak kritickou součást rámce pro komplexní zajištění kvality multimediálních služeb.

## K čemu slouží

PEAQ byl vytvořen, aby vyřešil potřebu efektivní, spolehlivé a standardizované metody pro objektivní hodnocení kvality zvuku, která by nahradila nebo doplnila nákladné a časově náročné subjektivní poslechové testy (jako jsou [ACR](/mobilnisite/slovnik/acr/) testy). Subjektivní testy vyžadují panely lidských posluchačů, nejsou snadno opakovatelné a jsou nepraktické pro automatizované testování nebo regresní analýzu během vývoje kodeků. Před PEAQ se často používaly objektivní metriky jako poměr signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)), ale ty jsou špatnými prediktory vnímané kvality, protože nezohledňují nelineární a frekvenčně závislé charakteristiky lidského sluchu. Motivací bylo vyvinout nástroj, který by dokázal přesně předpovědět názory posluchačů na základě výpočetního modelu psychoakustiky. Jeho přijetí do standardů 3GPP, počínaje Release 8, poskytlo společný etalon pro hodnocení výkonu vyvíjejících se hlasových a audio kodeků napříč generacemi mobilních sítí (3G, 4G, 5G). To zajišťuje, že kvalita je udržována a zlepšována, jak sítě zavádějí nové kompresní techniky a zpracovávají různorodý audio obsah, od úzkopásmové řeči po hudbu ve vysokém rozlišení.

## Klíčové vlastnosti

- Objektivní predikce kvality založená na psychoakustických modelech
- Výstupem je Objective Difference Grade (ODG) korelující s subjektivním MOS
- Porovnává zpracovaný audio signál s původním referenčním signálem
- Extrahuje Model Output Variables (MOVs) pro percepční rozdíly
- Umožňuje automatizované, reprodukovatelné testování výkonu kodeků
- Standardizovaná metodologie (ITU-R BS.1387) přijatá 3GPP

## Související pojmy

- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.274** (Rel-19) — AMR-WB+ Codec Conformance Testing Specification
- **TS 26.406** (Rel-19) — Enhanced aacPlus Audio Codec Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [PEAQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/peaq/)
