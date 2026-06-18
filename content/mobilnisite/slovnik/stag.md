---
slug: "stag"
url: "/mobilnisite/slovnik/stag/"
type: "slovnik"
title: "STAG – Secondary Timing Advance Group"
date: 2025-01-01
abbr: "STAG"
fullName: "Secondary Timing Advance Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/stag/"
summary: "Koncept v LTE a 5G NR pro správu časového předstihu (TA) ve scénářích s agregací nosných. Seskupuje sekundární buňky (SCells), které sdílejí stejnou hodnotu TA, čímž optimalizuje synchronizaci a snižu"
---

STAG je skupina sekundárních buněk v LTE nebo 5G NR s agregací nosných, které sdílejí stejnou hodnotu časového předstihu (timing advance), čímž optimalizují synchronizaci a snižují signalizační režii.

## Popis

Secondary Timing Advance Group (STAG) je koncept definovaný ve specifikacích 3GPP pro LTE a 5G New Radio (NR), používaný primárně v nasazeních s agregací nosných ([CA](/mobilnisite/slovnik/ca/)). Časový předstih ([TA](/mobilnisite/slovnik/ta/)) je mechanismus, který upravuje časování vysílání uživatelského zařízení (UE) pro kompenzaci zpoždění šíření, čímž zajišťuje synchronizaci uplinku na základnové stanici (např. [eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR). Při agregaci nosných, kdy UE agreguje více komponentních nosných ([CC](/mobilnisite/slovnik/cc/)) z potenciálně různých buněk, umožňuje STAG seskupovat sekundární buňky (SCells) na základě jejich požadavků na TA. Každý STAG se skládá z SCells, které mohou sdílet stejnou hodnotu TA, zatímco primární buňka (PCell) má obvykle vlastní skupinu TA (TAG), známou jako primární TAG (pTAG).

Z architektonického hlediska STAG spravuje vrstva Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) v UE a v síti. Při konfiguraci agregace nosných přiřazuje síť SCells konkrétním STAGům prostřednictvím signalizace RRC, například ve zprávě RRCConnectionReconfiguration. UE poté udržuje samostatné TA časovače a hodnoty pro každý STAG na základě příkazů pro časový předstih ([TAC](/mobilnisite/slovnik/tac/)) přijatých v řídicích prvcích Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Toto seskupování je zásadní, protože SCells mohou mít různou geografickou polohu nebo charakteristiky šíření; například SCells z dálkových rádiových hlav mohou vyžadovat odlišné TA ve srovnání s PCell. Jejich seskupením síť snižuje počet potřebných aktualizací TA, protože změny TA jedné SCell lze aplikovat na všechny SCells ve stejném STAGu.

V provozu STAG zvyšuje efektivitu ve scénářích, jako je agregace nosných mezi lokalitami nebo duální konektivita. UE provádí náhodný přístup na PCell, aby stanovilo počáteční TA pro pTAG, a může použít procedury, jako je náhodný přístup bez kolizí na SCells, pro určení TA pro STAGy. Mechanismy vrstvy MAC poté dynamicky upravují hodnoty TA na základě uplinkových přenosů. Mezi klíčové komponenty patří entity MAC a RRC v UE, plánovače eNB/gNB a rozhraní jako Uu (vzdušné rozhraní). Úlohou STAGu je minimalizovat signalizační režii a latenci a zajistit, aby agregované nosné zůstaly synchronizované bez častých překalibrací TA, což je klíčové pro udržení vysokých datových rychlostí a nízké latence v pokročilých rádiových sítích.

STAG také spolupracuje s funkcemi, jako je uplinková CA a více TAGů (až 4 TAGy na UE v pozdějších vydáních), čímž podporuje složitá nasazení. Je specifikován v dokumentech jako 36.331 pro LTE a 38.321 pro NR, s adaptacemi pro flexibilní numerologii NR. Tím, že umožňuje efektivní správu TA, přispívá STAG k celkovému výkonu a spolehlivosti agregace nosných, což je klíčová technologie pro dosažení gigabitových rychlostí v 4G a 5G.

## K čemu slouží

STAG byl zaveden, aby řešil výzvy časové synchronizace při agregaci nosných, které se staly významnými s LTE-Advanced ve vydání 11. Před jeho zavedením agregace nosných předpokládala, že všechny agregované buňky jsou umístěny společně a sdílejí stejný [TA](/mobilnisite/slovnik/ta/), což omezovalo flexibilitu nasazení. V reálných scénářích mohou být SCells geograficky oddělené (např. z různých základnových stanic nebo dálkových rádiových hlav), což způsobuje různá zpoždění šíření. Bez STAGu by každá SCell vyžadovala individuální správu TA, což by vedlo k nadměrné signalizaci a potenciálním chybám synchronizace, zhoršovalo by výkon uplinku a zvyšovalo spotřebu energie UE.

Historicky, když operátoři nasazovali heterogenní sítě (HetNety) a chtěli agregovat spektrum z nesousedních lokalit, objevila se potřeba více skupin TA. STAG to vyřešil tím, že umožnil seskupit SCells s podobnými charakteristikami šíření, čímž se snížil počet hodnot TA, které musí UE udržovat. To bylo motivováno snahou o vyšší datové rychlosti a efektivní využití spektra v LTE a později v 5G NR. Řeší omezení dřívějších implementací CA, které byly navrženy primárně pro agregaci v rámci jedné lokality, rozšířením podpory na scénáře mezi lokalitami a dokonce mezi různými kmitočty.

Navíc STAG umožňuje pokročilé funkce, jako je duální konektivita (DC) a vylepšená CA, kde jsou časové rozdíly výraznější. Optimalizací správy TA zlepšuje pokrytí a kapacitu uplinku, což je zásadní pro aplikace jako streamování videa a IoT. Jeho vytvoření odráží vývoj směrem k dynamičtějším a flexibilnějším architekturám RAN, kde síťové segmenty a multikonektivita vyžadují robustní synchronizační mechanismy. STAG tedy hraje klíčovou roli v zajištění, aby agregace nosných poskytovala své slibované výhody napříč různými topologiemi nasazení.

## Klíčové vlastnosti

- Seskupuje sekundární buňky (SCells) se sdílenými hodnotami časového předstihu
- Snižuje signalizační režii v nasazeních s agregací nosných
- Spravován prostřednictvím signalizace RRC a řídicích prvků MAC
- Podporuje více TAGů na jedno UE (např. pTAG a sTAGy)
- Umožňuje efektivní aktualizace TA pro buňky, které nejsou umístěny společně
- Integruje se s frameworky agregace nosných pro LTE a NR

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [STAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/stag/)
