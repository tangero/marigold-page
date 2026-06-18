---
slug: "rf"
url: "/mobilnisite/slovnik/rf/"
type: "slovnik"
title: "RF – Repeater type 2-O"
date: 2026-01-01
abbr: "RF"
fullName: "Repeater type 2-O"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rf/"
summary: "Specifický typ opakovače pracujícího ve frekvenčním rozsahu 2 (FR2, pásma mmWave) se souborem požadavků definovaných výhradně metrikami výkonu Over-The-Air (OTA) na rozhraní rádiového rozhraní (Radio"
---

RF je typ opakovače pro pásma FR2 (mmWave), jehož výkonnostní požadavky jsou definovány výhradně metrikami Over-The-Air na rozhraní rádiového rozhraní (Radio Interface Boundary) a který se používá k rozšíření pokrytí v sítích 5G.

## Popis

RF (Repeater type 2-O) je síťová komponenta definovaná v rámci standardů 3GPP, speciálně navržená pro provoz ve frekvenčním rozsahu 2 (FR2), který zahrnuje pásma milimetrových vln (mmWave) typicky od 24,25 GHz do 52,6 GHz. Jejím hlavním účelem je přijímat, zesilovat a retransmitovat rádiové signály, čímž rozšiřuje oblast pokrytí základnové stanice (gNB) a zlepšuje sílu signálu pro uživatelské zařízení (UE) v náročných podmínkách šíření. Na rozdíl od tradičních opakovačů s komplexním testováním shody klasifikace 'type 2-O' znamená, že jeho výkon a regulační shoda jsou hodnoceny výhradně prostřednictvím měření Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) na rozhraní rádiového rozhraní ([RIB](/mobilnisite/slovnik/rib/)). To znamená, že všechny požadavky – jako výstupní výkon, limity nežádoucích emisí a charakteristiky přijímače – jsou ověřovány pomocí radiačního testování v anechogenní komoře nebo ekvivalentním uspořádání, bez nutnosti vodivého testovacího portu. RIB je konceptuální rovina, kde jsou uvažovány anténní konektory opakovače, což zdůrazňuje integrovaný anténní systém typický pro zařízení mmWave.

Z architektonického hlediska je RF opakovač obousměrné plně duplexní zařízení. Skládá se z dárčí antény namířené k obsluhující gNB pro příjem signálu downlink, výkonového zesilovače pro zesílení signálu a služební antény, která retransmituje zesílený signál k UE. Uplinková cesta funguje obdobně opačným směrem. Mezi klíčové vnitřní komponenty patří šumově nízké zesilovače ([LNA](/mobilnisite/slovnik/lna/)), filtry pro izolaci pracovního pásma a potlačení rušení a obvody pro řízení zesílení, které zabraňují oscilacím a řídí výstupní výkon. U typu 2-O je celá jednotka včetně antén považována za integrovaný celek; výkon nelze oddělit od charakteristik antény. Tento návrh je klíčový pro frekvence mmWave, kde jsou beamforming a integrace antén inherentní součástí technologie.

V síti jsou RF opakovače nasazovány jako nákladově efektivní řešení pro rozšíření pokrytí, zejména v sítích mmWave, kde signály trpí vysokým útlumem na dráze a špatnou prostupností překážkami. Mohou vyplnit díry v pokrytí uvnitř budov nebo venku (např. v uličních kaňonech). Protože pracují na vrstvě 1 (fyzické vrstvě), jsou pro síť transparentní – nedekódují ani nemodifikují obsah signálu, což je činí jednoduššími a s nižší latencí než small cells nebo přenosové uzly. Avšak také zesilují šum a rušení, což vyžaduje pečlivé umístění a konfiguraci. Jejich role je klíčová v hustých městských nasazeních 5G pro zajištění konzistentního vysokorychlostního připojení bez nákladů na nasazení dalších základnových stanic.

## K čemu slouží

RF opakovač typu 2-O byl vytvořen, aby řešil jedinečné výzvy nasazování sítí 5G v milimetrovém spektru. Frekvence mmWave nabízejí obrovskou šířku pásma pro vícegigabitové datové rychlosti, ale trpí závažnými omezeními šíření: krátkým dosahem, vysokým útlumem od stěn a vegetace a citlivostí na překážky. Nasazení husté sítě plnohodnotných základnových stanic je ekonomicky neúnosné. Opakovače poskytují nákladově nižší alternativu pro rozšíření pokrytí z existujících gNB do zastíněných oblastí, jako jsou vnitřky budov, rohy ulic nebo podzemní prostory. Specifikace 'type 2-O' s požadavky pouze na [OTA](/mobilnisite/slovnik/ota/) odráží praktickou realitu hardwaru mmWave, kde jsou antény často fyzicky integrovány s rádiovou předkoncovou částí, což činí vodivé testování nepraktickým nebo bezvýznamným.

Historicky měly opakovače pro nižší pásma (např. FR1) často vodivé testovací porty, což umožňovalo ověřit výkon nezávisle na anténě. S postupem 5G do FR2 průmysl uznal potřebu standardizované kategorie opakovače, která by zohledňovala integrované anténní pole používané pro beamforming. Přístup OTA zajišťuje, že opakovač je testován tak, jak bude nasazen v terénu, a zachycuje kombinovaný výkon rádiového a anténního systému. Tato standardizace poskytuje jasnost výrobcům zařízení, síťovým operátorům a regulátorům a zajišťuje interoperabilitu a konzistentní výkonnostní standardy v celém odvětví.

Dále tím, že definuje specifický soubor požadavků, umožňuje 3GPP vývoj opakovačů optimalizovaných pro charakteristiky mmWave, jako je podpora širokých šířek pásma (např. 400 MHz a více) a zvládnutí beam-based povahy komunikace. Tím se řeší omezení předchozích návrhů opakovačů, které nebyly přizpůsobeny vysokým frekvencím a komplexním prostorovým charakteristikám 5G NR. Usnadňuje to rychlé zahušťování sítě a zlepšuje ekonomickou životaschopnost služeb 5G mmWave.

## Klíčové vlastnosti

- Pracuje výhradně v pásmech FR2 (mmWave) (např. 24,25–52,6 GHz)
- Výkonnostní požadavky definovány výhradně testováním Over-The-Air (OTA) na rozhraní rádiového rozhraní (Radio Interface Boundary)
- Integrovaný anténní systém, typický pro zařízení mmWave s beamformingem
- Transparentně zesiluje a retransmituje signály downlink i uplink (vrstva 1)
- Rozšiřuje pokrytí a zlepšuje kvalitu signálu v prostředích s vysokým útlumem na dráze
- Podléhá specifickým 3GPP testům shody pro výstupní výkon, nežádoucí emise a parametry přijímače

## Související pojmy

- [OTA – Over The Air](/mobilnisite/slovnik/ota/)
- [RIB – Radiated Interface Boundary](/mobilnisite/slovnik/rib/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- … a dalších 115 specifikací

---

📖 **Anglický originál a plná specifikace:** [RF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rf/)
