---
slug: "nn"
url: "/mobilnisite/slovnik/nn/"
type: "slovnik"
title: "NN – Number of audio channels"
date: 2025-01-01
abbr: "NN"
fullName: "Number of audio channels"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nn/"
summary: "NN specifikuje počet nezávislých zvukových kanálů pro mediální služby ve standardech 3GPP. Jedná se o základní parametr pro definici zvukových konfigurací v multimediálních aplikacích, který zajišťuje"
---

NN je parametr, který specifikuje počet nezávislých zvukových kanálů pro mediální služby ve standardech 3GPP a definuje zvukové konfigurace pro zajištění kompatibility a kvality.

## Popis

NN je parametr definovaný ve specifikacích 3GPP, který udává počet zvukových kanálů pro danou mediální službu nebo konfiguraci kodeku. Nejde o funkční entitu, ale o číselný atribut používaný v technických specifikacích pro popis uspořádání zvukových kanálů. Tento parametr je klíčový ve specifikacích týkajících se mediálních kodeků, streamovacích služeb a multimediální telefonie, kde definuje prostorovou konfiguraci zvuku, jako je mono (jeden kanál), stereo (dva kanály) nebo vícekanálová uspořádání pro imerzivní zvukové zážitky, jako je 3D audio nebo surround sound.

V kontextu 3GPP je NN odkazováno ve specifikacích jako TS 26.253 (Požadavky na výkon řečových a video kodeků), TS 26.847 (Požadavky na výkon pro imerzivní média) a TS 26.927 (Požadavky na výkon pro audio kodeky). Tyto dokumenty používají NN k specifikaci počtu zvukových kanálů jako součást testování výkonu kodeků, metrik kvality a požadavků na služby. Například při definování výkonu kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) nebo nového imerzivního audio kodeku NN indikuje, zda kodek podporuje mono, stereo nebo vyšší počty kanálů, což má vliv na hodnocení přenosové rychlosti, složitosti a kvality.

Parametr hraje roli při zajišťování interoperability a konzistentní kvality napříč zařízeními a sítěmi. Díky standardizaci počtu zvukových kanálů umožňuje 3GPP výrobcům a poskytovatelům služeb implementovat kompatibilní systémy zpracování a přehrávání zvuku. Ovlivňuje také výpočty šířky pásma a přidělování zdrojů pro mediální relace, protože vyšší počet kanálů obvykle vyžaduje vyšší datové rychlosti. Při plánování sítě a návrhu služeb pomáhá porozumění NN optimalizovat doručování zvuku pro různé aplikace, od základních hlasových hovorů až po pokročilé multimediální streamování.

## K čemu slouží

Parametr NN existuje proto, aby poskytl standardizovaný způsob specifikace konfigurace zvukových kanálů v mediálních specifikacích 3GPP. Jeho vytvoření řeší potřebu jasných a jednoznačných definic zvukových nastavení pro zajištění kompatibility mezi různými implementacemi a zařízeními. Jak se multimediální služby vyvinuly z jednoduchého mono hlasu přes stereo hudbu až po imerzivní audio, stalo se definování počtu kanálů nezbytným pro testování výkonu, návrh kodeků a požadavky na služby.

Historicky rané mobilní audio služby primárně používaly mono kanál pro hlas, ale s příchodem streamování hudby, videohovorů a imerzivních médií se stala nutná podpora více audio kanálů. Parametr NN umožňuje specifikacím přesně uvádět požadovaný počet kanálů pro konkrétní kodek nebo službu, což usnadňuje konzistentní hodnocení a implementaci. Řeší problém nejednoznačných zvukových konfigurací, které by mohly vést k problémům s interoperabilitou nebo podoptimální kvalitou.

Bez standardizovaného parametru, jako je NN, by různé specifikace mohly popisovat počty kanálů nekonzistentně, což by způsobovalo zmatek ve vývoji kodeků, poskytování sítě a certifikaci zařízení. Zařazením NN do příslušných specifikací zajišťuje 3GPP, že všechny strany – od návrhářů kodeků po síťové operátory – mají společný referenční bod pro definice zvukových kanálů, což umožňuje úspěšné nasazení pokročilých audio služeb v mobilních sítích.

## Klíčové vlastnosti

- Definuje počet nezávislých zvukových kanálů pro mediální konfigurace
- Používá se ve specifikacích výkonu kodeků a testovacích požadavcích
- Podporuje konfigurace od mono až po vícekanálové imerzivní audio
- Ovlivňuje výpočty přenosové rychlosti a kvality pro audio služby
- Zajišťuje interoperabilitu mezi zařízeními a implementacemi
- Poskytuje standardizovaný parametr pro specifikaci zvukových kanálů

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study

---

📖 **Anglický originál a plná specifikace:** [NN na 3GPP Explorer](https://3gpp-explorer.com/glossary/nn/)
