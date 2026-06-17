---
slug: "gan"
url: "/mobilnisite/slovnik/gan/"
type: "slovnik"
title: "GAN – Generative Adversarial Network"
date: 2025-01-01
abbr: "GAN"
fullName: "Generative Adversarial Network"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gan/"
summary: "GAN (Generativní adversariální síť) v kontextu 3GPP označuje techniky AI/ML pro optimalizaci sítě, ačkoli se nejedná o základní telekomunikační standard. Tyto neuronové sítě generují syntetická data a"
---

GAN je technika umělé inteligence/strojového učení využívající neuronové sítě, které generují syntetická data a modely pro trénink, testování a vylepšování síťových funkcí, jako je odhad kanálu a predikce provozu v systémech 5G/6G.

## Popis

V kontextu 3GPP představují generativní adversariální sítě (GAN) třídu technik umělé inteligence a strojového učení aplikovaných na různé problémy optimalizace telekomunikací, ačkoli samy o sobě nejsou základním síťovým standardem. GAN se skládají ze dvou neuronových sítí – generátoru a diskriminátoru – které jsou trénovány současně prostřednictvím adversariálního procesu. Generátor vytváří syntetické datové vzorky napodobující reálná síťová data, zatímco diskriminátor tyto vzorky vyhodnocuje proti autentickým datům, čímž vzniká konkurenční zpětnovazební smyčka, která v průběhu času zlepšuje schopnosti obou sítí. Tato architektura umožňuje vytváření vysoce realistických syntetických datových sad a modelů, které lze použít pro řadu úloh optimalizace sítě bez nutnosti rozsáhlého sběru dat z reálného světa.

Technická implementace GAN v systémech 3GPP zahrnuje integraci těchto modelů [AI/ML](/mobilnisite/slovnik/ai-ml/) do různých síťových funkcí a systémů řízení. Generátorová síť typicky přijímá jako vstup náhodný šum nebo částečná pozorování a produkuje syntetické výstupy, jako jsou informace o stavu kanálu, vzorce síťového provozu, trajektorie mobility uživatelů nebo mapy rádiového prostředí. Diskriminační síť, trénovaná na reálných síťových měřeních, se učí rozlišovat mezi autentickými a generovanými daty. Prostřednictvím iterativního tréninku se generátor stává stále zručnějším ve vytváření realistických syntetických dat, která mohou oklamat diskriminátor, zatímco diskriminátor se zlepšuje v detekci nedokonalostí. Tento proces pokračuje, dokud není dosaženo rovnováhy, což vede ke generátoru schopnému produkovat vysoce kvalitní syntetická data nerozlišitelná od reálných měření.

V praktickém nasazení v architekturách 3GPP lze GAN implementovat na různých místech sítě v závislosti na aplikaci. Pro optimalizaci rádiové přístupové sítě mohou GAN běžet na distribuovaných jednotkách ([DU](/mobilnisite/slovnik/du/)) nebo centralizovaných jednotkách ([CU](/mobilnisite/slovnik/cu/)) za účelem generování syntetických modelů kanálu pro trénink beamformingu nebo predikce vzorců interference. V jádru sítě mohou GAN fungovat v rámci funkcí síťové datové analytiky (NWDAF) pro vytváření syntetických profilů provozu pro plánování kapacity nebo detekci anomálií. Technologie funguje tak, že se průběžně učí z reálných síťových dat, přičemž generuje doplňková syntetická data, která rozšiřují tréninkové datové sady, zlepšují robustnost modelů a umožňují testování vzácných scénářů, které se v reálném provozu nemusí často vyskytovat. Role GAN v systémech 3GPP je zvláště cenná pro řešení problémů nedostatku dat, ochranu soukromí uživatelů prostřednictvím generování syntetických dat a umožnění komplexnějšího testování a optimalizace, než by bylo možné pouze s omezenými daty z reálného světa.

## K čemu slouží

Technologie GAN byla do standardů 3GPP začleněna, aby řešila několik nových výzev v moderních telekomunikačních sítích, zejména s příchodem 5G a postupem směrem k 6G. Primární motivací bylo využít pokročilé techniky [AI/ML](/mobilnisite/slovnik/ai-ml/) pro optimalizaci, automatizaci a inteligenci sítě bez omezení tradičních datově řízených přístupů. Jelikož se sítě stávají složitějšími s funkcemi jako massive [MIMO](/mobilnisite/slovnik/mimo/), síťové slicing a ultra-hustá nasazení, konvenční optimalizační metody nedokážou zvládnout dimenzionalitu a dynamiku problémového prostoru.

Klíčové problémy, které GAN pomáhají řešit, zahrnují nedostatek dat pro trénink modelů [AI](/mobilnisite/slovnik/ai/), obavy o soukromí při používání reálných uživatelských dat a potřebu testovat chování sítě za vzácných nebo extrémních podmínek. V mnoha scénářích optimalizace sítě je sběr dostatečného množství reálných dat nepraktický kvůli nákladům, času nebo omezením soukromí. GAN umožňují generování realistických syntetických dat, která zachovávají statistické vlastnosti reálných dat, ale neobsahují žádné skutečné uživatelské informace. Tato syntetická data pak lze použít k tréninku dalších modelů AI pro úlohy jako predikce kanálu, předpověď provozu nebo detekce anomálií. Navíc GAN umožňují síťovým operátorům simulovat okrajové případy a scénáře selhání, které se v produkčních sítích vyskytují zřídka, ale jsou klíčové pro pochopení při plánování robustnosti a odolnosti.

Historicky se GAN dostaly do diskuse 3GPP kolem Release 15 jako součást širší studijní položky AI/[ML](/mobilnisite/slovnik/ml/) pro NG-RAN a získaly větší význam v následujících releasech, když průmysl rozpoznal jejich potenciál pro řešení optimalizačních výzev 5G. Technologie řeší omezení předchozích přístupů, které spoléhaly na zjednodušené analytické modely nebo vyžadovaly masivní datové sady reálných síťových měření. GAN představují posun paradigmatu směrem k augmentaci dat a vytváření syntetického prostředí, což umožňuje sofistikovanější síťovou inteligenci při respektování předpisů na ochranu soukromí a praktických omezení sběru dat. Jejich integrace do standardů 3GPP odráží posun průmyslu směrem k AI-nativním sítím, kde je inteligence vestavěna do celé architektury, nikoli přidávána dodatečně.

## Klíčové vlastnosti

- Architektura se dvěma sítěmi – generátorovou a diskriminační neuronovou sítí
- Generování syntetických dat zachovávajících statistické vlastnosti reálných síťových dat
- Adversariální tréninkový proces pro průběžné vylepšování modelu
- Rozšiřování dat s ochranou soukromí pro trénink modelů AI
- Generování scénářů pro testování vzácných síťových podmínek
- Integrace s NWDAF pro vylepšení síťové analytiky

## Související pojmy

- [AI/ML – Artificial Intelligence and Machine Learning](/mobilnisite/slovnik/ai-ml/)

## Definující specifikace

- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TR 26.914** (Rel-19) — Multimedia Telephony over IP Optimization
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gan/)
