---
slug: "ns-sap"
url: "/mobilnisite/slovnik/ns-sap/"
type: "slovnik"
title: "NS-SAP – Network Service Service Access Point"
date: 2025-01-01
abbr: "NS-SAP"
fullName: "Network Service Service Access Point"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ns-sap/"
summary: "NS-SAP je služební přístupový bod (Service Access Point) definovaný ve specifikacích 3GPP pro rozhraní mezi řadičem základnových stanic (BSC) a jednotkou řízení paketů (PCU) v GSM/EDGE rádiové přístup"
---

NS-SAP je služební přístupový bod (Service Access Point) definovaný ve specifikacích 3GPP pro rozhraní mezi řadičem základnových stanic (Base Station Controller) a jednotkou řízení paketů (Packet Control Unit) v GERAN, který poskytuje logický bod pro služby paketově orientovaných dat.

## Popis

Služební přístupový bod síťové služby (Network Service Service Access Point, NS-SAP) je specifické rozhraní a logický bod definovaný v 3GPP TS 48.016. Nachází se v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)) a tvoří referenční bod mezi dvěma klíčovými síťovými prvky: řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a jednotkou řízení paketů ([PCU](/mobilnisite/slovnik/pcu/)). PCU je síťový prvek odpovědný za správu prostředků pro paketově orientovaná data, jako jsou ty používané pro datové služby [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. NS-SAP definuje, jak tyto dvě entity komunikují pro zpracování paketového datového provozu.

Z architektonického hlediska BSC zpracovává tradiční okruhově orientovaný hlas a signalizaci, zatímco PCU je vyhrazeno pro funkce řízení paketů. NS-SAP je demarkační bod, kde BSC předává paketová data z rádiového rozhraní do PCU pro další zpracování a směrování směrem k paketové části jádra sítě ([SGSN](/mobilnisite/slovnik/sgsn/)). Funguje pomocí definované sady primitiv a protokolů nad podkladovým fyzickým spojením (často linka T1/E1 nebo IP). Mezi klíčová primitiva patří požadavky a indikace přenosu dat, stejně jako řídicí zprávy pro správu kanálů paketových dat ([PDCH](/mobilnisite/slovnik/pdch/)). NS-SAP zajišťuje, že paketové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) pro uplink i downlink jsou správně přeposílány mezi vrstvou řízení rádiových zdrojů v BSC a vrstvou plánování paketů/řízení logického spoje v PCU.

Role NS-SAP v síti je klíčová pro oddělení funkcí okruhového a paketového přepojování v rámci GERAN. Umožňuje modernizovat tradiční GSM síť pro podporu paketových dat bez nutnosti kompletní výměny hardwaru BSC. Rozhraní standardizuje komunikaci mezi BSC a PCU nezávislou na dodavateli, což bylo zásadní pro interoperabilitu zařízení od různých výrobců během zavádění datových služeb 2.5G a 2.75G. Zpracovává multiplexování paketových dat více uživatelů na fyzické zdroje a spravuje související signalizaci pro přidělování a uvolňování paketových prostředků.

## K čemu slouží

NS-SAP byl vytvořen k řešení problému integrace schopností paketově orientovaných dat do stávající architektury okruhově orientované sítě GSM. Před GPRS byly GSM sítě navrženy výhradně pro hlas a SMS, což jsou okruhově orientované služby. Zavedení paketových dat vyžadovalo novou funkční entitu (PCU) a jasné, standardizované rozhraní pro její připojení k existující infrastruktuře BSC.

Historicky, bez standardizovaného rozhraní jako je NS-SAP, by každý dodavatel implementoval proprietární metodu pro komunikaci BSC-PCU, což by vedlo k fragmentaci a znemožnilo operátorům míchat zařízení od různých dodavatelů. To by vážně bránilo nákladově efektivnímu a rychlému nasazení GPRS/EDGE. Specifikace NS-SAP tento problém řešila definicí jednotného služebního přístupového bodu, který umožnil BSC a PCU – i od různých dodavatelů – bezproblémově spolupracovat. Motivovala k efektivnímu znovupoužití stávajícího hardwaru BSC při současném přidání nových funkcí pro paketová data, což byl klíčový ekonomický a technický faktor úspěchu mobilních dat v éře 2G.

## Klíčové vlastnosti

- Standardizované logické rozhraní mezi BSC a PCU v GERAN
- Definuje služební primitiva pro přenos a řízení paketových dat
- Umožňuje podporu paketově orientovaných služeb GPRS a EDGE přes GSM
- Usnadňuje interoperabilitu zařízení BSC a PCU od různých dodavatelů
- Spravuje předávání paketových datových jednotek (PDU) pro uplink a downlink
- Podporuje řídicí signalizaci pro přidělování a správu kanálů paketových dat (PDCH)

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [PCU – Packet Control Unit](/mobilnisite/slovnik/pcu/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [NS-SAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns-sap/)
