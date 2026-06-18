---
slug: "vga"
url: "/mobilnisite/slovnik/vga/"
type: "slovnik"
title: "VGA – Variable Gain Amplifier"
date: 2025-01-01
abbr: "VGA"
fullName: "Variable Gain Amplifier"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vga/"
summary: "Kritická RF komponenta v bezdrátových transceiverech, která poskytuje nastavitelnou zesilovačku signálu. Její zesílení lze dynamicky řídit pro udržení optimálních úrovní signálu za různých podmínek př"
---

VGA je kritická RF komponenta v bezdrátových transceiverech, která poskytuje nastavitelnou zesilovačku signálu, přičemž její zesílení je dynamicky řízeno pro udržení optimálních úrovní signálu za různých podmínek přenosového kanálu.

## Popis

Zesilovač s nastavitelným zesílením (Variable Gain Amplifier, VGA) je základní analogová/[RF](/mobilnisite/slovnik/rf/) integrovaná součástka hojně používaná v radiofrekvenčním (RF) front-endu jak uživatelských zařízení (UE), tak základnových stanic (gNB) v mobilních komunikačních systémech. Její primární funkcí je zesílení slabého příchozího RF nebo mezifrekvenčního ([IF](/mobilnisite/slovnik/if/)) signálu s faktorem zesílení, který lze elektronicky upravit nebo naprogramovat. Tato nastavitelnost je klíčová pro zvládnutí obrovského dynamického rozsahu přijímaných úrovní signálu v mobilním prostředí, který se může lišit o více než 100 dB v důsledku faktorů jako vzdálenost od buňky, útlum a interference. VGA zajišťuje, že signál předávaný následujícím stupňům přijímače, jako je analogově-digitální převodník ([ADC](/mobilnisite/slovnik/adc/)), je na optimální úrovni – dostatečně silný pro přesnou digitalizaci, ale ne tak silný, aby způsoboval saturaci nebo zkreslení.

Z architektonického hlediska je VGA typicky umístěn za počátečním šumově nízkým zesilovačem ([LNA](/mobilnisite/slovnik/lna/)) v přijímacím řetězci a před ADC. Ve vysílacím řetězci může být použit pro řízení výkonu. Funguje tak, že využívá řídicí obvody, které upravují pracovní podmínky zesilovače nebo používají proměnné útlumy ve zpětnovazební smyčce ke změně jeho faktoru zesílení. Řízení zesílení je často řízeno digitálním signálem z baseband procesoru nebo smyčkou automatického řízení zesílení ([AGC](/mobilnisite/slovnik/agc/)). AGC kontinuálně sleduje výkon signálu na vstupu ADC a generuje zpětnovazební signál pro VGA, kterým mu přikazuje zvýšit nebo snížit zesílení pro udržení konstantní cílové úrovně. Tento uzavřený regulační obvod kompenzuje rychlé útlumy a pomalé změny signálu, čímž zajišťuje robustní demodulaci.

Klíčové výkonnostní parametry VGA zahrnují rozsah řízení zesílení (např. 0 až 50 dB), linearitu (měřenou IP3), šumové číslo, šířku pásma a dobu ustálení. V moderních systémech podporujících agregaci nosných a massive [MIMO](/mobilnisite/slovnik/mimo/) musí VGA zvládat široká pásma a více paralelních cest. Jejich role je nedílnou součástí adaptace rádiového spoje a celkového výkonu systému; udržováním signálu v optimálním pracovním bodě ADC maximalizují efektivní počet bitů (ENOB) a minimalizují kvantizační šum. To přímo ovlivňuje datový propust, pokrytí a výdrž baterie, neboť správné nastavení zesílení brání tomu, aby energeticky náročný ADC a digitální procesory pracovaly se signály, které jsou buď příliš slabé na dekódování, nebo zbytečně silné.

## K čemu slouží

VGA existuje proto, aby řešil kritický problém řízení dynamického rozsahu v bezdrátových přijímačích. Mobilní komunikační kanály jsou ze své podstaty proměnlivé; UE může přijímat velmi silný signál v blízkosti základnové stanice a extrémně slabý na okraji buňky. Rané návrhy přijímačů s pevným zesílením byly nedostatečné, protože buď saturovaly a zkreslovaly silné signály (přesytí), nebo nedokázaly dostatečně zesílit slabé signály nad šumovou hladinu následujících stupňů, což vedlo k vysoké chybovosti. To omezovalo efektivní citlivost a provozní dosah zařízení. VGA byl zaveden jako součást systému [AGC](/mobilnisite/slovnik/agc/), aby automaticky přizpůsoboval zesílení přijímače okamžité přijímané síle signálu.

Jeho vývoj v rámci 3GPP release od Rel-12 dále je poháněn rostoucí složitostí a výkonnostními nároky celulárních standardů jako LTE-Advanced, 5G NR a nyní 5G-Advanced. Jak systémy přijímaly širší pásma, modulace vyššího řádu (až 1024QAM) a agregaci nosných, požadavky na linearitu, šumové vlastnosti a rychlost ustálení VGA se staly přísnějšími. Moderní VGA musí podporovat rychlé změny zesílení pro sledování rychlého útlumu ve scénářích s vysokou mobilitou a zvládat současné zesílení více agregovaných nosných bez zavádění intermodulačního zkreslení. Jejich účel přesahuje rámec prostého zesílení a jsou klíčovým prvkem umožňujícím pokročilé funkce přijímače, jako je potlačení interference a vylepšené pokrytí uplinku, což přímo přispívá ke konzistentně vysokým datovým rychlostem a spolehlivému připojení slibovanému moderními celulárními sítěmi.

## Klíčové vlastnosti

- Široký a spojitý rozsah řízení zesílení (typicky 50–80 dB) pro zvládnutí velkých změn signálu
- Rychlá doba ustálení pro sledování rychlého útlumu signálu v mobilním prostředí
- Vysoká linearita (vysoká IP3) pro minimalizaci zkreslení, zvláště kritická pro širokopásmové signály a signály s CA
- Nízké šumové číslo pro zachování citlivosti přijímače při zesilování slabých signálů
- Integrace s digitálními smyčkami automatického řízení zesílení (AGC) pro přesné nastavení úrovně
- Podpora více rozhraní pro řízení zesílení (analogové napětí, digitální kroky, sériová sběrnice)

## Související pojmy

- [AGC – Automatic Gain Control](/mobilnisite/slovnik/agc/)
- [LNA – Low Noise Amplifier](/mobilnisite/slovnik/lna/)
- [ADC – Application Detection and Control](/mobilnisite/slovnik/adc/)

## Definující specifikace

- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [VGA na 3GPP Explorer](https://3gpp-explorer.com/glossary/vga/)
