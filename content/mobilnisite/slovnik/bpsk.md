---
slug: "bpsk"
url: "/mobilnisite/slovnik/bpsk/"
type: "slovnik"
title: "BPSK – Binary Phase Shift Keying"
date: 2026-01-01
abbr: "BPSK"
fullName: "Binary Phase Shift Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bpsk/"
summary: "BPSK je základní schéma digitální modulace, kde dva odlišné fázové stavy (0° a 180°) reprezentují binární data (0 a 1). Poskytuje robustní přenos s nízkou složitostí a vynikající odolností proti šumu,"
---

BPSK je základní schéma digitální modulace, kde dva odlišné fázové stavy reprezentují binární data, a poskytuje robustní přenos s nízkou složitostí, který je nezbytný pro řídicí kanály a signalizaci s nízkou přenosovou rychlostí v systémech 3GPP.

## Popis

Binární fázová manipulace (BPSK) je lineární technika digitální modulace zásadní pro fyzickou vrstvu bezdrátových komunikačních systémů 3GPP. Funguje na principu změny fáze nosné vlny s konstantní amplitudou pro zakódování binární informace. Konkrétně je binární '0' reprezentováno nosnou vlnou s fází 0 stupňů, zatímco binární '1' je reprezentováno fázovým posunem o 180 stupňů. Tím vznikají dva antipodální signálové body v konstelacím diagramu, oddělené maximální možnou eukleidovskou vzdáleností pro danou energii signálu. Toto maximální oddělení je klíčem k robustnosti BPSK, neboť poskytuje nejvyšší možnou odolnost vůči aditivnímu bílému gaussovskému šumu ([AWGN](/mobilnisite/slovnik/awgn/)) ze všech binárních modulačních schémat.

V implementacích 3GPP se BPSK typicky realizuje pomocí koherentní detekce, což vyžaduje, aby přijímač měl přesný fázový referenční signál pro správnou demodulaci. Modulovaný signál lze matematicky vyjádřit jako s(t) = A_c * cos(2πf_c t + φ_n), kde φ_n je buď 0, nebo π radiánů. Proces demodulace zahrnuje korelaci přijímaného signálu s lokálně generovanou nosnou referencí. Klíčovou součástí systémů BPSK je smyčka fázového závěsu (PLL) nebo obvod pro obnovu nosné, který synchronizuje lokální oscilátor přijímače s fází nosné příchozího signálu. Díky své konstantní obálce je BPSK méně náchylný k nelineárnímu zkreslení ve výkonových zesilovačích ve srovnání s modulacemi měnícími amplitudu.

Ve stohu protokolů 3GPP je BPSK specifikováno ve specifikacích fyzické vrstvy pro různé technologie rádiového přístupu. V UMTS (3G) je definováno v TS 25.211 pro fyzické kanály a mapování transportních kanálů na fyzické kanály a v TS 25.222 pro multiplexování a kanálové kódování. Pro LTE (4G) je jeho použití podrobně popsáno v TS 36.201 pro obecný popis fyzické vrstvy a pro NR (5G) v TS 38.201. Úloha BPSK je často vyhrazena pro kritické řídicí informace, synchronizační signály a vysílací kanály, kde je spolehlivost nadřazena spektrální účinnosti. Například Primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)) a některé složky Fyzického vysílacího kanálu ([PBCH](/mobilnisite/slovnik/pbch/)) v LTE a NR mohou používat BPSK nebo jeho derivát, π/2-BPSK, aby zajistily robustní vyhledávání buňky a získávání systémových informací za náročných rádiových podmínek.

Výkon BPSK je charakterizován mírou bitových chyb ([BER](/mobilnisite/slovnik/ber/)) Q(√(2E_b/N_0)) pro koherentní detekci v kanálu s AWGN, kde E_b je energie na bit a N_0 je spektrální hustota výkonu šumu. To vede k požadavku přibližně 10,6 dB E_b/N_0 pro BER 10^-6. Zatímco jeho spektrální účinnost je pouze 1 bit/s/Hz, jeho energetická účinnost je optimální pro binární přenos. V moderních systémech založených na [OFDM](/mobilnisite/slovnik/ofdm/), jako jsou LTE a NR, se modulace BPSK aplikuje na jednotlivé subnosné. Varianta π/2-BPSK byla zavedena za účelem snížení poměru špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)) rotací konstelace o π/2 na střídavých symbolech, což je zvláště výhodné pro uplinkové přenosy ke zlepšení účinnosti výkonového zesilovače.

## K čemu slouží

BPSK bylo vyvinuto jako základní technika digitální modulace, která poskytuje jednoduchou a vysoce spolehlivou metodu pro přenos binárních dat přes rádiové kanály. Jeho primárním účelem v raných digitálních komunikačních systémech a následně ve standardech 3GPP od Release 99 bylo zajistit robustní přenos pro řídicí signalizaci a kritické systémové informace, kde je integrita dat důležitější než vysoké přenosové rychlosti. Před přijetím sofistikovaných modulačních schémat, jako je 64-QAM nebo 256-QAM, pro uživatelská data, sloužilo BPSK jako základní linie, nabízející maximální odolnost proti šumu díky 180stupňovému fázovému oddělení mezi jeho dvěma symbolovými stavy, což odpovídá největší možné eukleidovské vzdálenosti v dvoubodové konstelaci.

Historická motivace pro zahrnutí BPSK do standardů 3GPP vychází z potřeby modulačního schématu s předvídatelným výkonem za podmínek nízkého poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)) a ve fadingovém prostředí. V kontextu 2G GSM se používala Gaussovská minimální fázová manipulace ([GMSK](/mobilnisite/slovnik/gmsk/)), což je modulace s konstantní obálkou. Pro 3G UMTS poskytovala volba BPSK (a QPSK) pro downlink dobrou rovnováhu mezi složitostí a výkonem. BPSK řešilo omezení analogové FM modulace používané v dřívějších systémech 1. generace, která byla neefektivní ve využití spektra a náchylná k šumu. Jeho matematická zpracovatelnost a dobře prozkoumaný výkon v teoretických analýzách z něj navíc učinily ideálního kandidáta pro standardizaci, což zajišťuje interoperabilitu mezi zařízeními od různých výrobců.

Ve vyvíjejících se systémech 3GPP BPSK nadále řeší konkrétní problém přenosu nezbytných řídicích informací s vysokou spolehlivostí. Zatímco pro datové kanály se používají modulace vyšších řádů k maximalizaci propustnosti, řídicí kanály odpovědné za přístup k systému, plánovací povolení, příkazy k předání a synchronizaci musí být dekódovatelné na okraji buňky za špatných kanálových podmínek. Odolnost BPSK jej činí vhodným pro tyto funkce. Jeho jednoduchost také snižuje složitost přijímače a spotřebu energie pro dekódování těchto neustále aktivních signálů, což je zvláště důležité pro zařízení IoT s omezenou baterií zavedená v pozdějších releasech, jako jsou LTE-M a NB-IoT.

## Klíčové vlastnosti

- Dva antipodální fázové stavy (0° a 180°) reprezentující binární 0 a 1
- Optimální energetická účinnost a maximální odolnost proti šumu pro binární přenos
- Vlastnost konstantní obálky snižující citlivost na nelineární zkreslení zesilovače
- Koherentní detekce vyžadující přesnou obnovu fáze nosné na přijímači
- Spektrální účinnost 1 bit/s/Hz
- Základ pro odvozená schémata jako π/2-BPSK používaná ke snížení poměru špičkového a průměrného výkonu (PAPR)

## Související pojmy

- [QPSK – Quadrature Phase Shift Keying](/mobilnisite/slovnik/qpsk/)
- [QAM – Quadrature Amplitude Modulation](/mobilnisite/slovnik/qam/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [BPSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/bpsk/)
