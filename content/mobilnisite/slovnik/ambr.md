---
slug: "ambr"
url: "/mobilnisite/slovnik/ambr/"
type: "slovnik"
title: "AMBR – Aggregated Maximum Bit Rate"
date: 2026-01-01
abbr: "AMBR"
fullName: "Aggregated Maximum Bit Rate"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ambr/"
summary: "AMBR je parametr QoS, který definuje maximální celkovou přenosovou rychlost povolenou pro všechny non-GBR přenosy (bearers) pro konkrétní UE nebo APN. Zajišťuje spravedlivé sdílení prostředků a brání"
---

AMBR je parametr QoS (Quality of Service), který definuje maximální celkovou přenosovou rychlost povolenou pro všechny non-GBR přenosy (bearers) uživatele nebo APN, aby zajistil spravedlivé sdílení prostředků v mobilních širokopásmových sítích.

## Popis

Aggregated Maximum Bit Rate (AMBR) je základní parametr kvality služeb (QoS) v rámci 3GPP Evolved Packet System (EPS) a 5G System (5GS). Funguje na dvou úrovních: UE-AMBR (na úrovni User Equipment) a [APN-AMBR](/mobilnisite/slovnik/apn-ambr/) (na úrovni Access Point Name, v 5GS známý jako Session-AMBR). UE-AMBR je vynucován základnovou stanicí (eNodeB v 4G, gNB v 5G) na rádiovém rozhraní a omezuje agregovanou přenosovou rychlost všech non-Guaranteed Bit Rate (non-GBR) přenosů (bearers) nebo QoS toků (QoS Flows) asociovaných s jedním UE. APN-AMBR (neboli Session-AMBR) je vynucován User Plane Function (PGW-U/[UPF](/mobilnisite/slovnik/upf/)) v jádře sítě a uplatňuje se na agregát všech non-GBR přenosů/QoS toků v rámci konkrétního PDN připojení nebo PDU session. Toto hierarchické vynucování zajišťuje kontrolu jak na rádiovém rozhraní pro spravedlivost při přidělování rádiových prostředků, tak na rozhraní Gi/SGi/N6 pro správu prostředků v přenosové síti a jádře sítě.

Z architektonického hlediska je AMBR parametr předplatného uložený v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)). Během vytváření nebo modifikace session je tento parametr načten a poskytnut Policy and Charging Rules Function (PCRF) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), která následně komunikuje autorizované hodnoty AMBR k vynucovacím bodům prostřednictvím Packet Data Network Gateway (PGW) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). Vynucovací uzly, jako jsou eNodeB/gNB a PGW-U/UPF, využívají mechanismy kontroly provozu (traffic policing), například algoritmy typu token bucket, ke sledování a tvarování agregovaného provozu, aby nepřekročil nastavený limit AMBR. Pakety, které limit překračují, mohou být zpožděny nebo zahozeny.

AMBR se uplatňuje výhradně na non-GBR přenosy (bearers) nebo QoS toky, které se používají pro best-effort služby, jako je prohlížení webu, e-mail nebo streamování videa. To je v protikladu k [GBR](/mobilnisite/slovnik/gbr/) přenosům, které mají vyhrazenou, garantovanou šířku pásma pro služby jako hlasové hovory nebo hraní her v reálném čase. Toto oddělení umožňuje síti poskytovat striktní záruky pro provoz citlivý na zpoždění, zatímco zbývající kapacita je efektivně sdílena mezi pružné (elastic) aplikace bez požadavků na reálný čas. V 5GS je tento koncept rozšířen funkcí Reflective QoS, kde si může UE odvodit pravidla QoS pro provoz v uplinku na základě označení paketů v downlinku, ale Session-AMBR zůstává stropem vynucovaným sítí.

Jeho role je klíčová pro efektivitu sítě a uživatelský zážitek. Tím, že omezuje celkovou best-effort šířku pásma na uživatele nebo session, AMBR předchází zahlcení sítě způsobenému několika náročnými uživateli, podporuje spravedlivé rozdělení prostředků mezi všechna připojená UE a umožňuje operátorům zavádět vrstvené služební plány. Je to klíčový nástroj pro správu provozu a jeho monetizaci, který tvoří základ pro diferencované datové balíčky bez nutnosti kontroly provozu na úrovni každého jednotlivého toku pro každou aplikaci.

## K čemu slouží

AMBR byl zaveden v 3GPP Release 8 spolu s EPS, aby řešil omezení dřívějších 3G systémů při správě explozivního růstu mobilního datového provozu. Před-4G sítě se primárně spoléhaly na parametry QoS na úrovni jednotlivých přenosů (bearers), ale postrádaly efektivní mechanismus pro kontrolu agregované spotřeby více současných datových session jednoho uživatele (např. web, e-mail, aktualizace aplikací). Bez AMBR by uživatel mohl vytvořit více non-GBR přenosů, z nichž každý by požadoval vysokou šířku pásma, a potenciálně vyčerpat rádiové a síťové prostředky v jádře sítě, čímž by degradoval službu pro ostatní uživatele. AMBR tento problém řeší tím, že poskytuje jednoduchý, vynutitelný strop pro celkový best-effort provoz uživatele.

Vznik AMBR byl motivován potřebou škálovatelného a praktického řízení QoS ve všech-IP sítích. Umožňuje operátorům nabízet „neomezené“ datové tarify s pravidly spravedlivého použití (fair usage) tím, že technicky omezuje maximální dosažitelnou propustnost, a chrání tak integritu sítě. Také umožňuje diferenciaci služeb; například prémiový předplatitel může mít vyšší UE-AMBR než základní předplatitel, i když používají stejné aplikace. Tím byla řešena klíčová obchodní potřeba pro vrstvené cenové modely.

Navíc AMBR poskytuje zásadní oddělení mezi zpracováním garantovaných a best-effort služeb. Tím, že se uplatňuje pouze na non-GBR provoz, zajišťuje, že síť může vždy rezervovat potřebné prostředky pro [GBR](/mobilnisite/slovnik/gbr/) služby (jako je VoLTE), aby splnila jejich striktní požadavky na zpoždění a spolehlivost, zatímco zbývající kapacita je dynamicky sdílena. Tento architektonický princip agregované kontroly pro pružný (elastic) provoz a vyhrazených prostředků pro nepružný (inelastic) provoz se ukázal jako zásadní pro podporu různorodé směsi služeb na moderních mobilních sítích.

## Klíčové vlastnosti

- Definuje maximální agregovanou přenosovou rychlost pro všechny non-Guaranteed Bit Rate (non-GBR) přenosy (bearers) nebo QoS toky (QoS Flows).
- Vynucován na dvou úrovních: na úrovni UE (UE-AMBR) na rádiovém rozhraní a na úrovni APN/PDU Session (APN-AMBR/Session-AMBR) v jádře sítě.
- Parametr založený na předplatném, uložený v HSS/UDM a autorizovaný PCRF/PCF.
- Používá mechanismy kontroly provozu (např. token bucket) ve vynucovacích bodech (RAN a UPF/PGW-U).
- Aplikuje se pouze na best-effort provoz, čímž zajišťuje, že GBR služby dostávají vyhrazené prostředky.
- Základní pro implementaci pravidel spravedlivého použití (fair usage) a vrstvených datových služebních plánů.

## Související pojmy

- [GBR – Generic Binaural Renderer](/mobilnisite/slovnik/gbr/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [AMBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ambr/)
