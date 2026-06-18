---
slug: "txu"
url: "/mobilnisite/slovnik/txu/"
type: "slovnik"
title: "TXU – Transmitter Unit"
date: 2020-01-01
abbr: "TXU"
fullName: "Transmitter Unit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/txu/"
summary: "Vysílací jednotka (TXU) je funkční blok v rádiové základnové stanici zodpovědný za převod digitálních základnově-pásmových signálů na rádiové kmitočty pro přenos vzduchem. Zahrnuje zesílení výkonu, fi"
---

TXU je vysílací jednotka v rádiové základnové stanici, která převádí digitální základnově-pásmové signály na rádiové kmitočty pro přenos vzduchem, zajišťuje zesílení výkonu, filtraci a převod na vyšší kmitočet.

## Popis

Vysílací jednotka (TXU) je klíčová hardwarová a funkční součást v rádiové přístupové síti (RAN), která se konkrétně nachází v základnové stanici (např. gNB, eNodeB) nebo ve vzdálené rádiové jednotce (RRU). Tvoří poslední stupeň vysílacího řetězce ve zpracování fyzické vrstvy. Hlavní funkcí TXU je přijmout zpracované digitální základnově-pásmové signály – obsahující modulovaná uživatelská data, řídicí informace a referenční signály – a převést je na analogový signál rádiového kmitočtu ([RF](/mobilnisite/slovnik/rf/)) vhodný pro vyzařování anténou. Tento proces zahrnuje několik klíčových dílčích funkcí prováděných postupně.

Z architektonického hlediska TXU typicky následuje po jednotce základnového pásma ([BBU](/mobilnisite/slovnik/bbu/)) nebo distribuované jednotce ([DU](/mobilnisite/slovnik/du/)) v dělené architektuře. Její klíčové součásti zahrnují digitálně-analogové převodníky ([DAC](/mobilnisite/slovnik/dac/)), směšovače pro převod na vyšší kmitočet, lokální oscilátory, výkonové zesilovače ([PA](/mobilnisite/slovnik/pa/)) a pásmové filtry. Proces začíná převodem digitálních vzorků I/Q (fázového/kvadraturního signálu) na analogový základnově-pásmový signál pomocí DAC. Tento analogový signál je následně převeden na požadovanou nosnou frekvenci směšováním se signálem lokálního oscilátoru. Výsledný RF signál je stále nízkovýkonový a musí být výkonovým zesilovačem výrazně zesílen, aby dosáhl úrovně vysílacího výkonu potřebného pro pokrytí oblasti buňky.

Výkonový zesilovač je často nejkritičtější a nejnáročnější součástí v rámci TXU. Musí zesilovat signál lineárně v širokém dynamickém rozsahu, aby nedocházelo ke zkreslení složitých modulačních schémat (jako 256QAM nebo [OFDM](/mobilnisite/slovnik/ofdm/)) používaných v moderních systémech 3GPP. Nelinearita způsobuje spektrální rozšíření a únik do sousedního kanálu, což je přísně regulováno. Proto návrhy TXU zahrnují linearizační techniky, jako je digitální předzkreslení ([DPD](/mobilnisite/slovnik/dpd/)), kde je základnově-pásmový signál záměrně předem zkreslen komplementárním způsobem k nelinearitě PA, což vede k čistšímu zesílenému výstupu. Zesílený signál nakonec prochází pásmovým filtrem, který potlačuje nežádoucí emise mimo pásmo, než je přiveden na anténní porty.

Její role v síti je zásadní pro rádiový výkon. Charakteristiky TXU přímo určují efektivní izotropně vyzářený výkon ([EIRP](/mobilnisite/slovnik/eirp/)), metriky kvality signálu, jako je velikost chybového vektoru (EVM), a soulad s regulatorními spektrálními maskami. Pokročilé TXU podporují funkce jako Massive MIMO, kde desítky řetězců TXU pracují paralelně pro každý anténní prvek v poli, což vyžaduje přesnou kalibraci amplitudy a fáze napříč všemi jednotkami. Velký důraz je také kladen na energetickou účinnost, protože PA je největším spotřebičem energie v základnové stanici, což pohání výzkum účinnějších architektur PA (např. Dohertyho zesilovačů) a chytrého deaktivování řetězců TXU během období nízkého provozu.

## K čemu slouží

Vysílací jednotka existuje proto, aby řešila základní technickou výzvu spolehlivého doručování věrných, vysokovýkonných rádiových signálů z digitální domény sítě do analogového bezdrátového kanálu. Jádrem problému je překlenutí propasti mezi přesnými nízkonapěťovými digitálními signály generovanými procesory základnového pásma a vysokovýkonnými RF signály potřebnými pro přenos vzduchem na vzdálenost kilometrů. Bez specializované, optimalizované vysílací jednotky by nebylo možné splnit přísné výkonnostní a regulatorní požadavky mobilních sítí.

Řeší specifická omezení integrovaných nebo nespecializovaných vysílacích cest. Starší rádiové systémy často měly jednodušší, méně integrované vysílače s omezenou linearitou a účinností. Jak se standardy 3GPP vyvíjely směrem k používání širších šířek pásma a modulací vyššího řádu (od QPSK ve 3G po 1024QAM v 5G-Advanced), požadavky na linearitu a šum vysílače se exponenciálně zpřísnily. TXU jako definovaný funkční blok motivovala vývoj specializovaných součástek a technik – jako jsou vysoko-lineární výkonové zesilovače, pokročilé algoritmy DPD a nízkofázové kmitočtové syntezátory – pro zachování integrity signálu. To zajišťuje, že sofistikované zisky dosažené v digitálním základním pásmu (prostřednictvím kódování a MIMO) nejsou ztraceny v analogovém přenosu.

Historicky byl tento koncept nedílnou součástí již od prvních základnových stanic, ale jeho standardizace a explicitní odkazy ve specifikacích 3GPP (např. v požadavcích na výkon pro rádiový přenos UE a základnových stanic) se staly podrobnějšími s důrazem na energetickou účinnost sítí (významně od Rel-12 se studiemi o úsporách energie základnových stanic) a nástupem systémů s aktivními anténami (AAS). Účel TXU se rozšířil z pouhé konverze signálu na klíčový nástroj pro optimalizaci celkových nákladů vlastnictví (prostřednictvím úspor energie) a umožnění nových anténních technologií, jako je formování svazku, kde koordinované řízení více TXU je nezbytné pro utváření vysílaného rádiového svazku.

## Klíčové vlastnosti

- Provádí digitálně-analogový převod a převod základnově-pásmových signálů na vyšší kmitočet RF nosné
- Zahrnuje vysokovýkonové zesilovače (PA) s linearizačními technikami, jako je digitální předzkreslení (DPD)
- Obsahuje filtraci pro zajištění, že vysílaný signál splňuje regulatorní masky spektrálních emisí
- Podporuje více anténních portů pro aplikace MIMO a formování svazku
- Navržena pro vysokou linearitu k zachování složitých modulačních schémat (např. OFDM, vysokého řádu QAM)
- Zaměření na energetickou účinnost, často s adaptivním řízením výkonu a pokročilými architekturami PA

## Definující specifikace

- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background
- **TS 38.817** — 3GPP TR 38.817

---

📖 **Anglický originál a plná specifikace:** [TXU na 3GPP Explorer](https://3gpp-explorer.com/glossary/txu/)
