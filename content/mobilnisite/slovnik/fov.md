---
slug: "fov"
url: "/mobilnisite/slovnik/fov/"
type: "slovnik"
title: "FOV – Field of View"
date: 2025-01-01
abbr: "FOV"
fullName: "Field of View"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fov/"
summary: "Field of View (FOV, zorné pole) definuje rozsah pozorovatelného prostředí, které může zachytit kamera nebo senzor, a měří se jako úhlová šířka. V 3GPP se jedná o klíčový parametr pro imerzivní mediáln"
---

FOV je úhlová šířka definující rozsah pozorovatelného prostředí, které může zachytit kamera nebo senzor, což je klíčový parametr pro imerzivní mediální služby v 3GPP.

## Popis

Ve specifikacích 3GPP je Field of View (FOV) klíčovým parametrem v rámci architektur pro doručování médií a imerzivní služby. Jedná se o úhlovou míru, typicky ve stupních horizontálně a vertikálně, která popisuje část úplné sférické nebo panoramatické scény, která je vykreslena nebo přenesena na uživatelovo zařízení v daném okamžiku. Technicky definuje vizuální frustum pro daný pohled. U služeb jako 360stupňové video je zachycena celá scéna (sférické mapování), ale pro snížení šířky pásma je doručován pouze FOV odpovídající orientaci uživatelovy hlavy.

Architektura pro doručování médií s podporou FOV zahrnuje komponenty v aplikačním serveru, mediálním kodéru a na klientovi. Mediální server typicky ukládá nebo generuje vysoce rozlišený všesměrový mediální proud. Na základě informací o viewportu (data sledování polohy hlavy) zaslaných od klienta server nebo síťová procesní funkce dynamicky přizpůsobuje streamování. To může zahrnovat extrakci a kódování pouze dlaždic (tiles) v aktuálním FOV uživatele ve vysoké kvalitě, zatímco ostatní dlaždice jsou zasílány v nižší kvalitě nebo vůbec – technika známá jako viewport-adaptivní streamování.

Jeho role je klíčová pro umožnění efektivního doručování náročných imerzivních médií přes mobilní sítě. Sledováním FOV a predikcí budoucích viewportů systém optimalizuje využití zdrojů jak na rádiovém rozhraní, tak v core síti. Tím je zajištěna vysoká vizuální kvalita tam, kde se uživatel dívá, a zároveň je minimalizováno zpoždění a trhání při změně pohledu. Specifikace, jako jsou ty pro [MPEG](/mobilnisite/slovnik/mpeg/) Media Transport a Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), byly rozšířeny o podporu metadat pro FOV a dlaždicových reprezentací, aby tuto funkcionalitu umožnily.

## K čemu slouží

Standardizace parametrů souvisejících s FOV v 3GPP byla hnací silou nástupu komerčních služeb [VR](/mobilnisite/slovnik/vr/) a [AR](/mobilnisite/slovnik/ar/), které vyžadují obrovská množství videodat pro plně imerzivní zážitek. Přenos celých 360stupňových scén v ultra vysokém rozlišení by zahltil kapacitu sítě a výkon zařízení. Účelem definice mechanismů FOV bylo vyřešit tento problém škálovatelnosti.

Řeší omezení tradičního streamování videa, které všem uživatelům posílá jediný obdélníkový snímek. Pro imerzivní média je to vysoce neefektivní, protože většina přenášených pixelů leží mimo uživatelův bezprostřední výhled. Začleněním FOV do servisní a transportní vrstvy umožňují standardy 3GPP zásadní posun k doručování závislému na viewportu. Díky tomu jsou vysoce kvalitní, nízkolatenční VR/AR zážitky technicky a ekonomicky proveditelné přes sítě 5G, což podporuje nové případy užití v oblasti her, vzdálené spolupráce, živých událostí a výcviku.

## Klíčové vlastnosti

- Úhlová míra definující viditelnou část scény
- Klíčový prvek pro viewport-adaptivní streamování
- Integrováno s daty sledování orientace hlavy
- Snižuje spotřebu šířky pásma pro imerzivní média
- Podporuje dlaždicové kódování a doručování médií
- Definováno ve specifikacích mediálních formátů a transportu (např. MPEG, DASH)

## Definující specifikace

- **TS 22.156** (Rel-19) — Mobile Metaverse Services
- **TR 22.856** (Rel-19) — Feasibility Study on Localized Mobile Metaverse Services
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.929** (Rel-19) — QoE Metrics for VR Services Study

---

📖 **Anglický originál a plná specifikace:** [FOV na 3GPP Explorer](https://3gpp-explorer.com/glossary/fov/)
