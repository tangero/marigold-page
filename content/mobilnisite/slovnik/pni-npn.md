---
slug: "pni-npn"
url: "/mobilnisite/slovnik/pni-npn/"
type: "slovnik"
title: "PNI-NPN – Public Network Integrated Non-Public Network"
date: 2026-01-01
abbr: "PNI-NPN"
fullName: "Public Network Integrated Non-Public Network"
category: "Network Slicing"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pni-npn/"
summary: "PNI-NPN je architektura 3GPP, která umožňuje poskytování neveřejných sítí (NPN) využitím infrastruktury veřejného mobilního síťového operátora. Umožňuje vytváření vyhrazených, izolovaných síťových řez"
---

PNI-NPN je architektura 3GPP, která umožňuje neveřejné sítě (Non-Public Networks) využívající infrastrukturu veřejného operátora, poskytující vyhrazené, izolované síťové řezy pro podniky při využití stávajících aktiv operátora v rádiové přístupové síti a síti jádra.

## Popis

Public Network Integrated Non-Public Network (PNI-NPN) je standardizovaný model 3GPP pro nasazování neveřejných sítí (privátních sítí) využitím fyzické infrastruktury a kmitočtových zdrojů veřejného mobilního síťového operátora. Zavedený ve vydání 16 jako součást vylepšení 5G systému pro vertikální průmysly, je definován v komplexní sadě specifikací pokrývajících architekturu, procedury a správu. Základní koncept spočívá ve vytváření logicky izolovaných síťových řezů v rámci infrastruktury veřejné sítě pro obsluhu konkrétních podnikových zákazníků nebo vertikál, což jim poskytuje vyhrazené charakteristiky výkonu, zabezpečení a řízení typické pro privátní síť.

Architektonicky je PNI-NPN realizován prostřednictvím frameworku 5G síťového řezání. Síť jádra (5GC) a rádiová přístupová síť (RAN) veřejného síťového operátora jsou rozděleny za účelem vytvoření vyhrazených síťových řezů pro [NPN](/mobilnisite/slovnik/npn/). Tyto řezy zahrnují vyhrazené funkce síťového jádra (např. [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)) a mohou využívat vyhrazené rádiové zdroje nebo sdílené zdroje s kvalitou služby (QoS) zajišťující izolaci. Mezi klíčové komponenty patří informace pro podporu výběru síťového řezu ([NSSAI](/mobilnisite/slovnik/nssai/)) k identifikaci řezu, rozšířené mechanismy řízení přístupu pro omezení přístupu k NPN pouze na autorizovaná uživatelská zařízení (UE) a případně vyhrazený identifikátor sítě (PNI-NPN ID) pro její vyhledání. Architektura podporuje jak modely samostatných neveřejných sítí ([SNPN](/mobilnisite/slovnik/snpn/)), tak PNI-NPN, přičemž PNI-NPN konkrétně spoléhá na identifikátor [PLMN](/mobilnisite/slovnik/plmn/) veřejné sítě.

Z provozní perspektivy se UE připojuje k PNI-NPN navázáním spojení s buňkami veřejné sítě a následným směrováním do vyhrazeného řezu na základě předplatného a síťových politik. 5GC zajišťuje izolaci provozu mezi řezem PNI-NPN a ostatním provozem veřejné sítě. Správa a orchestrace řezu PNI-NPN jsou v režii veřejného síťového operátora, který často využívá rozhraní pro správu služeb zpřístupněná podnikovému zákazníkovi. To podniku umožňuje monitorovat a řídit aspekty svého vyhrazeného řezu, jako jsou politiky QoS nebo seznamy připojených zařízení, bez nutnosti spravovat podkladovou fyzickou infrastrukturu.

Model PNI-NPN funguje ve spojení s funkcemi jako je skupina s uzavřeným přístupem ([CAG](/mobilnisite/slovnik/cag/)) pro řízení přístupu na úrovni buňky, což zajišťuje, že pouze UE patřící konkrétnímu podniku mohou využívat určité rádiové zdroje. Integruje se také s mechanismy pro vyhledávání a výběr sítě, kde UE může identifikovat dostupné PNI-NPN. Úlohou PNI-NPN v síti je překlenout propast mezi plně privátními, samostatnými nasazeními a veřejným mobilním širokopásmovým připojením, což nabízí nákladově efektivní a škálovatelné řešení pro podnikové nasazení 5G díky využití stávajících investic operátorů a kmitočtových licencí.

## K čemu slouží

PNI-NPN byl vytvořen, aby reagoval na rostoucí poptávku průmyslových odvětví po privátních 5G sítích bez nutnosti pořizovat a spravovat vlastní licencované kmitočty a kompletní síťovou infrastrukturu. Před jeho standardizací měly podniky usilující o vyhrazený bezdrátový výkon omezené možnosti: nasadit Wi-Fi síť s jejími omezeními v mobilitě, spolehlivosti a determinismu, nebo investovat do nákladné samostatné privátní mobilní sítě. PNI-NPN tento problém řeší tím, že umožňuje veřejným síťovým operátorům nabízet 'privátní síť jako službu' za využití jejich stávajících aktiv.

Primární problém, který řeší, je poskytnout podnikům přizpůsobený výkon (ultraspolehlivá nízká latence, vysoká přenosová kapacita, hustota zařízení), zabezpečení a ochranu dat soukromé sítě, ale s provozní jednoduchostí a ekonomickými výhodami servisního modelu. Odstraňuje omezení předchozích přístupů využitím pokročilých schopností síťového řezání a QoS architektury 5G Standalone ([SA](/mobilnisite/slovnik/sa/)). To umožňuje provoz více izolovaných logických sítí na sdílené fyzické infrastruktuře, čímž se funkce privátních sítí stávají dostupnějšími pro širší spektrum malých a středních podniků.

Historicky vytvořil podnět pro tento model důraz vydání 16 na vertikály a průmyslový IoT. Motivovala jej potřeba otevřít trh 5G pro výrobu, logistiku, zdravotnictví a další sektory. PNI-NPN umožňuje operátorům monetizovat své investice do 5G nad rámec spotřebitelského širokopásmového připojení, zatímco podniky získávají budoucně bezpečné, standardizované a operátorské řešení pro své kritické komunikace, čímž se urychluje digitální transformace napříč průmyslovými odvětvími.

## Klíčové vlastnosti

- Logická izolace podnikového provozu prostřednictvím 5G síťového řezání
- Využití kmitočtů a infrastruktury RAN/CN veřejného síťového operátora
- Řízení přístupu pomocí mechanismů jako je skupina s uzavřeným přístupem (CAG)
- Podpora vyhrazených funkcí síťového jádra a politik QoS na řez
- Procedury pro vyhledávání a výběr sítě pro identifikaci PNI-NPN
- Rozhraní pro správu služeb pro samoobsluhu podnikového zákazníka

## Definující specifikace

- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 28.203** (Rel-18) — Charging management
- **TS 28.557** (Rel-19) — Management of Non-Public Networks (NPN)
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TR 28.807** (Rel-17) — Study on NPN Management
- **TR 28.828** (Rel-18) — Charging Aspects for Non-Public Networks
- **TR 28.907** (Rel-19) — Enhanced Management of Non-Public Networks
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.757** (Rel-19) — Security for PLMN Hosting Non-Public Network
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [PNI-NPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pni-npn/)
