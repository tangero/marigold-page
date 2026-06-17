---
slug: "imeisv"
url: "/mobilnisite/slovnik/imeisv/"
type: "slovnik"
title: "IMEISV – International Mobile station Equipment Identity and Software Version number"
date: 2025-01-01
abbr: "IMEISV"
fullName: "International Mobile station Equipment Identity and Software Version number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/imeisv/"
summary: "IMEISV je 16místný identifikátor kombinující jedinečné IMEI zařízení s dvoumístným číslem verze softwaru (SVN). Poskytuje přesnou identifikaci jak hardwarového modelu, tak konkrétní nainstalované soft"
---

IMEISV je 16místný identifikátor, který kombinuje jedinečné hardwarové IMEI mobilního zařízení s číslem verze softwaru (SVN) a umožňuje přesnou identifikaci jak modelu, tak konkrétní softwarové revize.

## Popis

International Mobile station Equipment Identity and Software Version number (IMEISV) je rozšířený identifikátor pro mobilní zařízení. Jedná se o 16místné číslo, které rozšiřuje standardní 15místné [IMEI](/mobilnisite/slovnik/imei/) o přidání dvoumístného čísla verze softwaru (SVN). Prvních 14 číslic tvoří přidělený typový kód (TAC, 8 číslic) a sériové číslo (SNR, 6 číslic), shodné s IMEI. 15. číslice je kontrolní číslice ([CD](/mobilnisite/slovnik/cd/)) vypočtená pomocí Luhnova algoritmu. Klíčovým doplněním je 16. číslice, SVN, která identifikuje verzi softwaru nebo firmwaru nahraného v zařízení. Tento identifikátor hlásí uživatelské zařízení (UE) síti a využívají jej různé síťové funkce.

V rámci síťové architektury je IMEISV zpracováván prvky jádra sítě a v některých případech i rádiové přístupové sítě (RAN). Podle specifikací jako 24.501 ([NAS](/mobilnisite/slovnik/nas/)) a 33.401 (bezpečnost) může UE poskytnout IMEISV během registrace nebo bezpečnostních procedur. Jádro sítě, například Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), může tyto informace předat registru identit zařízení ([EIR](/mobilnisite/slovnik/eir/)) nebo jiným správním systémům. EIR může spravovat politiky nejen na základě hardwarového TAC, ale také SVN, což umožňuje detailní kontrolu. Například síť může omezit přístup zařízením s neaktuálními, zranitelnými verzemi softwaru.

Komponenta SVN mění IMEI ze statického hardwarového identifikátoru na dynamický, který odráží aktuální softwarový stav zařízení. To je klíčové pro moderní správu zařízení. Operátoři a výrobci jej používají ke sledování plnění nasazení firmwaru, zajištění, že zařízení mají kritické bezpečnostní aktualizace před povolením přístupu k citlivým službám, a povolování nebo zakazování konkrétních funkcí na základě softwarových schopností. V RAN, jak je uvedeno ve specifikacích jako 36.413 a 38.423, může být IMEISV použit pro optimalizace správy rádiových prostředků přizpůsobené konkrétním kombinacím zařízení a softwaru. IMEISV poskytuje úplný obraz identity zařízení, zahrnující jeho výrobní původ, jedinečnou jednotku a provozní softwarovou vrstvu, což z něj činí mocný nástroj pro bezpečnost, provozování a optimalizaci sítě.

## K čemu slouží

IMEISV byl zaveden, aby odstranil omezení standardního [IMEI](/mobilnisite/slovnik/imei/), které identifikuje pouze hardware. Jak se mobilní zařízení stávala složitějšími s aktualizovatelným firmwarem a softwarem, potřebovali síťoví operátoři a výrobci způsob, jak identifikovat přesnou verzi softwaru běžícího na zařízení. To bylo hnací silou potřeby přesné vzdálené správy zařízení, zmírňování bezpečnostních zranitelností a zajištění kompatibility služeb.

Historicky, bez SVN, mohla síť znát pouze model zařízení (pomocí TAC), ale ne to, zda bylo aktualizováno záplatou, která opravila kritickou bezpečnostní chybu nebo povolila novou protokolovou funkci. Tato mezera ztěžovala vynucování bezpečnostních politik nebo zaručení kvality služby. IMEISV to řeší svázáním softwarového stavu s trvalou identitou zařízení. Umožňuje politiky, které například mohou zakázat přístup k síti zařízením se známými zranitelnými verzemi softwaru nebo je přesměrovat na servisní portál pro povinné aktualizace.

Jeho účel se rozšířil s nástupem aktualizací Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) a internetu věcí (IoT). Pro nasazení IoT s tisíci zařízeními je správa verzí firmwaru prvořadá. IMEISV poskytuje potřebný identifikátor pro automatizované správní systémy, aby inventarizovaly verze softwaru a cíleně distribuovaly aktualizace. V pozdějších vydáních, jako Rel-17 a Rel-18, je jeho role posílena v kontextu 5G bezpečnosti (33.501) a síťové automatizace, kde je porozumění softwarovým schopnostem zařízení nedílnou součástí dynamického vynucování politik a výběru síťových řezů.

## Klíčové vlastnosti

- 16místný identifikátor kombinující 14místné jádro IMEI s dvoumístným číslem verze softwaru (SVN)
- Jednoznačně identifikuje jak hardwarový model, tak konkrétní revizi firmwaru/softwaru
- Používá se pro detailní politiky registru identit zařízení (EIR) založené na verzi softwaru
- Umožňuje cílenou správu zařízení, aplikaci bezpečnostních záplat a povolování funkcí
- Hlášen zařízením UE během síťové registrace a bezpečnostních procedur
- Podporuje optimalizace správy rádiových prostředů pro specifické dvojice zařízení-software

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [IMEISV na 3GPP Explorer](https://3gpp-explorer.com/glossary/imeisv/)
