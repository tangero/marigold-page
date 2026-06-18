---
slug: "isar"
url: "/mobilnisite/slovnik/isar/"
type: "slovnik"
title: "ISAR – Immersive Audio for Split Rendering Scenarios"
date: 2025-01-01
abbr: "ISAR"
fullName: "Immersive Audio for Split Rendering Scenarios"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isar/"
summary: "ISAR je mediální kodek a aplikační rámec 3GPP pro imerzní audio zážitky v aplikacích rozšířené reality (XR) využívající rozdělený rendering (split rendering). Umožňuje streamování vysoce kvalitního pr"
---

ISAR je rámec 3GPP pro poskytování vysoce kvalitního prostorového audia s nízkou latencí v aplikacích rozšířené reality (Extended Reality), kde je audio rendering rozdělen mezi zařízení a síť.

## Popis

Immersive Audio for Split Rendering Scenarios (ISAR) je specifikace mediálního kodeku a systému 3GPP navržená pro poskytování vysoce kvalitního, objektově založeného prostorového audia pro aplikace rozšířené reality ([XR](/mobilnisite/slovnik/xr/)), zejména v síťových architekturách, kde je rendering rozdělen mezi uživatelské zařízení (např. XR headset) a síťový edge server. ISAR řeší jedinečné výzvy streamování imerzního audia, které vyžaduje rendering se šesti stupni volnosti (6DoF), nízkou celkovou latenci a vysokou kompresní účinnost pro úsporu šířky pásma. Architektura typicky zahrnuje XR aplikační server v síti (např. na edge), který generuje nebo zpracovává nezpracovanou audio scénu obsahující více audio objektů s metadaty popisujícími jejich pozice, orientace a akustické vlastnosti. ISAR enkodér tuto audio scénu komprimuje. Klíčovou inovací je rozdělení renderingového řetězce: část renderingu (např. časné odrazy, základní binauralizace) může být provedena na serveru, zatímco finální fáze (např. pozdní dozvuk, aplikace personalizované funkce přenosu hlavou ([HRTF](/mobilnisite/slovnik/hrtf/)) a kompenzace posledních pohybů hlavy) se provádí na uživatelském zařízení (UE). Toto rozdělení snižuje datový tok potřebný k přenosu ve srovnání s odesíláním plně renderovaného binauračního audia a zároveň odlehčuje náročné zpracování z potenciálně výkonově omezeného UE. ISAR stream, obsahující zakódované audio objekty a metadata pro rendering, je doručován přes 5G síť. ISAR dekodér a renderer v UE poté dokončí audio rendering na základě nejnovějších senzorových dat (polohy hlavy) a vytvoří přesný, personalizovaný prostorový audio zážitek. Specifikace (TS 26.249, 26.251 atd.) definují formáty kodeků, schémata metadat, [API](/mobilnisite/slovnik/api/) a systémová rozhraní pro umožnění této interoperabilní, nízkolatenční služby imerzního audia.

## K čemu slouží

ISAR byl vytvořen k řešení výzev spojených s doručováním audia pro skutečně imerzní a interaktivní [XR](/mobilnisite/slovnik/xr/) zážitky přes mobilní sítě. Tradiční audio kodeky (jako MPEG-H 3D Audio nebo Dolby Atmos) jsou navrženy pro kinematografické nebo vysílací scénáře s pevným prostředím pro přehrávání a vyšší tolerancí latence. Pro interaktivní XR, kde se uživatel může pohybovat hlavou a tělem v reálném čase, musí být audio renderováno dynamicky s ultranízkou latencí (<20 ms), aby odpovídalo vizuální scéně a předcházelo nevolnosti z pohybu. Přenos plně renderovaného binauračního audia pro každou možnou polohu hlavy je nepřijatelně náročný na šířku pásma. Účelem ISAR je umožnit efektivní streamování přijetím modelu rozděleného renderingu, který je v souladu s celkovým paradigmatem rozděleného renderingu XR studovaným v 3GPP. Tento model využívá výpočetní prostředky edge 5G sítě pro náročné audio zpracování, zatímco finální, uživatelsky specifický rendering ponechává na zařízení. Řeší tak omezení předchozích přístupů: buď vysokou spotřebu šířky pásma (odesílání předrenderovaného audia), nebo vysokou výpočetní zátěž zařízení (lokální rendering všeho z nezpracovaných objektů, což nemusí být proveditelné na lehkých XR brýlích). Standardizací ISAR usiluje 3GPP o zajištění interoperability mezi poskytovateli XR aplikací, síťovými operátory a výrobci zařízení, čímž podporuje ekosystém pro vysoce kvalitní cloudové/edge renderované XR služby přes 5G a další sítě.

## Klíčové vlastnosti

- Objektově založený kodek prostorového audia optimalizovaný pro nízkolatenční, interaktivní XR aplikace
- Architektura rozděleného renderingu (split rendering) dělící audio zpracování mezi síťový edge a uživatelské zařízení
- Podpora audia se šesti stupni volnosti (6DoF) s dynamickou aktualizací metadat audio objektů
- Efektivní komprese audio scén a přidružených prostorových metadat pro snížení šířky pásma
- Definovaná systémová rozhraní a API pro integraci mezi XR aplikačními servery, mediálními funkcemi a UE
- Personalizovaný audio rendering na UE využívající zařízení-specifické parametry, jako je HRTF

## Související pojmy

- [XR – AS Augmented/Virtual Reality Application Server](/mobilnisite/slovnik/xr/)
- [6DOF – Six Degrees of Freedom](/mobilnisite/slovnik/6dof/)

## Definující specifikace

- **TS 26.249** (Rel-19) — Immersive Audio Split Rendering (ISAR)
- **TS 26.251** (Rel-19) — IVAS Codec Fixed-Point C Code Specification
- **TS 26.252** (Rel-19) — IVAS Codec Test Sequences Specification
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [ISAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/isar/)
