---
slug: "spdcch"
url: "/mobilnisite/slovnik/spdcch/"
type: "slovnik"
title: "SPDCCH – Short Physical Downlink Control Channel"
date: 2025-01-01
abbr: "SPDCCH"
fullName: "Short Physical Downlink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/spdcch/"
summary: "Řídicí kanál v downlinku pro LTE-M a NB-IoT navržený s kratším přenosovým časovým intervalem pro snížení spotřeby energie zařízení a latence. Přenáší klíčové řídicí informace, jako jsou povolení pro u"
---

SPDCCH (krátký fyzický řídicí kanál v downlinku) je kanál v technologiích LTE-M a NB-IoT navržený s kratší dobou přenosu za účelem snížení spotřeby energie a latence, který přenáší nezbytné řídicí informace pro IoT zařízení.

## Popis

Short Physical Downlink Control Channel (SPDCCH) je specializovaný fyzický kanál zavedený pro zařízení LTE-M (Cat-M1) a NB-IoT ve specifikacích 3GPP Release 15 a novějších. Jedná se o variantu Enhanced Physical Downlink Control Channel ([EPDCCH](/mobilnisite/slovnik/epdcch/)) optimalizovanou pro potřeby aplikací Cellular Internet of Things (CIoT). Primárním cílem návrhu SPDCCH je extrémní energetická účinnost zařízení, které je dosaženo výrazným zkrácením doby přenosu. Na rozdíl od starších kanálů [PDCCH](/mobilnisite/slovnik/pdcch/)/EPDCCH, které zabírají první 1-3 [OFDM](/mobilnisite/slovnik/ofdm/) symboly subrámce, je SPDCCH omezen na jeden subrámec (1 ms) nebo i kratší dobu, což umožňuje, aby byl přijímač zařízení aktivní po mnohem kratší dobu pro dekódování řídicích informací.

Z hlediska fyzické struktury zabírá SPDCCH specifické zdrojové elementy v rámci úzkopásmového přenosu (pro LTE-M) nebo jednoho fyzického bloku zdrojů (pro NB-IoT). Používá konfigurovatelnou úroveň agregace (např. 2, 4, 8 bloků zdrojů) pro poskytnutí adaptace spojení zařízením v různých podmínkách kanálu. Kanál přenáší formáty Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) přizpůsobené pro CIoT, jako jsou povolení pro uplink pro přenosy na fyzickém sdíleném kanálu uplinku ([PUSCH](/mobilnisite/slovnik/pusch/)) a přiřazení pro downlink pro fyzický sdílený kanál downlinku ([PDSCH](/mobilnisite/slovnik/pdsch/)). Klíčovým provozním aspektem je jeho asociace se specifickými vyhledávacími prostory nakonfigurovanými pro zařízení. UE monitoruje tyto předdefinované sady kandidátů na SPDCCH během svých nakonfigurovaných cyklů [DRX](/mobilnisite/slovnik/drx/) nebo eDRX.

SPDCCH funguje v součinnosti s dalšími funkcemi CIoT, jako jsou režimy Coverage Enhancement ([CE](/mobilnisite/slovnik/ce/)) a Power Saving Mode (PSM). Jeho kratší doba trvání přímo snižuje energii potřebnou pro dekódování řídicího kanálu, což je častá aktivita. Umožněním rychlejšího dekódování také snižuje latenci pro transakce řídicí roviny. Síť konfiguruje parametry SPDCCH (periodicitu, zdroje) pomocí signalizace RRC nebo systémových informací, což umožňuje flexibilní nasazení. Jeho zavedení bylo součástí širší sady vylepšení, jejichž cílem bylo učinit LTE konkurenceschopnější technologií pro masivní, nízkopříkonová a hlubokopokrytí IoT nasazení.

## K čemu slouží

SPDCCH byl vytvořen, aby řešil významné nedostatky stávajících LTE řídicích kanálů v oblasti spotřeby energie a latence při použití pro IoT zařízení. Před jeho zavedením zařízení LTE-M a NB-IoT spoléhala na MPDCCH (pro LTE-M) nebo NPDCCH (pro NB-IoT), které samy o sobě byly vylepšením oproti PDCCH, ale stále představovaly energetickou zátěž. Hlavním problémem bylo, že dekódování těchto řídicích kanálů vyžadovalo, aby bylo rádiové rozhraní zařízení aktivní po dobu několika subrámců, což je dominantní zdroj vybíjení baterie u IoT zařízení v připojeném režimu, která často kontrolují čekající data nebo přenášejí malé hlášení.

Motivace pro SPDCCH vycházela z potřeby prodloužit životnost baterie IoT zařízení za hranici 10 let a podpořit aplikace citlivější na latenci. Kratší doba přenosu SPDCCH přímo znamená, že energeticky náročné obvody RF a základního pásma zařízení musí být aktivní po kratší dobu. Tím se řeší kritická překážka pro adopci IoT v oblasti utilities, sledování majetku a nositelné elektroniky. Navíc snížením doby dekódování řídicího kanálu se také snižuje latence pro nastavení přenosu dat, což umožňuje lepší podporu aplikací vyžadujících rychlejší odezvu komunikace. Byl součástí pracovní položky "Further LTE Physical Layer Enhancements for MTC" v Release 15, řízené požadavky trhu na IoT řešení, která jsou zároveň ultra-nízkopříkonová a schopná zlepšeného výkonu.

## Klíčové vlastnosti

- Krátká doba přenosu (např. jeden subrámec) pro snížení spotřeby energie UE
- Přenáší formáty DCI specifické pro CIoT pro povolení uplink a přiřazení downlink
- Funguje v rámci úzkopásmového přenosu pro LTE-M nebo jednoho PRB pro NB-IoT
- Podporuje konfigurovatelné úrovně agregace pro zvýšení pokrytí
- Je asociován s uživatelsky specifickými vyhledávacími prostory pro efektivní blind dekódování
- Integruje se s eDRX a PSM pro prodloužení životnosti baterie

## Související pojmy

- [MPDCCH – MTC Physical Downlink Control Channel](/mobilnisite/slovnik/mpdcch/)
- [NPDCCH – Narrow Band Physical Downlink Control Channel](/mobilnisite/slovnik/npdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [SPDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/spdcch/)
