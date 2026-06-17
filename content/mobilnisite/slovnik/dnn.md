---
slug: "dnn"
url: "/mobilnisite/slovnik/dnn/"
type: "slovnik"
title: "DNN – Data Network Name"
date: 2026-01-01
abbr: "DNN"
fullName: "Data Network Name"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dnn/"
summary: "Data Network Name identifikuje externí paketovou datovou síť, ke které se UE připojuje, například internet nebo službu IMS. Je to ekvivalent APN v systému 5G (5GS) a Evolved Packet System (EPS), použí"
---

DNN je identifikátor externí paketové datové sítě (např. internetu) v sítích 5G a 4G, používaný pro správu relací, řízení politik a účtování.

## Popis

Data Network Name (DNN) je základní identifikátor v systému 5G (5GS) a Evolved Packet System (EPS). Jedná se o řetězec (např. "internet", "ims"), který jednoznačně identifikuje paketovou datovou síť (PDN) nebo datovou síť ([DN](/mobilnisite/slovnik/dn/)) externí vůči síti 3GPP. Když UE zakládá relaci PDU (Protocol Data Unit) v 5GS nebo připojení PDN v EPS, musí specifikovat DNN. Tento DNN je klíčový parametr, který síť používá k výběru příslušné funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5GS nebo brány paketové datové sítě (PGW) v EPS, která zajišťuje připojení k této externí síti.

Z architektonického hlediska se DNN používá spolu s dalšími identifikátory, jako je informace pro pomocný výběr síťového řezu (S-NSSAI). Po přijetí žádosti o založení relace PDU s DNN funkce [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) interaguje s funkcí [SMF](/mobilnisite/slovnik/smf/) (Session Management Function). SMF použije DNN spolu s předplatitelskými daty z [UDM](/mobilnisite/slovnik/udm/) (Unified Data Management) a politikami z [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) k výběru konkrétní instance UPF. DNN určuje bod propojení s externí sítí a ovlivňuje charakteristiky QoS relace, účtovací politiky a bezpečnostní požadavky.

Role DNN přesahuje pouhý výběr brány. Je nedílnou součástí řízení politik a účtování. PCF může aplikovat různá pravidla řízení politik a účtování (PCC) na základě DNN. Například provoz určený pro DNN "internet" může mít jednu sadu pravidel QoS, zatímco provoz pro DNN spojený s podnikovým službou s nízkou latencí bude mít jinou. DNN se také používá při vystavování sítě; když funkce aplikace třetí strany ([AF](/mobilnisite/slovnik/af/)) požaduje specifické zacházení s provozem, často odkazuje právě na DNN. Dále je DNN kritickým parametrem pro síťové řezy, protože řez může být nakonfigurován tak, aby podporoval pouze specifické DNN, což umožňuje vytváření oddílů sítě pro konkrétní služby.

## K čemu slouží

DNN byl zaveden, aby plnil stejný základní účel jako Access Point Name ([APN](/mobilnisite/slovnik/apn/)) v dřívějších systémech, ale v rámci nové architektury založené na službách v 5GS. Řeší problém jednoznačné identifikace externí datové sítě, ke které má být relace uživatele připojena. To je základním požadavkem pro správné směrování provozu uživatelské roviny a aplikování odpovídajících síťových politik.

V kontextu podpory různorodých služeb v 5G (eMBB, URLLC, mMTC) poskytuje DNN síti jasný nástroj pro rozlišení typů služeb. Například UE může používat jeden DNN pro běžné prohlížení internetu a jiný DNN pro přístup k kritické službě průmyslového IoT, přestože obě relace mohou být obsluhovány stejným UE. To umožňuje současné připojení k více datovým sítím s nezávislým uplatňováním politik.

Vývoj z APN na DNN odráží architektonické zjednodušení a sladění s principy IP sítí. Zatímco APN mělo strukturu obsahující identifikátory sítě a operátora, DNN je přímočařejší označení. Jeho účel je hluboce integrován se základními principy 5G: síťovými řezy, kde může být DNN namapováno na konkrétní instanci řezu; architekturou založenou na službách, kde je DNN společným parametrem napříč rozhraními Nsmf, Npcf a dalšími rozhraními založenými na službách; a podporou edge computingu, kde DNN může odkazovat na lokální datovou síť (LADN). Řeší omezení staršího modelu APN tím, že je flexibilnější a lépe přizpůsobený pro automatizovanou správu a orchestraci v cloud-nativních jádrech 5G.

## Klíčové vlastnosti

- Jednoznačně identifikuje externí paketovou datovou síť (např. internet, IMS, podnikovou síť)
- Klíčový parametr pro založení relace PDU v 5GS a připojení PDN v EPS
- Používá se SMF (5GS) / MME (EPS) k výběru příslušné UPF / PGW
- Určuje bod propojení s externí datovou sítí (DN)
- Ovlivňuje pravidla řízení politik a účtování aplikovaná PCF
- Může být asociováno se specifickými síťovými řezy a lokacemi edge computingu (LADN)

## Definující specifikace

- **TR 22.874** (Rel-18) — Technical Report
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 24.575** (Rel-19) — UE Pre-configuration for MBS
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- … a dalších 39 specifikací

---

📖 **Anglický originál a plná specifikace:** [DNN na 3GPP Explorer](https://3gpp-explorer.com/glossary/dnn/)
