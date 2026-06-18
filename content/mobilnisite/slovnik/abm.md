---
slug: "abm"
url: "/mobilnisite/slovnik/abm/"
type: "slovnik"
title: "ABM – Asynchronous Balanced Mode"
date: 2025-01-01
abbr: "ABM"
fullName: "Asynchronous Balanced Mode"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/abm/"
summary: "ABM je provozní režim vrstvy datového spoje v protokolu LAPDm používaný pro signalizaci v GSM. Vytváří vyvážené peer-to-peer spojení mezi dvěma entitami, umožňující simultánní obousměrnou komunikaci s"
---

ABM je asynchronní vyvážený režim v protokolu LAPDm, který v sítích GSM vytváří peer-to-peer spojení pro simultánní obousměrný signalizační přenos s detekcí a opravou chyb.

## Popis

Asynchronous Balanced Mode (ABM) je základní provozní režim definovaný v protokolu Link Access Procedure on the Dm channel (LAPDm), což je protokol vrstvy datového spoje pro GSM rozhraní Um (mezi mobilní stanicí a podsystémem základnové stanice). ABM vytváří vyvážený peer-to-peer logický spoj mezi dvěma entitami, zejména mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou přenosovou stanicí ([BTS](/mobilnisite/slovnik/bts/)). V tomto režimu obě stanice fungují jako kombinované stanice, což znamená, že každá má schopnost zahájit přenos, vysílat příkazy a reagovat na přijaté rámce bez nutnosti povolení od primární stanice. Tato symetrická architektura je klíčová pro efektivní signalizaci.

Fungování ABM se opírá o sadu dozorových (S) a nečíslovaných (U) rámců pro správu spoje. Mezi klíčové procedury patří navázání spoje, při kterém si obě strany vymění rámce Set Asynchronous Balanced Mode ([SABM](/mobilnisite/slovnik/sabm/)) a Unnumbered Acknowledgment ([UA](/mobilnisite/slovnik/ua/)) k inicializaci logického spojení. Po navázání přenášejí informační (I) rámce vlastní signalizační zprávy vrstvy 3 (např. pro řízení hovoru, správu mobility). Protokol zajišťuje spolehlivé doručení pomocí mechanismů jako číslování rámců, cyklický redundantní součet ([CRC](/mobilnisite/slovnik/crc/)) pro detekci chyb a opakovaný přenos založený na odmítacích ([REJ](/mobilnisite/slovnik/rej/)) rámcích nebo na obnově řízené časovačem (např. časovač T200). Řízení toku je zajištěno pomocí dozorových rámců Receiver Ready ([RR](/mobilnisite/slovnik/rr/)) a Receiver Not Ready ([RNR](/mobilnisite/slovnik/rnr/)).

Role ABM je ústřední pro signalizační architekturu GSM na rádiovém rozhraní. Poskytuje spolehlivou, sekvenovanou a na chyby kontrolovanou transportní služnu nezbytnou pro kritické signalizační zprávy non-access stratum (NAS) mezi MS a sítí. To zahrnuje procedury pro aktualizaci polohy, autentizaci, šifrování, zřizování hovoru a přenos SMS. Režim pracuje na logických kanálech jako Stand-alone Dedicated Control Channel (SDCCH) nebo Slow Associated Control Channel (SACCH). Jeho vyvážená povaha eliminuje vztah typu master-slave, což umožňuje kterémukoli konci zahájit opravné akce nebo podle potřeby vysílat data, což optimalizuje odezvu a spolehlivost v dynamickém rádiovém prostředí.

## K čemu slouží

ABM byl vytvořen, aby poskytoval robustní a efektivní mechanismus řízení datového spoje pro signalizaci přes náchylné k chybám GSM rádiové rozhraní. Předchozí jednodušší režimy nebo protokoly nepostačovaly nárokům veřejné celulární sítě, která vyžaduje garantované a ve správném pořadí doručování kritických řídicích zpráv pro mobilitu, zabezpečení a správu hovorů. ABM řeší omezení nevyvážených režimů (jako je Normal Response Mode) tím, že umožňuje komunikaci peer-to-peer, což snižuje latenci a dovoluje kterékoli stanici zahájit nápravné akce při výpadku spoje.

Historický kontext spočívá v návrhu GSM jako digitálního systému oddělujícího uživatelský provoz (okruhově spínaný hlas) od řídicí signalizace. Vyhrazený, spolehlivý signalizační spoj byl nezbytný. ABM, adaptovaný z protokolu ISDN LAPD pro rádiové prostředí (čímž se stal LAPDm), toto vyřešil díky nabídce vyváženého provozu, komplexní kontroly chyb a řízení toku. Zajišťuje, že signalizační transakce – jako je příkaz k předání hovoru nebo výzva k autentizaci – jsou přesně doručeny navzdory útlumu a rušení na rádiovém rozhraní, což je základní pro spolehlivost sítě a zkušenost účastníka.

Jeho vytvoření bylo motivováno potřebou standardizovaného linkového postupu, který by podporoval složité signalizační dialogy definované v protokolech GSM bez nutnosti spoléhat se na centrální řadič, který by dotazoval sekundární stanice. Tento vyvážený přístup zlepšuje efektivitu a je klíčovým předpokladem pro sofistikované služby účastníků a síťově řízenou mobilitu, které jsou charakteristické pro systémy 2G a pozdějších celulárních generací.

## Klíčové vlastnosti

- Vyvážený peer-to-peer provoz mezi kombinovanými stanicemi
- Spolehlivý přenos dat pomocí číslování rámců a potvrzení
- Integrovaná detekce chyb prostřednictvím CRC a oprava chyb prostřednictvím opakovaného přenosu
- Řízení toku pomocí rámců Receiver Ready (RR) a Receiver Not Ready (RNR)
- Podpora multiplexování více entit vrstvy 3 pomocí Service Access Point Identifiers (SAPI)
- Pracuje nad logickými řídicími kanály GSM (např. SDCCH, SACCH)

## Související pojmy

- [SAPI – Service Access Point Identifier](/mobilnisite/slovnik/sapi/)
- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)
- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [ABM na 3GPP Explorer](https://3gpp-explorer.com/glossary/abm/)
