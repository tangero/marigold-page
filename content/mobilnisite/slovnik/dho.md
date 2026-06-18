---
slug: "dho"
url: "/mobilnisite/slovnik/dho/"
type: "slovnik"
title: "DHO – Diversity Handover"
date: 2025-01-01
abbr: "DHO"
fullName: "Diversity Handover"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dho/"
summary: "DHO je technika měkkého předávání používaná v sítích UMTS založených na WCDMA, při níž UE (uživatelské zařízení) udržuje současná rádiová spojení s více NodeB během přechodu mezi buňkami. Tím zajišťuj"
---

DHO je technika měkkého předávání v sítích UMTS, při níž uživatelské zařízení udržuje současná spojení s více základnovými stanicemi během změny buňky, aby zajistilo plynulé připojení a zlepšilo kvalitu hovoru.

## Popis

Diversity Handover (DHO), specificky definovaný pro systémy UMTS/[WCDMA](/mobilnisite/slovnik/wcdma/), je forma měkkého předávání, při níž je uživatelské zařízení (UE) během procesu předávání v simultánní komunikaci se dvěma nebo více NodeB (základnovými stanicemi) patřícími k různým buňkám. UE udržuje více aktivních rádiových spojení ve svém Aktivním souboru, který spravuje řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Základním principem je makro-diverzita: stejná data vyslaná UE v uplinku jsou přijata všemi NodeB v Aktivním souboru a data pro downlink vysílaná k UE jsou také odesílána ze všech těchto NodeB.

Z architektonického hlediska se DHO týká UE, zapojených NodeB a RNC. RNC je centrální řídicí entita, která provádí algoritmus předávání, spravuje Aktivní soubor (přidávání a odebírání rádiových spojení na základě měřicích hlášení od UE) a provádí selektivní kombinování v uplinku a vysílání v downlinku. V uplinku každý NodeB přijme signál, dekóduje jej a přepošle výsledný rámec do RNC. RNC vybere nejlepší rámec z přijatých (selektivní kombinování) a přepošle jej do jádra sítě. V downlinku RNC odešle stejný datový proud všem NodeB v Aktivním souboru, které jej následně synchronně vysílají k UE. UE používá RAKE přijímač ke kombinování těchto více přijatých signálů, čímž zlepšuje kvalitu signálu a potlačuje útlum.

Tento proces probíhá kontinuálně, jak se UE pohybuje. UE provádí měření na sousedních buňkách (měření na stejném kmitočtu) a hlásí je RNC prostřednictvím měřicích hlášení. Když signál z nové buňky dostatečně zesílí, RNC zahájí proceduru přidání rádiového spoje. Když signál z existující buňky příliš zeslábne, RNC zahájí proceduru odebrání rádiového spoje. UE je vždy připojeno k alespoň jedné buňce, což zajišťuje nepřerušenou službu. Úlohou DHO je poskytnout plynulou mobilitu, zlepšit pokrytí na hranicích buněk, zvýšit kapacitu díky snížení interference a výrazně zlepšit spolehlivost hovorů v [CDMA](/mobilnisite/slovnik/cdma/) síti, kde všechny buňky používají stejný kmitočet.

## K čemu slouží

DHO byl vytvořen k řešení kritických výzev vlastních [CDMA](/mobilnisite/slovnik/cdma/) buňkovým systémům, jako je UMTS, konkrétně problému 'blízko-daleko' a potřeby plynulé mobility na jediném kmitočtu. Ve [WCDMA](/mobilnisite/slovnik/wcdma/) síti všechny buňky pracují na stejném kmitočtu, což činí tvrdá předávání (přeruš-spoj) riskantními a náchylnými k přerušení hovoru, zejména na hranicích buněk, kde jsou úrovně signálu z více buněk srovnatelné. Účelem DHO je umožnit předávání typu 'spoj-přeruš', které zajišťuje, že UE má vždy alespoň jeden stabilní spoj.

Historicky se vyvinulo z konceptů měkkého předávání v IS-95 (cdmaOne). Pro 3GPP UMTS ([R99](/mobilnisite/slovnik/r99/)) to byla základní funkce mobility pro zaručení kvality služby pro aplikace v reálném čase, jako jsou hlasové a videohovory, v široké oblasti. Odstraňuje omezení tvrdého předávání GSM tím, že eliminuje krátké přerušení během přepínání buněk a poskytuje zisk z diverzity pro potlačení útlumu a stínění. To vede k menšímu počtu přerušených hovorů, lepší kvalitě hlasu na hranicích buněk a efektivnějšímu využití rádiového spektra díky snížené interferenci, protože UE v DHO vysílá s nižším výkonem díky kombinovanému příjmu na více NodeB.

## Klíčové vlastnosti

- Simultánní připojení k více NodeB (správa Aktivního souboru)
- Makro-diverzitní kombinování v uplinku (selektivní kombinování v RNC) a downlinku (RAKE kombinování v UE)
- Plynulý přechod typu 'spoj-přeruš' s nulovou dobou přerušení
- Snižuje vysílací výkon UE díky měkčímu předávání a zisku z diverzity v uplinku
- Zlepšuje pokrytí a kvalitu na hranicích buněk a v překryvných oblastech
- Řízeno RNC na základě měřicích hlášení od UE (Událost 1A, 1B, 1C)

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [DHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/dho/)
