---
slug: "lcs"
url: "/mobilnisite/slovnik/lcs/"
type: "slovnik"
title: "LCS – Location Services"
date: 2026-01-01
abbr: "LCS"
fullName: "Location Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcs/"
summary: "Location Services (LCS) je standardizovaná architektura 3GPP a soubor protokolů určených ke stanovení geografické polohy mobilního zařízení (UE). Podporuje řadu metod určení polohy (např. A-GNSS, OTDO"
---

LCS je standardizovaná architektura 3GPP a soubor protokolů určených ke stanovení geografické polohy mobilního zařízení, aby bylo možné poskytnout informace o poloze autorizovaným klientům.

## Popis

Location Services (LCS) je komplexní služební schopnost v systémech 3GPP, která umožňuje síti nebo autorizovaným externím klientům získat odhad geografické polohy uživatelského zařízení (UE). Není to jednotná technologie, ale celý architektonický rámec definovaný v jádrové síti i rádiovém přístupu, který podporuje více metod určení polohy. Architektura LCS definuje funkční role, jako je LCS klient (entita vyžadující polohu), LCS server (řídící požadavky na polohu, často Gateway Mobile Location Centre - [GMLC](/mobilnisite/slovnik/gmlc/)) a funkce určení polohy na základě UE nebo síť.

Proces určení polohy typicky začíná, když LCS klient zasílá síti požadavek na polohu, často prostřednictvím GMLC. GMLC požadavek ověří a autorizuje, pak ho směruje příslušné síťové uzlu (např. [MSC](/mobilnisite/slovnik/msc/) pro [CS](/mobilnisite/slovnik/cs/), [MME](/mobilnisite/slovnik/mme/) pro PS). Jádrová síťový uzel pak zapojí příslušný rádiový přístupový síť (RAN) k provedení měření pro určení polohy. Klíčové metody určení polohy zahrnují: Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), kde síť poskytuje pomocná data GNSS přijímači UE pro zvýšení rychlosti a přesnosti; Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), kde UE měří časové rozdíly od více základových stanic; a Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)), který využívá identitu obsluhující buňky plus časový předstih a měření úhlu příchodu pro přesnější určení než základní Cell ID.

RAN, v některých případech vybavený Location Measurement Unit (LMU), umožňuje tyto měření. Pro metody na straně UE si UE vypočítává vlastní polohu. Pro metody asistované UE nebo na straně síť jsou výsledky měření zasílány serveru určení polohy v síti (např. Evolved Serving Mobile Location Centre - E-SMLC v LTE, Location Management Function - LMF v 5GC) pro výpočet. Výsledný odhad polohy (např. zeměpisná šířka, délka, nepřesnost) je pak formátován a doručen zpět vyžadujícímu LCS klientovi prostřednictvím GMLC. Celý proces řídí striktní kontrola ochrany soukromí; účastník UE musí obecně mít nastavenou ochranu soukromí, která takový požadavek povoluje, kromě povinných služeb jako nouzové volání.

## K čemu slouží

LCS byl vytvořen, aby standardizoval určení polohy mobilních zařízení v globálním ekosystému mobilních síť, řešíc kritickou potřebu spolehlivých, přesných a síťově efektivních informací o poloze. Prvotními hybateli byly regulativní požadavky, nejvýznamněji pro určení polohy nouzových volajících (E911 v USA, E112 v Evropě). Před standardizací LCS existovaly proprietární řešení, ale ty postrádaly interoperabilitu, bránily roamingu a limitovaly rozvoj širokého komerčního trhu služeb na základě polohy (LBS).

Rámec 3GPP LCS, uvedený ve vydání 99, poskytl jednotnou, škálovatelnou architekturu, která mohla s síť evolvovat. Oddělil služební logiku od podkladových technologií určení polohy, umožňujíc postupně integrovat nové metody (jako OTDOA nebo A-GNSS) bez přestavby celé služební vrstvy. Tím byly řešeny limity jednoduchého určení polohy na základě Cell-ID, které nabízelo nízkou přesnost, obzvláště v venkovských oblastech. Standardizací rozhraní jako Le rozhraní pro externí klienty a SLg/SLh rozhraní mezi jádrovou síť a uzly určení polohy umožnil LCS třetím stranám (poskytovatelům aplikací, operátorům síť, záchranným službám) přístupovat datům o poloze konzistentním, bezpečným a ohleduplným k ochraně soukromí způsobem. Jeho vytvoření bylo základním pro bezpečnost, zákonný odposlech, řízení vozového parku, navigaci a širokou škálu moderních aplikací využívajících polohu.

## Klíčové vlastnosti

- Standardizovaná služební architektura s definovanými rolemi (Klient, Server, GMLC, LMF/E-SMLC)
- Podpora více metod určení polohy (A-GNSS, OTDOA, E-CID, UTDOA, atd.)
- Koncová ochrana soukromí a autorizační kontrola polohy účastníka
- Rozhraní pro přístup externích aplikací (Le rozhraní)
- Integrace záchranných služeb (např. NG-eCall, nouzové IoT)
- Kontinuální evoluce pro podporu nových technologií (určení polohy 5G NR, určení polohy přes sidelink)

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.899** (Rel-14) — Study on Enhanced User Location Reporting
- **TR 22.935** (Rel-13) — LCS Feasibility Study for 3GPP-WLAN Interworking
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.240** (Rel-19) — 3GPP Generic User Profile (GUP) Architecture
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- … a dalších 54 specifikací

---

📖 **Anglický originál a plná specifikace:** [LCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcs/)
