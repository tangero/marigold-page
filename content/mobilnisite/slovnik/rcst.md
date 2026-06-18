---
slug: "rcst"
url: "/mobilnisite/slovnik/rcst/"
type: "slovnik"
title: "RCST – Return Channel via Satellite Terminal"
date: 2025-01-01
abbr: "RCST"
fullName: "Return Channel via Satellite Terminal"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rcst/"
summary: "Uživatelský terminál v satelitní síti, který poskytuje zpětný komunikační spoj od uživatele k síti prostřednictvím satelitu. Umožňuje obousměrnou satelitní komunikaci pro služby jako širokopásmový int"
---

RCST je uživatelský terminál v satelitní síti, který zajišťuje obousměrný zpětný komunikační spoj od uživatele k síti prostřednictvím satelitu.

## Popis

Terminál pro zpětný kanál přes satelit (RCST) je klíčovou součástí satelitních mobilních komunikačních systémů standardizovaných 3GPP. Funguje jako uživatelské zařízení (UE) nebo terminál, který komunikuje s geostacionárními nebo negeostacionárními satelity za účelem vytvoření zpětného spoje – přenosové cesty od uživatelského terminálu zpět k síťové bráně nebo pozemní stanici. Architektonicky RCST rozhraní s rádiovým rozhraním satelitu, typicky pracujícím ve specifických kmitočtových pásmech vyhrazených pro satelitní komunikaci (např. Ka-pásmo nebo Ku-pásmo). Zahrnuje satelitní modem, anténní systém (často parabolickou anténu nebo fázovaný anténní řada) a protokolové zásobníky přizpůsobené pro dlouhé doby šíření a proměnlivé podmínky spojení typické pro satelitní spoje. Terminál zajišťuje funkce jako modulace/demodulace, kódování, časová synchronizace a řízení výkonu pro udržení spolehlivého spojení přes satelitní kanál.

Při provozu se RCST účastní procedur náhodného přístupu a navazování spojení definovaných 3GPP pro satelitní přístup, které jsou rozšířením pozemních protokolů (např. založených na LTE nebo 5G NR). Přijímá signalizaci a uživatelská data z jádra sítě přes satelitní dopředný spoj (ze sítě k terminálu) a vysílá vlastní data a řídicí informace na zpětném spoji. Mezi klíčové komponenty patří vysokofrekvenční část ([RF](/mobilnisite/slovnik/rf/) front-end) pro konverzi satelitních kmitočtů, jednotka základního pásma implementující protokoly vrstvy 1 (fyzická vrstva) a vrstvy 2 ([MAC](/mobilnisite/slovnik/mac/), [RLC](/mobilnisite/slovnik/rlc/)) dle 3GPP a řídicí software pro konfiguraci a mobilitu. Úlohou RCST je umožnit uživatelské aplikace – jako hlas, video nebo prohlížení internetu – tím, že poskytuje uplinkovou cestu v satelitní rádiové přístupové síti (RAN) a integruje se s prvky jádra sítě 3GPP, jako je [AMF](/mobilnisite/slovnik/amf/) a [UPF](/mobilnisite/slovnik/upf/) v systémech 5G.

Terminál podporuje různé třídy služeb a úrovně kvality služeb (QoS), přizpůsobuje přenosové parametry na základě pokynů sítě a podmínek spojení. Může implementovat pokročilé funkce, jako je adaptivní kódování a modulace ([ACM](/mobilnisite/slovnik/acm/)), pro optimalizaci propustnosti při měnících se povětrnostních podmínkách nebo rušení. V síťové architektuře se RCST připojuje k satelitu, který přeposílá signály k pozemní bráně rozhranující s jádrem 3GPP, čímž vytváří koncový spoj. To umožňuje, aby RCST fungoval jako součást širší neterestrické sítě ([NTN](/mobilnisite/slovnik/ntn/)) a poskytoval pokrytí v oblastech, kde je pozemní infrastruktura neproveditelná. Jeho konstrukce řeší výzvy jako vysoká latence (např. až 550 ms pro geostacionární satelity), Dopplerův jev v systémech s nízkou oběžnou dráhou ([LEO](/mobilnisite/slovnik/leo/)) a přerušovanou viditelnost, což zajišťuje bezproblémovou integraci s mobilitou a správou relací dle 3GPP.

## K čemu slouží

RCST byl zaveden za účelem rozšíření mobilních komunikačních služeb 3GPP do geografických oblastí bez pozemní síťové infrastruktury, jako jsou venkovské oblasti, oceány a vzdušný prostor. Před jeho standardizací satelitní komunikační systémy často používaly proprietární technologie nekompatibilní s hlavními mobilními sítěmi, což omezovalo kontinuitu služeb a interoperabilitu zařízení. Definováním standardizovaného terminálu pro satelitní zpětné kanály umožnilo 3GPP bezproblémovou integraci satelitního přístupu se stávajícími jádry sítí, což uživatelům umožňuje roamovat mezi pozemními a satelitními sítěmi bez změny zařízení nebo protokolů.

Tím se řeší problém digitální propasti poskytováním širokopásmového připojení na odlehlých místech, což podporuje aplikace jako nouzová komunikace, námořní a letecké služby a nasazení IoT v izolovaných oblastech. Motivací byl rostoucí požadavek na globální pokrytí, zejména pro kritickou komunikaci a IoT, kde jsou pozemní sítě ekonomicky neproveditelné. Specifikace RCST ve verzi 11 a pozdějších položila základ pro neterestrické sítě (NTN) v 5G, čímž zajistila, že satelitní spoje mohou tam, kde je to možné, splňovat požadavky 3GPP na latenci, spolehlivost a propustnost.

## Klíčové vlastnosti

- Podporuje adaptace fyzické vrstvy specifické pro satelity pro kanály s dlouhou dobou zpoždění
- Implementuje protokolové zásobníky 3GPP (např. založené na LTE nebo NR) pro integrovaný přístup
- Umožňuje obousměrnou komunikaci prostřednictvím zpětného spoje k satelitní bráně
- Poskytuje správu mobility pro předávání spojení mezi satelitními buňkami
- Zahrnuje adaptivní modulaci a kódování pro optimalizaci spojení
- Umožňuje zpracování QoS pro různé služby přes satelitní spoje

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [RCST na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcst/)
