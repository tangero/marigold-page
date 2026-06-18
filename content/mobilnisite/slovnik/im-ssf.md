---
slug: "im-ssf"
url: "/mobilnisite/slovnik/im-ssf/"
type: "slovnik"
title: "IM-SSF – IP Multimedia Service Switching Function"
date: 2025-01-01
abbr: "IM-SSF"
fullName: "IP Multimedia Service Switching Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/im-ssf/"
summary: "IM-SSF je funkce jádrové sítě, která umožňuje provádění dědičných služeb CAMEL (Customized Applications for Mobile network Enhanced Logic) pro účastníky využívající IP Multimedia Subsystem (IMS). Fung"
---

IM-SSF (IP Multimedia Service Switching Function) je brána jádrové sítě, která zajišťuje překlad mezi signalizací SIP v IMS a protokoly CAMEL, aby bylo možno poskytovat dědičné služby inteligentní sítě (Intelligent Network) účastníkům využívajícím IP Multimedia Subsystem (IMS).

## Popis

IP Multimedia Service Switching Function (IM-SSF) je kritický uzel pro interoperabilitu definovaný v rámci 3GPP architektury IMS. Jeho primární role spočívá v propojení řídicího paradigmatu služeb IMS založeného na [SIP](/mobilnisite/slovnik/sip/) a řízení služeb založeného na [IN](/mobilnisite/slovnik/in/)/[CAMEL](/mobilnisite/slovnik/camel/) používaném v tradičních sítích GSM, UMTS a [GPRS](/mobilnisite/slovnik/gprs/). V jádru IMS se IM-SSF jeví jako aplikační server (Application Server, [AS](/mobilnisite/slovnik/as/)), který přijímá zprávy SIP prostřednictvím rozhraní IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)) od Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)).

Interně IM-SSF obsahuje CAMEL Service Switching Function ([SSF](/mobilnisite/slovnik/ssf/)) a model stavu hovoru. Při aktivaci pro relaci mapuje stav dialogu SIP (např. INVITE, 200 OK, BYE) na ekvivalentní model stavu hovoru CAMEL. Poté formuluje a odesílá odpovídající operace CAMEL Application Part (CAP) (např. InitialDP, ApplyCharging, RequestReportBCSMEvent) externí CAMEL Service Control Function (gsmSCF nebo SCP). gsmSCF, která hostuje servisní logiku, vrací instrukce CAP (např. Continue, Connect, ApplyChargingReport), které IM-SSF zpětně přeloží na odpovídající manipulace se zprávami SIP nebo na akce vynucení politik v rámci IMS relace.

Z architektonického hlediska je IM-SSF propojena se S-CSCF přes ISC (pomocí SIP), s gsmSCF přes rozhraní CAP a s Home Subscriber Server (HSS) přes rozhraní Sh za účelem získání CAMEL předplatitelských informací. Může také komunikovat s Media Resource Function Controller (MRFC) pro hlasové informace. Provedením tohoto překladu protokolů a mapování stavů umožňuje IM-SSF gsmSCF řídit IMS relace, jako by šlo o tradiční okruhově přepínané hovory, což zajišťuje kontinuitu služeb a ochranu investic pro operátory migrující na IMS.

## K čemu slouží

IM-SSF byla vytvořena k vyřešení klíčové obchodní a technické výzvy během přechodu od okruhově přepínané telefonie k plně IP sítím IMS. Operátoři vložili obrovské investice do platformy Intelligent Network (IN) a služeb založených na CAMEL (předplacené hovory, virtuální privátní sítě, překlad čísel, bezplatná čísla). Tyto služby představovaly významné zdroje příjmů a zákaznické funkce. Zavedení IMS s jeho nativní servisní vrstvou SIP hrozilo, že tyto dědičné služby zastarají a bude nutná nákladná a riziková rekonstrukce.

IM-SSF poskytuje strategickou migrační cestu. Její vznik motivovala potřeba kontinuity služeb, která umožňuje účastníkům používat stejné známé služby (jako je účtování předplacených hovorů) bez ohledu na to, zda se jedná o dědičný okruhově přepínaný hovor nebo hovor založený na IMS (VoLTE/VoWiFi). Řeší zásadní nekompatibilitu mezi událostmi řízeným, dialogově orientovaným protokolem SIP a stavově orientovaným, transakčně zaměřeným protokolem CAMEL.

Standardizací IM-SSF umožnilo 3GPP operátorům nasadit IMS a postupně zavádět nové služby založené na SIP, a zároveň chránit jejich stávající infrastrukturu služeb CAMEL. Tím se zkrátila doba uvedení IMS nasazení na trh a snížilo se finanční a provozní riziko spojené s úplnou a současnou výměnou jak jádra sítě, tak servisní vrstvy.

## Klíčové vlastnosti

- Protokolová interoperabilita mezi SIP (IMS) a CAMEL Application Part (CAP)
- Mapuje stavy IMS relací (SIP dialogy) na modely stavu hovoru CAMEL
- Vůči S-CSCF se jeví jako aplikační server (Application Server, AS) IMS
- Získává CAMEL předplatitelská data z HSS přes rozhraní Sh
- Umožňuje gsmSCF řídit účtování, směrování a interakci s uživatelem pro IMS relace
- Podporuje dědičné fáze CAMEL (např. CAMEL Phase 2, 3, 4) pro řízení služeb IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [SCSCF – Serving Call Session Control Function](/mobilnisite/slovnik/scscf/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [IM-SSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/im-ssf/)
