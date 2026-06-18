---
slug: "op"
url: "/mobilnisite/slovnik/op/"
type: "slovnik"
title: "OP – Operator Platform"
date: 2026-01-01
abbr: "OP"
fullName: "Operator Platform"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/op/"
summary: "Standardizovaný rámec v rámci 3GPP, který umožňuje operátorům sítí zpřístupnit síťové schopnosti a informace důvěryhodným poskytovatelům služeb třetích stran a podnikovým zákazníkům. Usnadňuje vytváře"
---

OP je standardizovaný rámec 3GPP, který umožňuje operátorům sítí bezpečně zpřístupnit síťové schopnosti a data důvěryhodným třetím stranám za účelem vytváření nových služeb a aplikací.

## Popis

Operator Platform (OP) je servisní architektura definovaná 3GPP, která poskytuje řízené rozhraní mezi interními síťovými schopnostmi mobilního operátora ([MNO](/mobilnisite/slovnik/mno/)) a externími poskytovateli aplikací. Slouží jako brána, která abstrahuje složitost podkladové sítě a zpřístupňuje sadu standardizovaných, zabezpečených a zpoplatnitelných aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)). Mezi základní architektonické komponenty patří samotná Operator Platform (logická entita implementující API), funkce pro zpřístupnění sítě ([NEF](/mobilnisite/slovnik/nef/)) v 5G Core a backendové systémy MNO.

Jak to funguje, zahrnuje několik vrstev. Poskytovatelé aplikací třetích stran (např. společnost poskytující cloudové hraní, poskytovatel služeb IoT) se u Operator Platform zaregistrují a jsou jí ověřeni. Poté používají publikovaná API k vyžádání konkrétních síťových služeb. Například volání API může požadovat zvýšenou šířku pásma pro uplink pro konkrétní koncové zařízení během relace nahrávání videa. Operator Platform tento požadavek přijme, ověří jej vůči smlouvě o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) a bezpečnostním politikám poskytovatele, přeloží jej do interních síťových příkazů a prostřednictvím NEF komunikuje s funkcemi jádra sítě, jako je funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) nebo funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), aby požadovanou službu zavedla. Platforma také zpracovává záznamy o účtování, čímž zajišťuje, že třetí strana je za spotřebované síťové prostředky fakturována.

Její role v síti je klíčová pro monetizaci a inovace. Mění roli operátora z pouhého poskytovatele konektivity na subjekt umožňující diferencované služby. Zpřístupněním schopností, jako je správa kvality služeb (QoS), informace o poloze, stav sítě a aktivace zařízení, umožňuje OP podnikům a vývojářům vytvářet aplikace, které jsou těsně integrovány s výkonem a inteligencí sítě. To vytváří nové zdroje příjmů pro operátory a podporuje ekosystém aplikací, které jsou si vědomy sítě.

## K čemu slouží

Koncept Operator Platform byl zaveden, aby vyřešil problém 'uzavřených zahrad' a omezené inovace služeb v tradičních telekomunikačních sítích. Před jeho standardizací bylo zpřístupňování síťových schopností prováděno proprietárním, ad-hoc způsobem, což ztěžovalo vývojářům třetích stran vytvářet služby fungující napříč sítěmi různých operátorů. To dusilo inovace a omezovalo hodnotu získanou ze síťových investic.

Historicky, s nástupem aplikací typu Over-The-Top ([OTT](/mobilnisite/slovnik/ott/)), viděli operátoři, že jejich sítě jsou používány jako hloupé přenosové trubky, zatímco hodnotu získávali poskytovatelé aplikací. OP, zejména jak se vyvíjela prostřednictvím vydání jako Rel-15 a Rel-16 se zavedením [NEF](/mobilnisite/slovnik/nef/), byla motivována potřebou, aby operátoři znovu získali roli v hodnotovém řetězci služeb. Řeší omezení předchozích přístupů tím, že poskytuje standardizovaný, škálovatelný a bezpečný rámec pro zpřístupňování služeb. To umožňuje operátorům nabízet Síť jako službu (NaaS), účastnit se vertikálních trhů (jako je automobilový průmysl, zdravotnictví a Průmysl 4.0) a dynamicky přizpůsobovat chování sítě potřebám konkrétních aplikací, čímž vytvářejí nové obchodní modely nad rámec jednoduchých datových předplatných.

## Klíčové vlastnosti

- Standardizovaná aplikační programová rozhraní (API) směrem k poskytovatelům aplikací třetích stran
- Zabezpečené ověřování, autorizace a účtování (AAA) pro přístup k API
- Vrstva abstrakce, která skrývá interní složitost a topologii sítě
- Integrace s funkcí pro zpřístupnění sítě (NEF) v 5G Core
- Vymáhání politik a správa smluv o úrovni služeb (SLA)
- Zprostředkování účtování a fakturace za zpřístupněné síťové služby

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)
- [SCS – Subcarrier Spacing](/mobilnisite/slovnik/scs/)

## Definující specifikace

- **TS 22.895** (Rel-12) — 3GPP SSO Framework Integration Study
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification

---

📖 **Anglický originál a plná specifikace:** [OP na 3GPP Explorer](https://3gpp-explorer.com/glossary/op/)
