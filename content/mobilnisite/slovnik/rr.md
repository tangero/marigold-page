---
slug: "rr"
url: "/mobilnisite/slovnik/rr/"
type: "slovnik"
title: "RR – Radio Range"
date: 2025-01-01
abbr: "RR"
fullName: "Radio Range"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rr/"
summary: "Radio Range (RR) je maximální vzdálenost, na které lze mezi dvěma zařízeními, jako je základnová stanice a uživatelské zařízení, udržet spolehlivou rádiovou komunikaci. Jde o základní parametr při plá"
---

RR (dosah rádiového signálu) je maximální vzdálenost, na které lze mezi dvěma zařízeními, jako je základnová stanice a uživatelské zařízení, udržet spolehlivou rádiovou komunikaci.

## Popis

Radio Range (RR) je klíčový koncept v inženýrství bezdrátových sítí, který definuje provozní vzdálenostní limit pro rádiový spoj. Nejde o jedinou pevnou hodnotu, ale o komplexní funkci ovlivněnou řadou faktorů. Mezi hlavní determinanty patří vysílací výkon zařízení, citlivost přijímače, provozní frekvence, zisk a výška antény a daný prostředi šíření (např. městské, příměstské, venkovské). Modely útlumu na trase, jako jsou Okumura-Hata nebo COST-231, jsou matematicky odvozeny pro predikci útlumu signálu se vzdáleností a jsou nezbytným nástrojem pro výpočet RR ve fázi plánování sítě. Tyto modely zohledňují faktory jako difrakce, odraz a rozptyl, k nimž dochází při šíření rádiových vln.

Z pohledu systémové architektury RR přímo určuje velikost a topologii buňky. Při nasazení makrobuňky může být RR několik kilometrů, zatímco u malých buněk nebo indoor femtobuněk se měří v desítkách či stovkách metrů. Algoritmy správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) sítě využívají znalost RR a aktuálních podmínek signálu k rozhodování o předávání hovorů, řízení výkonu a řízení přístupu. Například uživatelské zařízení (UE) na okraji RR buňky bude typicky zaznamenávat nižší sílu signálu a vyšší interferenci, což spustí procedury předání hovoru nebo zvýšení výkonu v uplinku pro udržení spojení.

Jeho role se prolíná celým životním cyklem sítě. Při počátečním nasazení se výpočty RR používají pro umístění stanovišť a frekvenční plánování, aby bylo zajištěno souvislé pokrytí a minimalizována interference. Během provozu je RR klíčovým parametrem pro optimalizační úlohy, jako je úprava sklonu antény nebo výkonu pro řešení mezer v pokrytí nebo pilotní interference. Dále je RR nedílnou součástí definování regulatorních požadavků, jako jsou vyloučené zóny kolem základnových stanic, a je zohledňován při návrhu protokolů, které spravují mobilitu a kontinuitu relace při pohybu uživatelů mezi různými rádiovými dosahy.

## K čemu slouží

Koncept Radio Range existuje, aby poskytl kvantifikovatelný základ pro návrh, nasazení a optimalizaci rádiových sítí. Před systematickým modelováním RR bylo nasazování sítí z velké části empirické a neefektivní, což vedlo k mezerám v pokrytí, nadměrné interferenci a suboptimální kapacitě. Definice RR umožňuje inženýrům matematicky předpovídat oblasti pokrytí, což umožňuje proaktivní plánování sítě, které splňuje specifické cíle kvality služeb a kapacity ještě před vybudováním fyzické infrastruktury.

Řeší základní problém převodu specifikací rádiového zařízení na reálný výkon. Výstupní výkon a citlivost transceiveru jsou laboratorní měření, ale RR je kontextualizuje do praktické metriky založené na vzdálenosti pro nasazení v terénu. To je zásadní pro nákladově efektivní nasazení, protože pomáhá určit minimální počet buněčných stanovišť potřebných k pokrytí dané geografické oblasti. Dále, porozuměním faktorům, které RR omezují, jako jsou překážky nebo frekvenční pásma, mohou návrháři sítí vybrat vhodné technologie (např. nižší frekvence pro širší pokrytí) a strategie nasazení (např. zahušťování s malými buňkami) pro dosažení servisních cílů.

Historicky, s vývojem buněčné technologie od 2G k 5G, význam přesného modelování RR pouze vzrostl. Zatímco rané sítě se primárně soustředily na hlasové pokrytí velkých oblastí, moderní sítě musí poskytovat vysoké datové rychlosti a ultra-spolehlivou komunikaci s nízkou latencí. Tento posun vyžaduje složitější úvahy o RR, které zohledňují beamforming v systémech Massive [MIMO](/mobilnisite/slovnik/mimo/), charakteristiky šíření milimetrových vln s velmi krátkým dosahem a integraci heterogenních sítí (HetNets) s výrazně odlišnými profily RR pro makrobuňky, mikrobuňky a pikobuňky.

## Klíčové vlastnosti

- Určován analýzou rozpočtu spoje zahrnující vysílací výkon, citlivost přijímače a zisky antén
- Modelován pomocí empirických nebo deterministických modelů útlumu na trase (např. Hata, COST-231, Ray Tracing)
- Významně se liší v závislosti na frekvenčním pásmu, výšce antény a typu terénu/zástavby
- Základní vstup pro nástroje plánování a optimalizace buněčných sítí
- Definuje hranici buňky a ovlivňuje parametry předávání hovorů a řízení výkonu
- Klíčový faktor pro výpočet kapacity sítě a spektrální účinnosti

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.161** (Rel-19) — Network-based IP Flow Mobility (NBIFOM)
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.866** (Rel-19) — IMS Disaster Prevention & Restoration Enhancement
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [RR na 3GPP Explorer](https://3gpp-explorer.com/glossary/rr/)
