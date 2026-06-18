---
slug: "odg"
url: "/mobilnisite/slovnik/odg/"
type: "slovnik"
title: "ODG – Objective Difference Grade"
date: 2025-01-01
abbr: "ODG"
fullName: "Objective Difference Grade"
category: "Services"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/odg/"
summary: "Standardizovaná objektivní metrika percepční kvality videa používaná k hodnocení kvality videa bez lidských pozorovatelů. Kvantifikuje rozdíl mezi referenčním videem a zpracovanou verzí, což je klíčov"
---

ODG je standardizovaná objektivní metrika percepční kvality videa, která slouží k hodnocení kvality videa kvantifikací rozdílu mezi referenčním videem a jeho zpracovanou verzí.

## Popis

Objective Difference Grade (ODG) je klíčová metrika definovaná ve specifikacích 3GPP pro objektivní percepční hodnocení kvality videa. Funguje na principu algoritmického porovnání zpracovaného nebo degradovaného videosignálu s jeho původní, neporušenou referencí. Základní metodologie zahrnuje extrakci percepčních znaků z obou videoproudů, jako jsou prostorové a časové informace, kontrast a detaily hran. Tyto znaky jsou následně analyzovány, aby modelovaly lidské vizuální vnímání a předpověděly subjektivní skóre kvality, které by přiřadil typický divák. Výstupem je jediné číselné skóre, typicky v rozsahu od 0 (nepostřehnutelné zhoršení) po záporné hodnoty označující rostoucí úroveň vnímané degradace (např. -1 pro postřehnutelné, ale neotravné, -2 pro mírně otravné, -3 pro otravné, -4 pro velmi otravné). Tento automatizovaný proces odstraňuje potřebu nákladných a časově náročných panelů subjektivního testování pro rutinní kontroly kvality.

Z architektonického hlediska je výpočet ODG často integrován do testovacích zařízení, síťových sond nebo softwarových analytických nástrojů používaných operátory a výrobci zařízení. Spoléhá se na komplexní percepční modely, jako jsou ty standardizované skupinou Video Quality Experts Group (VQEG) nebo [ITU-T](/mobilnisite/slovnik/itu-t/), na které se specifikace 3GPP odkazují nebo které přizpůsobují. Metrika funguje tak, že zpracovává snímky videa pomocí modelu, který simuluje citlivost lidského zrakového systému na různé typy zkreslení, včetně kompresních artefaktů (blokování, rozmazání), ztráty paketů (zamrznutí, rozkrájení) a přenosových chyb. Klíčové součásti hodnocení zahrnují přesné časové zarovnání referenční a testované sekvence, převod barevného prostoru na percepčně jednotný prostor (jako je CIELAB) a víceúrovňovou prostorovou analýzu, která zohledňuje vzdálenost pozorování a charakteristiky zobrazovacího zařízení.

Její role v ekosystému 3GPP je primárně ve specifikaci a ověřování video kodeků a streamovacích služeb. Například při standardizaci nového profilu video kodeku se jeho výkon hodnotí nejen na základě úspory datového toku, ale také podle skóre ODG, kterého dosahuje při různých datových tocích ve srovnání s referenčním kodekem. Tím se zajišťuje, že zisky v účinnosti komprese nepřicházejí za nepřijatelnou cenu ztráty percepční kvality. Síťoví operátoři používají monitorování založené na ODG k zajištění kvality uživatelského vjemu ([QoE](/mobilnisite/slovnik/qoe/)) pro služby jako mobilní [TV](/mobilnisite/slovnik/tv/), videohovory a streamování. Poskytnutím objektivního a opakovatelného měření umožňuje ODG konzistentní srovnávání napříč implementacemi různých výrobců, síťovými podmínkami a typy zařízení, čímž tvoří kritickou součást řetězce komplexního řízení kvality multimediálních služeb v mobilních sítích.

## K čemu slouží

ODG byla zavedena, aby řešila kritickou potřebu efektivní, škálovatelné a standardizované metody pro hodnocení kvality videa v mobilních sítích. Před jejím přijetím se zajištění kvality do značné míry opíralo o subjektivní testovací metody, jako je střední hodnota uživatelského hodnocení ([MOS](/mobilnisite/slovnik/mos/)), kdy lidské osoby hodnotí videosekvence. Ačkoli je tento přístup přesný, je pro živý mobilní ekosystém s obrovským množstvím kodeků, zařízení a síťových podmínek neúměrně drahý, pomalý a nereprodukovatelný ve velkém měřítku. Průmysl potřeboval objektivní korelát subjektivního hodnocení, který by bylo možné automatizovat pro průběžné testování, vývoj kodeků a optimalizaci sítě.

Vznik ODG motivoval explozivní růst mobilního video provozu a zavedení pokročilých video kodeků, jako je H.264/[AVC](/mobilnisite/slovnik/avc/) a později [HEVC](/mobilnisite/slovnik/hevc/). Vzhledem k tomu, že se operátoři předháněli v kvalitě služeb, byla nutná standardizovaná metrika pro specifikaci minimálních požadavků na kvalitu v technických specifikacích a smlouvách o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). Řeší problém kvantifikace percepčního dopadu kompresních a přenosových zkreslení způsobem, který odpovídá lidské zkušenosti. To umožňuje inženýrům činit informovaná rozhodnutí o kompromisech mezi využitím šířky pásma a vizuální kvalitou a proaktivně detekovat degradaci kvality v síti dříve, než ovlivní velký počet účastníků, čímž se zlepšuje spokojenost zákazníků a snižuje se jejich odchod.

## Klíčové vlastnosti

- Poskytuje standardizované objektivní skóre korelující se subjektivním lidským vnímáním (např. MOS).
- Umožňuje automatizované testování kvality videa ve velkém objemu bez lidských panelů.
- Používá se pro srovnávání a ověřování výkonu video kodeků (např. AVC, HEVC, VVC).
- Podporuje monitorování a zajištění kvality pro mobilní video streamování a vysílání.
- Integruje percepční modely zohledňující prostorové, časové a barevné charakteristiky vidění.
- Poskytuje jedinou metriku (např. na škále od 0 do -4) pro snadnou interpretaci a vytváření upozornění.

## Definující specifikace

- **TS 26.274** (Rel-19) — AMR-WB+ Codec Conformance Testing Specification
- **TS 26.406** (Rel-19) — Enhanced aacPlus Audio Codec Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [ODG na 3GPP Explorer](https://3gpp-explorer.com/glossary/odg/)
