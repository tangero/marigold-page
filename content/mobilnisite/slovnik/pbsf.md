---
slug: "pbsf"
url: "/mobilnisite/slovnik/pbsf/"
type: "slovnik"
title: "PBSF – Personal Broadcast Service Function"
date: 2025-01-01
abbr: "PBSF"
fullName: "Personal Broadcast Service Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbsf/"
summary: "Funkce jádra sítě v architektuře 3GPP odpovědná za správu a řízení relací služby Personal Broadcast Service (PBS). Zajišťuje servisní logiku, správu skupin, autorizaci vysílatele a interakci s BM-SC p"
---

PBSF je funkce jádra sítě podle 3GPP, která spravuje relace služby Personal Broadcast Service, zajišťuje servisní logiku, správu skupin, autorizaci vysílatele a interakci s BM-SC pro doručování obsahu.

## Popis

Personal Broadcast Service Function (PBSF) je logická funkce sítě specifikovaná ve standardech 3GPP, která poskytuje řídicí rovinu a servisní logiku pro službu Personal Broadcast Service. Působí jako mozek [PBS](/mobilnisite/slovnik/pbs/), rozhraním komunikuje s uživatelem, systémem pro vysílání/multicastové doručování a dalšími funkcemi jádra sítě. Z architektonického hlediska může být PBSF implementována jako samostatný uzel nebo integrována v aplikačním serveru, často se nachází ve servisní vrstvě sítě a potenciálně komunikuje s IP Multimedia Subsystem (IMS). Jejím hlavním úkolem je spravovat životní cyklus osobní vysílací relace od zahájení do ukončení.

Fungování PBSF zahrnuje několik klíčových procedur. Když uživatel požádá o zahájení vysílání, PBSF autentizuje vysílatele a ověří jeho profil předplatného pro oprávnění k PBS. Spravuje vytváření, úpravy a rozpuštění vysílacích skupin a udržuje seznamy členů. Pro doručování založené na [MBMS](/mobilnisite/slovnik/mbms/) PBSF úzce spolupracuje s Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)). Spouští v BM-SC alokaci prostředků přenosu MBMS, definici oblasti služby a zahájení relace doručování obsahu. PBSF také zajišťuje oznámení služby, informuje potenciální příjemce o dostupných osobních vysíláních, často prostřednictvím mechanismů jako MBMS User Service Discovery nebo prostřednictvím oznámení na aplikační úrovni.

V rámci širšího síťového ekosystému PBSF komunikuje s několika entitami. Spojuje se s 5G Core (5GC) nebo EPC pro uživatelskou autentizaci a řízení politik (přes [PCF](/mobilnisite/slovnik/pcf/)) a s účtovacími systémy (např. [CHF](/mobilnisite/slovnik/chf/)) pro generování účtovacích událostí. Poskytuje aplikační programové rozhraní ([API](/mobilnisite/slovnik/api/)) nebo referenční bod pro klientskou aplikaci na UE. PBSF vynucuje bezpečnostní politiky, například autorizuje, kteří uživatelé se mohou připojit ke konkrétní vysílací skupině, a může spravovat šifrovací klíče obsahu. Centralizací této logiky PBSF abstrahuje složitost podkladového vysílacího přenosu (MBMS/[MBS](/mobilnisite/slovnik/mbs/)) od servisní aplikace a poskytuje standardizovaný způsob nabízení funkcí osobního vysílání napříč různými generacemi sítí a nasazeními.

## K čemu slouží

PBSF byla vytvořena, aby poskytla standardizovanou, síťově řízenou vrstvu servisní logiky pro službu Personal Broadcast Service, a zajistila tak konzistentní chování, bezpečnost a interoperabilitu napříč různými sítěmi operátorů a výrobci zařízení. Bez standardizované funkce, jako je PBSF, by byla implementace [PBS](/mobilnisite/slovnik/pbs/) roztříštěná a závislá na proprietární logice aplikačního serveru, což by bránilo roamingu, poskytování služeb mezi operátory a vývoji univerzálního ekosystému klientů. Řeší problém, jak integrovat uživatelem iniciovanou, skupinově orientovanou vysílací službu do řízeného, zabezpečeného a účtovatelného rámce sítě 3GPP.

K jejímu vytvoření vedla potřeba dát síťovým operátorům kontrolu a přehled nad funkcí PBS. PBSF umožňuje operátorům uplatňovat konzistentní politiky (např. kdo může vysílat, maximální dobu trvání relace, povolené oblasti služeb), implementovat přesné účtování (např. na základě délky trvání, objemu dat nebo velikosti skupiny) a zajistit správnou integraci služby se stávajícími síťovými funkcemi pro autentizaci a správu prostředků. Slouží jako kotvící bod, který překládá požadavky služby na vysoké úrovni („vysílat mé skupině“) do konkrétních technických příkazů potřebných ke konfiguraci BM-SC a RAN pro zřízení přenosu MBMS, čímž řeší integrační mezeru mezi konceptem služby a podkladovou infrastrukturou pro vysílací doručování.

## Klíčové vlastnosti

- Spravuje kompletní životní cyklus relací služby Personal Broadcast Service
- Zajišťuje autentizaci, autorizaci a poskytování služby pro vysílatele
- Řídí členství ve skupině, včetně vytváření, úprav a správy předplatného
- Komunikuje s BM-SC pro zahájení a řízení zřizování přenosu MBMS/MBS pro distribuci obsahu
- Řídí mechanismy oznamování a zjišťování služby pro příjemce
- Integruje se s funkcemi řízení politik (PCF), účtování (CHF) a zabezpečení jádra sítě

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [PBSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbsf/)
