---
slug: "nrt"
url: "/mobilnisite/slovnik/nrt/"
type: "slovnik"
title: "NRT – Neighbour Relation Table"
date: 2025-01-01
abbr: "NRT"
fullName: "Neighbour Relation Table"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nrt/"
summary: "Neighbour Relation Table je databáze spravovaná základnovou stanicí (eNodeB/gNB), která obsahuje informace o jejích sousedních buňkách, včetně jejich identit, kmitočtů a konfiguračních parametrů. Je z"
---

NRT je databáze v základnové stanici, která uchovává informace o sousedních buňkách a umožňuje jejich automatickou správu a optimalizaci pro předávání hovorů v samoorganizujících se sítích.

## Popis

Neighbour Relation Table (NRT) je základní datová struktura uložená ve správě (management plane) základnové stanice 3GPP – eNodeB v LTE nebo gNB v 5G NR. Je to lokální databáze, která katalogizuje známé sousední buňky pro každou buňku obsluhovanou danou stanicí. Každý záznam v NRT představuje sousední relaci (NR) a obsahuje komplexní sadu atributů nezbytných pro mobilitu a správu rádiových zdrojů. Mezi klíčová datová pole typicky patří globální identita cílové buňky ([E-UTRAN](/mobilnisite/slovnik/e-utran/) Cell Global Identifier ([ECGI](/mobilnisite/slovnik/ecgi/)) nebo NR Cell Global Identifier ([NCGI](/mobilnisite/slovnik/ncgi/))), fyzická identita buňky ([PCI](/mobilnisite/slovnik/pci/)), kmitočet nosné, kód sledovací oblasti a různé rádiové konfigurační parametry relevantní pro provedení předání hovoru.

Architektonicky se NRT nachází v [SON](/mobilnisite/slovnik/son/) a [RRM](/mobilnisite/slovnik/rrm/) funkčních blocích základnové stanice. Je zároveň zdrojem konfigurace pro algoritmy předávání hovorů i cílem aktualizací z [ANR](/mobilnisite/slovnik/anr/) funkce. Fungování NRT je ústřední pro proces ANR, který má tři hlavní fáze: Objevování sousedů, Odebírání sousedů a Správa sousedních relací. Ve fázi objevování základnová stanice nařídí UE v připojeném režimu provádět měření a hlásit zjištěné identity buněk (PCI), které nejsou v NRT. Základnová stanice následně požádá UE, aby přečetlo globální identitu buňky (ECGI/NCGI) a kód sledovací oblasti nově zjištěné buňky. Tyto nové informace se použijí k vytvoření nového záznamu v NRT.

Jak to funguje v praxi, zahrnuje neustálou interakci mezi UE, obsluhující základnovou stanicí a systémem Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)). Jakmile je záznam přidán do NRT, může základnová stanice konfigurovat parametry předání hovoru směrem k této buňce. NRT také uchovává stavové informace pro každou sousední relaci, například zda se jedná o relaci „No Remove“ (ručně konfigurovanou a chráněnou před automatickým smazáním) nebo relaci „No HO“ (buňku na černé listině, kde není předání hovoru povoleno). Systém OAM může provizorně zřídit počáteční záznamy NRT a nastavit politiky, ale funkce ANR automatizuje většinu správy životního cyklu. Tato automatizace drasticky snižuje manuální plánovací a konfigurační úsilí potřebné pro seznamy sousedů, zejména v hustých a dynamicky se měnících nasazeních sítí, a je základním kamenem SON schopností LTE a 5G.

## K čemu slouží

NRT a související funkce ANR byly vytvořeny, aby vyřešily obrovskou provozní zátěž a náchylnost k chybám při ruční konfiguraci seznamů sousedů v celulárních sítích. V sítích 2G a 3G museli inženýři ručně definovat a zřizovat seznam sousedních buněk pro každý sektor základnové stanice – což byl zdlouhavý, časově náročný proces náchylný k lidské chybě. Chybějící sousední relace vedly k přerušeným hovorům během mobility (selhání předání hovoru), zatímco nesprávné relace mohly způsobit interference nebo ping-pongová předání hovoru. Jak sítě s příchodem LTE a heterogenních nasazení (makro, mikro, piko buňky) houstly, tento manuální přístup se stal naprosto neudržitelným.

Zavedení NRT jako součásti SON frameworku ve 3GPP Release 8/9 představovalo změnu paradigmatu motivovanou potřebou provozní efektivity a robustnosti sítě. Vyřešilo omezení statického plánování tím, že umožnilo síti samostatně objevovat svou topologii. NRT poskytuje strukturované úložiště dat, které tuto automatizaci umožňuje. Z historické perspektivy to byl kritický krok k autonomním sítím, který snížil provozní náklady (OPEX) a zlepšil kvalitu služby tím, že zajistil, že seznamy sousedů pro předání hovoru jsou vždy přesné a aktuální, když jsou nasazovány nebo odebírány nové buňky.

Dále NRT řeší problém optimalizace sítě v reálném čase. Měnící se rádiové podmínky, dočasné výpadky buněk nebo nasazení nových small cells mohou být dynamicky reflektovány v NRT prostřednictvím procesu ANR. To zajišťuje optimální výkon mobility bez manuálního zásahu, což je nezbytné pro udržení vysoké spolehlivosti a uživatelského komfortu v moderních komplexních rádiových přístupových sítích. Tvoří datovou páteř pro pokročilé SON případy užití, jako je Mobility Robustness Optimization (MRO) a Mobility Load Balancing (MLB), které jsou závislé na přesné znalosti sousedů.

## Klíčové vlastnosti

- Lokální databáze v eNodeB/gNB uchovávající atributy sousedních buněk (ECGI/NCGI, PCI, kmitočet).
- Jádrová komponenta umožňující funkci Automatizované správy sousedních relací (ANR) v SON.
- Podporuje automatické objevování nových sousedů prostřednictvím hlášení měření od UE.
- Spravuje stavy sousedních relací (např. No Remove, No HO, normální).
- Poskytuje základní konfigurační data pro řídicí algoritmy předávání hovorů.
- Snižuje manuální úsilí při plánování a konfiguraci sítě pro správu mobility.

## Související pojmy

- [ANR – Automatic Neighbour Relationship](/mobilnisite/slovnik/anr/)
- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)
- [ECGI – E-UTRAN Cell Global Identification](/mobilnisite/slovnik/ecgi/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [NRT na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrt/)
