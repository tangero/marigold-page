---
slug: "ltoa"
url: "/mobilnisite/slovnik/ltoa/"
type: "slovnik"
title: "LTOA – Latest Time of Arrival"
date: 2025-01-01
abbr: "LTOA"
fullName: "Latest Time of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ltoa/"
summary: "Latest Time of Arrival je časové měření používané v UTRAN pro určování polohy a synchronizaci. Představuje nejpozději zjištěný čas příchodu signálu na Node B, klíčový pro metody určování polohy založe"
---

LTOA je nejpozdější zjištěný čas příchodu signálu na Node B, používaný v UTRAN pro metody určování polohy jako OTDOA a pro udržování synchronizace v uplinku.

## Popis

Latest Time of Arrival je specifické časové měření definované ve specifikacích 3GPP pro UMTS Terrestrial Radio Access Network. Odkazuje na změřený čas příchodu poslední detekovatelné dráhy rádiového signálu vysílaného z uživatelského zařízení (UE) na přijímač Node B. V kontextu určování polohy je LTOA základním parametrem používaným v metodě pozorovaného časového rozdílu příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) a dalších časově založených technikách určování polohy. Node B změří čas, ve kterém signál od UE dorazí, a porovnáním měření LTOA z více geograficky rozptýlených Node B může síť odhadnout polohu UE pomocí multilaterace.

Architektonicky měření LTOA zahrnuje koordinaci mezi UE, obsluhujícím a sousedními Node B a infrastrukturou pro určování polohy v síti, jako je Serving Mobile Location Centre. UE vysílá uplinkové signály, typicky vyhrazené fyzické kanály nebo referenční signály pro určování polohy. Fyzická vrstva každého zapojeného Node B tyto signály zachytí a použije pokročilé detekční algoritmy, jako jsou přizpůsobené filtry nebo korelátoři, k identifikaci více drah signálu způsobených vícecestným šířením. LTOA je určeno z poslední významné dráhy, která překročí určitý detekční práh, což je důležité pro zajištění, že měření zahrnuje zpožděné odrazy, které stále nesou použitelnou energii.

Proces měření je přísně řízen Radio Network Controllerem prostřednictvím zpráv pro řízení měření. [RNC](/mobilnisite/slovnik/rnc/) nakonfiguruje UE a Node B, co mají měřit a reportovat. Po přijetí konfigurace Node B provádějí kontinuální nebo spouštěná měření uplinkových signálů. Hodnota LTOA je typicky reportována jako časový posun vůči vnitřnímu hodinovému signálu Node B nebo společnému časovému referenčnímu signálu. Tato hrubá měření jsou následně odeslána do RNC nebo vyhrazeného uzlu pro určování polohy, kde jsou kombinována se známými polohami Node B a kalibračními daty pro výpočet polohy UE. Na přesnost LTOA mají vliv faktory jako poměr signálu k šumu, prostředí s vícecestným šířením a synchronizace hodin mezi Node B.

Kromě určování polohy hraje LTOA roli v procedurách synchronizace uplinku, zejména v režimu Time Division Duplex. Node B používá měření času příchodu k odesílání příkazů pro časový posun (timing advance) k UE, čímž zajišťuje, že signály z různých UE dorazí na Node B v očekávaném časovém okně, aby se předešlo interferenci. Mezi klíčové komponenty patří měřicí algoritmy ve fyzické vrstvě Node B, reportovací protokoly přes rozhraní Iub k RNC a algoritmy pro výpočet polohy v core síti. Role LTOA je klíčová pro poskytování služeb založených na poloze, optimalizaci sítě a udržování integrity uplinku v UMTS sítích.

## K čemu slouží

Latest Time of Arrival byl definován pro splnění regulatorních a servisních požadavků na služby určování polohy v mobilních sítích 3G UMTS. S tím, jak se mobilní telefony staly všudypřítomnými, rostla poptávka po přesném síťovém určování polohy ze strany záchranných služeb (jako E-911 v USA) a komerčních aplikací. Tradiční metody založené na Cell ID poskytovaly špatnou přesnost, zatímco [GPS](/mobilnisite/slovnik/gps/) nebyla vždy dostupná uvnitř budov nebo na všech zařízeních. Časově založené metody jako [OTDOA](/mobilnisite/slovnik/otdoa/) nabídly síťově centrické řešení a LTOA poskytlo přesnou měřicí primitivu nezbytnou pro tyto techniky.

Zavedení LTOA řešilo technickou výzvu přesného měření časů příchodu signálu v prostředí s vícecestným šířením rádiového signálu. Dřívější zjednodušená časová měření mohla být zkreslena první přijatou drahou, která mohla být slabým odrazem, nebo šumem. Zaměřením na nejpozději detekovatelný příchodu se LTOA snaží zachytit stabilnější a konzistentnější časovou referenci související s nejdelší přenosovou drahou, což může zlepšit robustnost výpočtu polohy, zejména v podmínkách bez přímé viditelnosti. Bylo to součástí úsilí 3GPP standardizovat sadu metod určování polohy ve vydání Release 4 a pozdějších, což operátorům poskytlo nástroje pro splnění požadavků na přesnost určení polohy.

LTOA také sloužilo účelu zlepšení výkonu uplinku. V [TDD](/mobilnisite/slovnik/tdd/) systémech je přesné časové zarovnání uplinkových přenosů klíčové pro zabránění překryvu časových slotů. Měřením času příchodu signálů od UE mohla síť efektivně spravovat časový posun (timing advance) a LTOA představovalo specifický měřicí bod pro tuto řídicí smyčku. Jeho pokračující přítomnost napříč více vydáními 3GPP, dokonce i když se sítě vyvíjely k LTE a 5G, podtrhuje jeho základní roli ve fyzice měření rádiového signálu. Zatímco pozdější technologie zaváděly pokročilejší referenční signály pro určování polohy, jako jsou Positioning Reference Signals v LTE, základní koncept měření času příchodu signálu pro určení polohy a synchronizaci vznikl u měření jako je LTOA v UMTS.

## Klíčové vlastnosti

- Měření času příchodu poslední detekovatelné dráhy signálu
- Základní vstup pro určování polohy metodou pozorovaného časového rozdílu příchodu (OTDOA)
- Podpora síťového určování polohy bez úpravy UE
- Použití v synchronizaci uplinku a řízení časového posunu (timing advance)
- Reportování Node B k Radio Network Controlleru přes rozhraní Iub
- Robustnost v prostředí s vícecestným šířením

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [LTOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ltoa/)
