---
slug: "sofa"
url: "/mobilnisite/slovnik/sofa/"
type: "slovnik"
title: "SOFA – Spatially Oriented Format for Acoustics"
date: 2025-01-01
abbr: "SOFA"
fullName: "Spatially Oriented Format for Acoustics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sofa/"
summary: "Standardizovaný 3GPP audio formát určený pro imerzivní prostorové zvukové zážitky, například v rozšířené realitě (AR) a virtuální realitě (VR). Definuje souborový formát a mechanismus pro přenos audio"
---

SOFA je standardizovaný 3GPP audio formát pro imerzivní prostorový zvuk, který definuje souborový formát a mechanismus pro přenos audio objektů s prostorovými metadaty za účelem vytvoření dynamických 3D zvukových scén.

## Popis

Spatially Oriented Format for Acoustics (SOFA) je technická specifikace vyvinutá 3GPP (primárně v TS 26.118) pro přenos dat prostorového zvuku. Na rozdíl od tradičního kanálového (např. stereo, 5.1) nebo scénového (např. Ambisonics) zvuku je SOFA objektový audio formát. Zapouzdřuje jednotlivé audio objekty, z nichž každý se skládá z audio esence (zvukového signálu) a přidružených prostorových metadat, která popisují polohu, orientaci a další akustické vlastnosti objektu v trojrozměrném souřadnicovém systému. Toto oddělení audio esence od metadat pro vykreslování je klíčovým architektonickým principem.

Jak SOFA funguje, zahrnuje fáze tvorby obsahu, přenosu a přehrávání. Při tvorbě se audio objekty vytvářejí včetně jejich prostorových trajektorií. Formát SOFA zabalí tyto objekty do strukturovaného souboru nebo streamovacího formátu. Specifikace definuje syntaxi pro ukládání audio dat (např. [PCM](/mobilnisite/slovnik/pcm/) kodek) a metadat založených na [XML](/mobilnisite/slovnik/xml/). Při přenosu přes síť lze formát přizpůsobit nebo částečně doručit na základě síťových podmínek nebo možností zařízení. V přehrávacím zařízení přijímá renderer SOFA audio objekty a metadata. Základní funkcí rendereru je syntéza konečného binaurálního nebo vícekanálového výstupu na základě *aktuální* polohy a orientace posluchače, které jsou typicky poskytovány v reálném čase senzory pro sledování polohy hlavy v [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/) headsetech. To umožňuje, aby zvuková scéna zůstala stabilní vůči virtuálnímu světu, i když uživatel pohybuje hlavou.

Úloha SOFA v ekosystému 3GPP spočívá v poskytnutí standardizovaného, interoperabilního formátu pro imerzivní audio služby v rámci aplikací bohatých na média, jako je VR telefonie, AR vzdálená asistence a 360stupňové video. Je součástí širší pracovní položky 3GPP Media Streaming (4G/5G Media). Specifikace podrobně popisuje profily a úrovně pro zajištění interoperability, definuje podmnožiny funkcí pro zařízení s různou složitostí. Rovněž specifikuje, jak lze obsah SOFA doručovat pomocí Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), čímž jej sladí s rámcem pro doručování médií od 3GPP.

## K čemu slouží

SOFA byla vytvořena, aby vyřešila nedostatek standardizovaného, efektivního formátu pro prostorový zvuk v mobilním a streamovacím kontextu, zejména pro nově vznikající [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/) aplikace. Předchozí přístupy k 3D zvuku, jako je Ambisonics vysokého řádu nebo vícekanálový zvuk, byly buď výpočetně náročné, nedokázaly se dynamicky přizpůsobit pohybu posluchače, nebo vyžadovaly pevné uspořádání reproduktorů, což je činilo nevhodnými pro personalizované zážitky se sledováním hlavy na mobilních zařízeních. Problémem bylo doručení přesvědčivého, imerzivního zvukového zážitku, který je pro pocit přítomnosti ve virtuálních prostředích stejně kritický jako vizuální ponoření.

Motivace pro její standardizaci v rámci 3GPP vycházela z pohybu průmyslu směrem k imerzivním médiím využívajícím 5G. Vysoká šířka pásma a nízká latence 5G jsou hybateli bohatého streamování médií, ale bez standardního audio formátu by došlo k fragmentaci. SOFA to řeší tím, že poskytuje objektový formát, který je efektivní z hlediska šířky pásma (přenášejí se pouze nezbytné objekty) a nezávislý na vykreslování (stejný obsah lze optimálně vykreslit na různých výstupních zařízeních, od sluchátek po reproduktorová pole). Odstraňuje tak omezení kanálového zvuku, který je vázán na konkrétní konfiguraci přehrávání, a poskytuje větší flexibilitu a interaktivitu než statické binaurální nahrávky. Její vznik byl hnán potřebou zajistit interoperabilitu mezi tvůrci obsahu, síťovými streamovacími službami a koncovými uživatelskými zařízeními v prostředí médií 5G.

## Klíčové vlastnosti

- Objektový formát prostorového zvuku oddělující audio esenci od prostorových metadat.
- Metadata založená na XML definující 3D polohu, orientaci a akustické vlastnosti audio objektů.
- Podpora dynamického přizpůsobení zvukové scény v reálném čase na základě sledování polohy hlavy posluchače.
- Navrženo pro efektivní streamování a adaptaci pomocí DASH (Dynamic Adaptive Streaming over HTTP).
- Definuje interoperabilní profily a úrovně pro různorodé možnosti zařízení.
- Umožňuje imerzivní audio zážitky pro služby AR, VR a 360stupňového videa.

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [SOFA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sofa/)
