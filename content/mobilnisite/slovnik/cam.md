---
slug: "cam"
url: "/mobilnisite/slovnik/cam/"
type: "slovnik"
title: "CAM – Cooperative Awareness Message"
date: 2026-01-01
abbr: "CAM"
fullName: "Cooperative Awareness Message"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cam/"
summary: "Periodická vysílací zpráva používaná v komunikaci Vozidlo-s-vším (V2X) ke sdílení dynamického stavu vozidla (poloha, rychlost, směr) a základních atributů s okolními účastníky provozu. Umožňuje kooper"
---

CAM je periodická vysílací zpráva ve V2X komunikaci, která sdílí dynamický stav a základní atributy vozidla s okolními účastníky provozu, aby umožnila kooperativní povědomí pro bezpečnost a plynulost provozu.

## Popis

Zpráva kooperativního povědomí (CAM) je základní datová struktura definovaná ve standardech 3GPP pro služby Cellular Vehicle-to-Everything (C-V2X), konkrétně v rámci komunikace Vozidlo-vozidlo ([V2V](/mobilnisite/slovnik/v2v/)) a Vozidlo-infrastruktura (V2I). Funguje ve vrstvě Facilities (služební vrstvě) protokolového zásobníku [ETSI](/mobilnisite/slovnik/etsi/) [ITS](/mobilnisite/slovnik/its/) (Inteligentní dopravní systémy), který je adaptován pro použití přes rozhraní PC5 (sidelink) a Uu v 3GPP. CAM není přímo zprávou protokolu 3GPP, ale zprávou aplikační vrstvy, jejíž generování, správa a přenos jsou usnadněny možnostmi systému 3GPP. Jejím hlavním účelem je vytvářet a udržovat aktuální lokalizovanou dynamickou mapu bezprostředního okolí vozidla prostřednictvím periodického vysílání vlastního stavu a příjmu aktualizací stavu od ostatních entit s podporou CAM v dosahu komunikace.

Technické fungování CAM zahrnuje několik klíčových procesů řízených ITS stanicí vozidla. Generování CAM je spouštěno na základě specifických podmínek definovaných v ETSI EN 302 637-2, jako je minimální změna polohy (např. 4 metry), minimální změna směru (např. 4 stupně) nebo uplynutí maximálního časového intervalu (typicky 100–1000 ms, nastavitelné podle dynamiky vozidla). Každá vygenerovaná CAM obsahuje standardizovanou sadu datových prvků definovaných ve formátu ASN.1. Jádrový 'Základní kontejner' zahrnuje přesnou geografickou polohu vozidla (zeměpisná šířka, délka, nadmořská výška), rychlost, směr a zrychlení. 'Vysokofrekvenční kontejner' přidává dynamičtější data, jako je zakřivení dráhy vozidla a úhlová rychlost. Volitelné kontejnery mohou zahrnovat roli vozidla (např. vozidlo záchranné služby), historii trasy a stav vnějšího osvětlení.

Po vygenerování je CAM předána dolů protokolovým zásobníkem. Pro přímou C-V2X komunikaci (sidelink režim 4 nebo režim 2) je zpráva naplánována k vysílání přes rozhraní PC5 pomocí fyzické vrstvy NR-V2X nebo LTE-V2X v pásmu ITS 5,9 GHz. Protokoly vrstvy 2 v 3GPP zajišťují skutečný výběr rádiových zdrojů, modulaci a kódování. Přenos využívá vysílací mechanismus bez nutnosti navázání spojení, což umožňuje nízkolatentní distribuci všem přijímačům v dosahu, typicky v řádu stovek metrů. Pro komunikaci s podporou sítě (přes Uu) může být CAM odeslána do sítě pro distribuci do relevantní geografické oblasti, jak rozhodne [V2X](/mobilnisite/slovnik/v2x/) aplikační server.

Po přijetí ostatní vozidla nebo vozovkové jednotky ([RSU](/mobilnisite/slovnik/rsu/)) dekódují CAM a aktualizují své lokální dynamické mapy. Tato mapa je softwarová konstrukce, která slučuje data z více přijatých CAM spolu s daty ze senzorů, aby poskytla souvislý obraz dopravního prostředí. Systémová architektura podporující CAM zahrnuje ITS stanici vozidla, která obsahuje V2X aplikaci generující CAM, přístupovou vrstvu 3GPP pro rádiovou komunikaci a případně V2X aplikační server v síti pro širší distribuci. Role CAM v síti 3GPP je zásadní; poskytuje základní data o situačním povědomí, na kterých jsou vybudovány aplikace vyšších vrstev pro bezpečnost a plynulost provozu – jako je varování před čelní srážkou, asistence pohybu na křižovatce nebo doporučení optimální rychlosti pro zelenou vlnu – což z ní činí klíčový prvek pro automatizovanou a kooperativní jízdu.

## K čemu slouží

CAM byla vytvořena, aby řešila základní bezpečnostní výzvu v silniční dopravě: nedostatek kooperativního povědomí mezi účastníky provozu. Tradiční bezpečnostní systémy vozidel (jako jsou protiblokovací brzdy, elektronický systém stability nebo radarový adaptivní tempomat) spoléhají výhradně na palubní senzory, které mají inherentní omezení. Tyto senzory (kamery, radar, lidar) jsou limitovány přímou viditelností, povětrnostními podmínkami a překážkami (např. velký nákladní vůz blokující výhled na auto vpředu). To vytváří 'mrtvé úhly' mimo přímou viditelnost, kde kritická nebezpečí zůstávají neodhalena až do chvíle, kdy je příliš pozdě na bezpečnou reakci lidského řidiče nebo automatizovaného systému.

Účelem CAM je elektronicky rozšířit percepční horizont vozidla za hranice jeho fyzických senzorů. Vysíláním svých klíčových stavových informací vozidlo v podstatě deklaruje: 'Jsem zde, pohybuji se tímto směrem touto rychlostí.' Když se všech vozidel a infrastruktury účastní, vytváří to sdílené, kooperativní percepční pole. Tím se řeší problém překážek a poskytuje se prediktivní povědomí. Například vozidlo přibližující se k neprůhledné křižovatce může být varováno před rychle se blížícím vozidlem na příčné komunikaci dříve, než kterýkoli řidič druhého uvidí. Historicky koncept vznikl ve standardech pro vyhrazenou krátkodobou komunikaci (DSRC/[WAVE](/mobilnisite/slovnik/wave/)). 3GPP tento koncept přijalo a integrovalo CAM do svých standardů C-V2X (počínaje Release 14 pro LTE-V2X a vylepšené v Release 15+ pro NR-V2X), aby využilo globálního rozsahu, bezpečnostního rámce a vyvíjejícího se výkonu buněčné technologie, čímž vytvořilo jednotný komunikační systém jak pro telematiku, tak pro přímé bezpečnostně kritické výměny.

## Klíčové vlastnosti

- Periodické a událostmi spouštěné generování na základě dynamiky vozidla
- Standardizovaná datová struktura ASN.1 obsahující polohu, rychlost, směr a zrychlení
- Vysílací přenos přes sidelink rozhraní PC5 v 3GPP pro přímou, nízkolatentní komunikaci
- Umožňuje vytvoření Lokální dynamické mapy (LDM) v přijímajících entitách
- Základ pro aplikace vyšších vrstev V2X pro bezpečnost (např. varování před kolizí)
- Podporuje jak LTE-V2X, tak NR-V2X rádiové přístupové technologie

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [CAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cam/)
