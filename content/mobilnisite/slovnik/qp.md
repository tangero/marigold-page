---
slug: "qp"
url: "/mobilnisite/slovnik/qp/"
type: "slovnik"
title: "QP – Quantization Parameter"
date: 2025-01-01
abbr: "QP"
fullName: "Quantization Parameter"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qp/"
summary: "Kvantizační parametr (QP) je klíčová hodnota ve standardech videokomprese jako H.264/AVC a H.265/HEVC, která řídí kompromis mezi kvalitou videa a datovým tokem. Určuje velikost kroku použitou při kvan"
---

QP je parametr ve videokompresi, který řídí velikost kroku pro kvantování transformačních koeficientů a přímo určuje kompromis mezi kvalitou zakódovaného videa a datovým tokem.

## Popis

Kvantizační parametr (QP) je základní řídicí proměnná v blokových hybridních videokodecích standardizovaných [ITU-T](/mobilnisite/slovnik/itu-t/) a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/), jako jsou H.264/[AVC](/mobilnisite/slovnik/avc/), H.265/[HEVC](/mobilnisite/slovnik/hevc/) a H.266/[VVC](/mobilnisite/slovnik/vvc/), které jsou široce používány v multimediálních službách 3GPP. Kvantizace je proces, který v kódovacím řetězci následuje po diskrétní kosinové transformaci ([DCT](/mobilnisite/slovnik/dct/)) nebo podobné transformaci. Snižuje přesnost transformačních koeficientů jejich dělením konkrétní velikostí kroku a zaokrouhlením na nejbližší celé číslo. Tato velikost kroku je odvozena od hodnoty QP. QP přímo určuje velikost kvantizačního kroku, obvykle podle exponenciálního vztahu (např. velikost kroku se zdvojnásobí s každým zvýšením QP o 6). Tento proces je hlavním zdrojem komprese – a ztráty kvality – v moderních videokodecích.

V architektuře kódování videa jsou výsledné reziduální transformační koeficienty, poté co makroblok nebo jednotka kódovacího stromu ([CTU](/mobilnisite/slovnik/ctu/)) projde predikcí (intra nebo inter) a transformací, přivedeny do kvantizéru. Enkodér vybírá hodnotu QP, často adaptivně na úrovni snímku, řezu nebo dokonce bloku, na základě algoritmů řízení datového toku. Kvantované koeficienty jsou následně entropicky kódovány a zabaleny do bitového proudu. Samotná hodnota QP je také zakódována a přenášena, aby dekodér mohl provést inverzní kvantizaci (násobení velikostí kroku) a rekonstruovat přibližnou hodnotu původních koeficientů. Nepřesnost zavedená tímto procesem se projevuje jako kompresní artefakty, například rozmazání, blokování nebo přetínání v dekódovaném videu.

Jeho role v sítích 3GPP je klíčová pro adaptivní doručování médií. Aplikace a mediální servery používají QP jako hlavní páku v adaptivním streamování (ABR). Na základě dostupné šířky pásma sítě (informované metrikami QoS) může enkodér dynamicky upravovat QP, aby vytvořil více reprezentací (variant datového toku a kvality) stejného obsahu. Když se síťové podmínky zhorší, klient může požadovat segment zakódovaný s vyšším QP (nižším datovým tokem), aby se předešlo opětovnému načítání buffru, byť za nižší vizuální kvality. Tato dynamická úprava, často součást logiky HAS (HTTP Adaptive Streaming) odkazované ve specifikacích 3GPP, je zásadní pro udržení plynulého a kontinuálního uživatelského komfortu (QoE) přes proměnlivé bezdrátové kanály.

## K čemu slouží

Kvantizační parametr existuje, aby řešil ústřední problém ztrátové videokomprese: dosažení co nejvyššího kompresního poměru při zachování přijatelné percepční kvality videa. Bez kvantizace by datové toky videa byly pro ukládání a přenos neprakticky vysoké. Rané standardy videokódování používaly pevné kvantizační matice. Zavedení dynamicky nastavitelného QP poskytlo enkodéru kontrolu pro jemné vyvažování kompromisu mezi datovým tokem a kvalitou v reálném čase, což je nezbytné pro vysílání a komunikaci v reálném čase.

V kontextu 3GPP a mobilních multimédií je motivace pro řízení QP hnána omezenou a proměnlivou povahou bezdrátových sítí. Rané mobilní video služby používaly kódování s konstantním datovým tokem, což často vedlo k vyprázdnění bufferu (zastavení) při poklesu šířky pásma nebo k zbytečně nízké kvalitě za dobrých podmínek. Adaptivní streamování, poháněné dynamickou úpravou QP, tuto neefektivitu odstranilo. Umožňuje jedinému kódovacímu řetězci generovat více kvalitativních vrstev, což síti a klientovi umožňuje vybrat optimální verzi pro každý segment. Tím se maximalizuje QoE v rámci dostupné propustnosti.

Dále, jak se 3GPP vyvíjelo pro podporu videa vyššího rozlišení (HD, 4K, 8K) a nových imerzních formátů jako video 360 stupňů, se efektivní komprese stala ještě kritičtější. Pokročilé kodeky jako HEVC a VVC používají sofistikovanější kvantizační techniky (např. závislá kvantizace, frekvenčně závislé posuny QP), ale základní koncept QP řídícího velikost kroku zůstává. Jeho standardizace v rámci kodeků odkazovaných 3GPP (v TS 26.114 pro paketově spínané streamovací služby) zajišťuje interoperabilitu mezi enkodéry, mediálními servery a UEs, což umožňuje globální ekosystém adaptivních video služeb přes mobilní sítě.

## Klíčové vlastnosti

- Přímo řídí velikost kvantizačního kroku, čímž určuje kompromis mezi datovým tokem a zkreslením
- Hodnoty v moderních kodecích typicky leží v rozsahu 0 až 51 (nebo podobném), přičemž nižší hodnoty označují jemnější kvantizaci
- Lze jej adaptivně upravovat na úrovni snímku, řezu nebo kódovacího bloku na základě složitosti obsahu a řízení datového toku
- Integrován do algoritmů řízení datového toku jako CBR, VBR a CRF za účelem splnění cílů pro datový tok nebo kvalitu
- Ovlivňuje jak složku jasu, tak i chrominance, často s oddělenými posuny QP pro chroma
- Nezbytný pro generování více reprezentací s různým datovým tokem a kvalitou v adaptivním streamování (ABR)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines

---

📖 **Anglický originál a plná specifikace:** [QP na 3GPP Explorer](https://3gpp-explorer.com/glossary/qp/)
