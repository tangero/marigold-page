---
slug: "tns"
url: "/mobilnisite/slovnik/tns/"
type: "slovnik"
title: "TNS – Transit Network Selection"
date: 2025-01-01
abbr: "TNS"
fullName: "Transit Network Selection"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tns/"
summary: "Mechanismus pro výběr tranzitní sítě pro směrování hovorů mezi různými operátory nebo sítěmi. Je klíčový pro propojení mezi operátory, optimalizaci nákladů a zajištění dokončení hovorů přes administra"
---

TNS je mechanismus pro výběr tranzitní sítě pro směrování hovorů mezi různými operátory, což je klíčové pro propojení mezi operátory, optimalizaci nákladů a dokončení hovorů přes administrativní hranice.

## Popis

Transit Network Selection (TNS) je funkce jádra sítě definovaná ve specifikacích 3GPP, která řídí, jak operátor mobilní sítě ([MNO](/mobilnisite/slovnik/mno/)) vybírá mezilehlou neboli tranzitní síť pro směrování hovoru, když je cíl mimo jeho vlastní síť. Funguje v rámci řídicích funkcí hovorové relace, zejména na straně iniciující sítě. Když je hovor určen pro účastníka v síti jiného operátora nebo v jiné zemi, musí iniciující síť rozhodnout, který zprostředkující přepravce nebo skupina přepravců přenese hovor do cílové sítě. Tento výběr není libovolný; je založen na souboru konfigurovatelných kritérií a dat známých jako seznam nebo data pro výběr tranzitní sítě.

Architektura zahrnuje síťové prvky zodpovědné za řízení hovorů, jako je Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) v okruhově spínaných doménách nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IP Multimedia Subsystem (IMS). Tyto prvky konzultují interní TNS data, která jsou typicky provozovatelem nastavena. Tato data obsahují prioritizovaný seznam preferovaných identifikátorů tranzitních sítí, často používajících kódy jako Carrier Identification Code ([CIC](/mobilnisite/slovnik/cic/)) nebo síťová směrovací čísla. Logika výběru vyhodnocuje faktory jako cílové číslo (např. kód země, národní cílový kód), denní dobu a komerční dohody (např. směrování s nejnižšími náklady). Zvolený identifikátor tranzitní sítě je pak zahrnut do signalizace pro zřízení hovoru, například v Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) v [ISUP](/mobilnisite/slovnik/isup/), aby instruoval následné ústředny o požadované trase.

Jeho role je nedílnou součástí globálního telekomunikačního ekosystému. Umožňuje operátorům strategicky spravovat své vzájemné spojovací vztahy. Výběrem konkrétních tranzitních přepravců může operátor kontrolovat náklady, zajišťovat kvalitu služeb (např. vyhýbáním se přetíženým trasám) a plnit regulatorní požadavky na ukončení hovorů. Mechanismus TNS zajišťuje, že složitá síť bilaterálních a multilaterálních dohod mezi operátory je převedena na rozhodnutí o směrování pro každý jednotlivý hovor, čímž je komunikace mezi operátory možná a ekonomicky životaschopná.

## K čemu slouží

Hlavním účelem Transit Network Selection je řešit základní problém ekonomického a spolehlivého propojení hovorů mezi různými telekomunikačními sítěmi. V počátcích telefonie měli operátoři přímá spojení (interconnekt) s každým dalším operátorem, ke kterému potřebovali dovolat, což se s globálním růstem počtu operátorů stalo nepraktickým. TNS byl vytvořen, aby do tohoto procesu vnesl flexibilitu a efektivitu.

Řeší omezení statického, bod-bod směrování tím, že umožňuje dynamický výběr zprostředkujících přepravců, známých jako tranzitní sítě. To umožňuje operátorům navázat vztahy s několika hlavními tranzitními přepravci namísto přímého spojení s každým možným cílovým operátorem. Motivace byla silně komerční: implementovat směrování s nejnižšími náklady ([LCR](/mobilnisite/slovnik/lcr/)), kde síť automaticky vybírá nejlevnější dostupnou trasu pro hovor na základě dynamicky aktualizovaných obchodních dohod. Dále poskytuje redundanci; pokud je primární tranzitní přepravce nedostupný, systém může přepnout na sekundárního, čímž se zlepšuje míra dokončení hovorů.

Historicky, jak se sítě vyvíjely z národních monopolů do konkurenčního prostředí více operátorů, se potřeba standardizovaného, inteligentního mechanismu směrování stala kritickou. TNS poskytl tento standardizovaný rámec v rámci 3GPP, umožňující operátorům automatizovat složitá rozhodnutí o směrování, která vyvažují náklady, kvalitu a spolehlivost, což by bylo v měřítku milionů hovorů nemožné spravovat manuálně.

## Klíčové vlastnosti

- Umožňuje dynamický výběr zprostředkujících přepravců (tranzitních sítí) pro odchozí hovory.
- Podporuje směrování na základě analýzy cíle (např. kód země, síťový kód).
- Usnadňuje Least Cost Routing (LCR) tím, že upřednostňuje tranzitní možnosti na základě cenových dohod.
- Poskytuje redundanci směrování a schopnost přepnutí na záložní trasu pomocí prioritizovaných seznamů.
- Používá standardizované identifikátory, jako jsou Carrier Identification Codes (CIC), v signalizaci.
- Konfigurovatelné operátorem tak, aby odráželo obchodní dohody a zásady směrování.

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.403** (Rel-19) — Enhanced aacPlus AAC Encoder Specification
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [TNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tns/)
