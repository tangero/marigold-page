---
slug: "gpu"
url: "/mobilnisite/slovnik/gpu/"
type: "slovnik"
title: "GPU – Graphics Processing Unit"
date: 2025-01-01
abbr: "GPU"
fullName: "Graphics Processing Unit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gpu/"
summary: "Specializovaný hardwarový procesor navržený pro paralelní výpočty, klíčový pro vykreslování grafiky a akceleraci multimediálních služeb v sítích 3GPP. V kontextu 3GPP umožňuje pokročilé služby jako cl"
---

GPU (Graphics Processing Unit) je specializovaný hardwarový procesor navržený pro paralelní výpočty, klíčový pro vykreslování grafiky a akceleraci multimediálních služeb, jako je cloud gaming a rozšířená realita, v sítích 3GPP.

## Popis

V rámci specifikací 3GPP není Graphics Processing Unit (GPU) síťovým protokolem, ale klíčovým hardwarovým prvkem, na který odkazují specifikace požadavků na služby. Jeho primární rolí je provádění masivně paralelních výpočtů potřebných pro vykreslování grafiky v reálném čase, zpracování videa a inferenci umělé inteligence. Tato výpočetní kapacita je zásadní pro poskytování pokročilých multimediálních služeb definovaných 3GPP, jako je cloud gaming a rozšířená realita (XR), kde jsou prvořadá nízká latence a vysoká propustnost. Specifikace (např. TS 22.874, TS 26.118) stanovují požadavky na služby, které implicitně nebo explicitně závisí na akceleraci GPU pro dosažení potřebné kvality uživatelského zážitku (QoE).

Z architektonického hlediska lze GPU nasadit na různých místech sítě v závislosti na modelu služby. Pro výpočetně náročné aplikace, jako je cloud gaming, jsou GPU typicky hostována v centralizovaných datových centrech nebo v uzlech multi-access edge computing ([MEC](/mobilnisite/slovnik/mec/)). Tento model vykreslování v cloudu/na okraji sítě přesouvá grafickou zátěž ze zařízení uživatele (UE), které může mít omezený výpočetní výkon a životnost baterie, na výkonné GPU na straně serveru. Vykreslené snímky videa jsou následně zakódovány a streamovány do UE přes síť 5G. Nízká latence a vysoká přenosová kapacita technologie 5G New Radio (NR) a core sítě jsou pro proveditelnost tohoto streamování zásadní, což vytváří symbiotický vztah mezi RAN a výpočetními zdroji GPU.

Integrace zdrojů GPU je řízena prostřednictvím aplikačních a servisních platforem vyšších vrstev, nikoliv jako přímá součást rádiových nebo core síťových protokolů 3GPP. Poskytovatelé služeb a vývojáři aplikací využívají [API](/mobilnisite/slovnik/api/) a platformy (které mohou být specifikovány ve spojení s prací 3GPP) k přidělení a správě zdrojů GPU pro danou relaci. Klíčové výkonnostní ukazatele těchto služeb, jako je latence od pohybu k zobrazení (motion-to-photon) a snímková frekvence, jsou přímo svázány s rychlostí zpracování GPU, šířkou pásma paměti a efektivitou kódovacího/streamovacího řetězce. Proto, přestože je GPU samo o sobě hardwarovou komponentou, jeho schopnosti a umístění jsou nedílnou součástí systémového návrhu pro dosažení cílů 3GPP na úrovni služeb pro imerzivní média.

## K čemu slouží

Zahrnutí aspektů GPU do specifikací 3GPP reaguje na rostoucí poptávku po výpočetně náročných, imerzivních službách, které nelze dostatečně podporovat tradičním zpracováním centrickým vůči UE. Účelem je definovat požadavky na služby a cíle kvality pro aplikace jako cloud gaming, virtuální realita (VR) a rozšířená realita ([AR](/mobilnisite/slovnik/ar/)), které jsou závislé na externalizovaném, výkonném grafickém zpracování. Historicky byly tyto aplikace omezeny tepelnými, energetickými a cenovými limity mobilních zařízení, což vedlo ke špatnému uživatelskému zážitku nebo omezené dostupnosti.

Práce 3GPP ve vydáních jako Rel-15 a novějších uznala, že sítě příští generace musí podporovat více než jen konektivitu; musí umožňovat nový ekosystém služeb náročných na výpočty. Specifikací výkonnostních požadavků (např. latence, datového toku, spolehlivosti) pro služby závislé na akceleraci GPU stanovuje 3GPP cíl pro síťové operátory a poskytovatele cloudových služeb při návrhu jejich infrastruktury. To motivuje konvergenci telekomunikací a cloud computingu a posouvá výpočetní zdroje blíže k uživateli prostřednictvím edge computingu, aby byly splněny přísné požadavky na latenci. GPU je tedy klíčovým prvkem při přechodu mobilních sítí z pouhých datových přenosů na platformy pro distribuované vysoce výkonné výpočty.

## Klíčové vlastnosti

- Masivně paralelní výpočetní architektura optimalizovaná pro grafické a vektorové výpočty
- Umožňuje modely vykreslování v cloudu/na okraji sítě, které odlehčují zátěž zařízení uživatele
- Klíčové pro dosažení nízké latence od pohybu k zobrazení (motion-to-photon) v imerzivních službách XR
- Podporuje vysoce efektivní video kodeky (HEVC, VVC) pro streamování vykresleného obsahu
- Integruje se s platformami Multi-access Edge Computing (MEC) pro síťově optimalizované přidělování zdrojů
- Umožňuje pokročilé zpracování médií, jako je skládání 360stupňového videa a volumetrické kódování

## Definující specifikace

- **TR 22.874** (Rel-18) — Technical Report
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [GPU na 3GPP Explorer](https://3gpp-explorer.com/glossary/gpu/)
