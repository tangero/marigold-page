---
slug: "nbmp"
url: "/mobilnisite/slovnik/nbmp/"
type: "slovnik"
title: "NBMP – Network Based Media Processing"
date: 2025-01-01
abbr: "NBMP"
fullName: "Network Based Media Processing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nbmp/"
summary: "Rámec definovaný 3GPP pro nasazování a správu funkcí pro zpracování médií (např. transkódování, analýza) jako virtualizovaných síťových služeb. Umožňuje flexibilní, škálovatelné doručování a obohacová"
---

NBMP je rámec 3GPP pro nasazování a správu virtualizovaných funkcí pro zpracování médií, jako je transkódování, který umožňuje flexibilní a škálovatelné doručování médií pro aplikace jako je imerzivní video a cloud gaming v sítích 5G.

## Popis

Network Based Media Processing (NBMP) je komplexní rámec standardizovaný 3GPP, počínaje Release 16, který umožňuje nasazení, orchestraci a správu životního cyklu úloh zpracování médií v telekomunikační síti. Zachází s funkcemi pro zpracování médií – jako je transkódování videa, míchání audia, detekce objektů, prostorové audio vykreslování a analýza kvality – jako s modulárními, znovupoužitelnými a síťově dostupnými službami. Hlavní myšlenkou je přesunout zpracování médií z rigidních, vyhrazených zařízení na okraji sítě nebo v koncových zařízeních uživatelů do flexibilního, cloud-nativního prostředí, které lze dynamicky vytvářet a řetězit za účelem vytváření pracovních postupů pro média.

Architektura NBMP je postavena kolem několika klíčových komponent definovaných ve specifikacích 3GPP. Ústřední entitou je NBMP Workflow Manager, který je zodpovědný za vytváření, konfiguraci a správu pracovních postupů pro zpracování médií. Pracovní postup je popsán pomocí Media Processing Description ([MPD](/mobilnisite/slovnik/mpd/)), což je XML nebo [JSON](/mobilnisite/slovnik/json/) dokument, který definuje zdroj média, sekvenci funkcí pro zpracování médií (nazývaných Media Functions nebo MFs), které mají být aplikovány, jejich konfigurační parametry a cíl pro zpracovaný výstup. Workflow Manager komunikuje s Media Function Repository, které ukládá deskriptory dostupných MFs, a s Media Function Instance Managerem, který je zodpovědný za vytváření skutečných softwarových kontejnerů nebo virtuálních strojů, které provádějí MFs na výpočetních prostředcích (např. v hostiteli [MEC](/mobilnisite/slovnik/mec/) nebo cloudovém datovém centru).

NBMP funguje tak, že umožňuje poskytovateli služeb nebo vývojáři aplikace odeslat popis pracovního postupu Workflow Manageru přes northbound [API](/mobilnisite/slovnik/api/). Workflow Manager tento popis následně zpracuje, vyhledá požadované Media Functions z repository a dá pokyn Media Function Instance Manageru, aby je nasadil na vhodné výpočetní prostředky s potřebnou síťovou konektivitou. Vytvoří datové toky mezi zdrojem, řetězcem MFs a cílem. Rámec také zahrnuje schopnosti pro monitorování stavu a výkonu pracovního postupu, aplikaci aktualizací a škálování instancí nahoru nebo dolů na základě zatížení. To umožňuje vytváření komplexních, reálných časových médiových kanálů, které se mohou přizpůsobit síťovým podmínkám, možnostem uživatelských zařízení a požadavkům aplikace, což je klíčové pro doručování vysoce kvalitních, interaktivních mediálních zážitků přes 5G.

## K čemu slouží

NBMP byl vytvořen, aby řešil rostoucí složitost a poptávku po pokročilých mediálních službách v éře 5G. Tradiční doručování médií spoléhalo na předzpracovaný obsah nebo náročné zpracování v koncových zařízeních uživatelů, což omezovalo flexibilitu, škálovatelnost a schopnost zavádět nové funkce. Vzestup aplikací jako cloud gaming, volumetrické video pro [AR](/mobilnisite/slovnik/ar/)/VR, analýza videa v reálném čase a personalizované vysílání (např. různé datové toky, rozlišení, překryvy pro různé diváky) vyžadoval nový paradigmat, kde by média mohla být dynamicky zpracovávána uvnitř samotné sítě.

Primární problémy, které NBMP řeší, jsou závislost na dodavateli, provozní rigidita a neefektivní využití prostředků. Před NBMP často nasazení nové mediální služby vyžadovalo integraci proprietárního hardwaru a softwaru od konkrétního dodavatele, což ztěžovalo inovace nebo škálování. NBMP standardizuje rozhraní a popisy pro mediální funkce, podporuje interoperabilitu a více-dodavatelský ekosystém. Také řeší problém latence a šířky pásma pro imerzivní média; zpracováním médií blíže uživateli na síťovém okraji (např. v uzlu Multi-access Edge Computing) může NBMP snížit latenci pro interaktivní aplikace a ušetřit šířku pásma páteřní sítě přizpůsobením jediného vysoce kvalitního streamu do více optimalizovaných verzí blízko místa spotřeby.

Dále je NBMP klíčovým enablerem pro síťové slicing a automatizaci služeb. Pracovní postup pro zpracování médií může být vytvořen jako součást síťového slicu vyhrazeného například pro živé vysílání události nebo esportovní turnaj. Schopnost rámce dynamicky spravovat životní cyklus těchto pracovních postupů umožňuje operátorům nabízet Media-as-a-Service, vytvářet nové zdroje příjmů a plnit přísné požadavky na kvalitu služeb (QoS) mediálních aplikací nové generace nákladově efektivním a agilním způsobem.

## Klíčové vlastnosti

- Standardizovaný Media Processing Description (MPD) pro deklarativní definici pracovního postupu
- Modulární a znovupoužitelné Media Functions (MFs) se standardizovanými deskriptory
- Dynamická orchestrace a správa životního cyklu úloh zpracování médií
- Podpora nasazení na heterogenních výpočetních platformách (cloud, MEC)
- Integrace s možnostmi sítě 5G pro QoS, síťový slicing a edge computing
- Northbound API pro poskytovatele služeb pro vytváření a správu mediálních pracovních postupů

## Definující specifikace

- **TS 26.238** (Rel-19) — Framework for Live Uplink Streaming (FLUS)
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.939** (Rel-19) — Framework for Live Uplink Streaming (FLUS)
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [NBMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nbmp/)
