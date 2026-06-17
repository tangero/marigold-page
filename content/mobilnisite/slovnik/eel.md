---
slug: "eel"
url: "/mobilnisite/slovnik/eel/"
type: "slovnik"
title: "EEL – Electric Echo Loss"
date: 2026-01-01
abbr: "EEL"
fullName: "Electric Echo Loss"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eel/"
summary: "Metrika výkonu kvantifikující ztrátu nebo útlum elektrického echového signálu v telekomunikační síti, typicky v kontextu hlasových služeb. Měří účinnost potlačení echa tím, že ukazuje, jak moc je echo"
---

EEL je metrika výkonu, která kvantifikuje útlum elektrického echového signálu v síti a měří účinnost potlačení echa, aby indikovala redukci echa a jeho dopad na kvalitu hlasu.

## Popis

Electric Echo Loss (EEL) je klíčový parametr výkonu přenosu definovaný ve specifikacích 3GPP, který se primárně týká služeb hlasové a multimediální telefonie. Kvantifikuje ztrátu aplikovanou na elektrický echový signál putující zpět ke svému zdroji. Echo v telefonii vzniká, když je hlasový signál mluvčího odražen zpět z hybridního obvodu (který provádí převod mezi dvoudrátovým a čtyřdrátovým vedením) nebo od jiných nepřizpůsobení impedance na přenosové cestě v síti. Pokud není dostatečně utlumeno, stává se toto echo slyšitelným a zhoršuje kvalitu hovoru, zejména při dlouhých přenosových zpožděních běžných u mobilních a mezinárodních hovorů.

Z architektonického hlediska se EEL měří a řídí na specifických místech hlasového přenosového řetězce. V tradiční mobilní síti s přepojováním okruhů je relevantní na rozhraní mezi Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Public Switched Telephone Network (PSTN) nebo uvnitř samotného MSC, kde jsou umístěna zařízení pro řízení echa. V IP Multimedia Subsystem (IMS) pro Voice over LTE (VoLTE) nebo Voice over NR (VoNR) je řízení echa řešeno funkcí Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která zahrnuje Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)) schopný akustického a elektrického potlačení echa. Parametr EEL definuje minimální požadovanou ztrátu, která musí být vnucena jakékoliv elektrické echové cestě, aby bylo zajištěno, že echo je pod vnímatelným prahem.

Metrika funguje tak, že definuje testovací signál (specifický tón nebo řečově podobný signál) vstřikovaný do přijímací cesty (např. od mluvčího na vzdáleném konci) a měří úroveň tohoto signálu vracejícího se na odpovídající vysílací cestu (směrem k mluvčímu na vzdáleném konci) poté, co projde potenciální echovou cestou uvnitř síťového zařízení. EEL je vyjádřen v decibelech (dB). Vyšší hodnota EEL indikuje lepší potlačení echa. Například síťový uzel může být povinen poskytovat EEL 46 dB nebo více, což znamená, že echový signál je utlumen alespoň o 46 dB. Tato ztráta může být dosažena kombinací inherentní ztráty hybridu a aktivního potlačení echa prováděného procesory digitálního signálu.

Jeho role v síti je klíčová pro udržení vysokého Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)) pro kvalitu hlasu. V moderních sítích využívajících IMS a pokročilé komunikační služby jsou požadavky na EEL specifikovány pro mediální brány a MRFP, aby bylo zajištěno konzistentní chování bez ohledu na podkladovou přístupovou technologii (2G, 3G, 4G, 5G). Je součástí souboru metrik kvality hlasu, který zahrnuje také parametry jako zpoždění, ztrátovost paketů a ztráta akustického echa. Dodržování specifikací EEL zajišťuje, že je echo řízeno na síťové straně, čímž se snižuje zátěž uživatelského zařízení při provádění potlačení echa a poskytuje jednotný uživatelský zážitek pro všechny uživatele v síti.

## K čemu slouží

Electric Echo Loss byl zaveden v raných verzích 3GPP (Rel-5), aby řešil přetrvávající problém mluvčího echa v digitálních telekomunikačních sítích. Jak se sítě vyvíjely z analogových na digitální a začaly zahrnovat delší přenosové cesty (např. přes satelity nebo mezinárodní brány), zvýšilo se zpětné zpoždění. I malé množství echa se stává zřetelně slyšitelným a rušivým při zpožděních nad přibližně 20–30 milisekund. Účelem definice EEL bylo stanovit standardizovaný, měřitelný požadavek na výkon síťového zařízení pro potlačení tohoto elektrického echa, čímž se zaručí minimální základní kvalita hlasu pro koncové uživatele.

Problémem, který řeší, je degradace kvality konverzační řeči způsobená nepřizpůsobením impedance, primárně v bodech převodu dvoudrátového na čtyřdrátové vedení (hybridy). Bez dostatečné ztráty slyší mluvčí na vzdáleném konci svůj vlastní hlas odražený se zpožděním. Před standardizovanými metrikami jako EEL bylo řízení echa implementováno ad-hoc způsobem, což vedlo k nekonzistentní kvalitě hlasu napříč různými síťovými segmenty a operátory. Standardizace EEL umožnila objektivní testování a typové schvalování přepojovacích zařízení, mediálních bran a později i IMS mediálních zdrojů, čímž se zajistila interoperabilita a předvídatelný uživatelský zážitek.

Historický kontext pro jeho pokračující relevanci až do Release 20 je přechod na čistě IP sítě a konvergence služeb. Zatímco rané verze se zaměřovaly na hlas s přepojováním okruhů, pozdější verze aplikovaly principy EEL na hlas s přepojováním paketů založený na IMS (VoLTE/VoNR). Řeší omezení, že čistě paketové sítě neřeší inherentně problémy analogového linkového echa; echo může stále pocházet z propojení s legacy PSTN nebo z analogových terminálů připojených přes adaptéry. EEL proto zůstává klíčovým požadavkem na end-to-end mediální cestě, aby bylo zajištěno, že služby vysokokvalitního hlasu a videotelefonie nejsou narušovány echem, bez ohledu na složitost nebo heterogenitu podkladových síťových propojení.

## Klíčové vlastnosti

- Kvantifikuje útlum elektricky odražených řečových signálů v dB
- Definován pro síťová zařízení (např. mediální brány, MRFP)
- Zásadní pro udržení vysoké kvality konverzačního hlasu (MOS)
- Měřen pomocí standardizovaných testovacích signálů a procedur
- Působí v součinnosti s akustickou echokontrolou pro komplexní řízení echa
- Zajišťuje interoperabilitu a konzistentní výkon napříč sítěmi více výrobců

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for
- **TS 33.749** (Rel-19) — Study on security aspects of edge computing enhancement

---

📖 **Anglický originál a plná specifikace:** [EEL na 3GPP Explorer](https://3gpp-explorer.com/glossary/eel/)
