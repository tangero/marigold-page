---
slug: "sonet"
url: "/mobilnisite/slovnik/sonet/"
type: "slovnik"
title: "SONET – Synchronous Optical Networking"
date: 2025-01-01
abbr: "SONET"
fullName: "Synchronous Optical Networking"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sonet/"
summary: "SONET je standardizovaný vysokorychlostní komunikační protokol pro optická vlákna určený k přenosu digitálních signálů. Poskytuje robustní synchronní přenosovou infrastrukturu pro telekomunikační sítě"
---

SONET je standardizovaný vysokorychlostní komunikační protokol pro optická vlákna, který poskytuje robustní synchronní přenosovou infrastrukturu pro telekomunikační sítě.

## Popis

Synchronous Optical Networking (SONET) a jeho mezinárodní protějšek Synchronous Digital Hierarchy ([SDH](/mobilnisite/slovnik/sdh/)) tvoří standardizovanou sadu protokolů pro synchronní přenos více digitálních bitových toků po optickém vlákně pomocí laserů nebo světelných diod (LED). Jeho architektura je založena na synchronní hierarchické struktuře přenosových rychlostí. Základním stavebním blokem je Synchronous Transport Signal level-1 (STS-1), který pracuje na rychlosti 51,84 Mbps. Vyšší rychlosti se vytvářejí bajtovým prokládáním více STS-1 rámců do signálu STS-N (např. STS-3 na 155,52 Mbps, STS-12, STS-48, STS-192). Optickým protějškem signálu STS-N je Optical Carrier level-N (OC-N). Struktura rámce se skládá z transportního režijního signálu (overhead) a synchronní přenosové obálky ([SPE](/mobilnisite/slovnik/spe/)). Režijní signál obsahuje bajty pro vrstvy sekce, linky a cesty a poskytuje klíčové funkce, jako je monitorování výkonnosti (bajty [B1](/mobilnisite/slovnik/b1/)/[B2](/mobilnisite/slovnik/b2/)/B3), kontrolu chyb, datové komunikační kanály ([DCC](/mobilnisite/slovnik/dcc/)) pro [OAM](/mobilnisite/slovnik/oam/)&P a signalizaci pro automatické přepojení ochrany (APS) prostřednictvím bajtů K1/K2.

SONET funguje tak, že synchronizuje všechny síťové prvky s jedním společným primárním referenčním hodinovým signálem, čímž zajišťuje přesné časování v celé síti. To umožňuje snadné multiplexování a demultiplexování nižších přítokových signálů (jako DS1, E1) přímo do vysokorychlostního toku STS-N bez složitého víceúrovňového multiplexování. Mezi klíčové síťové prvky patří Add-Drop Multiplexery ([ADM](/mobilnisite/slovnik/adm/)), které mohou vkládat (add) nebo vyjímat (drop) nízkorychlostní signály z vysokorychlostního toku bez demultiplexování celého signálu; Digitální přepojovací systémy ([DCS](/mobilnisite/slovnik/dcs/)) pro přepojování a usměrňování provozu; a regenerátory pro obnovu tvaru a časování optického signálu na dlouhých vzdálenostech. Protokol poskytuje robustní možnosti správy, provozu, údržby a plánování (OAM&P) díky svému rozsáhlému režijnímu signálu, což umožňuje vzdálené monitorování, izolaci poruch a správu výkonnosti.

V kontextu sítí 3GPP byl SONET/SDH historicky dominantní technologií pro přenosovou síťovou vrstvu, poskytující spolehlivá vysokokapacitní připojení pro přenos mezi radiovými síťovými řadiči (RNC), NodeB, lokalitami jádra sítě (MSC, SGSN) a propojovacími body. Jeho úlohou bylo zajistit transparentní a spolehlivý přenos dat uživatelské roviny (např. rozhraní Iub, Iu, Gn) a signalizace řídicí roviny. Ačkoli byl v moderních nasazeních 4G a 5G z velké části nahrazen přenosem založeným na Ethernetu a IP/MPLS (např. IP RAN, mikrovlnný přenos, Ethernet po vlákně), principy SONET týkající se odolnosti, synchronizace a vrstvené správy OAM ovlivnily pozdější paketové přenosové technologie, jako jsou MPLS-TP a OTN.

## K čemu slouží

SONET byl vyvinut v polovině 80. let 20. století, aby vyřešil kritické problémy interoperability a správy v předvlnových a raných optických telekomunikačních sítích v Severní Americe. Před SONETem nemohly proprietární optické systémy různých dodavatelů vzájemně spolupracovat, což operátory uzamykalo do řešení od jediného dodavatele. Navíc existující asynchronní (plesiochronní) digitální hierarchie (PDH) používala složité víceúrovňové multiplexování, které ztěžovalo a prodražovalo přidávání/odebírání jednotlivých nízkorychlostních kanálů z vysokorychlostního toku, protože vyžadovalo demultiplexování celých systémů. PDH také měla omezené proprietární provozní kanály, což ztěžovalo správu sítě a izolaci poruch.

Vznik SONETu byl motivován potřebou standardizovaného více-dodavatelského optického rozhraní, které by snížilo náklady na zařízení a zvýšilo flexibilitu. Jeho synchronní povaha, umožněná společným hodinovým signálem, zjednodušila multiplexování a umožnila přímý přístup k přítokovým signálům, což revolučně změnilo funkce přepojování a add-drop. Bohatý standardizovaný režijní signál poskytoval výkonné nástroje OAM&P nezávislé na dodavateli, což umožnilo rychlejší zřizování služeb, lepší dostupnost sítě díky automatickému přepojení ochrany (APS) a efektivnější správu poruch. Pro operátory mobilních sítí budující jejich přenosové a páteřní sítě poskytoval SONET spolehlivý, vysokokapacitní a spravovatelný 'přenosový kanál' nutný pro agregaci provozu z tisíců lokalit BTS a propojení prvků jádra sítě, čímž vytvořil spolehlivý základ, na kterém byly doručovány služby 2G (GSM), 3G (UMTS) a raného 4G.

## Klíčové vlastnosti

- Synchronní multiplexování pro přímé přidávání/odebírání přítokových signálů
- Standardizované rychlosti optického rozhraní (OC-1 až OC 192 a vyšší)
- Komplexní režijní signál pro OAM&P, včetně monitorování výkonnosti a datových komunikačních kanálů
- Automatické přepojení ochrany (APS) pro obnovu pod 50 ms (např. 1+1, 1:1)
- Podpora různých klientských signálů (DS1, E1, DS3, E3, Ethernet přes GFP)
- Hierarchická vrstvená architektura (Cesta, Linka, Sekce) pro izolaci poruch

## Související pojmy

- [SDH – Synchronous Digital Hierarchy](/mobilnisite/slovnik/sdh/)

## Definující specifikace

- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways

---

📖 **Anglický originál a plná specifikace:** [SONET na 3GPP Explorer](https://3gpp-explorer.com/glossary/sonet/)
