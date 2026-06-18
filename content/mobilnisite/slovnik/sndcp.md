---
slug: "sndcp"
url: "/mobilnisite/slovnik/sndcp/"
type: "slovnik"
title: "SNDCP – Sub-Network Dependent Convergence Protocol"
date: 2025-01-01
abbr: "SNDCP"
fullName: "Sub-Network Dependent Convergence Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sndcp/"
summary: "Protokol, který implementuje funkce vrstvy SNDC v GPRS a UMTS. Definuje podrobné procedury a formáty paketů pro kompresi dat, segmentaci a rozlišování protokolů mezi MS a SGSN. SNDCP je klíčový pro op"
---

SNDCP je Sub-Network Dependent Convergence Protocol v GPRS a UMTS, který zajišťuje kompresi dat, segmentaci a rozlišování protokolů mezi mobilní stanicí a SGSN za účelem optimalizace efektivity rozhraní rádiového přenosu.

## Popis

Sub-Network Dependent Convergence Protocol (SNDCP) je konkrétní specifikace protokolu, která realizuje funkce vrstvy SubNetwork Dependent Convergence ([SNDC](/mobilnisite/slovnik/sndc/)). Jde o peer-to-peer protokol fungující mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v sítích GPRS a UMTS. Definován v široké řadě specifikací 3GPP (např. TS 23.060, 24.065, 44.065) poskytuje SNDCP detailní mechanismy pro přizpůsobení protokolů síťové vrstvy podkladové vrstvě Logical Link Control ([LLC](/mobilnisite/slovnik/llc/)) a rozhraní rádiového přenosu.

Architektonicky se SNDCP nachází nad vrstvou LLC a pod protokoly síťové vrstvy, jako je IP. Spravuje více SNDCP kontextů, z nichž každý je spojen s aktivním Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) kontextem. Činnost protokolu je založena na zpracování Network layer Protocol Data Units (N-PDUs). Mezi klíčové součásti protokolu SNDCP patří kompresní entity, funkce segmentace/sestavování a řídicí logika protokolu. Kompresní entita může implementovat více kompresních algoritmů, jako je V.42bis pro obecnou kompresi dat a specifické schémata komprese hlaviček (např. pro [TCP/IP](/mobilnisite/slovnik/tcp-ip/) hlavičky). Tyto algoritmy jsou vyjednány během aktivace PDP kontextu. Funkce segmentace rozkládá [N-PDU](/mobilnisite/slovnik/n-pdu/) (po případné kompresi) na SNDCP Data Units, které odpovídají maximální přenosové jednotce (MTU) podporované podkladovou vrstvou LLC.

Protokol funguje prostřednictvím výměny SNDCP PDU, které se skládají z hlavičky a datové části. Hlavička SNDCP obsahuje kritické řídicí informace, včetně Network Layer Protocol Identifier (NLPI), který identifikuje protokol zapouzdřeného N-PDU (např. IPv4, IPv6), a pole Data Compression Protocol (DCP) udávající použitý kompresní algoritmus. U segmentovaných PDU obsahuje hlavička pořadová čísla a další příznaky umožňující správné sestavení na straně přijímače. Proces začíná, když síťová vrstva předá N-PDU. SNDCP vybere příslušný kontext, aplikuje vyjednanou kompresi, v případě potřeby data segmentuje, připojí SNDCP hlavičku a předá SNDCP-PDU vrstvě LLC. Na přijímací straně SNDCP použije NLPI k nasměrování dekomprimovaného a sestaveného N-PDU správné entitě síťové vrstvy. Celý tento proces je transparentní pro vyšší vrstvy a je klíčový pro zachování efektivity a spolehlivosti přes rádiové spojení, které má ve srovnání s pevnými sítěmi vyšší latenci a nižší přenosovou kapacitu.

## K čemu slouží

SNDCP byl vytvořen, aby poskytl standardizovaný, implementovatelný protokol pro konvergenční funkce vyžadované v GPRS. Zatímco SNDC definovala architektonickou vrstvu a její odpovědnosti, SNDCP poskytuje přesné formáty paketů, stavové automaty a procedury potřebné pro výrobce k výstavbě interoperabilních mobilních stanic a síťových zařízení. Problém, který řeší, je absence detailního protokolu pro efektivní mapování libovolného síťového provozu na přenosové mechanismy GPRS.

Jeho vývoj byl motivován potřebou robustního protokolu, který by dokázal zpracovat heterogenitu uživatelských dat a optimalizovat výkon. Před GPRS využívaly datové služby v celulárních sítích spojově orientovaná spojení nebo jednoduché paketové protokoly bez sofistikovaných konvergenčních funkcí. SNDCP zavedl povinné a volitelné kompresní techniky pro řešení režie hlaviček síťových protokolů, která je významná u malých paketů běžných při prohlížení webu a zasílání zpráv. Funkce segmentace řeší nesoulad mezi typickými velikostmi IP paketů (např. 1500 bajtů) a mnohem menšími rádiovými bloky (např. několik set bitů). Standardizací těchto procedur v SNDCP zajistil 3GPP, že zařízení a sítě různých výrobců mohou bezproblémově spolupracovat při poskytování efektivních paketových datových služeb, což umožnilo mobilní datovou revoluci. Položil základy pro trvalé internetové připojení, které se později vyvinulo v HSPA a LTE.

## Klíčové vlastnosti

- Specifikuje formáty paketů a hlaviček pro vrstvu SNDC, včetně polí NLPI a DCP
- Vyjednává a aplikuje kompresní algoritmy dat (např. V.42bis) a schémata komprese hlaviček během aktivace PDP kontextu
- Provádí segmentaci velkých N-PDU a jejich sestavování pomocí pořadových čísel
- Spravuje více SNDCP kontextů, z nichž každý je asociován s aktivním PDP kontextem a síťovým protokolem
- Definuje peer-to-peer procedury mezi MS a SGSN pro spolehlivou adaptaci přenosu dat
- Funguje transparentně vůči protokolům vyšších vrstev a poskytuje bezproblémové rozhraní

## Související pojmy

- [SNDC – SubNetwork Dependent Convergence](/mobilnisite/slovnik/sndc/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [NSAPI – Network layer Service Access Point Identifier](/mobilnisite/slovnik/nsapi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.065** (Rel-19) — GPRS SNDCP Specification
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- **TS 45.820** (Rel-13) — CIoT for Internet of Things
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [SNDCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sndcp/)
