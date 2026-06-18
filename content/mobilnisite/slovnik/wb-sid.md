---
slug: "wb-sid"
url: "/mobilnisite/slovnik/wb-sid/"
type: "slovnik"
title: "WB-SID – Wideband Silence Insertion Descriptor"
date: 2025-01-01
abbr: "WB-SID"
fullName: "Wideband Silence Insertion Descriptor"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wb-sid/"
summary: "WB-SID je typ rámce používaný v kodecích AMR-WB a EVS k efektivní reprezentaci ticha nebo šumu na pozadí během pauz v řeči. Umožňuje nespojitý přenos (DTX), čímž šetří rádiové prostředky a prodlužuje"
---

WB-SID je typ rámce používaný v kodecích AMR-WB a EVS k efektivní reprezentaci ticha nebo šumu na pozadí, což umožňuje nespojitý přenos za účelem úspory rádiových prostředků a prodloužení výdrže baterie.

## Popis

Wideband Silence Insertion Descriptor (WB-SID) je specializovaný datový rámec definovaný ve specifikacích 3GPP pro kodeky Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Používá se během period ticha nebo šumu na pozadí v hovoru, které jsou identifikovány detektorem hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)). Namísto přenosu běžných řečových rámců obsahujících skutečně zakódovaný audio signál je odeslán rámec WB-SID, který informuje přijímač o charakteristikách šumu na pozadí, což přijímači umožňuje syntetizovat komfortní šum. Tento mechanismus je součástí provozu nespojitého přenosu ([DTX](/mobilnisite/slovnik/dtx/)), kdy vysílač během pauz přestává vysílat plné řečové rámce.

Z architektonického hlediska jsou rámce WB-SID generovány subsystémy VAD a generování komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) řečového kodeku v UE nebo síťovém uzlu (např. [MGW](/mobilnisite/slovnik/mgw/)). V AMR-WB obsahuje rámec WB-SID parametry jako logaritmická energie rámce a sadu lineárních spektrálních frekvencí ([LSF](/mobilnisite/slovnik/lsf/)), které modelují spektrální tvar šumu na pozadí. Tyto parametry jsou odvozeny z posledních několika rámců skutečného šumu na pozadí před začátkem pauzy v řeči. Rámec je výrazně menší než plný řečový rámec (např. 40 bitů oproti několika stovkám bitů), což vede k významné úspoře šířky pásma. V EVS je koncept WB-SID rozšířen pro interoperabilní režim EVS AMR-WB, kde jsou přenášeny podobné parametry, aby byla zajištěna interoperabilita se staršími zařízeními podporujícími AMR-WB.

Fungování WB-SID zahrnuje koordinovaný proces mezi vysílačem a přijímačem. Během pauzy v řeči vysílač analyzuje šum na pozadí, vytvoří rámec WB-SID a vysílá jej sníženou rychlostí (např. jednou za 160 ms nebo podle konfigurace). Přijímač rámec WB-SID dekóduje, extrahuje parametry šumu a použije je k syntéze komfortního šumu prostřednictvím generátoru šumu. Tento syntetický šum přibližně odpovídá původnímu šumu na pozadí (jako je šum v kanceláři nebo zvuky z ulice), čímž zabraňuje nepřirozenému 'hluchému tichu', které by mohlo posluchače znepokojovat. Proces se periodicky opakuje, aby se přizpůsobil měnícím se šumovým podmínkám. Pokud se řeč obnoví, vysílač odešle řečový rámec se značkou označující konec periody ticha.

Role WB-SID v síti je klíčová pro efektivní poskytování hlasových služeb, zejména přes rádiová rozhraní. Snížením počtu přenášených rámců během ticha snižuje přenosovou rychlost v uplinku i downlinku, čímž šetří cenné rádiové prostředky v LTE a NR. To umožňuje multiplexovat více uživatelů na stejném nosiči a zlepšuje kapacitu systému. Navíc pro UE přenos menšího počtu rámců snižuje spotřebu energie a prodlužuje výdrž baterie. WB-SID je řízen mechanismy adaptace režimu kodeku a řízení rádiových prostředků, což zajišťuje správné zacházení s rámci ticha za různých síťových podmínek a při předávání spojení.

## K čemu slouží

WB-SID byl zaveden v 3GPP Release 13 jako součást vývoje širokopásmových hlasových kodeků k řešení neefektivity přenosu ticha během hovorů. Před zavedením [DTX](/mobilnisite/slovnik/dtx/) a SID rámců hlasové kodeky vysílaly rámce nepřetržitě i během pauz, čímž plýtvaly šířkou pásma a výkonem. Úzkopásmé kodeky jako AMR měly SID rámce, ale s přijetím AMR-WB (G.722.2) pro vysokokvalitní hlas byl potřebný širokopásmový ekvivalent, aby byly zachovány výhody DTX bez kompromisů v širším audio pásmu (50-7000 Hz).

Hlavní problém, který WB-SID řeší, je neefektivní využití prostředků během pauz v řeči, které tvoří asi 50-60 % typického rozhovoru. Bez DTX by tyto pauzy spotřebovávaly přenos na plné přenosové rychlosti, což by zatěžovalo rádiovou kapacitu a baterii UE. WB-SID umožňuje DTX pro AMR-WB, což systému umožňuje pracovat v režimu nízké přenosové rychlosti během ticha. To je obzvláště důležité pro VoLTE (Voice over LTE) a VoNR (Voice over NR), kde je hlas přenášen paketově a soutěží o prostředky s daty. Snížením průměrné přenosové rychlosti pomáhá WB-SID zachovat kvalitu hlasu a zároveň uvolňuje prostředky pro další služby.

Navíc WB-SID zajišťuje interoperabilitu a kvalitu ve smíšených nasazeních. S EVS (zavedeným v Rel-12), které podporuje interoperabilní režimy AMR-WB, umožňují rámce WB-SID zařízením vybaveným EVS komunikovat se staršími zařízeními podporujícími AMR-WB a zároveň využívat DTX. Vývoj směrem k EVS přinesl také vylepšené generování komfortního šumu, ale WB-SID poskytuje zpětně kompatibilní mechanismus. WB-SID byl tedy motivován potřebou efektivních, vysokokvalitních hlasových služeb v moderních mobilních sítích, které vyvažují kapacitu, výdrž baterie a uživatelský zážitek.

## Klíčové vlastnosti

- Reprezentuje ticho/šum na pozadí v režimech AMR-WB a EVS AMR-WB IO
- Obsahuje parametry šumu (energie, spektrální tvar) pro generování komfortního šumu
- Umožňuje nespojitý přenos (DTX), čímž snižuje průměrnou přenosovou rychlost
- Malá velikost rámce (např. 40 bitů) ve srovnání s řečovými rámci
- Přenáší se periodicky během pauz v řeči (např. každých 160 ms)
- Podporuje interoperabilitu mezi kodeky EVS a staršími kodeky AMR-WB

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [DTX – Discontinuous Transmission](/mobilnisite/slovnik/dtx/)

## Definující specifikace

- **TS 26.453** (Rel-19) — EVS Codec Generic Frame Format for 3G CS Networks
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks

---

📖 **Anglický originál a plná specifikace:** [WB-SID na 3GPP Explorer](https://3gpp-explorer.com/glossary/wb-sid/)
