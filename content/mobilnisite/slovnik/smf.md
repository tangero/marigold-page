---
slug: "smf"
url: "/mobilnisite/slovnik/smf/"
type: "slovnik"
title: "SMF – Service Management Function"
date: 2026-01-01
abbr: "SMF"
fullName: "Service Management Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smf/"
summary: "Service Management Function (SMF) je síťová funkce v jádru sítě 5G odpovědná za správu životního cyklu relací protokolových datových jednotek (PDU). Zajišťuje zřizování, modifikaci a ukončování relací"
---

SMF je síťová funkce 5G jádra odpovědná za správu životního cyklu PDU relací, včetně jejich zřizování, modifikace, ukončování, přidělování IP adres, vynucování politik a kontroly QoS.

## Popis

Service Management Function (SMF) je kritická síťová funkce řídicí roviny v rámci architektury 5G Core (5GC), definovaná standardy 3GPP. Je odpovědná za komplexní správu relací protokolových datových jednotek (PDU), což jsou logická spojení poskytující uživatelskému zařízení (UE) připojení k datové síti (DN), jako je internet nebo služba operátora. SMF interaguje s mnoha dalšími síťovými funkcemi při plnění svých úkolů. Během zřizování relace přijímá SMF požadavky na správu relace od funkce pro správu přístupu a mobility (AMF). Vybere instanci User Plane Function (UPF) jako kotvu datové cesty, přidělí UE IP adresu (funguje jako DHCP server nebo spolupracuje s externím DHCP serverem) a zřídí potřebné tunely (např. rozhraní N3, N9) mezi rádiovou přístupovou sítí (RAN), UPF a datovou sítí. SMF je také odpovědná za vynucování politik a kontrolu QoS. Spolupracuje s Policy Control Function (PCF) pro získání pravidel politiky, které následně konfiguruje v UPF k jejich vynucení, například aplikací uzavírání (gating), omezení šířky pásma nebo spouštění účtování. Dále SMF spravuje sběr údajů pro účtování prostřednictvím interakce s Charging Function (CHF). Generuje hlášení o využití a předává je pro offline nebo online účtování. SMF také zajišťuje procedury modifikace relace vyvolané síťovými politikami, požadavky uživatele nebo událostmi mobility (jako je předávání hovoru), čímž zajišťuje nepřerušovanou kontinuitu služby. Hraje klíčovou roli v dělení sítě (network slicing) tím, že je si vědoma instance řezu a zajišťuje, aby PDU relace odpovídala charakteristikám a požadavkům na izolaci konkrétního řezu. Její funkcionalita je vystavena prostřednictvím rozhraní založených na službách, primárně Nsmf, což umožňuje dalším autorizovaným NF vyvolávat její služby.

## K čemu slouží

SMF byla vytvořena jako součást nové architektury 5G Core (5GC) založené na službách (SBA) za účelem odstranění omezení staršího Evolved Packet Core (EPC). V EPC byla správa relací těsně svázána uvnitř MME (pro řídicí rovinu) a Serving Gateway (SGW) a PDN Gateway (PGW) pro uživatelskou rovinu a politiky. Tato monolitická architektura postrádala flexibilitu, škálovatelnost a brzdila rychlý vývoj služeb. Účelem SMF je oddělit správu relací do specializované softwarové funkce řídicí roviny. Toto oddělení umožňuje nezávislé škálování, podrobnější kontrolu politik a efektivní podporu různých případů užití 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB), ultra-spolehlivá komunikace s nízkou latencí (URLLC) a hromadná komunikace strojového typu (mMTC). Díky centralizaci stavu PDU relací SMF zjednodušuje správu mobility, umožňuje pokročilé funkce, jako je současná konektivita k více datovým sítím, a poskytuje jednotný bod pro aplikaci politik specifických pro relaci. Její vytvoření bylo motivováno potřebou cloud-nativního, agilního jádra sítě, které by mohlo dynamicky orchestrovat konektivitu přizpůsobenou specifickým požadavkům aplikací, což je zásadní pro naplnění celého potenciálu 5G, včetně dělení sítě a edge computingu.

## Klíčové vlastnosti

- Centralizovaná správa a řízení životního cyklu PDU relace (zřízení, modifikace, ukončení)
- Přidělování a správa IP adres pro UE (IPv4, IPv6 nebo obojí)
- Výběr a řízení instancí User Plane Function (UPF) pro přeposílání dat
- Vynucování relací a politik souvisejících se službami přijatých od PCF
- Správa a řízení QoS toků, včetně autorizace a vynucování parametrů QoS
- Sběr údajů pro účtování a interakce s Charging Function (CHF)

## Definující specifikace

- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- … a dalších 66 specifikací

---

📖 **Anglický originál a plná specifikace:** [SMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/smf/)
