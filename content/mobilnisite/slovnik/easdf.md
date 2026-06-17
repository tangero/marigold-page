---
slug: "easdf"
url: "/mobilnisite/slovnik/easdf/"
type: "slovnik"
title: "EASDF – Edge Application Server Discovery Function"
date: 2026-01-01
abbr: "EASDF"
fullName: "Edge Application Server Discovery Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/easdf/"
summary: "Funkce pro objevování serverů edge aplikací (EASDF) je funkce jádra sítě 5G, která pomáhá uživatelskému zařízení (UE) objevovat a vybírat optimální servery edge aplikací (Edge Application Servers). Po"
---

EASDF je funkce jádra sítě 5G, která pomáhá uživatelskému zařízení (UE) objevovat a vybírat optimální servery edge aplikací (Edge Application Servers) tím, že poskytuje překlad založený na DNS přizpůsobený pro edge computing.

## Popis

Funkce pro objevování serverů edge aplikací (EASDF) je specializovaná síťová funkce zavedená ve specifikaci 3GPP Release 17 pro vylepšení edge computingu v systémech 5G. Jejím hlavním úkolem je usnadnit objevování a výběr serverů edge aplikací ([EAS](/mobilnisite/slovnik/eas/)) uživatelským zařízením (UE) nebo jinými síťovými funkcemi. EASDF funguje jako server nebo proxy [DNS](/mobilnisite/slovnik/dns/) (Domain Name System), který má přehled o topologii sítě, poloze UE a umístění nasazení EAS. Když se UE pokusí přistoupit k edge aplikaci pomocí doménového jména, EASDF zachytí dotaz DNS a vrátí IP adresu nejvhodnější instance EAS, typicky té nejbližší k UE, aby se minimalizovala latence.

Z architektonického hlediska je EASDF součástí uživatelské roviny jádra sítě 5G nebo může být nasazena jako samostatná funkce komunikující s řídicí rovinou. Integruje se s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a funkcí vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)), aby získala politiky a kontextové informace ovlivňující výběr EAS. Mezi klíčové komponenty patří logika překladu DNS, databáze nebo rozhraní k informacím o dostupnosti a umístění EAS a mechanismy vynucování politik. EASDF funguje tak, že přijímá dotaz DNS od UE (který je k ní často směrován prostřednictvím politiky výběru trasy UE (URSP) nebo konfigurací lokálního breakoutu). Poté použije výběrová kritéria, jako je aktuální poloha UE, vytížení EAS, stav sítě a profily účastníků, aby zvolila optimální EAS. Přeložená IP adresa je vrácena UE, které následně naváže přímé spojení s vybraným EAS pro přenos dat aplikace.

Jeho provoz zahrnuje úzkou koordinaci s dalšími systémy 5G. EASDF může být informacemi o EAS zásobována prostřednictvím systémů správy nebo dynamicky pomocí rozhraní k funkci úložiště síťových funkcí ([NRF](/mobilnisite/slovnik/nrf/)). V provozu umožňuje dynamické a efektivní směrování provozu k edge prostředkům. Například pro aplikaci hry citlivou na latenci EASDF zajistí, že se UE připojí k hernímu serveru v nedalekém edge datovém centru, a ne ke vzdálenému centrálnímu cloudu. Jeho role je klíčová v prostředích s více edge lokalitami, kde je více instancí EAS nasazeno v různých geografických bodech přítomnosti, protože poskytuje inteligenci pro směrování uživatelů k nejlepší instanci na základě aktuálních síťových a servisních podmínek.

## K čemu slouží

EASDF byla vytvořena, aby vyřešila problém efektivního objevování a připojování k nejvhodnějšímu serveru edge aplikací v distribuovaném prostředí edge computingu. Před jejím zavedením byly mechanismy pro objevování edge často proprietární, postrádaly standardizaci nebo se spoléhaly na základní [DNS](/mobilnisite/slovnik/dns/), které není síťově informované. To vedlo k suboptimálnímu směrování, kdy mohlo být UE nasměrováno na vzdálený [EAS](/mobilnisite/slovnik/eas/), přestože byl dostupný bližší, což rušilo výhody nízké latence edge computingu. Rozmístění edge nasazení v 5G, poháněné aplikacemi jako autonomní vozidla, průmyslový IoT a rozšířená realita, si vyžádalo standardizované, síťově integrované řešení pro objevování.

Hlavním problémem, který EASDF řeší, je inteligentní výběr edge prostředků řízený politikami. Zajišťuje, že edge computing splní svůj slib nízké latence a vysoké propustnosti tím, že dynamicky směruje uživatele k optimálnímu EAS na základě aktuálních síťových podmínek. To je obzvláště důležité pro mobilní uživatele, protože se jejich poloha mění a nejlepší výběr EAS se může podle toho měnit. EASDF také řeší problém škálovatelnosti a správy ve velkých edge nasazeních tím, že poskytuje centralizovaný bod pro objevování, který může být aktualizován o nové instance EAS a jejich schopnosti.

Historická motivace vychází z práce 3GPP na architektuře edge computingu (EDGEAPP) v dřívějších vydáních, která definovala EAS, ale postrádala standardizovaný mechanismus objevování. EASDF tuto mezeru zaplňuje a dokončuje rámec edge computingu přidáním klíčového řídicího prvku. Umožňuje operátorům nabízet edge computing jako bezproblémovou službu, kde mohou být aplikace nasazeny na okraji sítě bez nutnosti, aby koncoví uživatelé nebo poskytovatelé aplikací spravovali složité podrobnosti připojení. Tato standardizace podporuje růst ekosystému, protože umožňuje vývojářům aplikací spoléhat se na konzistentní metodu pro objevování edge služeb napříč různými síťmi operátorů.

## Klíčové vlastnosti

- Poskytuje objevování a výběr serverů edge aplikací (EAS) založené na DNS
- Pro optimální výběr využívá polohu UE, topologii sítě a vytížení EAS
- Integruje se s řízením politik jádra 5G (PCF) pro překlad EAS založený na pravidlech
- Podporuje dynamické aktualizace informací o dostupnosti a umístění EAS
- Umožňuje přístup k aplikacím s nízkou latencí směrováním provozu k nejbližšímu edge
- Usnadňuje mobilitu a kontinuitu služeb při pohybu UE přes různé edge zóny

## Související pojmy

- [EAS – Enterprise Application Server](/mobilnisite/slovnik/eas/)
- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.556** (Rel-19) — EASDF Service Based Interface Protocol
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [EASDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/easdf/)
