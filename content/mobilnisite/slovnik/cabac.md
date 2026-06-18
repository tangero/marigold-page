---
slug: "cabac"
url: "/mobilnisite/slovnik/cabac/"
type: "slovnik"
title: "CABAC – Context Adaptive Binary Arithmetic Coding"
date: 2025-01-01
abbr: "CABAC"
fullName: "Context Adaptive Binary Arithmetic Coding"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cabac/"
summary: "CABAC je vysoce efektivní metoda entropického kódování používaná ve videokodecích 3GPP ke kompresi videodat. Dosahuje vynikajícího kompresního poměru tím, že přizpůsobuje své pravděpodobnostní modely"
---

CABAC je vysoce efektivní metoda entropického kódování používaná ve videokodecích 3GPP, která přizpůsobuje své pravděpodobnostní modely na základě kontextu, čímž dosahuje vynikající komprese videa v mobilních sítích.

## Popis

Context Adaptive Binary Arithmetic Coding (CABAC) je jádro entropického kódování v několika videokodecích 3GPP, nejvýznamněji v rodinách Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)/H.264) a High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)/H.265) přijatých pro služby jako Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Na rozdíl od jednodušších entropických kodérů funguje CABAC na principu binární aritmetické kódování, což mu umožňuje přiřazovat symbolům zlomkové bity a blížit se tak teoretické Shannonově hranici komprese. Proces začíná převodem nebinárních syntaktických prvků (jako transformační koeficienty nebo rozdíly pohybových vektorů) na posloupnost binárních rozhodnutí (binů) pomocí binarizačních schémat, jako je zkrácené unární kódování, k-tého řádu Exp-Golomb nebo kódování s pevnou délkou.

Klíčovou inovací CABAC je jeho kontextové modelování. Pro mnoho těchto binárních rozhodnutí udržuje CABAC více pravděpodobnostních modelů (kontextů). Výběr konkrétního pravděpodobnostního modelu pro kódování dalšího binu je určen 'kontextem', který je typicky odvozen z hodnot dříve zakódovaných sousedních syntaktických prvků v prostorové, časové nebo frekvenční doméně. Například kontext pro kódování příznaku významného koeficientu může záviset na tom, zda byly koeficienty nad a vlevo významné. Toto kontextově adaptivní modelování umožňuje kodéru dynamicky sledovat lokální statistiku, což jej činí mimořádně efektivním pro nestacionární statistiku videodat.

Samotné kódování provádí binární aritmetický kodér. Ten reprezentuje aktuální pravděpodobnostní interval, který je dále rozdělován na základě pravděpodobnosti nejméně pravděpodobného symbolu (LPS) a nejpravděpodobnějšího symbolu ([MPS](/mobilnisite/slovnik/mps/)). Je vybrán interval odpovídající skutečně zakódovanému binu a kodér začne vypisovat bity, jakmile rozsah intervalu klesne pod prahovou hodnotu přesnosti – proces známý jako renormalizace. Kritickou součástí je aktualizace stavu pravděpodobnosti: po zakódování každého binu je odhad pravděpodobnosti pro daný kontext aktualizován pomocí konečného automatu, aby odrážel nové pozorování a zajistil přesnost modelu. Některé syntaktické prvky, jako znaménka transformačních koeficientů, jsou kódovány v 'bypass' režimu bez kontextového modelování pro nižší složitost.

V rámci ekosystému 3GPP je role CABAC definována v specifikacích konkrétních kodeků. Je povinnou metodou entropického kódování pro Main a High profily AVC a HEVC, což jsou profily vyžadované pro 3GPP konverzační a streamovací služby. Jeho implementace přímo ovlivňuje klíčové ukazatele výkonu pro mobilní operátory: snížením datového toku potřebného pro danou kvalitu videa snižuje zatížení sítě, zlepšuje efektivitu využití spektra a zvyšuje uživatelský komfort umožněním vyššího rozlišení nebo robustnějšího streamování za špatných rádiových podmínek. Výpočetní složitost CABAC je výrazně vyšší než u jeho předchůdce, Context Adaptive Variable Length Coding ([CAVLC](/mobilnisite/slovnik/cavlc/)), ale výrazné úspory datového toku (typicky 10–15 % pro AVC) ospravedlňují jeho zařazení do profilů cílených na efektivní přenos mobilního videa.

## K čemu slouží

CABAC byl vyvinut k řešení základní výzvy komprese videa: snížení datového toku při zachování vnímané kvality, což je úkol prvořadého významu pro mobilní sítě s omezenou a drahou přenosovou kapacitou. Předchozí metody entropického kódování ve videostandardech, jako Huffmanovo kódování s proměnnou délkou ([VLC](/mobilnisite/slovnik/vlc/)) nebo dokonce jednodušší Context Adaptive VLC ([CAVLC](/mobilnisite/slovnik/cavlc/)) používané v Baseline profilu AVC, byly méně efektivní. Přiřazují celočíselný počet bitů každému symbolu a používají statické nebo méně adaptivní pravděpodobnostní modely, což neumožňuje plně využít statistické redundance a korelace přítomné ve videoprvcích. Tato neefektivita se přímo promítala do vyšších datových toků, což omezovalo rozlišení videa, zvyšovalo buffering a spotřebovávalo více síťových prostředků.

Vytvoření CABAC bylo motivováno potřebou výrazného skoku v kódové efektivitě, aby bylo možné zavádět nové videoslužby přes sítě 3G a později 4G LTE. Jak se uživatelská poptávka přesouvala od hlasových hovorů k videohovorům a mobilní televizi, byl vyžadován výkonnější kompresní nástroj. Teorie aritmetického kódování dlouho slibovala téměř optimální kompresi, ale její praktické využití brzdila výpočetní složitost a patentové překážky. Průlom CABAC spočíval ve spojení praktického binárního aritmetického kodéru se sofistikovaným adaptivním kontextovým modelem, což učinilo vysoce efektivní entropické kódování proveditelným pro reálné kódování a dekódování v koncových zařízeních.

Řešením problému efektivity datového toku umožnil CABAC standardizaci videoslužeb v rámci 3GPP, které byly ekonomicky životaschopné pro operátory a poskytovaly uspokojivou kvalitu uživatelského zážitku. Umožnil kodeku AVC dosáhnout přibližně 50% úspory datového toku oproti svému předchůdci MPEG-4 Part 2, přičemž CABAC byl klíčovým přispěvatelem k tomuto zisku. Jeho přijetí ve specifikacích 3GPP znamenalo, že mobilní video může být doručováno při nižších datových tocích, což snižuje zahlcení sítě a náklady na data, nebo při vyšších kvalitách ve stejném datovém toku, což přímo podporovalo obchodní případ pro mobilní streamování videa a videokonference.

## Klíčové vlastnosti

- Jádro binárního aritmetického kódování pro zlomkovou bitovou přesnost a vysokou kompresní efektivitu
- Adaptivní kontextové modelování využívající více pravděpodobnostních stavů na základě sousedních dat
- Binarizační proces pro převod vícehodnotových syntaktických prvků na binární rozhodnutí (biny)
- Samostatné režimy kódování: běžný kontextově adaptivní režim a nízkosložitostní bypass režim
- Integrovaný mechanismus aktualizace pravděpodobnostního stavu pomocí konečného automatu
- Povinné entropické kódování pro vysoce efektivní profily videokodeků 3GPP (např. AVC Main Profile)

## Související pojmy

- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [CABAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cabac/)
