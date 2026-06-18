---
slug: "fir"
url: "/mobilnisite/slovnik/fir/"
type: "slovnik"
title: "FIR – Finite Impulse Response"
date: 2025-01-01
abbr: "FIR"
fullName: "Finite Impulse Response"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fir/"
summary: "Typ digitálního filtru používaného při zpracování signálu v bezdrátové komunikaci, charakterizovaný konečně dlouhou impulsní odezvou. Poskytuje lineární fázi a stabilitu, což je nezbytné pro úlohy jak"
---

FIR je typ digitálního filtru používaného v bezdrátových systémech 3GPP, charakterizovaný konečně dlouhou impulsní odezvou, která zajišťuje lineární fázi a stabilitu pro úlohy jako ekvalizace kanálu nebo tvarování impulsů.

## Popis

Filtr s konečnou impulsní odezvou (FIR) je základní komponenta digitálního zpracování signálů hojně využívaná v technologiích radiového přístupu a fyzické vrstvy 3GPP. Funguje tak, že konvoluje vstupní signál s pevnou sadou koeficientů (odboček) za účelem vytvoření výstupu, přičemž impulsní odezva – výstup filtru při podání jediného impulsního vstupu – má konečnou délku, což znamená, že ustálí na nule během omezeného počtu vzorků. To je v kontrastu s filtry s nekonečnou impulsní odezvou (IIR), které využívají zpětnou vazbu a mohou mít trvalou odezvu. FIR filtry jsou vnitřně stabilní (protože postrádají zpětnou vazbu) a lze je navrhnout tak, aby měly lineární fázovou charakteristiku, což je v komunikacích klíčové pro zabránění zkreslení signálu. V systémech 3GPP se FIR filtry implementují v hardwaru (např. ASIC, FPGA) nebo softwaru uvnitř základnových stanic (eNodeB/gNB) a uživatelských zařízení pro funkce jako modulace, demodulace a kondicionování kanálu.

Z architektonického hlediska se FIR filtr skládá ze tří klíčových prvků: zpožďovací linky, která uchovává minulé vstupní vzorky, sady násobičů, které váží tyto vzorky pomocí koeficientů filtru, a sčítačky, která sumuje vážené vzorky za účelem vytvoření výstupu. Koeficienty určují kmitočtovou odezvu filtru, například dolní propust, horní propust nebo pásmovou propust. V kontextech 3GPP se FIR filtry používají pro tvarování impulsů – např. kořenové kosinusové filtry se zvednutou kosinusovkou v LTE pro omezení šířky pásma a snížení intersymbolové interference – a pro ekvalizaci kanálu za účelem kompenzace vícecestného šíření. Například v 5G NR pomáhají FIR filtry zpracovávat signály ortogonálního multiplexu s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)) odstraňováním emisí mimo pásmo a zlepšováním kvality signálu. Proces návrhu zahrnuje výběr koeficientů na základě kritérií jako zvlnění propustného pásma, útlum nepropustného pásma a šířka přechodu, často s využitím algoritmů jako je Parks-McClellanova metoda.

Jak FIR filtry fungují v praxi, zahrnuje zpracování digitalizovaných rádiových signálů v reálném čase. Když signál prochází bezdrátovým kanálem, je zkreslen šumem a útlumem; FIR ekvalizér na straně přijímače odhadne impulsní odezvu kanálu a aplikuje inverzní filtraci pro obnovení původního signálu. Dále se FIR filtry používají při beamformingu v systémech massive [MIMO](/mobilnisite/slovnik/mimo/) pro vážení signálů antén a směrování energie k určitým uživatelům. Jejich vlastnost lineární fáze zajišťuje, že všechny kmitočtové složky zažívají stejné časové zpoždění, což zachovává tvar vlny – což je klíčový aspekt pro přenosy s vysokou datovou rychlostí. Mezi klíčové výkonnostní metriky patří řád filtru (počet odboček), který ovlivňuje složitost a latenci, a přesnost koeficientů, která ovlivňuje kvantizační šum. Ve specifikacích 3GPP jako TS 26.090 (zpracování kodeku) nebo TS 29.333 (expozice služeb) podporují FIR filtry zpracování zvuku a streamování médií, což ukazuje jejich všestrannost mimo čistě rádiové funkce.

## K čemu slouží

FIR filtry byly v systémech 3GPP přijaty za účelem řešení potřeby spolehlivého, nezkresleného zpracování signálu v digitální komunikaci. Historicky analogové filtry trpěly tolerancemi součástek, teplotními změnami a nelineárními fázovými odezvami, což vedlo ke zhoršení signálu v raných mobilních sítích. Jak sítě přešly na digitální s 3G a novějšími, nabídly FIR filtry softwarově definovanou, přesnou alternativu, kterou bylo možné optimalizovat pro konkrétní standardy jako LTE a 5G. Jejich primárním účelem je tvarovat a čistit signály – řeší problémy jako omezení šířky pásma, potlačení interference a ekvalizace kanálu – což je nezbytné pro dosažení vysoké spektrální účinnosti a datových rychlostí.

Motivace pro použití FIR filtrů vychází z jejich matematických vlastností: stability, lineární fáze a snadného návrhu. V bezdrátovém prostředí způsobuje vícecestné šíření ozvěny, které rozmazávají symboly dohromady (intersymbolová interference); FIR ekvalizéry mohou tento efekt adaptivně invertovat, čímž zlepšují chybovost. Ve srovnání s IIR filtry se FIR vyhýbají problémům se stabilitou a fázovým zkreslením, což je činí vhodnějšími pro aplikace, kde je prvořadá integrita signálu, jako je vysokého řádu [QAM](/mobilnisite/slovnik/qam/) modulace používaná v 5G. Jejich konečná odezva také zjednodušuje implementaci v hardwaru, protože nevyžadují rekurzivní smyčky, které by mohly vést k přetečení nebo nestabilitě.

Od vydání 8 (Release 8) jsou FIR filtry nedílnou součástí pokroků fyzické vrstvy 3GPP a umožňují funkce jako agregace nosných a massive [MIMO](/mobilnisite/slovnik/mimo/). Řeší omezení dřívějších návrhů filtrů tím, že poskytují konzistentní výkon za různých podmínek, podpořené pokroky v rychlostech [DSP](/mobilnisite/slovnik/dsp/) procesorů. FIR filtry v podstatě existují proto, aby zajistily, že vysílané signály odpovídají regulačním maskám, minimalizovaly interferenci v sousedním kanálu a přesně obnovovaly data na přijímači – to vše je klíčové pro splnění výkonnostních cílů 3GPP a podporu vyvíjejících se služeb od hlasu po ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)).

## Klíčové vlastnosti

- Konečně dlouhá impulsní odezva zajišťující stabilitu a předvídatelné chování
- Lineární fázová charakteristika zabraňující fázovému zkreslení při přenosu signálu
- Implementovatelný pomocí konvoluce s pevnou nebo adaptivní sadou koeficientů
- Široké použití při tvarování impulsů, ekvalizaci a beamformingu
- Flexibilita návrhu prostřednictvím optimalizace koeficientů pro konkrétní kmitočtové odezvy
- Vhodnost pro zpracování digitálního signálu v reálném čase v hardwaru i softwaru

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec

---

📖 **Anglický originál a plná specifikace:** [FIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/fir/)
