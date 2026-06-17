---
slug: "mrfp"
url: "/mobilnisite/slovnik/mrfp/"
type: "slovnik"
title: "MRFP – Multimedia Resource Function Processor"
date: 2025-01-01
abbr: "MRFP"
fullName: "Multimedia Resource Function Processor"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mrfp/"
summary: "MRFP je komponenta přenosové roviny (media plane) funkce IMS Media Resource Function (MRF), která fyzicky zpracovává multimediální datové toky pod řízením MRFC. Zpracovává funkce v reálném čase, jako"
---

MRFP je mediální procesní komponenta sítě IMS, která pod řízením MRFC vykonává funkce v reálném čase, jako je mixování zvuku/videa, překódování a přehrávání médií.

## Popis

Multimedia Resource Function Processor (MRFP) je entita uživatelské roviny (user plane) neboli mediálního zpracování uvnitř funkce IMS Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)). Je zodpovědná za skutečnou manipulaci a zpracování mediálních toků v reálném čase, včetně zvuku, videa a textu v reálném čase. Při provozu pod přísným řízením Multimedia Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)) vykonává MRFP mediálně související operace prostřednictvím rozhraní Mp, které je založeno na protokolu H.248 (Megaco). MRFP obsahuje fyzické nebo virtualizované zdroje – jako jsou digitální signálové procesory ([DSP](/mobilnisite/slovnik/dsp/)), procesory pro obecné účely a specializovaný hardware – které provádějí výpočetně náročné úlohy, jako je mixování více mediálních toků do konference, překódování mezi různými kodeky (např. z [AMR](/mobilnisite/slovnik/amr/) na G.711), přehrávání předem nahraných hlášení a detekce vícefrekvenčních ([DTMF](/mobilnisite/slovnik/dtmf/)) signálů.

Z architektonického hlediska je MRFP podřízená komponenta, která přijímá pokyny od MRFC. MRFC používá příkazy H.248 k vytváření 'kontextů' uvnitř MRFP, což jsou logické kontejnery pro mediální relace. V rámci těchto kontextů MRFC přidává 'terminace', které představují koncové body pro mediální toky. MRFP pak tyto terminace propojuje a aplikuje specifikované 'balíčky' funkcí pro zpracování médií. Například v třístranné audio konferenci by MRFP vytvořil kontext se třemi terminacemi (jedna pro každého účastníka), aplikoval mixovací funkci, která kombinuje audio od všech stran, a poslal smíšený tok zpět do každé terminace. MRFP je z pohledu servisní logiky bezstavový; veškerá inteligence a stav relace sídlí v MRFC.

V praktickém provozu, když služba vyžaduje zpracování médií, MRFC nařídí MRFP, aby alokoval potřebné porty a výpočetní výkon. MRFP podle pokynů naváže spojení na úrovni přenosu (přes RTP/UDP/IP) s uživatelským zařízením (UE) nebo jinými síťovými koncovými body. Poté kontinuálně zpracovává příchozí mediální pakety v reálném čase, provádí nařízené funkce a přeposílá výsledné toky. MRFP také generuje hlášení a oznámení (např. 'detekována DTMF číslice 1') zpět do MRFC prostřednictvím H.248, což umožňuje řídicí rovině reagovat na mediální události. Tento návrh umožňuje zpracování médií s vysokou propustností a nízkou latencí, které je zcela oddělené od složitosti signalizace a servisní logiky.

## K čemu slouží

MRFP byl vyvinut, aby poskytoval standardizovanou, vysoce výkonnou platformu pro zpracování médií pro služby založené na IMS, oddělující náročný úkol manipulace s médii v reálném čase od signalizačních řídicích funkcí. Před jeho definicí bylo zpracování médií často integrováno do monolitických ústředen nebo proprietárních serverových platforem, což vedlo k závislosti na dodavateli, neefektivnímu využití zdrojů a obtížím při škálování mediální kapacity nezávisle na řídicí inteligenci. MRFP jako protějšek přenosové roviny k [MRFC](/mobilnisite/slovnik/mrfc/) řeší tyto problémy tím, že nabízí vyhrazený, říditelný fond zdrojů pro mediální funkce.

Jeho vytvoření bylo zásadní pro umožnění komerčního nasazení pokročilých, v síti hostovaných multimediálních služeb. Služby jako audio/video konference, multimediální vyzváněcí tóny a interaktivní hlasové systémy vyžadují konzistentní, spolehlivé a kvalitní zpracování médií, které lze škálovat pro obsluhu milionů účastníků. MRFP tuto schopnost poskytuje síťově centrickým způsobem, odlehčuje složité zpracování od koncových uživatelských zařízení a zajišťuje jednotnost služeb. Standardizací řídicího rozhraní H.248 umožnila 3GPP operátorům nasazovat MRFP od různých dodavatelů než jejich MRFC, což podpořilo konkurenci, inovace v hardwaru/softwaru pro zpracování médií a nákladově efektivní škálování mediálních zdrojů pro uspokojení rostoucích požadavků na provoz.

## Klíčové vlastnosti

- Vykonává zpracování médií v reálném čase (mixování, překódování, přehrávání) pod řízením MRFC
- Implementuje část přenosové (uživatelské) roviny MRF pomocí protokolu H.248 (rozhraní Mp)
- Poskytuje zdroje pro audio/video konference, přehrávání hlášení a zpracování tónů
- Zpracovává přenosová spojení (RTP/RTCP) s uživatelskými zařízeními (UE) a dalšími síťovými koncovými body
- Podporuje konverzi kodeků (překódování) a adaptaci (změnu přenosové rychlosti) mezi různými mediálními formáty
- Generuje hlášení o mediálních událostech (např. detekce DTMF) zpět do MRFC pro servisní logiku

## Související pojmy

- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)

## Definující specifikace

- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- … a dalších 31 specifikací

---

📖 **Anglický originál a plná specifikace:** [MRFP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrfp/)
