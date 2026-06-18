---
slug: "agc"
url: "/mobilnisite/slovnik/agc/"
type: "slovnik"
title: "AGC – Automatic Gain Control"
date: 2025-01-01
abbr: "AGC"
fullName: "Automatic Gain Control"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/agc/"
summary: "Automatic Gain Control (AGC) je technika zpracování signálu používaná v bezdrátových přijímačích k automatickému nastavení zesílení zesilovače za účelem udržení konstantní amplitudy signálu pro optimá"
---

AGC je technika zpracování signálu v bezdrátových přijímačích, která automaticky upravuje zesílení zesilovače, aby udržovala konstantní amplitudu signálu pro optimální zpracování, a vyrovnává se tak s kolísáním síly přijímaného signálu.

## Popis

Automatic Gain Control (AGC) je základní součástí řetězce vysokofrekvenčního ([RF](/mobilnisite/slovnik/rf/)) přijímače v uživatelském zařízení (UE) a základnových stanicích (gNodeB/eNodeB) v systémech 3GPP. Jejím hlavním úkolem je stabilizovat amplitudu přijímaného signálu před jeho předáním do analogově-digitálních převodníků ([ADC](/mobilnisite/slovnik/adc/)) a následných stupňů digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)). Bez AGC by příliš slabé signály byly po digitalizaci přehlušeny šumem kvantizace, zatímco příliš silné signály by mohly saturovat ADC, což by vedlo ke zkreslení a ořezávání signálu – obojí by způsobilo vysokou chybovost.

Systém AGC funguje na principu uzavřené zpětnovazební smyčky. Typicky se skládá z zesilovače s proměnným zesílením ([VGA](/mobilnisite/slovnik/vga/)), detektoru výkonu, který měří sílu signálu po zesílení, a řídicího algoritmu. Naměřený výkon je porovnán s požadovanou referenční úrovní. Na základě odchylky řídicí algoritmus generuje korekční signál, který upravuje zesílení VGA. Tento proces je nepřetržitý a dynamický, což umožňuje přijímači přizpůsobit se rychlým změnám podmínek na kanálu, jako jsou ty způsobené rychlým útlumem nebo pohybem uživatele. V širokopásmových systémech, jako jsou LTE a NR, musí AGC zvládat celkový výkon v celé šířce kanálu.

Z architektonického hlediska může implementace AGC zahrnovat více stupňů a jak analogovou, tak digitální doménu. Běžným přístupem je použití hrubé analogové AGC smyčky pro uvedení signálu do dynamického rozsahu ADC, následované jemnou digitální AGC smyčkou v základnovém pásmu pro přesné nastavení zesílení. Návrh musí zohledňovat různé scénáře, včetně přítomnosti silných rušivých signálů v sousedství požadovaného kanálu. Pokročilé AGC algoritmy dokážou rozlišit mezi výkonem požadovaného signálu a interferencí, aby optimalizovaly nastavení zesílení pro signál zájmu.

V kontextu specifikací 3GPP je výkon AGC klíčový pro splnění požadavků na citlivost přijímače, dynamický rozsah a selektivitu sousedního kanálu definovaných v specifikacích pro zkoušky shody (např. TS 38.101-1 pro NR). Umožňuje rádiovému rozhraní efektivně pracovat v širokém rozsahu úrovní signálu, se kterými se setkává v reálném nasazení – od podmínek na okraji buňky až po místa velmi blízko základnové stanice. To zajišťuje konzistentní kvalitu spojení, maximalizuje propustnost a je nezbytné pro funkce, jako je agregace nosných, kde musí být současně přijímány signály z více nosných potenciálně různé síly.

## K čemu slouží

AGC existuje, aby řešila základní problém velkých výkyvů přijímaného výkonu signálu v bezdrátových komunikačních systémech. V mobilním prostředí se síla signálu dramaticky mění v důsledku útlumu na trase, stínění, vícecestného útlumu a interference. Před rozšířením sofistikovaného AGC měly přijímače omezený dynamický rozsah, často vyžadovaly manuální nastavení zesílení nebo trpěly špatným výkonem, když se úroveň signálu odchýlila od ideálního pevného bodu. To omezovalo spolehlivost a efektivní pokrytí bezdrátových sítí.

Vytvoření a zdokonalování AGC bylo motivováno potřebou robustního, bezobslužného provozu mobilních zařízení a infrastrukturního vybavení. Řeší omezení přijímačů s pevným zesílením, které jsou buď snadno saturovány silnými signály, nebo nedokážou dostatečně zesílit slabé signály, což vede k vysoké chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)). Tím, že automaticky udržuje signál v optimálním vstupním rozsahu [ADC](/mobilnisite/slovnik/adc/) a demodulátoru, AGC zajišťuje, že procesor základního pásma přijímá pro dekódování stabilní signál bez ohledu na polohu uživatele nebo okamžité podmínky na kanálu.

Historicky, jak se buněčné standardy vyvíjely od 2G k 5G a podporovaly vyšší šířky pásma, složitou modulaci (jako 256QAM v LTE a 1024QAM v NR) a agregaci nosných, požadavky na linearitu přijímače a dynamický rozsah exponenciálně rostly. AGC se stala ještě kritičtější pro prevenci zkreslení těchto signálů s vysokým řádem modulace. Její implementace umožňuje systémům 3GPP dosáhnout vysoké spektrální účinnosti a datových rychlostí za realistických, proměnných rádiových podmínek, což je základním kamenem moderních mobilních širokopásmových služeb.

## Klíčové vlastnosti

- Dynamické nastavení zesílení přijímacího zesilovače pro udržení konstantní amplitudy signálu
- Uzavřená zpětnovazební regulace využívající měření výkonu a korekci odchylky
- Podpora širokého dynamického rozsahu pro zvládnutí slabých signálů na okraji buňky i silných signálů blízko buňky
- Rychlá adaptace pro sledování rychlých změn útlumu signálu
- Součinnost s potlačením interference optimalizací zesílení pro požadovanou složku signálu
- Umožňuje použití modulace vysokého řádu (např. 1024QAM) prevencí saturace a ořezávání ADC

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TR 38.868** (Rel-17) — Optimizations of pi/2 BPSK uplink power in NR
- **TR 38.886** (Rel-16) — NR V2X UE Radio Transmission & Reception
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec

---

📖 **Anglický originál a plná specifikace:** [AGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/agc/)
