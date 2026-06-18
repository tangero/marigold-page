---
slug: "vsrb"
url: "/mobilnisite/slovnik/vsrb/"
type: "slovnik"
title: "VSRB – Variable Sized Radio Block"
date: 2025-01-01
abbr: "VSRB"
fullName: "Variable Sized Radio Block"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vsrb/"
summary: "Struktura rádiového bloku v sítích GSM/EDGE, která umožňuje variabilní velikost přenosové jednotky na základě datových požadavků. Optimalizuje efektivitu využití spektra přizpůsobením velikosti bloku"
---

VSRB je struktura rádiového bloku v sítích GSM/EDGE, kde se velikost přenosové jednotky mění za účelem optimalizace efektivity spektra přizpůsobením se datovým požadavkům a stavu kanálu, čímž se snižuje režie.

## Popis

Variable Sized Radio Block (VSRB) je základní přenosová jednotka v rámci GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), definovaná pro zvýšení efektivity přenosu dat. Na rozdíl od rádiových bloků s pevnou velikostí není velikost datové části (payload) VSRB konstantní, ale může být dynamicky upravována. Tuto variabilitu spravuje síť na základě faktorů, jako je množství uživatelských dat k odeslání, aktuální kvalita kanálu a zvolený modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)). Blok se skládá z hlavičky obsahující řídicí informace (např. typ bloku a indikátor velikosti) a datové části. Přizpůsobení velikosti provádí vrstva Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), která segmentuje nebo spojuje datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) vyšších vrstev, aby odpovídaly zvolené velikosti rádiového bloku před přenosem přes fyzickou vrstvu.

Z architektonického hlediska je provoz VSRB integrován do struktury paketového datového kanálu ([PDCH](/mobilnisite/slovnik/pdch/)) GERAN. Síťový plánovač, který se typicky nachází v Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) pro GSM/EDGE, určuje vhodnou velikost bloku pro daný přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)). Toto rozhodnutí bere v úvahu stav vyrovnávací paměti řízení rádiového spoje (RLC), hlášení o kvalitě kanálu od mobilní stanice a dostupné rádiové zdroje. Zvolená velikost je pak signalizována mobilní stanici prostřednictvím řídicích zpráv, což zajišťuje, že oba konce spoje používají stejný formát pro úspěšné dekódování. Toto dynamické nastavování velikosti snižuje potřebu odsazení (padding) pomocí prázdných bitů, když je datový paket menší než pevný blok, čímž šetří rádiové zdroje a snižuje latenci pro malé datové přenosy.

VSRB hraje klíčovou roli v optimalizaci propustnosti a latence u Enhanced Data rates for GSM Evolution (EDGE) a pozdějších funkcí GERAN. Tím, že přenosová jednotka lépe odpovídá skutečné datové poptávce, zlepšuje spektrální účinnost rozhraní vzduch. To je zvláště důležité pro scénáře se smíšeným provozem, které podporují jak pakety voice-over-IP (VoIP), které jsou typicky malé a citlivé na zpoždění, tak větší datové pakety pro prohlížení webu. Tato technologie umožňuje efektivnější využití časových slotů a podporuje pokročilé funkce, jako je snížená latence a operace s dvojitým nosičem, což přispívá k vývoji sítí GSM směrem k vyšším datovým rychlostem a lepší podpoře paketově spínaných služeb.

## K čemu slouží

VSRB byl zaveden, aby řešil neefektivitu vlastní přenosům s pevnou velikostí rádiového bloku používaným v raných datových službách GSM, jako je GPRS. Pevné bloky často vyžadovaly významné odsazení (padding), když uživatelská data nezaplnila celou kapacitu bloku, což plýtvalo cenným rádiovým spektrem a zvyšovalo přenosové zpoždění. S růstem využívání mobilních dat se optimalizace spektrální účinnosti stala prvořadou pro podporu vyšších datových rychlostí a většího počtu uživatelů v rámci omezené šířky pásma. VSRB poskytl mechanismus pro přizpůsobení základní přenosové jednotky skutečným potřebám, což je koncept klíčový pro zlepšení výkonu sítí EDGE.

Vytvoření VSRB bylo motivováno potřebou vylepšit GSM/EDGE, aby zůstalo konkurenceschopné vůči vznikajícím technologiím 3G, a nabídnout tak lepší podporu paketově spínaných aplikací. Řešilo problém neefektivního využívání zdrojů pro přerušovaný (bursty) internetový provoz s proměnnou rychlostí. Umožněním dynamického nastavování velikosti bloku mohly sítě snížit režii, snížit latenci pro interaktivní služby a zvýšit celkovou kapacitu systému. Tato evoluce byla součástí širšího úsilí v rámci 3GPP o neustálé zlepšování schopností GERAN, což zajišťovalo zpětnou kompatibilitu a zároveň zavádělo funkce, které učinily sítě GSM vstřícnějšími k datům a efektivnějšími.

## Klíčové vlastnosti

- Dynamické přizpůsobení velikosti datové části na základě objemu dat a podmínek kanálu
- Snížení režie odsazení (padding) pro zlepšení spektrální účinnosti
- Podpora více modulačních a kódovacích schémat (MCS)
- Integrace s plánováním paketového datového kanálu (PDCH) GERAN
- Zlepšení výkonu z hlediska latence pro malé datové pakety
- Zpětná kompatibilita s dědičnými strukturami rádiového bloku GSM/GPRS

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [VSRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/vsrb/)
