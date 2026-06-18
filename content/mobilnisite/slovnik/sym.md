---
slug: "sym"
url: "/mobilnisite/slovnik/sym/"
type: "slovnik"
title: "SYM – SYMmetric conditions"
date: 2025-01-01
abbr: "SYM"
fullName: "SYMmetric conditions"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sym/"
summary: "Referenční podmínka používaná ve specifikacích testování výkonu 3GPP, zejména pro řečové a audio kodeky. Definuje konkrétní, vyváženou sadu zhoršení kvality sítě (jako ztráta paketů a zpoždění) apliko"
---

SYM je referenční podmínka pro testování kodeků dle 3GPP, která definuje vyváženou sadu zhoršení kvality sítě aplikovaných stejně v obou směrech, aby simulovala řízené, symetrické síťové prostředí.

## Popis

SYMmetric podmínky (SYM) jsou definovanou sadou parametrů síťového přenosu používanou jako standardizovaná testovací podmínka ve specifikacích 3GPP, zejména v TS 26.935 pro vyhodnocení výkonu řečových a audio kodeků v podmínkách paketově spínaných sítí. Nejde o síťovou funkci nebo protokol, ale o laboratorní referenční model. Podmínka SYM vytváří simulované síťové prostředí, kde jsou na mediální proud v obou směrech – uplink i downlink – mezi dvěma koncovými body (např. dvěma uživatelskými zařízeními, UE) aplikována stejná, tj. symetrická zhoršení kvality. Toto řízené prostředí je klíčové pro provádění reprodukovatelných a srovnatelných subjektivních nebo objektivních testů kvality.

Podmínka je charakterizována konkrétními, kvantifikovanými hodnotami klíčových parametrů zhoršení kvality sítě. Ty typicky zahrnují definovanou koncovou ztrátu paketů (např. konkrétní procento paketů je náhodně nebo v shlucích zahozeno), pevné síťové zpoždění (jednosměrné zpoždění) a může také zahrnovat specifikace pro jitter (variace zpoždění) a distribuci ztráty paketů (např. náhodná ztráta vs. ztráta v shlucích podle Gilbertova-Elliottova modelu). Aspekt 'symetrický' znamená, že pokud je na cestě z koncového bodu A do B aplikována 3% ztráta paketů, je stejná 3% ztráta aplikována i na cestě z B do A. Tím vzniká vyvážený zátěžový test pro algoritmy korekce chyb a odolnosti kodeku.

V praxi jsou testovací zařízení nebo síťové simulátory nakonfigurovány tak, aby na proudy Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) přenášející kódovanou řeč nebo audio uvalily tyto SYM podmínky. Testované kodeky, jako jsou [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/) nebo [EVS](/mobilnisite/slovnik/evs/), jsou pak těmto podmínkám vystaveny. Výsledný výstupní audio signál je hodnocen pomocí subjektivních poslechových testů (jako Mean Opinion Score – [MOS](/mobilnisite/slovnik/mos/)) nebo objektivních algoritmů percepční kvality (jako [POLQA](/mobilnisite/slovnik/polqa/)). Použitím společné sady SYM podmínek lze různé kodeky nebo různé módy stejného kodeku spravedlivě porovnávat, protože jsou všechny testovány ve stejném, přesně definovaném síťovém zatížení. To umožňuje 3GPP standardizovat kodeky se známými výkonnostními charakteristikami za konkrétních scénářů kvality sítě.

## K čemu slouží

SYMmetric podmínky byly definovány za účelem vytvoření společné, reprodukovatelné základny pro hodnocení a porovnávání odolnosti řečových a audio kodeků vůči zhoršení kvality v paketových sítích. Před zavedením takových standardizovaných testovacích podmínek mohlo hodnocení kodeků používat libovolné nebo dodavatelsky specifické profily zhoršení kvality, což ztěžovalo objektivní porovnání výkonnostních tvrzení a výběr nejlepšího kodeku pro standardizaci. Vytvoření SYM (a dalších podmínek jako ASYM – asymetrické) poskytuje řízený 'nejhorší možný' nebo typický scénář, který odráží reálné síťové problémy jako je zahlcení a ztráta.

Jeho účelem je zajistit technickou přísnost v procesu výběru a charakterizace kodeků v 3GPP. Definováním konkrétních symetrických úrovní zhoršení kvality umožňuje konzistentní testování v různých laboratořích a u různých dodavatelů zařízení. Tím se řeší problém nekonzistentních testovacích metodologií a umožňuje vytváření spolehlivých výkonnostních listů pro kodeky. Výsledky za SYM podmínek pomáhají síťovým plánovačům a výrobcům zařízení pochopit, jak se bude kodek chovat v degradovaných, ale vyvážených síťových situacích, a informují tak rozhodnutí o adaptaci módu kodeku a plánování kvality služeb (QoS) sítě. Jde o základní nástroj pro zajištění kvality ve službách voice over LTE (VoLTE) a voice over NR (VoNR).

## Klíčové vlastnosti

- Definuje vyváženou sadu stejných zhoršení kvality sítě (ztráta, zpoždění) v obou přenosových směrech
- Poskytuje standardizovanou, reprodukovatelnou referenci pro testování výkonu kodeků
- Typicky specifikuje parametry jako míra ztráty paketů, síťové zpoždění a model ztráty
- Umožňuje spravedlivé porovnání různých řečových/audio kodeků v řízené zátěži
- Používá se primárně ve spojení se subjektivními (MOS) a objektivními (POLQA) metodami hodnocení kvality
- Zdokumentováno ve specifikacích testování výkonu 3GPP, jako je TS 26.935

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [SYM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sym/)
