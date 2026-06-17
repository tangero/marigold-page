---
slug: "mttc"
url: "/mobilnisite/slovnik/mttc/"
type: "slovnik"
title: "MTTC – Mass Transit Train Control"
date: 2025-01-01
abbr: "MTTC"
fullName: "Mass Transit Train Control"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mttc/"
summary: "MTTC je kategorie služeb 3GPP pro železniční komunikační systémy, umožňující bezpečné a efektivní řízení a provoz vlaků. Podporuje kritické funkce jako automatické řízení vlaku, signalizaci a informac"
---

MTTC je kategorie služeb 3GPP pro železniční systémy, která umožňuje bezpečné řízení a provoz vlaků, jako je signalizace a informace pro cestující, prostřednictvím celulárních sítí za účelem zvýšení bezpečnosti a efektivity.

## Popis

Mass Transit Train Control (MTTC) je kategorie služeb definovaná 3GPP v rámci širšího rámce železničních komunikací, která konkrétně řeší potřeby systémů pro řízení a správu vlaků v prostředích hromadné dopravy, jako jsou metro, podzemní dráhy a lehké dráhy. Využívá celulární technologie, zejména 4G LTE a 5G, k zajištění spolehlivých, nízkolatenčních a vysoce dostupných bezdrátových spojů pro kritické železniční operace. Architektura se integruje se systémy železniční mobilní komunikace (Railway Mobile Communication Systems, RMCS) a využívá vyhrazené síťové řezy nebo specializované funkce core sítě k zajištění izolace a garancí výkonu. Mezi klíčové komponenty patří jednotky na palubě vlaku (onboard units, OBU), zařízení podél tratě (wayside equipment) a dispečinková centra, která řídí pohyb vlaků. MTTC podporuje výměnu dat pro funkce jako Automatické řízení vlaku (Automatic Train Control, [ATC](/mobilnisite/slovnik/atc/)), které zahrnuje Automatickou ochranu vlaku (Automatic Train Protection, [ATP](/mobilnisite/slovnik/atp/)) pro bezpečnost, Automatický provoz vlaku (Automatic Train Operation, [ATO](/mobilnisite/slovnik/ato/)) pro řízení a Automatický dohled nad vlakem (Automatic Train Supervision, [ATS](/mobilnisite/slovnik/ats/)) pro monitorování. Komunikační protokoly jsou přizpůsobeny železničním signalizačním standardům, jako je Evropský vlakový zabezpečovací systém (European Train Control System, ETCS) nebo Řízení vlaku na bázi komunikace (Communications-Based Train Control, CBTC), často využívající IP transport s přísnými požadavky na kvalitu služeb (QoS) pro latenci (např. pod 100 ms) a spolehlivost (např. 99,999 %). Služba komunikuje s core sítí 3GPP prostřednictvím vyhrazených [API](/mobilnisite/slovnik/api/) a může využívat edge computing pro lokální zpracování dat za účelem snížení latence. Bezpečnostní mechanismy zahrnují šifrování, autentizaci a ochranu integrity, aby se zabránilo neoprávněnému přístupu a zajistil bezpečný provoz. Úlohou MTTC je umožnit nepřetržitou komunikaci mezi vlakem a infrastrukturou, podporovat sledování v reálném čase, zabránění kolizím, regulaci rychlosti a nouzové brzdné příkazy, čímž tvoří páteř moderních automatizovaných železničních systémů.

## K čemu slouží

MTTC byl zaveden, aby řešil rostoucí potřebu standardizovaných komunikačních řešení založených na celulárních sítích pro železniční systémy hromadné dopravy, která nahrazují nebo rozšiřují starší systémy jako [GSM-R](/mobilnisite/slovnik/gsm-r/) (GSM for Railways). Tradiční železniční komunikace spoléhala na vyhrazené, často proprietární bezdrátové sítě, které byly nákladné na nasazení a údržbu a měly omezenou datovou kapacitu a možnosti vývoje. Rozšíření LTE a 5G nabídlo příležitost využít komerční celulární technologie pro železniční operace, poskytující vyšší šířku pásma, nižší latenci a lepší ekonomiku z rozsahu. MTTC tyto problémy řeší definováním rámce služeb v rámci 3GPP, který zajišťuje interoperabilitu, spolehlivost a bezpečnost pro aplikace řízení vlaků. Umožňuje železnicím migrovat na sítě založené na IP, podporující pokročilé funkce jako prediktivní údržba, informace pro cestující v reálném čase a zvýšená provozní efektivita. Historický kontext zahrnuje ukončení podpory GSM-R a posun odvětví k systému Future Railway Mobile Communication System ([FRMCS](/mobilnisite/slovnik/frmcs/)), kde MTTC slouží jako klíčová komponenta. Řeší omezení předchozích přístupů tím, že nabízí plynulou mobilitu, podporu pro scénáře s vysokou rychlostí a integraci se širší infrastrukturou IoT a chytrých měst, což v konečném důsledku zlepšuje bezpečnost a kapacitu v městských systémech hromadné dopravy.

## Klíčové vlastnosti

- Podpora kritických funkcí řízení vlaku (ATC, ATP, ATO, ATS)
- Nízkolatenční, vysoce spolehlivá komunikace pro bezpečnostní aplikace
- Integrace s 3GPP síťovými řezy pro vyhrazené železniční služby
- Podpora plynulé mobility a předávání spojení pro vysokorychlostní vlaky
- Spolupráce se staršími železničními signalizačními systémy (např. ETCS, CBTC)
- Rozšířené bezpečnostní mechanismy pro ochranu před kybernetickými hrozbami

## Související pojmy

- [FRMCS – Future Railway Mobile Communication System](/mobilnisite/slovnik/frmcs/)

## Definující specifikace

- **TS 22.289** (Rel-19) — 5G Rail Communication Service Requirements
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study

---

📖 **Anglický originál a plná specifikace:** [MTTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mttc/)
