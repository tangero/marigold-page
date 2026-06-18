---
slug: "bpre"
url: "/mobilnisite/slovnik/bpre/"
type: "slovnik"
title: "BPRE – Bits Per Resource Element"
date: 2025-01-01
abbr: "BPRE"
fullName: "Bits Per Resource Element"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bpre/"
summary: "BPRE je základní metrika fyzické vrstvy v 5G NR, která kvantifikuje počet přenášených informačních bitů na jeden zdrojový prvek (resource element). Je klíčovým parametrem pro výpočet dosažitelné přeno"
---

BPRE je základní metrika fyzické vrstvy 5G NR, která kvantifikuje počet přenášených informačních bitů na jeden zdrojový prvek (resource element) a slouží pro výpočet dosažitelné přenosové rychlosti.

## Popis

Bits Per Resource Element (BPRE, počet bitů na zdrojový prvek) je klíčová metrika definovaná v 3GPP TS 38.213, která představuje spektrální účinnost konkrétního datového přenosu na sdíleném kanálu fyzické downlinkové vrstvy ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo fyzické uplinkové vrstvy ([PUSCH](/mobilnisite/slovnik/pusch/)) 5G New Radio (NR). Není přímo konfigurovatelným parametrem, ale je odvozena z kombinace řádu modulace (Qm) a cílové kódové rychlosti (R). Výpočet je definován jako BPRE = (Qm * R), kde Qm je počet bitů na modulační symbol (např. 2 pro [QPSK](/mobilnisite/slovnik/qpsk/), 4 pro [16QAM](/mobilnisite/slovnik/16qam/), 6 pro [64QAM](/mobilnisite/slovnik/64qam/), 8 pro 256QAM) a R je cílová kódová rychlost poskytnutá v řídicí informaci pro downlink ([DCI](/mobilnisite/slovnik/dci/)). Tato odvozená hodnota představuje průměrný počet informačních bitů přenášených každým přiděleným fyzickým zdrojovým prvkem ([RE](/mobilnisite/slovnik/re/)) datového kanálu.

Role BPRE je ústřední pro proces určení velikosti transportního bloku ([TBS](/mobilnisite/slovnik/tbs/)) pro daný přenos. Plánovač gNodeB na základě hlášení indikátoru kvality kanálu (CQI) od UE vybere index modulačního a kódového schématu (MCS). Tento index MCS odkazuje na záznam v tabulce, který specifikuje jak řád modulace (Qm), tak cílovou kódovou rychlost (R). Z těchto hodnot je následně vypočtena BPRE. Poté je na základě přidělených časově-frekvenčních zdrojů, s ohledem na režijní náklady jako jsou referenční signály pro demodulaci (DM-RS), určen počet dostupných zdrojových prvků (N_RE). Počáteční počet informačních bitů (N_info) je vypočítán jako N_info = N_RE * BPRE. Tato hodnota N_info je pak použita ve vícestupňovém procesu zahrnujícím kvantizaci a vyhledávání v standardizovaných tabulkách TBS definovaných v 38.214, aby bylo konečně dosaženo přesné velikosti transportního bloku, který má být přenesen.

Z architektonického hlediska funguje BPRE jako klíčový spojovací člen mezi rozhodnutími plánování na vyšší vrstvě (výběr MCS) a implementací fyzické vrstvy (určení TBS). Abstrahuje složitý vztah mezi modulací, kódováním a alokací zdrojů do jediné metriky účinnosti. Fyzická vrstva gNodeB používá vypočítanou BPRE a N_RE k instruování vlastního zpracování přenosu a také, prostřednictvím DCI, zpracování příjmu na straně UE, pokud jde o očekávanou velikost datového bloku. Tím je zajištěna synchronizace mezi vysílačem a přijímačem. Výpočet musí zohledňovat konkrétní konfiguraci přenosu, včetně počtu vrstev v MIMO přenosu, protože zdroje se počítají na vrstvu.

BPRE je zásadně spojena s konceptem spektrální účinnosti, která měří, jak efektivně je omezené rádiové spektrum využito k přenosu dat. Vyšší hodnota BPRE znamená, že do každého zdrojového prvku je zabaleno více informačních bitů, čehož je dosaženo použitím modulace vyššího řádu (více bitů na symbol) a/nebo vyšší kódové rychlosti (méně redundance z kanálového kódování). Vyšší BPRE je však náchylnější k chybám při špatných rádiových podmínkách. Proto je adaptivní výběr MCS (a následně BPRE) prostřednictvím adaptace spojení klíčový pro vyvážení datové propustnosti a spolehlivosti přenosu. Síť průběžně upravuje BPRE na základě aktuální kvality kanálu, aby maximalizovala propustnost při zachování přijatelné míry chybovosti bloků (BLER).

## K čemu slouží

BPRE existuje proto, aby poskytla standardizovanou, jednoznačnou metodu pro výpočet velikosti transportního bloku v 5G NR, což je nezbytné pro zajištění, že jak vysílač (gNodeB nebo UE), tak přijímač (UE nebo gNodeB) nezávisle spočítají naprosto stejnou velikost datového bloku. Tato synchronizace je základním požadavkem pro správnou komunikaci. Bez přesně definovaného a vzájemně srozumitelného postupu zahrnujícího BPRE by nesoulad v očekávané velikosti dat vedl k chybám dekódování a katastrofické ztrátě komunikace. Tento koncept řeší problém převodu naplánovaného modulačního a kódového schématu (MCS) a sady časově-frekvenčních zdrojů na konkrétní počet datových bitů, které mají být zakódovány a přeneseny.

Historicky podobné výpočty existovaly v LTE, ale architektura 5G NR zavedla větší flexibilitu a složitější struktury zdrojů, jako jsou podrobnější části šířky pásma (bandwidth parts) a různé numerologie (rozestupy podnosných). Explicitní definice BPRE v rámci specifikací 3GPP poskytuje jasný a konzistentní matematický základ, který tuto flexibilitu akomoduje. Řeší tak omezení ad-hoc nebo implementačně specifických výpočtů a zaručuje interoperabilitu mezi síťovými prvky a uživatelskými zařízeními různých výrobců. Tím, že je odvození TBS založeno na BPRE a standardizovaném vyhledávání v tabulkách, systém zajišťuje deterministické chování a zároveň umožňuje efektivní implementaci.

Motivace pro její vytvoření pramení z potřeby škálovatelného a efektivního návrhu fyzické vrstvy, který podporuje rozmanité případy užití 5G, od rozšířeného mobilního širokopásmového připojení (eMBB) s velmi vysokými datovými rychlostmi až po ultra-spolehlivé komunikace s nízkou latencí (URLLC). Mechanismus určování TBS založený na BPRE je efektivní, protože se vyhýbá potřebě signalizovat velkou hodnotu TBS přímo vzduchem, což by spotřebovalo významnou režii řídicího kanálu. Místo toho jsou signalizovány pouze index MCS a alokace zdrojů a obě strany provedou stejný výpočet zahrnující BPRE. Tento návrh optimalizuje efektivitu řídicí signalizace, což je klíčový aspekt pro udržení nízké režie a podporu masivního připojení v IoT scénářích.

## Klíčové vlastnosti

- Odvozená metrika vypočítaná jako součin řádu modulace (Qm) a cílové kódové rychlosti (R)
- Základní vstup do procedury určování velikosti transportního bloku (TBS) definované v 3GPP TS 38.214
- Přímo představuje spektrální účinnost (bity/s/Hz) naplánovaného přenosu
- Umožňuje synchronizovaný výpočet TBS mezi gNodeB a UE bez explicitní signalizace velikosti bloku
- Dynamicky se přizpůsobuje prostřednictvím adaptace spojení na základě hlášení indikátoru kvality kanálu (CQI)
- Výpočet zohledňuje přidělené zdrojové prvky (RE) a režijní náklady, jako jsou referenční signály

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures

---

📖 **Anglický originál a plná specifikace:** [BPRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bpre/)
