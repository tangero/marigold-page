---
slug: "sssg"
url: "/mobilnisite/slovnik/sssg/"
type: "slovnik"
title: "SSSG – Search Space Set Group"
date: 2025-01-01
abbr: "SSSG"
fullName: "Search Space Set Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sssg/"
summary: "Mechanismus pro seskupování sad vyhledávacích prostorů PDCCH v 5G NR, zavedený ve verzi 17 (Release 17). Umožňuje uživatelskému zařízení (UE) monitorovat kandidáty PDCCH pouze z podmnožiny nakonfiguro"
---

SSSG je mechanismus pro seskupování sad vyhledávacích prostorů PDCCH zavedený ve verzi 17 (Release 17), který umožňuje uživatelskému zařízení (UE) monitorovat vždy pouze jejich podmnožinu, čímž snižuje počet pokusů o slepý dekódování a šetří energii.

## Popis

Search Space Set Group (SSSG, skupina sad vyhledávacích prostorů) je funkce v 5G New Radio (NR), která logicky seskupuje více sad vyhledávacích prostorů [PDCCH](/mobilnisite/slovnik/pdcch/) (Physical Downlink Control Channel) nakonfigurovaných pro uživatelské zařízení (UE). Sada vyhledávacího prostoru definuje, kde v čase a frekvenci (z hlediska sad řídicích zdrojů - [CORESET](/mobilnisite/slovnik/coreset/)ů) se má UE pokoušet slepě dekódovat potenciální přenosy PDCCH nesoucí informace o řízení downlinku ([DCI](/mobilnisite/slovnik/dci/)). Před verzí 17 muselo UE s více aktivními sadami vyhledávacích prostorů v každé monitorovací příležitosti potenciálně monitorovat kandidáty PDCCH napříč všemi těmito sadami, což vedlo k vysoké výpočetní složitosti a spotřebě energie.

Mechanismus SSSG umožňuje síti (gNB) nakonfigurovat pro UE prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) jednu nebo více SSSG. Každá SSSG obsahuje podmnožinu celkového počtu nakonfigurovaných sad vyhledávacích prostorů UE. Klíčové je, že síť může následně dynamicky aktivovat nebo deaktivovat konkrétní SSSG pomocí příkazu řídicího prvku [MAC](/mobilnisite/slovnik/mac/) (MAC [CE](/mobilnisite/slovnik/ce/)). Když je SSSG aktivována, je UE povinno monitorovat kandidáty PDCCH pouze v rámci sad vyhledávacích prostorů patřících do této aktivní skupiny. Může ignorovat sady vyhledávacích prostorů, které v aktivní skupině nejsou. Síť může přepínat UE mezi různými SSSG na základě provozní aktivity, což umožňuje formu dynamické úspory energie. Například jedna SSSG může obsahovat sady vyhledávacích prostorů pro plánovací povolení (vyžadující častější monitorování), zatímco jiná může obsahovat pouze minimální sadu pro paging nebo indikaci předběžného přerušení.

Z architektonického hlediska je konfigurace SSSG součástí informačního prvku PDCCH-Config. UE může být nakonfigurováno s více SSSG, každá s identifikátorem. Aktivace/deaktivace je řešena vrstvou MAC, což poskytuje rychlou rekonfiguraci bez režie signalizace RRC. Toto seskupování je zvláště výhodné pro pokročilé funkce zavedené v pozdějších verzích, jako je provoz s více paprsky a přenos s více [TRP](/mobilnisite/slovnik/trp/) (Transmission Reception Point), kde může být UE nakonfigurováno s velkým počtem sad vyhledávacích prostorů spojených s různými paprsky nebo TRP. Namísto monitorování všech možností může síť navést UE, aby monitorovalo pouze relevantní skupinu pro své aktuální podmínky, což významně snižuje počet pokusů o slepé dekódování na slot a tím šetří životnost baterie UE.

## K čemu slouží

SSSG byla zavedena ve specifikaci 3GPP Release 17 primárně za účelem řešení rostoucí složitosti a spotřeby energie spojené s monitorováním [PDCCH](/mobilnisite/slovnik/pdcch/) v pokročilých nasazeních 5G NR. Jak se NR vyvíjelo k podpoře funkcí jako je agregace nosných, provoz s více paprsky, více TRP a různorodé služby (eMBB, URLLC, mMTC), výrazně vzrostl počet sad vyhledávacích prostorů, které muselo být pro UE nakonfigurováno. Slepé dekódování všech možných kandidátů PDCCH napříč všemi těmito sadami v každé monitorovací příležitosti se stalo významnou zátěží pro životnost baterie UE a zvýšilo výpočetní složitost.

Účelem SSSG je poskytnout síti jemně nastavitelný nástroj pro dynamické řízení monitorovacího chování UE. Řeší problém statických, trvale aktivních požadavků na monitorování. Seskuplením vyhledávacích prostorů a umožněním rychlého přepínání mezi skupinami může síť sladit monitorovací aktivitu UE s jeho skutečným provozním vzorem a operačním stavem. Například během období vysoké aktivity může být aktivována SSSG s častými příležitostmi pro monitorování. Během období nečinnosti nebo stavů s nízkou spotřebou (jako je DRX v připojeném režimu) může být UE přepnuto na SSSG obsahující pouze nezbytné vyhledávací prostory (např. pro probouzející signály nebo indikaci předběžného přerušení), což drasticky snižuje spotřebu energie.

Tím se řeší klíčové omezení přístupu před verzí 17, kde byla úspora energie hrubší (např. závislá hlavně na cyklech DRX). SSSG umožňuje inteligentnější, na provoz adaptivní úsporu energie bez kompromisů v plánovací flexibilitě pro síť. Byla motivována zaměřením průmyslu na vylepšené funkce pro úsporu energie v 5G, zejména pro zařízení s omezeným příkonem a pro zlepšení celkového uživatelského zážitku prostřednictvím delší životnosti baterie.

## Klíčové vlastnosti

- Seskupuje více sad vyhledávacích prostorů PDCCH do logických celků pro účely řízení.
- Umožňuje dynamickou aktivaci/deaktivaci skupiny prostřednictvím rychlé signalizace MAC CE.
- Snižuje složitost slepého dekódování v UE omezením monitorování na aktivní podmnožinu.
- Umožňuje významnou úsporu energie v připojeném režimu přizpůsobením monitorování potřebám provozu.
- Podporuje pokročilá nasazení s mnoha sadami vyhledávacích prostorů (např. více paprsky, více TRP).
- Konfigurace se provádí prostřednictvím RRC, zatímco aktivaci řídí vrstva MAC.

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [CORESET – Control Resource Set](/mobilnisite/slovnik/coreset/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [SSSG na 3GPP Explorer](https://3gpp-explorer.com/glossary/sssg/)
