---
slug: "oba"
url: "/mobilnisite/slovnik/oba/"
type: "slovnik"
title: "OBA – Object-Based Audio"
date: 2025-01-01
abbr: "OBA"
fullName: "Object-Based Audio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oba/"
summary: "Object-Based Audio je mediální služba, která reprezentuje zvukové scény jako kolekci jednotlivých zvukových objektů s přidruženými metadaty, nikoli jako tradiční kanálové mixy. Umožňuje imerzivní, per"
---

OBA (objektové audio) je zvuková služba, která scény reprezentuje jako jednotlivé zvukové objekty s metadaty, což umožňuje imerzivní a personalizované zážitky, jako jsou 3D zvukové krajiny.

## Popis

Object-Based Audio (OBA) představuje zásadní posun v reprezentaci a distribuci zvuku, standardizovaný 3GPP pro mediální služby. Na rozdíl od tradičního kanálového zvuku (např. stereo nebo 5.1 surround), který kóduje zvuk pro pevné pozice reproduktorů, OBA rozkládá zvukovou scénu na diskrétní 'objekty'. Každý objekt je zvukový signál (např. stopa dialogu, zvukový efekt nebo ambientní hudba) doprovázený bohatými, časově proměnnými metadaty. Tato metadata popisují prostorovou polohu objektu (souřadnice v 3D prostoru), zesílení a další percepční atributy, což umožňuje dynamický rendering. Architektura zahrnuje fázi tvorby obsahu, kde jsou zvukové objekty a metadata vytvářeny, fázi distribuce, kde jsou efektivně kódovány a přenášeny (často s využitím kodeků jako MPEG-H 3D Audio), a fázi renderování na straně klienta. Renderer na základě metadat a možností přehrávacího zařízení (od sluchátek po komplexní soustavy reproduktorů) syntetizuje konečný zvukový výstup v reálném čase. Toto oddělení obsahu od prezentačního formátu je zásadní. V kontextu sítě specifikace 3GPP definují, jak jsou služby OBA doručovány přes mobilní sítě, včetně signalizace, mediálních formátů a aspektů kvality služby (QoS) pro zajištění synchronizovaného doručení zvukových objektů a jejich metadat pro bezproblémový zážitek. Jejím úkolem je poskytnout budoucím médiím odolný zvukový základ, který umožňuje funkce nedosažitelné s pevným kanálovým zvukem.

## K čemu slouží

OBA byla vytvořena, aby řešila omezení kanálového zvuku v kontextu vývoje spotřeby médií. Tradiční zvukové mixy jsou 'pečené' pro konkrétní konfiguraci reproduktorů a nenabízejí flexibilitu pro různá poslechová prostředí (např. sluchátka vs. soundbar), uživatelské preference nebo potřeby dostupnosti. Vzestup virtuální reality ([VR](/mobilnisite/slovnik/vr/)), rozšířené reality ([AR](/mobilnisite/slovnik/ar/)) a interaktivních médií vyžadoval zvuk, který by se mohl dynamicky přizpůsobovat pohybům hlavy uživatele a interaktivitě. OBA to řeší poskytnutím flexibilního přístupu založeného na popisu scény. Umožňuje personalizovaný zvuk, jako je nezávislé nastavení hlasitosti dialogu od pozadí hudby, nebo plynulou integraci stop s audio popisem. Z pohledu sítě a poskytovatele služeb také nabízí efektivitu; jediný proud OBA může být přizpůsoben mnoha výstupním zařízením, což snižuje potřebu ukládat a přenášet více kanálových verzí. Jeho zavedení v 3GPP Rel-14 bylo motivováno posunem průmyslu k standardům imerzivních médií a potřebou telekomunikačních sítí podporovat zvukové služby nové generace jako součást vylepšené služby Multimedia Broadcast/Multicast Service (eMBMS) a streamovacích nabídek.

## Klíčové vlastnosti

- Rozkládá zvuk na diskrétní objekty s přidruženými metadaty
- Umožňuje dynamický, reálný rendering přizpůsobený přehrávacímu zařízení
- Podporuje 3D prostorové umístění zvuku pro imerzivní zážitky
- Umožňuje uživatelskou interaktivitu a personalizaci (např. ovládání zesílení objektu)
- Poskytuje základ pro funkce dostupnosti, jako je audio popis
- Efektivně distribuuje jediný proud přizpůsobitelný více výstupním formátům

## Definující specifikace

- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [OBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/oba/)
