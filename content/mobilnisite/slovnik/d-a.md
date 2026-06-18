---
slug: "d-a"
url: "/mobilnisite/slovnik/d-a/"
type: "slovnik"
title: "D/A – Digital-to-Analogue"
date: 2025-01-01
abbr: "D/A"
fullName: "Digital-to-Analogue"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/d-a/"
summary: "D/A převod transformuje digitální základnové signály na analogové průběhy pro rádiový přenos. Jde o základní proces v řetězci vysílače základnových stanic a uživatelských zařízení, který umožňuje modu"
---

D/A je převod digitálních základnových signálů na analogové průběhy pro rádiový přenos v řetězci vysílače zařízení mobilní sítě.

## Popis

Převod z digitální do analogové domény (D/A) je kritický proces na fyzické vrstvě v systémech 3GPP, odpovědný za převod diskrétních digitálních signálů (v čase a amplitudě) na spojité analogové signály. Tato transformace probíhá v řetězci vysílače po fázích digitálního zpracování signálu, jako je kanálové kódování, mapování modulace (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)) a digitální přeměna nahoru. D/A převodník ([DAC](/mobilnisite/slovnik/dac/)) přijímá sekvenci digitálních kódových slov, typicky reprezentujících fázovou (I) a kvadraturní (Q) složku, a generuje odpovídající analogový napěťový nebo proudový průběh. Mezi klíčové technické parametry patří rozlišení (bitová hloubka), vzorkovací frekvence, linearita a dynamický rozsah bez nežádoucích složek (SFDR), které společně určují věrnost analogového výstupu a ovlivňují únik do sousedního kanálu a velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)).

Z architektonického hlediska je funkce D/A integrována do vysokofrekvenčních integrovaných obvodů (RFIC) nebo specializovaných datových převodníků v rámci rádiové jednotky ([RU](/mobilnisite/slovnik/ru/)) základnové stanice nebo transceiveru uživatelského zařízení (UE). V typické implementaci digitální základnový procesor vysílá vysokorychlostní digitální tok do DAC, který využívá techniky jako převzorkování, tvarování šumu a interpolační filtry ke zlepšení výkonu a snížení nároků na následný analogový rekonstrukční filtr. Analogový výstup z DAC je poté přiveden přes dolní propustný rekonstrukční filtr k odstranění nežádoucích obrazů, než je přeměřen nahoru na vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) nosnou směšovačem a zesílen pro přenos anténou.

Jeho role v síti je zásadní; kvalita D/A převodu přímo ovlivňuje integritu vysílaného signálu, což se projevuje na klíčových výkonnostních ukazatelích, jako je chybovost ([BER](/mobilnisite/slovnik/ber/)), propustnost a pokrytí. Nedokonalosti v DAC, jako je kvantizační šum, nelineární zkreslení a chvění hodinového signálu, zavádějí zkreslení, která mohou snížit přesnost modulace a zvýšit spektrální růst. Proto je návrh D/A převodníku úzce spojen se systémovými specifikacemi pro emise, citlivost a linearitu definovanými v technických specifikacích 3GPP (TS), zejména těch, které upravují rádiový přenos a příjem (např. TS 36.104 pro LTE, TS 38.104 pro NR). K dosažení přísných požadavků na širokopásmové signály v moderních standardech, jako je LTE-Advanced a 5G NR, se používají pokročilé techniky včetně vysokorozlišovacích DAC (např. 14-16 bitů) a smyček zpětné vazby pro digitální predistorzi (DPD).

## K čemu slouží

Účelem D/A převodu v systémech 3GPP je vytvořit most mezi digitální doménou zpracování informací a analogovou doménou šíření elektromagnetických vln. Moderní bezdrátová komunikace spoléhá na sofistikované digitální zpracování signálu pro korekci chyb, modulaci a vícenásobný přístup, ale fyzické médium – rádiový kanál – je inherentně analogové. D/A převodník řeší problém, jak přesně převést tyto zpracované digitální symboly na analogové průběhy, které lze modulovat na RF nosnou pro efektivní vyzařování. Bez vysoce věrného D/A převodu by byly výhody pokročilých digitálních modulačních schémat ztraceny kvůli zkreslení signálu, což by omezilo datové rychlosti a spektrální účinnost.

Historicky, jak se buněčné systémy vyvíjely z analogových (1G) na digitální (2G a dále), se role D/A převodu stávala stále kritičtější. Rané digitální systémy jako GSM používaly relativně jednoduché DAC pro Gaussovskou minimální fázovou manipulaci (GMSK), ale zavedení kvadraturní amplitudové modulace (QAM) vyššího řádu v 3G a 4G vyžadovalo převodníky s větší linearitou a dynamickým rozsahem, aby se zachovaly body konstelace. Přechod na širokopásmové, vícekanálové signály v LTE a 5G NR, s šířkami pásma až 100 MHz a více, dále zvýšil požadavky na vzorkovací frekvenci a výkon z hlediska nežádoucích složek, což motivovalo pokroky v technologii DAC pro podporu agregace nosných a massive MIMO.

Vytvoření a neustálé vylepšování D/A schopností v rámci standardů 3GPP řeší omezení předchozích přístupů, jako je nedostatečné rozlišení způsobující kvantizační šum, který zhoršuje poměr signálu a šumu (SNR), nebo nedostatečné vzorkovací frekvence vedoucí k aliasingu a emisím mimo pásmo. Specifikací požadavků na výkon v dokumentech jako TS 36.104 a TS 38.104 zajišťuje 3GPP, že se D/A převod nestane úzkým hrdlem pro dosažení vysokých datových rychlostí, nízké latence a spolehlivého připojení slibovaných každou novou generací, a umožňuje tak praktickou realizaci složitých digitálních algoritmů v reálných rádiových vysílačích.

## Klíčové vlastnosti

- Převádí digitální I/Q vzorky na analogové napěťové/proudové průběhy
- Definován kritickými parametry: rozlišení (bity), vzorkovací frekvence, linearita a SFDR
- Nedílná součást řetězce vysílače, předchází přeměně nahoru a výkonovému zesílení
- Výkon přímo ovlivňuje EVM, dodržování spektrální masky a BER
- Využívá techniky jako převzorkování a tvarování šumu ke zvýšení věrnosti
- Podléhá přísným specifikacím 3GPP pro emise a kvalitu signálu

## Definující specifikace

- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [D/A na 3GPP Explorer](https://3gpp-explorer.com/glossary/d-a/)
