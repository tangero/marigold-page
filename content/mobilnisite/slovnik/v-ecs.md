---
slug: "v-ecs"
url: "/mobilnisite/slovnik/v-ecs/"
type: "slovnik"
title: "V-ECS – Visited Edge Configuration Server"
date: 2026-01-01
abbr: "V-ECS"
fullName: "Visited Edge Configuration Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/v-ecs/"
summary: "Síťová funkce ve navštívené síti, která poskytuje konfigurační informace uživatelskému zařízení (UE) pro přístup ke službám edge computingu. Umožňuje roamujícím UE objevovat a připojovat se k místním"
---

V-ECS je síťová funkce ve navštívené síti, která poskytuje konfigurační informace roamujícímu uživatelskému zařízení (UE) pro vyhledání a připojení k místním službám edge computingu.

## Popis

Visited Edge Configuration Server (V-ECS) je servisní schopnost zavedená v 5G pro podporu edge computingu pro roamující uživatele. Jde o síťovou funkci umístěnou v navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), která slouží jako konfigurační a vyhledávací server pro informace o službách edge computingu ([ECS](/mobilnisite/slovnik/ecs/)). Když uživatelské zařízení (UE) přejde do roamingu v navštívené síti, V-ECS mu poskytne potřebná konfigurační data pro přístup k místním prostředkům edge computingu, jako jsou instance Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)) nebo místní datové sítě ([LDN](/mobilnisite/slovnik/ldn/)). To umožňuje UE využívat služby s nízkou latencí hostované na síťovém okraji (edge) navštíveného operátora.

Z architektonického hlediska V-ECS komunikuje s Home Edge Configuration Server ([H-ECS](/mobilnisite/slovnik/h-ecs/)) v domovské síti uživatele. H-ECS může poskytnout UE počáteční profily nebo politiky pro edge služby. Když se UE přesune do navštívené sítě, může kontaktovat V-ECS (objevený prostřednictvím mechanismů jako [DNS](/mobilnisite/slovnik/dns/) nebo místní konfigurace), aby získal konfiguraci pro edge specifickou pro navštívenou síť. V-ECS komunikuje s místními poskytovateli edge služeb a síťovými funkcemi, aby shromáždil aktuální informace o dostupných edge službách, jejich schopnostech a přístupových bodech. Typicky vystavuje rozhraní založené na službách, pravděpodobně založené na [HTTP](/mobilnisite/slovnik/http/)/2 nebo podobných protokolech, jak je definováno v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 3GPP.

Jak to funguje: UE odešle požadavek na V-ECS, případně ověřený a autorizovaný prostřednictvím domovské sítě. V-ECS tento požadavek zpracuje, případně se poradí s místní politikou nebo H-ECS ohledně předplatitelských oprávnění. Poté vrátí konfigurační odpověď obsahující podrobnosti, jako jsou plně kvalifikované názvy domén (FQDN) nebo IP adresy místních EAS, parametry připojení pro edge datové sítě a smlouvy o úrovni služeb (SLA). UE tyto informace použije k navázání PDU session nebo připojení k místním edge prostředkům, čímž se vyhne delším cestám do domovské sítě. V-ECS hraje klíčovou roli ve vrstvě Edge Computing Enabler, překlenující propast mezi roamující mobilitou a dostupností edge služeb.

## K čemu slouží

V-ECS byl vytvořen za účelem rozšíření výhod edge computingu – ultra nízké latence a lokalizovaného zpracování dat – na roamující předplatitele. Před jeho zavedením byly edge služby převážně dostupné pouze v domovské síti, což znamenalo, že roamující uživatel se musel pro edge aplikace připojovat zpět do své domovské oblasti, čímž se ztrácely výhody nízké latence. To bylo významným omezením pro případy užití, jako je průmyslový IoT, autonomní řízení a rozšířená realita, které vyžadují konzistentní výkon s nízkou latencí bez ohledu na polohu.

Zavedený v 3GPP Release 18 jako součást rozšířeného rámce edge computingu řeší V-ECS tento problém tím, že umožňuje navštíveným operátorům kontrolovaným způsobem vystavovat svou místní edge infrastrukturu roamujícím uživatelům. Řeší výzvu vyhledávání služeb a konfigurace v kontextu roamingu a umožňuje bezproblémový přístup k místním edge službám. Jeho vývoj byl motivován snahou průmyslu o globální interoperabilitu edge služeb a potřebou podporovat nové obchodní modely, kde mohou operátoři nabízet edge computing jako službu zákazníkům jiných operátorů. V-ECS usnadňuje tato roamingová ujednání tím, že poskytuje standardizovaný způsob konfigurace UE pro místní přístup k edge.

## Klíčové vlastnosti

- Poskytuje konfiguraci edge služeb roamujícímu uživatelskému zařízení (UE)
- Umístěn v navštívené veřejné pozemní mobilní síti (VPLMN)
- Spolupracuje s domovským ECS (H-ECS) na předplatitelských politikách
- Objevuje a inzeruje lokálně dostupné Edge Application Servery
- Podporuje rozhraní založená na službách pro doručení konfigurace
- Umožňuje přístup k edge službám s nízkou latencí pro roamující UE

## Související pojmy

- [H-ECS – Home Edge Configuration Server](/mobilnisite/slovnik/h-ecs/)
- [EAS – Enterprise Application Server](/mobilnisite/slovnik/eas/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [V-ECS na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-ecs/)
