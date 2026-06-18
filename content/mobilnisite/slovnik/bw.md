---
slug: "bw"
url: "/mobilnisite/slovnik/bw/"
type: "slovnik"
title: "BW – Bandwidth"
date: 2025-01-01
abbr: "BW"
fullName: "Bandwidth"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bw/"
summary: "Šířka pásma (BW) označuje rozsah frekvencí přidělený pro bezdrátový komunikační kanál, měřený v Hertzech (Hz). Určuje maximální datový tok, který kanál může podporovat dle Shannonovy věty, což z ní či"
---

BW (šířka pásma) je rozsah frekvencí přidělený pro bezdrátový komunikační kanál, měřený v Hertzech, který určuje maximální datový tok kanálu a je základním fyzickým zdrojem v celulárních sítích.

## Popis

Ve standardech 3GPP je šířka pásma (BW) klíčový parametr fyzické vrstvy definující šířku frekvenčního spektra přiděleného pro vysílání a příjem v rádiovém kanálu. Měří se jako rozdíl mezi horní a dolní mezní frekvencí, typicky vyjadřovaný v Hertzech (Hz), s běžnými jednotkami kHz, MHz a GHz. Šířka pásma přímo určuje teoretickou maximální rychlost přenosu dat kanálu, jak je popsáno Shannon-Hartleyho větou (C = B * log₂(1+[SNR](/mobilnisite/slovnik/snr/))), kde kapacita C je úměrná šířce pásma B. V praktických systémech závisí dosažitelná rychlost přenosu dat také na modulačním schématu, kódovacím poměru a technikách mnohonásobného přístupu, ale šířka pásma zůstává hlavním fyzickým omezením.

Pro LTE (Long-Term Evolution) zavedené ve vydání 8 je šířka pásma konfigurovatelný systémový parametr se standardizovanými hodnotami 1,4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz a 20 MHz. Tyto hodnoty odpovídají různému počtu zdrojových bloků ([RB](/mobilnisite/slovnik/rb/)), kde každý RB zabírá 180 kHz. Systémová šířka pásma je vysílána v hlavním informačním bloku ([MIB](/mobilnisite/slovnik/mib/)) na fyzickém kanálu pro vysílání ([PBCH](/mobilnisite/slovnik/pbch/)), aby se uživatelské zařízení (UE) mohlo synchronizovat a přistupovat k síti. Konfigurace šířky pásma ovlivňuje četné procedury fyzické vrstvy včetně hledání buněk, přenosu referenčních signálů, návrhu řídicích kanálů a granularity plánování.

V 5G NR (New Radio) se koncepty šířky pásma vyvinuly s větší flexibilitou. Šířka pásma kanálu je definována na nosnou a může se pohybovat od 5 MHz do 100 MHz pro frekvence pod 6 GHz (FR1) a až do 400 MHz pro pásma milimetrových vln (FR2). NR zavádí koncept části šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), což je souvislá sada bloků fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)) nakonfigurovaná pro UE v rámci celkové šířky pásma kanálu nosné. UE může být nakonfigurováno s více BWP a dynamicky mezi nimi přepínat, což umožňuje úsporu energie, adaptaci na různé požadavky služeb a podporu zařízení s omezenou rádiovou frekvenční ([RF](/mobilnisite/slovnik/rf/)) schopností. Blok synchronizačních signálů (SSB) zabírá pouze část šířky pásma kanálu a zbývající spektrum je využíváno prostřednictvím částí šířky pásma.

Správa šířky pásma zahrnuje několik klíčových komponent: základnová stanice (eNodeB v LTE, gNB v NR) určuje a vysílá systémovou šířku pásma; UE provádí RF ladění a analogově-digitální převod napříč specifikovanou šířkou pásma; zpracovatelské řetězce fyzické vrstvy ([FFT](/mobilnisite/slovnik/fft/)/IFFT, odhad kanálu, ekvalizace) pracují se vzorky odpovídajícími aktivní šířce pásma. Šířka pásma také interaguje s duplexními schématy – v systémech FDD jsou pro uplink a downlink přiděleny samostatné šířky pásma, zatímco v systémech TDD je stejná šířka pásma sdílena v čase. Pokročilé funkce jako agregace nosných kombinují více šířek pásma (komponentní nosné) k dosažení vyšších agregovaných přenosových rychlostí, čímž se šířka pásma stává škálovatelným zdrojem v moderních celulárních sítích.

## K čemu slouží

Šířka pásma existuje jako základní koncept v bezdrátové komunikaci ke kvantifikaci a správě omezeného zdroje frekvenčního spektra. Primární problém, který řeší, je, jak rozdělit elektromagnetické spektrum na použitelné kanály pro současnou komunikaci více uživatelů bez nadměrného rušení. Před standardizovanými definicemi šířky pásma používaly rané rádiové systémy ad-hoc přidělování kanálů vedoucí k neefektivnímu využití spektra a problémům s kompatibilitou. Standardizace hodnot šířky pásma v 3GPP zajišťuje globální interoperabilitu, umožňuje výrobcům zařízení navrhovat rádiové jednotky se známými parametry a umožňuje síťovým operátorům plánovat a nasazovat sítě s předvídatelnými výkonnostními charakteristikami.

Vytvoření konkrétních hodnot šířky pásma v LTE vydání 8 bylo motivováno potřebou flexibilního, a přitom jednoduchého rámce, který by mohl vyhovět různým scénářům nasazení – od venkovských oblastí s požadavky na široké pokrytí až po husté městské buňky vyžadující vysokou kapacitu. Vybrané hodnoty (1,4 až 20 MHz) představovaly kompromis mezi implementační složitostí, dostupností spektra a výkonnostními potřebami. Širší šířky pásma umožňují vyšší špičkové přenosové rychlosti, ale vyžadují dražší RF komponenty s lepší linearitou a vyššími vzorkovacími rychlostmi. Užší šířky pásma snižují náklady a spotřebu energie, což je činí vhodnými pro zařízení IoT a scénáře omezené pokrytím.

Standardizace šířky pásma také řeší problém fragmentovaného globálního přidělování spektra. Různé země přidělují pro mobilní služby různá frekvenční pásma, často s různým množstvím dostupného souvislého spektra. Definováním diskrétních možností šířky pásma umožňuje 3GPP konfigurovat zařízení podle místních předpisů při zachování kompatibility základní fyzické vrstvy. Tento přístup umožňuje úspory z rozsahu ve výrobě zařízení a zároveň podporuje regionální variace. Navíc, jak se sítě vyvíjely ze 4G na 5G, koncepty šířky pásma byly rozšířeny, aby podpořily širší kanály (až 400 MHz v NR) potřebné pro extrémní přenosové rychlosti, a zároveň byly zavedeny části šířky pásma pro efektivní obsluhu různorodých zařízení a služeb na stejné nosné.

## Klíčové vlastnosti

- Určuje maximální teoretickou kapacitu kanálu podle Shannonovy věty
- Konfigurovatelný systémový parametr se standardizovanými hodnotami (např. 1,4, 3, 5, 10, 15, 20 MHz pro LTE)
- Definuje počet dostupných zdrojových bloků v systémech založených na OFDMA
- Vysílán v systémové informaci pro synchronizaci a přístup UE
- Umožňuje flexibilní nasazení napříč různým přidělením spektra
- Interaguje s návrhem RF předkoncového stupně včetně požadavků na vzorkovací frekvenci a filtry

## Definující specifikace

- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report

---

📖 **Anglický originál a plná specifikace:** [BW na 3GPP Explorer](https://3gpp-explorer.com/glossary/bw/)
