---
slug: "easid"
url: "/mobilnisite/slovnik/easid/"
type: "slovnik"
title: "EASID – Edge Application Server Identification"
date: 2026-01-01
abbr: "EASID"
fullName: "Edge Application Server Identification"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/easid/"
summary: "Jedinečný identifikátor pro Edge Application Server (EAS) v edge computingu 3GPP. Umožňuje síti a aplikacím objevit, lokalizovat a směrovat provoz na správnou instanci edge výpočetního uzlu, což je kl"
---

EASID je jedinečný identifikátor pro Edge Application Server, který umožňuje síti a aplikacím objevit, lokalizovat a směrovat provoz na správnou instanci edge výpočetního uzlu.

## Popis

Edge Application Server Identification (EASID) je základní identifikátor definovaný v architektuře edge computingu 3GPP, konkrétně v rámci Edge Enabler Layer ([EEL](/mobilnisite/slovnik/eel/)) a Application Function ([AF](/mobilnisite/slovnik/af/)). Slouží jako jedinečný a jednoznačný štítek pro konkrétní instanci Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)). EAS je logická entita hostující aplikační logiku a data na okraji sítě, blíže k uživatelskému zařízení (UE). EASID se používá v procedurách objevování služeb a směrování provozu. Když aplikační klient (např. na UE) nebo Application Function (AF) potřebuje komunikovat s edge službou, může použít EASID, často ve spojení s dalšími parametry, jako je Data Network Name ([DNN](/mobilnisite/slovnik/dnn/)) nebo adresa Edge Configuration Server ([ECS](/mobilnisite/slovnik/ecs/)), k lokalizaci příslušné instance EAS.

Z architektonického hlediska EASID spravuje a využívá několik síťových funkcí. Edge Configuration Server (ECS) je klíčová komponenta, která udržuje mapování mezi EASID a skutečnými detaily nasazení EAS, jako je jeho IP adresa, port a podporovaná oblast služeb. Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) může také zpracovávat informace související s EASID při vystavování edge schopností externím Application Functions. Samotný identifikátor je strukturován tak, aby byl globálně jedinečný v kontextu edge nasazení mobilního operátora, čímž předchází konfliktům a zajišťuje přesné cílení služeb.

Během provozu je EASID klíčový pro proceduru objevování Edge Application Server. Klient nebo AF odešle žádost o objevení obsahující identitu požadované aplikace nebo požadavky na službu. Síť (např. prostřednictvím ECS) tuto žádost přeloží na konkrétní EASID a vrátí odpovídající informace o připojení. To umožňuje dynamické a efektivní směrování uživatelského provozu na optimální edge lokalitu, čímž se minimalizuje latence a zatížení backhaulového spoje. EASID také hraje roli v kontinuitě relace a mobilitě; když se UE pohybuje, síť může rozhodnout, zda má být pro probíhající službu vybrána nová, optimálnější instance EAS (s odlišným EASID).

## K čemu slouží

EASID byl vytvořen, aby řešil základní výzvu objevování služeb a směrování v distribuovaných prostředích edge computingu. Jak se sítě 3GPP vyvíjely pro podporu Multi-access Edge Computing ([MEC](/mobilnisite/slovnik/mec/)), aplikace mohly být nasazeny na více geograficky rozptýlených místech (např. centrální cloud, regionální datová centra, lokality na vzdáleném okraji sítě). Bez standardizovaného, jedinečného identifikátoru by nebylo možné, aby síť nebo klientské aplikace spolehlivě lokalizovaly a připojily se ke správné instanci edge služby. Předchozí přístupy spoléhaly na generická [DNS](/mobilnisite/slovnik/dns/) nebo názvy služeb, kterým chyběla granularita a kontextové povědomí potřebné pro mobilní edge scénáře, jako je zohlednění polohy uživatele, stavu sítě a stavu aplikace.

Zavedení EASID ve verzi 17 (Release 17) bylo motivováno potřebou škálovatelné a flexibilní edge architektury. Řeší problém nejednoznačných koncových bodů služeb. Například dvě různé továrny používající stejnou průmyslovou řídicí aplikaci by měly oddělené instance EAS, z nichž každá vyžaduje jedinečnou identifikaci pro správnou izolaci dat a lokalizované zpracování. EASID tuto jedinečnost poskytuje. Dále umožňuje pokročilé síťové schopnosti, jako je aplikací řízené směrování provozu a plynulá servisní mobilita, které jsou nezbytné pro případy použití kritické na latenci, jako jsou autonomní vozidla, rozšířená realita a analýza videa v reálném čase. Tvoří základ pro inteligentnější, aplikací řízený okraj sítě.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro instanci Edge Application Server
- Umožňuje přesné objevování a lokalizaci edge služeb
- Integruje se s Edge Configuration Server (ECS) pro překlad
- Podporuje zásady směrování provozu s ohledem na aplikaci
- Usnadňuje kontinuitu služby a mobilitu mezi edge lokalitami
- Používá se Network Exposure Function (NEF) pro žádosti o služby spouštěné AF

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [EASID na 3GPP Explorer](https://3gpp-explorer.com/glossary/easid/)
