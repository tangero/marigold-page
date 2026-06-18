---
slug: "arpi"
url: "/mobilnisite/slovnik/arpi/"
type: "slovnik"
title: "ARPI – Additional RRM Policy Index"
date: 2025-01-01
abbr: "ARPI"
fullName: "Additional RRM Policy Index"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/arpi/"
summary: "ARPI je parametr používaný v sítích 5G a LTE k označení specifických politik správy rádiových prostředků (RRM) pro uživatelské zařízení (UE) nad rámec standardního zacházení s QoS. Umožňuje detailnějš"
---

ARPI je indexový parametr používaný v sítích 5G a LTE k označení specifických politik správy rádiových prostředků (RRM) pro uživatelské zařízení (UE), umožňující detailní řízení pro síťové slicing a diferencované služby.

## Popis

Additional [RRM](/mobilnisite/slovnik/rrm/) Policy Index (ARPI) je signalizační parametr definovaný ve specifikacích 3GPP, který poskytuje rádiové přístupové síti (RAN) doplňující informace o tom, jak uplatňovat politiky správy rádiových prostředků (RRM) pro konkrétní uživatelské zařízení (UE) nebo datový tok. Na rozdíl od standardních parametrů QoS, které definují základní požadavky služby, jako je latence a propustnost, ARPI přenáší dodatečné směrnice politik, které ovlivňují, jak by měl plánovač RAN a funkce řízení přístupu upřednostňovat a spravovat rádiové prostředky. Tento parametr je přenášen v [NGAP](/mobilnisite/slovnik/ngap/) ([NG](/mobilnisite/slovnik/ng/) Application Protocol) a XnAP (Xn Application Protocol) zprávách mezi síťovými uzly, což umožňuje konzistentní uplatňování politik napříč různými prvky RAN.

Z architektonického hlediska ARPI funguje v rámci signalizační struktury řídicí roviny mezi jádrem sítě (konkrétně funkcí správy přístupu a mobility – [AMF](/mobilnisite/slovnik/amf/)) a uzly RAN (gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v LTE). Při zakládání nebo modifikaci [PDU](/mobilnisite/slovnik/pdu/) relace nebo přenosového kanálu může AMF zahrnout hodnoty ARPI v příslušných NGAP zprávách odeslaných do RAN. Uzel RAN pak tyto hodnoty interpretuje podle své lokální konfigurace a uplatňuje odpovídající politiky RRM. Tyto politiky mohou ovlivnit různé aspekty správy rádiových prostředků včetně plánovacích algoritmů, prahů řízení přístupu, parametrů předávání spojení a konfigurace rádiových přenosových kanálů.

Klíčové komponenty zapojené do implementace ARPI zahrnují framework řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), který může generovat politiky související s ARPI, AMF, který tyto politiky předává do RAN, a uzly RAN, které politiky interpretují a uplatňují. Hodnota ARPI je typicky celočíselný index, který se mapuje na specifické konfigurace politik RRM předem definované v RAN. Toto mapování umožňuje síťovým operátorům definovat vlastní chování RRM pro různé typy služeb, síťové slicy nebo kategorie účastníků bez nutnosti standardizace každé možné variace politiky.

V praxi ARPI umožňuje sofistikovanější diferenciaci služeb, než je možné pouze se standardními identifikátory tříd QoS ([QCI](/mobilnisite/slovnik/qci/)) nebo indikátory QoS pro 5G (5QI). Například zatímco dvě služby mohou mít identické požadavky na latenci a propustnost (stejný 5QI), mohou obdržet různé hodnoty ARPI, které indikují, že jedna by měla používat robustnější modulační schémata nebo jiné meze pro předání spojení. To operátorům umožňuje implementovat optimalizace specifické pro služby, které zohledňují faktory nad rámec základních parametrů QoS, jako jsou cíle spolehlivosti, preference energetické účinnosti nebo specifická pravidla sdílení rádiových prostředků mezi různými síťovými slicy.

## K čemu slouží

ARPI byl zaveden, aby řešil omezení stávajících mechanismů QoS při zvládání stále složitějších požadavků služeb a scénářů síťového sclingu v sítích 5G. Tradiční parametry QoS, jako jsou QCI a 5QI, definují základní charakteristiky služby, ale neposkytují dostatečnou granularitu pro operátory k implementaci diferencovaných politik RRM pro pokročilé služby. Jak se sítě vyvíjely, aby podporovaly různorodé případy užití od komunikací s ultra-spolehlivou nízkou latencí (URLLC) po masivní IoT, potřebovali operátoři flexibilnější nástroje pro řízení způsobu správy rádiových prostředků pro různé služby.

Vytvoření ARPI bylo motivováno potřebou vylepšené diferenciace služeb v prostředích síťového sclingu. Různé síťové slicy obsluhující různé vertikální odvětví (automobilový průmysl, zdravotnictví, průmyslové IoT) mohou vyžadovat nejen různé úrovně QoS, ale také různé chování RRM. Například slice pro tovární automatizaci může potřebovat agresivnější politiky předávání spojení než slice pro mobilní širokopásmový přístup, i když oba mají podobné požadavky na latenci. ARPI poskytuje mechanismus pro signalizaci těchto preferencí RRM specifických pro slice z jádra sítě do RAN.

Historicky byly politiky RRM z velké části určovány RAN na základě lokální konfigurace a standardizovaných parametrů QoS. Tento přístup omezoval schopnost jádra sítě ovlivňovat chování RAN pro konkrétní služby nebo účastníky. ARPI tuto mezeru překlenuje tím, že umožňuje, aby rozhodnutí o politikách přijatá v jádře sítě (potenciálně zohledňující profily účastníků, servisní dohody a požadavky síťových sliců) byla sdělena RAN a jím implementována. To umožňuje centralizovanější a konzistentnější uplatňování politik v celé síti, což je zvláště důležité pro plnění smluvních úrovní služeb (SLA) v prostředích s více dodavateli a pro implementaci pokročilé automatizace sítě.

## Klíčové vlastnosti

- Umožňuje diferenciaci politik RRM specifických pro službu nad rámec standardních parametrů QoS
- Podporuje síťový slicing tím, že umožňuje chování RRM specifické pro slice
- Přenášen v signalizaci NGAP a XnAP mezi jádrem sítě a RAN
- Používá mapování na bázi indexu na předem nakonfigurované politiky RRM v uzlech RAN
- Umožňuje vliv jádra sítě na rozhodnutí o správě prostředků v RAN
- Zvyšuje schopnost plnit různorodé požadavky SLA pro různé služby

## Definující specifikace

- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [ARPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/arpi/)
