---
slug: "eob"
url: "/mobilnisite/slovnik/eob/"
type: "slovnik"
title: "EOB – End Of Block"
date: 2025-01-01
abbr: "EOB"
fullName: "End Of Block"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eob/"
summary: "EOB je řídicí kód nebo signál používaný v telekomunikacích a protokolech přenosu dat k označení konce bloku dat. Slouží jako oddělovač, který informuje přijímač, že přenos definované datové jednotky j"
---

EOB je řídicí signál používaný v protokolech přenosu dat k označení konce datového bloku. Slouží jako oddělovač, který informuje přijímač o dokončení přenosu.

## Popis

End Of Block (EOB) je základní řídicí znak nebo signalizační koncept používaný k vymezení hranice datového bloku v rámci sériového datového toku nebo protokolové datové jednotky. V kontextu specifikací 3GPP, zejména těch souvisejících s kodeky a akustikou terminálů (TS 26.110), je EOB relevantní pro rámcování a přenos paketů zvukových dat. 'Blok' v tomto smyslu označuje logické seskupení dat, například rámec kódované řeči z hlasového kodeku (např. [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)) nebo sadu parametrů. Indikátor EOB signalizuje přijímající entitě, že byl přijat poslední bit nebo bajt aktuálního bloku.

Operačně vysílač sestaví blok dat podle pravidel protokolu – to zahrnuje užitečná data a často také hlavičku. Jakmile je přenos užitečných dat dokončen, vysílač vloží značku EOB. Tato značka může být specifická rezervovaná bitová sekvence, speciální posloupnost znaků nebo může být implikována polem délky v hlavičce. Při příjmu přijímač prohledává příchozí bitový tok. Když detekuje vzor EOB nebo dosáhne délky určené pro blok, ví, že získal kompletní, platnou datovou jednotku. Tento blok pak může předat dalšímu stupni zpracování, například dekodéru, k dalšímu zpracování. Použití EOB je klíčové pro synchronizaci; umožňuje přijímači znovu se synchronizovat se začátkem dalšího bloku, i když byly některé bity v předchozím bloku poškozeny nebo ztraceny, za předpokladu, že samotná značka EOB je správně identifikována.

V digitálních telefonních systémech, jako jsou ty definované 3GPP, jsou hlasová data zpracovávána po rámečcích (např. v 20ms intervalech). Tyto rámečky jsou paketizovány pro přenos přes paketové sítě (VoIP, VoLTE, VoNR). Koncept EOB zajišťuje, že přijímací kodek může správně identifikovat hranice každého řečového rámečku v rámci potenciálně kolísavého paketového toku. To je odlišné od, ale souvisí s, oddělovači vyšších vrstev, jako je End Of Packet v IP. EOB funguje na nižší vrstvě rozhraní kodeku nebo vrstvě datového spoje. Jeho správná implementace je nezbytná pro udržení kvality hlasu, protože nesprávně zarovnané hranice bloků by vedly ke zkreslené dekódování zvuku, což by mělo za následek klikání, praskání nebo úplnou ztrátu srozumitelnosti. Jde o jednoduchý, ale zásadní mechanismus pro spolehlivý sekvenční přenos dat.

## K čemu slouží

Účelem signálu End Of Block je řešit problém rámcování dat a synchronizace v sériové komunikaci. V každém systému, kde jsou data přenášena jako souvislý tok bitů, musí mít přijímač způsob, jak určit, kde jedna logická skupina dat končí a další začíná. Bez oddělovače, jako je EOB, by přijímač neměl žádný vnitřní způsob, jak tok správně segmentovat, což by vedlo k chybné interpretaci dat. Tento problém je zásadní v hlasové komunikaci, kde musí být časově citlivé rámečky dekódovány v přesných intervalech.

Historicky protokoly používaly jednoduché řídicí znaky, jako je EOB (a jeho protějšek, Start Of Block – SOB), aby tuto strukturu poskytly. Než se všudypřítomné rámcování založené na poli délky rozšířilo, byly tyto oddělovače v pásmu primární metodou. Ve specifikacích kodeků 3GPP koncept EOB zajišťuje robustnost rozhraní mezi hardwarovými a softwarovými komponentami zpracovávajícími hlasová data. Řeší omezení předpokladu pevných velikostí bloků nebo spoléhání se pouze na časování, což může být nespolehlivé v systémech s proměnnými zpracovatelskými zpožděními nebo v paketových sítích, kde mohou rámečky přicházet mimo pořadí. Poskytnutím explicitní značky 'konec' protokol zaručuje, že přijímač může vždy identifikovat kompletní datovou jednotku, což umožňuje správné dekódování a nepřerušované přehrávání zvuku, což je základní pro přijatelnou kvalitu služby v mobilní telefonii.

## Klíčové vlastnosti

- Slouží jako oddělovač označující konec přenášeného datového bloku
- Umožňuje synchronizaci rámečků mezi vysílačem a přijímačem v sériovém datovém toku
- Může být implementován jako specifická bitová sekvence, řídicí znak nebo implikován polem délky
- Nezbytný pro správnou funkci řečových kodeků tím, že definuje hranice zvukových rámečků
- Poskytuje přijímači bod pro opětovnou synchronizaci v případě chyb v průběhu toku
- Základní mechanismus nízké úrovně protokolu pro spolehlivý přenos dat orientovaný na bloky

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [EOB na 3GPP Explorer](https://3gpp-explorer.com/glossary/eob/)
