---
slug: "iff"
url: "/mobilnisite/slovnik/iff/"
type: "slovnik"
title: "IFF – Indirect Far Field"
date: 2025-01-01
abbr: "IFF"
fullName: "Indirect Far Field"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/iff/"
summary: "Měřicí technika pro Over-the-Air (OTA) testování velkých anténních polí, zejména pro 5G NR. Syntetizuje vyzařovací charakteristiky vzdáleného pole z měření v blízkém poli v kompaktní bezodrazové komoř"
---

IFF (nepřímé vzdálené pole) je měřicí technika, která syntetizuje vyzařovací charakteristiky vzdáleného pole z měření v blízkém poli v kompaktní komoře pro OTA testování velkých anténních polí, jaká se používají v 5G NR.

## Popis

Indirect Far Field (IFF, nepřímé vzdálené pole) je pokročilá metodologie Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)) testování standardizovaná v 3GPP pro hodnocení rádiového výkonu zařízení vybavených velkými anténními poli, jako je 5G New Radio (NR) User Equipment (UE) a základnové stanice (gNB). Na rozdíl od tradičního testování ve vzdáleném poli, které vyžaduje umístění testovací antény ve značné vzdálenosti (často několik metrů) od testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)), aby byla splněna podmínka Fraunhoferovy vzdálenosti pro vzdálené pole, IFF techniky syntetizují odezvu vzdáleného pole nepřímo. Toho je dosaženo provedením měření v oblasti zářícího blízkého pole DUT a následnou aplikací sofistikovaných matematických transformací, primárně založených na sférické vlnové expanzi nebo algoritmech transformace z rovinného blízkého pole na vzdálené pole, pro výpočet ekvivalentní vyzařovací charakteristiky vzdáleného pole.

Architektura IFF testovacího uspořádání typicky zahrnuje kompaktní bezodrazovou komoru vybavenou přesným robotickým pozicionérem pro měřicí sondu (jedinou anténu nebo malé pole) a DUT umístěné na rotačním stupni. Sonda skenuje plochu (sférickou, válcovou nebo rovinnou) v oblasti blízkého pole a zachycuje amplitudu i fázi vyzařovaného elektromagnetického pole. Tato zachycená data blízkého pole představují komplexní prostorový vzorek vyzařovaného pole DUT. Specializovaný postprocesní software následně aplikuje transformační algoritmy. Tyto algoritmy rozloží změřené pole blízkého pole na sadu koeficientů sférických vln, které jednoznačně reprezentují vyzařované pole. Z těchto koeficientů lze přesně vypočítat kompletní vyzařovací charakteristiku vzdáleného pole – včetně zisku, směrovosti, šířky svazku a úrovní bočních laloků – pro jakýkoli směr.

Jak to funguje, závisí na principu, že jakékoli vyzařované pole v oblasti bez zdrojů může být reprezentováno jako superpozice ortogonálních sférických vlnových funkcí. Vzorkováním pole na uzavřené ploše obklopující DUT lze tyto vlnové koeficienty vyřešit. Klíčovými komponentami jsou bezodrazová komora (pro eliminaci odrazů), přesný skenovací systém, vektorový síťový analyzátor pro [RF](/mobilnisite/slovnik/rf/) měření a transformační software. Jeho role v 5G a dalších generacích je zásadní, protože tyto systémy spoléhají na beamforming s anténními poli, která mohou mít desítky nebo stovky prvků. Přímé testování vzdáleného pole takových polí by vyžadovalo komory nepraktických rozměrů. IFF umožňuje přesnou charakterizaci kritických metrik, jako je Effective Isotropic Radiated Power ([EIRP](/mobilnisite/slovnik/eirp/)), Total Radiated Power ([TRP](/mobilnisite/slovnik/trp/)) a přesnost natočení svazku, ve standardním laboratorním prostředí, což je nezbytné pro validaci výkonu Massive [MIMO](/mobilnisite/slovnik/mimo/) a zajištění spolehlivého provozu sítě.

## K čemu slouží

IFF bylo vytvořeno, aby řešilo významné fyzikální a praktické výzvy zavedené Massive [MIMO](/mobilnisite/slovnik/mimo/) a pokročilými anténními systémy ([AAS](/mobilnisite/slovnik/aas/)) v 5G NR. Tradiční přímé OTA testování vzdáleného pole vyžaduje, aby testovací vzdálenost byla větší než 2D²/λ (kde D je největší rozměr antény a λ je vlnová délka). Pro velká pole na milimetrových vlnách může tato vzdálenost činit desítky metrů, což je neproveditelné pro stavbu a údržbu odpovídajících bezodrazových komor. Toto omezení hrozilo zastavením vývoje a certifikace 5G zařízení, protože jejich beamformingový výkon nemohl být adekvátně validován v laboratoři.

Historický kontext představuje přechod od 4G LTE, kde zařízení typicky měla 2-4 antény, k 5G, kde základnové stanice a špičková UE integrují anténní pole s 64, 128 nebo více prvky. Potřeba testovat komplexní trojrozměrné charakteristiky svazků, přepínání svazků a sledování svazků si vyžádala novou metodologii. IFF to řeší využitím dobře zavedené teorie měření v blízkém poli z anténního inženýrství a jejím přizpůsobením specifickým požadavkům testování integrovaných telekomunikačních zařízení, kde anténa není samostatnou součástkou, ale součástí uzavřeného zařízení s aktivní elektronikou.

Řeší klíčový problém umožnění přesného, opakovatelného a standardizovaného testování výkonu integrovaných AAS v kompaktním zařízení. Bez IFF by charakterizace beamformingového zisku, prostorové konzistence a potlačení interference byla během fáze vývoje a certifikace nespolehlivá nebo nemožná. Jeho vytvoření bylo motivováno průmyslovým konsenzem v rámci 3GPP RAN Working Group 4 (RAN4), která řídí testování rádiového výkonu a protokolů, s cílem definovat budoucím potřebám vyhovující testovací metodu, která se škáluje s velikostí antény a frekvencí, a zajišťuje, aby síťové výkonnostní sliby 5G – vysoké datové rychlosti, kapacita a spolehlivost – mohly být empiricky ověřeny před nasazením.

## Klíčové vlastnosti

- Umožňuje měření vyzařovací charakteristiky vzdáleného pole v kompaktních bezodrazových komorách
- Využívá algoritmy transformace ze sférického blízkého pole na vzdálené pole
- Podporuje testování velkých anténních polí a integrovaných aktivních anténních systémů (AAS)
- Kritické pro validaci výkonu beamformingu, EIRP a TRP v 5G NR
- Standardizovaná metodologie pro opakovatelné a srovnatelné výsledky OTA testů
- Aplikovatelné pro testování UE i základnových stanic (gNB)

## Definující specifikace

- **TS 38.771** (Rel-19) — FR2-1 OTA Testing for STxMP UEs
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [IFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/iff/)
