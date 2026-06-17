---
slug: "ehe"
url: "/mobilnisite/slovnik/ehe/"
type: "slovnik"
title: "EHE – Edge Hosting Environment"
date: 2026-01-01
abbr: "EHE"
fullName: "Edge Hosting Environment"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ehe/"
summary: "EHE je standardizovaný rámec v 3GPP pro nasazování a správu aplikací na síťové hraně, blízko uživatelů. Umožňuje služby s nízkou latencí, edge computing a síťovou expozici tím, že poskytuje konzistent"
---

EHE je standardizovaný 3GPP rámec pro nasazování a správu aplikací na síťové hraně, který umožňuje služby s nízkou latencí a poskytuje konzistentní hostitelské prostředí napříč sítěmi operátorů.

## Popis

Edge Hosting Environment (EHE) je architektonický rámec a soubor schopností definovaný 3GPP pro podporu nasazování, provádění a správy aplikací a síťových funkcí na hraně sítě operátora. Je součástí širšího ekosystému edge computingu v 5G, často spojovaného s Multi-access Edge Computing ([MEC](/mobilnisite/slovnik/mec/)). EHE poskytuje standardizované prostředí, které abstrahuje podkladové síťové a hardwarové zdroje, což umožňuje poskytovatelům aplikací nasazovat své služby konzistentním způsobem v různých sítích operátorů. Architektonicky je EHE typicky realizováno v rámci Edge Application Server nebo Edge Enabler Server, který hostuje toto prostředí a komunikuje se základními síťovými funkcemi, jako je Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)).

EHE funguje tak, že nabízí sadu služeb a [API](/mobilnisite/slovnik/api/) pro edge aplikace. Ty zahrnují správu životního cyklu (připojení, vytvoření instance, ukončení), pravidla pro směrování provozu (traffic steering) k nasměrování relevantních dat uživatelské roviny do aplikace, přístup k informacím o stavu sítě a uživatele (s řádnou autorizací) a konektivitu k dalším síťovým funkcím. Mezi klíčové komponenty patří EHE Platforma, která poskytuje běhové prostředí, a EHE Management System, který zajišťuje orchestraci a vynucování politik. Toto prostředí zajišťuje, že aplikace mohou dynamicky využívat síťové schopnosti, jako jsou lokalizační služby, správa šířky pásma a vynucování kvality služeb (QoS).

Jeho úlohou v síti je překlenout propast mezi telekomunikační infrastrukturou a vývojáři aplikací třetích stran. Tím, že poskytuje standardizované hostitelské prostředí na hraně, umožňuje aplikace s ultra nízkou latencí, snižuje zpětný provoz (backhaul) a umožňuje kontextově závislé poskytování služeb. EHE je nedílnou součástí naplnění plného potenciálu 5G pro případy užití, jako je rozšířená realita, průmyslová automatizace a analýza videa v reálném čase, kde musí zpracování probíhat geograficky blízko koncového uživatele nebo zdroje dat, aby byly splněny požadavky na výkon.

## K čemu slouží

EHE bylo vytvořeno za účelem řešení fragmentace a složitosti při nasazování edge aplikací napříč různorodými sítěmi telekomunikačních operátorů. Před standardizací poskytovaly iniciativy edge computingu, jako je [ETSI](/mobilnisite/slovnik/etsi/) [MEC](/mobilnisite/slovnik/mec/), rámce, ale plná integrace se základními mobilními sítěmi 3GPP vyžadovala proprietární řešení. To ztěžovalo vývojářům aplikací vytvářet služby, které by mohly bezproblémově běžet na edge infrastruktuře libovolného operátora. EHE standardizuje rozhraní mezi aplikacemi a síťovou hranou, čímž řeší problém závislosti na konkrétním dodavateli a umožňuje škálovatelné ekosystémy edge služeb.

Zavedeno v 3GPP Release 17 jako součást podpůrných prostředků pro edge computing, vychází motivace EHE z potřeby bezpečně a efektivně zpřístupnit síťové schopnosti autorizovaným aplikacím. Umožňuje operátorům monetizovat jejich edge infrastrukturu tím, že nabízejí platformu pro služby třetích stran, při zachování kontroly nad síťovými zdroji a soukromím uživatelů. EHE řeší omezení předchozích ad-hoc přístupů definováním jasných architektonických rolí, referenčních bodů a procedur pro správu životního cyklu aplikací, ovlivňování provozu a zpřístupňování síťových informací, čímž urychluje adopci edge computingu v 5G.

## Klíčové vlastnosti

- Standardizovaná správa životního cyklu aplikací (připojení, vytvoření instance, ukončení)
- Schopnosti směrování provozu (traffic steering) k nasměrování dat uživatelské roviny do edge aplikací
- Bezpečné zpřístupnění stavu sítě a uživatelských informací prostřednictvím API
- Integrace se základními síťovými funkcemi, jako je NEF a UPF
- Podpora pro přenos kontextu aplikace a kontinuitu služeb
- Vynucování politik pro využití zdrojů a řízení přístupu

## Související pojmy

- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 29.591** (Rel-19) — 5G NEF Southbound Services Stage 3
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [EHE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ehe/)
