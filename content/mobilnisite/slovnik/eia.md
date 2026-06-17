---
slug: "eia"
url: "/mobilnisite/slovnik/eia/"
type: "slovnik"
title: "EIA – EPS Integrity Algorithm"
date: 2025-01-01
abbr: "EIA"
fullName: "EPS Integrity Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/eia/"
summary: "Kryptografický algoritmus používaný v Evolved Packet System (EPS) k zajištění integritní ochrany a ověření signalizačních zpráv mezi uživatelským zařízením (UE) a sítí. Zajišťuje, že řídicí rovinná da"
---

EIA je EPS Integrity Algorithm, kryptografická funkce, která zajišťuje integritní ochranu a ověření signalizačních zpráv mezi uživatelským zařízením (UE) a sítí.

## Popis

EPS Integrity Algorithm (EIA) je soubor kryptografických algoritmů standardizovaných 3GPP pro ochranu integrity signalizačních zpráv v Evolved Packet System (EPS), který zahrnuje LTE a později i 5G core sítě komunikující s [E-UTRAN](/mobilnisite/slovnik/e-utran/). Integritní ochrana je základní bezpečnostní služba, která zaručuje, že přijatá signalizační data (např. zprávy [RRC](/mobilnisite/slovnik/rrc/) a [NAS](/mobilnisite/slovnik/nas/)) jsou autentická a nebyla během přenosu změněna. Algoritmy EIA vypočítávají pro každou chráněnou zprávu Message Authentication Code ([MAC](/mobilnisite/slovnik/mac/)), často nazývaný integritní token nebo [MAC-I](/mobilnisite/slovnik/mac-i/). Tento MAC je generován pomocí tajného integritního klíče ([IK](/mobilnisite/slovnik/ik/)), časově závislého vstupu (COUNT), bitu směru (uplink/downlink), samotné zprávy a identifikátoru přenosového kanálu (bearer identity).

Proces funguje následovně: odesílatel (UE nebo eNodeB/[MME](/mobilnisite/slovnik/mme/)) vloží výše uvedené parametry do zvoleného algoritmu EIA. Algoritmus vytvoří výstup MAC-I, který je připojen ke zprávě. Příjemce nezávisle vypočítá očekávaný MAC-I pomocí stejných vstupů a sdíleného tajného klíče. Pokud se vypočítaný MAC-I shoduje s přijatým, je integrita zprávy ověřena. Pokud ne, je zpráva zahozena a může být zahájen postup řešení bezpečnostní chyby. Mezi konkrétní definované algoritmy patří EIA0 (nulová integrita, používaná v některých omezených případech), EIA1 (založený na SNOW 3G), EIA2 (založený na [AES](/mobilnisite/slovnik/aes/)) a EIA3 (založený na ZUC).

Výběr konkrétního algoritmu EIA pro danou relaci je součástí vyjednávání bezpečnostního režimu během navazování spojení, jak je definováno v TS 33.401. Síť ve svých bezpečnostních schopnostech označí povolené algoritmy a UE jeden z nich vybere. Integritní klíč (IK) je odvozen z dlouhodobého tajného klíče (K) uloženého v USIM a v Authentication Centre (AuC) během procedury Authentication and Key Agreement (AKA). Tato vrstvená derivace klíčů zajišťuje, že integritní klíč je pro každou relaci čerstvý a jedinečný.

## K čemu slouží

EIA byl vytvořen, aby řešil kritickou potřebu integrity signalizačních zpráv v nové, plně IP architektuře LTE/EPS. V předchozích sítích 2G/3G, přestože se často používalo šifrování, integritní ochrana signalizace nebyla všeobecně aplikována, což činilo řídicí kanály zranitelnými vůči určitým typům útoků, jako je vkládání nebo manipulace se zprávami. Přechod na IP rozhraní přes rádio zvýšil potenciální útočnou plochu, což učinilo robustní kryptografickou ochranu nezbytnou.

Účelem EIA je zabránit útokům, jako jsou replay útoky, man-in-the-middle útoky a falšování signalizačních příkazů (např. zlomyslné příkazy k předání spojení nebo odpojení). Zajištěním integrity může síť věřit, že kritické příkazy pro správu mobility, správu relací a řízení spojení pocházejí od ověřené entity a nebyly pozměněny. Toto je základním kamenem bezpečnosti přístupu k síti, který chrání jak síť před zlomyslnými UE, tak UE před neoprávněnými síťovými prvky. Standardizace více algoritmů (SNOW 3G, AES, ZUC) také poskytuje kryptografickou flexibilitu, umožňující aktualizaci algoritmů v reakci na budoucí kryptografické průlomy nebo regulatorní požadavky.

## Klíčové vlastnosti

- Poskytuje kryptografickou integritní ochranu pro signalizační zprávy NAS a RRC
- Generuje Message Authentication Code (MAC-I) pro každou chráněnou zprávu
- Používá rodinu algoritmů: EIA1 (SNOW 3G), EIA2 (AES), EIA3 (ZUC) a EIA0 (nulový)
- Výběr algoritmu je vyjednán během procedury Security Mode Command
- Používá odvozený integritní klíč (IK) a časově proměnný vstup (COUNT) pro zajištění čerstvosti
- Zásadní pro prevenci manipulace se signalizačními zprávami a replay útoků

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [EIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/eia/)
