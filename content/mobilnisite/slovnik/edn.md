---
slug: "edn"
url: "/mobilnisite/slovnik/edn/"
type: "slovnik"
title: "EDN – Edge Data Network"
date: 2026-01-01
abbr: "EDN"
fullName: "Edge Data Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/edn/"
summary: "Distribuovaná výpočetní architektura v 5G, která nasazuje aplikační servery a cloudové prostředky na okraji sítě, blízko uživatele. Umožňuje ultra-nízkou latenci, vysokou přenosovou kapacitu a lokaliz"
---

EDN je distribuovaná 5G architektura, která nasazuje aplikační servery a cloudové prostředky na okraji sítě, aby umožnila ultra-nízkou latenci, vysokou přenosovou kapacitu a lokalizované zpracování dat pro služby jako AR/VR a IoT.

## Popis

Edge Data Network (EDN) je klíčový architektonický koncept v systémech 5G, definovaný 3GPP, který označuje lokální datovou síť umístěnou na okraji sítě mobilního operátora, v těsné blízkosti uživatelského zařízení (UE). Nejde pouze o fyzickou lokalitu, ale o logickou a službami řízenou architekturu hostující aplikační funkce, cloudové prostředky a cache obsahu. EDN je typicky spolulokalizován nebo přiléhá k uzlům 5G rádiové přístupové sítě (RAN), jako je gNB, nebo k funkci User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která poskytuje výstupní bod pro lokální datový provoz. Tato blízkost radikálně snižuje fyzickou vzdálenost, kterou data musí urazit, minimalizuje latenci a zatížení backhaul přenosů.

Architektonicky je EDN integrován do 5G Core (5GC) prostřednictvím funkce Local Area Data Network ([LADN](/mobilnisite/slovnik/ladn/)) a UPF. Klíčovou součástí je Data Network ([DN](/mobilnisite/slovnik/dn/)) v terminologii 5GC, což představuje jakoukoli síť poskytující datové služby (např. internet, IMS nebo privátní firemní síť). EDN je specifický typ DN, který je 'lokální' nebo 'edge'. UPF je konfigurována tak, aby směrovala specifické datové toky uživatele, identifikované názvem Data Network Name ([DNN](/mobilnisite/slovnik/dnn/)) a informacemi pro výběr síťového řezu (NSSAI), do EDN namísto jejich směrování centrální páteřní sítí do vzdáleného DN. Samotný EDN hostuje aplikační funkce ([AF](/mobilnisite/slovnik/af/)), které mohou komunikovat s 5GC prostřednictvím Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) za účelem ovlivnění směrování provozu a politik kvality služeb (QoS).

Jak to funguje, zahrnuje navázání relace a směrování provozu. Když UE žádá o připojení k edge službě (např. řídicí server továrního robota), použije DNN asociovaný s EDN. Funkce Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5GC vybere UPF, která je topologicky blízko umístění UE a má konektivitu k požadovanému EDN. UPF se pak stane kotvícím bodem a směruje IP pakety UE přímo na aplikační servery uvnitř EDN. To umožňuje interakci v reálném čase. EDN dále může využívat síťovou expozici pro pokročilé schopnosti, jako je přijímání notifikací o událostech mobility UE (např. vstupu do oblasti edge služby) prostřednictvím NEF, což aplikacím umožňuje dynamicky migrovat nebo přizpůsobovat svůj stav.

## K čemu slouží

EDN byl vytvořen, aby vyřešil základní omezení centralizovaného cloud computingu pro aplikace citlivé na latenci a náročné na přenosovou kapacitu. V tradičních mobilních sítích veškerý datový provoz procházel RAN, backhaul a páteřní sítí, aby dosáhl vzdálených datových center, což způsobovalo významnou latenci (často 50–100 ms). To je nepřijatelné pro aplikace jako autonomní vozidla, hmatový internet, rozšířená realita a průmyslové řízení v reálném čase, které vyžadují latenci pod 10 ms. EDN přesouvá výpočetní výkon a úložiště na okraj sítě, což přímo řeší tento problém s latencí.

Řeší také kritické problémy s přetížením sítě a náklady na backhaul přenosy. Lokálním zpracováním a ukládáním obsahu (např. cachováním oblíbeného videa) EDN snižuje objem opakovaného provozu, který musí být přenášen na velké vzdálenosti do centrální páteřní sítě a internetu. To zlepšuje celkovou účinnost sítě a uživatelský zážitek, zejména na přeplněných místech jako jsou stadiony. Motivace je hluboce spjata s vizí 5G, která má umožnit vertikální průmysly (např. výroba, zdravotnictví), jež vyžadují garantovanou nízkou latenci, vysokou spolehlivost a lokalitu dat z důvodů ochrany soukromí nebo regulace.

Historicky se koncept EDN vyvinul z Cloud Radio Access Network (C-RAN) a Mobile Edge Computing (MEC), které byly zpočátku více orientovány na RAN. Formalizace EDN v 3GPP Release 17 tyto koncepty nativně integrovala do službami řízené architektury 5G. Poskytuje standardizovaný rámec pro operátory, aby nabízeli edge computing jako plynulou síťovou službu, vytvářeli nové zdroje příjmů a umožnili ekosystém komunikace s ultra-spolehlivou nízkou latencí (URLLC) a aplikací rozšířeného mobilního širokopásmového přístupu (eMBB), které definují transformační potenciál 5G.

## Klíčové vlastnosti

- Hostuje aplikační servery a cloudové prostředky v blízkosti uživatele (na okraji RAN)
- Integrován s 5GC prostřednictvím funkce lokálního výstupu UPF a funkcí LADN
- Umožňuje ultra-nízkou latenci (v řádu jednotek milisekund) a vysokou přenosovou kapacitu pro aplikace
- Podporuje směrování provozu na základě DNN a síťového řezu
- Umožňuje aplikačním funkcím (AF) komunikovat s 5GC pro kontrolu QoS a politik
- Snižuje backhaul provoz a zatížení páteřní sítě prostřednictvím lokalizovaného zpracování dat a cachování

## Související pojmy

- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- **TR 28.815** (Rel-17) — Charging Study for Edge Computing
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [EDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/edn/)
