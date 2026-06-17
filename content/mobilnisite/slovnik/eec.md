---
slug: "eec"
url: "/mobilnisite/slovnik/eec/"
type: "slovnik"
title: "EEC – Ethernet Equipment Clock"
date: 2026-01-01
abbr: "EEC"
fullName: "Ethernet Equipment Clock"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eec/"
summary: "Hodinová funkce uvnitř síťového zařízení, která se synchronizuje s časovým vztažným signálem přenášeným po Ethernetové síti, například prostřednictvím IEEE 1588 PTP nebo Synchronous Ethernetu. Je klíč"
---

EEC (Ethernet Equipment Clock) je hodinový zdroj v síťovém zařízení, síťová funkce, která se synchronizuje s časovým vztažným signálem přenášeným po Ethernetu, aby poskytovala přesnou synchronizaci frekvence, fáze a času pro uzly mobilní sítě.

## Popis

Ethernet Equipment Clock (EEC) je logický funkční blok definovaný organizacemi 3GPP a [ITU-T](/mobilnisite/slovnik/itu-t/), který se nachází v síťových prvcích, jako jsou základnové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), směrovače nebo přepínače. Jeho hlavním účelem je získávat, generovat a distribuovat přesné časové informace (frekvenci, fázi a případně i přesný čas), když je zdrojem synchronizační signál založený na Ethernetu. EEC funguje tak, že synchronizuje svůj interní oscilátor s příchozím časovým vztažným signálem, který je typicky dodáván dvěma hlavními metodami: Synchronous Ethernet (SyncE) pro synchronizaci frekvence nebo [IEEE](/mobilnisite/slovnik/ieee/) 1588 Precision Time Protocol (PTP) pro synchronizaci fáze a času (často v kombinaci se SyncE pro robustní frekvenční podporu).

Z architektonického hlediska se EEC skládá z několika klíčových komponent: jednotky pro získání hodinového signálu, která extrahuje časování z fyzické vrstvy (pro SyncE) nebo z PTP event zpráv, smyčky fázového závěsu (PLL) nebo digitálně řízeného oscilátoru (DCO) pro korekci lokálních hodin a jednotky pro distribuci hodinového signálu, která poskytuje synchronizovaný čas interním podsystémům nebo výstupním portům. V základnové stanici je výstup EEC využíván pro synchronizaci kmitočtu rádiového nosného signálu a, pro Time Division Duplex (TDD) a New Radio (NR), přesného času vysílání a struktury rámců. EEC může pracovat v různých typech hodinových režimech, jak jsou definovány v řadách doporučení ITU-T G.826x a G.827x, například jako obyčejné hodiny (OC), hraniční hodiny ([BC](/mobilnisite/slovnik/bc/)) nebo průchozí hodiny (TC), v závislosti na své roli v synchronizační síti.

Jeho fungování spočívá v nepřetržitém měření a úpravách. Pro PTP funguje EEC jako PTP slave, vyměňuje si časové zprávy s PTP master hodinami pro výpočet časového posunu a zpoždění a podle toho upravuje své lokální hodiny. Pro SyncE získává hodinový signál přímo z fyzického Ethernetového liniového kódu. EEC často implementuje algoritmy pro odfiltrování síťového jitteru a wanderu a může podporovat funkci holdover, při které je schopen po určitou dobu po ztrátě vztažného signálu udržovat stabilní časování pomocí svého kvalitního interního oscilátoru. Jeho role je zásadní v moderních paketových sítích pro přenosovou síť (backhaul) a přístupovou síť (fronthaul) mobilních sítí, kde nahrazuje starší synchronizační zdroje jako [GPS](/mobilnisite/slovnik/gps/) nebo T1/E1 linky, a tím umožňuje nákladově efektivní, škálovatelné a spolehlivé plnění náročných synchronizačních požadavků pro rádiové přístupové sítě 4G a 5G.

## K čemu slouží

Koncept Ethernet Equipment Clock byl vyvinut pro řešení výzvy distribuce vysoce přesné synchronizace po paketových sítích, když operátoři přecházeli od přenosové sítě založené na TDM (využívající SDH/SONET nebo T1/E1 linky s inherentním časováním) k nákladově efektivním, ale asynchronním Ethernetovým a IP sítím. Předchozí mobilní technologie jako [FDD](/mobilnisite/slovnik/fdd/) LTE primárně vyžadovaly synchronizaci frekvence, kterou bylo možné získat s nižší přesností. Nasazení TDD-LTE, pokročilých funkcí LTE-Advanced (např. eICIC, CoMP) a zejména 5G NR s jeho přísnými požadavky na fázové zarovnání pro funkce jako massive [MIMO](/mobilnisite/slovnik/mimo/) a ultra-spolehlivá nízkolatenční komunikace (URLLC) však vytvořilo kritickou potřebu přesné synchronizace fáze a času v každé základnové stanici.

Motivací pro standardizaci EEC bylo zajistit interoperabilitu a konzistentní výkon v sítích s více dodavateli. Bez standardizované hodinové funkce by zařízení každého dodavatele mohlo signály časování založené na Ethernetu interpretovat nebo zpracovávat odlišně, což by vedlo k selhání synchronizace a degradaci výkonu sítě. Specifikace EEC definují požadavky na výkon (toleranci šumu, stabilitu v režimu holdover atd.) a funkční chování, což operátorům umožňuje budovat spolehlivé sítě pro distribuci synchronizace využívající [IEEE](/mobilnisite/slovnik/ieee/) 1588 PTP a SyncE. Tím je řešen základní problém, jak distribuovat přesné, sledovatelné časování z centrálního zdroje (jako jsou Grandmaster hodiny) potenciálně složitou paketovou sítí k stovkám či tisícům rádiových lokalit, což je nezbytné pro funkčnost sítě, spektrální efektivitu a prevenci interference v hustých nasazeních.

## Klíčové vlastnosti

- Podporuje synchronizaci prostřednictvím IEEE 1588 PTP (pro fázi/čas) a Synchronous Ethernetu (SyncE, pro frekvenci)
- Definované typy hodin: Obyčejné hodiny (OC), Hraniční hodiny (BC) a Průchozí hodiny (TC)
- Implementuje funkce získání hodinového signálu, filtrace a režimu holdover
- Poskytuje časový výstup pro frekvenci rádiového rozhraní a zarovnání rámců
- Splňuje výkonnostní profily dle ITU-T G.826x a G.827x pro telekomunikační aplikace
- Umožňuje distribuci přesného časování po paketových sítích pro přístupovou (fronthaul) a přenosovou (backhaul) síť

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [EEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/eec/)
