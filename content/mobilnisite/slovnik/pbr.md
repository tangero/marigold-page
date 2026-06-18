---
slug: "pbr"
url: "/mobilnisite/slovnik/pbr/"
type: "slovnik"
title: "PBR – Physically-Based Rendering"
date: 2025-01-01
abbr: "PBR"
fullName: "Physically-Based Rendering"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbr/"
summary: "Vykreslovací technika ve standardech 3GPP pro služby rozšířené reality (XR), která simuluje fyzikální chování světla za účelem generování fotorealistické grafiky. Je klíčová pro vytváření imerzivních"
---

PBR je 3GPP vykreslovací technika pro XR, která simuluje fyzikální chování světla za účelem vytváření fotorealistické grafiky, což je klíčové pro imerzivní AR/VR v sítích 5G.

## Popis

Physically-Based Rendering (PBR) v kontextu 3GPP označuje soubor pokročilých technik počítačové grafiky standardizovaných pro podporu vysoce kvalitních, imerzivních služeb rozšířené reality ([XR](/mobilnisite/slovnik/xr/)) v mobilních sítích. Na rozdíl od tradičních vykreslovacích metod, které používají aproximace a umělecké úpravy, algoritmy PBR simulují fyzikální vlastnosti materiálů a reálné interakce světla s těmito povrchy. To zahrnuje složité výpočty pro odraz, lom, absorpci a rozptyl světla založené na obousměrných distribučních funkcích odrazivosti (BRDF) a dalších fyzikálních modelech. Cílem je vytvářet vizuály, které jsou konzistentní za různých světelných podmínek, čímž se dosahuje vysokého stupně fotorealismu nezbytného pro přesvědčivá prostředí [AR](/mobilnisite/slovnik/ar/) a [VR](/mobilnisite/slovnik/vr/).

V architektuře systému pro poskytování služeb XR může být zpracování PBR distribuováno mezi uživatelské zařízení (UE), jako je například XR headset, a servery na okraji sítě nebo v cloudu. Specifikace 3GPP, zejména v TS 26.928 a TS 26.998, zkoumají dopady takového vykreslování na síť. Vykreslovací engine, ať už lokální nebo vzdálený, používá PBR shadery a texturové mapy (albedo, normálová, drsnost, metalická) k výpočtu finální barvy pixelu pro každý snímek. Tento výpočet je výpočetně náročný a přímo ovlivňuje požadavky na datový tok, latenci a snímkovou frekvenci pro mediální stream přenášený přes systém 5G.

Role PBR v síti je mnohostranná. Definuje klíčovou charakteristiku provozu generovaného aplikacemi XR nové generace. Síťové funkce, včetně 5G Core (5GC) a Radio Access Network (RAN), si musí být vědomy přísných požadavků QoS na obsah vykreslený pomocí PBR, jako je ultra-nízká latence pro interaktivní zpětnou vazbu a vysoká šířka pásma pro streamování detailních textur. Studie 3GPP tento provoz modelují, aby navrhly vhodné síťové řezy, strategie vykládání výpočetního výkonu na hranu sítě ([MEC](/mobilnisite/slovnik/mec/)) a politiky správy rádiových prostředků, které mohou efektivně doručovat takto náročné služby při zachování uživatelské kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

## K čemu slouží

Standardizace technik Physically-Based Rendering v 3GPP byla motivována vzestupem imerzivních služeb rozšířené reality jako klíčového případu užití pro sítě 5G a další generace. Předchozí mobilní grafické a streamovací služby, jako je tradiční video, spoléhaly na jednodušší vykreslovací modely, které nevyžadovaly stejnou úroveň fyzikální přesnosti nebo interaktivity. Tyto starší přístupy byly nedostatečné pro vytváření věrohodných virtuálních světů, kde je vizuální konzistence a realismus prvořadý pro uživatelskou imerzi a komfort, zejména v profesionálním tréninku, sociální interakci a zábavních aplikacích.

PBR řeší problém vizuální nekonzistence nacházející se ve starších, ad-hoc vykreslovacích metodách. Tím, že zakládá výpočty na fyzikálních zákonech, zajišťuje, že materiály vypadají správně v jakémkoli světelném prostředí, což je kritické pro aplikace [AR](/mobilnisite/slovnik/ar/), které prolínají digitální objekty s reálným světem. Z pohledu sítě je porozumění PBR zásadní, protože vytváří novou třídu provozu s předvídatelnými, ale náročnými vzorci. Práce 3GPP na PBR, započatá ve verzi 15 studiemi o [XR](/mobilnisite/slovnik/xr/), si klade za cíl charakterizovat tento provoz, aby vyřešila výzvy síťového plánování a optimalizace. Pomáhá definovat potřebné parametry QoS, jako je rozpočet zpoždění paketů a garantovaný datový tok, pro podporu streamování grafiky v reálném čase, interaktivní a s vysokou věrností, což nebylo primárním zájmem multimediálních služeb před érou 5G.

## Klíčové vlastnosti

- Simuluje interakci světla v reálném světě pomocí fyzikálních modelů, jako jsou BRDF a zákon zachování energie
- Využívá mapy vlastností materiálů (albedo, drsnost, metalická, normálová) pro přesnou reprezentaci povrchu
- Zajišťuje vizuální konzistenci objektů v různých světelných prostředích
- Generuje výpočetně náročné úlohy ovlivňující zpracování v UE a na síťové hraně
- Definuje přísné modely provozu pro plánování QoS sítě v aplikacích XR
- Umožňuje grafiku s vysokou věrností a fotorealismem pro imerzivní zážitky AR/VR

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [PBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbr/)
