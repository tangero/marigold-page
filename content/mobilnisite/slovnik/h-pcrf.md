---
slug: "h-pcrf"
url: "/mobilnisite/slovnik/h-pcrf/"
type: "slovnik"
title: "H-PCRF – Home Policy and Charging Rules Function"
date: 2025-01-01
abbr: "H-PCRF"
fullName: "Home Policy and Charging Rules Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-pcrf/"
summary: "H-PCRF (domácí funkce stanovování pravidel pro řízení přístupových politik a účtování) je prvek základní sítě 4G/LTE, který určuje pravidla pro řízení přístupových politik a účtování pro roamující úča"
---

H-PCRF (domácí funkce stanovování pravidel pro řízení přístupových politik a účtování) je prvek základní sítě 4G/LTE v domovské síti, který určuje pravidla pro řízení přístupových politik a účtování pro roamující účastníky prostřednictvím komunikace s navštíveným PCRF.

## Popis

H-PCRF (domácí funkce stanovování pravidel pro řízení přístupových politik a účtování) je ústřední komponenta v architektuře základní sítě 4G Evolved Packet Core (EPC), konkrétně v rámci Policy and Charging Control (PCC). Slouží jako bod rozhodování o přístupových politikách pro účastníky, kteří roamují mimo svou domovskou síť. H-PCRF sídlí v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) a komunikuje s navštíveným PCRF (V-PCRF) v navštívené síti (VPLMN) přes referenční bod S9. Jejím hlavním úkolem je poskytovat navštívené síti pravidla pro řízení přístupových politik a účtování od domovského operátora, čímž zajišťuje konzistentní uplatňování služeb specifických pro účastníka, kvality služeb (QoS) a mechanismů účtování během roamování.

Architektonicky je H-PCRF součástí PCRF, který je mozkem systému PCC. Ve scénářích roamování je PCRF logicky rozdělen na V-PCRF a H-PCRF. V-PCRF komunikuje s funkcí vynucování pravidel (PCEF) v bráně PDN ([P-GW](/mobilnisite/slovnik/p-gw/)) navštívené sítě, aby prosazoval politiky na úrovni přenosového kanálu. Když rozhodnutí o přístupových politikách vyžadují vstup z domovské sítě – například kvůli profilům služeb účastníka, limitům datového využití nebo specifickým autorizacím QoS – V-PCRF předává požadavky H-PCRF přes rozhraní S9. H-PCRF poté učiní konečné rozhodnutí o přístupové politice na základě dat účastníka získaných z úložiště profilů předplatitelů (SPR) nebo později z uživatelského datového úložiště (UDR).

H-PCRF funguje pomocí protokolu Diameter přes rozhraní S9, což je rozšíření rozhraní Gx používaného pro PCC v neramujících scénářích. Přijímá požadavky Diameter (např. [CCR](/mobilnisite/slovnik/ccr/) - Credit-Control-Request) od V-PCRF obsahující informace o [IP-CAN](/mobilnisite/slovnik/ip-can/) relaci UE. H-PCRF tyto požadavky zpracuje na základě politik domovské sítě a informací o účastníkovi. Následně vrací odpovědi Diameter (např. [CCA](/mobilnisite/slovnik/cca/) - Credit-Control-Answer) s pravidly PCC. Tato pravidla zahrnují parametry pro QoS ([QCI](/mobilnisite/slovnik/qci/), [ARP](/mobilnisite/slovnik/arp/), přenosové rychlosti), řízení povolování přístupu (povolit/blokovat) a instrukce pro účtování (online přes [OCS](/mobilnisite/slovnik/ocs/), offline přes OFCS). V-PCRF tato pravidla předává PCEF k provedení.

Klíčové komponenty komunikující s H-PCRF zahrnují referenční bod S9 pro komunikaci s V-PCRF, referenční bod Sp/UD pro přístup k datům účastníků ze SPR/UDR a potenciálně rozhraní Rx pro přijímání servisních informací od aplikačních funkcí (AF). Její role je klíčová pro umožnění pokročilých služeb, jako je sponzorovaný přenos dat, vrstvená QoS a roamující paketové filtry. Díky centralizaci logiky přístupových politik domovské sítě umožňuje H-PCRF navštíveným sítím implementovat politiky bez nutnosti znát kompletní údaje o účastníkovi, čímž zjednodušuje mezisíťové dohody a zajišťuje soulad s obchodními modely domovského operátora.

## K čemu slouží

H-PCRF byla zavedena ve 3GPP Release 8 jako součást nové architektury Policy and Charging Control (PCC) pro Evolved Packet Core (EPC). Byla vytvořena, aby řešila omezení starších mechanismů kontroly přístupových politik v sítích 2G/3G, které byly méně flexibilní a často vázané na konkrétní přístupové technologie. Před PCC byly přístupové politiky a účtování řešeny odděleně s omezenou dynamickou kontrolou, což ztěžovalo implementaci sofistikované diferenciace služeb a účtování v reálném čase pro roamující uživatele.

Hlavní motivací pro H-PCRF bylo umožnit dynamickou, na účastníka zaměřenou kontrolu přístupových politik a účtování ve scénářích roamování. S globálním rozšiřováním nasazení LTE potřebovali operátoři standardizovaný způsob, jak vynucovat politiky domovské sítě – jako je spravedlivé využívání, priorizace služeb a roamingové dohody – když se účastníci připojili k navštíveným sítím. H-PCRF prostřednictvím rozhraní S9 poskytla standardizovaný protokol (Diameter) a proceduru, pomocí které domovské sítě mohly vykonávat kontrolu nad QoS a účtováním, čímž zajišťovala konzistentní uživatelský zážitek a přesné účtování přes hranice.

Dále H-PCRF řešila problém škálovatelného řízení přístupových politik pro roamování. Oddělením domácích a navštívených funkcí pro přístupové politiky snížila signalizační zátěž na navštívených sítích a chránila data účastníků domovské sítě. Také usnadnila zavádění nových služeb, jako je Application Detection and Control (ADC) a sponzorovaný přístup k datům, v kontextu roamování. Koncepce H-PCRF byla zásadní pro komerční úspěch roamování v sítích LTE, neboť umožnila operátorům nabízet komplexní služební plány a udržovat jistotu příjmů, zatímco byli účastníci v zahraničí.

## Klíčové vlastnosti

- Slouží jako domácí síťový bod rozhodování o přístupových politikách pro roamující účastníky v 4G EPC
- Komunikuje s navštíveným PCRF (V-PCRF) přes referenční bod S9 založený na protokolu Diameter
- Poskytuje PCC pravidla zahrnující QoS, řízení povolování přístupu a instrukce pro účtování
- Přistupuje k profilům účastníků ze SPR/UDR pro personalizovaná rozhodnutí o přístupových politikách
- Podporuje dynamickou kontrolu přístupových politik pro služby jako je sponzorovaný přenos dat a vrstvená QoS
- Umožňuje konzistentní vynucování politik domovského operátora napříč navštívenými sítěmi

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface
- **TS 29.816** (Rel-10) — PCRF Failure & Restoration Study
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 32.843** (Rel-13) — PS Domain Online Charging in Roaming

---

📖 **Anglický originál a plná specifikace:** [H-PCRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-pcrf/)
