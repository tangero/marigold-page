---
slug: "plcch"
url: "/mobilnisite/slovnik/plcch/"
type: "slovnik"
title: "PLCCH – Physical Layer Common Control Channel"
date: 2025-01-01
abbr: "PLCCH"
fullName: "Physical Layer Common Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/plcch/"
summary: "Downlinkový fyzický kanál v UMTS přenášející řídicí informace společné všem uživatelům nebo skupině uživatelů v rámci buňky. Je primárně spojován s funkcí High Speed Downlink Packet Access (HSDPA) a v"
---

PLCCH je v UMTS downlinkový fyzický kanál, který nese společnou řídicí informaci, primárně pro HSDPA, za účelem signalizace přidělení zdrojů pro HS-DSCH.

## Popis

Physical Layer Common Control Channel (PLCCH) je specifický typ downlinkového fyzického kanálu definovaného v specifikacích UMTS Terrestrial Radio Access ([UTRA](/mobilnisite/slovnik/utra/)), zejména pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Je součástí architektury High Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) zavedené ve vydání 5. PLCCH slouží k přenosu řídicí signalizace související s kanálem High Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)), který je primárním kanálem pro vysokorychlostní přenos paketových dat. Na rozdíl od vyhrazených kanálů je PLCCH společným zdrojem, což znamená, že jeho informace jsou určeny pro více uživatelských zařízení (UE) nebo pro všechna UE v buňce.

Technicky je PLCCH mapován na fyzický kanál Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)). Nese informaci transportního kanálu High Speed Shared Control Channel ([HS-SCCH](/mobilnisite/slovnik/hs-scch/)). HS-SCCH je transportní kanál, který přenáší downlinkovou signalizaci nezbytnou pro dekódování HS-DSCH uživatelským zařízením. Tato signalizace zahrnuje kritické parametry, jako je sada kanalizačních kódů, modulační schéma ([QPSK](/mobilnisite/slovnik/qpsk/) nebo 16-QAM), velikost transportního bloku a informace o procesu Hybrid [ARQ](/mobilnisite/slovnik/arq/) (HARQ). Fyzické zpracování PLCCH zahrnuje kanálové kódování, prokládání a modulaci, podobně jako u jiných fyzických kanálů, předtím, než je kombinován s dalšími kanály pro vysílání.

Provoz je těsně spojen s přenosovým časovým intervalem (TTI) HSDPA o délce 2 ms. Pro každý TTI Node B naplánuje jedno nebo více UE pro přenos dat na HS-DSCH. Současně vysílá odpovídající řídicí informaci na PLCCH (prostřednictvím HS-SCCH) jeden až dva sloty před přidruženými daty HS-DSCH. UE kontinuálně monitoruje sadu HS-SCCH (PLCCH). Když detekuje řídicí informaci adresovanou jí (pomocí specifického dočasného identifikátoru HS-DSCH Radio Network Temporary Identifier, H-RNTI), použije UE dekódované parametry k řádnému příjmu a dekódování dat na HS-DSCH. PLCCH je tedy klíčovým fyzickým kanálem, který umožňuje rychlé, dynamické a sdílené přidělování zdrojů, jež je charakteristickým znákem výkonnostních zisků HSDPA.

## K čemu slouží

PLCCH byl zaveden s HSDPA ve vydání 5, aby vyřešil klíčové úzké místo v dřívějších vydáních UMTS (Rel-99/4). V systémech před zavedením HSDPA byla downlinková paketová data vysílána primárně na vyhrazených kanálech (DCH), kde byla řídicí signalizace pro plánování a adaptaci spojení zpracovávána prostřednictvím pomalejších mechanismů založených na Radiové síťové stanici (RNC) a vyhrazených řídicích kanálů. To vedlo k vysoké latenci a neefektivnímu využití zdrojů, což bylo nevhodné pro nerovnoměrný, vysokorychlostní internetový provoz.

Účelem PLCCH bylo umožnit rychlé plánování na úrovni buňky v Node B (základnové stanici). Zavedením společného řídicího kanálu mohl Node B rychle signalizovat rozhodnutí o plánování přímo uživatelským zařízením na základě každého 2ms TTI. To přesunulo kritické řídicí funkce z RNC do Node B, což drasticky snížilo latenci a umožnilo plánování závislé na stavu kanálu (rychlou adaptaci spojení) na základě okamžitých rádiových podmínek. PLCCH, který nese HS-SCCH, se stal fyzickým prostředkem pro tento posun paradigmatu, což umožnilo více uživatelům dynamicky a efektivně sdílet vysokorychlostní datový kanál. Vyřešil tak omezení vyhrazeného přidělování zdrojů a umožnil dosažení podstatně vyšších špičkových přenosových rychlostí a spektrální účinnosti pro downlinkové paketové služby.

## Klíčové vlastnosti

- Nese transportní kanál HS-SCCH pro řídicí signalizaci HSDPA
- Mapován na fyzický kanál S-CCPCH
- Přenáší kritické parametry pro dekódování HS-DSCH (kódy, modulace, informace HARQ)
- Funguje s 2ms TTI synchronizovaným s plánováním HSDPA
- Společný kanálový zdroj monitorovaný více UE v buňce
- Umožňuje rychlé plánování a adaptaci spojení zaměřené na Node B

## Související pojmy

- [HS-SCCH – High Speed Physical Downlink Shared Control Channel](/mobilnisite/slovnik/hs-scch/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [H-ARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/h-arq/)

## Definující specifikace

- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [PLCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/plcch/)
