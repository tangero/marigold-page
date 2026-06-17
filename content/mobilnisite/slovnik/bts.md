---
slug: "bts"
url: "/mobilnisite/slovnik/bts/"
type: "slovnik"
title: "BTS – Base Transceiver Station"
date: 2025-01-01
abbr: "BTS"
fullName: "Base Transceiver Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bts/"
summary: "BTS je rádiové zařízení, které v sítích 2G (GSM) a 3G (UMTS) komunikuje přímo s mobilními zařízeními. Zajišťuje vysílání a příjem rádiových signálů a jejich základní zpracování a tvoří fyzickou lokali"
---

BTS je rádiové zařízení v sítích 2G a 3G, které komunikuje přímo s mobilními zařízeními, zajišťuje vysílání, příjem a základní zpracování a tvoří fyzickou lokalitu buňky.

## Popis

Základnová přenosová stanice (BTS) je klíčový síťový prvek v GSM a UMTS rádiové přístupové síti (RAN). Skládá se z rádiových transceiverů, antén a jednotek pro zpracování signálu potřebných k navázání rozhraní s uživatelským zařízením (UE). Fyzicky lokalita BTS zahrnuje anténní stožár nebo sloup, přístřešek nebo skříň s rádiovým vybavením, ve které jsou umístěny jednotky transceiverů, kombinátory, duplexery, zesilovače a napájecí systémy. V typické architektuře GSM je více jednotek BTS řízeno a spravováno řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), čímž tvoří subsystém známý jako subsystém základnových stanic ([BSS](/mobilnisite/slovnik/bss/)). BTS je zodpovědná za funkce nižších vrstev rozhraní [E-UTRA](/mobilnisite/slovnik/e-utra/)/NR, konkrétně fyzické vrstvy (vrstva 1) a částí vrstvy spojení dat (vrstva 2).

Provozně BTS provádí modulaci a demodulaci rádiových signálů. Převádí digitální datový tok z jádra sítě (přes BSC a převodní jednotku) na analogové rádiové frekvenční signály pro vysílání vzduchem a naopak pro příjem. Mezi klíčové rádiové funkce patří kanálové kódování a prokládání pro opravu chyb, šifrování pro zabezpečení přenosu vzduchem, modulace (např. [GMSK](/mobilnisite/slovnik/gmsk/) pro GSM, QPSK/[16QAM](/mobilnisite/slovnik/16qam/) pro UMTS) a regulace výkonu pro řízení síly signálu a interference. BTS také v GSM zajišťuje výpočty časového předstihu pro synchronizaci vysílání z mobilních zařízení na různých vzdálenostech, což je klíčová funkce pro provoz s vícenásobným přístupem s časovým dělením (TDMA).

Z pohledu sítě BTS vymezuje oblast pokrytí buňky. Každá BTS může podporovat více buněk (sektorů) pomocí směrových antén. Spravuje rádiové zdroje pro svou buňku (buňky), včetně přidělování kanálů pro přenos (TCH) a řídicích kanálů (např. Broadcast Control Channel - [BCCH](/mobilnisite/slovnik/bcch/), Common Control Channel - [CCCH](/mobilnisite/slovnik/ccch/)). BTS provádí měření kvality a síly signálu v uplinku od UE a hlásí je BSC, aby pomohla při rozhodování o předání hovoru a algoritmech regulace výkonu. Její role je především výkonná, řídí se příkazy z BSC pro přiřazení kanálu, provedení předání hovoru a správu rádiových zdrojů. Rozhraní mezi BTS a BSC je standardizováno, nejvýznamněji rozhraní Abis v GSM.

## K čemu slouží

BTS byla vytvořena jako základní rádiový uzel pro celulární sítě, konkrétně se standardizací GSM na konci 80. a začátku 90. let 20. století. Jejím účelem bylo poskytnout standardizovanou, nasaditelnou jednotku, která by mohla navazovat a udržovat rádiové spojení s mobilními telefony a umožnit tak celoplošnou mobilní hlasovou komunikaci. Před celulárními systémy byly mobilní rádiové služby často omezeny na jednotlivé, vysokoenergetické vysílače pokrývající velké oblasti s velmi omezenou kapacitou. Celulární koncept, umožněný BTS, zavedl opakované využití frekvencí rozdělením geografické oblasti na menší buňky, z nichž každou obsluhovala vlastní BTS s nižším výkonem. To dramaticky zvýšilo kapacitu sítě a spektrální účinnost.

BTS vyřešila problém implementace složitého digitálního rádiového rozhraní vyžadovaného GSM. Zapouzdřila technicky náročné úkoly, jako je digitální modulace, rámování TDMA a zabezpečený přenos, do spravovatelného síťového prvku, který mohl být hromadně vyráběn a nasazován. Oddělila čistě rádiové funkce (zajišťované BTS) od síťové řídicí a přepojovací inteligence (zajišťované [BSC](/mobilnisite/slovnik/bsc/) a mobilní ústřednou). Tato modulární architektura umožnila škálovatelné zavádění sítě a efektivnější údržbu a aktualizace. Standardizovaný návrh BTS zajistil interoperabilitu mezi zařízeními od různých výrobců, což byl klíčový faktor pro rychlé celosvětové přijetí technologie GSM.

Při vývoji směrem k 3G UMTS byl koncept BTS přizpůsoben (často označován jako Node B) pro podporu technologie širokopásmového kódového dělení kanálů (WCDMA). Zatímco se základní rádiová technologie změnila z TDMA na CDMA, základní účel zůstal stejný: sloužit jako bod sítě pro rádiové vysílání a příjem. BTS/Node B umožnila přechod na vyšší datové rychlosti a služby s přepojováním paketů při zachování zpětné kompatibility a známé architektonické role v rámci RAN, což operátorům zajistilo hladkou technologickou migraci.

## Klíčové vlastnosti

- Moduluje a demoduluje rádiové signály pro rozhraní Uu
- Spravuje zpracování fyzické vrstvy (vrstva 1) včetně kanálového kódování a prokládání
- Provádí šifrování a dešifrování pro zabezpečení přenosu vzduchem
- Provádí příkazy regulace výkonu pro optimalizaci síly signálu a minimalizaci interference
- Podporuje více buněk/sektorů pomocí konfigurací se směrovými anténami
- Komunikuje s řadičem základnových stanic (BSC) přes standardizované rozhraní Abis (GSM)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [BTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bts/)
