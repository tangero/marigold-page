---
slug: "hmd"
url: "/mobilnisite/slovnik/hmd/"
type: "slovnik"
title: "HMD – Head Mounted Display"
date: 2025-01-01
abbr: "HMD"
fullName: "Head Mounted Display"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hmd/"
summary: "Head Mounted Display (HMD) je nositelné zařízení zobrazující vizuální média, často pro virtuální realitu (VR) nebo rozšířenou realitu (AR). Specifikace 3GPP řeší specifické požadavky HMD pro doručován"
---

HMD je nositelné zařízení pro vizuální média, jako je VR nebo AR, které má specifické požadavky 3GPP pro doručování přes mobilní sítě, včetně streamování s nízkou latencí a energetické účinnosti.

## Popis

Ve specifikacích 3GPP termín Head Mounted Display (HMD) označuje kategorii uživatelského zařízení a související servisní požadavky pro doručování imerzivních mediálních zážitků, jako je virtuální realita (VR), rozšířená realita ([AR](/mobilnisite/slovnik/ar/)) a rozšířená realita (XR), přes buněčné sítě. Je pokryt v řadě technických specifikací (např. TS 26.114, 26.118, 38.835), které definují kodeky, transportní protokoly, systémové architektury a výkonnostní metriky přizpůsobené pro HMD. HMD je nositelné zařízení s jedním nebo dvěma vysokorozlišovacími displeji umístěnými blízko očí uživatele, často vybavené senzory pro sledování polohy hlavy.

Z pohledu síťové architektury podpora HMD zahrnuje vylepšení na servisní vrstvě, v jádru sítě a v rádiové přístupové síti. Klíčové komponenty zahrnují aplikační server médií (např. pro 360stupňové video), 5G Core Network s podporou edge computingu ([MEC](/mobilnisite/slovnik/mec/)) a Radio Access Network (RAN) schopnou poskytovat vysokou propustnost a ultra-spolehlivou komunikaci s nízkou latencí (URLLC). Doručování médií často využívá Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) nebo podobné protokoly rozšířené o funkce jako viewport-dependent streaming, kde je v vysoké kvalitě doručována pouze ta část 360stupňového videa, která je aktuálně v zorném poli uživatele, čímž se šetří šířka pásma.

Fungování spočívá v těsné interakci mezi zařízením HMD, sítí a mediálním serverem. Senzory HMD nepřetržitě hlásí orientaci hlavy. Tato data jsou odesílána na aplikační server, často přes nízkolatenční spojení usnadněné zpracováním na síťovém okraji. Server následně přizpůsobuje video stream v reálném čase, načítá a doručuje vysoce kvalitní segmenty pro aktuální viewport uživatele, zatímco pro periferii doručuje nižší kvalitu. Síť musí garantovat potřebnou šířku pásma, latenci (často pod 20 ms pro motion-to-photon) a spolehlivost, aby se předešlo nevolnosti z pohybu a zajistila imerze. Úlohou 3GPP je standardizovat rozhraní, profily kodeků (jako pro video-based point clouds), mechanismy QoS a schopnosti zařízení, aby byl tento ekosystém interoperabilní a škálovatelný.

## K čemu slouží

Formalizace požadavků na Head Mounted Display (HMD) v rámci 3GPP byla hnací silou rychlého nástupu imerzivních médií jako klíčového případu užití pro sítě 5G a následující. Před tímto zaměřením byly mobilní sítě optimalizovány pro tradiční streamování videa na smartphony, které mají odlišná omezení týkající se latence, zorného pole a interakce. Rané systémy VR/[AR](/mobilnisite/slovnik/ar/) byly připoutány k výkonným PC nebo používaly offline obsah, což výrazně omezovalo mobilitu a masové přijetí.

Omezení sítí před 5G pro HMD zahrnovala nedostatečné špičkové datové rychlosti pro vysokorozlišovací 360stupňové video, vysokou latenci způsobující nevolnost z pohybu a nedostatek standardizovaných metod pro viewport-adaptive streaming vedoucí k neefektivnímu využití šířky pásma. 3GPP je začala řešit ve vydání 14 a významně je rozšířila v pozdějších vydáních, aby tyto problémy vyřešila. Účelem je umožnit kvalitní, bezdrátový a mobilní XR zážitek, což vyžaduje řešení jedinečných technických výzev kolem ultra-vysoké propustnosti, velmi nízké end-to-end latence a energeticky účinného provozu zařízení.

K jeho vytvoření motivovala vize XR jako transformační služby pro zábavu, vzdělávání, průmysl a sociální interakci. Standardizace podpory HMD zajišťuje, že poskytovatelé obsahu, výrobci zařízení a síťoví operátoři mají společný technický základ. To urychluje inovace, zajišťuje interoperabilitu a umožňuje úspory z rozsahu potřebné k uvedení imerzivních bezdrátových zážitků ke spotřebitelům a podnikům, naplňující tak klíčové výkonnostní sliby 5G.

## Klíčové vlastnosti

- Podpora viewport-adaptive streamingu 360stupňového a imerzivního videa
- Standardizované mediální formáty a kodeky pro 3D grafiku a point clouds (např. V-PCC)
- Síťové požadavky na nízkou latenci (URLLC) a vysokou propustnost (eMBB) pro XR provoz
- Požadavky na energetickou účinnost a modely pro nositelná zařízení HMD
- Integrace s funkcemi 5G System jako Network Slicing a Mobile Edge Computing (MEC)
- Definované metriky a reportování Quality of Experience (QoE) pro imerzivní služby

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.238** (Rel-19) — Framework for Live Uplink Streaming (FLUS)
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.865** (Rel-18) — Technical Report
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.929** (Rel-19) — QoE Metrics for VR Services Study
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [HMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hmd/)
