---
slug: "dmsu"
url: "/mobilnisite/slovnik/dmsu/"
type: "slovnik"
title: "DMSU – Data Mode Screen Up"
date: 2025-01-01
abbr: "DMSU"
fullName: "Data Mode Screen Up"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/dmsu/"
summary: "DMSU je mechanismus měření a hlášení v NR (New Radio) pro hlášení výkonové rezervy (PHR) uživatelského zařízení (UE). Umožňuje UE hlásit dostupnou rezervu vysílacího výkonu pro různé módy přenosu dat,"
---

DMSU je mechanismus v 5G NR, který umožňuje uživatelskému zařízení (UE) hlásit svou dostupnou rezervu vysílacího výkonu pro různé datové módy, čímž napomáhá řízení výkonu v uplinku a plánování.

## Popis

Data Mode Screen Up (DMSU) je specifický postup a formát hlášení definovaný ve specifikacích 3GPP NR pro hlášení výkonové rezervy (Power Headroom Reporting – PHR). Hlášení výkonové rezervy (PHR) je klíčové měření UE, které informuje gNB (Next Generation NodeB) o rozdílu mezi maximálním vysílacím výkonem UE a odhadovaným výkonem potřebným pro její aktuální uplinkový přenos. DMSU toto hlášení zpřesňuje tím, že poskytuje informace o rezervě výkonu podmíněné konkrétními 'datovými módy' neboli konfiguracemi přenosu.

Během provozu UE vypočítává výkonovou rezervu pro více hypotetických nebo skutečných přenosových scénářů. Tyto scénáře jsou definovány různými kombinacemi modulačních a kódových schémat ([MCS](/mobilnisite/slovnik/mcs/)), částí šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), počtu vrstev (pro [MIMO](/mobilnisite/slovnik/mimo/)) a případně dalších přenosových parametrů, které tvoří 'datový mód'. UE tyto módy vyhodnocuje (screens) a hlásí výsledné hodnoty výkonové rezervy. Tento proces zahrnuje interní výpočty, při nichž UE odhaduje potřebný vysílací výkon (P_required) pro referenční přenosový formát na dané nosné a porovnává jej se svým maximálním výkonem (P_cmax). Hlášená rezerva, často záporná hodnota označující nedostatek výkonu, je specifická pro předpokládaný datový mód.

Z architektonického hlediska je hlášení DMSU spouštěno událostmi, jako je změna útlumu na trase (pathloss), vypršení periodického časovače nebo konfigurace ze strany gNB prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/). Hlášení je přenášeno v rámci řídicího elementu [MAC](/mobilnisite/slovnik/mac/) (MAC [CE](/mobilnisite/slovnik/ce/)) na sdíleném kanálu pro uplink (UL-SCH). Plánovač gNB používá tyto podrobné informace o rezervě výkonu pro každý datový mód k přijímání informovaných rozhodnutí. Například se může vyhnout naplánování vysokého MCS na široký BWP pro UE, pokud hlášení DMSU pro tento mód ukazuje zápornou rezervu, a místo toho zvolit robustnější, ale spektrálně efektivnější alternativu, kterou může UE se svým dostupným výkonem podporovat.

Jeho role je zásadní pro dosažení vysoké spektrální efektivity a spolehlivosti v uplinku 5G NR, zejména v náročných rádiových podmínkách na okraji buňky nebo u zařízení s omezeným výkonem. Tím, že poskytuje podrobný vhled do výkonových omezení UE napříč různými přenosovými možnostmi, umožňuje DMSU síti optimalizovat přidělování zdrojů pro uplink (uplink grants), předcházet neúspěšným přenosům z důvodu nedostatku výkonu a udržovat kvalitu spoje, což přímo ovlivňuje propustnost pro uživatele a kapacitu sítě.

## K čemu slouží

DMSU bylo zavedeno, aby odstranilo omezení jednodušších mechanismů hlášení výkonové rezervy (PHR) používaných v LTE. V LTE bylo PHR poměrně hrubé a často hlásilo jedinou hodnotu rezervy na nosnou bez explicitního přiřazení ke konkrétnímu přenosovému formátu. S příchodem 5G NR, který přinesl dynamičtější a flexibilnější parametry uplinkového přenosu – jako jsou širší a různorodější části šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), agresivnější schémata [MCS](/mobilnisite/slovnik/mcs/) a složité víceanténní techniky – se stará metoda hlášení stala nedostatečnou. Plánovač gNB potřeboval jemněji odlišená data, aby pochopil nejen to, zda má UE ještě výkonovou rezervu, ale také pro jaký typ přenosu je tento výkon k dispozici.

Primární problém, který DMSU řeší, je neefektivita a potenciální selhání spoje způsobené nevhodným plánováním. Bez rezervy specifické pro mód by gNB mohlo naplánovat pro UE přenos s vysokým řádem modulace (např. 256QAM) v domnění, že má dostatek výkonu, zatímco UE ve skutečnosti nemá dostatek výkonu k dosažení potřebného SNR, což vede k chybám bloků. Naopak, gNB by mohlo být příliš konzervativní. DMSU poskytuje potřebnou granularitu pro přesnou adaptaci spoje a řízení výkonu v uplinku, což je klíčové pro splnění cílů 5G v oblasti vysoké spolehlivosti a vysoké propustnosti, zejména v případech použití rozšířené mobilní širokopásmové služby (eMBB) a ultra-spolehlivé nízkolatenční komunikace (URLLC).

Historicky bylo jeho vytvoření motivováno potřebou efektivnější podpory agregace nosných (CA) a duální konektivity (DC) v NR, kde UE vysílá na více buňkách s potenciálně odlišnými výkonovými omezeními. DMSU umožňuje hlášení pro každou nosnou a každý datový mód zvlášť, čímž poskytuje síti úplný přehled o výkonových možnostech UE v celém jejím aktivním souboru, a umožňuje tak optimální distribuci zdrojů napříč agregovanými nosnými.

## Klíčové vlastnosti

- Výpočet a hlášení výkonové rezervy specifické pro daný mód
- Podporuje hlášení pro více aktivních částí šířky pásma (BWP)
- Integruje se se scénáři agregace nosných (CA) a duální konektivity (DC)
- Spouštěno událostmi, jako je změna útlumu na trase, periodické časovače nebo konfigurace RRC
- Hlášení přenášeno prostřednictvím řídicího elementu MAC (MAC CE) na UL-SCH
- Umožňuje granularní plánování uplinku a přesnou adaptaci spoje ze strany gNB

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology

---

📖 **Anglický originál a plná specifikace:** [DMSU na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmsu/)
