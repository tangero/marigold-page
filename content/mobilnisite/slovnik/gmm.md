---
slug: "gmm"
url: "/mobilnisite/slovnik/gmm/"
type: "slovnik"
title: "GMM – Global Multimedia Mobility"
date: 2025-01-01
abbr: "GMM"
fullName: "Global Multimedia Mobility"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gmm/"
summary: "Koncept služby 3GPP zaměřený na zajištění plynulé kontinuity a mobility multimediálních relací napříč heterogenními sítěmi. Umožňuje uživatelům udržovat aktivní multimediální relace (např. hovor, vide"
---

GMM je koncept služby 3GPP pro zajištění plynulé kontinuity a mobility multimediálních relací, který umožňuje uživatelům udržovat aktivní relace, jako je hovor nebo video, při přesunu mezi různými přístupovými technologiemi, například LTE a Wi-Fi.

## Popis

Global Multimedia Mobility (GMM) je servisní rámec definovaný 3GPP pro podporu nepřerušené multimediální komunikace při pohybu uživatelského zařízení (UE) napříč různými síťovými doménami a přístupovými technologiemi. Řeší problém kontinuity relací v heterogenním prostředí, kde může UE přecházet mezi sítěmi 3GPP (např. LTE, 5G NR) a ne-3GPP sítěmi (např. Wi-Fi, pevný broadband). GMM zajišťuje, že aktivní multimediální relace, jako je Voice over IP (VoIP), videohovory nebo streamovací aplikace, jsou při přechodech mezi sítěmi nebo změnách sítě udržovány s konzistentní kvalitou služby (QoS). Rámec zahrnuje protokoly, procedury a síťové funkce, které spravují přenos relací, mobilní politiky a alokaci zdrojů za účelem minimalizace přerušení a zachování uživatelské zkušenosti.

Z architektonického hlediska GMM využívá stávající mechanismy správy mobility 3GPP, jako jsou ty definované pro IP Multimedia Subsystem (IMS) a Packet Data Networks (PDN). Mezi klíčové komponenty patří Policy and Charging Rules Function (PCRF) pro vynucování QoS politik, Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) pro usměrňování výběru sítě UE a prvky IMS jádra jako Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro řízení relací. Během provozu, když UE detekuje dostupnou alternativní přístupovou síť (např. vstup do dosahu Wi-Fi), mohou procedury GMM spustit rozhodnutí o přechodu na základě politik, síly signálu a požadavků služby. Síť usnadňuje přenos vytvořením paralelního přenosového kanálu nebo cestou relace v cílové síti před přepnutím mediálního toku, a to za použití technik jako Single Radio Voice Call Continuity (SRVCC) pro hlas nebo IMS-based session continuity pro multimédia.

Jak to funguje, zahrnuje koordinaci mezi UE a síťovými funkcemi. Nejprve se UE zaregistruje v IMS a naváže multimediální relaci přes aktuální přístup. Při událostech mobility iniciuje UE nebo síť přípravu přechodu. Například při přechodu z LTE na Wi-Fi může UE použít politiky ANDSF k rozhodnutí, kdy přepnout, a poté provést autentizaci a nastavení zdrojů s cílovou sítí přes důvěryhodné ne-3GPP přístupové brány. IMS relace je ukotvena v centrálním uzlu (např. Service Centralization and Continuity Application Server), který spravuje stav relace a přesměrovává mediální toky. Během přechodu jsou parametry QoS znovu vyjednány tak, aby odpovídaly možnostem nového přístupu, a mohou být použity vyrovnávací paměti pro zabránění ztrátě paketů. Specifikace jako 3GPP TS 23.228 a TS 24.007 detailně popisují signalizační toky, zatímco TS 23.851 pokrývá vylepšení mobility. GMM také interaguje s síťovými protokoly mobility jako Proxy Mobile IPv6 (PMIPv6) nebo General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) pro udržení IP kontinuity, což zajišťuje, že IP adresa UE je zachována nebo plynule změněna.

## K čemu slouží

GMM byl zaveden, aby řešil fragmentaci v poskytování multimediálních služeb při vývoji mobilních sítí směrem k all-IP architekturám a heterogennímu přístupu. Před jeho standardizací byly multimediální relace často omezeny na jediný typ sítě (např. komutovaný hlas v 2G/3G) a přechody mezi technologiemi jako LTE a Wi-Fi vedly k přerušení relací nebo degradaci kvality. Rozšíření služeb založených na IMS a uživatelská poptávka po trvalém připojení motivovaly vytvoření GMM pro zajištění plynulé mobility, podobně jako tomu bylo u předávání hovorů mezi buňkami v tradičních sítích.

Historicky, s nástupem VoIP a videa přes LTE ve verzi Release 8 a dalších, 3GPP uznalo potřebu jednotného přístupu ke kontinuitě relací. Raná řešení jako SRVCC se zaměřovala na hlas, ale postrádala komplexní podporu pro multimédia. GMM tuto mezeru zaplnil tím, že poskytl rámec rozšiřující kontinuitu na datově náročné relace a řešil tak omezení předchozí správy mobility, která byla primárně navržena pro přenosy datových přenosových kanálů bez ohledu na relace. Řešil problémy jako přerušení médií během síťových přechodů, což umožnilo aplikacím jako videokonference zůstat aktivní, když se uživatelé pohybovali mezi domácí, kancelářskou a mobilní sítí.

Dále GMM usnadnil konvergenci mezi 3GPP a ne-3GPP sítěmi, podporující scénáře jako Wi-Fi volání a integraci pevné a mobilní sítě. Jeho vývoj byl hnán touhou operátorů přesouvat provoz na Wi-Fi při zachování kvality služeb a regulačními požadavky na spolehlivou nouzovou komunikaci napříč přístupy. Standardizací procedur GMM zajistil interoperabilitu mezi dodavateli a verzemi, čímž snížil složitost implementace v UE. V pozdějších verzích se vyvinul pro podporu 5G a síťového řezání (network slicing), čímž zajistil, že multimediální relace mohou využívat dynamické síťové zdroje. Jeho účel zůstává klíčový v dnešních prostředích multi-access edge computing ([MEC](/mobilnisite/slovnik/mec/)), kde aplikace s nízkou latencí vyžadují robustní správu mobility.

## Klíčové vlastnosti

- Zajišťuje plynulou kontinuitu multimediálních relací napříč heterogenními sítěmi (např. LTE, Wi-Fi, 5G)
- Integruje se s IMS pro řízení relací a jejich ukotvení během přechodů
- Využívá ANDSF a PCRF pro výběr přístupu založený na politikách a správu QoS
- Podporuje techniky jako SRVCC pro hlas a IMS session transfer pro multimédia
- Udržuje IP konektivitu a parametry QoS během síťových přechodů
- Usnadňuje scénáře konvergence pevné a mobilní sítě a Wi-Fi volání

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 24.007** (Rel-19) — GSM Um Interface Layer 3 Architecture
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol
- **TS 44.065** (Rel-19) — GPRS SNDCP Specification

---

📖 **Anglický originál a plná specifikace:** [GMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmm/)
