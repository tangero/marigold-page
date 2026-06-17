---
slug: "asp"
url: "/mobilnisite/slovnik/asp/"
type: "slovnik"
title: "ASP – Application Service Provider"
date: 2026-01-01
abbr: "ASP"
fullName: "Application Service Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/asp/"
summary: "Entita, která poskytuje aplikační služby uživatelům přes sítě 3GPP a umožňuje integraci služeb třetích stran a nabídky přidané hodnoty. Hraje klíčovou roli v ekosystému poskytování služeb hostováním a"
---

ASP je entita, která poskytuje aplikační služby uživatelům přes sítě 3GPP, hostuje aplikace a rozhraní se síťovými schopnostmi, aby umožnila integraci služeb třetích stran.

## Popis

Application Service Provider (ASP) je základní architektonická komponenta v sítích 3GPP, která představuje externí entitu poskytující služby aplikační vrstvy koncovým uživatelům. ASP funguje mimo důvěryhodnou doménu operátora mobilní sítě, ale s ní komunikuje prostřednictvím standardizovaných referenčních bodů a aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), primárně definovaných v architekturách 3GPP Service Capability Exposure Function (SCEF) a Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)). ASP hostuje aplikační servery, vykonává servisní logiku, spravuje uživatelská data specifická pro své služby a iniciuje komunikaci s uživatelským zařízením (UE) nebo síťovými funkcemi za účelem doručení svých služeb. Toto oddělení umožňuje specializovaný vývoj služeb při současném využívání konektivity, zabezpečení a správy účastníků sítě 3GPP.

Technická činnost ASP zahrnuje několik klíčových rozhraní. Pro komunikaci strojového typu a služby IoT se ASP rozhraní s SCEF (ve 4G) nebo NEF (v 5G) pomocí standardizovaných RESTful API (např. založených na [HTTP](/mobilnisite/slovnik/http/)/[JSON](/mobilnisite/slovnik/json/)). Prostřednictvím těchto rozhraní může ASP žádat o síťové schopnosti, jako je spouštění zařízení (odesílání řídicích zpráv pro probuzení nebo příkaz UE), monitorování specifických událostí (jako dosažitelnost UE, změny polohy nebo selhání komunikace) a přístup k síťovým informacím (s souhlasem uživatele). ASP se vůči síti autentizuje a její požadavky jsou autorizovány na základě politik a předplatitelských dat. Síť následně na tyto požadavky reaguje a poskytuje ASP požadovanou službu nebo informaci při zachování síťové bezpečnosti a soukromí účastníka.

Architektonicky je ASP logická role, kterou mohou plnit různé reálné entity: firemní [IT](/mobilnisite/slovnik/it/) oddělení poskytující podnikové aplikace, poskytovatel cloudových služeb nabízející SaaS, platforma IoT spravující připojená zařízení nebo poskytovatel obsahu doručující mediální služby. V systému 5G (5GS) jsou interakce ASP podrobnější a služebně orientované, v souladu s principy cloud-nativního 5G Core. ASP se může přihlásit k odběru notifikací o síťových událostech a vyvolávat servisní operace prostřednictvím NEF, který funguje jako zabezpečený zprostředkovatel a bod vynucování politik. ASP je také klíčová pro koncept Edge Computing, kde mohou být instance aplikací nasazeny na síťovém okraji (prostřednictvím Edge Application Server) za účelem dosažení ultra-nízké latence, což je kritické pro služby jako průmyslová automatizace, rozšířená realita a inteligentní doprava.

Role ASP se rozšiřuje do oblasti účtování služeb a řízení politik. Může poskytovat služebně specifické informace síťovým účtovacím systémům (jako [CHF](/mobilnisite/slovnik/chf/) v 5G), aby umožnila diferencované účtování na základě využití aplikace. Pro řízení politik může ASP ovlivňovat kvalitu služby (QoS) pro své datové toky komunikací s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)). To umožňuje například ASP poskytujícímu službu videokonferencí požádat o přenos s garantovanou přenosovou rychlostí pro svůj provoz. Dále, v kontextu Network Slicing, může být ASP asociována se specifickým síťovým řezem (identifikovaným S-NSSAI), aby obdržela přizpůsobené síťové charakteristiky odpovídající jejím servisním požadavkům, jako je vylepšené mobilní širokopásmové připojení, ultra-spolehlivá komunikace s nízkou latencí nebo masivní konektivita IoT.

## K čemu slouží

Koncept ASP byl zaveden, aby formalizoval a standardizoval vztah mezi operátory mobilních sítí a poskytovateli služeb třetích stran, což se stalo kritickou potřebou s nástupem mobilních datových služeb a internetové ekonomiky. Před jeho standardizací se služby třetích stran často spoléhaly na nestandardní, proprietární integrace nebo fungovaly zcela "over-the-top" ([OTT](/mobilnisite/slovnik/ott/)) bez možnosti využívat vnitřní síťové schopnosti, jako je kvalita služby, přesné spouštění zařízení nebo služby s přihlédnutím k účastníkovi. To omezovalo sofistikovanost, spolehlivost a výkon mobilních aplikací. Model ASP, zavedený v 3GPP Release 8 spolu s Evolved Packet System (EPS), vytvořil rámec pro bezpečnou, škálovatelnou a účtovatelnou integraci externích služeb, což umožnilo, aby se síť operátora stala platformou pro inovace.

Primární problém, který architektura ASP řeší, je bezpečné vystavení síťových schopností autorizovaným externím entitám. Bez standardizovaného rozhraní ASP by operátoři čelili bezpečnostním rizikům a složitosti správy při povolování externího přístupu. Rámec ASP definuje mechanismy autentizace, autorizace a účtování (AAA), zajišťující, že pouze prověření poskytovatelé mají přístup k síťovým API a pouze pro povolené účely. Řeší také obchodní problém monetizace služeb, poskytuje jasné mechanismy pro operátory, aby účtovali ASP za využití síťových zdrojů a schopností, čímž vytváří nové zdroje příjmů nad rámec pouhé konektivity.

Dále je model ASP nezbytný pro umožnění pokročilých služeb, jako je Internet věcí (IoT), kde je třeba, aby cloudové aplikace spolehlivě dosáhly zařízení s přerušovanou konektivitou (prostřednictvím spouštění zařízení), nebo kde aplikace potřebují být informovány o změnách stavu zařízení. Také podporuje vizi 5G "síť jako služba" a podporu vertikálních odvětví, což podnikům (fungujícím jako ASP) umožňuje přímo řídit a přizpůsobovat svůj výsek sítě pro aplikace jako automatizace továren, chytrá síť nebo zdravotnictví. Vývoj role ASP v následujících vydáních odráží rostoucí význam otevřenosti a programovatelnosti sítě v telekomunikačním průmyslu.

## Klíčové vlastnosti

- Hostuje aplikační logiku a servery mimo jádrovou síť operátora
- Komunikuje s funkcemi pro vystavení sítě (SCEF/NEF) prostřednictvím standardizovaných RESTful API
- Může žádat o síťové schopnosti, jako je spouštění zařízení a monitorování událostí
- Ovlivňuje QoS a řízení politik pro své aplikační datové toky
- Podílí se na účtovacích mechanismech poskytováním služebně specifických dat
- Může být asociována se specifickými síťovými řezy (Network Slices) za účelem získání přizpůsobené konektivity

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 22.895** (Rel-12) — 3GPP SSO Framework Integration Study
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 26.532** (Rel-19) — 5G Data Collection and Reporting API Specification
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [ASP na 3GPP Explorer](https://3gpp-explorer.com/glossary/asp/)
