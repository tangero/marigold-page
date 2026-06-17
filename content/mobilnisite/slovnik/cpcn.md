---
slug: "cpcn"
url: "/mobilnisite/slovnik/cpcn/"
type: "slovnik"
title: "CPCN – Control Plane data transfer Charging Node"
date: 2025-01-01
abbr: "CPCN"
fullName: "Control Plane data transfer Charging Node"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cpcn/"
summary: "Účtovací uzel odpovědný za shromažďování a zpracování účtovacích dat pro přenosy dat po řídicí rovině v sítích 3GPP. Zpracovává účtování za data přenášená přes uzly MME, SCEF a IWK-SCEF, což umožňuje"
---

CPCN je účtovací uzel, který shromažďuje a zpracovává účtovací data pro přenosy dat po řídicí rovině přes uzly jako MME a SCEF, což umožňuje přesné účtování služeb, jako je doručování IoT dat.

## Popis

Control Plane data transfer Charging Node (CPCN) je specializovaná účtovací funkce zavedená ve 3GPP Release 17 pro zpracování účtování za přenosy dat, které probíhají po řídicí rovině namísto tradiční uživatelské roviny. V sítích 3GPP určité služby – zejména IoT aplikace a doručování ne-IP dat ([NIDD](/mobilnisite/slovnik/nidd/)) – využívají řídicí rovinu pro přenos malých, nepravidelných datových přenosů za účelem optimalizace síťové efektivity a životnosti baterie zařízení. CPCN shromažďuje, zpracovává a předává záznamy o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) generované síťovými uzly zapojenými do těchto přenosů dat po řídicí rovině, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Service Capability Exposure Function (SCEF) a Interworking SCEF ([IWK-SCEF](/mobilnisite/slovnik/iwk-scef/)).

Architektonicky CPCN funguje v rámci systému účtování definovaného ve specifikacích 3GPP, rozhraní se síťovými funkcemi přes standardizované referenční body. Přijímá účtovací události a informace o relacích od MME, SCEF a IWK-SCEF prostřednictvím rozhraní Rf (offline účtování) nebo Ro (online účtování) v závislosti na scénáři nasazení. CPCN agreguje tato data, aplikuje účtovací politiky na základě profilů účastníků, typů služeb a využití dat a generuje formátované CDR pro fakturační systémy. Podporuje jak účtování založené na událostech (pro jednotlivé transakce), tak účtování založené na relacích (pro dlouhodobé datové relace po řídicí rovině), čímž zajišťuje flexibilitu pro různé modely IoT služeb.

Klíčové součásti CPCN zahrnují funkci spouštěče účtování, která detekuje události přenosu dat po řídicí rovině; zpracovatelský engine účtovacích dat, který aplikuje tarifní pravidla a koreluje události z více uzlů; a modul generování CDR, který vytváří standardům odpovídající záznamy pro následné fakturační systémy. CPCN se také integruje s funkcemi řízení politik pro vynucování výdajových limitů a řízení účtování v reálném čase. Jeho role je klíčová pro zpoplatnění služeb přenosu dat po řídicí rovině, poskytuje operátorům detailní přehled o využití prostředků pro IoT nasazení a zajišťuje soulad s regulatorními požadavky na přesnost účtování.

Během provozu, když IoT zařízení iniciuje přenos dat po řídicí rovině – například odesílání senzorových dat přes NIDD – zapojený MME nebo SCEF vygeneruje účtovací informace včetně objemu dat, časových razítek, identifikátoru zařízení a parametrů služby. Tyto informace jsou odeslány do CPCN, který ověří data vůči profilům účastníků, vypočítá poplatky na základě nakonfigurovaných tarifů a vytvoří CDR. Pro online účtování může CPCN komunikovat s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) za účelem autorizace transakce v reálném čase před povolením přenosu dat. Tím je zajištěno, že předplacení účastníci nepřekročí své limity, a umožňuje okamžité účtování služeb IoT typu pay-as-you-go.

## K čemu slouží

CPCN byl vytvořen k řešení výzev účtování zaváděných mechanismy přenosu dat po řídicí rovině v sítích 3GPP, zejména pro služby IoT a komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)). Před jeho zavedením bylo účtování za data přenášená po řídicí rovině zpracováváno nekonzistentně nebo jako součást obecného účtování paketových dat, což postrádalo granularitu a přesnost potřebnou pro účtovací modely specifické pro IoT. Tradiční účtovací systémy byly optimalizovány pro data na uživatelské rovině (např. prohlížení internetu na smartphonech) a nedokázaly zachytit jedinečné charakteristiky přenosů dat po řídicí rovině, jako jsou malé velikosti zpráv, nepravidelné přenosové vzorce a ne-IP protokoly.

Historicky, jak se 3GPP vyvíjelo k podpoře masivních IoT nasazení ve verzích 13-16, funkce jako Control Plane CIoT EPS Optimization a [NIDD](/mobilnisite/slovnik/nidd/) se staly nezbytnými pro efektivní IoT komunikaci. Architektura účtování však zaostávala, což vytvořo mezeru v možnostech zpoplatnění. Operátoři potřebovali způsob, jak tyto služby přesně účtovat, ať už na základě počtu zpráv, objemu dat nebo spouštěčů založených na událostech. CPCN tuto mezeru zaplňuje tím, že poskytuje vyhrazený účtovací uzel, který rozumí specifikům přenosů dat po řídicí rovině, což umožňuje nové zdroje příjmů z IoT služeb a zároveň zajišťuje sledování spravedlivého využití.

CPCN řeší několik omezení předchozích přístupů: odděluje účtování na řídicí rovině od účtování na uživatelské rovině, což umožňuje přizpůsobené tarifní modely; podporuje účtování pro scénáře propojování (přes [IWK-SCEF](/mobilnisite/slovnik/iwk-scef/)), kde IoT zařízení roamují mezi sítěmi 3GPP a ne-3GPP; a umožňuje detailní korelaci účtování napříč uzly MME a SCEF, což je klíčové pro fakturaci služeb end-to-end. Standardizací CPCN ve specifikacích 3GPP průmysl zajišťuje interoperabilitu mezi síťovým vybavením a fakturačními systémy, snižuje integrační náklady a urychluje nasazování IoT služeb.

## Klíčové vlastnosti

- Shromažďuje účtovací data z MME, SCEF a IWK-SCEF pro přenosy po řídicí rovině
- Generuje standardům odpovídající CDR pro služby doručování IoT a ne-IP dat
- Podporuje jak offline (Rf), tak online (Ro) účtovací rozhraní
- Umožňuje modely účtování založené na událostech i na relacích pro flexibilitu
- Integruje se s řízením politik pro limity výdajů a autorizaci v reálném čase
- Koreluje účtovací události napříč více síťovými uzly pro přesné účtování

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [IWK-SCEF – InterWorking - Service Capability Exposure Function](/mobilnisite/slovnik/iwk-scef/)
- [NIDD – Non-IP Data Delivery](/mobilnisite/slovnik/nidd/)

## Definující specifikace

- **TR 28.816** (Rel-17) — Charging for 5G Cellular IoT
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification

---

📖 **Anglický originál a plná specifikace:** [CPCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpcn/)
