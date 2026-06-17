---
slug: "cn"
url: "/mobilnisite/slovnik/cn/"
type: "slovnik"
title: "CN – Core Network"
date: 2026-01-01
abbr: "CN"
fullName: "Core Network"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cn/"
summary: "Jádrová síť (CN) je centrální, neradiová část mobilní sítě 3GPP, zodpovědná za autentizaci, správu relací, mobilitu a propojení s externími sítěmi, jako je internet. Poskytuje inteligenci a řídicí fun"
---

CN (Core Network, jádrová síť) je centrální, neradiová část mobilní sítě 3GPP, která poskytuje inteligenci, řízení a konektivitu pro uživatelské služby, zajišťuje autentizaci, správu mobility a propojení s externími sítěmi.

## Popis

Jádrová síť (CN) představuje centrální přepínací a řídicí infrastrukturu mobilní sítě 3GPP, odlišnou od rádiové přístupové sítě (RAN). Je zodpovědná za celkové řízení, správu a směrování uživatelských dat a signalizačního provozu. CN autentizuje účastníky, spravuje jejich relace (navázání, změna, ukončení), zajišťuje správu mobility (sledování a předávání spojení mezi různými oblastmi) a poskytuje konektivitu k externím paketovým datovým sítím (PDN), jako je internet nebo privátní firemní sítě. Slouží jako kotvící bod pro uživatelské služby, zajišťuje kontinuitu a kvalitu služeb v celé síti.

Z architektonického hlediska se CN výrazně vyvinula. Ve sítích 2G/3G (GSM/UMTS) byla rozdělena na okruhově přepínanou ([CS](/mobilnisite/slovnik/cs/)) doménu pro hlas a paketově přepínanou (PS) doménu pro data, s klíčovými uzly jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN). Se zavedením IP Multimedia Subsystem (IMS) a System Architecture Evolution (SAE) pro 4G LTE došlo k přechodu na plně IP, plochou architekturu. Evolved Packet Core (EPC) pro 4G a 5G Core (5GC) jsou čistě paketově orientované a oddělují funkce řídicí roviny ([CP](/mobilnisite/slovnik/cp/)) a uživatelské roviny (UP). Mezi klíčové komponenty patří Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway (SGW), Packet Data Network Gateway (PGW) v EPC a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC.

CN rozhraní s RAN (např. přes rozhraní S1, N2, N3), s dalšími uzly CN a s externími sítěmi. Provádí kritické procedury jako Attach, Tracking Area Update, PDU Session Establishment a Handover. Také vynucuje politiky a řízení účtování (PCC), spravuje data účastníků v Home Subscriber Server (HSS) nebo Unified Data Management (UDM) a poskytuje možnosti zákonného odposlechu. V 5G je CN navržena podle cloud-nativních principů s využitím služebně orientované architektury (SBA), kde síťové funkce komunikují přes API založená na HTTP/2, což umožňuje síťové slicing, edge computing a vyšší míru automatizace.

## K čemu slouží

Jádrová síť existuje proto, aby poskytovala centralizovanou inteligenci, řízení a přepínací strukturu pro mobilní síť, odděluje tyto funkce od rádiově specifické přístupové vrstvy. Jejím hlavním účelem je umožnit spolehlivé, bezpečné a funkčně bohaté mobilní služby pro účastníky. Řeší základní problémy uživatelské autentizace, správy relací a mobility, poskytování služeb a propojení s jinými sítěmi (pevnými i mobilními). Bez CN by RAN byla pouze souborem izolovaných základnových stanic bez schopnosti směrovat hovory, spravovat uživatelskou identitu nebo poskytovat nepřetržitou službu při pohybu uživatelů.

Historicky se CN vyvinula z telefony orientovaných okruhově přepínaných sítí pro hlas ve 2G na podporu paketových dat ve 2.5G/3G, což vedlo k architektuře s dvojí doménou. Omezení tohoto přístupu – složitost, neefektivita pro IP provoz a obtížnost zavádění nových služeb – motivovala přechod na plně IP, plošší architekturu s 4G EPC a 5G 5GC. Vznik moderní CN byl hnán potřebou vyšší datové propustnosti, nižší latence, podpory obrovského počtu různorodých zařízení (IoT) a flexibility pro rychlé nasazování nových služeb prostřednictvím virtualizace a softwarizace sítě.

## Klíčové vlastnosti

- Autentizace a autorizace účastníků (prostřednictvím HSS/UDM)
- Správa relací (navázání, změna, ukončení datových relací)
- Správa mobility (sledování, registrace, podpora předávání spojení)
- Vynucování politik a řízení účtování (PCC)
- Propojení s externími paketovými datovými sítěmi (PDN)
- Podpora síťového slicingu a edge computingu (5GC)

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.468** (Rel-19) — Group Communication System Enabler Requirements
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 22.801** (Rel-12) — Study on Non-MTC Mobile Data Application Impacts
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- … a dalších 143 specifikací

---

📖 **Anglický originál a plná specifikace:** [CN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cn/)
