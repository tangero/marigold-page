---
slug: "tl"
url: "/mobilnisite/slovnik/tl/"
type: "slovnik"
title: "TL – Transfer Learning"
date: 2025-01-01
abbr: "TL"
fullName: "Transfer Learning"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tl/"
summary: "Transfer Learning (TL, přenos učení) v 3GPP označuje techniky pro efektivní adaptaci předtrénovaných modelů strojového učení na nové úlohy nebo prostředí v bezdrátových sítích. Snižuje množství trénin"
---

TL je technika pro efektivní adaptaci předtrénovaných modelů strojového učení na nové úlohy nebo prostředí v bezdrátových sítích za účelem snížení potřebných tréninkových dat a výpočetních zdrojů.

## Popis

Transfer Learning (TL, přenos učení) je paradigma strojového učení standardizované v rámci 3GPP za účelem zvýšení efektivity a adaptibility modelů [AI/ML](/mobilnisite/slovnik/ai-ml/) v bezdrátových sítích. Spočívá ve využití znalostí získaných ze zdrojové úlohy nebo domény (kde jsou dostupná bohatá data) ke zlepšení učení v příbuzné, ale odlišné cílové úloze nebo doméně (kde mohou být data vzácná). V architekturách 3GPP se TL uplatňuje uvnitř síťových funkcí, zejména v rádiové přístupové síti (RAN) a v core síti, pro optimalizaci výkonu, správu zdrojů a personalizaci služeb. Klíčové komponenty zahrnují repozitář ML modelů, tréninkové datové sady ze zdrojových domén a adaptační mechanismy, které doladí modely pro cílové scénáře. Protokoly a rozhraní, jako jsou definované v 29.244 a 29.482, usnadňují výměnu informací o modelech a tréninkových dat mezi síťovými entitami, jako je RAN Intelligent Controller (RIC) a funkce core sítě.

Operačně TL funguje tak, že inicializuje model pro novou úlohu parametry předtrénovanými na podobné, daty bohaté úloze, namísto začátku od náhodné inicializace. Například model trénovaný pro predikci mobility v městském prostředí může být adaptován pro venkovské prostředí s minimálním dodatečným tréninkem. Tento proces zahrnuje extrakci příznaků, kde nižší vrstvy neuronových sítí zachycují obecné vzorce, a doladění, kde jsou vyšší vrstvy upraveny na specifická cílová data. V systémech 3GPP může být TL implementována centralizovaně, distribuovaně nebo federovaně, v závislosti na případu užití. Interaguje se systémy správy sítě za účelem sběru metrik výkonu, periodického přetrénování modelů a nasazení aktualizovaných modelů napříč síťovými uzly, což zajišťuje kontinuální optimalizaci bez rozsáhlého přetrénování od nuly.

Úloha TL v sítích 3GPP spočívá v umožnění rychlého nasazení aplikací řízených [AI](/mobilnisite/slovnik/ai/)/[ML](/mobilnisite/slovnik/ml/), jako je správa beamů, vyvažování zátěže, úspora energie a predikce kvality uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)), díky snížení času a dat potřebných pro trénink modelů. Řeší výzvy jako nestacionární bezdrátová prostředí a různorodé scénáře nasazení tím, že umožňuje modelům se dynamicky adaptovat. Standardizací frameworků TL zajišťuje 3GPP interoperabilitu mezi dodavateli a konzistenci v implementacích AI/ML, čímž připravuje cestu pro autonomnější a inteligentnější sítě v systémech 5G-Advanced a budoucích 6G.

## K čemu slouží

TL byla zavedena v 3GPP za účelem překonání omezení tradičních přístupů strojového učení v bezdrátových sítích, které často vyžadují velké, označené datové sady a značné výpočetní zdroje pro každou novou úlohu nebo prostředí. Jak se sítě s příchodem 5G-Advanced a 6G stávají složitějšími, nasazování [AI/ML](/mobilnisite/slovnik/ai-ml/) pro optimalizaci – například v oblasti správy rádiových prostředků nebo síťového slicing – čelí výzvám kvůli nedostatku dat, vysokým nákladům na trénink a pomalé adaptaci na měnící se podmínky. TL tyto problémy řeší opětovným využitím již existujících znalostí, což umožňuje rychlejší a efektivnější trénink modelů s menším množstvím dat, což je klíčové pro provoz sítě v reálném čase.

Historický kontext zahrnuje rostoucí integraci [AI](/mobilnisite/slovnik/ai/)/[ML](/mobilnisite/slovnik/ml/) do standardů 3GPP za účelem zvýšení automatizace a výkonu sítě. Předchozí metody spoléhaly na modely šité na míru pro každý scénář, což vedlo k neefektivitám a problémům se škálovatelností. TL motivuje své zavedení tím, že poskytuje standardizovaný způsob přenosu naučených příznaků napříč podobnými doménami, čímž snižuje potřebu rozsáhlého sběru dat a přetrénování. Toto urychluje inovace, snižuje provozní náklady a zlepšuje agilitu sítě, podporujíc případy užití jako prediktivní údržba, personalizované služby a dynamická alokace zdrojů v heterogenních prostředích.

## Klíčové vlastnosti

- Přenos znalostí ze zdrojových do cílových domén pro efektivní trénink ML
- Snížení potřebných tréninkových dat a výpočetních zdrojů
- Podpora doladění a adaptace předtrénovaných modelů
- Integrace se síťovými funkcemi 3GPP jako RIC a core NWDAF
- Standardizované protokoly pro výměnu a správu modelů
- Aplikace na případy užití jako správa rádiových prostředků a predikce QoE

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.482** (Rel-19) — SEAL AIMLE Services Stage 3 Protocol
- **TS 29.585** (Rel-19) — TSN Interworking Protocol for 5G System

---

📖 **Anglický originál a plná specifikace:** [TL na 3GPP Explorer](https://3gpp-explorer.com/glossary/tl/)
