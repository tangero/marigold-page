---
slug: "grr"
url: "/mobilnisite/slovnik/grr/"
type: "slovnik"
title: "GRR – GPRS Radio Resources service access point"
date: 2025-01-01
abbr: "GRR"
fullName: "GPRS Radio Resources service access point"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/grr/"
summary: "GRR je servisní přístupový bod (SAP) v rámci protokolového zásobníku GPRS, konkrétně mezi vrstvami LLC a RLC/MAC. Definuje primitiva pro správu rádiových prostředků, což umožňuje přenos dat a signaliz"
---

GRR je servisní přístupový bod mezi vrstvami LLC a RLC/MAC v zásobníku GPRS, který definuje primitiva pro správu rádiových prostředků pro přenos dat a signalizaci.

## Popis

Servisní přístupový bod [GPRS](/mobilnisite/slovnik/gprs/) Radio Resources (GRR) je klíčové logické rozhraní v architektuře protokolu GPRS, jak je standardizováno ve specifikacích 3GPP. Nachází se mezi vrstvou Logical Link Control ([LLC](/mobilnisite/slovnik/llc/)) a vrstvou Radio Link Control/Medium Access Control (RLC/[MAC](/mobilnisite/slovnik/mac/)) jak na straně mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), tak na straně sítě (SGSN a [BSS](/mobilnisite/slovnik/bss/)). GRR-SAP není fyzické spojení, ale konceptuální bod, kde se vyměňují servisní primitiva. Tato primitiva jsou formátované zprávy nebo příkazy, které umožňují vrstvě LLC žádat o rádiové prostředky od vrstvy RLC/MAC pro vysílání a příjem dat.

Operačně GRR-SAP usnadňuje správu dočasných blokových toků (TBF), což jsou logická spojení zřizovaná pro přenos datových paketů přes rádiové rozhraní. Když má vrstva LLC data k odeslání, použije primitiva GRR k vyžádání zřízení TBF pro uplink. Vrstva RLC/MAC pak prostřednictvím podkladové fyzické vrstvy řeší kolize, alokaci prostředků a vlastní přenos rádiových bloků. Podobně pro downlink data používá síť indikace GRR k upozornění vrstvy LLC na příchozí datové bloky. Primitiva pokrývají funkce jako žádost o data, indikace dat, žádost o unitdata a indikace unitdata, čímž efektivně oddělují správu logického spoje od postupů specifických pro rádiový přenos.

Klíčovými součástmi interakce GRR jsou samotná servisní primitiva, která nesou parametry jako LLC Protocol Data Unit (PDU), identifikátor TBF a atributy kvality služby. GRR-SAP zajišťuje standardizovanou metodu, pomocí které vyšší vrstvy využívají sdílené, paketově orientované rádiové prostředky, aniž by musely rozumět složitým mechanismům časování a plánování na bázi TDMA v rozhraní vzduchu. Jeho role je zásadní pro umožnění efektivních, multiplexovaných paketových datových služeb přes sítě GSM a tvoří páteř základní datové služby GPRS před evolucí k 3G UMTS a dále.

## K čemu slouží

GRR byl vytvořen, aby poskytl standardizované, abstrahované rozhraní pro paketové datové služby přes stávající rádiovou infrastrukturu GSM s přepojováním okruhů. Před [GPRS](/mobilnisite/slovnik/gprs/) bylo GSM primárně navrženo pro hlasové hovory, které používají vyhrazená, nepřetržitá spojení s přepojováním okruhů. Tento model je neefektivní pro přerušovaný, nárazový datový provoz typický pro rané internetové aplikace. GRR-SAP jako součást architektury GPRS to vyřešil zavedením paradigmatu přepojování paketů přes rádiové rozhraní.

Konkrétní problém, který GRR řeší, je potřeba čistého oddělení odpovědností mezi vrstvou datového spoje ([LLC](/mobilnisite/slovnik/llc/)) a vrstvou správy rádiových prostředků (RLC/[MAC](/mobilnisite/slovnik/mac/)). Bez takto definovaného servisního přístupového bodu by správa dynamické alokace a uvolňování rádiových prostředků pro pakety byla ad-hoc a neinteroperabilní. GRR poskytuje dobře definovanou sadu primitiv, která umožňuje vrstvě LLC žádat o služby přenosu dat, aniž by byla zatížena složitostmi alokace časových slotů TDMA, kanálového kódování a řízení výkonu. Tato abstrakce byla klíčová pro umožnění efektivního sdílení stejných fyzických rádiových kanálů více uživateli, což je základním požadavkem pro nákladově efektivní mobilní data.

Historicky byl vývoj GRR v Release 8 (ačkoliv vycházel z dřívější práce na GPRS) součástí širšího úsilí 3GPP o údržbu a specifikaci vyvinuté GSM/EDGE Radio Access Network (GERAN). Zajišťoval zpětnou kompatibilitu a kontinuální specifikaci systému paketových dat 2G souběžně s vývojem 3G UMTS a 4G LTE. Vyřešil omezení čistého přepojování okruhů definováním řídicí roviny pro zřizování paketových rádiových prostředků, což byl základní krok směrem k dnešním plně IP sítím.

## Klíčové vlastnosti

- Definuje servisní primitiva pro přenos dat mezi vrstvami LLC a RLC/MAC
- Spravuje zřizování a uvolňování dočasných blokových toků (TBF)
- Podporuje jak potvrzované, tak nepotvrzované režimy přenosu dat
- Přenáší parametry kvality služby (QoS) pro paketové datové toky
- Umožňuje efektivní multiplexování více uživatelů na sdílených rádiových kanálech
- Poskytuje signalizační rozhraní pro alokaci paketových prostředků pro uplink a downlink

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [GRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/grr/)
