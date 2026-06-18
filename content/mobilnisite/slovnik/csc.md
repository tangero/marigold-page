---
slug: "csc"
url: "/mobilnisite/slovnik/csc/"
type: "slovnik"
title: "CSC – Communication Service Customer"
date: 2026-01-01
abbr: "CSC"
fullName: "Communication Service Customer"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/csc/"
summary: "Komunikační zákazník služeb (CSC) je koncept řízení v 3GPP představující entitu, která od síťového operátora nebo poskytovatele služeb nakupuje, spotřebovává a spravuje komunikační služby. Jde o klíčo"
---

CSC je řídicí entita 3GPP, která od síťového operátora nebo poskytovatele služeb nakupuje, spotřebovává a spravuje komunikační služby.

## Popis

Komunikační zákazník služeb (CSC) je funkční role definovaná v rámci architektury řízení 3GPP, konkrétně v kontextu frameworku Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) a síťového řezání. Představuje organizační entitu (kterou může být podnik, hráč vertikálního průmyslu, virtuální operátor nebo dokonce další poskytovatel služeb), která má komerční dohodu s Poskytovatelem komunikačních služeb ([CSP](/mobilnisite/slovnik/csp/)) ke spotřebě jedné nebo více komunikačních služeb. CSC není koncovým uživatelským zařízením, ale administrativní a obchodní entitou odpovědnou za servisní vztah.

Architektonicky CSC komunikuje s řídicími systémy CSP prostřednictvím standardizovaných referenčních bodů, primárně Rozhraní služeb orientovaných na zákazníka (CnF). Prostřednictvím tohoto rozhraní může CSC žádat o služby, jako je vytvoření instance síťového řezu, upravovat parametry služeb, monitorovat výkon služeb a přijímat hlášení o poruchách a výkonu. Doména CSC zahrnuje její vlastní řídicí systémy (CSC Management System), které se mohou integrovat s Business Support Systems ([BSS](/mobilnisite/slovnik/bss/)) a Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)) CSP. Toto oddělení umožňuje CSP zpřístupnit zákazníkovi řízenou sadu řídicích schopností, což podporuje samoobslužnost a automatizaci.

Role CSC je ústřední pro paradigma síťového řezání definované od 3GPP Release 15 dále. Když CSC (např. automobilová společnost) potřebuje vyhrazený síťový řez pro služby spojených vozidel, odešle prostřednictvím CnF žádost o službu. Tato žádost, obsahující Profil služby síťového řezu, spustí v orchestračních systémech CSP proces vytvoření potřebných síťových funkcí napříč RAN, přenosovou sítí a core sítí k naplnění smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). CSC pak získává průběžný přehled o výkonu řezu, včetně klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je latence, propustnost a dostupnost, což umožňuje proaktivní správu kvality uživatelského zážitku jejich aplikace.

Klíčovými komponentami v ekosystému CSC jsou CSC Management System, který formuluje žádosti o služby a spotřebovává data o zajištění služeb, a Service Management Function ([SMF](/mobilnisite/slovnik/smf/)) v doméně CSP, která tyto žádosti zpracovává. Vztah je upraven Smlouvou o úrovni služeb (SLA), která definuje technické výkonnostní cíle, obchodní podmínky a povinnosti vykazování. Koncept CSC umožňuje jasné vymezení mezi odpovědnostmi poskytovatele za správu sítě a odpovědnostmi zákazníka za správu služeb, což je nezbytné pro komplexní služby 5G a budoucích sítí řízené SLA.

## K čemu slouží

Koncept CSC byl zaveden, aby formalizoval a standardizoval vztah business-to-business ([B2B](/mobilnisite/slovnik/b2b/)) a zákazník–poskytovatel v telekomunikačních službách, zejména s tím, jak se sítě vyvíjely k podpoře různorodých vertikálních průmyslů s 5G. Před jeho formální definicí byla rozhraní pro správu služeb často proprietární, což omezovalo automatizaci a bránilo škálovatelnému připojování podnikových zákazníků. Model CSC řeší potřebu standardizovaného, automatizovaného a programovatelného rozhraní, prostřednictvím kterého mohou zákazníci přímo interagovat s možnostmi sítě poskytovatele.

Historicky se podnikové služby zřizovaly prostřednictvím manuálních procesů založených na tikatech s omezenou viditelností zákazníka do výkonu sítě. Posun k virtualizaci sítí, cloud-nativním principům a síťovému řezání vyžadoval dynamičtější, API řízený přístup. Role CSC spolu s rozhraním CnF byly vytvořeny, aby toto vyřešily tím, že umožnily správu služeb bez zásahu obsluhy. Umožňuje vertikálním zákazníkům (ve výrobě, zdravotnictví, logistice atd.) objednávat, konfigurovat a monitorovat jejich vyhrazené síťové služby (řezy) na požádání, podobně jako při spotřebě cloudových výpočetních zdrojů. To je zásadní změna oproti tradičnímu monolitickému modelu síťových služeb typu "jedna velikost pro všechny".

Dále framework CSC podporuje monetizaci sítí 5G tím, že poskytuje potřebnou architekturu řízení pro obchodní modely typu Síť-jako-sluzba (NaaS). Umožňuje Poskytovatelům komunikačních služeb zpřístupnit síťové schopnosti jako spravovatelné, fakturovatelné služby s jasnými hranicemi vlastnictví a odpovědnosti. To umožňuje podnikům inovovat integrací garantovaného síťového výkonu přímo do jejich operační technologie a aplikací, čímž pohání digitální transformaci průmyslů.

## Klíčové vlastnosti

- Představuje administrativní entitu spotřebovávající služby prostřednictvím komerční dohody
- Komunikuje s řídicím systémem poskytovatele prostřednictvím standardizovaného Rozhraní služeb orientovaných na zákazníka (CnF)
- Ústřední role při žádání o, úpravě a ukončování instancí síťových řezů
- Přijímá data o zajištění služeb, hlášení o výkonu a oznámení o poruchách
- Umožňuje zákaznickou samoobslužnost a automatizaci pro správu životního cyklu služeb
- Zásadní pro implementaci modelů B2B a Síť-jako-sluzba řízených SLA

## Definující specifikace

- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.557** (Rel-19) — Management of Non-Public Networks (NPN)
- **TS 28.805** (Rel-16) — Management of Communication Services in 5G
- **TR 28.812** (Rel-17) — Study on Intent Driven Management Services
- **TR 28.828** (Rel-18) — Charging Aspects for Non-Public Networks
- **TR 28.836** (Rel-18) — Technical Report on Intent Driven Management
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TR 32.847** (Rel-18) — Technical Report
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/csc/)
