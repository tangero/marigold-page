---
slug: "d2d"
url: "/mobilnisite/slovnik/d2d/"
type: "slovnik"
title: "D2D – Device-to-Device"
date: 2025-01-01
abbr: "D2D"
fullName: "Device-to-Device"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/d2d/"
summary: "Komunikace zařízení-zařízení (Device-to-Device, D2D) umožňuje přímou výměnu dat mezi blízkými uživatelskými zařízeními (UE) bez směrování provozu přes infrastrukturu mobilní sítě. Je základem pro služ"
---

D2D je metoda, která umožňuje blízkým mobilním zařízením komunikovat přímo bez využití infrastruktury mobilní sítě, čímž zvyšuje efektivitu a umožňuje služby jako je komunikace pro veřejnou bezpečnost.

## Popis

Komunikace zařízení-zařízení (Device-to-Device, D2D), standardizovaná 3GPP, umožňuje uživatelským zařízením (UE) v těsné blízkosti navázat přímé rádiové spojení pro výměnu dat, čímž se obejde tradiční cesta přes eNodeB/gNB a jádro sítě. Tento přímý spoj je často označován jako 'sidelink' (SL), na rozdíl od konvenčního 'uplinku' (do sítě) a 'downlinku' (ze sítě). Architektura integruje D2D do celkového rámce LTE a 5G NR, přičemž vyžaduje asistenci sítě pro kritické funkce, jako je objevování, přidělování zdrojů a zabezpečení, i když je používána přímá datová cesta. Síť si udržuje kontrolu nad navazováním D2D relace, vynucováním politik a správou mobility, čímž zajišťuje kontinuitu služeb a koordinaci rušení s mobilní sítí.

Operačně zahrnuje D2D komunikace několik klíčových fází. První je Objevování (Discovery), kdy si UE vzájemně identifikují svou přítomnost a vhodnost pro přímou komunikaci. 3GPP definuje jak objevování s asistencí sítě (kde síť poskytuje parametry pro objevování), tak přímé objevování (kde UE autonomně vysílají/naslouchají pomocí předkonfigurovaných zdrojů). Po objevení je navázán přímý komunikační spoj. Pro D2D založené na LTE (zavedené v Rel-12/13 pro ProSe) se k tomu používá specifická struktura fyzické vrstvy (sidelink kanály jako PSCCH a PSSCH) v rámci uplink spektra, s módy přidělování zdrojů od plánovaných sítí (Mode 1) po autonomní výběr UE (Mode 2). V 5G NR (od Rel-16 dále) je rámec sidelink významně vylepšen, podporuje nové numerologie, širší šířky pásma a sofistikovanější schémata přidělování zdrojů (Mode 1 a Mode 2) pro vyšší spolehlivost a nižší latenci.

Klíčové komponenty umožňující D2D zahrnují funkci ProSe v jádru sítě (pro LTE ProSe), která zpracovává data účastníků a autorizaci související s ProSe; aplikační server ProSe pro podporu na aplikační vrstvě; a úpravy UE a RAN pro podporu sidelink fyzických kanálů a procedur. Pro NR sidelink jsou tyto funkce integrovány do 5G Core (5GC) a Next-Generation RAN (NG-RAN). Protokolový zásobník D2D zahrnuje nové vrstvy a adaptace na vrstvách PHY, [MAC](/mobilnisite/slovnik/mac/), RLC a PDCP pro správu přímé komunikace, včetně specifických logických kanálů, [HARQ](/mobilnisite/slovnik/harq/) procesů a bezpečnostních mechanismů pro sidelink.

Role D2D v síti je mnohostranná. Slouží jako mechanismus odlehčení pro snížení přetížení na buněčných spojích a uzlech jádra sítě, zejména v hustých městských scénářích. Je klíčová pro komunikaci veřejné bezpečnosti, umožňující záchranářům komunikovat přímo, když je síťová infrastruktura poškozená nebo nedostupná. Dále tvoří základní rádiovou technologii pro komunikaci vozidlo-se-vším (Vehicle-to-Everything, V2X), umožňující výměnu bezpečnostních zpráv s nízkou latencí mezi vozidly (V2V), chodci (V2P) a infrastrukturou (V2I). D2D tak transformuje UE z pouhého koncového bodu na potenciální přenosový uzel nebo uzel přímé komunikace, čímž umožňuje decentralizovanější a odolnější síťové architektury.

## K čemu slouží

Komunikace D2D byla zavedena především k řešení dvou hlavních potřeb: zvýšení efektivity sítě a umožnění kritických služeb, kde je tradiční buněčné připojení nepraktické. Historicky byla veškerá buněčná komunikace striktně hvězdicová, vyžadující průchod všech dat přes základnovou stanici, dokonce i pro dvě zařízení nacházející se těsně vedle sebe. To bylo spektrálně neefektivní, zvyšovalo latenci a spotřebovávalo zbytečné zdroje jádra sítě. D2D to řeší tím, že umožňuje přímou lokální komunikaci, čímž odlehčuje provoz z infrastruktury, zlepšuje spektrální efektivitu (bity/Hz/buňka) a snižuje end-to-end latenci pro aplikace založené na blízkosti.

Druhým, stejně důležitým motivem byla podpora služeb veřejné bezpečnosti a služeb kritických pro misi. Během katastrof nebo v odlehlých oblastech může být buněčná infrastruktura narušena nebo neexistovat. Záchranáři a personál veřejné bezpečnosti potřebují spolehlivé komunikační kanály nezávislé na síti. D2D tuto schopnost poskytuje, umožňující přímou komunikaci zařízení-zařízení pro hlas i data, což byl klíčový faktor pro její počáteční standardizaci v 3GPP Rel-12 v rámci pracovní položky Proximity Services (ProSe). Tím se řešilo významné omezení sítí před 4G, kterým chyběly standardizované módy přímé komunikace pro takové scénáře.

Dále D2D položila základ pro budoucí pokročilé služby, nejvýznamněji pro komunikaci vozidlo-se-vším (Vehicle-to-Everything, V2X). Potřeba automobilového průmyslu po ultra-spolehlivé, nízkolatenční komunikaci (např. pro prevenci kolizí) nemohla být plně uspokojena pouze tradičními buněčnými přístupy V2N (vozidlo-síť). Přímá komunikace V2V prostřednictvím D2D/sidelink poskytuje potřebný výkon. D2D se tak vyvinula z technologie zaměřené na ProSe v LTE na zobecněný sidelink rámec v 5G NR, navržený k podpoře široké škály případů užití včetně pokročilého V2X, průmyslového IoT a rozšířené reality, kde je přímá, lokalizovaná komunikace výhodná.

## Klíčové vlastnosti

- Přímý komunikační spoj (sidelink) mezi UE bez průchodu síťovou infrastrukturou
- Řízené objevování a nastavení komunikace sítí pro autorizaci a správu zdrojů
- Více módů přidělování zdrojů (plánovaných sítí a autonomních UE) pro flexibilitu
- Provoz ve scénářích s pokrytím, bez pokrytí i s částečným pokrytím
- Integrovaný sidelink protokolový zásobník se specifickými PHY/MAC kanály (např. PSCCH, PSSCH)
- Základ pro služby založené na blízkosti (ProSe) a pokročilé komunikační služby V2X

## Definující specifikace

- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.843** (Rel-12) — D2D Proximity Services Feasibility Study
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements

---

📖 **Anglický originál a plná specifikace:** [D2D na 3GPP Explorer](https://3gpp-explorer.com/glossary/d2d/)
