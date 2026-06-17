---
slug: "haps"
url: "/mobilnisite/slovnik/haps/"
type: "slovnik"
title: "HAPS – High Altitude Platform Station"
date: 2025-01-01
abbr: "HAPS"
fullName: "High Altitude Platform Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/haps/"
summary: "High Altitude Platform Station (HAPS) je kvazistacionární letecká platforma, například balón nebo dron, operující ve stratosféře za účelem poskytování pokrytí bezdrátovou komunikací. Funguje jako zákl"
---

HAPS (High Altitude Platform Station) je kvazistacionární letecká platforma, například balón nebo dron, operující ve stratosféře, která slouží jako základnová stanice nebo přenosový uzel pro bezdrátovou komunikaci a rozšiřuje síťové pokrytí do odlehlých oblastí.

## Popis

High Altitude Platform Station (HAPS) je síťový uzel umístěný ve stratosféře, typicky v nadmořských výškách mezi 17 km a 22 km, který poskytuje služby bezdrátové komunikace. Funguje jako letecká základnová stanice nebo přenosový uzel, vybavená zařízením přístupové sítě (RAN) pro obsluhu uživatelských zařízení (UE) na zemi. Platformy HAPS zahrnují bezpilotní letouny (UAV), balóny nebo vzducholodě, navržené pro dlouhodobé lety s využitím solární energie a schopností udržování pozice. Ve specifikacích 3GPP je HAPS integrována do architektury RAN jako doplněk k pozemním sítím, nabízející přímou viditelnost ([LOS](/mobilnisite/slovnik/los/)) pokrytí přes rozsáhlé oblasti (až do poloměru 100 km) a umožňující konektivitu v náročném prostředí.

Architektura HAPS zahrnuje samotnou platformu, pozemní řídicí stanici pro navigaci a správu a přenosový spoj (backhaul) k jádru sítě. Platforma hostí gNodeB (pro 5G NR) nebo eNodeB (pro LTE), které vysílají a přijímají signály ve vyhrazených frekvenčních pásmech, jako je sub-6 GHz nebo milimetrové vlny. HAPS se připojuje k UE prostřednictvím přístupového spoje a k pozemním bránám prostřednictvím přenosového spoje (backhaul), který může využívat mikrovlnné, optické nebo satelitní spojení. Klíčové součásti zahrnují fázované anténní soustavy pro beamforming, energetické systémy pro dlouhodobý provoz a palubní zpracování pro manipulaci se signály. Specifikace 3GPP definují kanálové modely, požadavky na výkon a integrační protokoly, aby bylo zajištěno bezproblémové fungování HAPS s existujícími sítěmi.

HAPS funguje tak, že udržuje kvazistacionární pozici ve stratosféře, kde může pokrýt širokou geografickou oblast s minimálním stíněním ve srovnání s drony v nízkých výškách. Používá techniky beamformingu k dynamickému směrování signálů, přizpůsobujíc se pohybu platformy a rozmístění uživatelů. Přístupový spoj dodržuje standardní protokoly 3GPP rozhraní pro přenos vzduchem (např. NR), s úpravami pro delší šířicí zpoždění a Dopplerovy jevy způsobené výškou. HAPS může být nasazena jako samostatná síť pro zásahy při mimořádných událostech nebo integrována s pozemními sítěmi pro odlehčení provozu, zvýšení kapacity nebo vyplnění mezer v pokrytí. Její role sahá až k podpoře zařízení internetu věcí (IoT), širokopásmového přístupu a síťového segmentování (network slicing) pro specializované služby, čímž využívá svou flexibilní nasaditelnost a škálovatelnost.

## K čemu slouží

HAPS byla zavedena v rámci 3GPP k řešení problémů s pokrytím a kapacitou v bezdrátových sítích, zejména pro nedostatečně pokryté oblasti, jako jsou odlehlé regiony, oceány nebo oblasti postižené katastrofami, kde je pozemní infrastruktura nepraktická nebo poškozená. Tradiční základnové stanice mají v takovém prostředí omezený dosah a vysoké náklady na nasazení, což vede k mezerám v konektivitě. HAPS poskytuje nákladově efektivní alternativu tím, že nabízí širokoplošné pokrytí ze stratosféry, překlenuje digitální propast a zajišťuje všeobecnou dostupnost služeb.

Vytvoření HAPS je motivováno potřebou rychlého nasazení a škálovatelnosti v sítích 5G a novějších. Řeší problémy, jako je zahlcení sítě v městských oblastech odlehčením provozu, a podporuje dočasné události nebo vojenské operace poskytováním konektivity na vyžádání. Historicky satelitní systémy nabízely široké pokrytí, ale s vysokou latencí a náklady; HAPS zaplňuje mezeru mezi nimi a poskytuje služby s nízkou latencí, podobné buněčným sítím, s jednodušším nasazením než satelity. To je v souladu s vizí 3GPP pro neterestrické sítě (NTN) pro bezproblémové globální pokrytí.

Omezení předchozích přístupů zahrnují nepružnost pevné infrastruktury a vysokou latenci geostacionárních satelitů. HAPS je řeší tím, že umožňuje agilní, rekonfigurovatelné sítě, které lze podle potřeby přemístit. Zvyšuje také odolnost, poskytuje zálohu při výpadcích sítě nebo přírodních katastrofách. Integrace do standardů 3GPP zajišťuje interoperabilitu s existujícími zařízeními a sítěmi, podporuje inovace v letecké konektivitě a umožňuje nové případy užití, jako jsou autonomní vozidla a chytré zemědělství.

## Klíčové vlastnosti

- Provoz ve stratosféře (ve výšce 17–22 km) pro širokoplošné pokrytí až do poloměru 100 km
- Podpora rozhraní 3GPP pro přenos vzduchem (LTE a 5G NR) jako letecká základnová stanice nebo přenosový uzel
- Využití beamformingu a pokročilých antén pro efektivní směrování signálu a správu kapacity
- Integrace s pozemními sítěmi prostřednictvím přenosových spojů (backhaul) (mikrovlnné, optické nebo satelitní)
- Kvazistacionární nasazení se schopnostmi udržování pozice pro dlouhodobý provoz služeb
- Umožňuje rychlé nasazení pro nouzovou komunikaci, pokrytí venkovských oblastí a odlehčení provozu

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TR 38.882** (Rel-18) — Technical Report on UE Location Service

---

📖 **Anglický originál a plná specifikace:** [HAPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/haps/)
