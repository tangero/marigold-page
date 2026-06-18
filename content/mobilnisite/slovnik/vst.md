---
slug: "vst"
url: "/mobilnisite/slovnik/vst/"
type: "slovnik"
title: "VST – Virtual Studio Technology"
date: 2025-01-01
abbr: "VST"
fullName: "Virtual Studio Technology"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vst/"
summary: "Soubor specifikací 3GPP pro vytváření a poskytování imerzivních mediálních zážitků, jako je volumetrické video a rozšířená realita (XR). Umožňuje snímání, zpracování, streamování a vykreslování obsahu"
---

VST je soubor specifikací 3GPP pro vytváření a poskytování imerzivních médií, jako je volumetrické video a XR, umožňující jejich snímání, zpracování, streamování a vykreslování přes sítě 5G.

## Popis

Virtual Studio Technology (VST) je komplexní rámec definovaný 3GPP pro standardizaci produkce, distribuce a konzumace pokročilých imerzivních mediálních služeb přes mobilní sítě. Zahrnuje celý mediální řetězec od tvorby obsahu po jeho prezentaci uživateli. V jádru se VST zabývá volumetrickými médii – reprezentacemi scén nebo objektů jako 3D modelů nebo mračen bodů – a přidruženými metadaty, což umožňuje zážitky se šesti stupni volnosti (6DoF), kde uživatelé mohou interaktivně měnit svůj úhel pohledu. Architektura zahrnuje několik klíčových komponent: systémy pro snímání (např. rigy s více kamerami), funkce pro zpracování médií pro kódování a balení, síť pro doručování médií a vykreslovací enginy na straně klienta na zařízeních, jako jsou [XR](/mobilnisite/slovnik/xr/) headset nebo chytré telefony.

Technicky VST specifikuje, jak jsou volumetrická data formátována, komprimována a přenášena. Využívá stávající i nové mediální kodeky, jako jsou ty pro kompresi mračen bodů ([PCC](/mobilnisite/slovnik/pcc/)), a definuje přenosové protokoly optimalizované pro nízkou latenci a vysokou spolehlivost, což je klíčové pro interaktivní a živé zážitky. Média jsou často balena pomocí standardů jako [MPEG](/mobilnisite/slovnik/mpeg/) Media Transport ([MMT](/mobilnisite/slovnik/mmt/)) nebo Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), se specifickými úpravami pro časovaná metadata popisující polohy kamer a geometrii scény. VST server orchestruje relaci, spravuje synchronizaci více mediálních streamů (např. video, audio, haptika) a přizpůsobuje doručování na základě síťových podmínek a možností klienta.

V rámci systému 5G VST využívá síťové schopnosti jako edge computing (Multi-access Edge Computing, [MEC](/mobilnisite/slovnik/mec/)) k přesunutí náročného zpracování, jako je vykreslování v reálném čase nebo kompozice scény, blíže k uživateli, čímž se snižuje celková latence. Mechanismy Quality of Service (QoS) zajišťují vysokou šířku pásma a nízké zpoždění vyžadované pro imerzivní média. VST také definuje [API](/mobilnisite/slovnik/api/) pro vyhledávání služeb, správu relací a interakci uživatele, což umožňuje hladkou integraci s funkcemi jádra sítě 5G. Jeho úlohou je poskytnout interoperabilní ekosystém pro tvůrce obsahu, síťové operátory a výrobce zařízení, aby mohli nasazovat imerzivní služby ve velkém měřítku a využívat vysokou propustnost a nízkou latenci sítí 5G.

## K čemu slouží

VST bylo vytvořeno, aby vyřešilo nedostatek standardizace pro poskytování imerzivních médií nové generace, jako je volumetrické video a rozšířená realita (XR), přes telekomunikační sítě. Před jeho specifikací vedly proprietární řešení pro snímání, streamování a vykreslování takového obsahu k fragmentaci, což bránilo širokému přijetí a interoperabilitě. Vzestup 5G s jeho vylepšenými schopnostmi Enhanced Mobile Broadband (eMBB) a Ultra-Reliable Low-Latency Communications (URLLC) poskytl katalyzátor, protože nabídl potřebný výkon sítě, ale vyžadoval standardizované zpracování médií k odemknutí nových spotřebitelských a podnikových služeb.

Tato technologie řeší klíčové problémy při produkci a distribuci imerzivního obsahu ve velkém měřítku. Umožňuje efektivní kompresi a streamování rozsáhlých volumetrických datových sad, zvládá složitost synchronizace více streamů pro zážitky 6DoF a definuje, jak mohou sítě optimalizovat doručování pomocí edge computingu a síťového řezání. VST bylo motivováno poptávkou od vysílatelů, tvůrců obsahu a vývojářů XR aplikací po společném rámci, na kterém lze stavět, aby bylo zajištěno, že imerzivní zážitky mohou být spolehlivě doručeny masovému trhu přes 5G, což transformuje oblasti jako živá zábava, vzdálená spolupráce a interaktivní školení.

## Klíčové vlastnosti

- Standardizované snímání, kódování a streamování volumetrických médií a mračen bodů
- Podpora interaktivních zážitků prohlížení se šesti stupni volnosti (6DoF)
- Integrace se schopnostmi sítě 5G včetně edge computingu a síťového řezání
- Využití adaptivního streamování (např. DASH) s časovanými metadaty pro synchronizaci
- API pro orchestraci služeb, správu relací a interakci uživatele
- Přenosové protokoly s nízkou latencí optimalizované pro imerzivní aplikace v reálném čase

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming

---

📖 **Anglický originál a plná specifikace:** [VST na 3GPP Explorer](https://3gpp-explorer.com/glossary/vst/)
