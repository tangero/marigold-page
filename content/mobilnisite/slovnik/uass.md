---
slug: "uass"
url: "/mobilnisite/slovnik/uass/"
type: "slovnik"
title: "UASS – UAS Application Specific Server"
date: 2025-01-01
abbr: "UASS"
fullName: "UAS Application Specific Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uass/"
summary: "Síťový server poskytující aplikací specifické služby pro bezpilotní systémy (UAS). Podporuje integraci správy provozu UAS (UTM), umožňující funkce jako autorizace letu, sledování a řízení & ovládání p"
---

UASS je síťový server poskytující aplikací specifické služby pro bezpilotní systémy (Uncrewed Aerial Systems) a podporující integraci správy provozu UAS (UAS Traffic Management) pro funkce jako autorizace letu a sledování přes sítě 3GPP.

## Popis

[UAS](/mobilnisite/slovnik/uas/) Application Specific Server (UASS) je funkční entita definovaná v rámci architektury 3GPP pro podporu služeb bezpilotních systémů (UAS). Funguje jako aplikační server, který komunikuje se základní sítí 3GPP (konkrétně s funkcí Service Capability Exposure Function - [SCEF](/mobilnisite/slovnik/scef/) nebo Network Exposure Function - [NEF](/mobilnisite/slovnik/nef/)) a s externími systémy dodavatelů služeb UAS ([USS](/mobilnisite/slovnik/uss/)) nebo správy provozu UAS ([UTM](/mobilnisite/slovnik/utm/)). UASS poskytuje standardizované rozhraní pro aplikací specifické funkce UAS, umožňující bezpečné a efektivní poskytování služeb [UAV](/mobilnisite/slovnik/uav/) a jejich ovladačům.

Architektonicky je UASS součástí servisní vrstvy a je definován v kontextu podpory UAS systémem 3GPP. Komunikuje se základní sítí 3GPP přes referenční body, jako je N33 (mezi NEF a UASS) dle specifikace TS 29.257. To umožňuje UASS žádat o síťové služby (např. hlášení polohy, správu QoS, monitorování událostí) pro UAV a přijímat relevantní informace o expozici sítě. Samotný UASS může hostovat aplikační logiku pro služby jako identifikace UAS, geografické ohraničení, správa letové trasy a řešení nouzových situací.

Jeho role spočívá v abstrakci potřeb aplikací UAS do požadavků na síťové služby. Například UASS se může přihlásit k odběru událostí hlášení polohy pro konkrétní UAV ze sítě, tato data zpracovat a poskytnout je USS pro správu leteckého provozu. Zpracovává konverzi protokolů a správu relací vyžadovanou mezi světem aplikací (UTM/USS) a světem sítě 3GPP. Klíčové komponenty zahrnují servisní logiku, rozhraní k základní síti 3GPP (NEF/SCEF) a rozhraní k externím systémům UAS, zajišťující bezpečný a spolehlivý rámec pro poskytování služeb vzdušným vozidlům.

## K čemu slouží

UASS byl vytvořen, aby řešil potřebu standardizovaného, síťově integrovaného aplikačního serveru pro operace [UAS](/mobilnisite/slovnik/uas/) v rámci systémů 5G a novějších. Před jeho definicí musely aplikace UAS interagovat s mobilními sítěmi ad-hoc, nestandardizovaným způsobem, což činilo integraci komplexní a omezovalo možnost využívat pokročilé síťové schopnosti, jako je přesná lokalizace, komunikace s nízkou latencí nebo síťové segmentování pro služby dronů.

Jeho zavedení, počínaje Release 17, bylo motivováno rostoucím regulatorním a komerčním tlakem na systémy správy provozu UAS ([UTM](/mobilnisite/slovnik/utm/)). Sítě 3GPP jsou považovány za klíčový enabler pro operace dronů Beyond Visual Line of Sight (BVLOS), vyžadující spolehlivé řízení & ovládání a sledování. UASS poskytuje definovaný architektonický bod, kde může sídlit aplikační logika UAS, umožňující standardizovanou expozici síťových schopností 3GPP systémům UTM. Tím řeší problém fragmentované integrace a umožňuje škálovatelnou, bezpečnou a efektivní podporu různorodých aplikací UAS, jako je doručování zásilek, sledování nebo inspekce infrastruktury přes mobilní sítě.

## Klíčové vlastnosti

- Poskytuje standardizované rozhraní (N33) k základní síti 3GPP přes NEF/SCEF
- Hostuje aplikací specifickou logiku pro služby UAS (např. identifikace, autorizace letu)
- Usnadňuje integraci mezi sítěmi 3GPP a externími systémy správy provozu UAS (UTM)
- Může žádat o síťové služby, jako je hlášení polohy, monitorování událostí a QoS pro UAV
- Podporuje bezpečnou komunikaci a autorizaci služeb pro aplikace UAS
- Umožňuje správu síťových prostředků s ohledem na aplikace pro konektivitu UAV

## Související pojmy

- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [UAV – Uncrewed Aerial Vehicle](/mobilnisite/slovnik/uav/)
- [UTM – Uncrewed Aerial System Traffic Management](/mobilnisite/slovnik/utm/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications

---

📖 **Anglický originál a plná specifikace:** [UASS na 3GPP Explorer](https://3gpp-explorer.com/glossary/uass/)
