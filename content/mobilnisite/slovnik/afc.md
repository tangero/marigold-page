---
slug: "afc"
url: "/mobilnisite/slovnik/afc/"
type: "slovnik"
title: "AFC – Automatic Frequency Control"
date: 2025-01-01
abbr: "AFC"
fullName: "Automatic Frequency Control"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/afc/"
summary: "AFC je mechanismus, který automaticky upravuje kmitočet místního oscilátoru přijímače tak, aby odpovídal nosnému kmitočtu příchozího signálu. Kompenzuje kmitočtové odchylky způsobené Dopplerovým jevem"
---

AFC je mechanismus, který automaticky upravuje kmitočet místního oscilátoru přijímače tak, aby odpovídal nosnému kmitočtu příchozího signálu, a kompenzuje tak odchylky, jako je Dopplerův jev, aby zajistil stabilní demodulaci a spolehlivou komunikaci v mobilních sítích.

## Popis

Automatic Frequency Control (AFC) je základní technika fyzické vrstvy v bezdrátových komunikačních systémech, která zajišťuje přesné sladění kmitočtu místního oscilátoru přijímače s nosným kmitočtem přijímaného signálu. Nesoulad kmitočtů neboli odchylka může vzniknout z několika zdrojů: Dopplerova jevu způsobeného relativním pohybem vysílače a přijímače, inherentních nepřesností a teplotního driftu krystalových oscilátorů a zpoždění šíření. I malé odchylky mohou výrazně zhoršit výkon, protože způsobují fázovou rotaci přijímaných symbolů, což vede ke zvýšení míry bitových chyb ([BER](/mobilnisite/slovnik/ber/)) a v závažných případech ke ztrátě synchronizace a přerušení hovorů. AFC funguje jako uzavřený regulační obvod, který kontinuálně odhaduje kmitočtovou chybu a aplikuje korekční úpravu na obvody kmitočtové syntézy přijímače.

Základní architektura AFC zahrnuje detektor kmitočtové chyby, smyčkový filtr a řízený oscilátor, typicky implementovaný v řetězci digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) přijímače. Detektor kmitočtové chyby odhaduje odchylku analýzou přijímaného signálu, často pomocí pilotních symbolů, struktury fázového závěsu (PLL) nebo pozorováním rotace konstelace signálu v komplexním základním pásmu. Tento odhad chyby je následně přiveden přes smyčkový filtr – který může být jednoduchý zesilovací blok nebo sofistikovanější proporcionálně-integrační ([PI](/mobilnisite/slovnik/pi/)) filtr – aby se vyhladil šum a určil vhodný korekční signál. Tento korekční signál upravuje napětím řízený oscilátor ([VCO](/mobilnisite/slovnik/vco/)) nebo numericky řízený oscilátor (NCO) v kmitočtové syntéze přijímače, čímž posouvá kmitočet místního oscilátoru tak, aby anuloval odhadnutou chybu.

V systémech 3GPP, jako jsou UMTS a LTE, je AFC nedílnou součástí počátečních procedur hledání buňky a synchronizace a zůstává aktivní během nepřetržitého příjmu. Během hledání buňky se musí mobilní stanice (UE) rychle zachytit a zamknout na nosný kmitočet základnové stanice. AFC algoritmy spolupracují s bloky časové synchronizace, aby toho dosáhly. Jakmile je zámek dosažen, AFC smyčka pracuje v režimu sledování, kontinuálně kompenzuje pomalu se měnící odchylky, jako je drift oscilátoru, a rychlejší změny způsobené Dopplerovým jevem, zejména ve scénářích vysokých rychlostí. Návrh AFC smyčky – její šířka pásma, činitel tlumení a rozsah zachycení – představuje kompromis mezi rychlostí sledování, stabilitou a potlačením šumu. Širší pásmo umožňuje rychlejší sledování dynamických změn, ale je náchylnější na šum, zatímco užší pásmo poskytuje lepší filtrování šumu, ale nemusí efektivně sledovat rychlé změny.

Klíčové výkonnostní metriky pro AFC zahrnují dobu zachycení (čas potřebný k dosažení zámku z počáteční odchylky), rozsah sledování (maximální kmitočtová odchylka, kterou dokáže opravit), ustálenou chybu (zbytková odchylka po korekci) a odolnost vůči šumu a rušení. Pokročilé implementace mohou používat adaptivní algoritmy, které upravují parametry smyčky na základě podmínek kanálu nebo odhadované rychlosti UE. Ve vícekanálových systémech, jako je LTE-Advanced s agregací nosných, musí AFC zvládat kmitočtové odchylky napříč více komponentními nosnými, které mohou zažívat různé Dopplerovy jevy. Účinnost AFC přímo ovlivňuje metriky výkonnosti vyšších vrstev, jako je propustnost, latence a úspěšnost předávání spojení, což z ní činí základ spolehlivého provozu fyzické vrstvy ve všech mobilních standardech 3GPP.

## K čemu slouží

AFC existuje, aby řešila základní problém nesouladu kmitočtů mezi vysílačem a přijímačem v rádiové komunikaci, což je problém obzvláště akutní v mobilním prostředí. Bez AFC by i malé kmitočtové odchylky – v řádu stovek hertzů až několika kilohertzů – způsobily, že by přijímaná konstelace signálu v čase rotovala, což by vedlo ke katastrofálním chybám demodulace. V raných mobilních systémech bylo ruční ladění kmitočtu nepraktické a oscilátory s pevným kmitočtem byly nedostatečné kvůli teplotním změnám, stárnutí a Dopplerovu jevu způsobenému pohybem vozidla. Primární motivací pro AFC bylo umožnit stabilní, bezobslužný provoz mobilních terminálů, automaticky kompenzovat tyto dynamické poruchy a udržet spolehlivý komunikační spoj.

Historicky byly limity předchozích přístupů zjevné. Samotné krystalové oscilátory mají omezenou přesnost (typicky ±1 až ±10 ppm), což se převádí na kmitočtové chyby několika kilohertzů na GHz nosných kmitočtech. Dopplerův jev může přidat další odchylky; například na 2 GHz způsobí vozidlo pohybující se rychlostí 120 km/h Dopplerův jev přibližně ±220 Hz. Tyto kombinované chyby by rychle vyřadily konvenční přijímač ze zámku. Rané systémy mohly používat širší přijímací filtry, aby tolerovaly určitou odchylku, ale za cenu zvýšeného šumu a snížené citlivosti. AFC poskytla elegantní řešení pomocí zpětné vazby, umožňující použití cenově přijatelných oscilátorů při dosažení přesné kmitočtové stability vyžadované pro úzkopásmové modulační schémata jako [QPSK](/mobilnisite/slovnik/qpsk/) a [QAM](/mobilnisite/slovnik/qam/) používané v systémech 3GPP.

Vytvoření a standardizace AFC v rámci 3GPP bylo hnací silou potřeby robustní podpory mobility a vysoké spektrální účinnosti. Jak se systémy vyvíjely od GSM (které také používalo AFC) přes UMTS až k LTE, s vyššími nosnými kmitočty a složitější modulací, tolerance vůči kmitočtové chybě se stala ještě přísnější. AFC umožňuje funkce jako rychlé hledání buňky, plynulé předávání spojení a spolehlivý provoz při vysokých rychlostech (např. ve vysokorychlostních vlacích). Je to základní technologie, která řeší fyzickou realitu šíření rádiových vln a nedokonalostí hardwaru, a zajišťuje, že sofistikované protokoly a služby vyšších vrstev definované 3GPP mohou spolehlivě fungovat přes inherentně nestabilní rádiový kanál.

## Klíčové vlastnosti

- Uzavřená smyčka zpětné vazby pro kontinuální korekci kmitočtové chyby
- Kompensace Dopplerova jevu způsobeného relativním pohybem
- Potlačení driftu místního oscilátoru vlivem teploty a stárnutí
- Integrace s procedurami hledání buňky a synchronizace
- Podpora provozu v režimu sledování během ustáleného příjmu
- Konfigurovatelná šířka pásma smyčky pro kompromis mezi rychlostí sledování a odolností vůči šumu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [AFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/afc/)
