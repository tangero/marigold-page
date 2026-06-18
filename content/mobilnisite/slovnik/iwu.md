---
slug: "iwu"
url: "/mobilnisite/slovnik/iwu/"
type: "slovnik"
title: "IWU – Interworking Unit"
date: 2025-01-01
abbr: "IWU"
fullName: "Interworking Unit"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iwu/"
summary: "Funkční jednotka, která zajišťuje přizpůsobení mezi různými síťovými protokoly nebo rozhraními a tím umožňuje komunikaci mezi heterogenními systémy. Často se s ní pracuje při propojování se staršími n"
---

IWU je funkční jednotka, která zajišťuje přizpůsobení mezi různými síťovými protokoly nebo rozhraními, aby umožnila komunikaci mezi heterogenními systémy, například se staršími nebo externími sítěmi.

## Popis

Interworking Unit (IWU) je široký koncept 3GPP představující funkční entitu odpovědnou za přizpůsobení a konverzi protokolů mezi různými telekomunikačními systémy. Není to jediný fyzický uzel, ale logická sada funkcí, které mohou být implementovány v různých síťových prvcích, jako jsou [MSC](/mobilnisite/slovnik/msc/), [SGSN](/mobilnisite/slovnik/sgsn/) nebo specializované brány. Hlavní úlohou IWU je řešit nekompatibility v signalizaci, datových formátech a procedurách mezi sítí 3GPP a externí sítí, jako je např. pevná datová síť (např. X.25, Frame Relay) nebo jiná mobilní síť s odlišnou technologickou základnou.

Z architektonického hlediska jsou funkce IWU definovány pro jednotlivá rozhraní a služby. Například v kontextu paketově přepínaných služeb v [GPRS](/mobilnisite/slovnik/gprs/) se IWU nachází mezi Serving GPRS Support Node (SGSN) nebo Gateway GPRS Support Node (GGSN) a externí Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)). Přizpůsobuje protokoly GPRS (jako [GTP](/mobilnisite/slovnik/gtp/)) protokolům externí sítě (jako X.75 nebo IP). To zahrnuje mapování paketových formátů, adresních schémat (např. IP adres na X.121 adresy pro X.25) a mechanismů obnovy po chybě. Pro spojově přepínané služby může být IWU součástí MSC pro zvládnutí propojení s [ISDN](/mobilnisite/slovnik/isdn/) nebo [PSTN](/mobilnisite/slovnik/pstn/), kde provádí podobná přizpůsobení pro signalizaci a přenosové kanály.

Jak to funguje, je vysoce specifické pro daný scénář propojení. IWU funguje jako překladač protokolů. Přijímá protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) z jedné sítě, interpretuje je podle pravidel této sítě a poté generuje ekvivalentní PDU pro cílovou síť, přičemž zajišťuje sémantickou a syntaktickou správnost. Tento proces může zahrnovat správu stavu, protože některé protokoly jsou stavové (jako TCP spojení nebo X.25 virtuální okruh). IWU musí udržovat stav relací, které jí procházejí, a provádět odpovídající mapování. Její implementace je klíčová pro služby, jako je SMS interworking, kde IWMSC nebo SMS-GMSC používá funkce IWU pro připojení k externím Short Message Entities (SME) přes protokoly jako EIA/TIA-637. Specifikace (např. 23.040 pro SMS) podrobně popisují požadované adaptační vrstvy.

## K čemu slouží

IWU bylo koncipováno k řešení výzvy integrace vznikajících mobilních paketových datových služeb (GPRS, později UMTS) s existující globální sítí pevných a mobilních datových sítí. Na přelomu 90. let a počátku 21. století spolu koexistovaly četné paketově přepínané sítě, včetně X.25, Frame Relay a rodícího se Internetu (IP). Účelem IWU bylo poskytnout standardizovanou metodu, aby GPRS síť mobilního operátora mohla nabízet připojení svým účastníkům k podnikovým X.25 sítím nebo raným internetovým službám, aniž by vyžadovala podporu všech možných externích protokolů v každém mobilním zařízení nebo síťovém uzlu.

Řešilo problém heterogenity protokolů. Před standardizovanými funkcemi IWU vyžadovalo propojení proprietární řešení, což bránilo interoperability a roamingu. Definováním schopností IWU ve specifikacích, jako je 23.060 (GPRS), umožnilo 3GPP konzistentní přístup k různým externím paketovým datovým sítím. Odkazy na CCITT X.71 a X.75 (standardy ITU-T pro propojování datových sítí) zdůrazňují jeho kořeny v připojování ke klasickým veřejným datovým sítím. IWU abstrahovalo složitost externích sítí od jádra mobilní paketové sítě, což umožnilo SGSN a GGSN se soustředit na správu mobility a směrování IP, zatímco IWU zvládalo "okrajové" přizpůsobení. Tento modulární přístup byl klíčový pro postupnou evoluci od převahy spojového přepojování k převaze paketového přepojování v mobilních sítích.

## Klíčové vlastnosti

- Přizpůsobení a konverze protokolů mezi protokoly definovanými 3GPP a protokoly externích sítí (např. GTP na X.75)
- Mapování adres mezi různými číslovacími/adresovacími schématy (např. IP na X.121)
- Podpora propojení se staršími datovými sítěmi, jako jsou X.25 a Frame Relay
- Funkcionalita definovaná pro konkrétní rozhraní a služby (např. rozhraní Gi pro připojení k PDN)
- Může být implementována jako integrovaná funkce uvnitř síťového uzlu nebo jako samostatná jednotka
- Umožňuje mobilní přístup k široké škále služeb externích paketových datových sítí

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [IWU na 3GPP Explorer](https://3gpp-explorer.com/glossary/iwu/)
