---
slug: "sl-rnti"
url: "/mobilnisite/slovnik/sl-rnti/"
type: "slovnik"
title: "SL-RNTI – Sidelink Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SL-RNTI"
fullName: "Sidelink Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-rnti/"
summary: "Dočasný identifikátor přidělený sítí uživatelskému zařízení (UE) pro sidelink komunikaci. Používá se pro plánování a adresování na fyzické vrstvě a umožňuje přímý přenos dat mezi zařízeními bez směrov"
---

SL-RNTI je dočasný identifikátor přidělený sítí uživatelskému zařízení (UE) pro sidelink komunikaci, používaný pro plánování a adresování za účelem přímého přenosu dat mezi zařízeními.

## Popis

SL-RNTI je klíčový identifikátor v rámci sidelink komunikační architektury 3GPP, specificky definovaný pro služby zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)) a vozidlo-vše ([V2X](/mobilnisite/slovnik/v2x/)) založené na LTE a později přenesený do NR sidelink. Jedná se o 16bitovou hodnotu konfigurovanou sítí prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) nebo odvozenou z předkonfigurovaných parametrů pro provoz mimo pokrytí. Uživatelské zařízení (UE) tento [RNTI](/mobilnisite/slovnik/rnti/) používá ke sledování kanálu [PDCCH](/mobilnisite/slovnik/pdcch/) (Physical Downlink Control Channel) pro sidelink povolení. Když síť plánuje sidelink přenos, odešle informaci [DCI](/mobilnisite/slovnik/dci/) (Downlink Control Information) zašifrovanou konkrétním SL-RNTI daného UE. Uživatelské zařízení provede kontrolu cyklickým redundantním kódem ([CRC](/mobilnisite/slovnik/crc/)) na přijaté DCI pomocí svého přiděleného SL-RNTI; pokud kontrola projde, UE dekóduje informace o povolení, které obsahují podrobnosti o alokaci zdrojů pro kanál [PSSCH](/mobilnisite/slovnik/pssch/) (Physical Sidelink Shared Channel) nebo PSCCH (Physical Sidelink Control Channel). Tento mechanismus zajišťuje, že sidelink přiřazení zdrojů jsou směrována na správné UE, což umožňuje efektivní přímou komunikaci s prevencí kolizí. V režimu 1 (řízeném sítí) má gNB nebo eNB plnou kontrolu nad alokací zdrojů a k adresování UE používá právě SL-RNTI. Pro autonomní výběr zdrojů (režimy 2/3/4) může být SL-RNTI stále použit pro specifickou řídicí signalizaci nebo ve scénářích s částečným síťovým pokrytím. Jeho role je analogická k C-RNTI používanému pro uplink/downlink, ale je vyhrazena pro sidelink rozhraní, oddělující řídicí rovinu pro přímou komunikaci od tradičních buněčných spojení.

## K čemu slouží

SL-RNTI byl zaveden, aby umožnil síťově řízené plánování pro přímou komunikaci mezi zařízeními, což je základním požadavkem pro služby založené na blízkosti (ProSe) a V2X. Před jeho zavedením standardy 3GPP postrádaly mechanismus pro efektivní přidělování a správu rádiových zdrojů pro přímé přenosy mezi uživatelskými zařízeními. Bez takového identifikátoru by základnová stanice nemohla adresovat jednotlivá UE pro sidelink povolení, což by nutilo spoléhat se pouze na soutěživý autonomní výběr zdrojů, který vede k potenciálním kolizím, nepředvídatelné latenci a neefektivnímu využití spektra ve scénářích s vysokou hustotou. SL-RNTI tento problém řeší tím, že poskytuje jedinečný, dočasný nástroj pro síť, aby mohla plánovat sidelink zdroje se stejnou spolehlivostí a kontrolou, jako plánuje uplink zdroje. To bylo obzvláště kritické pro aplikace veřejné bezpečnosti, kde je vyžadována předvídatelná komunikace, a pro V2X, kde jsou nízká latence a vysoká spolehlivost prvořadé. Umožňuje síti koordinovat interferenci, stanovovat prioritu provozu a bezproblémově integrovat sidelink komunikaci do celkové strategie správy rádiových zdrojů, čímž překlenuje propast mezi tradičními buněčnými a ad-hoc D2D sítěmi.

## Klíčové vlastnosti

- 16bitový síťově přidělený identifikátor pro sidelink plánování
- Použit pro zašifrování CRC u DCI formátů nesoucích sidelink povolení
- Umožňuje síťově řízenou alokaci zdrojů (provoz v režimu 1)
- Konfigurován prostřednictvím signalizace RRC nebo z předkonfigurace
- Umožňuje cílené adresování UE pro sidelink řídicí informace
- Základní pro správu interference a prevenci kolizí v plánovaném sidelinku

## Související pojmy

- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SL-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-rnti/)
