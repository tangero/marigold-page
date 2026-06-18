---
slug: "hnb"
url: "/mobilnisite/slovnik/hnb/"
type: "slovnik"
title: "HNB – Home Node B"
date: 2025-01-01
abbr: "HNB"
fullName: "Home Node B"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/hnb/"
summary: "Home Node B (HNB) je zařízení instalované u zákazníka, které poskytuje 3G UMTS rádiové pokrytí pro malou oblast, například domácnost nebo kancelář. Připojuje se k páteřní síti mobilního operátora pros"
---

HNB je zařízení instalované u zákazníka, které poskytuje 3G UMTS rádiové pokrytí pro malou oblast a připojuje se k páteřní síti operátora prostřednictvím domácího širokopásmového připojení.

## Popis

Home Node B (HNB) je nízkovýkonová, uživatelem nasazená základnová stanice definovaná 3GPP pro sítě UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)/[HSPA](/mobilnisite/slovnik/hspa/)). Jedná se o typ femtobuňky určené pro prostředí domácností nebo malých firem. Fyzicky se jedná o malé zařízení, které se zapojí do stávajícího širokopásmového internetového připojení uživatele (např. [DSL](/mobilnisite/slovnik/dsl/) nebo kabel). HNB vytváří licencovanou 3G rádiovou buňku, typicky pokrývající oblast o rozloze několika set až tisíc čtverečních stop, což umožňuje standardním 3G uživatelským zařízením (UE) připojit se k mobilní síti prostřednictvím tohoto lokalizovaného přístupového bodu.

Architektonicky obsahuje HNB základní funkce Node B (základnové stanice UMTS) a zjednodušeného řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Zpracovává rádiový přenos/příjem, modulaci/demodulaci, kódování kanálu a řízení výkonu. Pro síťové připojení navazuje přes veřejný internet zabezpečený [IPsec](/mobilnisite/slovnik/ipsec/) tunel k vyhrazené bráně v síti operátora, známé jako HNB Gateway ([HNB-GW](/mobilnisite/slovnik/hnb-gw/)). Tento tunel přenáší jak provoz uživatelské roviny (hlas a data), tak signalizaci řídicí roviny ([RANAP](/mobilnisite/slovnik/ranap/) přes rozhraní Iu-h). HNB-GW následně komunikuje s ústřednou mobilního spojení ([MSC](/mobilnisite/slovnik/msc/)) páteřní sítě pro okruhově spínané služby a s podpůrným uzlem GPRS (SGSN) pro paketově spínané služby, čímž se femtobuňka pro páteřní síť jeví jako standardní RNC.

HNB pracuje s pokročilými schopnostmi samokonfigurace a samooptymalizace. Skenuje rádiové prostředí, aby vybral vhodný nosný kmitočet UMTS a skramblovací kód, a minimalizoval tak rušení s makro sítí a sousedními HNB. Také implementuje řízení přístupu, typicky umožňující připojení pouze uzavřené skupině účastníků (CSG) – předem definovanému seznamu účastníků – čímž se mění na 'femtoblast' pro domácnost nebo firmu. Správa a provizionování jsou zajišťovány prostřednictvím samostatného rozhraní k systému správy HNB (HMS), který je součástí infrastruktury správy sítě operátora.

## K čemu slouží

HNB bylo vytvořeno k řešení přetrvávajícího problému špatného vnitřního pokrytí mobilním signálem, zejména pro 3G služby, které pracují na vyšších kmitočtech náchylnějších na útlum pronikání budovami. Umožňuje operátorům rozšířit kvalitní hlasové a datové pokrytí do domácností a kanceláří bez masivních kapitálových výdajů na nasazení dalších makro stanic. Odlehčuje provoz z makro sítě, čímž zlepšuje celkovou kapacitu a uživatelský zážitek.

Před femtobuňkami zahrnovala řešení pro vnitřní pokrytí pikobuňky (instalované operátorem) nebo Wi-Fi, ale ta měla svá omezení. Pikobuňky byly pro hromadné nasazení v domácnostech nákladné na instalaci a správu. Wi-Fi vyžadovala dvoupásmové telefony a nenabízela bezproblémovou kontinuitu služeb mobilní sítě. Koncept HNB využil uživatelův vlastní širokopásmový přenosový okruh, což dramaticky snížilo náklady na nasazení pro operátora, a zároveň poskytlo transparentní mobilní zážitek pro účastníka používajícího standardní 3G telefon.

Zavedení HNB ve 3GPP Release 8 bylo motivováno komerční potřebou zlepšit penetraci 3G služeb a konkurovat pevným hlasovým službám. Řešilo obavy operátorů ohledně zabezpečení přenosového okruhu, integrace sítí, řízení rušení a škálovatelné správy pro miliony nasazených jednotek. Ekosystém HNB umožnil nové obchodní modely, jako jsou tarify 'domácí zóny', a položil základy pro budoucí technologie malých buněk v 4G a 5G.

## Klíčové vlastnosti

- Nízkovýkonový rádiový přístup UMTS/WCDMA/HSPA pro vnitřní pokrytí
- Pro přenosový okruh využívá spotřebitelský broadband (DSL, kabel, optika) prostřednictvím zabezpečených IPsec tunelů
- Podporuje uzavřenou skupinu účastníků (CSG) pro omezený přístup
- Implementuje autonomní rádiovou konfiguraci a řízení rušení
- Integruje se s páteřní sítí operátora prostřednictvím standardizovaného rozhraní Iu-h k HNB-GW
- Vzdálená správa a provizionování prostřednictvím protokolu TR-069 nebo podobných protokolů

## Související pojmy

- [HNB-GW – Home Node B Gateway](/mobilnisite/slovnik/hnb-gw/)
- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)

## Definující specifikace

- **TS 22.220** (Rel-19) — Home NodeB/Home eNodeB Service Requirements
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.830** (Rel-9) — Home NodeB/HeNB Architecture and CSG Study
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.285** (Rel-19) — Allowed CSG List Management Object
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.444** (Rel-19) — HNB User Data Transport Protocols
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 25.468** (Rel-19) — RANAP User Adaption (RUA) protocol specification
- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface
- **TS 25.470** (Rel-19) — PCAP User Adaption (PUA) protocol specification
- **TS 25.471** (Rel-19) — RNSAP User Adaptation (RNA) for Iurh
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TS 25.866** (Rel-9) — 1.28Mcps TDD Home NodeB Study Report
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [HNB na 3GPP Explorer](https://3gpp-explorer.com/glossary/hnb/)
