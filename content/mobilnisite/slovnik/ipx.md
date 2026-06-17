---
slug: "ipx"
url: "/mobilnisite/slovnik/ipx/"
type: "slovnik"
title: "IPX – Internetwork Packet Exchange"
date: 2026-01-01
abbr: "IPX"
fullName: "Internetwork Packet Exchange"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipx/"
summary: "Standardizovaný, zabezpečený a kvalitou služeb (QoS) podporovaný rámec pro propojení založený na IP, určený pro výměnu provozu mezi mobilními síťovými operátory a poskytovateli služeb. Umožňuje globál"
---

IPX je standardizovaný, zabezpečený a kvalitou služeb (QoS) podporovaný rámec pro propojení založený na IP, určený pro výměnu provozu mezi mobilními operátory a poskytovateli služeb za účelem umožnění globálního roamingu a spolehlivého poskytování služeb.

## Popis

Internetwork Packet Exchange (IPX) je klíčový architektonický rámec definovaný asociací GSM Association ([GSMA](/mobilnisite/slovnik/gsma/)) a přijatý ve standardech 3GPP pro propojování různých IP sítí poskytovatelů služeb. Není to jediný protokol, ale komplexní soubor komerčních a technických principů postavených na vrcholu IP sítí. Primárním cílem je poskytnout důvěryhodnou, spravovanou páteř pro výměnu paketově přepínaného provozu, která nahrazuje starší a méně efektivní okruhově přepínaná propojení. Vytváří multiservisní IP síť, která globálně propojuje mobilní síťové operátory ([MNO](/mobilnisite/slovnik/mno/)), pevné operátory, poskytovatele aplikačních služeb a poskytovatele obsahu.

Architektonicky je IPX založen na modelu hub-and-spoke, kde IPX Poskytovatelé fungují jako rozbočovače (huby) připojující více klientských sítí (spokes). IPX Poskytovatel je přepravce, který splňuje přísné specifikace GSMA pro zabezpečení, kvalitu služeb (QoS) a smlouvy o úrovni služeb (SLA). Rámec vyžaduje použití privátních IP adres (např. z rozsahu 10.0.0.0/8) a [IPsec](/mobilnisite/slovnik/ipsec/) tunelů nebo [MPLS](/mobilnisite/slovnik/mpls/) VPN k vytvoření zabezpečené, uzavřené skupiny uživatelů. Tím je provoz izolován od veřejného internetu, což zajišťuje důvěrnost, integritu a předvídatelný výkon. Klíčová rozhraní v ekosystému IPX zahrnují Network-to-Network Interface ([NNI](/mobilnisite/slovnik/nni/)) mezi IPX Poskytovatelem a klientskou sítí a Inter-IPX Provider Interface (IPI) pro propojení mezi různými IPX Poskytovateli.

Z funkčního hlediska IPX podporuje více služeb současně přes jediné propojení. To zahrnuje [GRX](/mobilnisite/slovnik/grx/) ([GPRS](/mobilnisite/slovnik/gprs/) Roaming Exchange) pro datový roaming, voice over IP (VoIP) pro služby založené na IMS, jako je VoLTE a VoWiFi, SMS over IP (SMSoIP) a rich communication services (RCS). Základním technickým mechanismem je použití proxy pro signalizaci Diameter a SIP v rámci IPX sítě pro správné směrování zpráv řídicí roviny mezi domovskou a navštívenou sítí. Rámec IPX vynucuje striktní klasifikaci QoS, typicky pomocí DiffServ Code Points ([DSCP](/mobilnisite/slovnik/dscp/)), pro upřednostnění provozu v reálném čase, jako je hlas, před méně časově citlivými daty. Zahrnuje také komplexní modely fakturace za přenos a roaming, zúčtování a podrobné reportování provozu, které jsou nezbytné pro komerční interoperabilitu mezi operátory.

## K čemu slouží

IPX byl vytvořen k řešení klíčových obchodních a technických výzev spojených s propojováním různorodých sítí operátorů v se vyvíjejícím prostředí plně založeném na IP. Před zavedením IPX mezinárodní roaming a propojení silně závisely na okruhově přepínaných technologiích, jako je SS7 pro hlas a SMS, a na GRX – best-effort IP síti – pro GPRS datový roaming. Když operátoři migrovali své základní sítě na architektury založené na IP, jako je IMS, bylo potřeba nové, robustnější propojení. Veřejný internet byl nevhodný kvůli nedostatku zabezpečení, nepředvídatelné latenci, zpoždění (jitteru), ztrátě paketů a absenci komerčních zúčtovacích modelů. Operátoři potřebovali alternativu na úrovni přepravců, která by mohla garantovat výkon a zabezpečení nezbytné pro služby v reálném čase generující příjmy.

Zavedení IPX poskytlo tuto spravovanou, multiservisní IP páteř. Vyřešilo problém fragmentace služeb tím, že umožnilo doručování hlasových, zprávových a datových služeb přes jediné, zabezpečené propojení s garantovanou kvalitou služeb (QoS) od konce do konce. To bylo obzvláště zásadní pro uvedení služeb hlasu ve vysoké kvalitě, jako je VoLTE, kde je klíčová konzistentně nízká latence a vysoká kvalita zvuku. Dále IPX stanovil standardizovaný komerční rámec s jasnými rolemi (IPX Poskytovatel, Zákaznická síť), SLA a fakturačními mechanismy, což snížilo složitost a podpořilo globální interoperabilitu služeb. Umožnil škálovatelné a efektivní zavádění nových služeb založených na IP napříč hranicemi operátorů a vytvořil páteř moderní globální telekomunikace.

## Klíčové vlastnosti

- Garance kvality služeb (QoS) od konce do konce s klasifikací a prioritizací provozu
- Vylepšené zabezpečení prostřednictvím použití privátních IP adres a povinných IPsec/MPLS VPN tunelů
- Multiservisní schopnost podporující GRX, VoLTE, VoWiFi, SMS a RCS přes jediné propojení
- Standardizované komerční a provozní modely včetně SLA a procesů zúčtování
- Směrování založené na proxy Diameter a SIP pro efektivní signalizaci řídicí roviny mezi sítěmi
- Globální dosah usnadněný propojením více IPX Poskytovatelů přes IPI

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 22.893** (Rel-10) — IP Service Interconnection Requirements Study
- **TS 22.894** (Rel-11) — IMS Network-Independent Public User Identities Study
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TS 29.809** (Rel-12) — Diameter Overload Control Study
- **TS 29.819** (Rel-13) — Diameter Base Protocol Update Analysis
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.517** (Rel-20) — 5G Security Assurance Specification (SCAS)
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G

---

📖 **Anglický originál a plná specifikace:** [IPX na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipx/)
