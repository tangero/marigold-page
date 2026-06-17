---
slug: "a2p"
url: "/mobilnisite/slovnik/a2p/"
type: "slovnik"
title: "A2P – Application to Person"
date: 2026-01-01
abbr: "A2P"
fullName: "Application to Person"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/a2p/"
summary: "A2P (Application to Person) označuje komunikaci iniciovanou strojem a směřovanou k lidským uživatelům, typicky pro služební oznámení, upozornění nebo interaktivní zasílání zpráv. Umožňuje aplikacím, s"
---

A2P je komunikace iniciovaná strojem a směřovaná k lidskému uživateli, která umožňuje aplikacím nebo službám odesílat zprávy, hovory nebo datové relace na koncová uživatelská zařízení za účelem oznámení, upozornění nebo interaktivního zasílání zpráv.

## Popis

A2P (Application to Person) je standardizovaný komunikační paradigma v sítích 3GPP, kde aplikace, služby nebo síťové funkce iniciují komunikaci směrem k zařízením lidských uživatelů. Na rozdíl od tradiční komunikace mezi osobami (P2P) má u A2P původ v automatizovaných systémech, které odesílají zprávy, navazují hovory nebo iniciují datové relace za účelem doručení oznámení, upozornění, aktualizací služeb nebo interaktivního obsahu. Architektura zahrnuje několik klíčových komponent: A2P Service Capability Server (SCS) nebo Application Server ([AS](/mobilnisite/slovnik/as/)), který hostuje aplikační logiku; Service Capability Exposure Function (SCEF) nebo Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) v 5G, která poskytuje zabezpečená síťová [API](/mobilnisite/slovnik/api/); a základní síťové prvky jako SMS Service Center (SMSC), IP Multimedia Subsystem (IMS) nebo funkce 5G Core, které zajišťují vlastní doručení k uživatelskému zařízení (UE).

Technicky A2P funguje prostřednictvím standardizovaných rozhraní a protokolů definovaných ve specifikacích 3GPP. Aplikační server komunikuje se sítí přes API vystavená SCEF (4G) nebo NEF (5G) za použití protokolů jako [HTTP](/mobilnisite/slovnik/http/)/2 s [JSON](/mobilnisite/slovnik/json/) datovou částí. Tyto požadavky jsou následně přeloženy do nativní síťové signalizace. Pro zasílání zpráv to typicky zahrnuje protokoly [MAP](/mobilnisite/slovnik/map/) nebo Diameter pro rozhraní s SMSC nebo [IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/). Pro hlasové nebo multimediální relace je zapojen IMS core využívající SIP signalizaci. Síť ověří a autorizuje A2P požadavek, aplikuje příslušné politiky (jako filtrování spamu, omezení rychlosti a účtování) a směruje komunikaci k cílovému účastníkovi na základě jeho [MSISDN](/mobilnisite/slovnik/msisdn/), IMSI nebo SUPI.

Mezi klíčové architektonické aspekty patří oddělení aplikační vrstvy od přenosové sítě, což umožňuje poskytovatelům služeb vyvíjet A2P služby nezávisle na podkladové síťové technologii. Exposiční funkce (SCEF/NEF) hrají kritickou roli abstrahováním síťových schopností a poskytováním zabezpečeného, škálovatelného a účtovatelného rozhraní. Dále musí implementace A2P řešit aspekty jako meziodběratelské směrování (když odesílatel a příjemce patří k různým mobilním sítím), hlášení o doručení a zpracování chyb. V systémech 5G A2P těží z network slicing, což umožňuje vyhrazené řezy se specifickou QoS pro různé typy A2P služeb, jako jsou kritická upozornění s nízkou latencí nebo finanční oznámení s vysokou spolehlivostí.

Role A2P v síťovém ekosystému je mnohostranná. Umožňuje monetizaci síťových schopností tím, že umožňuje poskytovatelům služeb třetích stran integrovat komunikaci do svých aplikací. Také podporuje četné vertikální odvětví: bankovnictví (upozornění na transakce), dopravu (potvrzení rezervací), zdravotnictví (upomínky na schůzky) a IoT (oznámení o stavu zařízení). Z pohledu sítě musí být provoz A2P efektivně řízen, aby se předešlo přetížení, musí být vhodně prioritizován vůči P2P provozu a musí být zabezpečen proti podvržení a podvodům. Specifikace 3GPP definují mechanismy pro ověření identity, diferenciaci provozu a řízení politik, aby byla zajištěna spolehlivost, zabezpečení a vysoká kvalita A2P služeb.

## K čemu slouží

Technologie A2P existuje za účelem usnadnění automatizované, škálovatelné a spolehlivé komunikace od aplikací a strojů k lidským účastníkům. Řeší problém umožnění službám, podnikům a IoT systémům proaktivně komunikovat s uživateli bez manuálního zásahu. Před standardizovanými A2P frameworky byly takové komunikace často realizovány ad-hoc metodami, jako jsou základní SMPP připojení k SMSC, kterým chyběla standardizovaná bezpečnost, řízení politik, meziodběratelské dohody a záruky kvality služby. To vedlo k problémům jako spam, podvody (např. podvržená ID odesílatele), síťové přetížení a nekonzistentní uživatelské zkušenosti napříč různými operátory a regiony.

Vytvoření A2P v rámci 3GPP bylo motivováno explozivním růstem mobilních aplikací, IoT a digitálních služeb, které vyžadují automatizovaná oznámení a interakce. Historický kontext zahrnuje rané použití SMS pro upozornění, které se vyvinulo ve složitější multimediální a interaktivní zasílání zpráv. Omezení předchozích přístupů zahrnovala neschopnost využít rich communication services (RCS), nedostatek podpory pro IP multimediální relace a absenci standardizovaného způsobu, jak bezpečně vystavit síťové schopnosti (jako lokalizaci nebo QoS) autorizovaným aplikacím. Standardizace 3GPP to řeší definováním jasných architektonických rolí, bezpečnostních frameworků a rozhraní, která umožňují inovace při současné ochraně integrity sítě a soukromí uživatelů.

Dále standardizace A2P podporuje nové obchodní modely, jako je sdílení výnosů založené na API mezi mobilními síťovými operátory a poskytovateli aplikací. Také řeší regulatorní požadavky na autenticitu zpráv (např. zákony proti podvržení) a nouzová upozornění. Poskytnutím jednotného frameworku 3GPP zajišťuje interoperabilitu napříč globálními sítěmi, což umožňuje bezproblémové A2P služby pro roamující účastníky a podporuje zdravý ekosystém pro vývojáře, operátory a koncové uživatele.

## Klíčové vlastnosti

- Standardizovaná síťová API prostřednictvím SCEF (4G) a NEF (5G) pro zabezpečený přístup aplikací
- Podpora více typů komunikace: SMS, MMS, RCS a IP hlasové/videohovory
- Integrované řízení politik pro správu provozu, filtrování spamu a omezení rychlosti
- Komplexní zabezpečení zahrnující autentizaci aplikací, integritu zpráv a mechanismy proti podvržení
- Schopnosti meziodběratelského směrování a vyúčtování pro mezisíťové A2P služby
- Diferenciace kvality služby (QoS) a podpora network slicing v 5G

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TS 28.851** (Rel-19) — Charging for Next Gen Real Time Communication Phase 2
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2

---

📖 **Anglický originál a plná specifikace:** [A2P na 3GPP Explorer](https://3gpp-explorer.com/glossary/a2p/)
