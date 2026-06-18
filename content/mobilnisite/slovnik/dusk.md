---
slug: "dusk"
url: "/mobilnisite/slovnik/dusk/"
type: "slovnik"
title: "DUSK – Discovery User Scrambling Key"
date: 2025-01-01
abbr: "DUSK"
fullName: "Discovery User Scrambling Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dusk/"
summary: "Kryptografický klíč používaný ke skramblování a zabezpečení zjišťovacích zpráv ve službách blízkosti (ProSe). Zajišťuje, že pouze autorizovaná zařízení mohou dekódovat zjišťovací informace, čímž chrán"
---

DUSK je kryptografický klíč používaný ke skramblování a zabezpečení zjišťovacích zpráv ve službách blízkosti (Proximity Services), který zajišťuje, že pouze autorizovaná zařízení mohou informace dekódovat, čímž chrání soukromí a brání neoprávněnému sledování.

## Popis

Discovery User Scrambling Key (DUSK) je základní bezpečnostní komponenta v architektuře služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) dle 3GPP, konkrétně pro funkci přímého zjišťování (Direct Discovery). Jedná se o symetrický kryptografický klíč odvozený z kořenového klíče, ProSe Key (PK), který sám je poskytován funkcí ProSe v síti. Primární úlohou DUSK je poskytnout důvěrnost a integritu ProSe Application Code, což je identifikátor vysílaný zařízením, aby oznámilo svou přítomnost a služby jiným blízkým zařízením. Proces skramblování zahrnuje aplikaci DUSK na ProSe Application Code pomocí kryptografického algoritmu před jeho vysíláním přes referenční bod PC5 (přímé rozhraní mezi zařízeními). Tím se kód přemění pro jakéhokoli odposlouchávajícího na skramblovaný, nesrozumitelný řetězec.

Při přijetí skramblované zjišťovací zprávy autorizované zjišťující zařízení, které musí mít také odpovídající DUSK (získaný síťovou provizí pro omezené zjišťování nebo odvozený pro otevřené zjišťování), aplikuje proces deskramblování. Tento proces obrátí skramblování a obnoví původní ProSe Application Code. Držení správného DUSK slouží jako důkaz autorizace pro zjištění dané konkrétní služby. Správu klíče pro DUSK zajišťuje funkce ProSe, která klíč nebo potřebný materiál pro odvození klíče bezpečně doručuje do UE přes rozhraní LTE-Uu nebo NR-Uu, čímž zajišťuje, že se nikdy přímo nepřenáší přes nezabezpečené vzdušné rozhraní PC5.

Z architektonického hlediska DUSK funguje v rámci protokolového zásobníku ProSe, rozhraní s aplikační vrstvou ProSe a bezpečnostní podvrstvou. Jeho generování a životní cyklus jsou svázány s předplatným ProSe a konkrétním ProSe Application ID. Použití DUSK je klíčové pro různé modely zjišťování: v otevřeném zjišťování (Open Discovery) může být použit společný DUSK, zatímco v omezeném zjišťování (Restricted Discovery) zajišťují jedinečné nebo skupinově specifické DUSK, že zjišťování je omezeno na předem autorizovanou skupinu zařízení. Tento mechanismus účinně odděluje vysílaný identifikátor od trvalé identity uživatele a přidává zásadní vrstvu ochrany soukromí.

## K čemu slouží

DUSK byl zaveden, aby řešil kritické bezpečnostní a soukromostní výzvy vlastní zjišťování mezi zařízeními, což je základním kamenem služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) standardizovaných od 3GPP Release 12. Bez takového mechanismu by zařízení vysílající zjišťovací kódy v čitelné podobě byla zranitelná vůči narušení soukromí, protože škodliví aktéři by mohli sledovat polohu a vazby uživatele v čase monitorováním těchto trvalých identifikátorů. Dále by byly snadné útoky falšováním identity, což by umožnilo jakémukoli zařízení vydávat se za legitimní službu.

Vytvoření DUSK bylo motivováno potřebou umožnit důvěryhodné zjišťování v komerčních scénářích a scénářích veřejné bezpečnosti. Předchozí ad-hoc metody zjišťování, jako názvy zařízení Bluetooth, nenabízely standardizovanou bezpečnost. DUSK poskytuje standardizovaný, sítí podporovaný bezpečnostní rámec, který umožňuje jak otevřené, tak omezené modely zjišťování. Řeší problém, jak veřejně oznamovat službu, a zároveň kontrolovat, kdo oznámení může porozumět, čímž umožňuje nové případy užití, jako je sociální síťování, místní reklama nebo komunikace týmů veřejné bezpečnosti, aniž by byla ohrožena soukromí uživatelů nebo bezpečnost sítě.

## Klíčové vlastnosti

- Poskytuje důvěrnost pro ProSe Application Codes během vysílání přes rozhraní PC5.
- Umožňuje řízení autorizace pro zjišťování zařízení; pouze zařízení se správným klíčem mohou dekódovat zprávy.
- Odvozen z kořenového klíče poskytovaného sítí (ProSe Key), což zajišťuje centralizovanou správu klíčů.
- Podporuje jak modely otevřeného (Open), tak omezeného (Restricted) zjišťování s různými strategiemi distribuce klíčů.
- Brání dlouhodobému sledování skramblováním zjistitelného identifikátoru, čímž zvyšuje ochranu soukromí uživatele.
- Integruje se s funkcí ProSe pro bezpečnou provizi klíčů a správu jejich životního cyklu.

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.555** (Rel-19) — 5G ProSe UE Policies Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay

---

📖 **Anglický originál a plná specifikace:** [DUSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/dusk/)
