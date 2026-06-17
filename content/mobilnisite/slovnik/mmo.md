---
slug: "mmo"
url: "/mobilnisite/slovnik/mmo/"
type: "slovnik"
title: "MMO – Massive Multiplayer Online"
date: 2025-01-01
abbr: "MMO"
fullName: "Massive Multiplayer Online"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmo/"
summary: "Kategorie služeb v 3GPP pro podporu rozsáhlých interaktivních online her a aplikací přes mobilní sítě. Definuje síťové požadavky na nízkou latenci, vysokou spolehlivost a masivní konektivitu, aby umož"
---

MMO je kategorie služeb 3GPP pro podporu rozsáhlých interaktivních online aplikací přes mobilní sítě, která definuje požadavky na nízkou latenci, vysokou spolehlivost a masivní konektivitu, aby umožnila reálný časový zážitek pro tisíce souběžných uživatelů.

## Popis

Massive Multiplayer Online (MMO) je kategorie služeb standardizovaná 3GPP, která se primárně zaměřuje na síťovou podporu potřebnou pro rozsáhlé interaktivní online aplikace, zejména cloud gaming a hromadné online multiplayerové hry. Technická práce zahrnuje definici klíčových výkonnostních ukazatelů ([KPI](/mobilnisite/slovnik/kpi/)), architektonických aspektů a požadavků na služby, aby bylo zajištěno, že mobilní sítě mohou poskytovat potřebnou kvalitu uživatelského zážitku. To zahrnuje přísné požadavky na koncovou latenci, ztrátu paketů, rozkolísání zpoždění a datové toky v uplinku/downlinku pro podporu vykreslování v reálném čase, synchronizaci řízení a aktualizace stavu napříč velkým počtem současných účastníků.

Architektura pro podporu MMO služeb využívá základní schopnosti 5G systému, včetně síťového řezání, edge computingu (Multi-access Edge Computing - [MEC](/mobilnisite/slovnik/mec/)) a rámců kvality služeb (QoS). Typické nasazení zahrnuje aplikační servery, potenciálně hostované na síťové hraně pro minimalizaci latence, které komunikují s 5G jádrem (5GC) přes standardizovaná rozhraní jako N6. Funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) hraje klíčovou roli v zajištění datových cest s nízkou latencí a vysokou propustností, potenciálně s funkcí klasifikátoru uplinku (UL [CL](/mobilnisite/slovnik/cl/)) nebo větvícím bodem pro optimální směrování provozu mezi uživateli a herními servery hostovanými na hraně.

Klíčové technické komponenty zahrnují interakci mezi aplikační vrstvou a 5G sítí. Specifikace 3GPP definují, jak mohou aplikační funkce ([AF](/mobilnisite/slovnik/af/)) prostřednictvím rozhraní N5 žádat o konkrétní QoS toky u funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), aby síť vyhradila odpovídající zdroje. Dále specifikace řeší kontinuitu relace, správu mobility a podporu pro masivní počty zařízení v omezené geografické oblasti, což je klíčové pro události nebo virtuální prostředí s vysokou hustotou uživatelů. Tato práce zajišťuje, že rádiová přístupová síť (RAN) pomocí funkcí jako grant-free přenos v uplinku a optimalizované plánování dokáže zvládnout trhané a obousměrné vzorce provozu typické pro interaktivní MMO aplikace.

## K čemu slouží

Účelem standardizace MMO v rámci 3GPP je formálně uznat a řešit jedinečné a náročné síťové požadavky vznikajících rozsáhlých interaktivních služeb, které nebyly plně pokryty předchozími generacemi mobilních sítí. Tradiční služby mobilního širokopásmového přístupu byly optimalizovány pro asymetrický provoz (např. streamování videa, prohlížení webu) a neupřednostňovaly ultra-nízkou latenci a masivní souběžnou konektivitu potřebnou pro synchronizované interakce v reálném čase mezi tisíci uživateli. Vzestup cloud gamingu a sofistikovaných online multiplayerových her odhalil tato omezení, což si vyžádalo standardizovaný přístup k zajištění konzistentní kvality služeb a interoperability mezi operátory a výrobci zařízení.

Historicky takové služby spoléhaly buď na nadměrné poskytování best-effort internetových připojení, nebo na proprietární řešení, což vedlo k nekonzistentním uživatelským zážitkům a bránilo rozšířenému nasazení služeb. Definováním MMO jako kategorie služeb ve vydání 17 poskytuje 3GPP společný rámec pro síťové operátory, poskytovatele aplikací a výrobce zařízení. To umožňuje efektivní využití funkcí 5G sítí, jako je síťové řezání, k vytvoření vyhrazených, optimalizovaných logických sítí pro MMO provoz, a zajištění, že jsou garantovány [KPI](/mobilnisite/slovnik/kpi/) pro latenci, spolehlivost a kapacitu, čímž se odemkne komerční potenciál těchto imerzních aplikací.

## Klíčové vlastnosti

- Definice přísných KPI pro latenci (např. cíle pro koncovou latenci)
- Podpora masivní hustoty konektivity pro souběžné uživatele v servisní oblasti
- Požadavky na integraci s edge computingem (MEC) pro lokalizované zpracování
- Mechanismy pro QoS s ohledem na aplikaci a řízení politik prostřednictvím interakce AF-PCF
- Aspekty pro trhané vzorce provozu s dominantním uplinkem typické pro hry
- Architektonická podpora pro kontinuitu relace a služby během mobility uživatele

## Definující specifikace

- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [MMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmo/)
