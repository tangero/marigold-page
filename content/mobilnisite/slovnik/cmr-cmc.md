---
slug: "cmr-cmc"
url: "/mobilnisite/slovnik/cmr-cmc/"
type: "slovnik"
title: "CMR/CMC – Codec Mode Request / Codec Mode Command"
date: 2025-01-01
abbr: "CMR/CMC"
fullName: "Codec Mode Request / Codec Mode Command"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cmr-cmc/"
summary: "CMR/CMC je signalizační mechanismus v hlasových službách 3GPP, primárně pro adaptivní vícerychlostní kodeky (AMR) a AMR se širokým pásmem (AMR-WB). Umožňuje přijímací straně hlasového hovoru vyžádat s"
---

CMR/CMC je signalizační mechanismus v hlasových službách 3GPP, který umožňuje přijímací straně hovoru vyžádat si od vysílače konkrétní režim kodeku, čímž optimalizuje kvalitu řeči a využití přenosové kapacity.

## Popis

Codec Mode Request ([CMR](/mobilnisite/slovnik/cmr/)) a Codec Mode Command ([CMC](/mobilnisite/slovnik/cmc/)) jsou nedílnou součástí signalizace v pásmu užitečného signálu používané s adaptivními vícerychlostními řečovými kodeky ([AMR](/mobilnisite/slovnik/amr/)) a AMR se širokým pásmem ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) v systémech 3GPP. Tyto mechanismy fungují uvnitř samotné hlasové přenosové vrstvy, konkrétně v rámci struktury řečových rámců definovaných v 3GPP TS 26.102 (pro AMR) a TS 26.202 (pro AMR-WB). Základní princip spočívá v tom, že přijímač řečového signálu (např. mobilní terminál nebo síťový uzel) analyzuje příchozí podmínky kanálu, jako je chybovost bitů a ztráta rámců, a tyto informace použije k určení optimálního režimu kodeku pro zpětný směr. Toto rozhodnutí je pak sděleno zpět vysílači prostřednictvím pole CMR vloženého do řečových rámců vysílaných v opačném směru.

Z architektonického hlediska funguje CMR/CMC na aplikační vrstvě v rámci hlasového přenosu, nezávisle na podkladovém rádiovém přístupu nebo transportu v jádru sítě. Každý řečový rámec AMR nebo AMR-WB obsahuje hlavičku s poli pro samotná řečová data a řídicí informace v pásmu užitečného signálu. CMR je 4bitové pole (pro AMR), které specifikuje požadavek na jeden z provozních režimů kodeku, které představují různé kompromisy mezi kvalitou řeči a přenosovou rychlostí. Například režimy sahají od nízkorychlostních robustních režimů pro špatné rádiové podmínky až po vysokorychlostní režimy s vysokou kvalitou pro výborné podmínky. Když vysílač přijme rámec obsahující CMR, interpretuje jej jako příkaz (CMC) k přepnutí svého kódování do požadovaného režimu pro následující řečové rámce určené danému přijímači.

Proces je nepřetržitý a obousměrný. Obě strany hlasového hovoru fungují jako vysílače i přijímače, přičemž každá vkládá CMR do svých odchozích řečových rámců, aby řídila režim kodeku používaný druhou stranou. Tím vzniká uzavřený regulační systém pro adaptaci kvality řeči. Síťové prvky, jako je Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) v jádru sítě, se na této signalizaci také podílejí. Mohou upravovat nebo generovat hodnoty CMR/CMC na základě operací překódování nebo síťové politiky, čímž zajišťují end-to-end optimalizaci. Povaha mechanismu v pásmu užitečného signálu zajišťuje nízkou latenci a synchronizaci s tokem řeči, díky čemuž jsou přechody mezi režimy pro uživatele nepostřehnutelné.

Mezi klíčové komponenty patří samotný řečový kodek (AMR nebo AMR-WB), struktura rámce s definovanými poli hlavičky a logika v softwaru terminálu a sítě, která provádí odhad kvality spoje a rozhodování o režimu. Úlohou CMR/CMC je umožnit robustní a kvalitní hlasové služby přes inherentně proměnlivý rádiový kanál. Dynamickým přizpůsobováním přenosové rychlosti kodeku a ochrany proti chybám maximalizuje srozumitelnost řeči při rušení nebo útlumu, zatímco při dobrých podmínkách šetří rádiové zdroje, což přímo ovlivňuje spektrální účinnost a uživatelský zážitek.

## K čemu slouží

[CMR](/mobilnisite/slovnik/cmr/)/[CMC](/mobilnisite/slovnik/cmc/) byl vytvořen, aby řešil problém poskytování konzistentní a kvalitní hlasové služby přes náchylné k chybám a kapacitně omezené rádiové rozhraní v mobilních sítích 2G/3G/4G. Před zavedením adaptivních kodeků, jako je [AMR](/mobilnisite/slovnik/amr/), se používaly kodeky s pevnou přenosovou rychlostí. Kodek s pevnou rychlostí pracující na vysoké přenosové rychlosti by poskytoval výbornou kvalitu za dobrých rádiových podmínek, ale mohl by katastroficky selhat (stát se nesrozumitelným), když se zvýšil počet chyb. Naopak robustní kodek s nízkou přenosovou rychlostí by fungoval za špatných podmínek, ale nevyužíval by dostupnou kapacitu kanálu a poskytoval by podprůměrnou kvalitu, když byly podmínky dobré. Tento přístup typu vše-nebo-nic byl neefektivní a vedl ke špatnému uživatelskému zážitku při pohybu na okraji buňky nebo při rušení.

Zavedení adaptivního vícerychlostního kodeku (AMR) v 3GPP Release 98 (pro GSM) a jeho integrace do UMTS (3G) poskytly řešení: jediný kodek s více provozními režimy. Byl však potřeba mechanismus pro dynamický výběr vhodného režimu. To je právě účel CMR/CMC. Řeší tento problém tím, že umožňuje reálnou, obousměrnou dohodu režimu kodeku na základě skutečných, měřených podmínek spoje na straně přijímače. Přijímač, který nejlépe rozumí kvalitě příchozího signálu, instruuje vysílač, jak optimalizovat odchozí signál pro aktuální stav kanálu. Tato adaptace v uzavřené smyčce maximalizuje pravděpodobnost úspěšného doručení řečových rámců a jejich srozumitelnost za všech podmínek.

Historicky to představovalo významný vývoj oproti síťově řízeným přechodům mezi buňkami a regulaci výkonu jakožto primárním prostředkům pro řízení kvality spoje. CMR/CMC zavedl adaptaci na aplikační vrstvě, specifickou pro službu, která spolupracuje s těmito mechanismy nižších vrstev. Umožnil síťovým operátorům vyvažovat kapacitu a kvalitu podrobněji, čímž připravil cestu pro kvalitní hlasové služby přes paketové sítě (VoIP) v pozdějších vydáních. Technologie byla motivována potřebou spektrální účinnosti (obsloužení více uživatelů na buňku) a zvýšené kvality služeb, což jsou základní komerční hnací síly pro mobilní operátory.

## Klíčové vlastnosti

- Signalizace v pásmu užitečného signálu vložená do hlaviček řečových rámců
- Obousměrné řízení umožňující oběma stranám hovoru žádat o změnu režimu
- Dynamická adaptace založená na měření kvality spoje na straně přijímače v reálném čase
- Podpora více režimů kodeku (např. 8 režimů AMR od 4,75 do 12,2 kbps)
- Přepínání režimů s nízkou latencí synchronizované s tokem řeči
- Průhlednost pro síť umožňující Media Gateway interpretovat a přeposílat příkazy

## Definující specifikace

- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification

---

📖 **Anglický originál a plná specifikace:** [CMR/CMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmr-cmc/)
