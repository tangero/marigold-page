---
slug: "pvr"
url: "/mobilnisite/slovnik/pvr/"
type: "slovnik"
title: "PVR – Persona Video Recorder"
date: 2025-01-01
abbr: "PVR"
fullName: "Persona Video Recorder"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pvr/"
summary: "Persona Video Recorder (PVR) je servisní funkce umožňující uživatelům zaznamenávat, ukládat a spravovat živě vysílaný televizní obsah na síťovém serveru nebo uživatelském zařízení. Poskytuje posunuté"
---

PVR je servisní funkce, která umožňuje uživatelům zaznamenávat, ukládat a spravovat živě vysílaný televizní obsah na síťovém serveru nebo zařízení pro posunuté sledování (time-shifted viewing) a osobní video knihovny.

## Popis

Persona Video Recorder (PVR), standardizovaný 3GPP, je servisní schopnost pro multimediální vysílací a skupinové služby, jako je [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) a jeho vylepšená forma eMBMS. V zásadě odděluje spotřebu vysílaného obsahu od jeho živého přenosového plánu. Na rozdíl od tradičního vysílání, kde je obsah sledován v reálném čase, umožňuje PVR síti nebo uživatelskému zařízení (UE) zaznamenávat vysílací proudy pro pozdější přehrávání. Tato funkčnost může být implementována ve dvou hlavních architektonických modelech: síťový PVR (nPVR) a klientský PVR (cPVR).

V modelu síťového PVR (nPVR) je funkce záznamu umístěna v rámci infrastruktury vysílací sítě. Síťový server, často součást Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), zaznamenává vysílaný obsah při jeho doručování vzduchem. Odběratelé pak mohou k tomuto zaznamenanému obsahu přistupovat na vyžádání prostřednictvím jednosměrného přenosu (unicast delivery, např. přes IMS). Tento model odlehčuje požadavky na úložiště na straně UE a umožňuje poskytovatelům služeb nabízet jednotnou službu 'catch-up [TV](/mobilnisite/slovnik/tv/)'. Model klientského PVR (cPVR) dává samotnému UE možnost zaznamenávat vysílací proud přímo do svého lokálního úložiště. UE se naladí na vysílací kanál a zaznamená transportní proud, přičemž úložiště a přehrávání spravuje lokálně. To dává uživatelům přímou kontrolu nad jejich osobním plánem záznamu a knihovnou.

Technický provoz zahrnuje signalizaci mezi servisní aplikací, vysílací sítí a UE. Oznámení služby (service announcements) informují UE o vysílacích plánech a mohou obsahovat metadata udávající, zda je záznam povolen autorskými právy k obsahu. Pro síťový PVR je záznam spouštěn a spravován poskytovatelem služby. Pro klientský PVR záznam zpracovává mediální klientská aplikace v UE na základě uživatelských preferencí. Mezi klíčové zapojené protokoly patří [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) pro doručování souborů přes vysílání a [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/) pro získávání obsahu nPVR na vyžádání. Služba PVR se integruje se systémy správy digitálních práv ([DRM](/mobilnisite/slovnik/drm/)) za účelem vynucení povolení k záznamu, počtu přehrání a doby uložení, čímž zajišťuje soulad s licenčními smlouvami k obsahu.

## K čemu slouží

Funkce PVR byla zavedena za účelem modernizace a zvýšení hodnoty služeb 3GPP vysílání, aby byly konkurenceschopné vůči tradiční kabelové/satelitní TV a internetovým streamovacím službám. Před PVR byl MBMS primárně čistě živým vysílacím médiem, což omezovalo jeho atraktivitu, protože uživatelé museli být přítomni v čase vysílání. To bylo významné omezení ve srovnání s jednosměrnými službami videa na vyžádání (unicast video-on-demand). Schopnost PVR tento problém přímo řeší přidáním funkce časového posunu (time-shift).

Její vytvoření bylo motivováno potřebou zvýšit adopci mobilních vysílacích služeb u odběratelů a zlepšit uživatelský zážitek. Řeší problém dostupnosti obsahu, protože umožňuje uživatelům sledovat pořady dle jejich vlastního pohodlí. Dále umožňuje poskytovatelům služeb nabízet nové funkce, jako je 'start-over' (restart živého programu od začátku) a 'pozastavení živého TV vysílání', které jsou nyní očekávanými funkcemi moderních TV služeb. Z pohledu efektivity sítě může být nPVR také strategický; populární obsah zaznamenaný jednou na okraji sítě může být efektivně doručován jednosměrným přenosem mnoha uživatelům, čímž se snižuje opakovaný vysílací přenos pro obsah typu catch-up. Přemosťuje tak mezeru mezi efektivním vysílacím doručováním a flexibilními způsoby spotřeby, které uživatelé požadují.

## Klíčové vlastnosti

- Umožňuje posunuté sledování (time-shifted viewing) živě vysílaného obsahu
- Podporuje jak síťovou (nPVR), tak klientskou (cPVR) architekturu záznamu
- Integruje se s oznámením služby (service announcement) a elektronickým průvodcem službami (ESG) pro plány záznamu
- Spolupracuje se systémy DRM pro vynucení práv k záznamu a použití obsahu
- Umožňuje funkce jako pozastavení/obnovení živého TV vysílání a osobní video knihovny
- Může doručovat zaznamenaný obsah prostřednictvím jednosměrného přenosu (pro nPVR) nebo přehráváním z lokálního úložiště (pro cPVR)

## Související pojmy

- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [DRM – Data call Routeing Mechanism](/mobilnisite/slovnik/drm/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [PVR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pvr/)
