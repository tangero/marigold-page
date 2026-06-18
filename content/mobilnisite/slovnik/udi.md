---
slug: "udi"
url: "/mobilnisite/slovnik/udi/"
type: "slovnik"
title: "UDI – Unrestricted Digital Interface"
date: 2025-01-01
abbr: "UDI"
fullName: "Unrestricted Digital Interface"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udi/"
summary: "Okruhově spínaná přenosová služba poskytující transparentní, neomezený 64 kbit/s digitální datový kanál, primárně založená na technologii ISDN B-kanálu. Podporuje aplikace v reálném čase, jako je vide"
---

UDI je okruhově spínaná přenosová služba (bearer service) poskytující transparentní, neomezený 64 kbit/s digitální kanál pro aplikace v reálném čase, jako je videokonferencing, v tradičních telekomunikačních sítích.

## Popis

Unrestricted Digital Interface (UDI) je základní okruhově spínaná přenosová služba definovaná v rámci specifikací 3GPP, která poskytuje transparentní, plně duplexní 64 kbit/s digitální datovou cestu mezi koncovými body terminálů. Technicky nabízí schopnost přenosu 'neomezených' (unrestricted) digitálních informací, což znamená, že síť neinterpretuje ani nemodifikuje bitovou sekvenci (kromě nezbytného řádkového kódování pro přenos) a zachází s ní jako s čistým kanálem. To je v protikladu k 'omezeným' (restricted) službám, jako je 3,1 kHz audio, které jsou optimalizovány pro hlas. Rychlost 64 kbit/s je odvozena od standardu [ISDN](/mobilnisite/slovnik/isdn/) B-kanálu pro rozhraní PRI (Primary Rate Interface) a [BRI](/mobilnisite/slovnik/bri/) (Basic Rate Interface), který tvoří základnu pro jeho implementaci v pevných i mobilních sítích.

V kontextu 3GPP je UDI implementována jako součást okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) domény, primárně v sítích GSM a UMTS. Když mobilní stanice požádá o UDI přenos, síť naváže okruhově spínané spojení pomocí stejných signalizačních procedur jako u hovoru (např. prostřednictvím protokolů [DTAP](/mobilnisite/slovnik/dtap/) a [BSSAP](/mobilnisite/slovnik/bssap/)), ale vyjedná informační prvek Bearer Capability specifikující 'Unrestricted Digital Information' jako schopnost přenosu informací. Přístupová rádiová síť (např. [GERAN](/mobilnisite/slovnik/geran/) nebo [UTRAN](/mobilnisite/slovnik/utran/)) poté přidělí příslušný provozní kanál ([TCH/F](/mobilnisite/slovnik/tch-f/) pro GSM nebo CS datový kanál v UMTS) schopný podporovat rychlost 64 kbit/s, často s využitím adaptivních vícerychlostních kodeků nebo transparentních datových protokolů. Jádrová síť, konkrétně MSC, spolupracuje s externí ISDN nebo PSTN sítí, aby tento transparentní kanál rozšířila ke vzdálené straně.

Z architektonického hlediska služba UDI zahrnuje několik klíčových síťových prvků: mobilní stanici (MS) s podporou UDI, subsystém základnové stanice (BSS), ústřednu mobilní sítě (MSC) a funkci pro vzájemné propojení (IWF), která může v případě potřeby provádět přizpůsobení rychlosti a konverzi protokolů. Služba funguje end-to-end; síť 3GPP slouží jako přenosové médium. Mezi klíčové zapojené protokoly patří LAPDm na rádiovém rozhraní pro spolehlivou spojovou vrstvu a série doporučení ITU-T I.460 pro přizpůsobení rychlosti, což zajišťuje, že datový proud uživatele 64 kbit/s je správně přizpůsoben možnostem rádiového rozhraní. UDI podporuje jak spojově orientované, tak nespojové protokoly vyšších vrstev (dle uživatelského zařízení), což ji činí univerzální pro různé starší datové aplikace.

## K čemu slouží

UDI byla vytvořena za účelem poskytování kvalitní, spolehlivé digitální datové služby přes telekomunikační sítě, čímž překlenula mezeru mezi tradičními analogovými modemy a moderními paketově spínanými daty. Její kořeny sahají do éry ISDN 80. let 20. století, kde byl 64 kbit/s B-kanál standardizován pro digitální hlas a data. 3GPP tento koncept převzalo, aby umožnilo mobilním sítím nabízet kompatibilní, vysokorychlostní datové služby pro obchodní a profesionální aplikace, jako je fax skupiny 4, videokonferencing (H.320) a zabezpečený přenos dat, které vyžadovaly garantovanou šířku pásma a nízký jitter, jež rané paketové služby jako GPRS nenabízely.

Hlavním problémem, který UDI řešila, bylo omezení analogových modemových připojení přes mobilní sítě, která byla pomalá (zpočátku 9,6 kbit/s), nespolehlivá a nekompatibilní se službami založenými na ISDN v pevné síti. Poskytnutím transparentní 64 kbit/s digitální 'trubky' umožnila UDI mobilním uživatelům bezproblémově se připojovat k ISDN terminálům, podnikovým LAN přes terminálové adaptéry a videokonferenčním systémům. To bylo klíčové pro rané přijetí mobilních dat ve vertikálních trzích. Řešila potřebu spolehlivosti okruhového spínání – kde je šířka pásma vyhrazena a latence předvídatelná – což bylo před rozšířeným nasazením paketových sítí s podporou QoS zásadní pro aplikace v reálném čase citlivé na zpoždění.

Motivace pro její zařazení a pokračující odkazování napříč četnými releasy 3GPP (Rel-4 až Rel-19) pramení z podpory starších služeb a regulatorních požadavků. I když se paketově spínané LTE a 5G NR staly dominantními, mnoho starších systémů a služeb (např. v oblasti veřejné bezpečnosti, bankovnictví nebo vzdáleného monitorování) stále spoléhá na okruhově spínané UDI. Proto specifikace 3GPP udržují definice UDI pro kompatibilitu, vzájemné propojení a jako měřítko kvality v popisech služeb. Její vývoj odráží přechod od primární datové přenosové služby ke starší službě podporované prostřednictvím CS Fallback (CSFB) a nakonec v 5G potenciálně prostřednictvím integrace s IMS pro emulované okruhově spínané služby.

## Klíčové vlastnosti

- Transparentní 64 kbit/s neomezená digitální přenosová služba (bearer service)
- Založena na technologii ISDN B-kanálu pro schopnost čistého kanálu (clear channel capability)
- Okruhově spínaný provoz s garantovanou šířkou pásma a nízkou latencí
- Podporuje aplikace v reálném čase, jako je videokonferencing (H.320) a fax G4
- End-to-end digitální konektivita s propojením mobilní sítě a ISDN
- Definována v mnoha specifikacích 3GPP (21.905, 23.910, 27.007 atd.) pro popis a správu služby

## Související pojmy

- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 41.033** (Rel-14) — GSM Lawful Interception Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [UDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/udi/)
