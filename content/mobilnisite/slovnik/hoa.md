---
slug: "hoa"
url: "/mobilnisite/slovnik/hoa/"
type: "slovnik"
title: "HOA – Higher Order Ambisonics"
date: 2025-01-01
abbr: "HOA"
fullName: "Higher Order Ambisonics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hoa/"
summary: "Higher Order Ambisonics (HOA) je pokročilý prostorový audio formát pro ponořující média, který zachycuje a reprodukuje úplné 360stupňové zvukové pole. Standardizován 3GPP pro služby jako VR a AR, umož"
---

HOA (Higher Order Ambisonics) je pokročilý prostorový audio formát standardizovaný 3GPP pro zachycení a reprodukci úplného 360stupňového zvukového pole, který umožňuje ponořující, objektově založené zvukové zážitky přes mobilní sítě.

## Popis

Higher Order Ambisonics (HOA) je parametrická reprezentace zvukového pole navržená pro zachycení a reprodukci ponořujícího, trojrozměrného zvuku. Na rozdíl od kanálově založených formátů (např. surround 5.1 nebo 7.1), které přiřazují audio konkrétním umístěním reproduktorů, Ambisonics reprezentuje zvukové pole jako sadu koeficientů sférických harmonických funkcí. Tyto koeficienty matematicky popisují, jak se akustický tlak mění ve všech směrech kolem bodu v prostoru. 'Řád' (např. 1., 2., 3.) určuje prostorové rozlišení a přesnost; vyšší řády poskytují přesnější směrové a prostorové informace, jako je šířka a elevace zdrojů zvuku.

Technicky je HOA audio vytvořeno zakódováním signálů z mikrofonního pole (nebo syntetizovaných z audio objektů) do Ambisonics B-formátových kanálů. Každý kanál odpovídá specifické složce sférické harmonické funkce (např. W pro všesměrovou, X/Y/Z pro prvního řádu s charakteristikou osmičky). Pro Ambisonics N-tého řádu existuje (N+1)² kanálů. Tento zakódovaný signál je reprezentací založenou na scéně, což znamená, že je nezávislý na jakémkoli konkrétním přehrávacím systému. Pro vykreslení je HOA proud dekódován na základě cílového rozložení reproduktorů nebo binauraálně pro sluchátka, s využitím sady dekódovacích koeficientů, které promítají sférické harmonické funkce na dostupné výstupní měniče.

V rámci ekosystému 3GPP je HOA integrováno do standardů pro doručování médií, zejména pro virtuální realitu ([VR](/mobilnisite/slovnik/vr/)), rozšířenou realitu ([AR](/mobilnisite/slovnik/ar/)) a ponořující telekonference. Klíčové specifikace definují přenos a ukládání HOA obsahu, jako je jeho zapouzdření v [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) pro Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Kodeky jako MPEG-H 3D Audio podporují HOA jako vstupní formát pro kompresi a přenos. Úlohou sítě je efektivně doručovat tyto potenciálně vysokopřenosové, vícekanálové audio proudy, často synchronizované s 360stupňovým videem, což vyžaduje robustní QoS a funkce sítě s ohledem na média.

## K čemu slouží

HOA bylo standardizováno v 3GPP, aby řešilo omezení tradičních audio formátů pro nově vznikající ponořující mediální aplikace. Kanálově založený surround zvuk je vázán na pevnou, předdefinovanou konfiguraci reproduktorů a nedostatečně podporuje 360stupňovou rotaci posluchače, která je zásadní pro [VR](/mobilnisite/slovnik/vr/)/[AR](/mobilnisite/slovnik/ar/). Ambisonics prvního řádu (FOA) nabízí základní 3D audio, ale s omezeným prostorovým rozlišením a přesností, což často vede k rozmazané nebo nepřesné lokalizaci zdroje zvuku. HOA bylo zavedeno, aby tyto problémy vyřešilo, a poskytuje vysoce věrné, plnosférické audio nezbytné pro přesvědčivou přítomnost a realismus ve virtuálních prostředích.

Hnací motivací byl komerční vzestup služeb VR a 360stupňového videa, které vyžadovaly audio formát schopný odpovídat vizuálnímu ponoření. HOA umožňuje, aby zvuk zůstal stabilní a přesně umístěný vzhledem k vizuální scéně, když uživatel otáčí hlavou, což je klíčové pro udržení iluze 'být uvnitř' obsahu. Z pohledu sítě a služeb standardizace HOA zajišťuje interoperabilitu mezi nástroji pro tvorbu obsahu, kompresními kodeky, streamovacími servery a přehrávacími zařízeními, čímž předchází závislosti na dodavateli a podporuje zdravý ekosystém pro ponořující média.

Navíc je povaha HOA založená na scéně efektivnější pro interaktivní a adaptivní streamování ve srovnání s přenosem více diskrétních objektových stop. Jeden HOA proud může reprezentovat komplexní sluchovou scénu a vykreslování může být adaptováno na straně klienta na základě uživatelské interakce (pohyb hlavy) nebo možností zařízení (různé typy sluchátek), aniž by to vyžadovalo překódování nebo odesílání více audio proudů ze serveru. Tím se snižuje složitost serveru a zatížení sítě, což z něj činí škálovatelné řešení pro doručování personalizovaného ponořujícího audia přes mobilní sítě.

## Klíčové vlastnosti

- Reprezentace audia založená na scéně s využitím koeficientů sférických harmonických funkcí, nezávislá na konfiguraci přehrávacího zařízení.
- Škálovatelné prostorové rozlišení definované řádem Ambisonics (např. 1., 2., 3. řád).
- Podporuje zachycení a reprodukci úplného 360stupňového zvukového pole včetně elevace.
- Umožňuje stabilní vykreslování audia s sledováním polohy hlavy pro aplikace VR/AR.
- Standardizovaný přenos v ISOBMFF pro adaptivní streamování (DASH).
- Podpora komprese prostřednictvím pokročilých audio kodeků jako MPEG-H 3D Audio a EVS.

## Související pojmy

- [VR – Virtualized Resource](/mobilnisite/slovnik/vr/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [ISOBMFF – International Organization for Standards, Base Media File Format](/mobilnisite/slovnik/isobmff/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.865** (Rel-18) — Technical Report
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [HOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/hoa/)
