---
slug: "rrh"
url: "/mobilnisite/slovnik/rrh/"
type: "slovnik"
title: "RRH – Remote Radio Head"
date: 2025-01-01
abbr: "RRH"
fullName: "Remote Radio Head"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rrh/"
summary: "Remote Radio Head (RRH) je distribuovaná jednotka rádiového vysílače/přijímače, která je fyzicky oddělena od jednotky pro zpracování základního pásma (BBU). Instaluje se v blízkosti antény, typicky na"
---

RRH je distribuovaná jednotka rádiového vysílače/přijímače, fyzicky oddělená od jednotky pro zpracování základního pásma a instalovaná v blízkosti antény za účelem snížení útlumu signálu a umožnění flexibilního nasazení sítě.

## Popis

Remote Radio Head (RRH) je klíčový architektonický prvek moderních decentralizovaných rádiových přístupových sítí (RAN). Obsahuje obvody pro rádiové kmitočty ([RF](/mobilnisite/slovnik/rf/)), včetně výkonových zesilovačů, filtrů, analogově-digitálních/digitálně-analogových převodníků a modulů optického rozhraní. RRH je nasazeno vzdáleně, v blízkosti anténního systému, zatímco funkce zpracování základního pásma (digitální zpracování signálu, protokoly vrstvy 2/vrstvy 3) jsou centralizovány v jednotce základního pásma ([BBU](/mobilnisite/slovnik/bbu/)) nebo v distribuované jednotce ([DU](/mobilnisite/slovnik/du/)) v terminologii 5G. Toto fyzické oddělení umožňuje vysokokapacitní transportní propojení s nízkou latencí (tzv. fronthaul), tradičně využívající protokol Common Public Radio Interface (CPRI) nebo jeho rozšířenou verzi eCPRI.

Primární úlohou RRH je provádění RF funkcí: převod digitalizovaných signálů základního pásma z BBU/DU na rádiový kmitočet pro vysílání a převod přijímaných RF signálů na digitalizované základní pásmo pro odeslání zpět ke zpracovatelské jednotce. RRH zajišťuje poslední stupeň vysílacího řetězce (zesílení) a první stupeň přijímacího řetězce (zesílení s nízkým šumem a filtrování). Díky umístění u antény RRH odstraňuje potřebu dlouhých koaxiálních výkonových kabelů s vysokým útlumem, které tradičně spojovaly anténu se skříní základnové stanice na úrovni terénu. To výrazně zlepšuje RF výkon a energetickou účinnost systému.

V síťové architektuře RRH umožňuje několik pokročilých modelů nasazení. V architektuře Centralized RAN (C-RAN) je více RRH z geografické oblasti připojeno k centralizovanému fondu BBU, což umožňuje sdružování zdrojů, kooperativní zpracování (jako je CoMP) a zjednodušenou údržbu. Rozdělení funkcí mezi RRH a BBU následuje funkční rozdělení definované standardy. Zavedení konceptu RRH bylo zásadní pro vývoj směrem k Cloud RAN a Open RAN (O-RAN), kde je rozhraní mezi RRH (nyní často nazývané Radio Unit nebo O-RU) a DU standardizováno a otevřené, což podporuje interoperabilitu mezi více dodavateli a síťovou flexibilitu.

## K čemu slouží

RRH bylo vytvořeno, aby řešilo významné ztráty rádiového signálu, které vznikají v dlouhých koaxiálních výkonových kabelech vedoucích od skříní základnových stanic na zemi k anténám na vrcholu stožáru. Tyto ztráty, které mohou činit několik decibelů, zhoršují výkon jak v uplinku, tak v downlinku, vyžadují vyšší vysílací výkon a snižují citlivost přijímače. Umístěním [RF](/mobilnisite/slovnik/rf/) obvodů k anténě RRH minimalizuje tyto ztráty ve výkonových kabelech, což vede ke zlepšenému pokrytí, kapacitě a energetické účinnosti lokality buňky.

Jeho vývoj byl dále motivován potřebou flexibilnějšího a nákladově efektivnějšího nasazení sítě. RRH jsou typicky menší, lehčí a vyžadují méně energie a chlazení než integrované základnové stanice, což usnadňuje jejich instalaci na stávající infrastrukturu, jako jsou lampové sloupy nebo fasády budov, pro husté městské pokrytí nebo indoorová řešení. Oddělení RRH a [BBU](/mobilnisite/slovnik/bbu/) umožňuje centralizaci zpracování základního pásma, což snižuje náklady na pronájem lokalit, zjednodušuje hardwarové aktualizace a usnadňuje pokročilé síťové funkce, jako je koordinované vícebodové vysílání a příjem (CoMP), které závisí na těsné koordinaci mezi více rádiovými body. Architektura RRH je tedy základním předpokladem pro moderní, škálovatelné a efektivní mobilní sítě, zejména pro nasazení 4G LTE-Advanced a 5G NR.

## Klíčové vlastnosti

- Vzdálené nasazení na místě antény k odstranění ztrát ve výkonových kabelech
- Obsahuje RF vysílač/přijímač, výkonový zesilovač a optické rozhraní
- Připojuje se k jednotce základního pásma přes standardizovaný fronthaul (např. CPRI, eCPRI)
- Umožňuje architektury Centralized RAN (C-RAN) a Cloud RAN
- Snižuje prostorové nároky, spotřebu energie a nároky na chlazení na lokalitě
- Usnadňuje pokročilé anténní systémy (AAS) a integraci Massive MIMO

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.871** (Rel-11) — Downlink MIMO Enhancement for LTE-Advanced
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TS 36.887** (Rel-12) — Energy Saving Enhancement for E-UTRAN Study
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements

---

📖 **Anglický originál a plná specifikace:** [RRH na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrh/)
