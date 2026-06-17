---
slug: "ep2"
url: "/mobilnisite/slovnik/ep2/"
type: "slovnik"
title: "EP2 – Elementary Procedure 2 (GSM Link Performance)"
date: 2025-01-01
abbr: "EP2"
fullName: "Elementary Procedure 2 (GSM Link Performance)"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ep2/"
summary: "Referenční bod pro měření výkonu rádiového spoje GSM, definovaný jako poměr užitečného signálu k rušení (C/I) 7 dB s hrubou chybovostí bitů (GBER) 8 %. Modeluje náročné podmínky na hranici buňky, kde"
---

EP2 je referenční bod pro měření výkonu rádiového spoje GSM, definovaný jako poměr užitečného signálu k rušení (C/I) 7 dB s hrubou chybovostí bitů (GBER) 8 %, modelující náročné podmínky na hranici buňky.

## Popis

EP2 je standardizovaná testovací podmínka definovaná v dokumentu 3GPP TS 46.055, představující náročnější rádiové prostředí než [EP1](/mobilnisite/slovnik/ep1/). Je charakterizována poměrem užitečného signálu k rušení ([C/I](/mobilnisite/slovnik/c-i/)) 7 dB a cílovou hrubou chybovostí bitů ([GBER](/mobilnisite/slovnik/gber/)) 8 %. Tato podmínka je explicitně definována pro modelování výkonu mobilní stanice GSM při provozu 'na hranici buňky', kde je přijímaná síla signálu z obsluhující buňky relativně slabá a srovnatelná se silou rušivých signálů ze sousedních buněk používajících stejnou frekvenci.

C/I 7 dB znamená, že požadovaný užitečný signál je pouze přibližně pětkrát silnější než rušení. Jedná se o typický scénář v těsných frekvenčních režimech sítí GSM, kde je kapacita maximalizována opakovaným použitím stejných frekvenčních kanálů v geograficky blízkých buňkách. Při tomto nižším C/I je hrubá chybovost bitů na rádiovém kanálu před dekódováním vyšší, proto specifikovaná GBER stoupá na 8 %. Robustní kanálové kódování GSM (včetně konvolučního kódování a prokládání) a algoritmy pro maskování chyb v řečovém kodeku jsou v této podmínce kriticky testovány. Výkon přijímače při EP2 určuje efektivní pokrytí buňky a pravděpodobnost přerušení hovoru nebo špatné kvality hlasu pro uživatele na jejím okraji.

Testování při EP2 je klíčovou součástí typové zkoušky a zkoušky shody pro zařízení GSM. Testovací systém generuje rádiový signál simulující tuto přesnou podmínku C/I a testované zařízení (např. mobilní telefon) musí úspěšně demodulovat a dekódovat kanál pro přenos řeči. Měří se metriky jako míra zamítnutých rámců ([FER](/mobilnisite/slovnik/fer/)) nebo skóre kvality řeči, aby bylo zajištěno, že spadají do přijatelných mezí definovaných standardem. Úspěšné absolvování testů EP2 prokazuje, že zařízení dokáže udržet přijatelnou službu ve scénářích omezených rušením, což je zásadní pro zajištění konzistentního pokrytí a kvality sítě.

## K čemu slouží

EP2 bylo zavedeno za účelem definice minimálního přijatelného výkonu zařízení GSM v podmínkách silného rušení na hranici buňky. Jeho vytvoření bylo motivováno praktickou realitou plánování mobilních sítí: účastníci musí dostávat službu i na geografických hranicích pokrytí buňky, kde je rušení dominantním faktorem. Bez standardizovaného zátěžového testu, jako je EP2, by zařízení mohla vykazovat dobrý výkon při čistém signálu (jako [EP1](/mobilnisite/slovnik/ep1/)), ale na hranicích buněk by selhávala, což by vedlo ke špatnému uživatelskému zážitku a nerovnoměrnému pokrytí sítě.

Řeší problém kvantifikace a vynucení výkonu pro nejhorší běžný provozní scénář. Operátoři sítí potřebují záruky, že koncová zařízení v jejich síti udrží kvalitu hovoru i při nízkých úrovních signálu. Nastavením referenčního bodu na [C/I](/mobilnisite/slovnik/c-i/)=7 dB a [GBER](/mobilnisite/slovnik/gber/)=8 % zajišťuje 3GPP, že všechna kompatibilní zařízení obsahují dostatečnou citlivost přijímače, filtraci a robustnost dekódování pro zvládnutí této úrovně rušení. To přímo ovlivňuje návrh sítě, protože definuje 'hranu propasti' pokrytí, kde musí být spuštěny předávání hovoru nebo kde se může kvalita sítě zhoršit.

Historicky, spolu s EP1, tvořil EP2 jednoduchý, ale účinný dvoubodový model pro charakterizaci výkonu systému v GSM. Byl to klíčový nástroj během masivního globálního nasazení GSM, který umožnil interoperabilitu a konzistentní kvalitu napříč miliardami zařízení. Motivoval průběžné zlepšování přijímacích algoritmů a návrhu antén, protože dodavatelé soutěžili nejen o splnění, ale i o překročení těchto referenčních bodů, čímž zlepšovali celkovou kapacitu sítě a spokojenost uživatelů na hranici buňky.

## Klíčové vlastnosti

- Definuje referenční poměr užitečného signálu k rušení (C/I) 7 dB
- Specifikuje cílovou hrubou chybovost bitů (GBER) 8 %
- Modeluje náročné rádiové podmínky 'na hranici buňky'
- Používá se pro zátěžové testování výkonu přijímače GSM při významném ko-kanálovém rušení
- Určuje efektivní hranici pokrytí a body spouštění předávání hovoru
- Poskytuje klíčový referenční bod pro plánování sítě a zkoušky shody zařízení

## Související pojmy

- [EP1 – Elementary Procedure 1 (GSM Link Performance)](/mobilnisite/slovnik/ep1/)
- [GBER – Average Gross Bit Error Rate](/mobilnisite/slovnik/gber/)

## Definující specifikace

- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [EP2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ep2/)
