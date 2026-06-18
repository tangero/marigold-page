---
slug: "ttota"
url: "/mobilnisite/slovnik/ttota/"
type: "slovnik"
title: "TTOTA – Test Tolerance for Over-The-Air"
date: 2025-01-01
abbr: "TTOTA"
fullName: "Test Tolerance for Over-The-Air"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ttota/"
summary: "TTOTA definuje přípustné odchylky měření pro testování Over-The-Air (OTA) rádiových zařízení, zejména pro 5G NR. Zajišťuje opakovatelnost a spravedlivost testů tím, že zohledňuje inherentní nejistoty"
---

TTOTA je definovaná přípustná odchylka měření pro testování Over-The-Air (přes vzduch), která zohledňuje nejistoty v testovacích komorách a anténních charakteristikách, aby bylo zajištěno opakovatelné a spravedlivé certifikování rádiových zařízení.

## Popis

TTOTA (Test Tolerance for Over-The-Air) je soubor standardizovaných parametrů definovaných ve specifikacích 3GPP, které stanovují přijatelné chybové tolerance pro měření prováděná v [OTA](/mobilnisite/slovnik/ota/) testovacích prostředích. Na rozdíl od vedeného testování, které používá přímá kabelová propojení, OTA testování vyhodnocuje vyzařovaný výkon kompletního anténního systému zařízení v řízené, anekonické komoře. Tato metoda je nezbytná pro moderní zařízení s integrovanými, neodnímatelnými anténami. Hodnoty TTOTA zohledňují různé nejistoty vlastní procesu OTA měření. Ty zahrnují nedokonalosti anekonické komory (např. odrazy), chyby kalibrace sondovací antény, nepřesnosti v pozicování testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)) a statistickou povahu měření vyzařovaných polí. Pro každý konkrétní testovací případ – jako je Celkový vyzařovaný výkon ([TRP](/mobilnisite/slovnik/trp/)), Celková izotropní citlivost (TIS) nebo zisk beamformingu – příslušná specifikace 3GPP (např. 38.141 pro testování základnových stanic) stanovuje hodnotu TTOTA, často vyjádřenou v decibelech (dB).

Architektura pro aplikaci TTOTA je zabudována do logiky posouzení shody testovacího systému. Testovací laboratoř změří klíčový výkonnostní ukazatel ([KPI](/mobilnisite/slovnik/kpi/)), jako je výstupní výkon. Tato naměřená hodnota je pak porovnána s absolutní mezní hodnotou definovanou ve standardu. TTOTA poskytuje 'ochranný pás' kolem této meze. Pokud naměřená hodnota po aplikaci tolerance TTOTA (buď přičtené nebo odečtené v závislosti na tom, zda se jedná o horní nebo dolní mez) stále porušuje absolutní limit, zařízení testem neprojde. Tím je zajištěno, že zařízení, které testem projde, tak učiní s rezervou, která zohledňuje reálný šum měření, a garantuje tak robustní výkon.

Klíčové komponenty ovlivněné TTOTA zahrnují samotnou testovací komoru (kvalita tiché zóny), měřicí přijímač, systém pro pozicování a referenční anténu. Její role je v zásadě o zajištění kvality a standardizaci. Definováním těchto tolerancí 3GPP zajišťuje, že certifikační testy jsou reprodukovatelné v různých laboratořích po celém světě, a zabraňuje tak situacím, kdy zařízení projde v jedné laboratoři, ale v jiné neprojde pouze kvůli odlišnostem měřicího systému. Vytváří rovné podmínky pro výrobce zařízení a síťové operátory a zajišťuje, že všechna certifikovaná zařízení splňují minimální, ověřitelný výkonnostní práh v realistických podmínkách vyzařování.

## K čemu slouží

TTOTA byla vytvořena, aby řešila základní výzvy a nejistoty zavedené povinným přechodem od vedeného testování k testování Over-The-Air pro moderní rádiová zařízení, zejména s příchodem 5G New Radio (NR). Starší mobilní technologie často měly externí anténní konektory, což umožňovalo přímé, vedené testování s vysokou přesností a opakovatelností. Trend průmyslu směrem k elegantním, uzavřeným zařízením s integrovanými anténami a použití pokročilých anténních systémů ([AAS](/mobilnisite/slovnik/aas/)) a beamformingu v 5G však učinily vedené testování nepraktickým nebo nemožným. [OTA](/mobilnisite/slovnik/ota/) testování se stalo jedinou životaschopnou metodou.

Hlavním problémem, který TTOTA řeší, je nedostatek konzistence v OTA měřeních. Bez standardizovaných tolerancí by různé testovací laboratoře používající různé návrhy komor, kalibrační metody a vybavení mohly pro stejné zařízení dosáhnout výrazně odlišných výsledků. To by vedlo k zmatku na trhu, nekonzistentní kvalitě zařízení a potenciálním právním sporům během certifikace. TTOTA poskytuje potřebný rámec 'chyby měření', který bere v potaz fyziku vyzařovaných měření a zároveň vynucuje společný srovnávací základ. Byla motivována potřebou zachovat integritu certifikačního procesu 3GPP a zajistit, aby výsledek 'vyhověl' spolehlivě indikoval zařízení, které bude adekvátně fungovat v živé síti, navzdory nedokonalostem jakéhokoli jednotlivého testovacího uspořádání.

## Klíčové vlastnosti

- Definuje přípustné chybové tolerance pro vyzařovaná RF měření v anekonických komorách
- Zajišťuje reprodukovatelnost a spravedlivost testovacích výsledků v různých laboratořích po celém světě
- Aplikuje se na klíčové OTA metriky jako Celkový vyzařovaný výkon (TRP) a Celková izotropní citlivost (TIS)
- Specifikováno odděleně pro testování základnových stanic (gNB) a uživatelských zařízení (UE) v příslušných specifikacích
- Nedílná součást procesu testování shody a certifikace zařízení pro 5G NR
- Zohledňuje nejistoty ve výkonu komory, kalibraci sondy a pozicování testovaného zařízení (DUT)

## Související pojmy

- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing

---

📖 **Anglický originál a plná specifikace:** [TTOTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttota/)
