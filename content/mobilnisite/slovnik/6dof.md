---
slug: "6dof"
url: "/mobilnisite/slovnik/6dof/"
type: "slovnik"
title: "6DOF – Six Degrees of Freedom"
date: 2025-01-01
abbr: "6DOF"
fullName: "Six Degrees of Freedom"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/6dof/"
summary: "6DOF označuje schopnost sledovat pohyb a orientaci v trojrozměrném prostoru pomocí šesti nezávislých proměnných: tří pro polohu (X, Y, Z) a tří pro rotaci (náklon, klopení, odchylka). V 3GPP je klíčov"
---

6DOF je schopnost sledovat pohyb a orientaci v 3D prostoru pomocí šesti proměnných pro polohu a rotaci, což je klíčové pro imerzivní služby, jako je rozšířená realita v sítích 5G.

## Popis

Six Degrees of Freedom (6DOF) je základní koncept v normách 3GPP pro reprezentaci úplného prostorového pohybu a orientace v trojrozměrných prostředích. Skládá se ze šesti nezávislých parametrů: tří translačních stupňů volnosti (poloha podél os X, Y a Z) a tří rotačních stupňů volnosti (orientace kolem těchto os, obvykle popsaná jako náklon, klopení a odchylka). Tato komplexní prostorová reprezentace umožňuje přesné sledování pohybu uživatele a orientace jeho pohledu, což je zásadní pro vytváření přesvědčivých imerzivních zážitků, kde se uživatelé mohou volně pohybovat a přirozeně interagovat s virtuálními nebo rozšířenými prostředími.

V architektuře 3GPP je podpora 6DOF integrována přes více vrstev a rozhraní. Na aplikační vrstvě specifikace 3GPP definují, jak jsou data 6DOF formátována, přenášena a synchronizována s mediálními proudy. Architektura Media Streaming Architecture (MSA) v TS 26.918 a TS 26.929 specifikuje protokoly pro doručování médií 6DOF, včetně způsobu kódování informace o pohledu spolu s video a audio daty. To zahrnuje specializované mediální formáty, které dokáží reprezentovat nejen tradiční 2D video, ale i prostorová média, která se mění na základě polohy a orientace uživatele.

Technická implementace zahrnuje několik klíčových komponent pracujících společně. Klientská zařízení (jako jsou XR headset) průběžně sledují svou 6DOF polohu pomocí senzorů, jako jsou akcelerometry, gyroskopy a někdy externí sledovací systémy. Tato sledovací data jsou zpracovávána lokálně a mohou být přenášena k síťovým prvkům nebo obsahovým serverům. Na síťové straně musí systémy 5G zvládnout požadavky na přenos dat 6DOF s nízkou latencí, protože i malá zpoždění mohou u imerzivních aplikací způsobit nevolnost z pohybu. Rámec Quality of Service (QoS) je rozšířen pro podporu mediálních proudů 6DOF se specifickými požadavky na latenci, spolehlivost a šířku pásma.

Doručování médií 6DOF typicky využívá adaptivní streamovací techniky upravené pro prostorová média. Namísto streamování jediného video proudu může systém přenášet více pohledů nebo používat volumetrické video formáty, které umožňují vykreslování z libovolných pozic. Síť musí efektivně doručovat pouze potřebná data na základě aktuálního pohledu uživatele a předpokládaného pohybu. To vyžaduje těsnou integraci mezi protokoly aplikační vrstvy a schopnostmi sítě 5G, včetně network slicing pro zaručený výkon a edge computing pro snížení latence zpracováním dat 6DOF blíže uživateli.

Role 6DOF v sítích 5G přesahuje základní doručování médií a umožňuje nové paradigmaty služeb. Tvoří základ pro aplikace teleprezence, kde vzdálení uživatelé mohou interagovat, jako by byli fyzicky přítomni, pro kolaborativní virtuální pracovní prostory a imerzivní tréninkové simulace. Specifikace 3GPP zajišťují interoperabilitu mezi zařízeními a službami různých dodavatelů definováním standardních rozhraní pro výměnu dat 6DOF mezi uživatelským zařízením (UE), síťovými funkcemi a mediálními servery. Tato standardizace je klíčová pro vytvoření životaschopného ekosystému služeb s podporou 6DOF, které mohou využívat vysokou propustnost a nízkou latenci sítě 5G.

## K čemu slouží

Technologie 6DOF byla zavedena v 3GPP, aby řešila rostoucí poptávku po imerzivních mediálních službách vyžadujících úplné prostorové sledovací schopnosti. Předchozí mobilní mediální služby byly omezeny na tři stupně volnosti (3DOF), které sledovaly pouze rotační pohyb (orientaci hlavy), nikoliv však pohyb polohy. Toto omezení bránilo skutečně imerzivním zážitkům, kde by se uživatelé mohli pohybovat ve virtuálních prostorech, naklánět se, aby viděli za objekty, nebo interagovat s virtuálními prostředími přirozenými pohyby těla. Přechod z 3DOF na 6DOF představuje zásadní posun v tom, jak uživatelé prožívají digitální obsah, od pasivního sledování k aktivní účasti v trojrozměrných prostorech.

Vytvoření norem pro 6DOF v 3GPP bylo motivováno vznikem rozšířené reality (XR) jako klíčového use case pro 5G. Průmyslové prognózy identifikovaly imerzivní média jako hlavní hnací sílu pro adopci sítí 5G, což vyžadovalo standardizované přístupy k zajištění interoperability napříč zařízeními, sítěmi a poskytovateli obsahu. Bez standardizace by proprietární řešení fragmentovala trh a omezila růst služeb XR. Práce 3GPP na 6DOF poskytuje technický základ pro jednotný ekosystém, kde tvůrci obsahu mohou vyvíjet jednou a nasazovat všude, síťoví operátoři mohou optimalizovat svou infrastrukturu pro imerzivní média a výrobci zařízení mohou implementovat konzistentní rozhraní.

6DOF řeší několik technických výzev, které předchozí přístupy nedokázaly vyřešit. Umožňuje realistické sociální interakce ve virtuálních prostorech, kde uživatelé mohou udržovat odpovídající osobní prostor a používat přirozená gesta. Podporuje prostorový audio, který se realisticky mění, když se uživatelé pohybují prostředím. Nejvýznamněji umožňuje pocit přítomnosti – psychologický pocit skutečného pobytu na virtuálním místě – což je klíčové pro aplikace sahající od vzdálené spolupráce po zábavu. Standardizací 6DOF v Rel-15 a novějších vytvořil 3GPP technický rámec potřebný pro to, aby tyto pokročilé služby mohly vzkvétat na sítích 5G.

## Klíčové vlastnosti

- Kompletní prostorové sledování se třemi polohovými a třemi rotačními stupni volnosti
- Požadavky na přenos s nízkou latencí pro interakci v reálném čase
- Integrace s rámcem QoS sítě 5G pro zaručený výkon
- Standardizované mediální formáty pro doručování obsahu 6DOF
- Podpora adaptivního streamování na základě predikce pohledu
- Interoperabilita mezi zařízeními a službami různých dodavatelů

## Definující specifikace

- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.929** (Rel-19) — QoE Metrics for VR Services Study

---

📖 **Anglický originál a plná specifikace:** [6DOF na 3GPP Explorer](https://3gpp-explorer.com/glossary/6dof/)
