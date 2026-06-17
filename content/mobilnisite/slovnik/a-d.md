---
slug: "a-d"
url: "/mobilnisite/slovnik/a-d/"
type: "slovnik"
title: "A/D – Analogue to Digital"
date: 2025-01-01
abbr: "A/D"
fullName: "Analogue to Digital"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/a-d/"
summary: "A/D (analogově-digitální převod) označuje základní proces převodu spojitých analogových signálů na diskrétní digitální reprezentace. Tento převod je klíčový pro moderní telekomunikační systémy, aby mo"
---

A/D (analogově-digitální převod) je základní proces převodu spojitých analogových signálů na diskrétní digitální reprezentace, který je nezbytný pro digitální zpracování, přenos a ukládání v sítích 3GPP.

## Popis

Analogově-digitální (A/D) převod je klíčový proces, který umožňuje digitálním komunikačním systémům rozhraní s fyzickým analogovým světem. V sítích 3GPP k tomuto procesu dochází na více místech, nejkritičtěji v uživatelském zařízení (UE) a potenciálně i v síťových prvcích, jako jsou základnové stanice. Proces zahrnuje vzorkování spojitého analogového signálu v čase a amplitudě (například hlasové vlny z mikrofonu nebo rádiového signálu) v diskrétních časových intervalech a kvantování amplitudy každého vzorku na konečnou sadu digitálních hodnot. Výsledný proud digitálních čísel (obvykle binárních) může být následně zpracován, zakódován, modulován a přenášen přes digitální síťovou infrastrukturu.

Technická implementace zahrnuje několik klíčových fází. Nejprve antialiasingový filtr omezuje šířku pásma vstupního analogového signálu na méně než polovinu vzorkovací frekvence, jak určuje Nyquist-Shannonův teorém vzorkování. Tím se zabrání aliasingu, kdy se vysokofrekvenční složky přeloží zpět do požadovaného frekvenčního pásma a způsobí zkreslení. Filtrovaný signál je poté vzorkován obvodem sample-and-hold, který zachytí jeho napětí v přesných, pravidelných intervalech definovaných vzorkovacím hodinovým signálem. Každý zachycený vzorek je předán kvantizéru, který mapuje spojitou amplitudu na nejbližší diskrétní úroveň z předdefinované sady. Nakonec enkodér převede kvantizovanou úroveň na binární kódové slovo (např. pomocí pulzně kódové modulace - PCM). Rozlišení tohoto převodu je definováno bitovou hloubkou (např. 8-bit, 16-bit), která určuje dynamický rozsah a kvantizační šum.

V kontextu specifikací 3GPP, jako je 26.975 (Specifikace akustických testů terminálu pro hlasovou a videoslužbu) a 46.008 (Rozhraní mobilní stanice - systém základnových stanic ([MS](/mobilnisite/slovnik/ms/) - [BSS](/mobilnisite/slovnik/bss/)); specifikace vrstvy datového spoje ([DL](/mobilnisite/slovnik/dl/))), jsou parametry A/D převodu kriticky definovány pro zajištění interoperability a kvality. Pro hlasové služby prochází analogový audio signál z mikrofonu A/D převodem jako první krok v řetězci hlasového kodeku (např. v kodecích [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)). Vzorkovací frekvence a kvantování musí být pečlivě zvoleny, aby byla vyvážena kvalita hlasu, efektivita šířky pásma a spotřeba energie. Podobně v rádiové oblasti jsou přijímané analogové RF signály převáděny na digitální pro základnové pásmové zpracování pomocí vysokorychlostních, vysokorozlišujících analogově-digitálních převodníků ([ADC](/mobilnisite/slovnik/adc/)) v řetězci RF transceiveru. Výkon těchto ADC, včetně jejich vzorkovací frekvence, efektivního počtu bitů (ENOB) a poměru signál-šum (SNR), přímo limituje dosažitelné datové rychlosti, citlivost a celkový výkon rádiového spoje.

Role A/D převodu sahá za počáteční zachycení signálu. Je nedílnou součástí architektur softwarově definovaného rádia (SDR) a moderních návrhů přijímačů, jako je přímá konverze nebo nulové střední kmitočty, kde je RF signál převeden na digitální co nejdříve, aby umožnil flexibilní, softwarové zpracování signálu. Dále je A/D převod implicitně zapojen do měření kvality kanálu, regulačních smyček výkonu a různých procedur fyzické vrstvy, které spoléhají na digitalizované reprezentace analogového rádiového prostředí. Proto, přestože je A/D základním, obecným elektronickým procesem, je jeho konkrétní implementace a požadavky na výkon v rámci 3GPP pečlivě standardizována, aby byla zaručena konzistentní kvalita a spolehlivý provoz celého ekosystému mobilních sítí, od zastaralých okruhově spínaných hlasových služeb po pokročilé 5G NR systémy s masivním [MIMO](/mobilnisite/slovnik/mimo/).

## K čemu slouží

Účelem A/D převodu v systémech 3GPP je překlenout propast mezi analogovým fyzickým světem a digitálním jádrem moderní telekomunikace pro zpracování a přenos. Všechny reálné informační zdroje – lidský hlas, video, data ze senzorů – a rádiové vlny, které je přenášejí, jsou inherentně analogové. Aby bylo možné využít obrovských výhod digitální technologie – včetně opravy chyb, šifrování, komprese, efektivního multiplexování, odolnosti proti šumu a flexibilního softwarového zpracování – musí být tyto analogové signály přesně převedeny do digitálního formátu. Bez věrného A/D převodu by výhody digitálních mobilních sítí nemohly být realizovány.

Historicky se první mobilní systémy více spoléhaly na analogový přenos (např. 1G AMPS). Přechod na digitální 2G GSM byl zásadně umožněn schopností převést hlas na digitální bitový proud. Tím byly vyřešeny kritické limity analogových systémů: nízká spektrální efektivita, náchylnost k šumu a rušení, nedostatek zabezpečení a omezené možnosti služeb. A/D převod, následovaný zdrojovým a kanálovým kódováním, umožnil efektivní sdílení spektra více uživateli pomocí TDMA/[FDMA](/mobilnisite/slovnik/fdma/), umožnil silné šifrování pro soukromí a položil základy pro datové služby. Neustálý tlak na vyšší datové rychlosti a bohatší služby (3G, 4G, 5G) dále zvýšil požadavky na A/D převodníky, zejména v rádiové předkoncové části, aby podporovaly širší šířky pásma a složitější modulační schémata jako 256-QAM a 1024-QAM.

A/D převod tedy neexistuje jako volitelná součást, ale jako nezbytná umožňující technologie. Řeší základní problém, jak zachytit, zachovat a manipulovat s informacemi z reálného světa v rámci digitální síťové architektury. Referenční specifikace (např. 26.975) definují výkonnostní charakteristiky těchto převodníků v uživatelských zařízeních, aby byla zajištěna konzistentní minimální kvalita uživatelského zážitku pro služby, jako je hlasová telefonie, bez ohledu na výrobce. V podstatě je jeho účelem definovat kvalitu 'digitálních dveří', kterými všechny informace vstupují do sítě 3GPP.

## Klíčové vlastnosti

- Převádí spojité analogové signály v čase a amplitudě na diskrétní digitální data v čase a amplitudě
- Řídí se Nyquist-Shannonovým teorémem vzorkování, aby se zabránilo aliasingovému zkreslení
- Zahrnuje klíčové fáze: antialiasingové filtrování, vzorkování, kvantování a kódování
- Výkon je definován parametry jako vzorkovací frekvence, bitová hloubka (rozlišení) a efektivní počet bitů (ENOB)
- Kritický první krok pro zdrojové kódování (např. hlasové kodeky jako AMR, EVS) a zpracování rádiového základního pásma
- Specifikováno v normách 3GPP pro zajištění akustického výkonu terminálu a interoperability RF rozhraní

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [A/D na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-d/)
