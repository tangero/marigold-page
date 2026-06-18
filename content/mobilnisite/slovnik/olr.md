---
slug: "olr"
url: "/mobilnisite/slovnik/olr/"
type: "slovnik"
title: "OLR – Overall Loudness Rating"
date: 2025-01-01
abbr: "OLR"
fullName: "Overall Loudness Rating"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/olr/"
summary: "Celkové hlasitostní číslo (OLR) je objektivní, standardizovaná metrika používaná v 3GPP ke kvantifikaci útlumu nebo zesílení hlasitosti v celé přenosové cestě od konce ke konci. Vypočítává se z jednot"
---

OLR je 3GPP metrika kvantifikující celkový hlasitostní zesil nebo útlum hovoru, vypočítaná z hodnocení vysílací, přijímací a vedlejší (sidetone) cesty za účelem zajištění konzistentní a komfortní hlasitosti.

## Popis

Celkové hlasitostní číslo (OLR) je klíčovým parametrem v 3GPP modelu pro plánování telefonního přenosu, definovaném v [ITU-T](/mobilnisite/slovnik/itu-t/) G.107 E-modelu a přijatém 3GPP. Představuje celkový hlasitostní útlum, který zaznamená řečový signál na úplné cestě od konce ke konci od mluvčího u vysílacího terminálu k posluchači u přijímacího terminálu. OLR je vyjádřeno v decibelech (dB) a je odvozeno z algebraického součtu tří hlavních dílčích čísel: vysílacího hlasitostního čísla (SLR), přijímacího hlasitostního čísla ([RLR](/mobilnisite/slovnik/rlr/)) a členu reprezentujícího efekt maskování vedlejším tónem ([STMR](/mobilnisite/slovnik/stmr/) - Sidetone Masking Rating a [LSTR](/mobilnisite/slovnik/lstr/) - Listener Sidetone Rating).

Výpočet je definován jako OLR = SLR + RLR + 10*log10(1+10^((STMR - LSTR)/10)). SLR charakterizuje útlum od vstupu mikrofonu k síťovému rozhraní, zahrnující akusticko-elektrickou přeměnu a vysílací digitální zpracování. RLR charakterizuje útlum od síťového rozhraní ke sluchátku/reproduktoru, pokrývající přijímací digitální zpracování a elektro-akustickou přeměnu. Člen pro vedlejší tón zohledňuje psychologický efekt, kdy vlastní hlas mluvčího, slyšený přes cestu vedlejšího tónu terminálu, může maskovat vnímanou hlasitost řeči druhé strany.

V síťovém plánování a návrhu terminálů se specifikují cílové hodnoty OLR pro zajištění konzistence hlasitosti. 3GPP definuje výchozí hodnoty OLR a přijatelné rozsahy pro různé typy služeb (např. úzkopásmový, širokopásmový, plnopásmový hovor). Síťoví operátoři a výrobci zařízení navrhují své systémy tak, aby tyto cíle OLR splňovaly, což zahrnuje pečlivé vyvážení SLR a RLR terminálů a přenosového útlumu páteřní sítě. Testy shody pro terminály zahrnují ověření, že jejich OLR (vypočtené z naměřených SLR, RLR a STMR) spadá do standardizovaných limitů, což zajišťuje interoperabilitu a předvídatelný uživatelský zážitek. Specifikace pokrývající OLR zahrnují TS 26.131 (akustické charakteristiky terminálů), TS 26.132 (zpracování zvuku specifické pro kodek) a TS 29.809 (studie monitorování kvality hlasu).

## K čemu slouží

Metrika OLR byla vytvořena, aby vyřešila základní problém nekonzistentní a nepředvídatelné hlasitosti v telefonních hovorech. Historicky, bez standardizovaného plánování hlasitosti, mohly být hovory příliš tiché (způsobující námahu posluchače) nebo příliš hlasité (způsobující zkreslení nebo nepohodlí) v závislosti na konkrétní kombinaci používaných přístrojů a síťového zařízení. Toto degradovalo uživatelský zážitek a ztěžovalo síťovou interoperabilitu.

Jejím účelem je poskytnout objektivní, vypočítatelný cíl pro výkonnost hlasitosti na end-to-end cestě, což umožňuje inženýrům navrhovat sítě a terminály, které poskytují konzistentní a komfortní úroveň poslechu. Řeší omezení pouhého subjektivního testování tím, že nabízí reprodukovatelný inženýrský model. OLR, jako součást širšího E-modelu používaného pro plánování přenosu, umožňuje kvantifikovat a řídit příspěvek hlasitosti každého síťového prvku (terminál, kodek, přenosová linka).

Přijetí OLR ve standardech 3GPP, počínaje systémy 3G, bylo motivováno potřebou zachovat kvalitu hlasu v vyvíjejících se mobilních sítích s různými kodeky, širokopásmovým audiem a VoIP technologiemi. Zajišťuje, že nové služby jako VoLTE a VoNR poskytují stabilitu hlasitosti srovnatelnou nebo lepší než tradiční přepojování okruhů hlasem. Definováním požadavků na OLR zajišťuje 3GPP, že hlasový hovor z 5G smartphonu do staršího 2G přístroje, procházející více generacemi sítí, má stále předvídatelnou a přijatelnou hlasitost, což je základním kamenem kvality základní telefonní služby.

## Klíčové vlastnosti

- Objektivní metrika pro hlasitost přenosu hlasu od konce ke konci (v dB)
- Vypočítává se z vysílacího hlasitostního čísla (SLR), přijímacího hlasitostního čísla (RLR) a parametrů vedlejšího tónu
- Založeno na ITU-T G.107 E-modelu
- Definuje cílové hodnoty a tolerance pro různé šířky pásma hlasu (NB, WB, FB)
- Používá se pro testování shody terminálů a plánování přenosu v síti
- Zajišťuje konzistentní vnímanou hlasitost napříč různými sítěmi a zařízeními

## Související pojmy

- [RLR – Receiver Loudness Rating](/mobilnisite/slovnik/rlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 29.809** (Rel-12) — Diameter Overload Control Study
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [OLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/olr/)
