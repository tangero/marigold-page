---
slug: "rsrq"
url: "/mobilnisite/slovnik/rsrq/"
type: "slovnik"
title: "RSRQ – Reference Signal Receiving Quality"
date: 2026-01-01
abbr: "RSRQ"
fullName: "Reference Signal Receiving Quality"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rsrq/"
summary: "RSRQ je klíčové měření v LTE a NR, které reprezentuje kvalitu přijatých referenčních signálů. Je definováno jako poměr RSRP k celkovému přijatému výkonu. Poskytuje metriku podobnou poměru signálu k šu"
---

RSRQ je poměr výkonu přijatého referenčního signálu (RSRP) k celkovému přijatému výkonu a poskytuje metriku podobnou SINR pro hodnocení kvality rádiového spoje v mobilních sítích.

## Popis

Reference Signal Receiving Quality (RSRQ, kvalita přijmu referenčního signálu) je základní měření na první vrstvě (Layer 1) v sítích LTE i 5G NR, které kvantifikuje kvalitu přijatých buňkově specifických referenčních signálů. Je definováno jako poměr N * [RSRP](/mobilnisite/slovnik/rsrp/) / ([E-UTRA](/mobilnisite/slovnik/e-utra/) carrier [RSSI](/mobilnisite/slovnik/rssi/)), kde N je počet bloků zdrojů ([RB](/mobilnisite/slovnik/rb/)) v šířce pásma, ve které se měří E-UTRA carrier RSSI. Zjednodušeně řečeno, RSRQ porovnává výkon požadovaných referenčních signálů (RSRP) s celkovým přijatým výkonem, včetně rušení a šumu, ve stejné šířce měřicího pásma. Výsledkem je bezrozměrná metrika, typicky vyjadřovaná v dB, která přibližně odpovídá úzkopásmovému poměru signálu k šumu a rušení ([SINR](/mobilnisite/slovnik/sinr/)) pro referenční signály.

Z architektonického hlediska měření RSRQ provádí uživatelské zařízení (UE). Síť prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) nakonfiguruje měřené objekty, konfiguraci hlášení a měřicí mezery. UE změří RSRP na buňkově specifických referenčních signálech ([CRS](/mobilnisite/slovnik/crs/) v LTE, SSB nebo [CSI-RS](/mobilnisite/slovnik/csi-rs/) v NR) a indikátor síly přijímaného signálu (RSSI) v nakonfigurovaném pásmu. Fyzická vrstva tato měření provede a výsledky jsou před nahlášením vyšším vrstvám filtrovány (pomocí L1 a L3 filtrování). V LTE je RSRQ primárním měřením pro správu rádiových zdrojů (RRM), včetně výběru/opětovného výběru buňky a předávání hovoru. V NR zůstává SS-RSRQ (založené na SSB) důležité a bylo zavedeno CSI-RSRQ pro flexibilnější hodnocení kvality, zejména ve scénářích s formováním svazku.

Role RSRQ v síti je mnohostranná. Poskytuje kritický vstup pro mobilní algoritmy. Zatímco RSRP ukazuje sílu signálu, RSRQ ukazuje, jak „čistý“ tento signál je. Buňka s vysokým RSRP, ale špatným RSRQ může být silně vytížená nebo trpět silným rušením, což z ní činí méně vhodného kandidáta na připojení. Proto síťové algoritmy často využívají RSRQ (nebo jeho deriváty) ke spouštění předání hovoru, správě vyvažování zátěže a konfiguraci parametrů opětovného výběru buňky. Je spolehlivějším ukazatelem potenciální propustnosti pro uživatele a stability spojení než samotné RSRP, a to zejména na okrajích buněk, kde převládá rušení.

## K čemu slouží

RSRQ bylo zavedeno v LTE Release 8, aby vyřešilo zásadní omezení používání pouze RSRP pro správu rádiových zdrojů. Samotné RSRP udává sílu signálu z obsluhující nebo sousední buňky, ale nezohledňuje úroveň rušení ani celkovou zátěž kanálu. Buňka může mít silné RSRP, ale být nepoužitelná kvůli nadměrnému rušení ze sousedních buněk pracujících na stejné frekvenci (soukanálové rušení). To mohlo vést k nevhodným rozhodnutím o předání hovoru, kdy se UE připojilo k silné, ale silně rušené buňce, což mělo za následek zhoršený uživatelský zážitek a přerušení hovorů.

Zavedení RSRQ poskytlo standardizovanou, sítí řízenou metriku, která kombinuje sílu signálu a rušení do jediného ukazatele kvality. To umožnilo inteligentnější výběr buňky a předání hovoru, čímž se zlepšil celkový výkon sítě, kapacita a kvalita vnímaná uživatelem. Jeho účel se v následujících verzích rozšířil o podporu nových funkcí, jako je agregace nosných (kde výběr sekundární buňky zohledňuje kvalitu), duální konektivita a v NR spolupráce s měřeními svazků. RSRRQ zůstává klíčovým měřením, protože řeší klasický kompromis v celulárních sítích mezi silou signálu a rušením, což umožňuje algoritmy optimalizující jak připojení, tak kvalitu služeb.

## Klíčové vlastnosti

- Definováno jako poměr: N * RSRP / RSSI, což poskytuje metriku kvality relativní k celkovému přijatému výkonu.
- Slouží jako primární vstup pro mobilní procedury v LTE a NR (výběr buňky, opětovný výběr, předání hovoru).
- Dostupné pro měření založená jak na CRS v LTE, tak na SSB (SS-RSRQ) a CSI-RS (CSI-RSRQ) v NR.
- Konfigurovatelná šířka měřicího pásma a kritéria hlášení prostřednictvím signalizace RRC.
- Podporuje filtrování na první vrstvě (L1) a třetí vrstvě (L3) pro stabilitu měření.
- Kritické pro optimalizaci sítě s ohledem na rušení a vyvažování zátěže.

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [RSSI – Received Signal Strength Indication](/mobilnisite/slovnik/rssi/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [RSRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsrq/)
