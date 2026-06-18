---
slug: "rs"
url: "/mobilnisite/slovnik/rs/"
type: "slovnik"
title: "RS – Remote Source"
date: 2025-01-01
abbr: "RS"
fullName: "Remote Source"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rs/"
summary: "Termín z konvence pojmenování protokolu H.248/Megaco používané v řízení mediálních bran (Media Gateway control) 3GPP. Odkazuje na logickou entitu, která představuje koncový bod příchozího mediálního t"
---

RS je logická entita představující koncový bod příchozího mediálního toku na mediální bráně (Media Gateway), například audio z okruhově přepínané části sítě nebo IP tok.

## Popis

V kontextu architektur 3GPP, zejména těch zahrnujících Mediální brány ([MGW](/mobilnisite/slovnik/mgw/)) a funkci řízení mediální brány ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo řadič prostředků médií ([MRFC](/mobilnisite/slovnik/mrfc/)), znamená "RS" Remote Source (vzdálený zdroj). Jedná se o termín na úrovni protokolu převzatý z protokolu H.248 (Megaco), což je standardní rozhraní pro řízení mediálních bran. V modelu H.248 je mediální brána abstrahována do řady ukončení (terminations) a kontextů (contexts). Ukončení jsou zdroje nebo příjemci mediálních toků a kontexty jsou asociace míchající nebo přepínající více ukončení. "Remote Source" je specifický typ deskriptoru nebo vlastnosti ukončení, který identifikuje vzdálený koncový bod, ze kterého mediální tok pochází.

Operačně, když řadič mediální brány ([MGC](/mobilnisite/slovnik/mgc/)), jako je MGCF, nastavuje hovor procházející mediální bránou – například převod mezi hlasem s časovým multiplexem ([TDM](/mobilnisite/slovnik/tdm/)) ze starší [PSTN](/mobilnisite/slovnik/pstn/) a pakety [RTP](/mobilnisite/slovnik/rtp/)/IP pro jádro IMS – používá k nastavení ukončení v MGW příkazy H.248. Pro ukončení, které bude přijímat příchozí mediální tok (např. RTP tok z IP strany nebo časový slot z TDM trunku), může řadič specifikovat vlastnosti, které zahrnují jeho identifikaci jako Remote Source. Tento deskriptor nese informace o mediálních parametrech vzdálené strany, jako je IP adresa, číslo portu, typ kodeku a charakteristiky paketizace. V podstatě říká mediální bráně: "očekávej příjem toku z tohoto vzdáleného zdroje s těmito vlastnostmi."

Deskriptor RS je klíčový pro správnou konfiguraci přijímací cesty v MGW. Umožňuje bráně otevřít správné porty, inicializovat příslušné jitter buffery a připravit potřebné transkódovací prostředky, pokud se přijímaný kodek liší od toho, který má být odeslán na druhém ukončení. Koncept je symetrický s "Remote Sink" (vzdálený příjemce), který popisuje cíl pro odchozí tok. Společně umožňují řadiči MGC plně popsat obousměrný mediální tok pomocí spojovacího modelu protokolu H.248. Ve specifikacích 3GPP, jako je TS 29.232 (rozhraní Mn), které profilují H.248 pro použití v 3GPP, se tyto termíny používají k definování přesných informací vyměňovaných mezi MGCF a MGW za účelem vytvoření mediálních přenosů pro služby, jako je kontinuita hlasového hovoru mezi doménami [CS](/mobilnisite/slovnik/cs/) a IMS.

## K čemu slouží

Účelem konceptu "Remote Source" (vzdálený zdroj) v rámci řídicí architektury 3GPP je poskytnout abstraktní, standardizovaný způsob, jak může řadič instruovat mediální bránu o charakteristikách příchozího mediálního toku. Tato abstrakce je základním kamenem dekomponované architektury řízení bran (Gateway Control architecture), která odděluje řízení hovoru a zpracování médií. Historicky byly v monolitických ústřednách řízení hovoru a přepojování médií těsně integrovány. Přechod k dekomponovaným architekturám se samostatnými MGCF (pro signalizaci) a MGW (pro média) vyžadoval robustní protokol – H.248 – aby mohl řadič ovládat mediální rovinu. Deskriptor RS je klíčovým prvkem tohoto protokolu a řeší problém, jak přesně popsat dynamický, vzdálený mediální koncový bod relativně "hloupé" mediální bráně.

Před těmito abstrakcemi byla konfigurace mediálních cest často nízkourovňová a specifická pro výrobce. Termín RS jako součást standardu H.248 vytváří společný jazyk. Umožňuje řadiči mediální brány od jednoho výrobce úspěšně nakonfigurovat mediální bránu od jiného výrobce tak, aby přijímala tok od koncového bodu třetí strany. Tato interoperabilita je klíčová pro vícevýrobcové sítě. Jeho vytvoření bylo motivováno potřebou flexibility a škálovatelnosti v sítích příští generace. MGCF zpracovávající složité směrování hovorů (např. pro hovor roamujícího účastníka) musí být schopno instruovat MGW, aby připojila tok z potenciálně neznámé vzdálené IP adresy (RS) k místnímu TDM okruhu. Deskriptor RS zapouzdřuje všechny potřebné informace o IP transportu a kódování médií strukturovaným způsobem.

Dále, ve vývoji 3GPP směrem k IMS a SRVCC (Single Radio Voice Call Continuity) je schopnost rychle přesměrovat mediální toky během předání hovoru zásadní. MGCF používá příkazy H.248 s deskriptory RS (a Remote Sink) k rychlé rekonfiguraci mediálních spojení v MGW při předání hovoru z LTE do sítí 2G/3G. Koncept RS tedy existuje proto, aby umožnil přesné, interoperabilní a dynamické řízení mediálních toků v dekomponované síťové architektuře, což je základním kamenem moderních telekomunikačních sítí podporujících jak starší, tak IP-based služby.

## Klíčové vlastnosti

- Deskriptor protokolu H.248/Megaco pro koncový bod příchozího mediálního toku
- Používán řadiči mediálních bran (MGCF/MRFC) ke konfiguraci Mediálních bran (Media Gateways)
- Zapouzdřuje detaily vzdáleného koncového bodu, jako je IP adresa, port a informace o kodeku
- Umožňuje dynamické nastavení a modifikaci mediálních cest v dekomponované architektuře
- Kritický pro interoperabilitu mezi řadiči a branami od různých výrobců
- Podporuje služby vyžadující mediální propojení (interworking), jako je kontinuita hovorů CS-IMS a SRVCC

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rs/)
