---
slug: "bep"
url: "/mobilnisite/slovnik/bep/"
type: "slovnik"
title: "BEP – Bit Error Probability"
date: 2025-01-01
abbr: "BEP"
fullName: "Bit Error Probability"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bep/"
summary: "Bit Error Probability (BEP) je základní metrika výkonu fyzické vrstvy představující pravděpodobnost, že přenesený bit je přijat chybně. Je to přímé měřítko spolehlivosti rádiového spoje, které kvantif"
---

BEP je základní metrika fyzické vrstvy představující pravděpodobnost, že přenesený bit je přijat chybně, a přímo měří spolehlivost rádiového spoje.

## Popis

Bit Error Probability (BEP) je statistická míra definovaná jako poměr chybně přijatých bitů k celkovému počtu přenesených bitů za dané období nebo pro konkrétní blok dat. Je to klíčový parametr pro hodnocení výkonu digitálních modulačních a kódovacích schémat v přítomnosti zhoršení kanálu, jako je šum, interference a útlum. V systémech 3GPP je BEP typicky odhadován přijímačem (např. uživatelským zařízením nebo základnovou stanicí) porovnáním přijatých měkkých bitů nebo symbolů se známými referenčními signály nebo prostřednictvím výsledků cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) po dekódování kanálu. Proces odhadu zahrnuje měření poměru signálu k interferenci a šumu (SINR) a jeho mapování na předpokládaný BEP na základě charakteristik použité modulace (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)) a rychlosti kódování kanálu.

Z architektonického hlediska se odhad BEP provádí v rámci fyzické vrstvy (vrstva 1) zásobníku rádiového protokolu. Řetězec digitálního zpracování signálu přijímače po synchronizaci, demodulaci a ekvalizaci vytváří logaritmy věrohodnostního poměru (LLR) nebo měkké hodnoty pro každý bit. Tyto měkké hodnoty představují úroveň spolehlivosti každého bitového rozhodnutí. Statistické rozdělení těchto hodnot vzhledem k rozhodovacím prahům se používá k výpočtu okamžitého odhadu BEP. Tento odhad může být v čase filtrován, aby poskytl stabilnější, průměrné měření BEP, které je následně hlášeno vyšším vrstvám, jako je vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) nebo vrstva řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), pro funkce optimalizace sítě.

Úloha BEP v síti je mnohostranná. Slouží jako primární vstup pro algoritmy adaptace spoje s uzavřenou smyčkou, kde síť dynamicky vybírá nejvhodnější modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) pro maximalizaci propustnosti při zachování přijatelné chybovosti. Pokud je hlášený BEP příliš vysoký, což signalizuje špatné podmínky kanálu, může síť přejít na robustnější (nižší) modulaci nebo silnější kód kanálu. Naopak nízký BEP umožňuje použití vyšších modulací pro zvýšení spektrální účinnosti. Měření BEP také vstupují do algoritmů řízení výkonu, pomáhají upravovat vysílací výkon pro dosažení cílové chybovosti, čímž šetří životnost baterie v uživatelských zařízeních a snižují mezibuněčnou interferenci. Dále je BEP klíčovou metrikou pro správu mobility, ovlivňuje rozhodování o předání hovoru tím, že poskytuje detailní pohled na kvalitu spoje na úrovni bitů, a doplňuje tak další měření, jako je Reference Signal Received Power (RSRP).

Ve specifikacích jako 3GPP TS 45.903 (GSM/[EDGE](/mobilnisite/slovnik/edge/)) a TS 45.912 (GSM/EDGE Radio Access Network) je BEP definován pro okruhově i paketově přepínané kanály. Pro Enhanced Data rates for GSM Evolution (EDGE) jsou měření BEP klíčová pro fungování přírůstkové redundance ([IR](/mobilnisite/slovnik/ir/)) a řízení kvality spoje. Přijímač odhaduje BEP na rádiový blok a hlásí jej síti, která tyto informace používá k rozhodnutí, zda data retransmitovat, nebo přizpůsobit kódovací schéma. Přesnost odhadu BEP je tedy prvořadá, protože přímo ovlivňuje vnímanou datovou rychlost uživatele a latenci.

## K čemu slouží

Koncept Bit Error Probability existuje, aby poskytl základní kvantitativní míru kvality digitálního komunikačního spoje. Před sofistikovanými metrikami, jako je BEP, se používala jednodušší měření, jako jsou hrubé počty chybných bitů nebo míry chybovosti rámců, ty však postrádaly pravděpodobnostní a detailní povahu potřebnou pro jemně odstupňované řízení rádiových zdrojů. Hlavní problém, který BEP řeší, je potřeba spolehlivého, okamžitého ukazatele toho, jak dobře si fyzická vrstva vede za konkrétních podmínek kanálu, což je nezbytné pro adaptivní systémy, které musí dynamicky reagovat na časově proměnné rádiové prostředí.

Historicky, jak se buněčné systémy vyvíjely z analogových na digitální (např. GSM), vznikla potřeba inteligentnějších algoritmů pro řízení rádiových zdrojů za účelem zlepšení spektrální účinnosti a uživatelského zážitku. Statická modulace a kódování byly neefektivní; spoj dostatečně dobrý pro robustní schéma plýtval kapacitou, zatímco spoj příliš špatný pro vysokorychlostní schéma trpěl vysokou chybovostí. BEP, jakožto přímý důsledek SINR kanálu a zvolené modulace/kódování, poskytuje nezbytnou zpětnou vazbu pro optimalizaci těchto adaptací. Jeho vznik byl motivován snahou o vyšší datové rychlosti a spolehlivější spojení v omezeném spektru, což umožnilo technologiím jako EDGE posouvat limity sítí 2G.

Dále BEP řeší omezení spočívající v pouhém spoléhání se na měření síly signálu (jako je RSSI). Zatímco síla signálu udává výkon, nezohledňuje interferenci nebo šum, které jsou klíčovými faktory skutečného výkonu na úrovni bitů. BEP inherentně zahrnuje účinky šumu i interference a nabízí tak přesnější obraz o tom, zda jsou bity dekódovány správně. To umožňuje síti rozlišit mezi silným, ale rušeným signálem a čistým, ale slabým signálem, což vede k lepším rozhodnutím při předání hovoru, řízení výkonu a plánování a v konečném důsledku zvyšuje kapacitu sítě a kvalitu služeb.

## Klíčové vlastnosti

- Kvantitativní míra spolehlivosti spoje na úrovni bitů
- Odhadován z měkkých bitových hodnot přijímače nebo výsledků CRC
- Primární vstup pro dynamický výběr modulačního a kódovacího schématu (MCS)
- Klíčová metrika pro algoritmy řízení výkonu s uzavřenou smyčkou
- Používá se při správě mobility a procesech rozhodování o předání hovoru
- Hlášen na rádiový blok nebo měřicí období vyšším vrstvám sítě

## Definující specifikace

- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [BEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bep/)
