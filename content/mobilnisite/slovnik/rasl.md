---
slug: "rasl"
url: "/mobilnisite/slovnik/rasl/"
type: "slovnik"
title: "RASL – Random Access Skipped Leading picture"
date: 2025-01-01
abbr: "RASL"
fullName: "Random Access Skipped Leading picture"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rasl/"
summary: "Technika kódování videa v kodeku Enhanced Voice Services (EVS) standardu 3GPP. Zlepšuje odolnost proti chybám u přenosu řeči a audia přes paketové sítě tím, že řeší ztrátu paketů v prediktivních snímc"
---

RASL je technika kódování videa v kodeku 3GPP EVS, která zlepšuje odolnost proti chybám u řeči a audia tím, že řeší ztrátu paketů v prediktivních snímcích videa.

## Popis

Random Access Skipped Leading picture (RASL) je specifický mechanismus odolnosti proti chybám definovaný ve specifikacích kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) standardu 3GPP, podrobně popsaný zejména v TS 26.346 pro doručování médií přes [MBMS](/mobilnisite/slovnik/mbms/). Funguje na pomezí kódování audio/videa a maskování ztráty paketů. Tato technika je navržena pro řešení scénářů, kdy je úvodní snímek ve videosignálu, který je prediktivně zakódován a závisí na předchozím snímku náhodného přístupu, ztracen nebo dorazí mimo pořadí kvůli ztrátě paketů nebo kolísání zpoždění v síti. V prediktivním kódování videa (jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo [HEVC](/mobilnisite/slovnik/hevc/) používané v multimediální telefonii) je RASL snímek typem úvodního snímku, který předchází snímku Clean Random Access ([CRA](/mobilnisite/slovnik/cra/)) v dekódovacím pořadí, ale následuje ho ve výstupním pořadí. Pokud chybí CRA snímek (klíčový bod obnovy), tyto závislé RASL snímky nelze správně dekódovat. Systémová vrstva kodeku EVS, pokud je nakonfigurována pro práci s vědomím videa, může tyto závislosti signalizovat a spravovat. Mechanismus funguje tak, že umožňuje dekodéru nebo systému 'přeskočit' nebo zahodit tyto nedekódovatelné úvodní snímky, když je ztracen potřebný referenční snímek (CRA), čímž zabraňuje šíření vizuálních artefaktů a umožňuje rychlejší obnovu na dalším platném bodě náhodného přístupu. To zahrnuje pečlivou správu časových razítek a synchronizaci dekódovacího pořadí mezi audio (EVS) a video streamy, aby byla zachována synchronizace rtů a kontinuita prezentace. Jeho role je klíčová v konverzačních službách a streamování, kde jsou nízká latence a robustnost prvořadé, a zajišťuje, že dočasné poruchy sítě nezpůsobí dlouhodobé zhoršení audiovizuální prezentace.

## K čemu slouží

RASL byl zaveden, aby řešil výzvu robustní multimediální komunikace přes nespolehlivé paketové sítě, jako jsou LTE a 5G NR. Předchozí přístupy ve videoslužbách mohly trpět závažným a přetrvávajícím vizuálním poškozením při ztrátě paketů v blízkosti bodů náhodného přístupu, protože dekodéry se mohly pokoušet dekódovat závislé snímky bez platných referencí, což vedlo k šíření chyb. Hlavní problém, který řeší, je elegantní zpracování ztráty paketů u prediktivně zakódovaných videosnímků, které jsou mimo pořadí vzhledem ke svým referenčním snímkům – běžný problém v přenosu v reálném čase. Formálním definováním zpracování RASL snímků v rámci frameworku pro doručování médií 3GPP umožňuje odolnější videoslužby spolu s vysoce kvalitním audiem [EVS](/mobilnisite/slovnik/evs/). To bylo zvláště motivováno vývojem směrem k plně IP sítím pro hlasové a videoslužby (VoLTE, ViLTE, VoNR), kde tradiční mechanismy odolnosti proti chybám z okruhových sítí nebyly použitelné. Zajišťuje, že kvalita uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) pro kombinované služby řeči a videa splňuje očekávání uživatelů i za suboptimálních rádiových podmínek.

## Klíčové vlastnosti

- Definuje zpracování úvodních snímků, které závisí na chybějícím snímku Clean Random Access (CRA)
- Zabraňuje šíření chyb v prediktivním kódování videa po ztrátě paketu
- Umožňuje rychlejší vizuální obnovu na dalším platném synchronizačním bodě
- Integruje se se systémovou vrstvou kodeku 3GPP EVS pro synchronizované přehrávání médií
- Podporuje robustní multimediální telefonii přes paketové sítě (např. ViLTE)
- Specifikováno v architekturách služeb MBMS a streamování v rámci 3GPP

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [CRA – Clean Random Access](/mobilnisite/slovnik/cra/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [RASL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rasl/)
