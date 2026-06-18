---
slug: "scpa"
url: "/mobilnisite/slovnik/scpa/"
type: "slovnik"
title: "SCPA – Single Carrier Power Amplifier"
date: 2025-01-01
abbr: "SCPA"
fullName: "Single Carrier Power Amplifier"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scpa/"
summary: "Výkonový zesilovač (PA) určený k zesílení jednoho rádiového nosného signálu. Je klíčovou součástí rádiových vysílačů, zejména v základnových stanicích a uživatelských zařízeních, zodpovědnou za zvýšen"
---

SCPA (zesilovač výkonu pro jeden nosný signál) je výkonový zesilovač určený k zesílení jednoho rádiového nosného signálu, který zvyšuje jeho výkon pro vysílání v rádiových zařízeních, jako jsou základnové stanice a uživatelská zařízení.

## Popis

Single Carrier Power Amplifier (SCPA, zesilovač výkonu pro jeden nosný signál) je specializovaný typ výkonového zesilovače používaný v řetězcích pro vysílání rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) v bezdrátových komunikačních systémech. Jeho primární funkcí je zesílit jeden modulovaný RF nosný signál na výkonovou úroveň dostatečnou pro vysílání přes rozhraní vzduchem prostřednictvím antény. SCPA přijímá nízkovýkonový RF signál z modulátoru transceiveru a zvyšuje jeho amplitudu, typicky pracuje v posledním stupni vysílače před anténou. Konstrukce SCPA je optimalizována pro charakteristiky signálu s jedním nosným, což se liší od požadavků na zesilování signálů s více nosnými, jako jsou ty používané v ortogonálním frekvenčním multiplexu s dělením ([OFDM](/mobilnisite/slovnik/ofdm/)).

Klíčovými konstrukčními aspekty pro SCPA jsou jeho pracovní kmitočtové pásmo, výstupní výkon, zisk, účinnost a linearita. Zesilovač musí pracovat v konkrétním kmitočtovém rozsahu definovaném bezdrátovým standardem (např. pásmo pro LTE nebo 5G NR). Výstupní výkon je kritický pro určení pokrytí; SCPA pro základnové stanice mohou dodávat desítky nebo stovky wattů, zatímco SCPA v uživatelských zařízeních dodávají výkon v rozsahu miliwattů až několika wattů. Zisk definuje, jak moc zesilovač zvýší výkon vstupního signálu. Účinnost, často měřená jako účinnost přidaného výkonu (PAE), je prvořadá, protože určuje, kolik stejnosměrného výkonu je přeměněno na užitečný RF výkon oproti ztrátám ve formě tepla. Vysoká účinnost snižuje spotřebu energie a problémy s řízením teploty.

Linearita je dalším zásadním parametrem výkonu. Výkonový zesilovač musí signál zesilovat bez zavádění významného zkreslení, které může způsobit nežádoucí spektrální regrowth (únik do sousedního kanálu) a degradovat velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) modulovaného signálu. Pro modulační schémata s konstantní obálkou (jako Gaussovský minimální fázový posun používaný v časném GSM) jsou požadavky na linearitu méně přísné, což umožňuje vysoce účinné, ale nelineární třídy zesilovačů, jako je třída C. Pro moderní modulační schémata s nekonstantní obálkou (jako [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/) používaná v LTE a 5G) je však vysoká linearita nezbytná, což často vyžaduje použití lineárnějších, ale méně účinných tříd zesilovačů (jako třída A nebo [AB](/mobilnisite/slovnik/ab/)) nebo nasazení linearizačních technik, jako je digitální predistorze ([DPD](/mobilnisite/slovnik/dpd/)). Výkon SCPA přímo ovlivňuje celkový přenosový řetězec, datovou propustnost a výdrž baterie v mobilních zařízeních.

## K čemu slouží

Single Carrier Power Amplifier (SCPA) existuje jako základní stavební prvek prakticky ve všech rádiových vysílačích. Jeho účelem je řešit problém vysílání rádiového signálu na významnou vzdálenost. Signály generované obvody pro modulaci a převod nahoru mají velmi nízký výkon a nejsou schopny se šířit prostorem k přijímači. SCPA poskytuje potřebné zvýšení výkonu. Motivací pro návrh zesilovačů specificky pro jednonosný provoz pramení z charakteristik signálu a systémových požadavků různých generací bezdrátové komunikace.

Historicky mnoho raných digitálních celulárních systémů, jako GSM, využívalo modulaci s jedním nosným a konstantní obálkou. To umožnilo použití vysoce účinných, nelineárních výkonových zesilovačů, maximalizující výdrž baterie v telefonech a snižující provozní náklady základnových stanic. S vývojem celulárních standardů pro podporu vyšších datových rychlostí s komplexnější modulací (např. v EDGE, WCDMA a později v LTE/5G v některých kontextech) se požadavky na linearitu zvýšily. Návrh SCPA pro tyto systémy se stal kompromisem mezi účinností a linearitou. Vytváření pokročilých návrhů SCPA, často integrovaných s linearizačními obvody, bylo motivováno potřebou zachovat přijatelnou účinnost při splnění přísných požadavků na spektrální masku a kvalitu signálu, které ukládají standardy 3GPP, čímž se zajišťuje spolehlivá komunikace a minimalizuje interference do sousedních kanálů a buněk.

## Klíčové vlastnosti

- Zesílení jednoho RF nosného signálu na vysoké výkonové úrovně
- Navržen pro provoz v konkrétních licencovaných nebo nelicencovaných kmitočtových pásmech
- Optimalizován pro klíčový kompromis mezi účinností přidaného výkonu (PAE) a linearitou
- Definován parametry: výstupní výkon, zisk, šířka pásma a šumové číslo
- Často zahrnuje obvody pro tepelný management a ochranu
- Může být realizován pomocí různých polovodičových technologií (GaAs, GaN, LDMOS, CMOS)

## Definující specifikace

- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [SCPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/scpa/)
