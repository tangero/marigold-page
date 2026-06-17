---
slug: "gea"
url: "/mobilnisite/slovnik/gea/"
type: "slovnik"
title: "GEA – GPRS Encryption Algorithm"
date: 2025-01-01
abbr: "GEA"
fullName: "GPRS Encryption Algorithm"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gea/"
summary: "Rodina algoritmů proudové šifry používaná k šifrování uživatelských dat a signalizace přes rozhraní GPRS a EDGE rádiového přístupu. Zajišťuje důvěrnost komunikace mezi mobilní stanicí a sítí a chrání"
---

GEA je rodina algoritmů proudové šifry používaných v sítích 2G/3G k šifrování uživatelských dat a signalizace přes rozhraní GPRS rádiového přístupu, zajišťuje důvěrnost a chrání před odposlechem.

## Popis

[GPRS](/mobilnisite/slovnik/gprs/) Encryption Algorithm (GEA) je soubor algoritmů proudové šifry standardizovaný 3GPP pro zajištění důvěrnosti dat přenášených přes rozhraní Gb mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a uzlem SGSN v sítích GSM/GPRS/[EDGE](/mobilnisite/slovnik/edge/). Působí v rámci protokolového zásobníku GPRS, konkrétně na vrstvě Logical Link Control ([LLC](/mobilnisite/slovnik/llc/)). Šifrování a dešifrování se provádí pomocí šifrovacího klíče (Kc), který je odvozen během procedury autentizace a dohody o klíči, a vstupního parametru zvaného číslo rámce LLC, který zajišťuje synchronizaci a zabraňuje útokům opakováním. Algoritmus generuje šifrovací proud (keystream), který je XORován s otevřenými daty za vzniku šifrového textu, nebo naopak při dešifrování.

Existuje několik verzí GEA, především GEA1, GEA2, GEA3 a GEA4, z nichž každá má odlišný kryptografický návrh a sílu. GEA1 a GEA2 byly vyvinuty v 90. letech a jsou založeny na proprietárních návrzích, přičemž u GEA1 byly později zjištěny významné kryptografické slabiny. Později zavedené GEA3 a GEA4 jsou založeny na robustnějším a mezinárodně prověřeném algoritmu Kasumi (používaném v 3G), respektive algoritmu SNOW 3G (používaném v 4G), a nabízejí mnohem silnější zabezpečení. Konkrétní algoritmus použitý v relaci je dohodnut mezi MS a sítí na základě vzájemných možností.

Proces šifrování je zahájen odesláním příkazu 'Ciphering Mode Command' ze sítě do mobilní stanice. Po přijetí tohoto příkazu obě entity začnou aplikovat dohodnutou variantu GEA na všechny následující LLC rámce. Úloha algoritmu je omezena na část rádiového přístupu spojení; data jsou dešifrována v SGSN před směrováním přes jádro sítě. Tato architektura znamená, že GEA zabezpečuje nejzranitelnější bezdrátový spoj, ale neposkytuje šifrování end-to-end. Jeho činnost je základní součástí bezpečnostní architektury GPRS a pracuje společně s mechanismem GPRS Authentication and Key Agreement (GPRS-AKA) pro vytvoření kompletního bezpečnostního kontextu pro paketové datové služby.

## K čemu slouží

GEA byla vytvořena pro řešení kritické potřeby důvěrnosti v nově zavedených paketově orientovaných datových službách sítí GSM, známých jako [GPRS](/mobilnisite/slovnik/gprs/). Před GPRS používaly okruhově orientované hlasové služby GSM řadu algoritmů A5 pro šifrování přes rádiové rozhraní. Odlišná protokolová architektura a kontinuální tok dat paketových služeb však vyžadoval nový šifrovací mechanismus integrovaný na vrstvě [LLC](/mobilnisite/slovnik/llc/). Primárním problémem, který GEA řeší, je zabránění neautorizovanému zachycení a dekódování uživatelských dat (jako je internetový provoz) a citlivých signalizačních zpráv při jejich průchodu rádiovým spojem.

Historicky byly původní algoritmy GEA1 a GEA2 navrženy s ohledem na vývozní omezení a výpočetní limity 90. let. To vedlo k tomu, že GEA1 byl záměrně slabý, což se v pozdějších letech stalo významným bezpečnostním problémem. Vývoj GEA3 a GEA4 byl motivován potřebou nahradit tyto slabé algoritmy silnějšími a transparentnějšími kryptografickými návrhy sladěnými s bezpečnostními standardy 3G a 4G. Řeší omezení dřívějších verzí využitím dobře zavedených, veřejně hodnocených algoritmů (Kasumi a SNOW 3G), čímž obnovují robustní důvěrnost pro starší sítě GPRS/[EDGE](/mobilnisite/slovnik/edge/), které koexistovaly a vyvíjely se směrem k UMTS a LTE.

## Klíčové vlastnosti

- Návrh proudové šifry pro efektivní šifrování spojitých datových toků
- Působí na vrstvě Logical Link Control (LLC) protokolového zásobníku GPRS
- Používá šifrovací klíč (Kc) odvozený z procesu autentizace účastníka
- Synchronizace pomocí čísla rámce LLC zabraňuje opakovanému použití šifrovacího proudu
- Podporuje více variant algoritmu (GEA1, GEA2, GEA3, GEA4) pro zpětnou kompatibilitu a zvýšené zabezpečení
- Šifrování je aplikováno mezi mobilní stanicí (MS) a uzlem SGSN

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [GEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gea/)
