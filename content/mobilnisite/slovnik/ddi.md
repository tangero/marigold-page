---
slug: "ddi"
url: "/mobilnisite/slovnik/ddi/"
type: "slovnik"
title: "DDI – Data Description Indicator"
date: 2025-01-01
abbr: "DDI"
fullName: "Data Description Indicator"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ddi/"
summary: "Data Description Indicator (Ukazatel popisu dat) je protokolový prvek používaný ve signalizaci RRC podle 3GPP k popisu charakteristik datového toku nebo rádiového přenosového kanálu. Poskytuje síti a"
---

DDI je protokolový prvek ve signalizaci RRC podle 3GPP, který popisuje charakteristiky datového toku, jako je třída provozu a QoS, aby umožnil síti a UE správnou konfiguraci rádiového přenosového kanálu.

## Popis

Data Description Indicator (DDI) je základní součástí protokolové vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), podrobně specifikovanou např. v dokumentu 25.331. Funguje jako strukturovaný informační prvek vložený do zpráv RRC, jako jsou zprávy Radio Bearer Setup, Reconfiguration a Release. Primární rolí DDI je předat podrobný profil datového toku, který síť hodná zřídit, upravit nebo ukončit pro uživatelské zařízení (UE). Tento profil zahrnuje komplexní soubor atributů, které definují, jak mají být data zpracována přes rozhraní rádiového přenosu a v rámci protokolové architektury UE.

Z architektonického hlediska DDI generuje Core Network, obvykle na základě profilu QoS vyjednaného během procedury aktivace [PDP](/mobilnisite/slovnik/pdp/) kontextu nebo podobného procesu zahájení relace. Tyto informace jsou předány Radio Access Network (RAN), konkrétně Radio Network Controlleru ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS, přes rozhraní Iu. RNC následně začlení příslušné parametry z tohoto profilu do struktury DDI v rámci zprávy RRC odeslané UE. Vrstva RRC v UE DDI parsuje, aby odpovídajícím způsobem nakonfigurovala své nižší vrstvy, jako jsou Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Tato konfigurace zajišťuje, že logické kanály, režimy RLC a priority plánování odpovídají potřebám služby.

Klíčové součásti popsané DDI typicky zahrnují Třídu provozu (např. Conversational, Streaming, Interactive, Background), klíčové parametry QoS jako Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)), Maximum Bit Rate ([MBR](/mobilnisite/slovnik/mbr/)), Transfer Delay a Traffic Handling Priority (THP). Dále specifikuje mapování mezi rádiovým přenosovým kanálem a logickým kanálem, což definuje, zda je přenosový kanál pro uživatelská data nebo signalizaci řídicí roviny. DDI v podstatě funguje jako překladový mechanismus, který převádí abstraktní požadavky služby z Core Networku na konkrétní, proveditelné konfigurační příkazy pro protokoly rádiového rozhraní. Jeho přesná interpretace jak RAN, tak UE je klíčová pro zajištění, že celková přenosová cesta podporuje zamýšlený výkon aplikace, ať už se jedná o hlasové volání, video stream nebo webové prohlížení.

## K čemu slouží

DDI byl zaveden k vyřešení kritického problému dynamické a efektivní komunikace komplexních požadavků datových služeb od Core Networku k rádiovému rozhraní a mobilnímu zařízení. Před standardizovanými signalizačními mechanismy QoS bylo řízení různorodých datových služeb s různými nároky na latenci, spolehlivost a šířku pásma obtížné. DDI poskytuje strukturovaný a jednoznačný způsob popisu těchto požadavků, který umožňuje RAN přidělit odpovídající rádiové zdroje (jako jsou kódy rozprostření, výkon a časové sloty) a optimálně nakonfigurovat protokolové vrstvy pro každý konkrétní datový tok.

Jeho vytvoření bylo motivováno evolucí od okruhově spínaných hlasově orientovaných sítí (2G) k paketově spínaným sítím s podporou dat (3G/UMTS). Tento posun přinesl množství nových služeb – od webového prohlížení po videotelefonii – z nichž každá měla odlišné požadavky na QoS. Jednoduchý "best-effort" kanál byl nedostatečný. DDI jako součást protokolu RRC se stal klíčovým prostředkem pro vyjednávání a vynucování QoS přes rádiové rozhraní. Odstranil omezení pevných, předdefinovaných typů přenosových kanálů tím, že umožnil flexibilní a detailní popis charakteristik dat pro každou relaci, což bylo zásadní pro umožnění diferencovaných služeb a efektivní využití rádiových zdrojů v sítích 3GPP.

## Klíčové vlastnosti

- Zapouzdřuje detailní parametry QoS pro datový tok
- Umožňuje dynamické zřizování a rekonfiguraci rádiového přenosového kanálu
- Usnadňuje mapování mezi požadavky služby a konfigurací logického kanálu
- Přenášen v rámci signalizačních zpráv RRC (např. Radio Bearer Setup)
- Podporuje více tříd provozu (Conversational, Streaming, Interactive, Background)
- Umožňuje síťově řízenou priorizaci a přidělování zdrojů

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ddi/)
