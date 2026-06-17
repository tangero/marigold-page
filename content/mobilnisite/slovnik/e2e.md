---
slug: "e2e"
url: "/mobilnisite/slovnik/e2e/"
type: "slovnik"
title: "E2E – End-to-End"
date: 2026-01-01
abbr: "E2E"
fullName: "End-to-End"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e2e/"
summary: "E2E (end-to-end) označuje úplnou cestu služby nebo komunikace od zdrojového uživatelského zařízení k cílovému koncovému bodu, která prochází všemi síťovými doménami. Je to základní architektonický pri"
---

E2E (end-to-end) je úplná cesta služby od zdrojového uživatelského zařízení k cílovému koncovému bodu, která prochází všemi síťovými doménami za účelem zajištění kontinuity a výkonu.

## Popis

Ve standardech 3GPP je End-to-End (E2E) holistický architektonický a služební koncept, který definuje úplnou komunikační cestu mezi dvěma koncovými body, což mohou být uživatelská zařízení (UE), aplikační servery nebo jiné síťové funkce. Tato cesta zahrnuje všechny zúčastněné síťové segmenty: rádiovou přístupovou síť (RAN), páteřní síť (CN) a potenciálně i externí sítě, jako je internet nebo domény jiných operátorů. Perspektiva E2E je klíčová pro poskytování služeb, protože zajišťuje, že jsou požadavky na výkon, zabezpečení a funkčnost zachovány na každém přeskoku a přes administrativní hranice. Posouvá důraz z izolovaného výkonu síťových prvků na kompletní uživatelský zážitek a doručení služby.

Z architektonického hlediska jsou aspekty E2E zakotveny v definicích služeb a specifikacích požadavků. Například při definici nové služby, jako je rozšířené mobilní širokopásmové připojení (eMBB) nebo ultra-spolehlivá komunikace s nízkou latencí (URLLC), specifikuje 3GPP E2E klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je latence, spolehlivost a přenosová rychlost. Tyto KPI musí být splněny kolektivním výkonem RAN, přenosové sítě, funkcí páteřní sítě a jakýchkoli aplikačních serverů. To vyžaduje koordinaci mezi různými síťovými doménami, která je často řízena prostřednictvím řízení politik, zpřístupnění sítě a orchestračních funkcí, jako je Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)).

Z pohledu protokolu může E2E odkazovat na logické spojení mezi partnerskými entitami na nejvyšší vrstvě protokolového zásobníku, jako je aplikační vrstva. V systémové architektuře 3GPP však častěji odkazuje na služební vrstvu. Mechanismy jako toky kvality služeb (QoS) jsou zřizovány E2E, přičemž identifikátory třídy QoS ([QCI](/mobilnisite/slovnik/qci/)) a 5G identifikátory QoS ([5QI](/mobilnisite/slovnik/5qi/)) zajišťují, že pakety dostávají odpovídající zacházení od UE přes gNB/NG-RAN, User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) až do datové sítě. Síťové krájení (Network Slicing) je hlavním příkladem E2E konstrukce, kde je vytvořena logická síť zahrnující specifické zdroje RAN, přenosové a páteřní sítě, aby poskytla izolovanou E2E službu se zaručenými charakteristikami.

Role E2E v síti je zásadní pro zajištění služeb a inovace. Umožňuje operátorům nabízet smlouvy o úrovni služeb (SLA) podnikovým zákazníkům nebo vertikálním odvětvím, protože výkon může být garantován na celé síťové cestě. Pro systémy správy jsou monitorování služeb E2E a správa poruch zásadní pro rychlou izolaci problémů, které degradují kvalitu služby vnímanou uživatelem. Dále modely zabezpečení E2E zajišťují konzistentní aplikaci ochrany od zařízení až po cloudovou aplikaci, čímž předcházejí zranitelnostem na síťových hranicích.

## K čemu slouží

Koncept End-to-End (E2E) byl v 3GPP formálně zdůrazněn, aby řešil výzvy spojené s poskytováním konzistentních, vysoce kvalitních služeb napříč stále složitějšími a vícedoménovými síťovými architekturami. Rané mobilní sítě (2G, 3G) se primárně zaměřovaly na konektivitu v rámci rádiové a páteřní sítě jediného operátora. S příchodem služeb založených na IP, roamingu a propojení s externími paketovými datovými sítěmi se uživatelský zážitek stal závislým na výkonu všech procházených sítí. Nedostatek E2E pohledu ztěžoval garantování kvality služeb, řešení problémů a implementaci pokročilých funkcí, jako je prioritní zacházení s provozem pro specifické aplikace.

Zavedení E2E jako klíčového principu, zejména od Release 9 dále, bylo motivováno potřebou podporovat rozmanité služby s přísnými požadavky. Vzestup služeb v reálném čase (VoIP, videokonference), kritických komunikací a později aplikací pro IoT a vertikální odvětví vyžadoval předvídatelný výkon nejen na rádiovém spoji, ale na celé datové cestě. To bylo omezením předchozích přístupů, kde mechanismy QoS mohly být aplikovány pouze v páteřní síti, přičemž RAN nebo externí tranzitní sítě zůstávaly potenciálními úzkými místy. Návrh E2E zajišťuje, že jsou požadavky služby převedeny do specifických konfigurací a politik pro každý síťový segment, což umožňuje skutečnou služebně orientovanou architekturu.

Historicky učinila evoluce směrem k 5G a síťovému krájení (Network Slicing) koncept E2E nepostradatelným. Síťový řez (slice) je podle definice logická síť E2E. Vytvoření řezu pro tovární automatizaci nebo nasazení masivního IoT vyžaduje koordinovanou rezervaci a konfiguraci zdrojů v RAN, přenosové a páteřní síti. Rámec E2E definovaný ve specifikacích, jako je TS 22.261 (požadavky na služby 5G), poskytuje plán, jak jsou tyto izolované E2E sítě koncipovány, vytvářeny a spravovány, čímž řeší problém síťové rigidity a umožňuje jedné fyzické infrastruktuře podporovat nespočet přizpůsobených virtuálních sítí.

## Klíčové vlastnosti

- Holistická definice služby zahrnující UE, RAN, páteřní síť a datovou síť
- Umožňuje definici a garantování klíčových ukazatelů výkonu (KPI) E2E
- Základ pro síťové krájení (Network Slicing), vytváření logických izolovaných sítí E2E
- Podporuje koordinované vynucování politik QoS napříč všemi síťovými doménami
- Nezbytné pro monitorování, zajištění a správu poruch služeb E2E
- Usnadňuje smlouvy o úrovni služeb (SLA) s podniky a vertikálními odvětvími

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TR 22.893** (Rel-10) — IP Service Interconnection Requirements Study
- **TS 29.548** (Rel-19) — SEAL Data Delivery Server Services Stage 3
- **TS 33.863** (Rel-14) — Security for Battery-Efficient IoT Device to Enterprise

---

📖 **Anglický originál a plná specifikace:** [E2E na 3GPP Explorer](https://3gpp-explorer.com/glossary/e2e/)
