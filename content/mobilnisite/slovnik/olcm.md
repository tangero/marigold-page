---
slug: "olcm"
url: "/mobilnisite/slovnik/olcm/"
type: "slovnik"
title: "OLCM – Outgoing Leg Control Model"
date: 2025-01-01
abbr: "OLCM"
fullName: "Outgoing Leg Control Model"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/olcm/"
summary: "Řídicí model používaný v architektuře CAMEL (Customised Applications for Mobile network Enhanced Logic) pro správu odchozí větve hovoru nebo relace. Definuje interakci mezi gsmSCF (CAMEL service contr"
---

OLCM je řídicí model CAMEL, který definuje interakci mezi gsmSCF a MSC/GMSC za účelem správy sestavení a směrování odchozí větve hovoru nebo relace.

## Popis

Outgoing Leg Control Model (OLCM) je základní součástí servisní architektury [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic) definované 3GPP. CAMEL umožňuje operátorsky specifické služby (jako předplacené, překlad čísel nebo VPN) tím, že externímu uzlu servisní logiky, gsmSCF (GSM Service Control Function), dovoluje řídit zpracování hovorů v přepínacích uzlech sítě ([MSC](/mobilnisite/slovnik/msc/) - Mobile Switching Centre nebo [GMSC](/mobilnisite/slovnik/gmsc/) - Gateway MSC). OLCM konkrétně řídí kontrolu 'odchozí větve' hovoru – tedy části od bodu, kde je hovor směrován k cíli. Když je detekován hovor spouštěný CAMEL (na základě dat o účastníkovi z [HLR](/mobilnisite/slovnik/hlr/)), MSC/GMSC pozastaví běžné zpracování hovoru a odešle zprávu InitialDP (Initial Detection Point) gsmSCF. gsmSCF pak může pomocí OLCM dát přepínači pokyn, jak pokračovat. Mezi klíčové pokyny patří 'Continue' (pokračovat v běžném směrování), 'Connect' (směrovat na konkrétní cílové číslo poskytnuté gsmSCF), 'ReleaseCall' (ukončit hovor) nebo 'RequestReportBCSMEvent' (požádat o další oznámení o událostech hovoru). Model funguje prostřednictvím sekvence detekčních bodů (DPs) a událostí, což umožňuje gsmSCF být notifikováno v konkrétních okamžicích hovoru (např. odpověď, obsazeno, neodpovězeno) a reagovat odpovídajícími řídicími příkazy. Tento model je stavový, přičemž gsmSCF udržuje dialog s MSC po dobu trvání větve hovoru, kterou řídí. OLCM je definován spolu s Incoming Leg Control Model ([ILCM](/mobilnisite/slovnik/ilcm/)) pro hovory prezentované účastníkovi a T-BCSM (Terminating Basic Call State Model) tvoří podkladový stavový stroj v přepínači, se kterým OLCM interaguje.

## K čemu slouží

OLCM byl vytvořen jako součást standardu [CAMEL](/mobilnisite/slovnik/camel/) k vyřešení problému umožnění inteligentní, reálné kontroly odchozích hovorů zevnitř jádrové sítě s přepojováním okruhů. Před CAMEL byly pokročilé hovorové služby pevně zakódovány v přepínačích, což je činilo závislými na dodavateli a pomalými k nasazení. OLCM poskytuje standardizované, otevřené rozhraní ([CAP](/mobilnisite/slovnik/cap/) - CAMEL Application Part), které umožňuje centralizované servisní platformě (gsmSCF) dynamicky řídit směrování a chování hovorů. To bylo motivováno potřebou konkurenčních funkcí, jako je předplacené roamování, bezplatná čísla a virtuální privátní sítě. Řeší omezení tradičních přístupů [IN](/mobilnisite/slovnik/in/) (Intelligent Network) tím, že je přizpůsoben aspektům mobility sítí GSM/UMTS, jako je zpracování mobility účastníka a využití dat z HLR. Model umožňuje operátorům rychle vytvářet a nasazovat nové služby generující příjmy bez nutnosti aktualizace každého přepínače v síti.

## Klíčové vlastnosti

- Definuje řídicí rozhraní mezi gsmSCF a MSC/GMSC pro odchozí větev hovoru.
- Využívá protokol CAP pro signalizační a řídicí zprávy.
- Umožňuje dynamické směrování hovorů (např. překlad čísel, přesměrování hovoru na základě servisní logiky).
- Umožňuje řízení účtování hovorů v reálném čase, což je klíčové pro předplacené služby.
- Podporuje hlášení událostí, což gsmSCF umožňuje sledovat průběh hovoru (odpověď, odpojení atd.).
- Funguje ve spojení se stavovým modelem T-BCSM v přepínači.

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [OLCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/olcm/)
