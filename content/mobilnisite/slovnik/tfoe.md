---
slug: "tfoe"
url: "/mobilnisite/slovnik/tfoe/"
type: "slovnik"
title: "TFOE – TFO Enable"
date: 2025-01-01
abbr: "TFOE"
fullName: "TFO Enable"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfoe/"
summary: "TFOE je řídicí parametr používaný v jádře sítě 3GPP k povolení nebo zakázání režimu Tandem Free Operation (TFO). Je klíčový pro správu překódování řečových kodeků v přenosové cestě hovoru, neboť zlepš"
---

TFOE je řídicí parametr 3GPP, který povoluje nebo zakazuje režim Tandem Free Operation (operace bez tandemového zapojení) pro správu překódování řečových kodeků v přenosové cestě hovoru, čímž zlepšuje kvalitu hlasu a snižuje využití přenosové kapacity.

## Popis

[TFO](/mobilnisite/slovnik/tfo/) Enable (TFOE) je specifický parametr definovaný ve specifikacích 3GPP, konkrétně v TS 48.061, který řídí kontrolu překódování pro hlasové hovory. Působí v kontextu jádra sítě, konkrétně v Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)). Primární funkcí TFOE je sloužit jako řídicí příznak, který indikuje, zda je pro daný hovor povolena Tandem Free Operation. Když je TFOE nastaveno na 'povoleno', signalizuje to, že síť by se měla pokusit navázat TFO spojení mezi překodéry, což jim umožní obejít proces plného dekódování a opětovného kódování, pokud je na obou koncích použit stejný řečový kodek. Tento parametr je vyměňován mezi síťovými prvky během procedur navazování hovoru, například v rámci protokolu Bearer Independent Call Control (BICC) nebo jiných relevantních signalizačních zpráv. Jeho hodnota přímo ovlivňuje konfiguraci překodéru a rozhoduje o tom, zda hovor využije efektivnější TFO režim, nebo přejde na standardní tandemové překódování, při kterém je řeč plně dekódována do [PCM](/mobilnisite/slovnik/pcm/) a poté znovu zakódována, což spotřebovává více procesních zdrojů a může snížit kvalitu. Správa parametru TFOE je nedílnou součástí celkové strategie sítě pro optimalizaci hlasového provozu, zajišťuje, že výhody TFO jsou uplatněny tam, kde je to podporováno a vhodné, a zároveň zachovává kompatibilitu se staršími zařízeními nebo specifickými požadavky služeb, které mohou vyžadovat standardní překódování.

## K čemu slouží

Parametr TFOE byl zaveden, aby poskytl explicitní kontrolu nad funkcí Tandem Free Operation v sítích 3GPP. Před jeho formalizací mohla být aktivace [TFO](/mobilnisite/slovnik/tfo/) implicitní nebo založená na implementacích specifických pro dodavatele, což vedlo k potenciálním problémům s interoperabilitou a neoptimálnímu využití zdrojů. Zavedení TFOE řešilo potřebu standardizovaného, síťově řízeného mechanismu pro povolení nebo zakázání TFO pro každý jednotlivý hovor. To umožňuje operátorům sítí efektivně spravovat své překódovací zdroje a zajistit, že TFO je použito pouze tehdy, když přinese jasný benefit, například když oba konce hovoru podporují stejný kodek. Řeší problém nekontrolovaných nebo trvale aktivovaných pokusů o TFO, které by mohly selhat a způsobit zpoždění při navazování hovoru nebo přechody na záložní režim. Díky vyhrazenému indikátoru povolení/zákazu může síť činit informovaná rozhodnutí, což zlepšuje celkovou kvalitu hovoru a snižuje zbytečné zatížení překodérů, což je obzvláště důležité ve vysoce kapacitních jádrových sítích.

## Klíčové vlastnosti

- Standardizovaný řídicí parametr pro aktivaci TFO
- Vyměňován během signalizace navazování hovoru (např. v BICC)
- Umožňuje optimalizaci překódování řízenou sítí
- Podporuje rozhodování na úrovni jednotlivého hovoru o obejití kodeku
- Snižuje zatížení jádra sítě zpracováním při povolení
- Zlepšuje kvalitu hlasu end-to-end tím, že se vyhne tandemovému překódování

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [TFOE na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfoe/)
