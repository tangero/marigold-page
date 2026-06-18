---
slug: "upcmi"
url: "/mobilnisite/slovnik/upcmi/"
type: "slovnik"
title: "UPCMI – Uniform Pulse Code Modulation Interface (13-bit)"
date: 2025-01-01
abbr: "UPCMI"
fullName: "Uniform Pulse Code Modulation Interface (13-bit)"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/upcmi/"
summary: "Specifický standard pro 13bitové lineární PCM rozhraní definovaný pro propojení síťových prvků v systémech 3GPP. Specifikuje elektrické a logické charakteristiky pro přenos vysoce kvalitních, rovnoměr"
---

UPCMI je standard pro 13bitové lineární PCM rozhraní pro propojení síťových prvků 3GPP, který specifikuje elektrické a logické charakteristiky pro přenos vysoce kvalitních, rovnoměrně kvantovaných digitálních hlasových signálů.

## Popis

Uniform [PCM](/mobilnisite/slovnik/pcm/) Interface (UPCMI) je konkrétní specifikace fyzického a logického rozhraní, která vyžaduje použití 13bitového lineárního pulzně kódové modulace (PCM) pro přenos digitálních hlasových signálů mezi specifickými síťovými uzly v systému 3GPP. Definována ve specifikacích jako 3GPP TS 21.905 (slovní zásoba), TS 26.131 (akustické charakteristiky terminálu) a TS 43.050 (plánování GSM rádiové sítě), standardizuje formátování a přenos nekomprimovaných, věrných hlasových vzorků. Rozhraní pracuje se standardní telefonní vzorkovací frekvencí 8 kHz, což vede k datovému toku 104 kbps na hlasový kanál (13 bitů/vzorek * 8000 vzorků/sec). Tato hodnota je vyšší než 64 kbps u standardního A-zákon/μ-zákon PCM díky dodatečným bitům, které poskytují větší dynamický rozsah a přesnost.

Z architektonického hlediska se UPCMI typicky aplikuje na spojení mezi základnovou přenosovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) a řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v sítích GSM, nebo podobnými uzly v raných architekturách 3GPP. Definuje charakteristiky digitálního trunku přenášejícího více časově dělených multiplexovaných ([TDM](/mobilnisite/slovnik/tdm/)) hlasových kanálů. Klíčovými komponentami jsou jednotky liniového rozhraní v BTS i BSC, které musí tomuto standardu vyhovovat. Rozhraní zajišťuje, že hlasová kvalita je zachována ve své nejpřesnější digitální podobě na tomto segmentu sítě, minimalizuje kvantizační šum a zkreslení, než může být signál komprimován kodekem jako [TRAU](/mobilnisite/slovnik/trau/) pro přenos přes rozhraní Abis nebo dále do jádra sítě.

Princip fungování spočívá v tom, že BTS převede přijímaný rádiový signál (již dekódovaný z jeho rádiového kodeku, např. [FR](/mobilnisite/slovnik/fr/), [EFR](/mobilnisite/slovnik/efr/) nebo [AMR](/mobilnisite/slovnik/amr/)) na 13bitový lineární PCM vzorek pro každý aktivní hlasový kanál. Tyto vzorky jsou následně multiplexovány s dalšími do TDM rámce (např. pomocí E1 nebo T1 formátování) a odeslány do BSC. BSC tento proud přijímá, může provádět operace jako detekci hlasové aktivity nebo potlačení ozvěn v lineární doméně s vysokou přesností, a následně může vzorky předat k dalšímu zpracování nebo překódování. Rozlišení 13 bitů je specifický technický kompromis, který vyvažuje zlepšenou kvalitu oproti 8bitovému komprimovanému PCM s přiměřenými požadavky na datový tok, a vyhýbá se vyšší spotřebě šířky pásma plného 16bitového lineárního PCM.

## K čemu slouží

UPCMI bylo vytvořeno za účelem standardizace digitálního hlasového rozhraní mezi klíčovými prvky rádiového přístupové sítě, konkrétně pro zaručení konzistentního a kvalitního předání hlasového signálu. Před takovou standardizací mohly proprietární rozhraní nebo různé formáty PCM vést k problémům s interoperabilitou a kumulativní degradaci kvality při propojení zařízení od různých výrobců v síti. Lineární 13bitový formát byl zvolen pro řešení omezení 8bitového komprimovaného PCM (A-zákon/μ-zákon), které, ač efektivní, může zavádět kvantizační zkreslení, zejména pro signály nízké úrovně a při vícenásobném kaskádovém kódování.

Historický kontext představuje digitalizace celulárních sítí v éře 2G GSM. Existovala potřeba robustního, na výrobci nezávislého rozhraní pro hlasovou cestu mezi BTS a BSC. Použití lineárního rozhraní zjednodušilo návrh potlačovačů ozvěn a dalších funkcí pro zlepšení hlasové kvality umístěných v BSC. Řešilo problém udržení kvality hlasu end-to-end vytvořením kvalitního 'kotvícího' bodu v RAN před případnou ztrátovou kompresí pro přenos přes omezené backhaulové linky. To bylo obzvláště důležité pro podporu pokročilých hlasových služeb a zajištění konzistentního výkonu v síťových nasazeních s více výrobci.

## Klíčové vlastnosti

- Standardizované 13bitové lineární PCM kódování na hlasový vzorek
- Vzorkovací frekvence 8 kHz pro telefonní přenosové pásmo 300-3400 Hz
- Definuje elektrické a logické charakteristiky rozhraní pro TDM přenos
- Typicky používáno na E1/T1 trunkách mezi BTS a BSC v GSM
- Poskytuje vylepšený poměr signál-šum a dynamický rozsah oproti 8bitovému komprimovanému PCM
- Zajišťuje interoperabilitu mezi síťovými zařízeními od různých výrobců

## Související pojmy

- [PCM – Pulse Code Modulation](/mobilnisite/slovnik/pcm/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [UPCMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/upcmi/)
