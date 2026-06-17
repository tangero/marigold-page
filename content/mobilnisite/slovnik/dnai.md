---
slug: "dnai"
url: "/mobilnisite/slovnik/dnai/"
type: "slovnik"
title: "DNAI – Data Network Access Identifier"
date: 2026-01-01
abbr: "DNAI"
fullName: "Data Network Access Identifier"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dnai/"
summary: "Identifikátor přístupového bodu uživatelské roviny ke konkrétní datové síti (DN) nebo lokalizované službě v ní. Používají jej aplikace a 5G Core k optimalizaci směrování provozu, což umožňuje nízkolat"
---

DNAI je identifikátor přístupového bodu uživatelské roviny ke konkrétní datové síti, používaný k optimalizaci směrování provozu pro služby, jako je edge computing, nasměrováním uživatelského provozu na optimální výstupní bod sítě.

## Popis

Data Network Access Identifier (DNAI) je klíčovým prvkem pro edge computing a přístup k lokalizovaným službám v 5G systému. Identifikuje konkrétní bod, přes který může PDU Session přistupovat k datové síti, což často odpovídá instanci User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) nasazené na okrajové lokalitě sítě blízko uživatele nebo aplikačního serveru. DNAI není síťová adresa, ale logický identifikátor, který 5G Core mapuje na skutečné transportní a UPF prostředky potřebné k dosažení konkrétní [DN](/mobilnisite/slovnik/dn/) nebo instance služby.

Z architektonického hlediska se informace o DNAI používají v rámci Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). Application Function ([AF](/mobilnisite/slovnik/af/)), jako je video streamovací server nebo průmyslová IoT platforma, může poskytnout DNAI 5G Core prostřednictvím NEF, aby ovlivnila směrování PDU Session. To se děje prostřednictvím služby vlivu AF na směrování provozu definované v TS 23.501. Žádost AF zahrnuje DNAI a požadovanou politiku směrování provozu. Jádrová síť, konkrétně SMF, pak použije tento DNAI spolu s aktuální polohou UE k výběru UPF, která poskytuje konektivitu k datové síti v bodě identifikovaném tímto DNAI. To může zahrnovat zřízení nové PDU Session Anchor (PSA) UPF nebo přesun stávající.

Jak to funguje, zahrnuje úzkou interakci mezi aplikační vrstvou a síťovou vrstvou. Když UE spustí aplikaci vyžadující edge prostředky, AF signalizuje potřebu připojení prostřednictvím konkrétního DNAI. SMF konzultuje Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) a svou lokální konfiguraci, aby namapovala DNAI na konkrétní instanci UPF (nebo skupinu instancí), která může poskytnout požadovaný přístup. SMF pak spravuje N4 session ke zvolené UPF a zřizuje N6 připojení k DN. Toto dynamické nasměrování umožňuje přístup ke stejné logické službě (identifikované Data Network Name, [DNN](/mobilnisite/slovnik/dnn/)) přes různé fyzické body (identifikované DNAI) na základě mobility uživatele a požadavků aplikace, což je zásadní pro ultra spolehlivou nízkolatenční komunikaci (URLLC) a mobilní edge computing ([MEC](/mobilnisite/slovnik/mec/)).

## K čemu slouží

DNAI bylo vytvořeno k vyřešení problému statického a neoptimálního směrování provozu v mobilních sítích, což byla hlavní překážka pro nízkolatenční služby, jako je autonomní řízení, průmyslová automatizace a rozšířená realita. Před zavedením DNAI by PDU Session k datové síti (identifikované DNN) typicky opouštěla jádro sítě na centralizovaném místě, což přidávalo významnou latenci pro aplikace využívající edge. Nebyl standardizovaný způsob, jak by aplikace mohla požadovat konkrétní, geograficky optimální přístupový bod.

Jeho zavedení ve verzi 15 bylo motivováno požadavkem 5G podporovat Edge Computing a síťové řezy s lokalizovanými službami. DNAI poskytuje chybějící článek mezi povědomím aplikace o tom, kde je její služba hostována (např. v konkrétním edge datovém centru), a schopností sítě směrovat uživatelský provoz přesně do tohoto bodu. Řeší tak omezení DNN, které identifikuje pouze *ke které* síti se připojit, ale ne *kde* se připojit z topologie mobilní sítě.

Tato schopnost odemyká nové obchodní modely a technické možnosti. Umožňuje operátorům nasadit více instancí stejné služby napříč jejich sítí a dynamicky směrovat uživatele k té nejbližší. Je zásadní pro naplnění slibů 5G ohledně latence a šířky pásma pro vertikální průmysly, což jim umožňuje považovat mobilní síť za distribuovanou výpočetní platformu, nikoli pouze za spojovací kanál.

## Klíčové vlastnosti

- Identifikuje logický přístupový bod k datové síti nebo lokalizované službě
- Umožňuje směrování provozu ovlivněné aplikací pro optimalizaci na edge
- Používá se SMF pro optimální výběr UPF a správu PDU Session Anchor
- Mapován na fyzické síťové prostředky (UPF, N6 rozhraní)
- Funguje ve spojení s informacemi o DNN a poloze UE
- Základní prvek pro umožnění 5G Edge Computing a scénářů MEC

## Definující specifikace

- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- **TR 28.844** (Rel-18) — Technical Report on Charging Aspects of Satellite in 5GS
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [DNAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dnai/)
