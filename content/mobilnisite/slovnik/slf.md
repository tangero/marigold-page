---
slug: "slf"
url: "/mobilnisite/slovnik/slf/"
type: "slovnik"
title: "SLF – Subscription Location Function"
date: 2025-01-01
abbr: "SLF"
fullName: "Subscription Location Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/slf/"
summary: "Funkce jádra sítě v IMS a 5G, která vyhledá příslušný HSS nebo UDM pro daného účastníka. Je klíčová pro směrování dotazů ke správnému úložišti uživatelských dat v sítích s více dodavateli nebo geograf"
---

SLF je funkce jádra sítě v IMS a 5G, která vyhledá příslušný HSS nebo UDM pro daného účastníka, aby dotazy směrovaly ke správnému úložišti uživatelských dat.

## Popis

Subscription Location Function (SLF) je klíčová součást architektur IP Multimedia Subsystem (IMS) a 5G Core (5GC), konkrétně navržená k určení, která instance Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) uchovává předplatitelská data daného uživatele. Funguje jako jednoduchý mechanismus dotaz-odpověď. Když IMS Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) nebo 5G Network Function ([NF](/mobilnisite/slovnik/nf/)), jako je Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)), potřebuje přístup k datům účastníka, ale nezná konkrétní instanci HSS/UDM, odešle dotaz na SLF pomocí protokolu Diameter nebo [HTTP](/mobilnisite/slovnik/http/). Tento dotaz obsahuje identifikátor uživatele, například IMS Private User Identity ([IMPI](/mobilnisite/slovnik/impi/)) nebo Subscription Permanent Identifier ([SUPI](/mobilnisite/slovnik/supi/)). SLF pomocí nakonfigurované mapovací databáze nebo algoritmu vrátí adresu (např. hostname, IP adresu) HSS nebo UDM, která daného účastníka obsluhuje. Tento proces je pro koncového uživatele transparentní a je základním prvkem správy předplatitelských dat v prostředích s více HSS/UDM.

Architektonicky je SLF definována jako samostatná logická funkce, ale pro jednoduchost v menších nasazeních může být umístěna společně s HSS. V čisté 5G Core síti je funkčnost SLF integrována do UDM interně prostřednictvím mechanismů objevování UDR (Unified Data Repository), takže samostatná SLF je méně častá. V IMS a během scénářů propojování mezi 4G EPC a 5GC však SLF zůstává klíčovou entitou. Jejím primárním rozhraním je rozhraní Dx (založené na protokolu Diameter) směrem k I-CSCF a S-CSCF v IMS a rozhraní N10/N11 (založená na HTTP/2) v 5G Service-Based Architecture (SBA) při interakci s UDM.

Role SLF je čistě vyhledávací a sama neukládá skutečná data profilu účastníka. Toto oddělení odpovědností umožňuje flexibilní škálování sítě. Operátoři mohou nasadit více instancí HSS/UDM pro obsluhu velkého počtu účastníků nebo pro redundanci, přičemž SLF poskytuje potřebnou vrstvu nepřímého odkazování. Podporuje vyvažování zátěže a geografické rozložení uživatelských dat. Například účastníci v různých regionech mohou být přiřazeni k různým instancím HSS a SLF zajišťuje, že dotazy ze sítě jsou vždy směrovány ke správné regionální databázi. Tato schopnost je klíčová pro udržení přístupu k datům účastníka s nízkou latencí a pro implementaci schémat zotavení po havárii, kde jsou uživatelská data replikována napříč lokalitami.

## K čemu slouží

SLF byla zavedena k vyřešení zásadního problému škálování v raných nasazeních IMS. Jak sítě rostly nad rámec jediného HSS, neexistoval standardní mechanismus, jak síťové funkce určily, která instance HSS obsahuje data konkrétního uživatele. Bez SLF by síťové prvky potřebovaly předem nakonfigurovaná statická mapování nebo by musely vysílat dotazy na všechny instance HSS, což je neefektivní a neškálovatelné. SLF poskytuje centralizovanou, standardizovanou vyhledávací službu, která umožňuje nasazení více nezávislých databází HSS. To operátorům umožňuje horizontálně škálovat kapacitu pro účastníky přidáváním dalších uzlů HSS bez nutnosti rekonfigurace každého CSCF v síti.

Její vytvoření bylo motivováno přechodem k distribuovaným, carrier-grade architekturám. V jádrech 2G/3G s přepojováním okruhů byl HLR (Home Location Register) typicky monolitická, centralizovaná databáze. IMS, navržená pro IP-based multimediální služby, vyžadovala flexibilnější a škálovatelnější přístup. SLF to umožnila oddělením logiky vyhledání účastníka od servisní logiky v CSCFs. Tento návrhový princip pokračoval i v 5G, kde je koncept vestavěn do service-based architektury UDM. SLF řeší omezení monolitických databází tím, že umožňuje bezestavovým, škálovatelným řídicím rovinám funkcím (jako jsou CSCFs) dynamicky lokalizovat stavová datová úložiště, což je základním kamenem cloud-native návrhu sítí.

## Klíčové vlastnosti

- Poskytuje standardizovaný dotazovací mechanismus pro vyhledání HSS nebo UDM pro daný identifikátor účastníka.
- Umožňuje horizontální škálování předplatitelských databází podporou více instancí HSS/UDM.
- Podporuje jak Diameter (rozhraní Dx) pro IMS, tak HTTP/2 (N10/N11) pro 5G Service-Based Architecture.
- Umožňuje geografické rozložení a redundanci úložišť uživatelských dat.
- Funguje jako bezestavová vyhledávací funkce, která neukládá skutečná data profilu účastníka.
- Klíčová pro procedury registrace v IMS a navazování relací.

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 29.228** (Rel-19) — Cx and Dx Interface Signaling Flows
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [SLF na 3GPP Explorer](https://3gpp-explorer.com/glossary/slf/)
