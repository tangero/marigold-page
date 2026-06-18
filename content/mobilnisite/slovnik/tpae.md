---
slug: "tpae"
url: "/mobilnisite/slovnik/tpae/"
type: "slovnik"
title: "TPAE – Third Party Authorized Entity"
date: 2026-01-01
abbr: "TPAE"
fullName: "Third Party Authorized Entity"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tpae/"
summary: "Důvěryhodná externí entita autorizovaná operátorem mobilní sítě k přístupu k síťovým schopnostem a uživatelským datům pro specifické služby. Umožňuje bezpečnou integraci služeb třetích stran, jako je"
---

TPAE je důvěryhodná externí entita autorizovaná operátorem mobilní sítě k bezpečnému přístupu k síťovým schopnostem a uživatelským datům pro specifické služby třetích stran.

## Popis

Third Party Authorized Entity (TPAE) je bezpečnostní a architektonický koncept zavedený ve 3GPP Release 17, primárně v rámci architektury vrstvy služeb ([SEAL](/mobilnisite/slovnik/seal/)) a vystavení sítě. Představuje externího poskytovatele aplikací nebo služeb, kterému mobilní operátor ([MNO](/mobilnisite/slovnik/mno/)) nebo síťová funkce (jako Network Exposure Function - [NEF](/mobilnisite/slovnik/nef/)) udělil explicitní autorizaci pro přístup k určitým síťovým schopnostem, [API](/mobilnisite/slovnik/api/) nebo uživatelským datům. TPAE není součástí důvěryhodné domény 3GPP sítě, ale funguje v důvěryhodném vztahu založeném na formálních autorizačních procesech. Její identita a oprávnění jsou ověřeny před jakoukoli interakcí, což zajišťuje, že přístup třetích stran je řízený, auditovatelný a v souladu s regulatorními požadavky jako GDPR.

Architektonicky TPAE komunikuje s 3GPP core sítí, typicky prostřednictvím NEF v 5G core (5GC). NEF funguje jako bezpečná brána a bod pro vynucování politik, vystavující síťová API (např. služby Nnef) autorizovaným externím entitám. TPAE se musí autentizovat pomocí přihlašovacích údajů (jako certifikáty) a je jí přiřazen specifický rozsah přístupu na základě její autorizace. Tyto rozsahy definují, které síťové funkce může vyvolat, jaká data může požadovat (např. informace o poloze, úpravy kvality služby) a za jakých podmínek. Požadavky TPAE podléhají politickým kontrolám, včetně ověření souhlasu uživatele, omezení rychlosti a účtování, které vynucuje NEF a další funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)).

Klíčové komponenty zapojené do provozu TPAE zahrnují NEF, který spravuje vystavení a zabezpečení; Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) nebo Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)), které mohou asistovat v autentizaci; a PCF, který poskytuje pravidla politik. Samotná TPAE je charakterizována svou identitou aplikace, bezpečnostními přihlašovacími údaji a autorizovaným profilem služby. Její role je klíčová pro umožnění inovativních služeb, jako jsou aplikace edge computing, kde poskytovatel edge aplikací třetí strany potřebuje přístup s nízkou latencí k uživatelským rovinám funkcí, nebo IoT vertikály vyžadující stav zařízení v reálném čase. Formalizací konceptu TPAE poskytuje 3GPP standardizovaný, bezpečný model pro integraci třetích stran, posunující se od ad-hoc rozhraní k řízenému ekosystému, který chrání integritu sítě a soukromí uživatele.

## K čemu slouží

TPAE byla vytvořena, aby řešila rostoucí poptávku po bezpečném a standardizovaném přístupu třetích stran ke schopnostem 5G sítě. Historicky měli poskytovatelé služeb mimo doménu operátora omezené nebo proprietární způsoby interakce se sítí, často vyžadující komplexní bilaterální dohody a vlastní integrace, což brzdilo inovace a škálovatelnost. S nástupem edge computing, IoT a network slicing vznikla jasná potřeba řízeného mechanismu, který by umožnil externím entitám využívat síťové funkce – jako je řízení kvality služby, lokalizační služby nebo monitorování událostí – bez kompromisů v zabezpečení nebo operační kontrole.

Tento koncept řeší problém, jak bezpečně otevřít síť širšímu ekosystému vývojářů aplikací a vertikálních průmyslů, při zachování autority operátora nad jeho prostředky. Vytváří důvěryhodný rámec, kde mohou být třetí strany autentizovány, autorizovány a auditovány, což zajišťuje, že přístup je udělen pouze pro zamýšlené účely a v souladu se souhlasem uživatele a předpisy na ochranu dat. Model TPAE umožňuje nové obchodní modely, jako je network-as-a-service, tím, že poskytuje jasný technický a procedurální základ pro partnerství s třetími stranami, a tím podporuje otevřené inovační prostředí v éře 5G.

## Klíčové vlastnosti

- Autorizace externí entity prostřednictvím politik definovaných operátorem
- Bezpečný přístup prostřednictvím Network Exposure Function (NEF)
- Řízení přístupu na základě rozsahu omezujícího vystavení API a dat
- Integrace s mechanismy souhlasu uživatele a ochrany soukromí dat
- Podpora autentizace pomocí certifikátů nebo OAuth 2.0
- Umožňuje inovace služeb třetích stran v oblasti edge a IoT

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)

## Definující specifikace

- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.853** (Rel-19) — Charging for Uncrewed Aerial Systems
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TR 33.854** (Rel-17) — Security aspects of Uncrewed Aerial Systems

---

📖 **Anglický originál a plná specifikace:** [TPAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpae/)
