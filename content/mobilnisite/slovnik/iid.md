---
slug: "iid"
url: "/mobilnisite/slovnik/iid/"
type: "slovnik"
title: "IID – Interaural Intensity Difference"
date: 2025-01-01
abbr: "IID"
fullName: "Interaural Intensity Difference"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iid/"
summary: "Stereo audio parametr představující rozdíl úrovně mezi levým a pravým kanálem. Je klíčový pro prostorové vykreslování zvuku a imerzivní zvukové zážitky v multimediálních službách, neboť umožňuje vnímá"
---

IID je interaurální rozdíl intenzity (interaural intensity difference), stereo audio parametr představující rozdíl úrovně mezi levým a pravým kanálem pro prostorové vykreslování zvuku.

## Popis

Interaurální rozdíl intenzity (Interaural Intensity Difference – IID) je základní psychoakustický parametr používaný v systémech prostorového kódování a vykreslování zvuku standardizovaných 3GPP. Kvantifikuje rozdíl ve hladině akustického tlaku (intenzitě) mezi signály dopadajícími na levé a pravé ucho posluchače pro daný audio objekt nebo zdroj. Tento rozdíl v úrovni je spolu s interaurálním časovým rozdílem (Interaural Time Difference – [ITD](/mobilnisite/slovnik/itd/)) jedním z hlavních vodítek, které lidský sluchový systém využívá k lokalizaci zvuku ve vodorovné rovině. V kontextu specifikací 3GPP je IID klíčovým parametrem v rámci parametrického stereo a vícekanálových audio kodeků, jako jsou například ty definované v kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) a v imerzních audio formátech. Umožňuje efektivní reprezentaci stereo nebo vícekanálového zvuku tím, že popisuje prostorový obraz parametrickým způsobem namísto přenosu diskrétních tvarů vln jednotlivých kanálů, což vede k významným úsporám přenosové rychlosti při zachování percepční kvality.

Technicky se IID počítá pro konkrétní časově-frekvenční segmenty uvnitř audio signálu. Audio enkodér analyzuje přicházející signály levého a pravého kanálu, rozloží je na frekvenční subpásma (např. pomocí kvadraturní zrcadlové banky filtrů nebo modifikované diskrétní kosinové transformace). Pro každé subpásmo a časový rámec enkodér vypočítá výkon nebo energii signálu v levém a pravém kanálu. Parametr IID je pak odvozen, často jako logaritmus poměru těchto výkonů (vyjádřený v decibelech). Kladná hodnota IID značí hlasitější signál v levém uchu, což naznačuje pozici zdroje zvuku vlevo, zatímco záporná hodnota značí převahu na pravé straně. Hodnota 0 dB značí vycentrovaný obraz.

V rámci architektury 3GPP jsou tyto vypočtené parametry IID spolu s dalšími prostorovými parametry, jako je mezikanálová koherence (Inter-Channel Coherence – [ICC](/mobilnisite/slovnik/icc/)), kvantovány, zakódovány a multiplexovány do audio datového toku. Odpovídající dekodér tento datový tok přijme, extrahuje parametry a použije je k syntéze stereo nebo vícekanálového výstupu z potenciálně mono snímacího signálu nebo z redukovaného souboru kanálů. Tato parametrická syntéza zahrnuje aplikaci úprav úrovně na audio signály směrované na virtuální levý a pravý reproduktor či binaální vykreslovací jednotky, čímž se znovu vytvoří zamýšlený prostorový dojem. Přesnost a časové/frekvenční rozlišení přenosu parametru IID jsou v normách jako TS 26.405 pro EVS a TS 26.926 pro imerzní audio pečlivě vyváženy s ohledem na omezení přenosové rychlosti.

Role IID přesahuje rámec prostého stereo. V pokročilých audio službách 3GPP, jako je 3D Audio nebo audio pro virtuální realitu (Virtual Reality – VR) specifikované ve vydáních jako Rel-16 a novějších, jsou koncepty IID rozšířeny na objektové audio a ambisoniku vyššího řádu (Higher Order Ambisonics – [HOA](/mobilnisite/slovnik/hoa/)). Zde přispívají rozdíly v úrovni podobné IID k vykreslování audio objektů na konkrétních azimutálních a výškových úhlech kolem posluchače. Jeho přesná reprezentace je klíčová pro telekonference (k rozlišení více mluvčích), mobilní hraní her a doručování imerzních médií přes sítě 5G, protože zajišťuje přesvědčivý a poutavý sluchový zážitek odpovídající vizuálnímu obsahu.

## K čemu slouží

Primárním účelem standardizace parametru interaurálního rozdílu intenzity (Interaural Intensity Difference – IID) v rámci 3GPP bylo umožnit poskytování vysokokvalitních stereo a prostorových audio služeb s efektivním využitím přenosové kapacity přes mobilní sítě. Rané mobilní hlasové služby byly mono, a i když se streamování hudby a videa stalo populárním, přenos plných diskrétních stereo audio kanálů spotřebovával značnou přenosovou kapacitu – což byl vzácný zdroj, zejména v dřívějších sítích 3G a 4G. Motivací bylo vyvinout pokročilé audio kodeky schopné poskytovat imerzní stereo zážitek při nižších přenosových rychlostech než prosté vlnové kódování dvou kanálů, což učinilo služby jako streamování hudby, videohovory s prostorovým zvukem a později imerzní realitní aplikace komerčně a technicky životaschopnými na mobilních zařízeních.

Historicky, před nástupem technik parametrického sterea, nebylo stereo audio podporováno, nebo bylo přenášeno pomocí duálního mono či intenzitního stereo kódování při velmi nízkých přenosových rychlostech, což často vedlo ke špatné prostorové kvalitě, „úzkému“ zvukovému poli či fantomovým centrálním obrazům. Zavedení parametrického sterea s IID jako základním kamenem tyto nedostatky odstranilo. Umožnilo kodekům analyzovat a zachytit podstatné percepční vodítka stereo obrazu odděleně od základního audio obsahu. Toto oddělení znamenalo, že mono snímací audio signál mohl být kódován s vysokou věrností pomocí základního řečového/audio kodeku, zatímco prostorový obraz (definovaný IID a dalšími parametry) byl popsán pouze několika málo dodatečnými bity na rámec. Tento přístup vyřešil problém doručení přijatelné stereo kvality při přenosových rychlostech, kde by tradiční stereo kódování selhalo.

Dále, jak 3GPP rozvíjelo své multimediální schopnosti napříč vydáními, potřeba standardizované a efektivní reprezentace prostorového zvuku se stala klíčovou pro interoperabilitu služeb. Definice IID v rámci specifikací jako TS 26.405 ([EVS](/mobilnisite/slovnik/evs/)) a TS 26.926 (Immersive Audio) zajistila, že enkodéry a dekodéry od různých výrobců budou prostorová vodítka interpretovat a vykreslovat konzistentně. To otevřelo cestu pokročilým službám, jako jsou vylepšené hovory s ambientním zvukem pozadí, 360stupňové video s prostorovým zvukem a síťové audio zpracování, které všechny spoléhají na přesnou manipulaci a přenos interaurálních rozdílů úrovně pro vytvoření věrohodného zvukového prostředí.

## Klíčové vlastnosti

- Kvantifikuje rozdíl úrovně mezi levým a pravým audio kanálem pro časově-frekvenční segment
- Klíčový parametr pro parametrické stereo a prostorové audio kódování v 3GPP
- Umožňuje efektivní reprezentaci stereo obrazu s nízkou přenosovou rychlostí
- Používá se pro lokalizaci zdroje zvuku při vykreslování ve vodorovné rovině
- Integrováno do kodeků jako EVS a Immersive Audio
- Podporuje pokročilé služby jako 3D audio, VR a telekonference

## Definující specifikace

- **TS 26.405** (Rel-19) — Parametric Stereo Encoder for Enhanced aacPlus
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [IID na 3GPP Explorer](https://3gpp-explorer.com/glossary/iid/)
