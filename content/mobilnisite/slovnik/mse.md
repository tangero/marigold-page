---
slug: "mse"
url: "/mobilnisite/slovnik/mse/"
type: "slovnik"
title: "MSE – Mobility Speed Estimation"
date: 2025-01-01
abbr: "MSE"
fullName: "Mobility Speed Estimation"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mse/"
summary: "Mobility Speed Estimation (MSE) je síťová funkce, která určuje rychlostní kategorii (např. stacionární, pěší, vozidlovou) uživatelského zařízení (UE). Je klíčová pro optimalizaci parametrů předávání s"
---

MSE je síťová funkce, která určuje rychlostní kategorii uživatelského zařízení (User Equipment), což je klíčové pro optimalizaci parametrů předávání spojení (handover), řízení rádiových zdrojů a funkcí pro úsporu energie.

## Popis

Mobility Speed Estimation (MSE) je kritická algoritmická funkce v rámci rádiové přístupové sítě (RAN), primárně implementovaná v základnové stanici (eNodeB v LTE, gNB v 5G NR). Jejím hlavním účelem je klasifikovat stav mobility uživatelského zařízení (UE) do definovaných rychlostních kategorií, jako jsou nízká, střední nebo vysoká, které odpovídají typickým scénářům, jako je stacionární stav, pohyb pěšky nebo v vozidle. Odhad se provádí analýzou časových a prostorových změn měření rádiového kanálu hlášených UE nebo pozorovaných sítí. Mezi klíčové vstupní parametry patří rychlost změny referenčního signálu přijímaného výkonu ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo kvality ([RSRQ](/mobilnisite/slovnik/rsrq/)), četnost událostí předávání spojení (handover) a odhady Dopplerova posuvu odvozené z uplinkových signálů. Algoritmus typicky používá filtrační techniky, jako je průměrování nebo hystereze, pro vyhlazení měřicího šumu a poskytnutí stabilní rychlostní klasifikace.

Architektura MSE je distribuovaná, přičemž hlavní logika sídlí v uzlu RAN obsluhujícím UE. Základnová stanice průběžně shromažďuje měřicí reporty nakonfigurované prostřednictvím signalizace řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)). Tyto reporty obsahují informace o obsluhující buňce a sousedních buňkách. Sledováním identity a síly signálu těchto buněk v čase může síť odvodit trajektorii a rychlost UE. Například rychlé sledované předávání spojení mezi malými buňkami indikuje vysokou mobilitu, zatímco stabilní měření z jedné buňky naznačuje nízkou mobilitu. V pokročilejších implementacích, zejména od LTE-Advanced výše, může síť pro zvýšení přesnosti také využívat informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a specifické referenční signály navržené pro sledování.

Role MSE přesahuje pouhou klasifikaci; přímo ovlivňuje několik klíčových procedur RAN. Na základě odhadnuté rychlosti může síť dynamicky upravovat parametry předávání spojení, jako je čas do spuštění ([TTT](/mobilnisite/slovnik/ttt/)) a hysterezní okraje. Pro vysokorychlostní UE může být aplikován kratší TTT pro urychlení předávání spojení a prevenci přerušení hovoru, zatímco pro pěší UE může delší TTT snížit zbytečné ping-pong předávání spojení. Dále MSE informuje o konfiguraci cyklů nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)), kde může být stacionárnímu UE přidělen delší spánkový cyklus pro úsporu baterie, a o strategiích správy svazků v 5G, kde se algoritmy tvarování a sledování svazku přizpůsobují rychlosti uživatele. MSE je tedy základním prvkem umožňujícím kontextově-aware, efektivní a robustní řízení rádiových zdrojů.

## K čemu slouží

Mobility Speed Estimation (MSE) byla zavedena, aby řešila rostoucí potřebu inteligentního, adaptivního řízení rádiových zdrojů v celulárních sítích. Rané celulární systémy používaly statické konfigurace pro předávání spojení a další mobilní procedury, které byly neefektivní a mohly vést ke špatnému výkonu – například k přerušeným hovorům pro rychle se pohybující uživatele nebo nadměrné signalizační režii pro pomalu se pohybující uživatele. Jak se sítě vyvíjely, aby podporovaly širší škálu uživatelských rychlostí, od stacionárních IoT zařízení po vysokorychlostní vlaky, se jednotný přístup pro všechny stal neudržitelným. MSE poskytuje síti kontextové povědomí o mobilitě uživatele, což jí umožňuje proaktivně optimalizovat své chování.

Primární problém, který MSE řeší, je kompromis mezi robustností mobility a efektivitou sítě. Bez přesného odhadu rychlosti musí síť pro všechny uživatele používat konzervativní nastavení pro nejhorší případ, což plýtvá zdroji a ovlivňuje výkon. Například používání krátkých [DRX](/mobilnisite/slovnik/drx/) cyklů pro všechny uživatele vyčerpává baterii UE a používání dlouhých časovačů pro předávání spojení pro všechny uživatele zvyšuje riziko selhání ve vysokorychlostních scénářích. MSE umožňuje síti tyto parametry přizpůsobovat, čímž zlepšuje kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) a celkovou kapacitu systému. Její vytvoření bylo motivováno specifikacemi pro LTE/EPC, kde se pokročilé funkce mobility a úspory energie staly ústředními pilíři, a zůstala nezbytná i v 5G pro správu mobility v hustých a heterogenních nasazeních sítí.

## Klíčové vlastnosti

- Klasifikace stavu mobility UE do standardizovaných kategorií (např. Normal-Mobility, Medium-Mobility, High-Mobility)
- Jako primární vstupy využívá měřicí reporty UE (RSRP/RSRQ) a síťová měření (Dopplerův posuv)
- Ovlivňuje dynamické přizpůsobení parametrů předávání spojení (Time-To-Trigger, Hysteresis)
- Optimalizuje cykly nespojitého příjmu (DRX) pro úsporu energie UE na základě mobility
- Podporuje vylepšené procedury správy a sledování svazků v 5G NR
- Umožňuje parametry výběru buňky závislé na rychlosti pro mobilitu v režimu idle

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.812** (Rel-18) — Technical Report
- **TS 26.819** (Rel-19) — Spatial Computing Functions for AR/XR in 3GPP
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 28.908** (Rel-19) — AI/ML Management for 5GS
- **TS 36.839** (Rel-11) — HetNet Mobility Improvements for LTE

---

📖 **Anglický originál a plná specifikace:** [MSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mse/)
