---
slug: "3d-hevc"
url: "/mobilnisite/slovnik/3d-hevc/"
type: "slovnik"
title: "3D-HEVC – Three-Dimensional High Efficiency Video Coding"
date: 2025-01-01
abbr: "3D-HEVC"
fullName: "Three-Dimensional High Efficiency Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/3d-hevc/"
summary: "3D-HEVC je pokročilý standard komprese videa pro stereoskopický a vícepohledový videoobsah, který umožňuje efektivní přenos 3D videa přes mobilní sítě. Rozšiřuje HEVC o specializované kódovací nástroj"
---

3D-HEVC je pokročilý standard komprese videa, který rozšiřuje HEVC o specializované nástroje pro hloubkové mapy a více pohledů, aby umožnil efektivní přenos 3D videa přes mobilní sítě.

## Popis

3D-HEVC je standard pro kódování videa vyvinutý jako rozšíření standardu High Efficiency Video Coding (HEVC/H.265) speciálně navržený pro trojrozměrný videoobsah. Tato technologie řeší jedinečné požadavky stereoskopického 3D a vícepohledového videa zavedením specializovaných kódovacích nástrojů, které efektivně komprimují jak texturu (barevné informace), tak hloubkové mapy. Na rozdíl od konvenčního 2D kódování videa musí 3D-HEVC zpracovávat více korelovaných pohledů na stejnou scénu, což vyžaduje sofistikované predikční mechanismy pro využití redundance mezi pohledy při zachování schopnosti rekonstruovat mezilehlé pohledy v dekodéru.

Architektura 3D-HEVC staví na rámci HEVC, ale zavádí několik klíčových rozšíření. Systém podporuje více texturových pohledů spolu s odpovídajícími hloubkovými mapami, které poskytují informaci o hloubce na úrovni pixelu. Hloubkové mapy jsou typicky reprezentovány jako stupňovité obrazy, kde intenzita pixelu odpovídá vzdálenosti od kamery. 3D-HEVC využívá pokročilé predikční techniky včetně predikce s kompenzací disparit (DCP), která umožňuje predikci mezi různými pohledy, podobně jako pohybová kompenzace mezi snímky v temporální predikci. Tato predikce mezi pohledy významně snižuje redundanci mezi sousedními kamerovými pohledy.

Mezi klíčové technické komponenty patří režimy modelování hloubky (DMM) speciálně navržené pro kódování hloubkových map, které využívají po částech hladkou povahu hloubkových informací. Standard podporuje různé formáty 3D videa včetně stereoskopického videa (dva pohledy), vícepohledového videa (více kamerových pohledů) a formátů vícepohledového videa plus hloubka (MVD). Kódovací proces zahrnuje společnou optimalizaci kódování textury a hloubky, kde optimalizace rychlost-deformace bere v úvahu jak kvalitu rekonstruovaných texturových pohledů, tak přesnost syntetizovaných mezilehlých pohledů.

V sítích 3GPP umožňuje 3D-HEVC efektivní doručování imerzních videoslužeb přes mobilní připojení s omezenou šířkou pásma. Standard podporuje škálovatelné kódovací konfigurace, kde základní vrstvy poskytují základní 3D kvalitu, zatímco vylepšující vrstvy přidávají další pohledy nebo vyšší rozlišení. Tato škálovatelnost je obzvláště důležitá pro scénáře adaptivního streamování, kde se mohou podmínky sítě měnit. Technologie je integrována s multimediálními doručovacími frameworky 3GPP včetně Dynamic Adaptive Streaming over HTTP (DASH) a Multimedia Broadcast/Multicast Service (MBMS) pro unicastovou i broadcastovou distribuci 3D obsahu.

## K čemu slouží

3D-HEVC byl vyvinut, aby řešil rostoucí poptávku po imerzních 3D videoslužbách a zároveň překonal omezení šířky pásma mobilních sítí. Tradiční přístupy kódování 2D videa se ukázaly jako neefektivní pro 3D obsah, protože zacházely s více pohledy jako s nezávislými videoproudy a nevyužívaly vysokou korelaci mezi různými perspektivami stejné scény. To vedlo k přibližně dvojnásobným požadavkům na šířku pásma pro stereoskopické video ve srovnání s 2D videem, což činilo 3D služby nepraktickými pro masové nasazení přes celulární sítě.

Technologie se objevila v období rostoucího zájmu o 3D televizi a imerzní mediální zážitky. Předchozí přístupy k doručování 3D videa buď používaly formáty kompatibilní se snímky, které obětovaly rozlišení, nebo nezávisle přenášely plné levé a pravé pohledy s neefektivní kompresí. 3D-HEVC tyto problémy vyřešil zavedením specializovaných kódovacích nástrojů, které rozpoznávají geometrické vztahy mezi pohledy, což umožnilo mnohem vyšší kompresní účinnost. To umožnilo doručování vysoce kvalitního 3D videa s datovými toky jen o něco vyššími než u ekvivalentního 2D obsahu.

Další klíčovou motivací byla potřeba podporovat pokročilé technologie 3D zobrazování včetně autostereoskopických displejů, které pro 3D prohlížení bez brýlí vyžadují více pohledů. Tyto displeje typicky potřebují 5–9 různých pohledů, aby poskytly správné 3D vnímání z různých úhlů pohledu. Nezávislý přenos všech těchto pohledů by byl z hlediska šířky pásma neúnosně nákladný. Schopnost 3D-HEVC efektivně kódovat více pohledů a syntetizovat mezilehlé pohledy na přijímači umožnila praktické nasazení takových pokročilých 3D zobrazovacích systémů přes mobilní sítě.

## Klíčové vlastnosti

- Predikce s kompenzací disparit pro kódování mezi pohledy
- Kódování hloubkových map se specializovanými režimy modelování hloubky
- Podpora formátu vícepohledového videa plus hloubka (MVD)
- Optimalizace syntézy pohledů pro generování mezilehlých pohledů
- Škálovatelné kódování se základními a vylepšujícími vrstvami
- Integrace s multimediálními doručovacími frameworky 3GPP

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [3D-HEVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/3d-hevc/)
