---
slug: "mo-sms"
url: "/mobilnisite/slovnik/mo-sms/"
type: "slovnik"
title: "MO-SMS – Mobile Originated Short Message Service"
date: 2025-01-01
abbr: "MO-SMS"
fullName: "Mobile Originated Short Message Service"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mo-sms/"
summary: "MO-SMS je proces, při kterém mobilní zařízení zahájí a odešle krátkou textovou zprávu do sítě. Jedná se o základní službu mobilních sítí umožňující zasílání zpráv mezi osobami, se standardizovanými po"
---

MO-SMS je proces iniciovaný mobilním zařízením, při kterém zařízení zahájí a odešle krátkou textovou zprávu do sítě, což umožňuje základní zasílání zpráv mezi osobami napříč generacemi 3GPP.

## Popis

Mobile Originated Short Message Service (MO-SMS) označuje standardizovaný postup, při kterém uživatelské zařízení (UE) vytvoří a přenese krátkou zprávu ([SM](/mobilnisite/slovnik/sm/)) do centra služby krátkých zpráv (SM-SC) prostřednictvím mobilní sítě. Jedná se o základní službu v systémech 3GPP, definovanou v mnoha vydáních od dob GSM. Proces zahrnuje sestavení zprávy v UE a její odeslání přes síťovou infrastrukturu, která ji směruje k zamýšlenému příjemci prostřednictvím SM-SC. Architektura zahrnuje UE, rádiovou přístupovou síť (RAN), prvky jádra sítě (CN), jako je [MSC](/mobilnisite/slovnik/msc/) (v okruhově spínaných doménách) nebo [AMF](/mobilnisite/slovnik/amf/)/[MME](/mobilnisite/slovnik/mme/) (v paketově spínaných doménách), a SM-SC, které zprávy ukládá a přeposílá.

Jak to funguje: Když uživatel odešle [SMS](/mobilnisite/slovnik/sms/), UE zabalí text zprávy a cílovou adresu do datové jednotky protokolu SM. V tradičních okruhově spínaných sítích (2G/3G) UE naváže signalizační spojení a odešle MO-SMS přes MSC, které komunikuje se SM-SC pomocí protokolů [MAP](/mobilnisite/slovnik/map/). V paketově spínaných sítích (4G/5G) lze MO-SMS přenášet přes IP pomocí IP Short Message Gateway ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)) nebo prostřednictvím signalizace [NAS](/mobilnisite/slovnik/nas/) přes AMF v 5G. UE odešle SMS v transportní zprávě NAS do AMF, která ji přepošle do SM-SC přes SMSF (SMS Function) v 5G Core. Mezi klíčové komponenty patří SMS aplikace v UE, funkce směrování SMS v síti a SM-SC, které zajišťuje doručení.

Role MO-SMS se vyvinula ze základní textové služby na kritickou komponentu pro autentizaci, oznámení a komunikaci IoT. Zůstává nedílnou součástí navzdory vzestupu OTT messagingu díky své spolehlivosti, univerzálnosti a využití v backendových službách. Postupy zajišťují interoperabilitu napříč zařízeními a sítěmi, přičemž specifikace pokrývají kódování, signalizaci a zpracování chyb.

## K čemu slouží

MO-SMS byl vytvořen, aby poskytl standardizovanou a spolehlivou metodu pro odesílání krátkých textových zpráv z mobilních zařízení, a to počínaje GSM (2G) jako součást služby krátkých zpráv (SMS). Řešil problém umožnění jednoduché a efektivní komunikace mezi osobami bez nutnosti hovoru, přičemž využíval nevyužité signalizační kanály v mobilních sítích. Historicky, před SMS, byla mobilní komunikace omezena na hlas, a zavedení MO-SMS ve 3GPP Release 5 (ačkoli konceptuálně dříve v GSM) umožnilo asynchronní zasílání zpráv, které se stalo nesmírně populární.

Tato technologie řeší potřebu zasílání zpráv s nízkou šířkou pásma a funkcí store-and-forward, které funguje napříč různými sítěmi a zařízeními. Omezení předchozích přístupů zahrnovala proprietární systémy zasílání zpráv nebo nedostatek interoperability; MO-SMS tento proces standardizoval a zajistil tak globální kompatibilitu. Jeho vytvoření bylo motivováno rostoucí poptávkou po textových službách a od té doby se vyvinulo, aby podporovalo rozšířené funkce, jako jsou zřetězené zprávy, Unicode pro mezinárodní znaky a integraci s IP sítěmi v pozdějších vydáních. MO-SMS zůstává relevantní díky své robustnosti, širokému pokrytí a využití v kritických službách, jako je dvoufaktorová autentizace a výstrahy, a to i přes nástup datových messagingových aplikací.

## Klíčové vlastnosti

- Standardizovaný postup pro odesílání SMS z mobilních zařízení
- Podporuje textové zprávy o délce až 160 znaků (nebo více pomocí zřetězení)
- Funguje v okruhově i paketově spínaných síťových doménách
- Využívá signalizaci NAS v 4G/5G pro SMS přes IP
- Integruje se s SM-SC pro funkci store-and-forward (ulož a přepošli)
- Zajišťuje interoperabilitu prostřednictvím specifikací 3GPP napříč generacemi

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MT-SMS – Mobile Terminated Short Message Service](/mobilnisite/slovnik/mt-sms/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [MO-SMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mo-sms/)
