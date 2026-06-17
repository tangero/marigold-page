---
slug: "cpn"
url: "/mobilnisite/slovnik/cpn/"
type: "slovnik"
title: "CPN – Customer Premises Network"
date: 2026-01-01
abbr: "CPN"
fullName: "Customer Premises Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpn/"
summary: "Privátní síť umístěná v prostorách zákazníka, která se připojuje k síti 3GPP. Umožňuje podnikové a průmyslové aplikace tím, že poskytuje lokalizovanou konektivitu a služby při zachování integrace s in"
---

CPN je privátní síť umístěná v prostorách zákazníka, která se připojuje k síti 3GPP, aby umožnila podnikovým aplikacím lokalizovanou konektivitu při zachování integrace s mobilní sítí.

## Popis

Customer Premises Network (CPN) je infrastruktura privátní sítě nasazená na fyzické lokalitě zákazníka, která rozhraní s mobilní sítí 3GPP. Slouží jako doména lokalizované konektivity pro podnikové, průmyslové nebo rezidenční uživatele, poskytuje síťové služby a propojuje různá zařízení v rámci daného prostoru. Architektura CPN typicky zahrnuje zařízení pro lokální síť ([LAN](/mobilnisite/slovnik/lan/)), směrovače, přepínače, přístupové body a případně specializované průmyslové řadiče nebo brány pro internet věcí (IoT), které spravují komunikaci mezi zařízeními v prostorách a širší sítí 3GPP.

V architektuře 3GPP se CPN připojuje k mobilní síti prostřednictvím standardizovaných rozhraní, nejčastěji přes funkci User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v jádru sítě 5G Core. Toto připojení umožňuje CPN využívat služby mobilní sítě, jako je autentizace, řízení politik a správa kvality služby (QoS), při zachování lokální autonomie pro aplikace specifické pro daný prostor. CPN může implementovat různé přístupové technologie včetně Wi-Fi, Ethernetu, Bluetooth nebo specializovaných průmyslových protokolů, přičemž síť 3GPP slouží jako přenosová trasa (backhaul) nebo propojení k dalším sítím a cloudovým službám.

CPN hraje klíčovou roli v podnikových a průmyslových scénářích tím, že poskytuje lokalizované zpracování, komunikaci s nízkou latencí a datovou suverenitu při zachování integrace se službami mobilní sítě. Umožňuje případy užití, jako je automatizace výroby, chytré budovy, kampusové sítě a pobočky, kombinací flexibility privátního sítění s funkcemi spolehlivosti a zabezpečení sítí 3GPP. Architektura CPN podporuje síťové segmenty (network slicing), což umožňuje naplňovat různé požadavky na služby prostřednictvím vyhrazených logických sítí, které se rozprostírají od mobilního jádra až k prostorům zákazníka.

Klíčové komponenty CPN v kontextu 3GPP zahrnují Customer Premises Equipment ([CPE](/mobilnisite/slovnik/cpe/)), které poskytuje bránovou funkci mezi mobilní sítí a lokálními zařízeními, lokální body pro autentizaci a vynucování politik a případně prostředky pro edge computing. Systém správy CPN se integruje se systémy správy sítě 3GPP pro koordinovaný provoz, monitorování a řešení problémů. Bezpečnostní mechanismy v CPN zahrnují lokální firewally, systémy detekce narušení a integraci s autentizačními a šifrovacími protokoly 3GPP, aby byla zajištěna zabezpečení od koncových zařízení až po aplikace.

## K čemu slouží

Koncept CPN byl v 3GPP zaveden, aby řešil rostoucí potřebu podnikových a průmyslových aplikací, které vyžadují jak schopnosti mobilních sítí, tak kontrolu nad privátními sítěmi. Jak se sítě 5G rozšířily za rámec mobilního širokopásmového připojení pro spotřebitele, aby podporovaly vertikální průmysly, objevila se potřeba sítí, které lze nasadit na straně zákazníka při zachování bezproblémové integrace s infrastrukturou mobilního operátora. Tím se řeší omezení předchozích přístupů, kdy podnikové sítě fungovaly zcela nezávisle na mobilních sítích, což vyžadovalo složitou integraci a znamenalo ztrátu funkcí specifických pro mobilní sítě.

Předchozí řešení podnikového sítování často spoléhala na oddělenou infrastrukturu pro lokální a rozlehlou konektivitu, což vytvářelo složitost správy a neoptimální výkon pro aplikace využívající mobilní síť. Koncept CPN umožňuje jednotný přístup, kdy se síť v prostorách zákazníka stává rozšířením mobilní sítě, což umožňuje konzistentní vynucování politik, zabezpečení a poskytování služeb napříč oběma doménami. To je zvláště důležité pro aplikace Průmyslu 4.0, chytré kampusy a distribuované podniky, které vyžadují jak lokální zpracovatelské schopnosti, tak spolehlivé připojení k centrálním zdrojům.

Zavedení CPN ve vydání Release 18 odráží vývoj 3GPP směrem k podpoře různorodých scénářů nasazení a požadavků vertikálních průmyslů. Umožňuje mobilním operátorům nabízet spravované služby podnikového sítování, které kombinují nejlepší aspekty buněčného a lokálního sítění, a vytváří tak nové obchodní modely a příležitosti pro služby. Standardizací rozhraní mezi CPN a sítěmi 3GPP zajišťuje interoperabilitu mezi zařízeními různých výrobců a umožňuje škálovatelné nasazení řešení podnikového sítování.

## Klíčové vlastnosti

- Integrace s architekturou sítě 3GPP prostřednictvím standardizovaných rozhraní
- Podpora technologií pro lokální konektivitu včetně Wi-Fi, Ethernetu a průmyslových protokolů
- Schopnosti síťových segmentů (network slicing) rozprostírající se od mobilního jádra až k prostorům zákazníka
- Lokální vynucování politik a správa provozu integrovaná s politikami mobilní sítě
- Podpora edge computingu pro aplikace s nízkou latencí v prostorách zákazníka
- Integrace zabezpečení s autentizačními a šifrovacími mechanismy 3GPP

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [CPE – Customer Premises Equipment](/mobilnisite/slovnik/cpe/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.858** (Rel-18) — Technical Report on Residential 5G Services

---

📖 **Anglický originál a plná specifikace:** [CPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpn/)
