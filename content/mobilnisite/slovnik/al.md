---
slug: "al"
url: "/mobilnisite/slovnik/al/"
type: "slovnik"
title: "AL – Application Layer"
date: 2025-01-01
abbr: "AL"
fullName: "Application Layer"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/al/"
summary: "AL označuje aplikační vrstvu (Application Layer) v architektuře služeb 3GPP, která hostí koncové uživatelské služby a aplikace. Jedná se o konceptuální vrstvu nad jádrem sítě, kde sídlí služby s přida"
---

AL je konceptuální aplikační vrstva v architektuře služeb 3GPP, kde sídlí koncové uživatelské služby, jako je multimediální streamování a IoT aplikace, a která interaguje s podkladovými přenosovými schopnostmi sítě.

## Popis

Aplikační vrstva (AL) v 3GPP je logický architektonický stupeň, který zahrnuje aplikace a schopnosti služeb využívané koncovými uživateli a podniky. Nachází se nad jádrem sítě a využívá funkce konektivity, správy relací a kvality služeb (QoS) poskytované nižšími vrstvami, jako je IP Multimedia Subsystem (IMS) nebo 5G Core Network. AL není jediná fyzická entita, ale soubor aplikačních serverů, servisních platforem a klientského softwaru, které implementují služby jako Voice over LTE (VoLTE), videohovory, rich communication services ([RCS](/mobilnisite/slovnik/rcs/)), multimedia broadcast/multicast services ([MBMS](/mobilnisite/slovnik/mbms/)) a různé IoT aplikace. Tyto aplikace používají standardizovaná aplikační programová rozhraní ([API](/mobilnisite/slovnik/api/)) a referenční body, jako jsou ty definované v 3GPP TS 23.247 pro zpřístupnění služeb, k interakci se síťovými funkcemi pro autentizaci, řízení politik a doručování médií.

Architektonicky AL rozhraní s funkcemi jádra sítě prostřednictvím dobře definovaných servisně orientovaných rozhraní (SBIs) v 5G nebo tradičních referenčních bodů v dřívějších vydáních. Například aplikační server v AL může komunikovat s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a žádat o specifickou QoS pro video stream nebo s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro autentizaci uživatele. Klíčové komponenty v AL zahrnují Application Function ([AF](/mobilnisite/slovnik/af/)), což je formální síťová funkce 3GPP, která ovlivňuje směrování provozu a rozhodování o politikách, a různé služební prostředky jako Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)). AL také zahrnuje aplikační logiku na straně klienta v uživatelském zařízení (UE), která implementuje protokoly jako Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) pro média nebo HTTP/2 pro webové služby.

Úlohou AL je poskytnout standardizované prostředí pro vývoj a nasazení služeb, což zajišťuje interoperabilitu mezi různými operátory a typy zařízení. Abstrahuje složitosti podkladových rádiových a jádrových sítí, což umožňuje vývojářům aplikací se soustředit na servisní logiku a spoléhat se na síťové schopnosti pro zabezpečení, mobilitu a správu relací. Ve specifikacích jako 3GPP TS 26.110 pro charakteristiky kodeků nebo TS 38.857 pro podporu aplikační vrstvy vehicle-to-everything (V2X) AL definuje protokoly, datové formáty a chování specifické pro služby, jako je adaptivní streamování videa pro video nebo kolektivní percepční zprávy pro autonomní řízení. Tato vrstva je klíčová pro umožnění pokročilých případů užití v 5G a dalších generacích, včetně rozšířené reality, průmyslové automatizace a aplikací využívajících síťové slicing, tím, že poskytuje rámec pro zpřístupnění služeb a integraci sítí.

## K čemu slouží

Aplikační vrstva existuje, aby oddělila inovace služeb od vývoje síťové infrastruktury, což umožňuje operátorům a vývojářům třetích stran vytvářet a nasazovat aplikace nezávisle na podkladové přenosové technologii. Před jejím formalizováním v 3GPP byly služby často těsně integrovány se specifickými síťovými implementacemi, což vedlo k závislosti na dodavateli, problémům s interoperabilitou a pomalému uvedení nových funkcí na trh. Definováním standardizované AL s jasnými rozhraními 3GPP umožňuje živou ekosystémovou platformu aplikací, které mohou konzistentně fungovat napříč různorodými sítěmi, od 4G LTE po 5G a budoucí systémy. Tento přístup řeší omezení monolitických síťových architektur, kde byla servisní logika zabudována do prvků jádra sítě, což činilo aktualizace těžkopádnými a bránilo škálovatelnosti.

Historicky koncept AL získal na významu se zavedením IMS v 3GPP Release 5, které poskytlo platformu pro doručování služeb pro multimediální aplikace. Byl však dále zdokonalován v pozdějších vydáních, aby podporoval širší škálu služeb, včetně těch pro IoT a V2X komunikaci. Motivací pro jeho kontinuální vývoj je potřeba podporovat vznikající případy užití, které vyžadují nízkou latenci, vysokou spolehlivost nebo masivní konektivitu, jako je tomu v 5G. Specifikací aplikačních protokolů a prostředků 3GPP zajišťuje, že tyto služby mohou efektivně využívat síťové schopnosti, jako je síťový slicing, edge computing a diferenciace QoS, a řeší tak problémy související s výkonem služeb, zabezpečením a správou v komplexních prostředích s více dodavateli.

## Klíčové vlastnosti

- Standardizované služební prostředky a API pro vývoj aplikací
- Integrace s funkcemi jádra sítě prostřednictvím definovaných referenčních bodů (např. AF interagující s PCF)
- Podpora multimediálních služeb prostřednictvím kodeků a streamovacích protokolů
- Umožňuje IoT a V2X aplikace se specifickými formáty zpráv a procedurami
- Usnadňuje zpřístupnění služeb pro vývojáře třetích stran prostřednictvím Network Exposure Function (NEF)
- Poskytuje rámec pro správu síťového slicingu a QoS s ohledem na aplikace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO

---

📖 **Anglický originál a plná specifikace:** [AL na 3GPP Explorer](https://3gpp-explorer.com/glossary/al/)
