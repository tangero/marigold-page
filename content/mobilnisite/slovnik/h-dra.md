---
slug: "h-dra"
url: "/mobilnisite/slovnik/h-dra/"
type: "slovnik"
title: "H-DRA – Home Diameter Routing Agent"
date: 2025-01-01
abbr: "H-DRA"
fullName: "Home Diameter Routing Agent"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-dra/"
summary: "H-DRA je směrovací uzel protokolu Diameter v domácí síti. Směruje signalizační zprávy Diameter (např. pro autentizaci, politiky, účtování) mezi síťovými funkcemi na základě identity účastníka a domény"
---

H-DRA je směrovací uzel protokolu Diameter v domácí síti, který směruje signalizační zprávy mezi síťovými funkcemi na základě identity účastníka a domény (realm) za účelem škálovatelných operací páteřní sítě.

## Popis

Home Diameter Routing Agent (H-DRA) je specializovaná síťová funkce definovaná v architektuře Policy and Charging Control (PCC) standardu 3GPP. Funguje jako stavový směrovací uzel protokolu Diameter výrazně v rámci hranic domácí sítě účastníka. Protokol Diameter je primárním signalizačním protokolem používaným v páteřních sítích LTE a 5G pro funkce jako autentizace ([AAA](/mobilnisite/slovnik/aaa/)), řízení politik a účtování. Hlavní funkcí H-DRA je přijímat požadavky Diameter, prozkoumat klíčové atributy uvnitř zpráv – především User-Name ([IMSI](/mobilnisite/slovnik/imsi/)) a Destination-Realm – a směrovat je ke správné cílové síťové funkci, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Policy and Charging Rules Function (PCRF) nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)).

Z architektonického hlediska se H-DRA nachází na signalizační cestě mezi klienty Diameter (jako [MME](/mobilnisite/slovnik/mme/), SGSN nebo [P-CSCF](/mobilnisite/slovnik/p-cscf/)) a servery Diameter (jako HSS nebo PCRF). Udržuje vazební cache (binding cache) nebo směrovací tabulku, která mapuje identity účastníků (např. IMSI) na konkrétní instanci serveru, která daného účastníka aktuálně obsluhuje. To je zásadní pro udržování stavu relace a zajištění, že všechny související zprávy Diameter pro danou relaci účastníka jsou směrovány ke stejné instanci serveru, což je požadavek pro funkce jako relace politik. H-DRA používá Realm-Based Routing Table, nakonfigurovanou s politikami síťového operátora, k určení dalšího směrovacího kroku pro zprávy, pokud přímá vazba neexistuje.

Během provozu, když dorazí na H-DRA požadavek Diameter (např. Credit-Control-Request od [P-GW](/mobilnisite/slovnik/p-gw/) k OCS), nejprve zkontroluje, zda pro daného účastníka a aplikaci existuje vazba. Pokud ano, přepošle zprávu k zaznamenanému serveru. Pokud ne, provede směrování na základě domény (realm), což často zahrnuje Diameter Redirect Agent ([DRA](/mobilnisite/slovnik/dra/)) nebo použití statické konfigurace, aby našel příslušný server. Jakmile úvodní zpráva naváže relaci, H-DRA vytvoří vazební záznam. Všechny následující zprávy pro tuto relaci pak použijí tuto vazbu pro přímé směrování, čímž se sníží latence a režie vyhledávání. H-DRA také poskytuje vyrovnávání zatížení mezi více instancemi serveru stejného typu (např. fond PCRF) a nabízí odolnost přesměrováním provozu při výpadku serveru.

## K čemu slouží

H-DRA byl zaveden, aby vyřešil problémy škálovatelnosti signalizace a složitosti, které se objevily s all-IP Evolved Packet Core (EPC) ve verzi 3GPP Release 8. Jak sítě přecházely na distribuované, cloudové architektury s mnoha instancemi funkcí páteřní sítě, přímá point-to-point spojení Diameter se stala nezvladatelnými. Vytvořila se síť spojení, kterou bylo obtížné škálovat, zabezpečovat a udržovat. H-DRA poskytuje centralizovanou směrovací vrstvu, která odděluje klienty Diameter od serverů.

Jeho zavedení bylo motivováno potřebou efektivního směrování s ohledem na účastníka. Bez DRA by každá síťová funkce musela znát adresu každého možného serveru pro každého účastníka, což je v rozsáhlých dynamických sítích nepraktické. H-DRA zavádí úroveň zprostředkování, která zjednodušuje topologii sítě, skrývá detaily nasazení serverů a umožňuje pokročilé funkce jako vyrovnávání zatížení a geografickou redundanci. Je klíčovým prvkem pro virtualizaci síťových funkcí (NFV), protože umožňuje přidávat nebo odebírat instance serverů bez nutnosti rekonfigurace každého klienta. Hraje také kritickou roli ve scénářích mezi operátory (prostřednictvím I-DRA) tím, že poskytuje zabezpečenou bránu pro signalizaci Diameter mezi různými síťami operátorů.

## Klíčové vlastnosti

- Stavové směrování zpráv Diameter na základě identity účastníka (IMSI) a vazby relace (session binding)
- Směrování na základě domény (Realm-Based Routing) pro počáteční přeposílání zpráv a komunikaci mezi doménami
- Vyrovnávání zatížení mezi více instancemi serverů Diameter (např. fond PCRF)
- Udržování vazby relace (Session Binding Maintenance) pro zajištění konzistentního směrování všech zpráv relace
- Skrytí topologie (Topology Hiding) abstrakcí adres serverů před klienty
- Usnadnění interoperability mezi různými implementacemi dodavatelů a síťovými doménami

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping

---

📖 **Anglický originál a plná specifikace:** [H-DRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-dra/)
