---
slug: "cca"
url: "/mobilnisite/slovnik/cca/"
type: "slovnik"
title: "CCA – Critical Communications Application"
date: 2026-01-01
abbr: "CCA"
fullName: "Critical Communications Application"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cca/"
summary: "Standardizovaný aplikační rámec umožňující služby hlasové, video a datové komunikace s požadavky na spolehlivost (mission-critical) v sítích 3GPP. Poskytuje funkční architekturu a rozhraní pro kritick"
---

CCA je standardizovaný aplikační rámec umožňující služby hlasové, video a datové komunikace s požadavky na spolehlivost (mission-critical) v sítích 3GPP pro organizace veřejné bezpečnosti a průmyslové organizace.

## Popis

Critical Communications Application (CCA) je komplexní rámec definovaný 3GPP pro podporu služeb s požadavky na spolehlivost (mission-critical) v sítích LTE a 5G. Poskytuje aplikační architekturu, funkční entity a referenční body nezbytné pro implementaci schopností profesionální mobilní rádiové sítě (PMR), konkrétně zaměřený na vývoj a náhradu starších systémů, jako je [TETRA](/mobilnisite/slovnik/tetra/) (Terrestrial Trunked Radio). Rámec CCA funguje v rámci širší architektury Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), rozhraní s funkcemi jádra sítě a klientskými aplikacemi na uživatelském zařízení (UE) pro zajištění zabezpečené skupinové komunikace, nouzových upozornění a prioritního přístupu.

Architektonicky se CCA skládá z několika klíčových funkčních komponent, které vzájemně komunikují prostřednictvím standardizovaných rozhraní. Aplikační server Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) zpracovává nastavení skupinových hovorů, řízení přístupu k vysílání (floor control) a distribuci médií pro hlasovou komunikaci. Servery Mission Critical Video ([MCVideo](/mobilnisite/slovnik/mcvideo/)) a Mission Critical Data (MCData) tyto schopnosti rozšiřují na přenos videa v reálném čase a datové zprávy. Tyto aplikační servery komunikují se základní jádrovou sítí 3GPP (EPC nebo 5GC) prostřednictvím standardizovaných referenčních bodů a využívají síťové schopnosti, jako je kvalita služeb (QoS), zpracování priorit a lokalizační služby. Rámec také zahrnuje funkce správy pro konfiguraci, předplatné a bezpečnostní politiky.

Z provozního hlediska CCA funguje tak, že vytváří zabezpečené relace mezi uživatelským zařízením (UE) a aplikačními servery, přičemž síť 3GPP poskytuje transportní vrstvu s odpovídajícími zárukami QoS. Když uživatel zahájí kritickou komunikaci (jako je hovor push-to-talk), klient CCA na zařízení se ověří u aplikačního serveru a vyžádá si prostředky od sítě. Síť uplatňuje politiky priority a přednostního přerušení na základě předplatného uživatele a kritické povahy komunikace. Toky médií jsou pak navázány se zaručenými charakteristikami šířky pásma a zpoždění, což zajišťuje spolehlivou komunikaci i v podmínkách přetížené sítě. Rámec podporuje jak provoz v síti (on-network), tak provoz mimo síť (off-network, přímá komunikace mezi zařízeními) prostřednictvím služeb Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)).

Úloha CCA v síti spočívá v poskytování standardizované, interoperabilní platformy pro kritickou komunikaci, kterou lze nasadit společně s komerčními mobilními službami. Umožňuje síťovým operátorům nabízet vyhrazené služby kritické komunikace pro orgány veřejné bezpečnosti, dopravní společnosti, energetické společnosti a průmyslové organizace. Díky využití komerčních sítí LTE a 5G poskytuje CCA významné výhody oproti starším systémům PMR, včetně vyšších datových rychlostí, lepší spektrální účinnosti a integrace s širokopásmovými aplikacemi. Rámec také podporuje regulatorní požadavky na služby tísňového volání a reakci na katastrofy prostřednictvím funkcí, jako je prioritní přístup, správa skupin a lokalizační služby.

## K čemu slouží

CCA bylo vytvořeno za účelem řešení rostoucí potřeby moderních systémů kritické komunikace s podporou širokopásmového přenosu, které by mohly nahradit zastaralé technologie, jako jsou [TETRA](/mobilnisite/slovnik/tetra/) a [P25](/mobilnisite/slovnik/p25/). Tyto starší systémy, ačkoli byly spolehlivé pro hlasovou komunikaci, postrádaly šířku pásma a flexibilitu potřebnou pro moderní aplikace veřejné bezpečnosti a průmyslové aplikace vyžadující video, data a vysokorychlostní mobilitu. Mezi omezení TETRA patřily úzkopásmové schopnosti (typicky kanály o šířce 25 kHz), omezené datové rychlosti (až 28,8 kbps) a proprietární implementace, které bránily interoperabilitě mezi různými dodavateli a regiony. Jak technologie LTE dospívala, bylo zřejmé, že komerční mobilní sítě by mohly poskytnout nákladově efektivnější a schopnější platformu pro kritickou komunikaci, pokud by byly standardizovány odpovídající aplikační rámce.

Primární motivací pro vývoj CCA bylo umožnit organizacím veřejné bezpečnosti a provozovatelům kritické infrastruktury využívat investice do komerčních mobilních sítí při zachování spolehlivosti, zabezpečení a funkčnosti požadované pro operace s požadavky na spolehlivost (mission-critical). Před standardizací CCA se pokusy o využití komerčních sítí pro kritickou komunikaci spoléhaly na proprietární řešení, kterým chyběla interoperabilita a která nemohla garantovat potřebné výkonnostní charakteristiky během mimořádných událostí. Standardizační úsilí 3GPP si kladlo za cíl vytvořit globálně uznávaný rámec, který by umožnil výrobcům zařízení, síťovým operátorům a vývojářům aplikací vytvářet kompatibilní řešení, což by podpořilo úspory z rozsahu a podnítilo inovace na trhu s kritickou komunikací.

CCA řeší několik klíčových problémů: poskytuje migrační cestu ze starších systémů PMR na širokopásmové sítě, umožňuje konvergenci více aplikací kritické komunikace (hlas, video, data) na jedné platformě a zajišťuje, že kritická komunikace získá odpovídající prioritu a prostředky ve sdílených komerčních sítích. Rámec také řeší regulatorní požadavky na komunikaci služeb tísňového volání, včetně podpory zákonného odposlechu, lokalizačních služeb a prioritního přístupu při přetížení sítě. Standardizací těchto schopností CCA umožňuje síťovým operátorům nabízet služby kritické komunikace jako spravovanou službu, což snižuje kapitálové a provozní náklady pro organizace veřejné bezpečnosti ve srovnání s údržbou vyhrazených sítí PMR.

## Klíčové vlastnosti

- Standardizovaný aplikační rámec pro služby s požadavky na spolehlivost (mission-critical) v sítích LTE/5G
- Podpora hlasové komunikace Mission Critical Push To Talk (MCPTT)
- Schopnosti Mission Critical Video (MCVideo) a Mission Critical Data (MCData)
- Integrace s jádrovou sítí 3GPP pro QoS, prioritu a zabezpečení
- Správa skupin a dynamické přeskupování pro reakci na incidenty
- Podpora provozu v síti (on-network) a mimo síť (off-network, ProSe)

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)
- [TETRA – Trans European Trunked RAdio](/mobilnisite/slovnik/tetra/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 32.825** (Rel-10) — Study on Rc Reference Point for ABMF
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [CCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cca/)
