---
slug: "psbch"
url: "/mobilnisite/slovnik/psbch/"
type: "slovnik"
title: "PSBCH – Physical Sidelink Broadcast Channel"
date: 2025-01-01
abbr: "PSBCH"
fullName: "Physical Sidelink Broadcast Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psbch/"
summary: "Fyzický kanál používaný v postranním spoji (sidelink, zařízení-zařízení) LTE a NR pro vysílání základních systémových informací z vysílajícího UE k ostatním UE v blízkosti. Umožňuje přímé zjišťování a"
---

PSBCH je fyzický kanál používaný v postranním spoji (sidelink) LTE a NR pro vysílání základních systémových informací z vysílajícího UE k ostatním blízkým UE, aby umožnil přímé zjišťování a synchronizaci.

## Popis

Physical Sidelink Broadcast Channel (PSBCH) je základním kanálem v rámci rozhraní postranního spoje (sidelink, [SL](/mobilnisite/slovnik/sl/)) podle 3GPP, které usnadňuje přímou komunikaci typu zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)) a vozidlo-vše ([V2X](/mobilnisite/slovnik/v2x/)). Funguje na fyzické vrstvě (vrstva 1) a je primárně odpovědný za vysílání informací hlavního informačního bloku pro postranní spoj (SL-MIB). Tyto informace jsou klíčové pro to, aby se UE vzájemně zjistila a vytvořila společný časový referenční bod pro následnou komunikaci po postranním spoji. PSBCH vysílá UE fungující jako zdroj synchronizace, kterým může být eNodeB/gNodeB (v pokrytí), jiné UE (mimo pokrytí) nebo globální družicový navigační systém ([GNSS](/mobilnisite/slovnik/gnss/)). Kanál nese parametry jako indikátor pokrytí, přímé číslo rámce a šířku pásma systému pro postranní spoj, což umožňuje přijímajícím UE synchronizovat se v čase a frekvenci a správně dekódovat další kanály postranního spoje.

Z architektonického hlediska je PSBCH mapován na specifické prvky zdrojů v rastru zdrojů postranního spoje. V postranním spoji založeném na LTE (často označovaném jako rozhraní PC5 v kontextu [ProSe](/mobilnisite/slovnik/prose/)) je PSBCH vysílán v podrámcích nakonfigurovaných pro komunikaci po postranním spoji, konkrétně v rámci periody řídicího kanálu pro vysílání po postranním spoji ([SBCCH](/mobilnisite/slovnik/sbcch/)). Struktura kanálu zahrnuje specifické modulace ([QPSK](/mobilnisite/slovnik/qpsk/)) a kódovací schémata definovaná v příslušných specifikacích 3GPP (např. TS 36.211). Informace přenášené PSBCH používají přijímající UE k získání časování rádiového rámce postranního spoje a k pochopení základní konfigurace nosné postranního spoje, což je předpokladem pro dekódování řídicího kanálu fyzického postranního spoje ([PSCCH](/mobilnisite/slovnik/pscch/)) a sdíleného kanálu fyzického postranního spoje (PSSCH).

V postranním spoji NR (zavedeném ve verzi 16 a vylepšeném v pozdějších verzích) má PSBCH i nadále zásadní roli, ačkoli jeho struktura a podrobnosti přenášených informací (nyní označovaných jako blok synchronizačního signálu NR postranního spoje, NR S-SSB) jsou přizpůsobeny flexibilnějšímu číslování a struktuře rámce NR. PSBCH NR je součástí S-SSB, který také zahrnuje primární synchronizační signál postranního spoje (PSSS) a sekundární synchronizační signál postranního spoje (SSSS). Tento blok je vysílán periodicky a jeho obsah zahrnuje základní informace pro počáteční přístup a konfiguraci fondu zdrojů. PSBCH je základním kamenem pro umožnění autonomního provozu postranního spoje, zejména ve scénářích, kdy jsou UE mimo síťové pokrytí, jako je komunikace pro veřejnou bezpečnost nebo formování kolon ve V2X.

## K čemu slouží

PSBCH byl zaveden, aby vyřešil základní problém synchronizace a distribuce systémových informací v přímé komunikaci zařízení-zařízení standardizované 3GPP. Před jeho zavedením byla buněčná komunikace striktně síťově centrická a vyžadovala, aby veškerá komunikace procházela základnovou stanicí (eNodeB). Tato architektura byla nedostatečná pro případy použití, jako je veřejná bezpečnost, kde si první respondenti potřebují komunikovat přímo, když je infrastruktura poškozena, nebo pro vozidlové sítě vyžadující komunikaci s ultranízkou latencí mezi blízkými vozidly. PSBCH poskytuje nezbytný mechanismus pro UE, aby vytvořila společnou 'síť postranního spoje' vysíláním minimální sady informací potřebných pro to, aby jiná zařízení našla potenciální vysílač a synchronizovala se s ním.

Jeho vytvoření bylo motivováno potřebou efektivní komunikace nezávislé na infrastruktuře. Bez PSBCH by zařízení neměla standardizovaný způsob, jak zjistit vzájemné časování nebo porozumět základní konfiguraci přímého komunikačního spoje. To by vedlo k neefektivní, ad-hoc komunikaci náchylné k rušení a vysoké spotřebě energie. PSBCH jako součást širšího rámce postranního spoje umožňuje řízenou, naplánovanou a efektivní přímou komunikaci. Řeší omezení předchozích řešení D2D mimo 3GPP (jako Wi-Fi Direct), kterým chyběla těsná integrace, kvalita služeb a škálovatelnost vyžadovaná pro rozsáhlé, kritické služby buněčných sítí mimo síť.

## Klíčové vlastnosti

- Vysílá hlavní informační blok pro postranní spoj (SL-MIB)
- Umožňuje časovou a frekvenční synchronizaci mezi UE
- Nese indikaci stavu pokrytí (v pokrytí/mimo pokrytí)
- Udává šířku pásma systému pro postranní spoj
- Podporuje více zdrojů synchronizace (síť, UE, GNSS)
- Základní pro počáteční procedury zjišťování a přístupu na postranním spoji

## Související pojmy

- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [PSSCH – Physical Sidelink Shared Channel](/mobilnisite/slovnik/pssch/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSBCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/psbch/)
