---
slug: "sbr"
url: "/mobilnisite/slovnik/sbr/"
type: "slovnik"
title: "SBR – Spectral Band Replication"
date: 2025-01-01
abbr: "SBR"
fullName: "Spectral Band Replication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sbr/"
summary: "Technika rozšíření šířky pásma při kódování audia používaná ve službách Enhanced Voice Services (EVS) a dalších kodecích. Rekonstruuje vysokofrekvenční složky zvuku z nízkofrekvenčního základního sign"
---

SBR je technika rozšíření šířky pásma při kódování audia, která rekonstruuje vysokofrekvenční složky zvuku z nízkofrekvenčního základního signálu za účelem zlepšení vnímané kvality audia při nízkých přenosových rychlostech.

## Popis

Spectral Band Replication (SBR) je sofistikovaná technologie kódování audia standardizovaná 3GPP pro použití v kodecích, jako je kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) a dříve Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)+). Klasifikuje se jako technika 'rozšíření šířky pásma'. Základní princip SBR spočívá v efektivním přenosu vysokofrekvenčního obsahu audio signálu bez přímého kódování vysokofrekvenčních vzorků, které jsou náročné na přenosovou rychlost. Místo toho vysílač (enkodér) přenáší základní signál nízkého pásma (např. 0–6,4 kHz) na základní přenosové rychlosti pomocí tradičního základního kodeku (jako [ACELP](/mobilnisite/slovnik/acelp/) nebo [MDCT](/mobilnisite/slovnik/mdct/)) spolu s velmi kompaktní sadou řídicích parametrů, které popisují spektrální charakteristiky vysokého pásma (např. 6,4–16 kHz).

Z architektonického hlediska se kodek s podporou SBR skládá ze základního dekodéru a modulu SBR syntézy. Enkodér provádí komplexní analýzu. Rozdělí původní širokopásmový signál na nízké a vysoké pásmo. Nízké pásmo je zakódováno základním kodekem. Současně analyzuje vysoké pásmo, aby extrahoval parametry, jako je spektrální obálka (úrovně energie v různých kmitočtových oblastech) a časový šumový podklad. Tyto parametry SBR jsou kvantovány a odeslány do dekodéru jako vedlejší informace. Bitová náročnost těchto parametrů je mnohem nižší než plné kódování průběhu vysokého pásma.

Na straně dekodéru proces probíhá obráceně. Základní dekodér rekonstruuje signál nízkého pásma. Modul SBR syntézy poté vygeneruje signál vysokého pásma. Dělá to transpozicí nebo kopírováním kmitočtových složek z dekódovaného nízkého pásma do vysokofrekvenční oblasti. Tato zkopírovaná 'surová' vysokofrekvenční složka postrádá správný spektrální tvar. Dekodér následně použije přijaté parametry SBR – data o spektrální obálce a šumovém podkladu – k pečlivému tvarování a úpravě vygenerovaného signálu vysokého pásma tak, aby co nejvěrněji odpovídal charakteristikám originálu. Nakonec je syntetizované vysoké pásmo sloučeno s dekódovaným nízkým pásmem za vzniku plně šířkopásmového výstupu. Tato technika umožňuje kodeku poskytovat audio se širokopásmovou nebo super-širokopásmovou subjektivní kvalitou při přenosových rychlostech typicky spojovaných s úzkopásmovou řečí, což představuje významný skok v efektivitě kódování pro hlasové a audio služby.

## K čemu slouží

Spectral Band Replication byl vytvořen, aby překonal základní kompromis mezi šířkou pásma audia (a tedy kvalitou) a přenosovou rychlostí v mobilních komunikacích. Tradiční kodeky pracující s průběhem signálu vyžadují téměř lineární nárůst přenosové rychlosti k reprezentaci vyšších kmitočtů. Jak se sítě vyvíjely, aby podporovaly vyšší kapacitu, poptávka uživatelů se posunula od pouhé srozumitelnosti k vysoce kvalitnímu, přirozeně znějícímu hlasu a hudbě. SBR to řešil oddělením šířky pásma od přenosové rychlosti psychoakusticky inteligentním způsobem.

Historický kontext spočívá ve vývoji od úzkopásmové (300–3400 Hz) telefonie k širokopásmovému (50–7000 Hz) hlasu, jak je vidět u [AMR-WB](/mobilnisite/slovnik/amr-wb/). Pro dosažení ještě vyšší kvality (super-širokopásmový až 16 kHz) nebo stereofonní hudby při omezených přenosových rychlostech pro mobilní streamování byla potřeba efektivnější metoda. SBR to řeší využitím vlastností lidského sluchového systému: jemná struktura vysokých kmitočtů je pro vnímání méně kritická než celkový spektrální tvar a energie. Proto je replikace struktury z nízkého pásma a pouhé zasílání parametrů tvarování vysoce efektivní. To umožnilo kodekům 3GPP, jako je [EVS](/mobilnisite/slovnik/evs/), poskytovat kvalitu '[HD](/mobilnisite/slovnik/hd/) Voice+' při přenosových rychlostech podobných starším úzkopásmovým kodekům, což umožnilo vynikající kvalitu hlasu i na vytížených sítích a efektivní využití síťových zdrojů pro pokročilé komunikační služby.

## Klíčové vlastnosti

- Umožňuje širokopásmovou nebo super-širokopásmovou kvalitu audia při nízkých až středních přenosových rychlostech
- Funguje jako doplňková technologie k základnímu audio kodeku (např. jádro EVS)
- Přenáší pouze kompaktní sadu parametrů spektrální obálky a šumu vysokého pásma
- Rekonstruuje vysoké kmitočty transpozicí a tvarováním dekódovaného signálu nízkého pásma
- Poskytuje významné úspory přenosové rychlosti pro daný cíl kvality audia
- Integrální součást kodeku 3GPP EVS pro rozšířené hlasové a audio služby

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.401** (Rel-19) — Enhanced aacPlus Audio Codec Mapping
- **TS 26.402** (Rel-19) — Enhanced aacPlus Error Concealment & Processing
- **TS 26.403** (Rel-19) — Enhanced aacPlus AAC Encoder Specification
- **TS 26.404** (Rel-19) — Enhanced aacPlus SBR Encoder Specification
- **TS 26.405** (Rel-19) — Parametric Stereo Encoder for Enhanced aacPlus
- **TS 26.406** (Rel-19) — Enhanced aacPlus Audio Codec Conformance Testing
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code

---

📖 **Anglický originál a plná specifikace:** [SBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbr/)
