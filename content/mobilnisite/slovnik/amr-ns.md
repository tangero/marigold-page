---
slug: "amr-ns"
url: "/mobilnisite/slovnik/amr-ns/"
type: "slovnik"
title: "AMR-NS – Adaptive Multi-Rate Noise Suppressor"
date: 2025-01-01
abbr: "AMR-NS"
fullName: "Adaptive Multi-Rate Noise Suppressor"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/amr-ns/"
summary: "AMR-NS je algoritmus pro potlačení šumu integrovaný do řečového kodeku Adaptive Multi-Rate (AMR) za účelem zlepšení kvality hlasu v hlučném prostředí. Zpracovává řečový signál ke snížení hluku na poza"
---

AMR-NS je algoritmus pro potlačení šumu, integrovaný do řečového kodeku AMR, který zpracovává řečový signál za účelem snížení hluku na pozadí, čímž zlepšuje kvalitu hlasu a srozumitelnost při mobilních hovorech v hlučném prostředí.

## Popis

Adaptive Multi-Rate Noise Suppressor (AMR-NS) je komponenta pro zpracování signálu, která funguje ve spojení s řečovým kodekem Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)), jenž je primárním kodekem pro okruhově spínané hlasové služby v sítích 2G a 3G a používá se také ve VoLTE. Jeho architektura je vestavěna do enkodovacího řetězce kodeku, typicky aplikována na vstupní řečový signál před jádrovým kódováním nebo jako součást vnitřních zpracovacích modulů kodeku. Potlačovač funguje tak, že analyzuje spektrální charakteristiky zvukového signálu, aby rozlišil mezi požadovanými řečovými složkami a nežádoucím hlukem na pozadí. Používá algoritmy, jako je spektrální odečítání, Wienerova filtrace nebo pokročilejší statistické modely, k odhadu profilu šumu během neslovních segmentů (např. pauz), a poté potlačuje frekvenční pásma dominovaná šumem, zatímco zachovává řečové harmonické. Klíčové součásti zahrnují odhadovač šumu, detektor hlasové aktivity (VAD) pro identifikaci období řeči a šumu a banku filtrů nebo procesor ve transformační oblasti pro spektrální manipulaci. V síti AMR-NS funguje primárně na straně uživatelského zařízení (UE) během vysílání v uplinku, kde čistí zachycený zvuk před kompresí a přenosem přes rádiové rozhraní, čímž snižuje zátěž přenosové rychlosti způsobenou kódováním šumu a zlepšuje celkovou kvalitu přijímané řeči na druhém konci. Může být také implementován v síťových prvcích, jako jsou mediální brány, pro zpracování v downlinku. Potlačovač se přizpůsobuje různým podmínkám šumu, jako je dopravní hluk, hladina davu nebo vítr, což jej činí nedílnou součástí udržování konzistentní kvality hlasu v mobilním prostředí, kde se uživatelé často pohybují. Jeho integrace je specifikována v dokumentech 3GPP TS 26.077 pro kodek AMR a TS 26.978 pro širokopásmový kodek [AMR-WB](/mobilnisite/slovnik/amr-wb/), což zajišťuje interoperabilitu napříč zařízeními a sítěmi.

## K čemu slouží

AMR-NS byl vytvořen k řešení výrazného zhoršování kvality hlasu v hlučném prostředí, což je běžný problém v mobilních komunikacích. Před jeho zavedením se hluk na pozadí zachycený mikrofony mobilních zařízení kódoval a přenášel spolu s řečí, čímž spotřebovával cennou šířku pásma a snižoval srozumitelnost, zejména v režimech kodeku s nízkou přenosovou rychlostí. To často vedlo k únavě posluchače, zvýšené míře chyb v rozpoznávání řeči a špatné uživatelské zkušenosti, zejména ve scénářích s hands-free nebo venkovním použitím. Primárním cílem bylo zlepšit percepční kvalitu řeči kódované kodekem [AMR](/mobilnisite/slovnik/amr/) bez nutnosti změn stávajících přenosových rychlostí kodeku nebo síťové infrastruktury, a to využitím pokroků v digitálním zpracování signálu. Historicky bylo potlačení šumu často řešeno externími proprietárními řešeními, což vedlo k problémům s interoperabilitou a nekonzistentnímu výkonu. Standardizací AMR-NS v rámci 3GPP počínaje Release 8 byl zajištěn jednotný přístup k redukci šumu, což umožnilo jeho široké přijetí a spolehlivé zlepšení kvality napříč zařízeními a operátory. Vyřešil tak omezení starších kodeků, které postrádaly integrované zpracování šumu, a umožnil čistší přenos hlasu i v náročných akustických podmínkách, což je zásadní pro udržení kvality služeb, jak se mobilní použití rozšiřovalo do různorodých prostředí, jako jsou automobily, veřejné prostory a průmyslová prostředí.

## Klíčové vlastnosti

- Integrované potlačení šumu v rámci kodeků AMR a AMR-WB.
- Adaptivní algoritmy, které v reálném čase odhadují a potlačují hluk na pozadí.
- Detekce hlasové aktivity (VAD) pro rozlišení období řeči a šumu.
- Spektrální techniky zpracování, jako je spektrální odečítání nebo Wienerova filtrace.
- Podpora více režimů a přenosových rychlostí kodeku bez změny jádrového kódování.
- Standardizovaná implementace zajišťující interoperabilitu napříč zařízeními vyhovujícími specifikacím 3GPP.

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report

---

📖 **Anglický originál a plná specifikace:** [AMR-NS na 3GPP Explorer](https://3gpp-explorer.com/glossary/amr-ns/)
