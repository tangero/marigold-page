---
slug: "vlan"
url: "/mobilnisite/slovnik/vlan/"
type: "slovnik"
title: "VLAN – Virtual Local Area Network"
date: 2026-01-01
abbr: "VLAN"
fullName: "Virtual Local Area Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vlan/"
summary: "Síťová technologie, která logicky segmentuje fyzickou síť LAN do více vysílacích domén a izoluje provoz z důvodu zabezpečení, správy a výkonu. V rámci 3GPP se VLANy hojně používají v přenosových sítíc"
---

VLAN je síťová technologie, která logicky rozděluje fyzickou síť LAN do více vysílacích domén za účelem izolace provozu; používá se v přenosových sítích 3GPP a datových centrech k oddělení provozu z různých řezů, od různých operátorů nebo služeb.

## Popis

Virtuální lokální síť (VLAN) je základní konstrukce síťové vrstvy 2, která vytváří nezávislé logické sítě v rámci sdílené fyzické síťové infrastruktury. Funguje tak, že do hlavičky ethernetového rámce vloží VLAN tag (definovaný standardem [IEEE](/mobilnisite/slovnik/ieee/) 802.1Q). Tento 4bajtový tag obsahuje 12bitový identifikátor VLAN ([VID](/mobilnisite/slovnik/vid/)) v rozsahu od 1 do 4094, což umožňuje segmentaci jednoho fyzického přepínače nebo sítě na tisíce odlišných vysílacích domén. Rámce patřící do konkrétní VLAN jsou přeposílány pouze na porty nakonfigurované jako členy této VLAN, čímž se efektivně izoluje vysílací, skupinový a neznámý individuální provoz. Toto logické oddělení je vynucováno síťovými přepínači, které udržují přepínací tabulky pro každou VLAN.

V architekturách systémů 3GPP hrají VLANy klíčovou roli při segmentaci přenosové sítě. Používají se k oddělení provozu od různých logických entit přes společnou fyzickou infrastrukturu. Například v rádiové přístupové síti (RAN) mohou VLANy izolovat fronthaul provoz (např. CPRI/eCPRI toky mezi distribuovanou jednotkou ([DU](/mobilnisite/slovnik/du/)) a rádiovou jednotkou ([RU](/mobilnisite/slovnik/ru/))) od backhaul provozu (mezi DU/[CU](/mobilnisite/slovnik/cu/) a jádrem sítě). Také oddělují provoz řídicí roviny, uživatelské roviny a synchronizační roviny, čímž zajišťují kvalitu služeb a zabezpečení. Uvnitř jádra sítě 5G, nasazeného jako virtualizované síťové funkce ([VNF](/mobilnisite/slovnik/vnf/)) v datových centrech, se VLANy používají k vytváření izolovaných sítí pro provoz správy, northbound, southbound a east-west, v souladu s principy cloud-nativního přístupu.

Implementace zahrnuje přepínače a směrovače podporující VLAN na síťových demarkačních bodech. V typické mobilní síti může směrovač na lokalitě buňky používat VLANy k oddělení provozu z více sektorů nebo od různých technologií rádiového přístupu před jeho agregací na sdílený backhaulový spoj. Při síťovém řezání poskytují VLANy (často v kombinaci s jinými technologiemi, jako je [MPLS](/mobilnisite/slovnik/mpls/) nebo SRv6) základní izolaci na vrstvě 2 pro různé instance síťových řezů, čímž zajišťují, že provoz jednoho řezu neovlivňuje provoz jiného. Konfigurace a správa VLAN jsou klíčové pro provoz sítě a jsou často automatizovány prostřednictvím řadičů [SDN](/mobilnisite/slovnik/sdn/) (Software-Defined Networking) jako součást širší správy přenosové sítě definované ve specifikacích 3GPP.

## K čemu slouží

Technologie VLAN byla vytvořena, aby řešila omezení tradičních plochých sítí vrstvy 2, které trpěly velkými vysílacími doménami, bezpečnostními slabinami a neflexibilními omezeními fyzické topologie. Před zavedením VLAN vyžadovala segmentace sítě samostatné fyzické přepínače a kabeláž pro každé oddělení nebo službu, což vedlo k vysokým nákladům a špatnému využití zdrojů. VLANy zavedly logickou segmentaci, která umožnila, aby jeden přepínač obsluhoval více skupin, jako by byly na samostatných fyzických sítích, čímž vyřešily problémy se škálovatelností a správou v podnikových a přenosových sítích.

Přijetí a specifikace použití VLAN v rámci 3GPP bylo hnací silou evoluce směrem k plně IP přenosovým a cloud-nativním sítím. Když se mobilní sítě přesouvaly od vyhrazených spojů TDM/ATM ke sdílenému Ethernetovému/IP přenosu kvůli nákladové efektivitě, byl potřebný mechanismus pro zachování striktního oddělení provozu pro různé služby (např. hlas, data, signalizace) a různé nájemce (např. virtuální mobilní operátory). VLANy poskytly standardizovanou, široce podporovanou metodu, jak této izolace dosáhnout v paketových sítích. S příchodem 5G a síťového řezování se potřeba silné izolace provozu stala prvořadou. VLANy jako osvědčená a spolehlivá technologie tvoří základní vrstvu pro vytváření izolovaných podsítí konektivity vyžadovaných koncovými síťovými řezy, což umožňuje souběžný provoz různorodých služeb s různými požadavky na výkon a zabezpečení na společné fyzické infrastruktuře.

## Klíčové vlastnosti

- Logická segmentace fyzické sítě LAN pomocí tagů IEEE 802.1Q
- Izoluje vysílací domény pro lepší zabezpečení a výkon
- Podporuje až 4094 VLAN ID (VID) na síťovou doménu
- Umožňuje flexibilní návrh skupin nezávislý na topologii
- Klíčová pro oddělení provozu v přenosové síti RAN (fronthaul/backhaul) a v datových centrech
- Základní technologie pro implementaci izolace na přenosové vrstvě při síťovém řezání

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 22.821** (Rel-16) — 5G LAN-type Services Requirements
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.734** (Rel-16) — Enhancements for 5GS in Vertical Domains
- **TS 28.314** (Rel-20) — Management and Orchestration - Plug and Connect
- **TR 28.833** (Rel-18) — Technical Report on 5G LAN-type Service Management
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 32.501** (Rel-19) — Self-Configuration of Network Elements Concepts
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [VLAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/vlan/)
