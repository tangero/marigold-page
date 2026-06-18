---
slug: "msc"
url: "/mobilnisite/slovnik/msc/"
type: "slovnik"
title: "MSC – Mobile Services Switching Centre"
date: 2026-01-01
abbr: "MSC"
fullName: "Mobile Services Switching Centre"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/msc/"
summary: "Ústředna jádra sítě druhé generace (2G), která zpracovává okruhově přepínané hlasové hovory a správu mobility v sítích GSM. Připojuje se k rádiové přístupové síti přes rozhraní A a spravuje směrování"
---

MSC je ústředna jádra sítě v sítích GSM, která zpracovává okruhově přepínané hlasové hovory, správu mobility, směrování hovorů a předávání spojení a připojuje se k rádiovému přístupu přes rozhraní A.

## Popis

Mobile Services Switching Centre (MSC) je centrální komponenta sítě GSM (Global System for Mobile Communications) a časného okruhově přepínaného jádra sítě 3GPP. Funguje jako telefonní ústředna pro mobilní účastníky a poskytuje přepínání hovorů, správu mobility a doplňkové služby. Architektonicky se MSC rozhraním A připojuje k podsystému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), které přenáší signalizaci (pomocí Base Station System Application Part, [BSSAP](/mobilnisite/slovnik/bssap/)) i uživatelský provoz (okruhově přepínaný hlas). Také se připojuje k dalším MSC, domovskému registru polohy ([HLR](/mobilnisite/slovnik/hlr/)), návštěvnickému registru polohy ([VLR](/mobilnisite/slovnik/vlr/)) a veřejné telefonní síti ([PSTN](/mobilnisite/slovnik/pstn/)) nebo jiným externím sítím.

Provozně je MSC zodpovědná za řízení hovorů, včetně navázání, směrování a ukončení okruhově přepínaných hovorů iniciovaných z mobilního zařízení i směřujících do něj. Zpracovává funkce správy mobility, jako je registrace polohy, aktualizace polohy a předávání spojení mezi různými buňkami nebo MSC, aby udržela kontinuitu hovoru při pohybu uživatele. MSC také komunikuje s VLR (často umístěným společně), aby získala profil účastníka a servisní data pro autentizaci a autorizaci služeb. Pro doplňkové služby, jako je přesměrování hovoru, zákazy a konferenční hovory, MSC provádí potřebnou logiku a komunikuje s HLR.

V hierarchii sítě může MSC sloužit jako Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)), když se připojuje k externím sítím, a určuje směrování pro příchozí hovory dotazem na HLR. Její role je čistě okruhově přepínaná, zpracovává hlasové kanály založené na časovém multiplexu ([TDM](/mobilnisite/slovnik/tdm/)). MSC nespravuje paketově přepínaná data; tuto funkci zajišťují samostatné uzly jako [SGSN](/mobilnisite/slovnik/sgsn/) v paketovém jádru. Její provoz je definován rozsáhlou sadou specifikací 3GPP pokrývajících protokoly, rozhraní a služby, což z ní činí vysoce standardizovaný a interoperabilní síťový prvek.

## K čemu slouží

MSC byla vytvořena, aby poskytovala základní přepínací funkčnost pro sítě mobilní telefonie, umožňovala automatizované směrování hovorů a mobilitu účastníků. Před buněčnými systémy byla mobilní telefonie manuální nebo používala primitivní rádiové systémy bez plynulého předávání spojení. MSC jako součást architektury GSM vyřešila problém automatizace přepínání hovorů a umožnila uživatelům pohybovat se v různých oblastech pokrytí při zachování aktivního hovoru, což je základní požadavek pro masovou mobilní komunikaci.

Odstranila omezení dřívějších analogových mobilních systémů (jako 1G) zavedením digitálního přepínání a standardizovaných rozhraní, což zlepšilo kvalitu hlasu, zabezpečení a efektivitu sítě. Oddělení řídicí a uživatelské roviny v MSC spolu s její integrací s databázemi jako HLR/VLR umožnilo pokročilé funkce, jako je mezinárodní roaming a široká škála služeb pro účastníky. Její vytvoření bylo motivováno potřebou škálovatelného, spolehlivého a standardizovaného prvku jádra sítě pro podporu explozivního růstu služeb GSM po celém světě.

## Klíčové vlastnosti

- Řízení a přepínání okruhově přepínaných hovorů pro hlasové a CS datové služby
- Správa mobility včetně registrace polohy, aktualizace a provádění předávání spojení
- Rozhraní k rádiové přístupové síti (BSS) přes standardizované rozhraní A
- Integrace s VLR pro správu dat účastníků a autentizaci
- Brána (jako GMSC) pro propojení s externími sítěmi jako PSTN
- Podpora široké škály doplňkových služeb (např. přesměrování hovoru, zákazy)

## Související pojmy

- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.053** (Rel-19) — Tandem Free Operation (TFO) Stage 1
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- … a dalších 62 specifikací

---

📖 **Anglický originál a plná specifikace:** [MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/msc/)
