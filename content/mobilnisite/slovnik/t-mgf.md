---
slug: "t-mgf"
url: "/mobilnisite/slovnik/t-mgf/"
type: "slovnik"
title: "T-MGF – Trunking Media Gateway Function"
date: 2025-01-01
abbr: "T-MGF"
fullName: "Trunking Media Gateway Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-mgf/"
summary: "Media Gateway Function (MGF) specializovaná pro obsluhu vysokokapacitních trunkovacích rozhraní, typicky mezi sítěmi s přepojováním okruhů (jako PSTN) a sítěmi s přepojováním paketů (jako IMS). Provád"
---

T-MGF (Trunking Media Gateway Function) je funkce trunkovacího mediálního bránového uzlu, specializovaná MGF, která obsluhuje vysokokapacitní trunkovací rozhraní mezi sítěmi s přepojováním okruhů a sítěmi s přepojováním paketů za účelem provádění konverze a zpracování médií pro hromadný provoz.

## Popis

Trunking Media Gateway Function (T-MGF) je síťový prvek v architektuře 3GPP, který funguje jako specializovaná mediální brána. Je navržena pro správu a zpracování mediálních toků na vysokokapacitních trunkovacích rozhraních, která se používají pro propojení různých síťových domén nebo operátorů. Fyzicky i logicky se nachází na hranici mezi legacy sítěmi s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), jako je veřejná telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) nebo legacy mobilní jádro, a moderními sítěmi s přepojováním paketů, jako je IP Multimedia Subsystem (IMS) nebo paketové jádro. Jejím hlavním úkolem je konverze mediálních formátů a transportních protokolů. Například transformuje hlasové kanály s časovým multiplexem ([TDM](/mobilnisite/slovnik/tdm/)) z trunků E1/T1 na pakety Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) přes IP a naopak.

Provozně je T-MGF řízena řadičem mediálních bran ([MGC](/mobilnisite/slovnik/mgc/)), jako je Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)), za použití řídicích protokolů jako H.248 (Megaco) nebo [SIP](/mobilnisite/slovnik/sip/). Řídicí rovina T-MGF nařizuje navazování, modifikaci a uvolňování mediálních spojení (kontextů a terminací) přes její trunkové linky. Na uživatelské rovině zajišťuje vlastní zpracování médií. To zahrnuje nejen překódování kodeků (např. z G.711 A-law/μ-law na AMR-NB), ale také pokročilejší funkce, jako je potlačení ozvěn, detekce hlasové aktivity, generování komfortního šumu a maskování ztrát paketů pro udržení kvality hovoru. Pro trunkové scénáře často podporuje rozsáhlou signalizační interoperabilitu, například převod signalizace ISDN User Part (ISUP) z trunků SS7 na SIP zprávy pro síť IMS.

Architektonicky je T-MGF klíčovou součástí mediální roviny IMS, často spojovanou s funkcí Interconnection Border Control Function (IBCF) a MGCF v architektuře IMS pro propojení se sítěmi CS. Je konstruována pro provozní spolehlivost na úrovni operátora a konfigurace s vysokou hustotou portů, aby zvládla tisíce simultánních hovorů. Její návrh se zaměřuje na škálovatelnost, nízkou latenci a efektivní využití zdrojů pro správu agregovaného provozu celých skupin trunků, což ji zásadně odlišuje od přístupových mediálních bran obsluhujících jednotlivé účastnické linky.

## K čemu slouží

T-MGF byla vyvinuta pro řešení kritické potřeby interoperability a migrace během přechodu od tradiční telefonie s přepojováním okruhů k plně IP síťovým architekturám, jako je IMS. Když operátoři začali nasazovat IMS pro základní služby, stále potřebovali zachovat konektivitu s rozsáhlou instalovanou základnou sítí PSTN a legacy mobilních sítí, které převážně využívají TDM trunkové linky a signalizaci SS7. Standardní mediální brána byla pro rozsah a specifické požadavky těchto mezispolečenských spojovacích bodů nedostatečná.

Trunková rozhraní vyžadují mnohem vyšší kapacitu, odlišné signalizační profily (např. ISUP) a robustní záruky výkonu ve srovnání s přístupovými rozhraní pro účastníky. T-MGF byla vytvořena jako specializovaná varianta MGF, aby tyto požadavky splnila. Řeší problém efektivní konverze a zpracování médií ve velkém měřítku na síťových hranicích, což umožňuje plynulé hlasové a videohovory mezi IP-based a legacy sítěmi. Její vznik byl motivován ekonomickou a praktickou nutností: umožnila operátorům využít jejich nové investice do IMS při současném ochránění stávajících investic do infrastruktury, čímž zajistila kontinuitu služeb během postupného, fázového vývoje sítě. Bez T-MGF by mezidoménová komunikace vyžadovala nákladná a komplexní bodová řešení, což by brzdilo přijetí IP-based základních sítí.

## Klíčové vlastnosti

- Podpora vysokohustotních rozhraní pro TDM trunkové linky E1/T1/J1 a IP porty
- Konverze médií mezi TDM časovými sloty a IP/RTP/UDP paketovými toky
- Překódování kodeků mezi legacy (G.711) a mobilními/IP (AMR, EVS) kodeky
- Řízení pomocí H.248 (Megaco) nebo SIP z řadiče mediálních bran (Media Gateway Controller)
- Pokročilé zpracování médií: potlačení ozvěn, detekce hlasové aktivity, maskování ztrát paketů
- Často integruje signalizační interoperabilitu pro převod SS7/ISUP na SIP na hranici uživatelské roviny

## Související pojmy

- [MGF – Media Gateway Function](/mobilnisite/slovnik/mgf/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IBCF – Interconnection Border Control Functions](/mobilnisite/slovnik/ibcf/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS

---

📖 **Anglický originál a plná specifikace:** [T-MGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-mgf/)
