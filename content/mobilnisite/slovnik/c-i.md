---
slug: "c-i"
url: "/mobilnisite/slovnik/c-i/"
type: "slovnik"
title: "C/I – Carrier-to-Interference Power Ratio"
date: 2025-01-01
abbr: "C/I"
fullName: "Carrier-to-Interference Power Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/c-i/"
summary: "C/I je základní měření rádiové frekvence představující poměr výkonu požadovaného signálu nosné k výkonu rušivého signálu na přijímači. Jde o klíčový parametr pro hodnocení kvality rádiového spoje, urč"
---

C/I (Carrier-to-Interference Power Ratio) je poměr výkonu požadovaného signálu nosné k výkonu rušivého signálu na přijímači, což je klíčový parametr pro hodnocení kvality rádiového spoje a výkonu sítě.

## Popis

Carrier-to-Interference Power Ratio (C/I) je bezrozměrná veličina vyjádřená v decibelech (dB), která kvantifikuje relativní sílu požadovaného signálu ve srovnání s nežádoucími rušivými signály ve stejném kmitočtovém pásmu. Matematicky je C/I = 10·log₁₀(P_c/P_i), kde P_c je přijímaný výkon požadovaného signálu nosné a P_i je celkový výkon rušivých signálů. Toto měření se typicky provádí na přijímači po zpracování rádiové frekvence, ale před demodulací a dekódováním, a poskytuje přímou indikaci kvality signálu dostupné pro obnovení informace.

V systémech 3GPP jsou měření C/I zásadní pro četné funkce správy rádiových prostředků. Tento poměr přímo určuje maximální dosažitelný poměr signálu k šumu (SNR) na vstupu demodulátoru, což následně určuje modulační schéma nejvyššího řádu a nejnižší kódovací rychlost, které lze spolehlivě použít. Například v systémech LTE a 5G NR umožňují vyšší hodnoty C/I použití modulace 256-QAM nebo 1024-QAM s nízkou kódovací rychlostí, což vede k výrazně vyšší spektrální účinnosti a propustnosti pro uživatele. Naopak nízké hodnoty C/I nutí systém přejít na robustnější, ale méně účinná modulační schémata, jako je QPSK s vyšší kódovou redundancí.

Měření C/I zahrnuje různé zdroje rušení včetně rušení na stejném kanálu (co-channel interference) od sousedních buněk používajících stejný kmitočet, rušení na sousedním kanálu (adjacent channel interference) od signálů v blízkých kmitočtových pásmech a mezisymbolového rušení způsobeného vícecestným šířením. V celulárních sítích je C/I obzvláště důležité pro plánování kmitočtového opakování, kde se stejné kmitočty znovu používají v různých buňkách vzdálených natolik, aby byla zachována přijatelná úroveň rušení. Tento poměr je průběžně sledován uživatelským zařízením (UE) a hlášen síti prostřednictvím hlášení o měřeních, což umožňuje dynamickou adaptaci přenosových parametrů.

Z pohledu systémové architektury dochází k odhadu C/I na více místech v řetězci přijímače. Počáteční odhad probíhá během procedur synchronizace a vyhledávání buněk, kde UE měří výkon referenčního signálu vůči rušení. Během příjmu dat poskytují vyhrazené měřicí symboly a pilotní signály průběžné sledování C/I. Základnová stanice tato měření používá k činění klíčových rozhodnutí o předávání spojení (handover), úpravách řízení výkonu a přidělování prostředků pro plánování (scheduling). V pokročilých systémech využívajících techniky koordinace rušení, jako je eICIC (enhanced Inter-Cell Interference Coordination) nebo CoMP (Coordinated Multi-Point), jsou měření C/I z více buněk agregována za účelem optimalizace výkonu v celé síti.

Praktická implementace měření C/I zahrnuje sofistikované algoritmy, které oddělují složky požadovaného signálu od rušení. Tyto algoritmy musí zohledňovat časově proměnné podmínky kanálu, kmitočtově selektivní útlum a statistické vlastnosti rušení. Moderní přijímače používají adaptivní filtraci, potlačování rušení a pokročilé techniky zpracování signálu ke zlepšení přesnosti odhadu C/I. Výsledné hodnoty C/I jsou vstupem pro algoritmy adaptace spoje, které dynamicky vybírají optimální modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) pro každý přenosový časový interval, vyvažujíce spektrální účinnost proti pravděpodobnosti chyby.

## K čemu slouží

Carrier-to-Interference Power Ratio existuje jako základní metrika pro kvantifikaci a správu rušení rádiové frekvence v bezdrátových komunikačních systémech. V celulárních sítích, kde je kmitočtové spektrum vzácným a drahým zdrojem, je efektivní opakované použití kmitočtů napříč více buňkami nezbytné pro dosažení vysoké kapacity. Toto opakované použití kmitočtů však nevyhnutelně vytváří rušení mezi buňkami používajícími stejné kmitočty, což omezuje výkon systému. C/I poskytuje standardizovaný způsob měření tohoto rušení a umožňuje inteligentní rozhodnutí o správě sítě, která maximalizují kapacitu při zachování přijatelné kvality služby.

Před rozšířeným přijetím metrik C/I se rané celulární systémy pro optimalizaci sítě spoléhaly primárně na indikátory síly přijímaného signálu (RSSI). Zatímco měření RSSI mohla naznačit, zda je signál dostatečně silný k detekci, neposkytovala žádné informace o relativní síle rušivých signálů. Toto omezení se stalo kritickým s vývojem celulárních sítí z analogových na digitální systémy a implementací agresivnějších vzorů opakovaného použití kmitočtů. Digitální modulační schémata jsou na rušení obzvláště citlivá, přičemž i relativně slabé rušivé signály způsobují významné zhoršení míry bitových chyb. Zavedení měření C/I umožnilo sítím rozlišit mezi scénáři se silnými požadovanými signály a silným rušením a scénáři se slabými požadovanými signály, ale minimálním rušením.

Vytvoření a standardizace technik měření C/I ve specifikacích 3GPP řeší několik klíčových omezení předchozích přístupů. Za prvé umožnily přesnější předpověď výkonu spoje, protože vztah mezi C/I a mírou bitových chyb je dobře charakterizován pro různá modulační schémata. Za druhé usnadnily vývoj adaptivní modulace a kódování, kde se přenosové parametry dynamicky upravují na základě aktuálních podmínek kanálu. Za třetí poskytly základ pro pokročilé techniky správy rušení, jako je plánování s ohledem na rušení, řízení výkonu a koordinovaný vícebodový přenos. Kvantifikací rušení namísto pouhého měření absolutní síly signálu se C/I stalo základním kamenem moderní optimalizace celulárních sítí, což umožnilo vysokou spektrální účinnost vyžadovanou pro systémy 3G, 4G a 5G.

## Klíčové vlastnosti

- Kvantifikuje poměr výkonu požadovaného signálu k výkonu rušení v dB
- Základní vstup pro výběr modulačního a kódovacího schématu
- Umožňuje dynamickou adaptaci spoje na základě rádiových podmínek
- Podporuje rozhodnutí o plánování s ohledem na rušení
- Kritický parametr pro procedury předání spojení a převýběru buňky
- Základ pro pokročilé techniky koordinace rušení

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [C/I na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-i/)
