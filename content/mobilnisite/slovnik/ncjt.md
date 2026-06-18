---
slug: "ncjt"
url: "/mobilnisite/slovnik/ncjt/"
type: "slovnik"
title: "NCJT – Non-Coherent Joint Transmission"
date: 2025-01-01
abbr: "NCJT"
fullName: "Non-Coherent Joint Transmission"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncjt/"
summary: "Technika vysílání s více TRP, při níž více vysílacích/přijímacích bodů (TRP) vysílá nezávislé datové toky do UE bez nutnosti fázového sladění. Zvyšuje spolehlivost a propustnost, zejména na okrajích b"
---

NCJT (nekoherentní sdružené vysílání) je technika vysílání s více TRP, při níž více bodů vysílá nezávislé datové toky do uživatelského zařízení bez fázového sladění, čímž zvyšuje spolehlivost a propustnost využitím prostorové diverzity.

## Popis

Non-Coherent Joint Transmission (NCJT) je pokročilá technologie fyzické vrstvy s více vysílacími/přijímacími body (multi-TRP) zavedená ve specifikaci 3GPP Release 17 pro 5G-NR. Funguje v rámci vylepšení pro multi-TRP a vícepanelová uživatelská zařízení (UE). Na rozdíl od koherentního sdruženého vysílání ([CJT](/mobilnisite/slovnik/cjt/)), které vyžaduje přesnou fázovou synchronizaci a sdílení informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) mezi [TRP](/mobilnisite/slovnik/trp/) pro vytvoření koherentního paprsku, NCJT umožňuje více geograficky odděleným TRP (nebo panelům v rámci jednoho TRP) vysílat nezávislé datové toky do stejného UE současně na stejných časově-frekvenčních zdrojích. Tato vysílání nejsou fázově sladěna; jsou považována za samostatné prostorové vrstvy nebo vysílací příležitosti. UE přijímá tyto vícečetné toky a musí je oddělit pomocí pokročilého přijímacího zpracování, jako je potlačení interference s kombinací nebo postupná eliminace interference, využívající prostorové charakteristiky a potenciálně různá předpokládaná kvazi-ko-lokace ([QCL](/mobilnisite/slovnik/qcl/)) kanálů od každého TRP.

Architektonicky NCJT závisí na síťové koordinaci, kterou typicky řídí centrální jednotka ([CU](/mobilnisite/slovnik/cu/)) nebo koordinační uzel, jenž plánuje vysílání z účastnících se TRP. TRP mohou být propojeny ideálním (např. fronthaul) nebo neideálním přenosovým propojením (rozhraní Xn). Mezi klíčové komponenty patří plánovací entita, účastnící se TRP (kterými mohou být gNB nebo dálkové rádiové hlavice) a UE schopné vícepanelového příjmu nebo pokročilého dekódování více toků. Fyzický sdílený downlinkový kanál ([PDSCH](/mobilnisite/slovnik/pdsch/)) je primárním kanálem pro NCJT, kde může být z různých TRP vysíláno více PDSCH. Síť konfiguruje UE prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) a dynamického plánování ([DCI](/mobilnisite/slovnik/dci/)) pomocí parametrů, jako jsou stavy indikátoru konfigurace vysílání (TCI), z nichž každý je asociován s konkrétním TRP, aby indikoval referenční signály QCL pro každý tok.

Úlohou NCJT je zlepšit spektrální účinnost, spolehlivost a uživatelský zážitek, zejména pro uživatele se střední až vysokou mobilitou a na hranicích buněk. Je klíčovým prvkem pro scénáře ultra-spolehlivé komunikace s nízkou latencí (URLLC) a vylepšeného mobilního širokopásmového přístupu (eMBB). Tím, že nevyžaduje těsnou fázovou koherenci, snižuje oproti CJT přísné požadavky na synchronizaci a zpětnou vazbu CSI, což jej činí praktičtějším pro nasazení s neideálním přenosovým propojením. Technologie je podrobně specifikována v dokumentech 3GPP TS 38.214 pro procedury fyzické vrstvy a TS 38.306 pro rádiové přístupové schopnosti UE.

## K čemu slouží

NCJT bylo vytvořeno, aby řešilo rostoucí poptávku po vyšších přenosových rychlostech, lepším pokrytí a ultra-spolehlivé komunikaci v sítích 5G-Advanced, zejména v náročných rádiových prostředích. Před Release 17 se provoz s více TRP primárně zaměřoval na schémata jako koordinovaný vícebodový přístup (CoMP) se sdruženým vysíláním vyžadujícím koherentní kombinaci, což představovalo významnou režii pro odhad kanálu, zpětnou vazbu a těsnou synchronizaci mezi TRP. To omezovalo jeho praktičnost, zejména v nasazeních s neideálními přenosovými propojeními typickými pro heterogenní sítě.

Motivace pro NCJT vychází z potřeby robustnějšího a realizovatelnějšího řešení s více TRP, které obětuje část zisku z formování paprsku výměnou za sníženou složitost koordinace a zvýšený zisk z diverzity. Řeší problémy jako díry v pokrytí, mezibuněčný interference na okrajích a požadavky na spolehlivost služeb průmyslového IoT a URLLC. Tím, že umožňuje nekoherentní vysílání, umožňuje sítím využívat prostorovou diverzitu z více TRP bez nutnosti dokonalého sladění znalostí o kanálu, čímž zvyšuje odolnost proti překážkám a rychlému útlumu. Tento vývoj odráží posun směrem k využívání více, potenciálně méně koordinovaných, vysílacích bodů ke zvýšení výkonu systému v reálných scénářích nasazení.

## Klíčové vlastnosti

- Umožňuje simultánní vysílání s více TRP bez požadavků na fázovou synchronizaci
- Podporuje vysílání nezávislých datových toků na stejných časově-frekvenčních zdrojích
- Využívá více stavů TCI pro indikaci kvazi-ko-lokace na TRP
- Zvyšuje spolehlivost a propustnost prostřednictvím zisku z prostorové diverzity
- Kompatibilní s ideálním i neideálním přenosovým propojením mezi TRP
- Konfigurováno prostřednictvím RRC a dynamického DCI pro flexibilní plánování

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [NCJT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncjt/)
