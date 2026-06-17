---
slug: "lmr"
url: "/mobilnisite/slovnik/lmr/"
type: "slovnik"
title: "LMR – Land Mobile Radio"
date: 2026-01-01
abbr: "LMR"
fullName: "Land Mobile Radio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lmr/"
summary: "Profesionální služba mobilní radiokomunikace používaná organizacemi pro veřejnou bezpečnost, energetikou a průmyslem pro zásadní (mission-critical) hlas a data. V kontextu 3GPP označuje integraci a vý"
---

LMR (Land Mobile Radio, pozemní mobilní radiokomunikace) je tradiční profesionální mobilní radiová služba pro zásadní (mission-critical) hlas a data, kterou standardy 3GPP usilují integrovat a rozvíjet společně se širokopásmovými buněčnými sítěmi, jako jsou LTE a 5G.

## Popis

Land Mobile Radio (LMR) v kontextu 3GPP označuje soubor standardů a systémových schopností, které umožňují integraci, vzájemné propojení a vývoj tradičních profesionálních (nebo privátních) systémů mobilní radiokomunikace se širokopásmovými buněčnými sítěmi založenými na 3GPP, primárně pro služby kritické pro plnění úkolů (Mission-Critical, [MC](/mobilnisite/slovnik/mc/)). Tradiční LMR systémy, jako jsou TETRA, P25 nebo [DMR](/mobilnisite/slovnik/dmr/), jsou úzkopásmové sítě optimalizované pro hlasové služby push-to-talk a nízkorychlostní data pro sektor veřejné bezpečnosti, dopravy a energetiky. Práce 3GPP, počínaje Release 12, se zaměřuje na poskytnutí ekvivalentních a vylepšených funkcí pro kritické služby přes LTE a následně 5G NR, což vede k tzv. Mission-Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), Mission-Critical Video ([MCVideo](/mobilnisite/slovnik/mcvideo/)) a Mission-Critical Data (MCData).

Architektura pro umožnění LMR služeb přes systémy 3GPP zahrnuje několik klíčových funkčních komponent definovaných v jádru sítě. Ústřední entitou je aplikační server služeb pro kritické úkoly (Mission-Critical Service, [MCS](/mobilnisite/slovnik/mcs/)), který hostuje servisní logiku pro správu skupin, řízení práva ke slovu (floor control) a správu identit. Tento server komunikuje s jádrem sítě 3GPP (EPC nebo 5GC) přes standardizovaná rozhraní, jako je referenční bod MCx. Uživatelské zařízení (UE) musí podporovat klienta pro kritické služby, který komunikuje s tímto serverem. Podpůrná síť 3GPP poskytuje základní přenosové služby s vylepšenou kvalitou služeb (QoS) a mechanismy priority, jako je identifikátor třídy kvality služeb ([QCI](/mobilnisite/slovnik/qci/)) a hodnoty priority přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)) specificky určené pro provoz kritický pro plnění úkolů, což zajišťuje možnost vytěsnění jiného provozu a vysokou spolehlivost.

Princip fungování: Typické volání MCPTT zahrnuje stisknutí tlačítka push-to-talk na zařízení uživatele. Klient v UE odešle požadavek na zahájení relace na aplikační server MCS. Server spravuje skupinové volání, rozhoduje o požadavcích na právo ke slovu (přiděluje 'právo ke slovu' vždy pouze jednomu mluvčímu) a vytváří potřebné mediální cesty mezi účastníky. Síť 3GPP zajišťuje přenos signalizačních a hlasových paketů s nízkou latencí a vysokou prioritou, případně využívá služeb komunikace na blízkou vzdálenost (ProSe) pro přímou komunikaci mezi zařízeními, pokud není dostupné síťové pokrytí. Systém podporuje základní funkce LMR, jako jsou skupinová volání, vysílací hovory, tísňová upozornění, dynamická správa skupin a požadavky na odolná UE, a to vše při využití vysoké přenosové kapacity, nízké latence a všudypřítomného pokrytí moderních buněčných sítí.

## K čemu slouží

Hlavním účelem standardizace schopností LMR v rámci 3GPP je řešení omezení tradičních, izolovaných LMR systémů a podpora vývoje globálního, interoperabilního širokopásmového standardu pro kritické komunikace. Tradiční LMR sítě, ačkoli jsou pro hlas vysoce spolehlivé, pracují v spektrálně omezených úzkopásmových kanálech, což značně omezuje možnosti přenosu dat pro video, mapy s vysokým rozlišením nebo přístup k databázím. Jsou také často fragmentované na národní úrovni, což brání přeshraniční interoperabilitě mezi složkami veřejné bezpečnosti. Vytvoření služeb pro kritické úkoly založených na 3GPP bylo motivováno událostmi v oblasti veřejné bezpečnosti, které zdůraznily potřebu širokopásmových dat vedle hlasu.

Práce 3GPP, silně ovlivněná požadavky organizací jako je National Public Safety Telecommunications Council (NPSTC) a TCCA, si kladla za cíl využít výhod rozsahu a rychlé inovace komerčního buněčného průmyslu. Řeší problém poskytování zabezpečených, odolných a funkčně bohatých kritických komunikací přes společnou, rozvíjející se síťovou infrastrukturu (potenciálně pomocí síťového řezání). Tato konvergence umožňuje organizacím mít jedno zařízení jak pro širokopásmové datové aplikace, tak pro hlasové služby kritické pro plnění úkolů, což snižuje náklady a složitost a zároveň umožňuje možnosti nové generace, jako je streamování videa v reálném čase z místa zásahu, sdílení polohy a integrace s IoT senzory, což zásadně mění operační účinnost jednotek první pomoci a průmyslových týmů.

## Klíčové vlastnosti

- Mission-Critical Push-To-Talk (MCPTT) s pokročilým řízením práva ke slovu (floor control) a správou skupin
- Podpora služeb Mission-Critical Video (MCVideo) a Mission-Critical Data (MCData)
- Vysoká priorita QoS s možností vytěsnění jiného provozu v sítích 3GPP
- Podpora komunikačních režimů v síti, mimo síť (pomocí ProSe) a přechodových režimů
- Vzájemné propojení se stávajícími tradičními LMR systémy (např. TETRA, P25)
- Robustní bezpečnostní rámec zahrnující autentizaci, šifrování a ochranu integrity pro kritické komunikace

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [GCSE – AS Group Communication Service Enabler Application Server](/mobilnisite/slovnik/gcse/)

## Definující specifikace

- **TS 22.468** (Rel-19) — Group Communication System Enabler Requirements
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TS 24.283** (Rel-19) — Mission Critical Location Management Protocol
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems
- **TS 29.379** (Rel-19) — MCPTT call control interworking with LMR systems

---

📖 **Anglický originál a plná specifikace:** [LMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmr/)
