---
slug: "fecc"
url: "/mobilnisite/slovnik/fecc/"
type: "slovnik"
title: "FECC – Far End Camera Control"
date: 2025-01-01
abbr: "FECC"
fullName: "Far End Camera Control"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fecc/"
summary: "Protokol a schopnost v rámci služby multimediální telefonie pro IMS (MTSI), která vzdálenému účastníku videohovoru umožňuje ovládat orientaci (pan, tilt, zoom) kamery uživatele na druhém konci. Vylepš"
---

FECC je protokol v rámci služby multimediální telefonie pro IMS, který vzdálenému účastníku videohovoru umožňuje ovládat pan, tilt a zoom kamery uživatele na druhém konci.

## Popis

Far End Camera Control (FECC) je standardizovaná servisní funkce od 3GPP, která je součástí služby multimediální telefonie pro IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) a dalších konverzačních videoslužeb. Definuje mechanismus, který uživateli v bod-bod nebo multipoint videosession umožňuje odesílat řídicí příkazy pro vzdálené ovládání kamery na druhém konci. Tyto příkazy typicky zahrnují Pan (pohyb doleva/doprava), Tilt (pohyb nahoru/dolů), Zoom (přiblížení/oddálení) a případně další funkce specifické pro kameru. Protokol funguje v signalizační rovině, často využívá zpráv SIP (Session Initiation Protocol) nebo je součástí řídicího kanálu médií, aby zajistil spolehlivý a bezpečný přenos řídicích příkazů odděleně od mediálního streamu.

Architektonicky FECC zahrnuje několik funkčních entit v IMS a UE. Ovládající UE generuje požadavky FECC na základě vstupu uživatele. Tyto požadavky jsou formátovány podle specifikací 3GPP (např. za použití XML formátu definovaného v TS 26.114) a přenášeny prostřednictvím SIP [INFO](/mobilnisite/slovnik/info/) zpráv nebo jako součást toku [BFCP](/mobilnisite/slovnik/bfcp/) (Binary Floor Control Protocol) ve scénáři centralizované konference. Požadavek prochází jádrem IMS, případně přes aplikační servery, až ke vzdálenému UE. Klient MTSI vzdáleného UE přijme požadavek, interpretuje příkazy a komunikuje se svým místním hardwarovým nebo softwarovým rozhraním kamery, aby příkazy provedl. Kamera pak začne posílat nový video pohled zpět do mediálního streamu směřujícího k ovládajícímu uživateli.

Jak to funguje, zahrnuje fázi vyjednávání během navazování session. Výměna podpory pro FECC se provádí pomocí SIP/SDP (Session Description Protocol), přičemž koncové body označují podporu FECC a konkrétní sady příkazů (např. základní posun, relativní posun, absolutní posun), které dokáží zpracovat. Toto zajišťuje interoperabilitu. Během session je příkaz spuštěn ovládajícím uživatelem, zakódován do definované syntaxe a odeslán. Zařízení na druhém konci příkaz zpracuje, provede bezpečnostní a autorizační kontroly (např. ověří, zda je odesílatel autorizovaný účastník) a poté akci provede. Tato funkce je klíčová pro profesionální videokonference, teleprezence a scénáře vzdálené asistence, protože umožňuje prezentujícímu nebo instruktorovi nasměrovat pohled kamery vzdáleného účastníka pro lepší společný zážitek.

## K čemu slouží

FECC byl vytvořen pro řešení klíčového omezení v časných systémech videotelefonie a konferencí: statickou nebo pouze lokálně ovládanou podstatu pohledu kamery. Ve scénářích jako je vzdálená technická podpora, telemedicína nebo distanční výuka potřebuje odborník nebo instruktor často vidět specifický detail nebo oblast na vzdáleném místě. Bez FECC by musel slovně instruovat místního uživatele k fyzickému nastavení kamery, což je neefektivní, náchylné k chybám a rušivé. Účel FECC spočívá v poskytnutí přímého, přesného vzdáleného ovládání, čímž se zlepší efektivita komunikace a celkový uživatelský zážitek u interaktivních videoslužeb.

Motivace vychází z evoluce telefonních služeb založených na IMS, které překračují prostý hlas a směřují k bohaté multimediální komunikaci. Když 3GPP definovalo [MTSI](/mobilnisite/slovnik/mtsi/) pro konkurenci a vylepšení služeb [OTT](/mobilnisite/slovnik/ott/) (over-the-top), začlenění pokročilých funkcí jako je adaptace kvality videa a ovládání kamery se stalo nezbytným pro nabídku prémiového, operatorského zážitku. FECC standardizuje to, co bylo dříve proprietární funkcí v špičkových systémech teleprezence, a umožňuje tak interoperabilitu mezi zařízeními od různých výrobců v rámci ekosystémů 3GPP. Řeší problém pasivního sledování v rámci kolaborativní session a mění videohovory na interaktivní vizuální spolupráci.

Historicky, před standardizací, podobná funkčnost existovala v izolovaných systémech používajících neinteroperabilní protokoly. Práce 3GPP, počínaje Release 13, integrovala FECC do IMS architektury a využila existující SIP signalizaci pro přenos ovládání. Tím se vyřešila omezení ad-hoc řešení poskytnutím bezpečného, vyjednaného a síťově-aware řídicího kanálu. Umožňuje nové případy užití, jako je vzdálený dohled (s souhlasem), immersivní vzdělávání a vylepšené obchodní konference, čímž se video komunikace stává mocnějším nástrojem pro interakci namísto pouhého pozorování.

## Klíčové vlastnosti

- Vzdálené ovládání funkcí kamery pro pan, tilt a zoom (PTZ)
- Signalizace pomocí SIP INFO zpráv nebo BFCP pro přenos v rámci IMS session
- Vyjednávání podpory (capability negotiation) pomocí SDP parametrů během navazování session
- Podpora různých typů příkazů: Základní posun (Basic Move), Relativní posun (Relative Move) a Absolutní posun (Absolute Move)
- Integrace s 3GPP MTSI (Multimedia Telephony Service for IMS) architekturou
- Obsahuje bezpečnostní mechanismy pro autorizaci řídicích požadavků

## Související pojmy

- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [BFCP – Binary Floor Control Protocol](/mobilnisite/slovnik/bfcp/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [FECC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fecc/)
