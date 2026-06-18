---
slug: "srf"
url: "/mobilnisite/slovnik/srf/"
type: "slovnik"
title: "SRF – Specialised Resource Function"
date: 2025-01-01
abbr: "SRF"
fullName: "Specialised Resource Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/srf/"
summary: "Síťová funkce v rámci IP multimediálního subsystému (IMS), která poskytuje zdroje pro zpracování médií pro pokročilé telefonní služby. Zajišťuje úlohy jako konferenční hovor, překódování a hlášení, co"
---

SRF je funkce IP multimediálního subsystému (IMS), která poskytuje zdroje pro zpracování médií pro pokročilé služby, jako je konferenční hovor, překódování a hlášení.

## Popis

Specialised Resource Function (SRF) je logická entita v architektuře IMS, často implementovaná jako součást Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)). MRF je rozdělena na řídicí část ([MRFC](/mobilnisite/slovnik/mrfc/) – Media Resource Function Controller) a zpracovatelskou část ([MRFP](/mobilnisite/slovnik/mrfp/) – Media Resource Function Processor). SRF typicky odkazuje na schopnosti poskytované MRFP. Jejím hlavním úkolem je poskytovat služby související s médii na požádání od aplikačního serveru ([AS](/mobilnisite/slovnik/as/)) nebo Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) prostřednictvím MRFC. SRF obsahuje fyzické zdroje pro zpracování mediálních proudů. To zahrnuje hardware a software pro funkce jako mixování audia pro víceúčastnické konference, zpracování řečových a audio signálů (např. pro generování a detekci tónů), překódování médií mezi různými kodeky (např. G.711 na [AMR](/mobilnisite/slovnik/amr/)), přehrávání nahraných hlášení a sbírání číslic ([DTMF](/mobilnisite/slovnik/dtmf/)). Když služba vyžaduje takový zdroj, AS nebo S-CSCF odešle řídicí zprávu (pomocí protokolů jako [SIP](/mobilnisite/slovnik/sip/)) do MRFC. MRFC poté pomocí řídicího protokolu, jako je H.248 (Megaco), instruuje MRFP/SRF, aby alokoval potřebné zdroje a aplikoval specifické zpracování na určené mediální proudy. Samotné mediální proudy jsou směrovány do SRF pomocí mediální roviny IMS, typicky přes IP síť. SRF tyto proudy zpracuje podle pokynů a poté je přepošle na příslušný cíl(e). Toto oddělení řízení (MRFC) a médií (SRF/MRFP) umožňuje škálovatelné a flexibilní nasazení služeb. SRF je klíčovým prvkem pro přidané hodnotové služby (VAS), který umožňuje síťovým operátorům a poskytovatelům třetích stran vytvářet funkce vyžadující manipulaci s obsahem médií samotných, nikoli pouze se signalizací.

## K čemu slouží

SRF byla vytvořena za účelem centralizace a správy složitých zdrojů pro zpracování médií v paketově přepínané, IP-based multimediální síti (IMS). Před IMS často pokročilé telefonní služby, jako je konferenční hovor nebo interaktivní hlasová odezva (IVR), vyžadovaly proprietární, izolované zařízení připojené k okruhově přepínanému jádru. To bylo neefektivní, obtížně škálovatelné a těžko integrovatelné s novými IP službami. Koncept SRF to řeší tím, že poskytuje standardizovanou, síťově centrickou zásobu mediálních zdrojů, kterou může dynamicky alokovat a ovládat jakákoli autorizovaná servisní logika uvnitř IMS. Řeší problém fragmentace služeb a umožňuje vytváření kombinovaných multimediálních služeb (hlas, video, text), které mohou tyto zdroje plynule využívat. Motivací bylo odstranit těsné propojení mezi servisní inteligencí a hardwarem pro zpracování médií, v souladu s obecným principem IMS oddělovat řídicí rovinu a uživatelskou rovinu. To umožňuje operátorům nasazovat a škálovat mediální zdroje nezávisle na aplikacích, které je využívají, což snižuje náklady a zvyšuje agilitu služeb. Usnadňuje nabízení konzistentních pokročilých služeb (jako je audio konference, nahrávání pro legální odposlech nebo personalizovaná hlášení) napříč staršími i novějšími přístupovými sítěmi.

## Klíčové vlastnosti

- Poskytuje centralizované zdroje pro zpracování médií pro síť IMS.
- Provádí funkce jako mixování audia, překódování, přehrávání/sbírání tónů a přehrávání hlášení.
- Funguje pod řízením MRFC s využitím protokolu H.248/Megaco.
- Propojuje se s mediální rovinou IMS pro příjem, zpracování a přeposílání RTP/RTCP proudů.
- Umožňuje pokročilé telefonní služby, jako je konferenční hovor, IVR a zpracování videa.
- Navrženo pro škálovatelnost a sdílené využití napříč více službami a aplikacemi.

## Související pojmy

- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 22.823** (Rel-16) — IMS enhancements for new real-time communication services
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [SRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/srf/)
