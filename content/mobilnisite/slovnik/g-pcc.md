---
slug: "g-pcc"
url: "/mobilnisite/slovnik/g-pcc/"
type: "slovnik"
title: "G-PCC – Geometry-based Point Cloud Compression"
date: 2025-01-01
abbr: "G-PCC"
fullName: "Geometry-based Point Cloud Compression"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/g-pcc/"
summary: "Kompresní standard pro 3D data bodových mračen, vyvinutý 3GPP pro imerzivní média a aplikace XR. Efektivně kóduje geometrické a atributové informace bodových mračen, což umožňuje kvalitní streamování"
---

G-PCC je kompresní standard 3GPP pro 3D data bodových mračen, který efektivně kóduje geometrické a atributové informace, aby umožnil kvalitní streamování a ukládání pro imerzivní média a aplikace XR.

## Popis

Geometry-based Point Cloud Compression (G-PCC) je standardizovaná kompresní technologie pro 3D data bodových mračen, specifikovaná v 3GPP Release 16 a později v dokumentech jako 26.928 a 26.998. Bodová mračna jsou soubory datových bodů v 3D souřadnicovém systému, které reprezentují povrchovou geometrii objektů nebo scén a často se používají v aplikacích jako rozšířená realita ([AR](/mobilnisite/slovnik/ar/)), virtuální realita (VR) a autonomní vozidla. G-PCC se zaměřuje na efektivní kódování jak geometrie (prostorové pozice bodů), tak atributů (např. barva, odrazivost) bodových mračen a využívá pokročilé algoritmy ke snížení objemu dat bez výrazné ztráty kvality. Funguje jako součást širšího souboru MPEG-I pro imerzivní média a integruje se se sítěmi 5G, aby umožnil streamování v reálném čase a interaktivní zážitky.

Z architektonického hlediska G-PCC používá dvouproudový přístup: jeden proud pro kompresi geometrie a druhý pro kompresi atributů. Komprese geometrie typicky využívá rozdělení na bázi oktalového stromu (octree), kde je 3D prostor rekurzivně rozdělován na oktanty a obsazenost těchto oktantů je kódována pomocí technik entropického kódování, jako je aritmetické kódování. Tato metoda efektivně reprezentuje řídké distribuce bodů běžné v reálných skenech. Pro atributy G-PCC aplikuje prediktivní kódování nebo metody založené na transformaci, jako je Region Adaptive Hierarchical Transform (RAHT), aby využila prostorové korelace mezi body. Kompresní proces zahrnuje kroky jako kvantizace, kde se upravuje přesnost pro vyvážení kvality a datového toku, a entropické kódování pro odstranění statistické redundance. Klíčové komponenty zahrnují enkodér, který zpracovává nezpracovaná data bodového mračna do komprimovaných bitových proudů, a dekodér, který rekonstruuje bodové mračno pro vykreslování nebo analýzu.

Jak to funguje v praxi: bodové mračno zachycené senzory (např. LiDAR nebo hloubkové kamery) je vstupem do G-PCC enkodéru, který analyzuje geometrii a atributy, aplikuje rozdělení a predikci a vytváří komprimovaný bitový proud. Tento bitový proud lze přenášet přes sítě 5G s nižšími nároky na šířku pásma, efektivně ukládat nebo dekódovat v reálném čase na zařízeních, jako jsou VR headset. G-PCC podporuje různé profily a úrovně přizpůsobené různým případům užití, od statických objektů po dynamické sekvence. Jeho role v síti spočívá v usnadnění imerzivních služeb tím, že umožňuje doručování kvalitního 3D obsahu v rámci omezení dostupné šířky pásma, v souladu se schopnostmi 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB) a ultra-spolehlivá komunikace s nízkou latencí (URLLC). Standardizací komprese G-PCC zajišťuje interoperabilitu napříč zařízeními a platformami a podporuje soudržný ekosystém pro rozšířenou realitu (XR) a další aplikace.

## K čemu slouží

G-PCC byl vytvořen, aby řešil rostoucí poptávku po efektivní kompresi 3D dat bodových mračen, kterou pohání rozšíření imerzivních médií a aplikací XR v éře 5G. Před jeho standardizací byla data bodových mračen často nekomprimovaná nebo používala proprietární kompresní schémata, což vedlo k nadměrným požadavkům na úložiště a šířku pásma – bodová mračna ze zdrojů, jako jsou LiDAR skenery nebo 3D kamery, mohla generovat gigabajty dat za sekundu, což činilo streamování v reálném čase přes stávající sítě nepraktickým. Toto omezení bránilo adopci [AR](/mobilnisite/slovnik/ar/)/VR, teleprezence a autonomních systémů, které spoléhají na věrné 3D reprezentace. G-PCC tyto problémy řeší tím, že poskytuje standardizovanou, vysoce účinnou kompresní metodu, která výrazně snižuje objemy dat při zachování percepční kvality.

Motivována potřebou integrovat imerzivní média do služeb 5G, zavedla 3GPP G-PCC v Release 16 jako součást širšího úsilí o definici mediálních kodeků pro nové případy užití. Historický kontext zahrnuje dřívější standardy [MPEG](/mobilnisite/slovnik/mpeg/), jako je video-based point cloud compression (V-PCC), které promítaly 3D data do 2D rovin pro video kódování; G-PCC nabízí přímější přístup založený na geometrii, který je vhodnější pro řídké a nepravidelné distribuce bodů běžné v reálných snímcích. Řeší omezení předchozích přístupů tím, že umožňuje nižší latenci, lepší škálovatelnost a vylepšené kompresní poměry pro širokou škálu typů bodových mračen, od statických skenů kulturního dědictví po dynamická automobilová prostředí.

Dále G-PCC podporuje vývoj směrem k aplikacím metaverse a digitálních dvojčat tím, že umožňuje efektivní přenos složitých 3D světů. Jeho vytvoření bylo poháněno průmyslovou spoluprací v rámci 3GPP a MPEG s cílem stanovit jednotný standard, který snižuje fragmentaci a podporuje inovace. Řešením klíčových výzev v manipulaci s daty G-PCC připravuje cestu pro služby nové generace, které vyžadují bohaté 3D interakce, a zajišťuje, že sítě 5G mohou doručovat imerzivní zážitky udržitelně a ve velkém měřítku.

## Klíčové vlastnosti

- Efektivní komprese geometrie 3D bodových mračen využívající rozdělení na bázi oktalového stromu (octree-based partitioning)
- Pokročilá komprese atributů s technikami jako RAHT pro data barvy a odrazivosti
- Podpora jak ztrátových, tak bezztrátových kompresních režimů pro flexibilní kompromisy mezi kvalitou a datovým tokem
- Umožňuje streamování v reálném čase a dekódování s nízkou latencí pro interaktivní aplikace XR
- Standardizované profily pro různé případy užití včetně statických, dynamických a LiDAR bodových mračen
- Integruje se se sítěmi 5G, aby usnadnil doručování imerzivních médií v rámci eMBB a URLLC

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [G-PCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-pcc/)
