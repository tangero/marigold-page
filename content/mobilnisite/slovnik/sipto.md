---
slug: "sipto"
url: "/mobilnisite/slovnik/sipto/"
type: "slovnik"
title: "SIPTO – Selected IP Traffic Offload"
date: 2025-01-01
abbr: "SIPTO"
fullName: "Selected IP Traffic Offload"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sipto/"
summary: "SIPTO je funkce optimalizace sítě, která operátorovi umožňuje odklonit určité typy IP provozu (typicky směřujícího na internet) z páteřní mobilní sítě na síťový uzel blíže k uživateli, například na mí"
---

SIPTO je funkce optimalizace sítě, která operátorovi umožňuje odklonit specifický IP provoz blíže k uživateli, například na místní bráně, aby se snížila latence a přetížení páteřní sítě.

## Popis

Selected IP Traffic Offload (SIPTO) je standard 3GPP pro optimalizaci směrování datového provozu v mobilních sítích odkloněním specifických IP datových toků z centrální páteřní sítě na místnější bod průniku (breakout). Primárním cílem je zabránit tunelování veškerého provozu uživatelské roviny přes centrální bránu paketové datové sítě ([P-GW](/mobilnisite/slovnik/p-gw/)) v Evolved Packet Core (EPC) nebo přes funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core (5GC), zejména u provozu směřujícího na internet nebo do místní servisní sítě. SIPTO umožňuje vytvoření spojení uživatelské roviny z rádiové přístupové sítě (RAN) přímo k místní bráně ([L-GW](/mobilnisite/slovnik/l-gw/)), která je umístěna společně např. s makro eNodeB, bránou Home eNodeB nebo centralizovaným bodem agregace RAN. V 5G se tento koncept rozšiřuje na výběr místní UPF.

Z architektonického hlediska SIPTO zahrnuje síťovou detekci provozu a rozhodování o směrování. V EPC, když uživatelské zařízení (UE) aktivuje spojení s paketovou datovou sítí ([PDN](/mobilnisite/slovnik/pdn/)), může síť (konkrétně [MME](/mobilnisite/slovnik/mme/) po konzultaci s [HSS](/mobilnisite/slovnik/hss/)) vybrat P-GW, která je topologicky blízko k aktuálnímu bodu připojení UE. Pro ještě jemnější odklon umožňuje funkce 'SIPTO at the Local Network' HeNB s podporou místního IP přístupu ([LIPA](/mobilnisite/slovnik/lipa/)) použít společně umístěnou L-GW k přímému odklonu provozu. Řídicí signalizace ([GTP-C](/mobilnisite/slovnik/gtp-c/)) stále prochází páteřní sítí (MME, S-GW), ale data uživatelské roviny (GTP-U) využívají zkratku. V 5GC funkce správy relací (SMF) vybere na základě polohy UE a požadavků na provoz vhodnou UPF, která bude sloužit jako místní breakoutový bod, a to s využitím zjišťování z NRF a místních směrovacích politik.

Proces funguje na základě konfigurací APN (v EPC) nebo DNN (v 5GC) a profilů účastníků. Operátor může definovat, že provoz odpovídající určitému APN/DNN (např. 'internet') je kandidátem pro SIPTO. Když UE vyžádá spojení pro toto APN/DNN, uzel páteřní sítě (MME/AMF/SMF) vyhodnotí polohu UE, schopnosti blízkých bran a síťové politiky. Pokud jsou podmínky splněny, vybere místní bránu/UPF a podle toho vytvoří přenosový kanál/PDU relaci. Klíčovými komponentami jsou místní brána (L-GW v EPC, místní UPF v 5GC), uzly řídicí roviny, které výběr provádějí, a politický rámec, který určuje, který provoz je pro odklon způsobilý. SIPTO je pro koncové uživatelské zařízení transparentní, nevyžaduje pro základní síťový odklon žádnou specifickou podporu na straně UE, což z něj činí účinný nástroj pro efektivitu sítě.

## K čemu slouží

SIPTO bylo vytvořeno jako odpověď na explozivní růst mobilního datového provozu, zejména náročného provozu směřujícího na internet, jako je streamování videa a prohlížení webu, který způsoboval přetížení a problémy se škálovatelností v páteřní mobilní síti a na nákladných přenosových trasách (backhaul). Tradiční model směrování všech dat přes centralizovanou P-GW/GGSN vytvářel neefektivní 'trombónový efekt', kdy data směřující do místní internetové výměny nejprve putovala stovky kilometrů do páteřní sítě, aby byla poslána zpět, což zvyšovalo latenci a náklady na přenos.

Historický kontext představuje vývoj od 3G k 4G LTE, kdy objemy dat začaly zatěžovat ekonomiku sítí. Předchozí přístupy postrádaly standardizovanou metodu pro inteligentní místní průnik (breakout). Operátoři se uchylovali k proprietárním řešením nebo funkcím jako LIPA, která byla omezena na prostředí femtobuněk. SIPTO, zavedené ve verzi 10, poskytlo standardizovaný, škálovatelný a síťově řízený mechanismus pro odklon vybraného provozu blíže k okraji sítě. Motivací byla potřeba snížit latenci pro lepší uživatelský komfort, minimalizovat kapitálové a provozní výdaje úsporou přenosových tras a zdrojů páteřní sítě a připravit sítě na příval dat od chytrých telefonů a později zařízení IoT. Položilo to základy klíčovým principům 5G, jako je distribuovaná uživatelská rovina a edge computing.

## Klíčové vlastnosti

- Síťový výběr místní brány (L-GW/UPF) topologicky blízko k RAN uzlu UE pro průnik (breakout) uživatelské roviny
- Snižuje latenci a zatížení páteřní sítě a přenosových tras (backhaul) optimalizací směrovacích cest pro vybraný IP provoz (např. internet)
- Výběr provozu je založen na APN (EPC) nebo DNN (5GC) a může být řízen profily účastníků a provozními politikami
- Může fungovat nad úrovní RAN (např. v uzlu agregace RAN) nebo přímo v RAN uzlu (např. společně umístěno s HeNB)
- Pro základní odklon transparentní pro UE, nevyžaduje úpravy na straně klienta
- Základní koncept umožňující pozdější technologie, jako je Mobile Edge Computing (MEC) a Local Area Data Network (LADN) v 5G

## Související pojmy

- [LIPA – Local IP Access](/mobilnisite/slovnik/lipa/)
- [LADN – Local Area Data Network](/mobilnisite/slovnik/ladn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.646** (Rel-12) — UTRAN NRM IRP Solution Set Definitions
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [SIPTO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sipto/)
