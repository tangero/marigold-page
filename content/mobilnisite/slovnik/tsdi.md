---
slug: "tsdi"
url: "/mobilnisite/slovnik/tsdi/"
type: "slovnik"
title: "TSDI – Transceiver Speech & Data Interface"
date: 2025-01-01
abbr: "TSDI"
fullName: "Transceiver Speech & Data Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tsdi/"
summary: "Standardizovaná specifikace rozhraní v rámci 3GPP, která definuje elektrické a logické charakteristiky pro připojení vysílací-přijímací jednotky (RF části) mobilního terminálu k jeho základnové pásmov"
---

TSDI je standardizovaná specifikace rozhraní 3GPP, která definuje elektrické a logické charakteristiky pro připojení vysílací-přijímací jednotky (transceiveru) mobilního terminálu k jeho základnové pásmové procesorové jednotce, aby umožnila modulární design a interoperabilitu mezi dodavateli.

## Popis

Rozhraní Transceiver Speech & Data Interface (TSDI) je technická specifikace 3GPP, která standardizuje vnitřní rozhraní v mobilním terminálu (např. telefonu nebo datovém modulu) mezi vysílací-přijímací jednotkou rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) a jednotkou základnového pásma / aplikačního procesoru. Definováno ve slovníku 3GPP (TS 21.905), je klíčovým prvkem pro modularitu designu terminálů. Fyzicky TSDI specifikuje typ konektoru, přiřazení pinů, úrovně elektrických signálů, časování a řídicí signalizaci potřebnou pro toto kritické vnitřní propojení.

Funkčně TSDI přenáší všechny potřebné signály pro provoz terminálu. To zahrnuje digitalizované vzorky řeči (ve vysílacím i přijímacím směru), paketový datový provoz a kritické řídicí informace. Na vysílací cestě poskytuje jednotka základnového pásma digitalizované I/Q vzorky (in-fázové a kvadraturní) nebo modulovaný signál střední frekvence ([IF](/mobilnisite/slovnik/if/)) RF transceiveru, který jej následně převede na vyšší frekvenci, zesílí a vysílá. Na přijímací cestě RF transceiver převede přijímaný signál na nižší frekvenci a digitalizuje jej, přičemž posílá I/Q vzorky nebo demodulovaný datový proud zpět do jednotky základnového pásma pro dekódování. Kromě dat uživatelské roviny přenáší TSDI řídicí signály pro správu RF jednotky: to zahrnuje příkazy pro řízení výkonového zesilovače, ladění frekvenčního syntetizéru (výběr kanálu), řízení zesílení a sledování stavu (např. indikátor síly přijímaného signálu - [RSSI](/mobilnisite/slovnik/rssi/)).

Z architektonického hlediska definice TSDI umožňuje 3GPP jasné oddělení mezi 'front-end' RF částí a 'back-end' digitální částí základnového pásma a aplikačním procesorem. Toto oddělení je pro výrobce terminálů klíčové. Umožňuje odebírat RF transceivery a čipsety základnového pásma od různých polovodičových výrobců, pokud obě komponenty splňují standard TSDI. Také zjednodušuje testování a certifikaci, protože RF jednotky a jednotky základnového pásma lze validovat nezávisle vůči specifikaci rozhraní. V moderních terminálech, i když fyzická implementace může být vysoce integrována do jediného systému na čipu (SoC), logické rozdělení definované koncepty jako je TSDI zůstává relevantní pro design, testování a softwarové abstraktní vrstvy (např. ovladače modemu).

## K čemu slouží

TSDI bylo vytvořeno k řešení základního problému raného průmyslu mobilních telefonů: vázanosti na dodavatele a nedostatku interoperability mezi komponentami terminálu. Před takovou standardizací byli výrobci mobilních přístrojů často nuceni používat vertikálně integrovaný řetězec od jediného dodavatele pro [RF](/mobilnisite/slovnik/rf/) a základnové pásmové komponenty, protože rozhraní mezi nimi byla proprietární. To brzdilo inovace, zvyšovalo náklady a omezovalo flexibilitu designu. Motivací pro TSDI bylo definovat otevřené, standardizované vnitřní rozhraní, které by oddělilo vývoj RF transceiveru od vývoje procesoru základnového pásma.

Zavedením TSDI umožnilo 3GPP konkurenční ekosystém, kde specializovaní výrobci RF čipů a výrobci procesorů základnového pásma mohli vyvíjet produkty nezávisle, s jistotou, že budou spolupracovat, pokud oba dodrží standard. To zrychlilo vývojové cykly terminálů, snížilo náklady prostřednictvím konkurence a umožnilo výrobcům přístrojů kombinovat nejlepší komponenty na trhu. Také zajistilo budoucí kompatibilitu designů, protože jednotka základnového pásma (zajišťující protokolové zásobníky a aplikace) mohla být vylepšena nebo změněna nezávisle na RF front-endu (optimalizovaném pro konkrétní kmitočtová pásma a energetickou účinnost), což bylo obzvláště důležité, když 3GPP v průběhu času přidávalo nové technologie rádiového přístupu (jako UMTS, LTE). TSDI je tedy základním standardem, který podpořil modulární a efektivní vývoj mobilních terminálů od éry 3G dále.

## Klíčové vlastnosti

- Standardizuje elektrické a logické rozhraní mezi RF transceiverem a jednotkou základnového pásma
- Přenáší digitalizované vzorky řeči a paketová data (I/Q nebo modulované datové proudy)
- Obsahuje řídicí signály pro správu RF (výkon, frekvence, zesílení)
- Definuje fyzický konektor a specifikace pinů pro interoperabilitu
- Umožňuje modulární design terminálu a nákup komponent od více dodavatelů
- Podporuje nezávislé testování a certifikaci RF jednotek a jednotek základnového pásma

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TSDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsdi/)
