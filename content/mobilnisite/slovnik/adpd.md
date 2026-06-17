---
slug: "adpd"
url: "/mobilnisite/slovnik/adpd/"
type: "slovnik"
title: "ADPD – Associated Delivery Procedure Description"
date: 2025-01-01
abbr: "ADPD"
fullName: "Associated Delivery Procedure Description"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adpd/"
summary: "ADPD je strukturovaný popis používaný v MBMS (Multimedia Broadcast/Multicast Service) od 3GPP k definici postupu doručování přidruženého obsahu. Specifikuje, jak jsou pomocná data, jako titulky nebo m"
---

ADPD je strukturovaný popis používaný v MBMS od 3GPP k definici postupu doručování pomocného obsahu, který zajišťuje jeho synchronizaci a doručení spolu s hlavními mediálními proudy.

## Popis

Associated Delivery Procedure Description (ADPD, popis postupu přidruženého doručení) je klíčovou součástí architektury služby [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast/Multicast Service) od 3GPP, konkrétně definovanou pro doručování služeb založených na File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)) a Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Funguje jako kontejner metadat, který popisuje způsob doručení, časování a vztah přidruženého obsahu – jako jsou titulky, skryté titulky, audiopopisy, aplikační data nebo časovaná metadata – k hlavní mediální prezentaci. ADPD je typicky přenášen v rámci Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) pro streamování založené na DASH nebo v rámci File Delivery Table ([FDT](/mobilnisite/slovnik/fdt/)) pro doručování souborů založené na FLUTE, čímž poskytuje klientovi potřebné instrukce ke správnému získání a synchronizaci pomocných dat.

Architektonicky ADPD funguje na aplikační vrstvě přenosové služby MBMS. Je generován poskytovatelem služby nebo Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a doručen do User Equipment (UE) jako součást oznámení služby nebo v rámci probíhající doručovací relace. Samotný popis je struktura založená na XML, která odkazuje na umístění přidruženého obsahu (např. URL nebo identifikátor souboru) a definuje klíčové parametry doručení. Mezi tyto parametry patří typ postupu doručení (např. DASH Segment, FLUTE File nebo HTTP-URL), volitelné informace o šířce pásma a především časové informace, které propojují doručení a dostupnost přidruženého obsahu s časovou osou mediální prezentace hlavní služby.

Základní technická operace zahrnuje parsování ADPD v UE po přijetí popisu služby. Na základě typu postupu klient inicializuje příslušný protokolový zásobník – jako je FLUTE nebo HTTP – k získání popsaných obsahových objektů. Pro synchronizované doručení ADPD používá konstrukty jako `availabilityStartTime` a `availabilityEndTime` zarovnané s časovou osou hlavního média, což zajišťuje, že titulky nebo metadata jsou dostupné přesně v okamžiku, kdy jsou potřeba pro přehrávání. Tím je odděleno doručení přidruženého obsahu od streamování hlavního média v reálném čase, což umožňuje efektivní opakování založené na karuselu ve vysílacích scénářích nebo na vyžádání v režimech unicastového záložního přenosu, při zachování přísných požadavků na synchronizaci.

Jeho úlohou v síti je umožnit bohaté, přístupné a interaktivní vysílací/multicastové služby bez zatížení hlavního mediálního proudu. Poskytnutím standardizovaného deklarativního popisu umožňuje různým implementacím klientů jednotně zpracovávat pomocný obsah. To zjednodušuje tvorbu služeb pro poskytovatele a zaručuje konzistentní uživatelský zážitek. ADPD je základním prvkem pro umožnění služeb, jako je přístupné vysílání (pro uživatele s postižením), rozšířená TV se synchronizovanými aplikacemi a doručování průvodce službou nebo dat tísňového varování spolu s video a audio proudy.

## K čemu slouží

ADPD bylo vytvořeno, aby řešilo rostoucí potřebu doručování synchronizovaného pomocného obsahu v rámci se vyvíjejících vysílacích a multicastových rámců 3GPP, především [MBMS](/mobilnisite/slovnik/mbms/) a jeho evoluce do Enhanced Multimedia Broadcast Multicast Service (eMBMS). Před jeho standardizací bylo doručování časovaných metadat, titulků nebo interaktivních aplikačních dat spolu s hlavním mediálním proudem ve vysílacím prostředí často řešeno proprietárními nebo ad-hoc metodami. To vedlo k problémům s interoperabilitou, zvýšené složitosti klienta a neefektivnímu využití vysílacích zdrojů, protože logika doručení přidruženého obsahu byla pevně zakódována nebo špatně definována.

Zavedení ADPD ve verzi 12 (Release 12) poskytlo standardizované, flexibilní a deklarativní řešení. Bylo motivováno posunem průmyslu k IP-bázenému doručování médií (jako je DASH) a požadavkem na bohaté mediální služby, včetně těch povinných pro přístupnost (např. skryté titulky). Základní problém, který řeší, je efektivní a synchronizované doručení nespojitého, často přerušovaného přidruženého obsahu v rámci spojitého vysílacího nebo multicastového proudu. Umožňuje poskytovatelům služeb popsat *jak* a *kdy* je tento pomocný obsah doručován odděleně od hlavního média, což klientům umožňuje jej získávat právě včas, a tím optimalizovat šířku pásma a úložiště na UE.

Historicky, bez ADPD, mohl být přidružený obsah vložen do mediálního kontejneru (což zvyšovalo složitost a omezovalo flexibilitu) nebo doručován na samostatném nesynchronizovaném kanálu. Účelem ADPD je oddělit popis doručení od kódování média a poskytnout síťově agilní metodu. To bylo zvláště kritické pro nasazení eMBMS zaměřená na podporu mobilní TV, komunikací pro veřejnou bezpečnost a aktualizací softwaru přes vysílání, kde přidružená data (jako tísňová varování nebo metadata služby) musí být spolehlivě a včas doručena synchronně s primárním obsahem bez ohledu na síťové podmínky nebo stav klienta.

## Klíčové vlastnosti

- Deklarativní popis založený na XML pro postupy doručení
- Podporuje více doručovacích protokolů včetně FLUTE, DASH Segments a HTTP-URL
- Definuje přesnou časovou synchronizaci s časovou osou prezentace hlavního média
- Umožňuje efektivní doručování přidruženého obsahu pro vysílání založené na karuselu
- Usnadňuje doručování funkcí přístupnosti, jako jsou titulky a audiopopisy
- Umožňuje specifikaci šířky pásma pro doručení přidruženého obsahu

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview

---

📖 **Anglický originál a plná specifikace:** [ADPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/adpd/)
