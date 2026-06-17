---
slug: "mo"
url: "/mobilnisite/slovnik/mo/"
type: "slovnik"
title: "MO – Mobile Originated Short Message Service"
date: 2026-01-01
abbr: "MO"
fullName: "Mobile Originated Short Message Service"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mo/"
summary: "MO (Mobile Originated, odeslané z mobilního zařízení) označuje odeslání služby krátkých textových zpráv (SMS) z mobilního zařízení. Jedná se o základní proces, kdy uživatel pošle textovou zprávu za úč"
---

MO je odeslání služby krátkých textových zpráv (SMS) z mobilního zařízení, které zahrnuje uživatelské zařízení (UE), obsluhující síť a centrum služby krátkých zpráv (SMSC) a umožňuje zasílání zpráv mezi osobami.

## Popis

Služba krátkých textových zpráv odeslaných z mobilního zařízení ([MO-SMS](/mobilnisite/slovnik/mo-sms/)) je standardizovaný mechanismus, který umožňuje uživatelskému zařízení (UE) iniciovat a odeslat krátkou textovou zprávu příjemci prostřednictvím mobilní sítě. Proces začíná, když uživatel na zařízení složí a odešle SMS. UE zabalí zprávu, včetně cílové adresy (obvykle [MSISDN](/mobilnisite/slovnik/msisdn/)) a textového obsahu, do zprávy CP-DATA podle protokolu definovaného v 3GPP TS 24.011. Tato zpráva je odeslána přes signalizační kanály (např. pomocí podsložky správy spojení - [CM](/mobilnisite/slovnik/cm/)) do ústředny pro mobilní spojení ([MSC](/mobilnisite/slovnik/msc/)) v sítích s přepojováním okruhů nebo do Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))/Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v sítích s přepojováním paketů pro SMS přes IP.

MSC nebo MME/AMF po přijetí MO-SMS ji přepošle do mezisíťové MSC ([IWMSC](/mobilnisite/slovnik/iwmsc/)) nebo do [IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/), které fungují jako brána k centru služby krátkých zpráv (SMSC). SMSC je centrální uzel zodpovědný za funkci uložení a přeposlání. Přijme MO zprávu, uloží ji a poté zahájí proces doručení zprávy do mobilního zařízení (MT) pro její doručení zamýšlenému příjemci. Doručení zahrnuje dotaz na Home Location Register (HLR) nebo Home Subscriber Server (HSS) za účelem zjištění aktuálního obsluhujícího síťového uzlu příjemce.

Mezi klíčové architektonické komponenty zapojené do MO-SMS patří UE (s jeho SMS aplikací a protokolovým zásobníkem), rádiová přístupová síť (RAN) pro přenos, uzly řídicí roviny jádra sítě (MSC, MME, AMF, SMSC) a potřebná rozhraní (např. rádiové rozhraní, rozhraní k SMSC). Služba funguje na řídicí rovině, což zajišťuje doručení i když není navázáno přenosové spojení na uživatelské rovině, což je klíčové pro spolehlivost. MO-SMS podporuje jak domény s přepojováním okruhů (CS), tak s přepojováním paketů (PS), s vývojem směrem k SMS přes IP (IMS) podle definic v pozdějších vydáních.

Úloha MO-SMS v síti je základní pro textovou komunikaci. Využívá stávající signalizační infrastrukturu, což z ní činí službu s nízkou šířkou pásma a vysokou spolehlivostí. Její integrace do jádra sítě zajišťuje širokou interoperabilitu a tvoří základ pro nadstandardní služby, jako je ověřování pomocí SMS, oznámení a komunikace mezi stroji (M2M). Protokoly zajišťují zpracování chyb, hlášení o doručení a spojování delších zpráv.

## K čemu slouží

MO-SMS bylo vytvořeno za účelem poskytnutí jednoduché, efektivní a všudypřítomné služby textového zasílání zpráv pro mobilní účastníky. Před SMS byla mobilní komunikace primárně zaměřena na hlas. Vývoj SMS, včetně schopnosti MO, využil nevyužitou kapacitu ve signalizačních kanálech sítí GSM (konkrétně Stand-alone Dedicated Control Channel - SDCCH), což umožnilo odesílání textových zpráv bez nutnosti vyhrazeného hlasového kanálu. Šlo o revoluční, nákladově efektivní způsob umožnění asynchronní komunikace.

Technologie řešila problém umožnění krátké, nehlasové komunikace mezi uživateli a mezi sítěmi a zařízeními. Řešila potřebu spolehlivého systému zasílání zpráv typu uložení a přeposlání, který by mohl fungovat napříč různými síťovými operátory a regiony. Její vytvoření bylo motivováno snahou efektivněji využívat síťové zdroje a otevřít nový zdroj příjmů a služeb pro operátory.

V průběhu času se MO-SMS stalo páteří pro četné aplikace přesahující zasílání zpráv mezi osobami, včetně aktivace služeb, bankovních upozornění a dvoufázového ověřování, díky své vysoké spolehlivosti a téměř univerzálnímu dosahu. Stanovilo základní architekturu a protokoly pro datové služby odeslané z mobilního zařízení, které se později vyvinuly pro podporu složitějších scénářů zasílání zpráv a IoT.

## Klíčové vlastnosti

- Přenos na řídicí rovině: Pro přenos zpráv využívá signalizační kanály (např. SDCCH v GSM, NAS signalizaci v LTE/NR) a nevyžaduje vyhrazený přenosový kanál.
- Uložení a přeposlání přes SMSC: Zprávy jsou spolehlivě uloženy v centru služby krátkých zpráv (SMSC) před pokusy o jejich doručení příjemci.
- Podpora hlášení o doručení: Může poskytnout odesílateli potvrzení o úspěšném nebo neúspěšném doručení zprávy do sítě.
- Spojené SMS: Umožňuje rozdělení a opětovné složení zpráv delších než limit 160 znaků do více segmentů.
- Propojení mezi doménami: Podporuje odeslání jak z domén jádra sítě s přepojováním okruhů (CS), tak s přepojováním paketů (PS/IMS).
- Mezinárodní roaming: Umožňuje odeslání zprávy, když se UE nachází v roamingu v navštívených sítích, prostřednictvím standardizovaných mezilehlých rozhraní.

## Související pojmy

- [MT-SMS – Mobile Terminated Short Message Service](/mobilnisite/slovnik/mt-sms/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.031** (Rel-19) — Fraud Information Gathering System (FIGS) Stage 1
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- … a dalších 125 specifikací

---

📖 **Anglický originál a plná specifikace:** [MO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mo/)
