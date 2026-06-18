---
slug: "3gspec"
url: "/mobilnisite/slovnik/3gspec/"
type: "slovnik"
title: "3GSPEC – 3GPP Specific Proxy Mobile IPv6 Error Code"
date: 2025-01-01
abbr: "3GSPEC"
fullName: "3GPP Specific Proxy Mobile IPv6 Error Code"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/3gspec/"
summary: "Standardizovaný kód chyby definovaný v rámci protokolu Proxy Mobile IPv6 (PMIPv6) pro 3GPP-specifické chybové stavy. Umožňuje síťovým prvkům komunikovat přesné důvody selhání během procedur správy mob"
---

3GSPEC je standardizovaný kód chyby Proxy Mobile IPv6 pro 3GPP-specifické poruchy, který umožňuje síťovým prvkům komunikovat přesné důvody během mobilních procedur za účelem usnadnění odstraňování problémů v sítích EPC a 5G Core.

## Popis

3GSPEC je specifická hodnota kódu chyby definovaná v 3GPP Technical Specification 29.275 pro použití v rámci sady protokolů Proxy Mobile IPv6 (PMIPv6). PMIPv6 je síťový protokol správy mobility, který umožňuje IP mobilitu mobilního uzlu bez nutnosti jeho účasti na signalizaci mobility. V tomto rámci slouží 3GSPEC jako standardizovaný mechanismus k označení, že během PMIPv6 procedury došlo k chybovému stavu specifickému pro provoz 3GPP sítí, například při výměně zpráv Proxy Binding Update ([PBU](/mobilnisite/slovnik/pbu/)) nebo Proxy Binding Acknowledgment ([PBA](/mobilnisite/slovnik/pba/)) mezi Mobile Access Gateway ([MAG](/mobilnisite/slovnik/mag/)) a Local Mobility Anchor ([LMA](/mobilnisite/slovnik/lma/)).

Kód chyby funguje v poli Status Code zpráv hlavičky mobility PMIPv6. Když síťová entita (jako LMA v Packet Data Network Gateway, [PGW](/mobilnisite/slovnik/pgw/), nebo MAG v Serving Gateway, [SGW](/mobilnisite/slovnik/sgw/)) narazí na selhání definované specifikacemi 3GPP – například selhání ověření předplatného, neshodu parametrů QoS, selhání překladu [APN](/mobilnisite/slovnik/apn/) nebo nenalezení kontextu UE – může nastavit Status Code na hodnotu 3GSPEC. To signalizuje přijímající entitě, že podrobná příčina chyby je obsažena v následující 3GPP-specifické podvolbě chyby v této zprávě. Tato podvolba nese podrobnější hodnotu příčiny chyby, což umožňuje přesnou identifikaci důvodu selhání.

Z architektonického hlediska je 3GSPEC nedílnou součástí rozhraní S5/S8 v Evolved Packet Core (EPC) při použití varianty protokolu PMIPv6 (alternativou je [GTP](/mobilnisite/slovnik/gtp/)). Rozhraní S5 spojuje Serving Gateway (SGW) a Packet Data Network Gateway (PGW), zatímco S8 je jeho roamingový ekvivalent mezi SGW navštívené PLMN a PGW domovské PLMN. Když je na těchto rozhraních nasazen PMIPv6, umožňuje 3GSPEC standardizované hlášení chyb mezi těmito funkcemi jádra sítě. Jeho role je klíčová pro provoz, údržbu a správu poruch sítě, protože transformuje obecné PMIPv6 chyby na konkrétní, 3GPP-specifické diagnostické informace.

Implementace zahrnuje generování chybové odpovědi LMA (obvykle spolulokalizovaným s PGW) nebo MAG (obvykle spolulokalizovaným se SGW). Při detekci 3GPP-specifické chybové podmínky entita sestaví odpověď (např. PBA s chybovým stavem). Nastaví základní PMIPv6 Status Code na 3GSPEC a zahrne mobilní volbu '3GPP Specific Error Cause'. Tato vnořená volba obsahuje specifický kód příčiny chyby (např. 130 pro 'Missing or Unknown APN', 131 pro 'Unknown PDN Type' atd., jak definují specifikace 3GPP). Tato dvouúrovňová struktura – obecný 3GPP indikátor plus specifická příčina – zachovává kompatibilitu se standardem PMIPv6 od IETF a zároveň poskytuje podrobné, doménově specifické informace o chybě nezbytné pro správu 3GPP sítí a zpracování relací UE.

## K čemu slouží

Primárním účelem definice 3GSPEC bylo překlenout propast mezi obecnými možnostmi hlášení chyb standardizovaného protokolu Proxy Mobile IPv6 od IETF a specifickými, podrobnými scénáři selhání, ke kterým dochází v architekturách mobilních sítí 3GPP. PMIPv6, jak jej definuje IETF, poskytuje sadu obecných kódů chyb pro selhání na úrovni protokolu (jako chybějící parametry nebo selhání autentizace). Nicméně sítě 3GPP zahrnují četné složité, na dodavatelích a standardech závislé procedury související se správou předplatitelů, QoS, překladem APN a účtováním, které jsou mimo rozsah základní specifikace IETF. Bez mechanismu jako je 3GSPEC by PGW odmítající relaci z důvodu 'Unknown APN' mohl odeslat pouze obecnou PMIPv6 chybu, což by ponechalo SGW a systémy správy sítě bez přesné příčiny potřebné pro efektivní odstraňování problémů a automatizované obnovení.

Historicky, když 3GPP v Release 8 (EPC) přijalo PMIPv6 jako jednu z možností protokolu pro rozhraní S5/S8, bylo okamžitě zřejmé, že standardní kódy chyb IETF jsou nedostatečné. Síťoví operátoři potřebovali podrobné, standardizované informace o chybách pro udržení kvality služeb, diagnostiku roamingových problémů a zajištění správné interoperability mezi zařízeními od různých dodavatelů. 3GSPEC byl vytvořen, aby tuto potřebu naplnil, což umožnilo 3GPP definovat vlastní výčtový seznam příčin chyb v rámci PMIPv6. Tím byl vyřešen problém neprůhledných režimů selhání, což umožnilo rychlejší izolaci poruch, informativnější logování a potenciál pro inteligentnější síťové prvky k provedení nápravných akcí na základě přijaté specifické příčiny chyby.

Dále 3GSPEC podporuje architekturu 3GPP policy and charging control (PCC). Chyby související s provisioningem nebo vynucováním pravidel PCC z Policy and Charging Rules Function (PCRF) mohou být přesně komunikovány pomocí tohoto mechanismu. Řeší omezení předchozích přístupů, kdy by taková doménově specifická selhání byla buď nesprávně namapována na obecný kód, nebo by vyžadovala proprietární rozšíření, což by poškozovalo multi-vendorovou interoperabilitu. Standardizací tohoto kódu chyby a jeho přidružených podvoleb zajistilo 3GPP, že PMIPv6 může být robustním, operátorským protokolem pro správu mobility ve svých sítích.

## Klíčové vlastnosti

- Standardizované hlášení 3GPP chyb v rámci protokolu IETF PMIPv6
- Dvouúrovňová indikace chyby: obecný kód stavu 3GSPEC plus podrobná hodnota příčiny
- Umožňuje přesnou diagnostiku selhání souvisejících s předplatným, QoS, APN a kontexty PDN
- Kritický pro interoperabilitu na rozhraních S5/S8 používajících variantu PMIPv6
- Podporuje funkce provozu, správy a údržby (OAM) sítě
- Usnadňuje roamingové scénáře poskytováním jasných příčin chyb mezi navštívenou a domovskou sítí

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [3GSPEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/3gspec/)
