---
slug: "ranap"
url: "/mobilnisite/slovnik/ranap/"
type: "slovnik"
title: "RANAP – Radio Access Network Application Protocol"
date: 2025-01-01
abbr: "RANAP"
fullName: "Radio Access Network Application Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ranap/"
summary: "RANAP je signalizační protokol mezi jádrovou sítí (CN) a rádiovou přístupovou sítí UMTS (UTRAN). Spravuje rádiové přístupové kanály, funkce mobility a zabezpečení, což umožňuje jádrové síti řídit RAN"
---

RANAP je signalizační protokol mezi jádrovou sítí a rádiovou přístupovou sítí UMTS, který spravuje přenosové kanály, mobilitu a zabezpečení za účelem umožnění řízení ze strany jádrové sítě a doručování služeb.

## Popis

Radio Access Network Application Protocol (RANAP) je klíčový signalizační protokol definovaný v architektuře UMTS od 3GPP, který funguje přes rozhraní Iu. Toto rozhraní spojuje jádrovou síť (CN), konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro okruhově spínané služby a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) pro paketově spínané služby, s pozemní rádiovou přístupovou sítí UMTS ([UTRAN](/mobilnisite/slovnik/utran/)). RANAP je aplikační protokol, který pro přenos svých zpráv využívá transportní protokoly nižších vrstev, jako jsou [SCCP](/mobilnisite/slovnik/sccp/) a [MTP3-B](/mobilnisite/slovnik/mtp3-b/) přes [ATM](/mobilnisite/slovnik/atm/) nebo IP. Jeho hlavní funkcí je poskytovat standardizovaný, spolehlivý mechanismus, pomocí kterého může jádrová síť řídit a spravovat zdroje a operace UTRAN, a tím abstrahovat specifika rádiové vrstvy od entit jádrové sítě.

RANAP funguje prostřednictvím souboru elementárních procedur ([EP](/mobilnisite/slovnik/ep/)), které představují základní jednotky signalizační výměny. Tyto procedury se dělí do tří tříd: procedury třídy 1 vyžadují odpověď (úspěch nebo selhání), procedury třídy 2 nevyžadují odpověď a procedury třídy 3 zahrnují více požadavků/odpovědí. Mezi klíčové procedury patří správa rádiového přístupového kanálu (RAB) pro zřizování, modifikaci a uvolňování přenosových kanálů uživatelských dat; procedury přesunu pro předání kontroly nad uživatelem mezi radiovými síťovými řadiči (RNC) nebo mezi RNC a jádrovou sítí; a volání pro lokalizaci neaktivního uživatelského zařízení (UE). Protokol také zajišťuje transparentní přenos zpráv Non-Access Stratum (NAS), jako je signalizace správy mobility a řízení hovoru, mezi UE a jádrovou sítí.

Z architektonického hlediska jsou zprávy RANAP zpracovávány entitou protokolu RANAP uvnitř RNC a příslušného uzlu jádrové sítě (MSC nebo SGSN). Protokol podporuje jak spojovanou, tak nespojovanou signalizaci. Pro uživatelsky specifickou signalizaci související s aktivním UE je zřízeno vyhrazené signalizační spojení Iu. Pro společnou nebo vysílací signalizaci nevázanou na konkrétní UE se používá nespojovaný transport. Návrh RANAP zajišťuje, že jádrová síť může nařídit RAN provedení konkrétních úkolů – například zřízení rádiového kanálu s určitými parametry kvality služeb (QoS) – aniž by musela rozumět složitým detailům algoritmů správy rádiových zdrojů implementovaných v UTRAN. Toto jasné oddělení odpovědností je základním principem architektury UMTS.

## K čemu slouží

RANAP byl vytvořen, aby uspokojil potřebu robustního, standardizovaného signalizačního rozhraní mezi novou, složitější rádiovou přístupovou sítí UMTS a vyvíjející se jádrovou sítí. Před 3G používal GSM protokol Base Station System Application Part (BSSAP) mezi MSC a Base Station Controller (BSC). Zavedení UTRAN s novou architekturou obsahující Node B a RNC a podpora pokročilých služeb s různými požadavky na QoS si však vyžádaly výkonnější a flexibilnější protokol. RANAP byl navržen tak, aby tuto funkcionalitu poskytl, a umožnil tak jádrové síti efektivně řídit bohatší sadu schopností nabízenou UTRAN založeným na WCDMA.

Protokol řeší problém abstrakce specifik rádiové sítě od servisní logiky v jádru. Umožňuje MSC a SGSN spravovat mobilitu, relace a řízení přenosových kanálů pomocí služebně orientovaných primitiv, zatímco RNC zajišťuje rádiově závislé mapování těchto požadavků na fyzické rádiové zdroje. Toto oddělení umožňuje nezávislý vývoj rádiových a jádrových sítí. Dále RANAP podporuje klíčové funkce 3G, jako je měkký handover (kdy je UE připojeno k více Node B současně), což vyžaduje složitou koordinaci mezi RNC a jádrovou sítí při správě přenosových kanálů během událostí mobility.

Jeho vytvoření bylo motivováno přechodem od okruhově spínaných služeb 2G k hybridní síti 3G podporující vysokorychlostní paketová data. RANAP musel umět spravovat jak okruhově spínané hlasové kanály, tak paketově spínané datové kanály s dynamickou QoS. Poskytl potřebné procedury, aby jádrová síť mohla požadovat zřízení rádiového přístupového kanálu se specifickou třídou provozu, maximální přenosovou rychlostí a charakteristikami zpoždění, což byl významný pokrok oproti jednodušší správě přenosových kanálů v GSM.

## Klíčové vlastnosti

- Spravuje zřizování, modifikaci a uvolňování rádiových přístupových kanálů (RAB)
- Zajišťuje přesun SRNS pro přenos kontextu UE mezi RNC
- Transparentně přenáší zprávy Non-Access Stratum (NAS) mezi UE a jádrovou sítí
- Řídí celkovou konfiguraci systému rádiového rozhraní (RAB) a parametry QoS
- Iniciuje volání UE v určitých oblastech služeb
- Podporuje správu přetížení a chyb mezi jádrovou sítí a UTRAN

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [RANAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ranap/)
