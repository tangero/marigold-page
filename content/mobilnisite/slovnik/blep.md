---
slug: "blep"
url: "/mobilnisite/slovnik/blep/"
type: "slovnik"
title: "BLEP – Block Error Probability"
date: 2025-01-01
abbr: "BLEP"
fullName: "Block Error Probability"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/blep/"
summary: "BLEP je základní metrika fyzické vrstvy představující pravděpodobnost, že přenášený datový blok obsahuje po dekódování kanálu neopravitelné chyby. Slouží jako přímá míra kvality rádiového spoje a je k"
---

BLEP je pravděpodobnost, že přenášený datový blok obsahuje po dekódování kanálu neopravitelné chyby, a slouží jako přímá míra kvality rádiového spoje v sítích 3GPP.

## Popis

Pravděpodobnost chyby bloku (BLEP) je kvantitativní metrika výkonu definovaná jako statistická pravděpodobnost, že přenášený transportní blok ([TB](/mobilnisite/slovnik/tb/)) nebo kódový blok ([CB](/mobilnisite/slovnik/cb/)) obsahuje chyby, které nemohou být opraveny dekodérem dopředné korekce chyb ([FEC](/mobilnisite/slovnik/fec/)) přijímače. V systémech 3GPP jsou data organizována do bloků pro přenos přes rádiové rozhraní. Každý blok prochází kanálovým kódováním (jako Turbo kódy ve starších verzích nebo [LDPC](/mobilnisite/slovnik/ldpc/)/Polar kódy v 5G NR), které přidává redundanci a umožňuje detekci a korekci chyb na straně přijímače. Po demodulaci a dekódování přijímač provede na dekódovaném bloku kontrolu cyklickým redundantním součtem ([CRC](/mobilnisite/slovnik/crc/)). Pokud kontrola CRC selže, je blok prohlášen za chybný a přispívá k výpočtu BLEP.

Výpočet BLEP se typicky provádí na dostatečně velkém počtu přenesených bloků, aby bylo dosaženo statisticky spolehlivého odhadu. Vyjadřuje se jako BLEP = Počet chybných bloků / Celkový počet přenesených bloků. Toto měření probíhá na vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro transportní bloky a/nebo na fyzické ([PHY](/mobilnisite/slovnik/phy/)) vrstvě pro kódové bloky. Síť, konkrétně základnová stanice (eNodeB/gNB), využívá odhady BLEP, často odvozené z potvrzení hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)) (ACK/NACK), k vyhodnocení okamžité kvality rádiového spoje k danému uživatelskému zařízení (UE).

Primární úlohou BLEP je vstupovat do klíčových algoritmů správy rádiových zdrojů (RRM). Nejvýznamněji je základní metrikou pro adaptaci spojení (LA). Algoritmus adaptace spojení, typicky běžící na vysílači (základnové stanici), si klade za cíl vybrat nejefektivnější schéma modulace a kódování (MCS) pro nadcházející přenosy. Cílem je maximalizovat propustnost při zachování cílové hodnoty BLEP, která je pro počáteční přenosy v systémech používajících HARQ často kolem 10 %. Pokud je odhadovaná BLEP příliš vysoká, algoritmus zvolí robustnější (nižší) MCS; pokud je nízká, zvolí agresivnější (vyšší) MCS pro zvýšení spektrální účinnosti.

BLEP dále úzce souvisí s mechanismy řízení výkonu. V řízení výkonu v uplinku uživatelské zařízení (UE) upravuje svůj vysílací výkon, aby dosáhlo cílové BLEP (nebo související metriky, jako je poměr signálu k šumu a interferenci, SINR, který s BLEP koreluje), dle pokynů základnové stanice. Slouží také jako klíčový ukazatel výkonu (KPI) pro monitorování systému, jeho optimalizaci a srovnávání. Operátoři sítí a výrobci zařízení používají měření BLEP k vyhodnocení pokrytí, identifikaci problémů s interferencí a ladění síťových parametrů pro optimální výkon a kapacitu.

## K čemu slouží

BLEP existuje jako základní, přímo měřitelný ukazatel úspěšného doručení dat přes inherentně nespolehlivý bezdrátový kanál. Před zavedením sofistikovaných metrik, jako je BLEP, se kvalita rádiového spoje často hodnotila pomocí hrubých fyzikálních měření, jako je indikátor síly přijímaného signálu (RSSI) nebo míra chybovosti bitů (BER). Tyto metriky však přímo neodrážejí výkon skutečných datových bloků po dekódování kanálu, což je pro uživatelský zážitek konečně důležité. BLEP byl zaveden, aby tuto mezeru překlenul, a poskytuje metriku reflektující výsledek přenosového procesu včetně účinků FEC, která je vědoma si vrstvy 2.

Základní problém, který BLEP řeší, je umožnění efektivního a adaptivního využití rádiového spektra. Bezdrátové kanály jsou dynamické, trpí útlumem, interferencí a útlumem dráhy závislým na vzdálenosti. Přenos s pevným, konzervativním MCS by plýtval kapacitou, zatímco použití pevného, agresivního MCS by vedlo k častým selháním. BLEP poskytuje nezbytnou zpětnovazební smyčku pro adaptaci spojení s uzavřenou smyčkou. Průběžným sledováním dosažené BLEP může systém dynamicky upravovat MCS tak, aby odpovídalo aktuálním podmínkám kanálu, a tím maximalizovalo datový tok, který může kanál v daném okamžiku spolehlivě podporovat. Tento adaptivní přístup je základním kamenem efektivity moderních buněčných systémů.

Historicky jeho formální definice a použití v rámci 3GPP, například ve studiích proveditelnosti pro vývoj GSM (dokumentováno v 45.912), pomohlo standardizovat metodiky hodnocení výkonu. Poskytlo společný jazyk pro specifikaci požadavků, porovnávání různých přijímacích algoritmů a návrh systémů, které mohou spolehlivě splňovat cíle kvality služeb (QoS). BLEP zůstává kritickým konceptem, protože přímo spojuje podmínky fyzické vrstvy s výkonem vyšších vrstev a umožňuje inteligentní správu zdrojů, která definuje moderní sítě 3GPP od UMTS přes LTE až po 5G NR.

## Klíčové vlastnosti

- Kvantifikuje pravděpodobnost neopravitelných chyb v přeneseném datovém bloku po dekódování FEC
- Slouží jako primární zpětnovazební metrika pro adaptaci spojení s uzavřenou smyčkou (výběr MCS)
- Koreluje s metrikami výkonu vyšších vrstev, jako je propustnost a latence
- Používá se jako cílový parametr pro algoritmy řízení výkonu v uplinku a downlinku
- Poskytuje standardizovaný KPI pro monitorování výkonu sítě a její optimalizaci
- Základní pro fungování hybridního ARQ (HARQ), kde retransmise mají za cíl snížit efektivní BLEP

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [BLEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/blep/)
