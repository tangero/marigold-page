---
slug: "ip"
url: "/mobilnisite/slovnik/ip/"
type: "slovnik"
title: "IP – IP Packet eXchange"
date: 2026-01-01
abbr: "IP"
fullName: "IP Packet eXchange"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ip/"
summary: "Standardizovaný, multislužební rámec pro IP propojení definovaný asociací GSMA a přijatý konsorciem 3GPP. Prostřednictvím akreditovaných IPX poskytovatelů umožňuje zabezpečené propojení mezi poskytova"
---

IP je standardizovaný, multislužební rámec pro IP propojení, který prostřednictvím akreditovaných IPX poskytovatelů umožňuje zabezpečené propojení mezi poskytovateli služeb se zaručenou kvalitou.

## Popis

IP Packet eXchange ([IPX](/mobilnisite/slovnik/ipx/)) je komplexní rámec pro propojení služeb, původně definovaný GSM Association ([GSMA](/mobilnisite/slovnik/gsma/)) a hojně odkazovaný ve specifikacích 3GPP pro IP služby mezi operátory. Nejde o jediný protokol, ale o vztahový model, soubor požadavků a komerční ekosystém navržený pro propojení IP služeb mezi různými poskytovateli služeb ([SP](/mobilnisite/slovnik/sp/)), jako jsou mobilní síťoví operátoři ([MNO](/mobilnisite/slovnik/mno/)), poskytovatelé aplikačních služeb a poskytovatelé obsahu. Ústřední entitou v tomto modelu je IPX poskytovatel (IPXP), specializovaný přepravce, který funguje jako zprostředkovatel a poskytuje spravovanou, hubovou propojovací platformu.

Architektonicky IPX vytváří vrstvený peer-to-peer model, kde se poskytovatelé služeb nepřipojují přímo k sobě v plné síti, ale připojují se k jednomu nebo více IPX poskytovatelům. IPX poskytovatel pak spravuje konektivitu ke všem ostatním partnerským poskytovatelům služeb ve své síti. Tento hub-and-spoke model výrazně snižuje složitost bilaterálních dohod a technických integrací. Rámec ukládá přísné požadavky napříč několika vrstvami: Síťová vrstva vyžaduje robustní, privátní IP konektivitu (často využívající [MPLS](/mobilnisite/slovnik/mpls/)) se zaručenými smlouvami o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) pro dostupnost, latenci, zkreslení zpoždění a ztrátu paketů. Služební vrstva definuje, jak jsou přenášeny konkrétní služby jako Voice over LTE (VoLTE), [SMS](/mobilnisite/slovnik/sms/) over IP a služby rich communication ([RCS](/mobilnisite/slovnik/rcs/)), včetně aspektů označování kvality služeb (QoS), identifikace provozu a funkcí session border control (SBC).

Klíčové součásti ekosystému IPX zahrnují síť IPX poskytovatele, která obsahuje SBC pro zabezpečení a interoperabilitu, Diameter agenty pro signalizaci a deep packet inspection (DPI) pro služebně orientované směrování a regulaci provozu. Rámec také definuje komerční principy, jako jsou bilaterální, netranzitní dohody a 'waterfall' model pro finanční vyúčtování, který zjednodušuje fakturaci. Z pohledu 3GPP je IPX doporučovanou páteří pro služby mezi operátory založené na IMS (jako je roaming VoLTE), což umožňuje bezproblémové poskytování služeb přes hranice operátorů. Funguje tak, že zajišťuje zabezpečené tunelování služební signalizace (SIP, Diameter) a mediálních toků (RTP) přes IPX síť s odpovídajícím zacházením z hlediska QoS, čímž udržuje kvalitu a zabezpečení služeb od konce ke konci, které veřejný internet nezaručuje. Jeho úlohou je poskytovat důvěryhodný, 'carrier-grade' infrastrukturní systém pro přechod globálního telekomunikačního průmyslu na plně IP služby.

## K čemu slouží

IPX byl vytvořen k řešení kritických výzev, které vznikly při migraci telekomunikačního průmyslu z legacy okruhově přepínaného propojení (např. využívajícího SS7 a TDM linky) na paketově přepínané, IP služby. Veřejný internet, i když je všudypřítomný, postrádá zaručenou kvalitu, zabezpečení a komerční rámce nezbytné pro služby na úrovni přepravců, jako je hlas a messaging. Přímé bilaterální IP propojení mezi stovkami operátorů by bylo technicky a komerčně neškálovatelné. IPX tyto problémy řešil zavedením standardizovaného, multislužebního modelu propojení.

Historicky sloužil GRX (GPRS Roaming Exchange) podobnému účelu pro základní roaming dat GPRS, ale byl omezeného rozsahu. Vývoj směrem k pokročilým IP službám, jako je HD hlas založený na IMS, videohovory a RCS, vyžadoval robustnější rámec. Motivací pro IPX byla potřeba jedné, jednotné propojovací platformy, která by mohla podporovat všechny tyto služby s kvalitou od konce ke konci (QoS), zabezpečením (např. prostřednictvím privátních sítí a SBC) a zjednodušeným komerčním vyúčtováním. Řeší omezení veřejného internetu (best-effort, nezabezpečený) a omezení fragmentovaného, služebně specifického přístupu k propojení.

Jeho vytvoření bylo řízeno mobilními operátory a asociací GSMA, aby zajistilo úspěšné a výnosné nasazení služeb příští generace. Poskytuje budoucí perspektivu, umožňuje nejen služby mezi osobami, ale také vznikající služby IoT a M2M, které vyžadují spolehlivou globální konektivitu s nízkou latencí. IPX je základním kamenem, který umožňuje operátorům nabízet bezproblémové zážitky 'kdekoli a kdykoli' pro své účastníky při zachování kontroly nad kvalitou služeb a toky příjmů ve světě plně IP.

## Klíčové vlastnosti

- Hubový model propojení založený na akreditovaných IPX poskytovatelích (IPXP)
- Smlouvy o úrovni služeb (SLA) od konce ke konci pro výkon sítě (latence, zkreslení zpoždění, ztráta)
- Podpora více služeb (Hlas, Video, Messaging, Data) přes jediné propojení
- Vestavěné zabezpečení prostřednictvím privátních IP sítí a povinného Session Border Control (SBC)
- Komerční rámec s bilaterálními dohodami a waterfall modelem finančního vyúčtování
- Bezproblémová podpora roamingu služeb 3GPP IMS (např. VoLTE, ViLTE)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.250** (Rel-19) — IMS Group Management Requirements
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.340** (Rel-19) — IMS Messaging Stage 1 Requirements
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TR 22.893** (Rel-10) — IP Service Interconnection Requirements Study
- **TR 22.940** (Rel-19) — IMS Messaging Requirements Analysis
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- … a dalších 250 specifikací

---

📖 **Anglický originál a plná specifikace:** [IP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ip/)
