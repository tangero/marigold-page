---
slug: "mrf"
url: "/mobilnisite/slovnik/mrf/"
type: "slovnik"
title: "MRF – Multimedia Resource Function"
date: 2025-01-01
abbr: "MRF"
fullName: "Multimedia Resource Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mrf/"
summary: "Základní prvek sítě v IP Multimedia Subsystem (IMS), který poskytuje služby související s médii, jako je mixování audio/videa, transkódování, generování tónů a přehrávání pro multimediální relace. Je"
---

MRF je základní prvek sítě IMS, který poskytuje mediální služby, jako je mixování, transkódování a generování tónů, a je rozdělen na řídicí MRFC a zpracovatelský MRFP.

## Popis

Multimedia Resource Function (MRF) je klíčová komponenta v architektuře 3GPP IP Multimedia Subsystem (IMS), zodpovědná za veškeré zpracování a manipulaci médií nad rámec prostého přeposílání paketů. Je logicky rozdělena na dvě odlišné funkční entity: Multimedia Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)) a Multimedia Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)). Toto rozdělení odpovídá standardnímu oddělení řídicí a uživatelské roviny v IMS. MRFC je entita řídicí roviny, která interpretuje signalizaci z Application Server ([AS](/mobilnisite/slovnik/as/)) nebo S-CSCF přes rozhraní Mr (pomocí SIP) a řídí akce MRFP pro zpracování médií. MRFP je entita uživatelské roviny, která fyzicky zpracovává mediální toky a provádí funkce jako mixování, transkódování a přehrávání, a to pod příkazem MRFC přes rozhraní Mp (pomocí H.248/Megaco).

Při provozu, když služba IMS, jako je konferenční hovor více účastníků, vyžaduje mixování médií, AS instruuje S-CSCF, aby směroval relaci k MRF. MRFC přijímá SIP signalizaci, interpretuje servisní logiku (např. 'vytvořit třícestný audio mix') a použije protokol H.248 ke konfiguraci MRFP konkrétními příkazy. MRFP následně alokuje potřebné procesní zdroje. Pro konferenci přijímá RTP mediální toky od všech účastníků, mixuje audio (nebo video) podle daných pravidel a odesílá každému účastníkovi zpět jeden složený tok. Mezi další klíčové funkce patří mediální transkódování (převod mezi různými kodeky, jako je [AMR](/mobilnisite/slovnik/amr/) a G.711), přehrávání audio/video oznámení, generování a detekce [DTMF](/mobilnisite/slovnik/dtmf/) tónů a duplikace médií pro zákonné odposlechy.

Architektura MRF je navržena pro škálovatelnost a flexibilitu. Více MRFP může být řízeno jedním nebo více MRFC, což umožňuje operátorům sítí škálovat kapacitu pro zpracování médií nezávisle na signalizačním řízení. MRF komunikuje s dalšími uzly IMS: přijímá řízení od AS nebo S-CSCF a MRFP se připojuje k mediální rovině IMS, typicky rozhraním s Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a IP sítěmi pro přenos médií. Její role je nezbytná pro umožnění služeb Rich Communication Services (RCS), hlasových/video konferencí, systémů interaktivní hlasové odezvy ([IVR](/mobilnisite/slovnik/ivr/)) a multimediálních oznámení, čímž tvoří motor mediálních služeb ekosystému IMS.

## K čemu slouží

MRF byla vytvořena za účelem centralizace a standardizace složitých schopností zpracování médií v rámci paketově orientované architektury IMS. Před IMS a MRF byly pokročilé telefonní funkce, jako jsou konference nebo oznámení, typicky řešeny monolitickými přepínači nebo proprietárními servery v sítích s přepojováním okruhů. Jak se sítě vyvíjely směrem k all-IP, vznikla potřeba standardizovaného, otevřeného a škálovatelného způsobu poskytování těchto mediálních služeb, které by mohly být dynamicky vyvolány jakoukoli aplikací IMS. MRF řeší problém oddělení servisní logiky (umístěné v [AS](/mobilnisite/slovnik/as/)) od náročného zpracování médií.

Její zavedení spolu s IMS ve 3GPP Release 5 bylo motivováno vizí konvergovaných multimediálních služeb přes IP. Řeší omezení zpracování na koncovém bodě (např. v mobilních zařízeních), které je limitováno schopnostmi zařízení a baterií, a konferencí typu mesh (kde každý účastník posílá toky všem ostatním), která spotřebovává nadměrnou šířku pásma pro uplink. MRF poskytuje síťový bod pro mixování, který je efektivní a zajišťuje konzistentní uživatelský zážitek ze služby. Dále, standardizací rozhraní Mr (SIP) a Mp (H.248) umožňuje interoperabilitu mezi více dodavateli pro aplikační servery, řadiče a mediální procesory, což podporuje inovace a konkurenci v servisní vrstvě. MRF je tedy klíčovým prvkem pro přeměnu IMS ze základní SIP proxy infrastruktury na plnohodnotnou platformu telekomunikačních služeb.

## Klíčové vlastnosti

- Rozdělená architektura oddělující funkce řídicí (MRFC) a uživatelské roviny (MRFP)
- Poskytuje konferenční spojení více účastníků s možnostmi mixování audio/videa
- Provádí mediální transkódování mezi různými hlasovými a video kodeky
- Podporuje přehrávání předem nahraných audio a video oznámení
- Umožňuje sběr a generování DTMF tónů pro interaktivní služby
- Rozhraní využívající standardní protokoly: SIP (Mr) pro řízení a H.248/Megaco (Mp) pro správu mediálních zdrojů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.182** (Rel-19) — Customized Alerting Tones (CAT) Protocol
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- **TR 26.982** (Rel-19) — Multiparty Real-Time Text Protocol Details
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions

---

📖 **Anglický originál a plná specifikace:** [MRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrf/)
