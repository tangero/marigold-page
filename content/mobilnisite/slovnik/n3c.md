---
slug: "n3c"
url: "/mobilnisite/slovnik/n3c/"
type: "slovnik"
title: "N3C – Non-3GPP Connection"
date: 2025-01-01
abbr: "N3C"
fullName: "Non-3GPP Connection"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/n3c/"
summary: "Entita protokolové vrstvy v zásobníku uživatelské roviny 5G NR, která spravuje přenos dat přes bezdrátové spoje mimo 3GPP. Adaptuje pakety vyšší vrstvy PDCP pro přenos přes alternativní přístupová méd"
---

N3C je protokolová entita uživatelské roviny v 5G, která adaptuje data pro přenos přes bezdrátové spoje mimo 3GPP (jako Wi-Fi) a umožňuje tak integrovaný provoz s více přístupovými technologiemi.

## Popis

Non-3GPP Connection (N3C) je protokolová podvrstva zavedená v architektuře protokolu uživatelské roviny 5G New Radio (NR), která funguje mezi vrstvami Service Data Adaptation Protocol (SDAP)/Packet Data Convergence Protocol (PDCP) a podléhající spojovou vrstvu přístupové technologie mimo 3GPP. Funguje jako adaptační vrstva, která umožňuje horním vrstvám zásobníku 5G radiového protokolu (konkrétně PDCP) pracovat nezávisle na vlastnostech spodní vrstvy rádiového spoje mimo 3GPP. Entita N3C je umístěna jak v uživatelském zařízení (UE), tak na straně sítě (např. v gNB-CU nebo v dedikovaném uzlu podporujícím více přístupových technologií). Jejím hlavním úkolem je mapovat PDCP Protocol Data Units (PDU) na služební datové jednotky spojové vrstvy spoje mimo 3GPP a řešit aspekty jako segmentaci, opětovné sestavení a doručování v pořadí, pokud tento spoj tyto služby nativně neposkytuje.

Z architektonického hlediska je N3C součástí širšího rámce Multi-Radio Dual Connectivity ([MR-DC](/mobilnisite/slovnik/mr-dc/)) a Access Traffic Steering, Switching, and Splitting ([ATSSS](/mobilnisite/slovnik/atsss/)). Když je UE konfigurováno s připojením mimo 3GPP jako sekundární skupinou buněk nebo cestou pro rozdělování provozu, gNB používá vrstvu N3C ke správě toku dat přes tento spoj. Vrstva N3C může k PDCP PDU přidat vlastní hlavičku obsahující pořadová čísla a indikátory délky potřebné pro adaptační funkci. To umožňuje vrstvě PDCP zachovat své klíčové funkce – jako je šifrování, ochrana integrity a detekce duplicit – konzistentně, ať už podléhajícím fyzickým přenosem je 5G NR, LTE nebo technologie mimo 3GPP. Specifikace (např. TS 38.322, 38.323) definují přesné postupy pro zřízení, rekonfiguraci a uvolnění N3C, stejně jako jeho interakce s řídicí vrstvou [RRC](/mobilnisite/slovnik/rrc/).

Z provozní perspektivy vrstva N3C abstrahuje specifika spoje mimo 3GPP a prezentuje vrstvě PDCP spolehlivější a uspořádaný datový kanál. To je zásadní pro zachování očekávání koncové kvality služby (QoS) a spolehlivosti služeb 5G při použití heterogenního přístupu. Například, pokud je spoj mimo 3GPP satelitní připojení s vysokou latencí, mechanizmy vyrovnávací paměti a řazení vrstvy N3C pomáhají zmírnit dopad na celkový tok dat. Standardizací této adaptační vrstvy umožňuje 3GPP začlenění široké škály radiových technologií mimo 3GPP do rámce 5G RAN čistým, modulárním způsobem, aniž by bylo nutné měnit základní protokol PDCP pro každý nový typ přístupu.

## K čemu slouží

N3C byl vyvinut, aby řešil rostoucí potřebu hluboké integrace přístupových technologií mimo 3GPP na vrstvě 2 ([L2](/mobilnisite/slovnik/l2/)) do 5G RAN, která jde nad rámec integrace v jádře sítě poskytované [N3AN](/mobilnisite/slovnik/n3an/). Předchozí přístupy, jako je LTE-WLAN Aggregation ([LWA](/mobilnisite/slovnik/lwa/)), vyžadovaly specifickou adaptaci a byly omezeného rozsahu. Vize 5G o skutečně integrovaném provozu s více přístupovými technologiemi, zejména pro [ATSSS](/mobilnisite/slovnik/atsss/), si vyžádala obecnější a flexibilnější řešení, které by mohlo pracovat s různými spoji mimo 3GPP (např. Wi-Fi 6/7, satelit, privátní sítě), jako by šlo z pohledu vyšších vrstev o nativní rádiové spoje 3GPP.

Jeho účelem je řešit technický problém nekompatibility protokolových zásobníků. Technologie mimo 3GPP mají své vlastní vrstvy [MAC](/mobilnisite/slovnik/mac/) a PHY s odlišnými charakteristikami (velikosti rámců, mechanizmy spolehlivosti, absence doručování v pořadí). N3C poskytuje potřebnou 'vazbu', která umožňuje vrstvě 5G NR PDCP, navržené pro 3GPP MAC/PHY, aby správně fungovala přes tyto odlišné spoje. To umožňuje hladkou implementaci pokročilých funkcí RAN, jako je duplikace paketů pro ultra-spolehlivost nebo inteligentní rozdělování provozu přes cesty 3GPP i mimo 3GPP. Vytvoření N3C je motivováno snahou o konvergenci sítí na rádiové úrovni, která operátorům umožňuje budovat robustnější, vysokokapacitní a efektivnější radiové sítě tím, že využívají nejlepší charakteristiky všech dostupných bezdrátových technologií těsně koordinovaným způsobem.

## Klíčové vlastnosti

- Adaptační protokolová vrstva mezi PDCP a spojovými vrstvami technologií mimo 3GPP
- Umožňuje PDCP fungovat přes heterogenní rádiové spoje mimo 3GPP
- Podporuje adaptaci segmentace/opětovného sestavení a doručování v pořadí
- Integruje se s rámci MR-DC a ATSSS pro provoz s více přístupovými technologiemi
- Spravována signalizací RRC pro zřízení a konfiguraci
- Umožňuje integraci na rádiové úrovni pro funkce jako duplikace paketů

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [N3C na 3GPP Explorer](https://3gpp-explorer.com/glossary/n3c/)
