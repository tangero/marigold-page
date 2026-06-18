---
slug: "cnn"
url: "/mobilnisite/slovnik/cnn/"
type: "slovnik"
title: "CNN – Convolutional Neural Network"
date: 2025-01-01
abbr: "CNN"
fullName: "Convolutional Neural Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cnn/"
summary: "Architektura hlubokého učení specializovaná pro zpracování dat ve formě mřížky, jako jsou obrazy a časové řady signálů. Ve standardech 3GPP se CNN používají pro správu rádiových zdrojů, predikci stavu"
---

CNN je architektura hlubokého učení používaná ve standardech 3GPP pro zpracování dat o rádiovém prostředí za účelem umožnění inteligentních síťových operací, jako je správa zdrojů a predikce kanálu.

## Popis

Konvoluční neuronová síť (CNN) je specializovaný typ umělé neuronové sítě navržený pro zpracování dat s topologií podobnou mřížce, která je obzvláště účinná pro rozpoznávání obrazu, analýzu časových řad a zpracování prostorových dat. Ve standardech 3GPP jsou CNN využívány jako modely strojového učení v rámci frameworku [AI/ML](/mobilnisite/slovnik/ai-ml/) pro různé úlohy optimalizace rádiové přístupové sítě. Architekturu charakterizují konvoluční vrstvy, které aplikují filtry na vstupní data pro extrakci hierarchických příznaků, poolingové vrstvy, které redukují prostorové dimenze při zachování důležitých informací, a plně propojené vrstvy, které provádějí klasifikaci nebo regresi na základě extrahovaných příznaků.

Architektura CNN v aplikacích 3GPP typicky sestává z více konvolučních vrstev s aktivačními funkcemi (obvykle ReLU), vrstev batch normalizace pro stabilní trénink a vrstev dropout pro regularizaci. Konvoluční operace zahrnuje posouvání filtrů (jader) přes vstupní data za účelem vytvoření příznakových map, které zachycují lokální vzorce. Tyto filtry se během tréninku učí pomocí zpětné propagace, což síti umožňuje automaticky objevovat relevantní příznaky ze surových vstupních dat bez nutnosti ručního inženýrství příznaků. V rádiových přístupových sítích CNN zpracovávají data jako jsou informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), vzory beamformingu, mapy interference a vzorce distribuce uživatelů.

Ve specifikacích 3GPP jsou CNN integrovány do architektur funkce pro analýzu síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) a inteligentního kontroléru rádiové přístupové sítě (RIC). Operují nad daty shromážděnými od síťových funkcí, uživatelských zařízení (UE) a rádiových měření, aby prováděly úlohy jako predikce provozu, optimalizace mobility, správa beamů a přidělování zdrojů. Modely CNN mohou být trénovány offline pomocí historických síťových dat a následně nasazeny pro inferenci v reálném provozu sítě. 3GPP specifikuje rozhraní pro trénink, validaci a nasazení modelů, včetně mechanismů pro aktualizace modelů a sledování výkonnosti.

Klíčové technické aspekty CNN v 3GPP zahrnují jejich schopnost zpracovávat vícerozměrná vstupní data (jako jsou časově-frekvenční mřížky zdrojů), podporu různých vstupních modalit (včetně CSI reportů, měřicích reportů a výkonnostních metrik) a integraci se systémy správy sítě. Modely jsou navrženy tak, aby byly výpočetně efektivní pro nasazení v síťových prvcích s omezenými zdroji, a podporují techniky kvantizace a prořezávání. 3GPP také specifikuje požadavky na vysvětlitelnost modelů, robustnost vůči adversariálním útokům a spravedlnost v rozhodování, když jsou CNN používány pro úlohy optimalizace sítě.

## K čemu slouží

CNN byly zavedeny do standardů 3GPP, aby řešily rostoucí složitost optimalizace rádiové přístupové sítě v systémech 5G a dalších generací. Tradiční optimalizační algoritmy založené na matematických modelech nedokážou zvládnout vysoce dimenzionální, nelineární vztahy v moderních bezdrátových sítích s massive [MIMO](/mobilnisite/slovnik/mimo/), beamformingem a dynamickým sdílením spektra. CNN poskytují daty řízený přístup, který se dokáže naučit složité vzorce ze síťových měření a přizpůsobit se měnícím se rádiovým podmínkám bez explicitního naprogramování optimalizačních pravidel.

Motivace pro začlenění CNN do standardů 3GPP vychází z potřeby inteligentní síťové automatizace a samooptymalizujících se sítí ([SON](/mobilnisite/slovnik/son/)). Jak se sítě stávají hustšími a heterogennějšími se zavedením small cells, mmWave komunikací a síťového slicingu, ruční konfigurace a optimalizace založená na pravidlech se stává nepraktickou. CNN umožňují prediktivní správu sítě tím, že se učí z historických dat a předvídají síťové události, jako jsou špičky provozu, podmínky interference a vzorce mobility. To umožňuje proaktivní přidělování zdrojů a ladění parametrů, které zlepšuje výkon sítě a uživatelský zážitek.

Předchozí přístupy k optimalizaci sítě spoléhaly na zjednodušené modely a heuristické algoritmy, které nedokázaly zachytit plnou složitost reálného rádiového prostředí. Tyto metody často vyžadovaly rozsáhlé ruční ladění a nemohly se rychle přizpůsobit měnícím se podmínkám. CNN řeší tato omezení tím, že poskytují framework pro učení optimálních řídicích politik přímo z dat, což umožňuje přesnější predikce a lepší optimalizační rozhodnutí. Integrace CNN do standardů 3GPP představuje posun směrem k AI-nativnímu síťovému designu, kde se strojové učení stává integrální součástí síťových operací a správy.

## Klíčové vlastnosti

- Hierarchická extrakce příznaků prostřednictvím konvolučních vrstev
- Prostorová invariance prostřednictvím poolingových operací
- Sdílení parametrů snižující složitost modelu
- Schopnosti zpracování vícerozměrných vstupů
- Integrace s frameworkem a rozhraními AI/ML 3GPP
- Podpora offline tréninku i online inference

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 22.874** (Rel-18) — Technical Report
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface

---

📖 **Anglický originál a plná specifikace:** [CNN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnn/)
