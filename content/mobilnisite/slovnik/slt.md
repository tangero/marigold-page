---
slug: "slt"
url: "/mobilnisite/slovnik/slt/"
type: "slovnik"
title: "SLT – Service List Table"
date: 2025-01-01
abbr: "SLT"
fullName: "Service List Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/slt/"
summary: "Datová struktura používaná ve službě Multimedia Broadcast Multicast Service (MBMS) k poskytnutí seznamu dostupných vysílacích/multicastových služeb. Slouží jako elektronický programový průvodce, který"
---

SLT je datová struktura používaná v MBMS, která slouží jako elektronický programový průvodce a uvádí dostupné vysílací/multicastové služby, aby umožnila uživatelskému zařízení (UE) tyto služby v určité oblasti objevit a vybrat.

## Popis

Service List Table (SLT) je klíčovou součástí architektury služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) podle 3GPP, konkrétně v rámci frameworku evolved MBMS (eMBMS) a Further evolved MBMS (FeMBMS). Jedná se o strukturovanou tabulku, která je typicky doručována prostřednictvím protokolu [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) po nosiči MBMS a obsahuje metadata a přístupové informace pro všechny služby MBMS dostupné v dané geografické oblasti, známé jako servisní oblast. SLT poskytuje uživatelskému zařízení (UE) potřebné informace k objevení, výběru a připojení se k vysílacím službám bez nutnosti předchozí konfigurace nebo signalizace typu unicast pro každou službu.

Z architektonického hlediska je SLT generována a spravována Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťová entita zodpovědná za poskytování služeb MBMS. Tabulka je poté doručena přes vysílací kanál všem UE v servisní oblasti. Každá položka v SLT odpovídá jedné službě MBMS a zahrnuje kritické parametry, jako je název služby, jedinečný identifikátor služby, přidružený Temporary Mobile Group Identity ([TMGI](/mobilnisite/slovnik/tmgi/)), IP multicast adresu a port pro datový tok služby, informace o oznámení služby a deskriptory pro typ obsahu služby (např. audio, video, aplikační data).

Princip fungování zahrnuje, že UE, když je nakonfigurováno pro příjem MBMS, nejprve získá řídicí informace pro fyzickou vrstvu MBMS. Poté přijme a zpracuje SLT, která je periodicky vysílána. Čtením SLT může UE uživateli zobrazit seznam dostupných služeb (jako průvodce programem). Když uživatel službu vybere, UE použije přístupové informace z SLT (jako TMGI a IP multicast detaily) ke konfiguraci svých nižších vrstev pro připojení ke správné multicast skupině a zahájení příjmu datového toku služby. Role SLT spočívá v oddělení objevování služeb od jejich konzumace, což umožňuje efektivní, sítí řízené oznamování služeb obrovskému počtu zařízení současně, což je klíčové pro vysílací scénáře.

## K čemu slouží

SLT byla vyvinuta k řešení výzvy škálovatelného objevování služeb ve vysílacích a multicastových sítích. Před její standardizací se objevování služeb pro skupinově orientované služby často spoléhalo na unicastové metody nebo mechanismy mimo pásmo, které se neškálují efektivně, když potenciálně miliony zařízení potřebují zjistit informace o dostupných službách. To byla významná překážka pro nasazení masových vysílacích služeb, jako je mobilní [TV](/mobilnisite/slovnik/tv/).

Její zavedení, zvláště zdokonalené v kontextu eMBMS a FeMBMS, bylo motivováno potřebou lehkého mechanismu oznamování služeb v pásmu. SLT řeší problém, jak může UE, zejména ta v klidovém režimu nebo bez navázaného unicastového spojení, efektivně zjistit, jaké vysílací služby jsou nabízeny. Poskytuje standardizovaný, sítí řízený "jídelní lístek" služeb, který zjednodušuje uživatelský zážitek a snižuje signalizační zátěž sítě. Tato schopnost je klíčová pro systémy veřejného varování, vysílání živých událostí a doručování obsahu velkému publiku, kde je vyžadováno okamžité a rozšířené povědomí o službách.

## Klíčové vlastnosti

- Poskytuje výpis všech dostupných služeb MBMS v rámci vysílací servisní oblasti.
- Doručována v pásmu přes vysílací nosič MBMS pomocí FLUTE/ALC.
- Obsahuje přístupové informace pro každou službu (TMGI, IP multicast adresa/port).
- Zahrnuje metadata služby (název, popis, typ obsahu) pro prezentaci uživateli.
- Umožňuje efektivní, sítí řízené objevování služeb pro masivní počty UE.
- Podporuje výběr a připojení ke službě bez nutnosti unicastové signalizace pro objevování.

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [SLT na 3GPP Explorer](https://3gpp-explorer.com/glossary/slt/)
