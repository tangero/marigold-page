---
slug: "3dof"
url: "/mobilnisite/slovnik/3dof/"
type: "slovnik"
title: "3DOF – Three Degrees of Freedom"
date: 2025-01-01
abbr: "3DOF"
fullName: "Three Degrees of Freedom"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/3dof/"
summary: "3DOF označuje základní úroveň prostorového zvukového a vizuálního ponoření v mediálních službách, typicky podporující rotaci hlavy (odchylku, náklon, převýšení) bez sledování polohy. Umožňuje počátečn"
---

3DOF je základní úroveň prostorového ponoření v mediálních službách, která podporuje sledování rotace hlavy, nikoliv však pohyb polohy, a umožňuje zážitky jako 360stupňové video v rámci standardů 3GPP.

## Popis

V rámci ekosystému 3GPP definuje 3DOF (Three Degrees of Freedom, tři stupně volnosti) schopnost mediální služby doručovat imerzivní audiovizuální obsah, kde se pohledový úhel spotřebitele může otáčet ve třech úhlových dimenzích, ale nemůže se translačně pohybovat v rámci virtuálního prostředí. Tři rotační osy jsou odchylka (rotace doleva/doprava kolem svislé osy), náklon (rotace nahoru/dolů kolem příčné osy) a převýšení (nakláněcí rotace kolem osy vpřed/vzad). To je zásadně implementováno doručováním a vykreslováním všesměrového (360stupňového) média, kde je zachyceno nebo generováno plné sférické zorné pole a klientská aplikace nebo zařízení vykresluje pouze výřez (viewport) na základě aktuální orientace hlavy uživatele.

Technicky specifikace 3GPP, jako je TS 26.114 (Multimedia Telephony) a TS 26.118 (Immersive Telephony), definují protokoly a kodeky pro přenos 3DOF médií. Obsah je typicky kódován pomocí projekčních formátů, jako je ekvidistantní válcová projekce ([ERP](/mobilnisite/slovnik/erp/)) nebo krychlová projekce ([CMP](/mobilnisite/slovnik/cmp/)), pro mapování sférického videa na 2D rovinu za účelem komprese standardními videokodeky jako [HEVC](/mobilnisite/slovnik/hevc/) nebo [VVC](/mobilnisite/slovnik/vvc/). Přidružený prostorový zvuk je definován ve specifikacích jako TS 26.918 ([XR](/mobilnisite/slovnik/xr/) Media) tak, aby odpovídal vizuálnímu pohledovému úhlu, často s využitím formátů jako scénový zvuk (např. Higher Order Ambisonics - [HOA](/mobilnisite/slovnik/hoa/)) nebo objektový zvuk s přidruženými metadaty. Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) v [DASH](/mobilnisite/slovnik/dash/) (Dynamic Adaptive Streaming over HTTP) je rozšířena pro signalizaci charakteristik 3DOF, což umožňuje adaptivní streamování segmentů různé kvality pro různé prostorové oblasti (viewport-dependent streaming) za účelem optimalizace šířky pásma.

Architektura zahrnuje 3DOF mediální server, který ukládá a streamuje promítané video a prostorové zvukové asety, a 3DOF klienta, kterým může být smartphone v head-mounted prohlížeči nebo samostatné VR zařízení se senzory orientace. Klient dekóduje video, extrahuje příslušný výřez na základě vstupu ze senzorů v reálném čase pro orientaci hlavy a vykreslí jej na displeji. Zvukový vykreslovač používá hlavou přenášené přenosové funkce (HRTF) pro binaurální vykreslení prostorové zvukové scény odpovídající aktuální orientaci hlavy. Mezi klíčové síťové komponenty patří rámec 5G Media Streaming (5GMS), který využívá schopnosti sítě 5G, jako je vysoká propustnost a nízká latence, k zajištění plynulého a kvalitního zážitku ze streamování 3DOF bez zpoždění způsobujícího nevolnost.

Role 3DOF spočívá v poskytování vstupní úrovně imerzivní mediální služby v rámci širšího kontinua rozšířené reality (XR) definovaného 3GPP. Poskytuje základní uživatelský zážitek a technický rámec, na kterém jsou budovány složitější služby jako 6DOF (Six Degrees of Freedom). Je klíčová pro aplikace jako virtuální cestovní ruch, základní tréninkové simulace a 360stupňové živé události, kde není vyžadána plná polohová volnost, ale je žádoucí pocit přítomnosti.

## K čemu slouží

3DOF bylo zavedeno za účelem standardizace doručování základního imerzivního média přes mobilní sítě v reakci na tržní nástup dostupných VR prohlížečů a 360stupňových kamer. Před standardizací 3GPP existovala proprietární řešení pro streamování 360stupňového videa, což vedlo k fragmentaci, problémům s interoperabilitou a neefektivnímu využití síťových zdrojů. Nedostatek jednotného přístupu bránil širokému nasazení služeb ze strany operátorů a poskytovatelů obsahu. Práce 3GPP si kladla za cíl vytvořit škálovatelný, adaptivní a kvalitně řízený ekosystém pro imerzivní média s využitím stávajících multimediálních rámců jako DASH a jejich rozšířením o prostorové charakteristiky.

Primární problém, který 3DOF řeší, je umožnění přesvědčivého, standardizovaného imerzivního zážitku v rámci omezení současného spotřebitelského hardwaru (kterému často chybí sledování polohy) a šířky pásma mobilní sítě. Umožňuje operátorům nabízet nové mediální služby, které přesahují tradiční ploché video, a vytvářet tak nové zdroje příjmů v zábavě, vzdělávání a podnikové sféře. Definováním efektivních projekčních a kompresních metod spolu s adaptivním streamováním podle výřezu řeší významnou výzvu šířky pásma 360stupňového videa (které vyžaduje 4-6krát více pixelů než standardní HD výřez), aniž by bylo nutné, aby spotřebitelé stahovali celou sféru v ultra vysokém rozlišení a plné kvalitě.

Historicky představuje 3DOF první krok ve formalizaci XR služeb 3GPP, zahájený ve vydání 15 spolu s ranými nasazeními 5G. Bylo motivováno potřebou demonstrovat hodnotu 5G nad rámec vylepšeného mobilního širokopásmového přístupu a ukázat jeho schopnost podporovat nové mediální formáty vyžadující vysoké datové toky a konzistentní kvalitu. Zavedením 3DOF poskytlo 3GPP jasnou evoluční cestu od tradičních médií k plně interaktivní XR s 6DOF, což umožnilo průmyslu vyvíjet a nasazovat služby postupně, zatímco se nadále rozvíjely základní schopnosti zařízení a síťové optimalizace (jako edge computing pro složitější vykreslování).

## Klíčové vlastnosti

- Podporuje tři rotační pohyby (odchylka, náklon, převýšení) pro ovládání pohledového úhlu
- Využívá sférické videoprojekční formáty (např. ERP, CMP) pro efektivní kódování a ukládání
- Umožňuje adaptivní streamování podle výřezu pro optimalizaci šířky pásma doručováním vyšší kvality pouze do aktuálního zorného pole uživatele
- Integruje formáty prostorového zvuku synchronizované s orientací vizuálního pohledového úhlu
- Využívá standardizovaný rámec 5G Media Streaming (5GMS) pro doručování a zajištění kvality
- Poskytuje základní metadata a signalizaci v DASH MPD pro adaptivní přehrávání imerzivního obsahu řízené klientem

## Související pojmy

- [6DOF – Six Degrees of Freedom](/mobilnisite/slovnik/6dof/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.929** (Rel-19) — QoE Metrics for VR Services Study

---

📖 **Anglický originál a plná specifikace:** [3DOF na 3GPP Explorer](https://3gpp-explorer.com/glossary/3dof/)
