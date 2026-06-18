---
slug: "scs"
url: "/mobilnisite/slovnik/scs/"
type: "slovnik"
title: "SCS – Subcarrier Spacing"
date: 2026-01-01
abbr: "SCS"
fullName: "Subcarrier Spacing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scs/"
summary: "Frekvenční rozestup mezi sousedními ortogonálními podnosnými v rádiovém systému založeném na OFDM, jako jsou 4G LTE a 5G NR. Jde o základní parametr fyzické vrstvy, který určuje délku symbolu, ovlivňu"
---

SCS je základní frekvenční rozestup mezi sousedními ortogonálními podnosnými v systému založeném na OFDM, jako je 5G NR, který určuje délku symbolu a umožňuje flexibilní numerologii pro různé služby.

## Popis

Rozestup podnosných (Subcarrier Spacing, SCS) je klíčový parametr v systémech Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([OFDM](/mobilnisite/slovnik/ofdm/)) a Orthogonal Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([OFDMA](/mobilnisite/slovnik/ofdma/)), které tvoří základ rozhraní 4G LTE a 5G New Radio (NR). Definuje frekvenční rozdíl od středu ke středu mezi sousedními podnosnými, které tvoří celkovou šířku pásma kanálu systému. V těchto systémech jsou uživatelská data rozdělena a modulována na mnoho těsně rozmístěných, ortogonálních podnosných vysílaných paralelně. Ortogonalita, která zabraňuje interferenci mezi nosnými, je matematicky zachována, když je SCS přesně reciproký hodnotě užitečné délky symbolu (s výjimkou cyklické předpony). SCS tedy přímo určuje strukturu v časové oblasti: větší SCS má za následek kratší délku symbolu a kratší délku slotu, a naopak.

Z architektonického hlediska je SCS součástí 'numerologie' systému OFDM. V 5G NR byl tento koncept výrazně rozšířen zavedením flexibilní numerologie, kde je SCS definováno jako Δf = 2μ * 15 kHz, kde μ je celočíselný parametr numerologie (např. 0, 1, 2, 3, 4). To dává standardní hodnoty SCS jako 15 kHz (μ=0, běžné v LTE), 30 kHz (μ=1), 60 kHz (μ=2), 120 kHz (μ=3) a 240 kHz (μ=4). Každá numerologie vytváří odlišnou strukturu časově-frekvenční mřížky. Síť může konfigurovat různé numerologie pro různá frekvenční pásma (FR1: pod 6 GHz, FR2: mmWave) a pro různé požadavky služeb. Širší SCS poskytuje větší odolnost vůči Dopplerovu rozprostření a fázovému šumu, což jej činí vhodným pro vysokofrekvenční pásma a vysokorychlostní mobilitu, zatímco užší SCS nabízí delší symboly, což je výhodné pro rozšíření pokrytí a efektivní podporu úzkopásmových IoT zařízení.

SCS hraje v síti mnohostrannou roli. Je klíčovým determinantem výkonu a flexibility systému. Ovlivňuje režii z cyklické předpony ([CP](/mobilnisite/slovnik/cp/)), latenci (prostřednictvím délky symbolu a slotu), citlivost na frekvenční posuny a dosažitelnou přesnost sledování fáze. Během počátečního přístupu zařízení detekuje SCS ze synchronizačních signálů. gNodeB (v 5G) nebo eNodeB (v LTE) plánuje prostředky na fyzických sdílených kanálech pro downlink a uplink na základě nakonfigurované numerologie. Volba SCS je tedy kritickou konfigurací na úrovni spojení, která umožňuje 5G splnit své rozmanité klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) pro rozšířené mobilní širokopásmové připojení (eMBB), ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a hromadnou komunikaci mezi stroji (mMTC).

## K čemu slouží

Koncept rozestupu podnosných (SCS) existoval v LTE, ale byl pevně nastaven na 15 kHz pro většinu scénářů downlinku a uplinku, se speciálním rozestupem 7,5 kHz používaným pouze pro úzkopásmové [MBSFN](/mobilnisite/slovnik/mbsfn/) podrámce. Tento pevný přístup byl dostačující pro primární zaměření 4G na mobilní širokopásmový přenos. Avšak výrazně rozšířený rozsah 5G – zahrnující frekvence od pod 1 GHz po milimetrové vlny a služby od nízkopříkonového IoT po vysokorychlostní vlaky a průmyslovou automatizaci – vyžadoval flexibilnější základ. Jediná, pevná hodnota SCS nemohla optimálně řešit protichůdné požadavky na široké pokrytí (vyžadující dlouhé symboly), vysokou mobilitu a vysoké frekvence (vyžadující krátké symboly pro potlačení Dopplerova jevu/fázového šumu) a ultra-nízkou latenci (vyžadující krátké přenosové časové intervaly).

Zavedení flexibilní numerologie založené na škálovatelném SCS v 5G NR tento problém vyřešilo. Umožnilo systému přizpůsobit jeho základní časově-frekvenční strukturu scénáři nasazení. Tato flexibilita byla klíčovou inovací fyzické vrstvy, která umožnila, aby bylo 5G skutečně univerzální. Například SCS 15 kHz lze použít pro pokrytí široké oblasti v pásmech pod 1 GHz, 30 kHz nebo 60 kHz pro hlavní mobilní širokopásmový přenos v mid-bandech a 120 kHz nebo 240 kHz pro nasazení v milimetrových vlnách, kde je fázový šum významný. Umožňuje také smíšené numerologie v rámci stejné nosné, podporující latencí kritický provoz URLLC na širším SCS v 'mini-slotu', zatímco provoz eMBB pokračuje na mřížce s užším SCS. Tato účelově řízená přizpůsobivost je ústřední pro schopnost 5G sloužit jako jednotná platforma pro všechny komunikační potřeby.

## Klíčové vlastnosti

- Definuje frekvenční odstup mezi OFDM podnosnými (např. 15, 30, 60, 120, 240 kHz)
- Nepřímo úměrný užitečné délce OFDM symbolu
- Umožňuje flexibilní numerologii v 5G NR (Δf = 2μ * 15 kHz)
- Ovlivňuje odolnost vůči Dopplerovu rozprostření a fázovému šumu
- Určuje délku slotu a minimální granularitu plánování
- Konfigurovatelné dle frekvenčního pásma a typu služby (eMBB, URLLC, mMTC)

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- … a dalších 112 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/scs/)
