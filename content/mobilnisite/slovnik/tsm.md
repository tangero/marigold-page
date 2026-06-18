---
slug: "tsm"
url: "/mobilnisite/slovnik/tsm/"
type: "slovnik"
title: "TSM – Time Scale Modification"
date: 2025-01-01
abbr: "TSM"
fullName: "Time Scale Modification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tsm/"
summary: "Funkce zpracování médií, která upravuje rychlost přehrávání audio nebo video streamů bez změny výšky tónu. Používá se v telekomunikačních službách, jako je Voice over IP (VoIP), pro kompenzaci síťovéh"
---

TSM je funkce zpracování médií, která upravuje rychlost přehrávání audio nebo video streamů bez změny výšky tónu. Používá se v telekomunikacích pro kompenzaci síťového jitteru nebo synchronizaci streamů.

## Popis

Time Scale Modification (TSM, úprava časové osy) je technika digitálního zpracování signálu standardizovaná v rámci 3GPP pro použití v multimediálních telekomunikačních službách. Jejím hlavním úkolem je komprimovat nebo expandovat časovou osu audio (nebo video) signálu. Klíčové je, že toho dosahuje bez změny percepční výšky tónu audio signálu. Například zrychlení řečového signálu o 10 % pomocí TSM vede k rychlejší řeči, ale hlas mluvčího nezní výše. To je zásadní rozdíl oproti prosté konverzi vzorkovací frekvence, která by změnila jak rychlost, tak výšku tónu.

Architektonicky lze TSM implementovat v různých síťových prvcích nebo v uživatelském zařízení (UE) v závislosti na službě. Ve službě Voice over IP (VoIP) nebo videotelefonie může být funkce TSM umístěna v Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) v rámci IP Multimedia Subsystem (IMS) nebo v aplikačním serveru. Může to být také schopnost mediálního kodeku UE nebo postprocesního softwaru. Algoritmus TSM funguje tak, že analyzuje vstupní mediální stream, typicky po jeho dekódování do lineárního [PCM](/mobilnisite/slovnik/pcm/) formátu. Poté segmentuje signál, často pomocí technik založených na Short-Time Fourier Transform ([STFT](/mobilnisite/slovnik/stft/)) nebo metodách waveform similarity overlap-and-add (WSOLA), aby našel optimální body pro odstranění nebo duplikaci malých segmentů signálu bez vytváření slyšitelných artefaktů.

Jak TSM funguje, zahrnuje syntetizační fázi, ve které jsou tyto upravené segmenty překryty a sečteny zpět k sobě, aby vytvořily výstupní signál v novém časovém měřítku. Pro časovou kompresi jsou redundantní nebo méně percepčně kritická období (jako ticha nebo ustálené samohláskové zvuky) zkrácena nebo odstraněna. Pro časovou expanzi jsou vkládány další segmenty pečlivým překrýváním a prolínáním podobných částí vlnového tvaru. Proces je řízen škálovacím faktorem (např. 0,9 pro 10% zrychlení, 1,1 pro 10% zpomalení). V síťovém kontextu je běžnou aplikací správa jitter bufferu. Jitter buffer příjemce používá TSM k mírnému přizpůsobení rychlosti přehrávání, aby odpovídala dlouhodobé průměrné míře příchodu paketů, čímž zabraňuje podtečení nebo přetečení bufferu bez nutnosti synchronizace hodin mezi odesílatelem a příjemcem.

Jeho role v síti sahá za kompenzaci jitteru. TSM se používá pro synchronizaci nezávisle doručovaných mediálních streamů, jako je zarovnání audia s videem v multimediálních zprávách nebo vysílacích službách. Také umožňuje uživatelské funkce, jako je rychlý posun vpřed nebo zpomalené přehrávání nahraných hlasových zpráv nebo přednáškových videí bez nepřirozeného zkreslení výšky tónu. Specifikace podrobně popisují výkonnostní požadavky, jako je přijatelný rozsah škálovacích faktorů a maximální přípustné zhoršení kvality řeči, což zajišťuje interoperabilitu mezi různými implementacemi od různých dodavatelů.

## K čemu slouží

Time Scale Modification byla zavedena k řešení praktických problémů vznikajících v paketové multimediální komunikaci, kde nelze zaručit dokonalé izochronní doručení. V tradičních okruhově přepínaných hlasových sítích vyhrazený synchronní kanál zajišťoval konstantní zpoždění. Ve službách VoIP a paketově přepínaných multimediálních službách 3GPP pakety zažívají proměnlivé zpoždění (jitter) při průchodu IP sítí. Jednoduchý přehrávací buffer tento jitter dokáže pohltit, ale pokud se hodiny odesílatele a příjemce i jen mírně rozcházejí, buffer se nakonec vyprázdní nebo přeteče, což způsobí slyšitelné mezery nebo přeskočení ve řeči.

TSM poskytuje elegantní řešení tohoto problému s rozchodem hodin bez nutnosti složité synchronizace hodin v celé síti (jako [IEEE](/mobilnisite/slovnik/ieee/) 1588). Aplikací velmi mírných, nepostřehnutelných úprav časového měřítka (např. ±50 ppm) může přehrávací buffer upravit svou spotřební rychlost tak, aby odpovídala dlouhodobé průměrné míře příchodu paketů. To je mnohem efektivnější a levnější než pokusy synchronizovat každý koncový bod a síťový uzel se společným zdrojem hodin. Přímo řeší omezení jednoduchého bufferingu v asynchronních paketových sítích.

Navíc TSM umožňuje vylepšené uživatelské služby. Schopnost měnit rychlost přehrávání bez změny výšky tónu byla požadovanou funkcí pro služby zasílání zpráv (např. rychlejší poslech hlasové pošty) a pro přístupnost (např. zpomalení instruktážního audia). Před standardizovanými algoritmy TSM vedly proprietární řešení k problémům s interoperabilitou. Standardizace 3GPP zajistila konzistentní úroveň kvality a funkčnosti napříč sítěmi a zařízeními, což podpořilo lepší uživatelský zážitek při přehrávání médií s upraveným časem a robustní, odolnou komunikaci v reálném čase přes nespolehlivé paketové sítě.

## Klíčové vlastnosti

- Upravuje délku přehrávání (rychlost) audia/videa bez změny percepční výšky tónu
- Používá se pro dynamické řízení jitter bufferu ke kompenzaci rozchodu síťových hodin
- Umožňuje synchronizaci audia a videa v multimediálních službách
- Podporuje uživatelem řízenou rychlost přehrávání pro zasílání zpráv a streamování
- Založeno na pokročilých DSP algoritmech, jako je WSOLA nebo fázové vokodéry
- Standardizované výkonnostní požadavky pro zajištění kvality a interoperability

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.256** (Rel-19) — Jitter Buffer Management for IVAS
- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [TSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsm/)
