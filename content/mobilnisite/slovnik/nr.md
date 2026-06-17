---
slug: "nr"
url: "/mobilnisite/slovnik/nr/"
type: "slovnik"
title: "NR – New Radio"
date: 2026-01-01
abbr: "NR"
fullName: "New Radio"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr/"
summary: "New Radio (NR) je globální standard 5G rozhraní pro přenos vzduchem definovaný 3GPP, který zahrnuje technologii rádiového přístupu a síťovou architekturu. Podporuje rozšířenou mobilní širokopásmovou k"
---

NR je globální standard 5G rozhraní pro přenos vzduchem definovaný 3GPP, který podporuje rozšířenou mobilní širokopásmovou komunikaci, ultra-spolehlivou komunikaci s nízkou latencí a hromadnou komunikaci mezi stroji v širokém spektru kmitočtů.

## Popis

New Radio (NR) je komplexní technologie 5G rádiového přístupu standardizovaná 3GPP, která definuje fyzickou vrstvu, protokoly a architekturu pro novou generaci bezdrátových sítí. Její architektura je postavena na flexibilním, službami řízeném rámci, který odděluje funkce řídicí roviny ([CP](/mobilnisite/slovnik/cp/)) a uživatelské roviny (UP), což umožňuje síťové segmentování (network slicing) a cloudová nasazení. Funkce jádra sítě, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), komunikují s Radio Access Network (RAN) přes rozhraní [NG](/mobilnisite/slovnik/ng/), zatímco gNB (Next Generation NodeB) slouží jako základnová stanice spravující rádiové zdroje a konektivitu. NR pracuje jak ve frekvenčním rozsahu 1 (FR1: 410 MHz – 7,125 GHz), tak ve frekvenčním rozsahu 2 (FR2: 24,25 GHz – 52,6 GHz), a podporuje různé scénáře nasazení od širokoplošného pokrytí až po hotspoty s vysokou kapacitou.

Na fyzické vrstvě NR využívá pokročilé technologie, jako je flexibilní numerologie se škálovatelným rozestupem subnosných (15 kHz až 480 kHz), dynamický duplex s časovým dělením (TDD) a masivní [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) s formováním svazku. Rámová struktura je založena na slotech a mini-slotech, což umožňuje přenos s nízkou latencí a efektivní přidělování zdrojů. Klíčové protokolové vrstvy zahrnují Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro správu spojení, Packet Data Convergence Protocol (PDCP) pro zabezpečení a kompresi hlaviček, Radio Link Control (RLC) pro segmentaci a [ARQ](/mobilnisite/slovnik/arq/) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro plánování a multiplexování. Tyto vrstvy spolupracují na podpoře funkcí, jako je agregace nosných, duální konektivita a integrovaný přístup a přenos (IAB).

Úlohou NR v síti je poskytnout jednotné rozhraní pro přenos vzduchem, které splňuje rozmanité požadavky služeb 5G. Umožňuje rozšířenou mobilní širokopásmovou komunikaci (eMBB) prostřednictvím vysokých špičkových přenosových rychlostí (až 20 Gbps pro downlink) a zlepšené spektrální účinnosti. Pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) nabízí funkce jako mini-sloty a uplink bez udělení oprávnění (grant-free) pro dosažení latence pod 1 ms a spolehlivosti 99,9999 %. Pro hromadnou komunikaci mezi stroji (mMTC) podporuje režimy úspory energie a efektivní signalizaci pro obrovský počet zařízení IoT. NR také usnadňuje síťové segmentování (network slicing), což operátorům umožňuje vytvářet virtuální sítě přizpůsobené konkrétním službám, a podporuje mimozemské sítě (NTN) pro globální pokrytí.

## K čemu slouží

NR bylo vytvořeno, aby odstranilo omezení předchozích generací mobilních sítí (2G, 3G, 4G) a vyhovělo exponenciálnímu růstu mobilního datového provozu, různorodým případům užití a přísným požadavkům na výkonnost ve 20. letech 21. století a dále. 4G LTE, ačkoli bylo úspěšné, čelilo výzvám v podpoře velmi vysokých přenosových rychlostí, masivní konektivity IoT a aplikací s kritickými požadavky na nízkou latenci. Motivací pro NR byla potřeba flexibilnějšího, škálovatelnějšího a efektivnějšího rozhraní pro přenos vzduchem, které by dokázalo využít nová kmitočtová pásma včetně milimetrových vln (mmWave) a integrovat pokročilé technologie jako formování svazku a síťové segmentování.

Historicky každá generace přinášela přírůstková vylepšení, ale 5G NR představuje změnu paradigmatu tím, že je navržena od základů pro širokou škálu služeb. Řeší problémy, jako je nedostatek spektra umožněním provozu ve vysokých kmitočtových pásmech, zahlcení sítě prostřednictvím zvýšené kapacity a účinnosti a různorodost služeb pomocí přizpůsobitelných síťových řezů (slices). Vytvoření NR bylo hnací silou globálních standardizačních snah v rámci 3GPP, počínaje Release 15, aby byla zajištěna interoperabilita, podpořena inovace a podpořena digitální transformace napříč odvětvími, jako je automobilový průmysl, zdravotnictví a výroba.

## Klíčové vlastnosti

- Flexibilní numerologie se škálovatelným rozestupem subnosných (15–480 kHz) a délkou slotů
- Masivní MIMO a pokročilé formování svazku pro zlepšenou kapacitu a pokrytí
- Dynamické sdílení spektra (DSS) pro plynulou migraci z LTE na 5G
- Integrovaný přístup a přenos (IAB) pro nákladově efektivní zhušťování sítě
- Podpora ultra-spolehlivé komunikace s nízkou latencí (URLLC) pomocí mini-slotů
- Síťové segmentování (network slicing) umožňující více logických sítí na sdílené fyzické infrastruktuře

## Definující specifikace

- **TR 21.916** (Rel-16) — Rel-16 Description Summary
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.008** (Rel-19) — Organization of Subscriber Data
- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- … a dalších 195 specifikací

---

📖 **Anglický originál a plná specifikace:** [NR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr/)
