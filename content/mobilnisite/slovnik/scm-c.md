---
slug: "scm-c"
url: "/mobilnisite/slovnik/scm-c/"
type: "slovnik"
title: "SCM-C – SEAL Configuration Management Client"
date: 2025-01-01
abbr: "SCM-C"
fullName: "SEAL Configuration Management Client"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scm-c/"
summary: "Funkční entita v uživatelském zařízení (UE), která funguje jako klient pro protokol SEAL a je zodpovědná za přijímání, správu a aplikaci konfiguračních politik SEAL ze sítě. Umožňuje dynamickou konfig"
---

SCM-C je funkční entita v uživatelském zařízení (UE), která funguje jako klient pro protokol SEAL a spravuje a aplikuje konfigurační politiky ze sítě pro optimalizovanou zabezpečenou komunikaci.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Configuration Management Client (SCM-C) je klient protokolu definovaný v 3GPP TS 24.546, který sídlí v uživatelském zařízení (UE). Je součástí architektury SEAL (Service Enabler Architecture Layer), která poskytuje sadu společných služebních enablerů pro aplikace. Primární rolí SCM-C je rozhraní se SEAL Configuration Management Server ([SCM-S](/mobilnisite/slovnik/scm-s/)) v síti za účelem získání, správy a vynucení konfiguračních politik pro protokolový zásobník SEAL v zařízení. Funguje jako správní agent v rámci architektury SEAL klienta v UE.

Technicky SCM-C komunikuje se SCM-S pomocí SEAL Configuration Management Protocol (SCMP), který typicky běží nad [HTTPS](/mobilnisite/slovnik/https/) nebo jiným zabezpečeným transportem. Síťový operátor nebo poskytovatel služeb zasílá konfigurační dokumenty (např. založené na [XML](/mobilnisite/slovnik/xml/)) SCM-C. Tyto dokumenty obsahují politiky a parametry, které řídí chování různých služebních enablerů SEAL, jako jsou například ty pro zasílání zpráv, službu presence nebo přenos souborů. SCM-C je zodpovědný za parsování těchto konfiguračních dokumentů, jejich validaci proti schématu a následnou aplikaci nastavení na příslušné moduly služeb SEAL v rámci UE. To může zahrnovat nastavení časovačů, definování serverových adres (jako jsou adresy pro [RCS](/mobilnisite/slovnik/rcs/) Application Server), specifikaci bezpečnostních parametrů nebo povolování/zakazování určitých funkcí.

Architektura pozicuje SCM-C jako kritický kontrolní bod pro poskytování služeb a správu jejich životního cyklu. Umožňuje vzdálené, dynamické aktualizace chování služeb bez nutnosti kompletní aktualizace aplikace z obchodu s aplikacemi. Například operátor může změnit parametry pro službu zasílání zpráv nebo zavést novou funkci založenou na SEAL pouhou aktualizací konfigurace na SCM-S, která se následně rozšíří do všech UE prostřednictvím jejich instancí SCM-C. Klient musí také zvládat verzování konfiguračních dokumentů, návrat k předchozím konfiguracím při selhání aktualizace a zabezpečené ukládání citlivých parametrů. Jeho provoz je zásadní pro škálovatelné a spravovatelné nasazení standardizovaných služebních enablerů, jako jsou ty definované pro Rich Communication Services (RCS).

## K čemu slouží

SCM-C byl vytvořen, aby řešil provozní výzvu správy a konfigurace standardizovaných služebních enablerů v masivním měřítku nasazených zařízení. Před existencí takového správního rámce byla konfigurace pro služby jako [RCS](/mobilnisite/slovnik/rcs/) často pevně zabudována do firmwaru zařízení nebo spravována pomocí složitých protokolů pro správu zařízení, které nebyly uzpůsobeny pro služby aplikační vrstvy. To operátorům ztěžovalo dynamické úpravy parametrů služeb, zavádění nových funkcí nebo opravy konfiguračních problémů bez nutnosti, aby koncoví uživatelé aktualizovali software svého zařízení.

[SEAL](/mobilnisite/slovnik/seal/), zavedený v pozdějších vydáních 3GPP, si kladl za cíl poskytnout opakovaně použitelnou architekturu pro běžné komunikační služby. SCM-C jako jeho součást řeší problém flexibilní a vzdálené konfigurace. Umožňuje síťovým operátorům centrálně řídit chování služeb založených na SEAL v UE. To je klíčové pro zajištění konzistentní uživatelské zkušenosti se službou, implementaci operátorských politik a umožnění rychlého vývoje služeb. Vytvoření SCM-C v Rel-16 odráží posun průmyslu směrem ke konfigurovatelnějším a cloudem spravovaným servisním architekturám, odklon od statických, aplikací centrických konfigurací k modelu řízenému sítí, který zvyšuje agilitu a snižuje čas uvedení nových komunikačních funkcí na trh.

## Klíčové vlastnosti

- Klientská entita pro správu konfigurace SEAL
- Komunikuje se SCM-S pomocí SEAL Configuration Management Protocol (SCMP)
- Přijímá a parsuje konfigurační politiky ze sítě
- Aplikuje konfigurační parametry na služební enablery SEAL v rámci UE
- Podporuje dynamické aktualizace chování služeb přes vzdušné rozhraní
- Spravuje verzování konfigurace a záložní mechanismy

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [SCM-S – SEAL Configuration Management Server](/mobilnisite/slovnik/scm-s/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)

## Definující specifikace

- **TS 24.546** (Rel-19) — SEAL Configuration Management Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SCM-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/scm-c/)
