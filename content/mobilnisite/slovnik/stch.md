---
slug: "stch"
url: "/mobilnisite/slovnik/stch/"
type: "slovnik"
title: "STCH – Sidelink Traffic Channel"
date: 2025-01-01
abbr: "STCH"
fullName: "Sidelink Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/stch/"
summary: "Sidelink Traffic Channel (STCH) je fyzický kanál používaný pro přímou komunikaci mezi zařízeními (D2D) v LTE a NR sidelink. Přenáší uživatelská data a řídicí informace mezi uživatelskými zařízeními (U"
---

STCH je fyzický kanál používaný pro přímou komunikaci mezi zařízeními (D2D) v LTE a NR sidelink, který přenáší uživatelská data a řídicí informace mezi uživatelskými zařízeními (UE) podporujícími ProSe.

## Popis

Sidelink Traffic Channel (STCH) je základní součástí sidelink architektury 3GPP, která umožňuje přímou komunikaci mezi uživatelskými zařízeními (UE). V kontextu LTE (od Release 12) a následně NR je sidelink komunikace navržena pro scénáře, kdy jsou UE v blízkosti, což jim umožňuje přímo si vyměňovat data přes rozhraní PC5. STCH je fyzický kanál odpovědný za přenos vlastních uživatelských dat a souvisejících řídicích informací vrstvy 2 mezi těmito zařízeními. Funguje spolu s řídicími kanály, jako je Physical Sidelink Control Channel ([PSCCH](/mobilnisite/slovnik/pscch/)) a Physical Sidelink Shared Channel ([PSSCH](/mobilnisite/slovnik/pssch/)), přičemž PSSCH často představuje fyzickou vrstvu nesoucí transportní kanál STCH.

Architektonicky existuje STCH na vrstvě transportních kanálů (vrstva 2). Data z vyšších vrstev jsou zpracována přes transportní kanál Sidelink Shared Channel ([SL-SCH](/mobilnisite/slovnik/sl-sch/)), který je následně namapován na STCH. Zpracování STCH zahrnuje standardní postupy fyzické vrstvy, jako je kanálové kódování (např. Turbo kódování v LTE, [LDPC](/mobilnisite/slovnik/ldpc/) v NR), modulace a mapování zdrojů. Zdroje pro přenos STCH jsou přidělovány na základě režimů definovaných sítí nebo vybraných autonomně uživatelským zařízením (UE). V režimu 1 (plánované přidělování zdrojů) [eNB](/mobilnisite/slovnik/enb/)/gNB přiděluje konkrétní zdroje pro sidelink přenos. V režimu 2 (autonomní výběr zdrojů) si UE vybírá zdroje z fondu nakonfigurovaného sítí, přičemž využívá procedury snímání a rezervace ke zmírnění interference.

Klíčové komponenty spojené s STCH zahrnují Sidelink Radio Bearer (SLRB) pro správu QoS, podvrstvy [RLC](/mobilnisite/slovnik/rlc/) a [MAC](/mobilnisite/slovnik/mac/) pro segmentaci, [ARQ](/mobilnisite/slovnik/arq/) a plánování a zdroje fyzické vrstvy (resource bloky). STCH podporuje jak broadcast, tak groupcast komunikační režimy, což je zásadní pro V2X aplikace, kde vozidlo potřebuje vysílat bezpečnostní zprávy všem blízkým vozidlům nebo komunikovat v rámci specifické skupiny. Jeho návrh zahrnuje vlastnosti pro vysokou spolehlivost a nízkou latenci, jako je HARQ zpětná vazba v NR sidelink a pokročilá schémata kanálového kódování.

Úloha STCH v síti spočívá v umožnění efektivní komunikace bez infrastruktury. Uvolňuje zátěž z buněčného uplink/downlink, snižuje latenci pro kritickou komunikaci a rozšiřuje pokrytí v oblastech se špatnou nebo žádnou síťovou infrastrukturou. Pro veřejnou bezpečnost umožňuje přímou komunikaci záchranným složkám. Ve V2X je páteří pro zprávy spolupracujícího povědomí a předcházení kolizím. Vývoj STCH od LTE k NR přinesl významná vylepšení ve spektrální efektivitě, spolehlivosti a podpoře nových případů užití, jako je pokročilé autonomní řízení.

## K čemu slouží

Sidelink Traffic Channel byl zaveden, aby řešil rostoucí potřebu přímé komunikace mezi zařízeními, což představuje posun oproti tradičním buněčným sítím, kde veškerý provoz prochází základnovými stanicemi. Před standardizací 3GPP byla přímá komunikace omezena na nebuněčné technologie, jako je WiFi Direct, kterým chyběla řízená QoS, zabezpečení a bezproblémová integrace s buněčnými sítěmi potřebná pro kritické služby. Primární motivací pro STCH a širší sidelink rámec v Release 12 byla komunikace pro veřejnou bezpečnost, inspirovaná zkušenostmi z mimořádných situací, kdy síťová infrastruktura selhala. Řešil problém udržení komunikace mezi záchrannými složkami a civilisty, když je buněčná síť přetížená nebo zničená.

Další vývoj poháněly požadavky automobilového průmyslu na komunikaci Vehicle-to-Everything (V2X). Stávající komunikace na krátkou vzdálenost (DSRC) založená na IEEE 802.11p měla omezení v škálovatelnosti, dosahu a výkonu ve scénářích s vysokou rychlostí. Integrace V2X do buněčného ekosystému pomocí sidelink (a STCH) slibovala globální standardizaci, lepší koexistenci s buněčnými službami a cestu k 5G-vylepšenému V2X. Řešila potřebu ultra-spolehlivé komunikace s nízkou latencí (URLLC) pro bezpečnostně kritické aplikace, jako je kooperativní vnímání a koordinace autonomního řízení.

Vytvoření STCH také umožnilo komerční proximity služby (ProSe), což otevřelo nové aplikace, jako je sociální síťování, sdílení lokálního obsahu a objevování IoT zařízení. Řešilo problémy s efektivitou spektra tím, že umožnilo blízkým zařízením komunikovat přímo, čímž se snížilo zatížení síťové infrastruktury a páteřní sítě. Návrh technologie zajišťuje, kde je to možné, síťově řízený provoz, což udržuje dohled operátora nad rádiovými zdroji a správou interference, a zároveň umožňuje autonomní provoz ve scénářích bez pokrytí.

## Klíčové vlastnosti

- Podporuje přímou komunikaci UE-UE přes rozhraní PC5
- Přenáší uživatelská data a řídicí informace vrstvy 2 pro sidelink
- Funguje v režimech přidělování zdrojů plánovaných sítí (režim 1) i autonomních pro UE (režim 2)
- Umožňuje broadcast, groupcast a unicast komunikační režimy (zejména vylepšené v NR)
- Využívá pokročilé kanálové kódování (Turbo kódování v LTE, LDPC v NR) pro spolehlivost
- Je integrován s procedurami sidelink synchronizace a objevování

## Související pojmy

- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [PSSCH – Physical Sidelink Shared Channel](/mobilnisite/slovnik/pssch/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)

---

📖 **Anglický originál a plná specifikace:** [STCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/stch/)
