---
slug: "slam"
url: "/mobilnisite/slovnik/slam/"
type: "slovnik"
title: "SLAM – Simultaneous Localization and Mapping"
date: 2025-01-01
abbr: "SLAM"
fullName: "Simultaneous Localization and Mapping"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/slam/"
summary: "Simultaneous Localization and Mapping (SLAM) je výpočetní technika, která umožňuje zařízení, jako je robot nebo AR headset, vytvořit mapu neznámého prostředí a zároveň v něm sledovat svou vlastní polo"
---

SLAM je výpočetní technika standardizovaná organizací 3GPP pro vylepšené polohové služby, která umožňuje zařízení vytvořit mapu neznámého prostředí a zároveň v něm sledovat svou vlastní polohu.

## Popis

Simultaneous Localization and Mapping (SLAM) je základní algoritmus v robotice a rozšířené realitě, který řeší problém navigace typu „slepice a vejce“: k vytvoření mapy prostředí potřebujete znát svou polohu a k určení polohy potřebujete mapu. 3GPP standardizoval podporu SLAM pro pokročilé služby založené na poloze v 5G a dalších generacích, zejména pro vertikály jako průmyslový IoT, autonomní systémy a rozšířenou realitu ([XR](/mobilnisite/slovnik/xr/)). Systém 3GPP poskytuje potřebná data a referenční rámce, které pomáhají uživatelskému zařízení (UE) nebo síťovým entitám provádět SLAM přesněji a efektivněji.

Technicky SLAM funguje fúzí dat z více senzorů. Zařízení využívá své vlastní senzory (např. kamery, LiDAR, jednotky pro měření setrvačnosti – [IMU](/mobilnisite/slovnik/imu/)) k vnímání prvků v prostředí (orientačních bodů). Jak se zařízení pohybuje, pozoruje tyto orientační body z různých perspektiv. Algoritmus SLAM, často založený na pravděpodobnostních rámcích jako Kalmanovy filtry nebo částicové filtry, iterativně odhaduje dvě propojené proměnné: pozici zařízení (polohu a orientaci) a 3D polohy všech pozorovaných orientačních bodů, čímž mapu postupně vytváří. Výzvou je zvládání nejistoty a přiřazování dat – správné určení, které nové pozorování odpovídá kterému dříve zmapovanému orientačnímu bodu.

Úloha 3GPP, jak je definována v dokumentech jako TR 26.928, spočívá v poskytování vylepšení, která napomáhají procesu SLAM. To zahrnuje dodávání vysoce přesných absolutních polohových dat (např. z polohových metod LTE/5G jako [OTDOA](/mobilnisite/slovnik/otdoa/) nebo [RTT](/mobilnisite/slovnik/rtt/)) pro korekci driftu, který je vlastní SLAM založenému pouze na senzorech. Síť může také poskytnout předem existující částečné mapy nebo sémantické informace (např. půdorysy) jako výchozí podklad, nebo přesunout výpočetně náročné části zpracování SLAM na servery edge cloudu. Tento síťově asistovaný SLAM zlepšuje spolehlivost, snižuje výpočetní zátěž UE a umožňuje kolaborativní mapování, při kterém více zařízení přispívá ke sdílené mapě.

## K čemu slouží

Technologie SLAM existuje proto, aby umožnila autonomní provoz a pokročilé kontextové povědomí v prostředích, kde nejsou k dispozici podrobné předem vytvořené mapy nebo která jsou dynamická. Pro roboty, drony a zařízení [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/) je [GPS](/mobilnisite/slovnik/gps/) často nedostupná v interiérech nebo nedostatečně přesná. Čistá inerciální navigace ([IMU](/mobilnisite/slovnik/imu/)) rychle akumuluje drift. SLAM tento problém řeší vytvářením mapy za běhu, což umožňuje dlouhodobou navigaci a interakci.

Standardizace podpory SLAM v 3GPP, počínaje verzí Rel-16, byla motivována potřebami nových vertikál 5G. Průmyslová automatizace vyžaduje, aby autonomní vozidla (AGV) navigovala v továrnách; rozšířená realita potřebuje trvalý obsah ukotvený ve světě. Předchozí polohové služby 3GPP (např. A-GNSS, OTDOA) poskytovaly absolutní polohu, ale postrádaly husté, relativní porozumění prostředí potřebné pro tyto aplikace. Samostatný SLAM prováděný na zařízení má omezení v měřítku, konzistenci napříč zařízeními a přesnosti v dlouhých časových úsecích.

Integrací SLAM s mobilní sítí řeší 3GPP tato omezení. Síť poskytuje absolutní referenční body k eliminaci kumulativního driftu SLAM, umožňuje sdílení a trvalost map pro více uživatelů a umožňuje výpočetně efektivní architektury s rozděleným zpracováním. Vytváří tak škálovatelnou a spolehlivou polohovou a mapovací službu, která je klíčovým prvkem pro metaverse, Průmysl 4.0 a autonomní systémy.

## Klíčové vlastnosti

- Současný odhad pozice zařízení a mapy prostředí v reálném čase
- Fúze vizuálních, LiDARových, inerciálních a měření z buněčného rádiového rozhraní
- Poskytování absolutních polohových referenčních bodů sítí pro korekci driftu senzorů
- Podpora kolaborativního mapování napříč více uživatelskými zařízeními
- Přesun výpočetně náročné optimalizace mapy do cloudu nebo na edge
- Integrace s architekturou polohování 3GPP (LPP, NRPPa) pro asistovaná data

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [XR – AS Augmented/Virtual Reality Application Server](/mobilnisite/slovnik/xr/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [SLAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/slam/)
