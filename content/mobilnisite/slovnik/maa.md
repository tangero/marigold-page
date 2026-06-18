---
slug: "maa"
url: "/mobilnisite/slovnik/maa/"
type: "slovnik"
title: "MAA – MBMS-Aware Application"
date: 2025-01-01
abbr: "MAA"
fullName: "MBMS-Aware Application"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/maa/"
summary: "Aplikace, která je speciálně navržená k využití a interakci s možnostmi služby Multimedia Broadcast Multicast Service (MBMS) sítě 3GPP. Využívá vysílání (broadcast/multicast) pro efektivní distribuci"
---

MAA je aplikace speciálně navržená k využití a interakci s možnostmi služby Multimedia Broadcast Multicast Service (MBMS) sítě 3GPP za účelem využití vysílání (broadcast/multicast) pro doručování obsahu.

## Popis

Aplikace s podporou [MBMS](/mobilnisite/slovnik/mbms/) (MBMS-Aware Application, MAA) je klientská nebo serverová aplikace, která má vnitřní znalost a rozhraní pro rámec služby Multimedia Broadcast Multicast Service (MBMS) 3GPP. Na rozdíl od běžných aplikací používajících jednosměrná (unicast) spojení je MAA navržena k vyžádání, přijetí a zpracování obsahu doručovaného prostřednictvím vysílacích (broadcast) nebo skupinových (multicast) přenosů MBMS. Tato podpora umožňuje aplikaci optimalizovat své chování pro scénáře vysílání, jako je zpracování oznámení služeb, správa relací doručování souborů a poskytování uživatelského rozhraní pro výběr vysílacích služeb.

Z architektonického hlediska se MAA nachází na uživatelském zařízení (UE) nebo potenciálně na síťovém serveru. Na UE komunikuje s middlewarem klienta MBMS, který sám komunikuje se zásobníkem protokolů 3GPP (včetně vrstev specifických pro MBMS), aby přijímal řídicí a uživatelská data MBMS. MAA používá standardizovaná aplikační programová rozhraní ([API](/mobilnisite/slovnik/api/)) nebo dodržuje specifické postupy definované ve specifikacích 3GPP k vyhledání dostupných služeb MBMS, přihlášení se k nim a následnému přijímání vysílacích datových toků. Musí rozumět popisům relací MBMS (např. poskytovaným přes [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) nebo [RTP](/mobilnisite/slovnik/rtp/)) a může implementovat opravu chyb na aplikační vrstvě ([FEC](/mobilnisite/slovnik/fec/)) nebo procedury opravy souborů s využitím komplementárních jednosměrných přenosů, pokud to služba definuje.

Jak funguje, zahrnuje několik kroků. Nejprve MAA typicky přistupuje k popisu uživatelské služby MBMS ([USD](/mobilnisite/slovnik/usd/)), který obsahuje seznam dostupných vysílacích služeb. Po výběru uživatele aplikace spustí proces připojení UE k příslušné skupinové skupině MBMS a aktivaci potřebných rádiových přenosů. Jak přicházejí vysílací data, MAA je zpracovává – to může zahrnovat dekódování videoproudu, opětovné sestavení souborů nebo prezentaci živého obsahu. Klíčovým aspektem je její schopnost zvládnout inherentně jednosměrnou povahu vysílání; pro interaktivní funkce nebo obnovu ztracených paketů může MAA iniciovat samostatné jednosměrné spojení (proces známý jako „carousel“ nebo „repair“ tok). Jejím úkolem je překlenout propast mezi efektivním mechanismem vysílání sítě a uživatelským zážitkem ze služby, což umožňuje aplikace jako živé [TV](/mobilnisite/slovnik/tv/), výstrahy pro veřejnou bezpečnost a bezdrátové aktualizace softwaru.

## K čemu slouží

Koncept MAA byl zaveden, aby plně využil výhod MBMS, které bylo navrženo jako technologie pro zvýšení efektivity sítě při doručování oblíbeného obsahu mnoha uživatelům současně. Před standardizací MAA byly aplikace z velké části nezávislé na základní metodě doručování (unicast vs. broadcast). To znamenalo, že i když síť MBMS nasadila, aplikace nemohly optimálně využít její funkce, jako je vyhledávání služeb, režimy příjmu šetřící energii nebo integrované protokoly pro doručování souborů, což omezovalo přijetí a uživatelský zážitek.

Její vytvoření řeší problém integrace na aplikační vrstvě se službou přenosu MBMS. Síť MBMS může efektivně doručovat obsah, ale bez „podporující“ aplikace nemůže UE službu řádně objevit, připojit se k ní nebo ji zobrazit. MAA poskytuje standardizovaný model pro vývojáře aplikací k vytváření služeb, které jsou od počátku kompatibilní s vysílacím doručováním. To bylo motivováno potřebou učinit z MBMS životaschopnou platformu pro komerční a služby kritické z hlediska mise, jako je mobilní TV, skupinová komunikace (GCSE) a zprávy V2X, kde je efektivní hromadná distribuce zásadní. Řeší omezení spočívající v existenci výkonné vysílací síťové vrstvy bez odpovídajícího aplikačního rámce pro její efektivní využití.

## Klíčové vlastnosti

- Schopnost vyhledávat a zpracovávat popisy uživatelských služeb MBMS (USD) pro prezentaci dostupných vysílacích služeb
- Rozhraní s middlewarem klienta MBMS na UE pro aktivaci/deaktivaci přenosů MBMS
- Zpracovává obsah doručovaný prostřednictvím vysílacích/skupinových protokolů MBMS (např. FLUTE, RTP)
- Podporuje mechanismy obnovy chyb na aplikační úrovni, případně s využitím jednosměrných opravných toků
- Může poskytovat uživatelská rozhraní pro výběr a ovládání služeb specifických pro vysílací služby
- Může implementovat strategie úspory energie sladěné s plánováním MBMS (např. MBSFN podrámce)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming

---

📖 **Anglický originál a plná specifikace:** [MAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/maa/)
