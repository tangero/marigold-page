---
slug: "imu"
url: "/mobilnisite/slovnik/imu/"
type: "slovnik"
title: "IMU – Inertial Measurement Unit"
date: 2026-01-01
abbr: "IMU"
fullName: "Inertial Measurement Unit"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imu/"
summary: "Inertial Measurement Unit (IMU) je senzorové zařízení, které měří a vyhodnocuje specifickou sílu, úhlovou rychlost a někdy i orientaci tělesa. V kontextu 3GPP je integrováno do zařízení, jako jsou dro"
---

IMU je senzorové zařízení, které měří specifickou sílu a úhlovou rychlost za účelem poskytnutí pohybových dat pro vylepšené lokalizační služby v systémech 3GPP, například pro drony nebo vozidla.

## Popis

Inertial Measurement Unit (IMU) je klíčová senzorová komponenta v mobilních zařízeních, zejména v kontextu internetu věcí (IoT) a vertikálních aplikací, jako jsou bezpilotní systémy ([UAS](/mobilnisite/slovnik/uas/)). Typicky se skládá z kombinace akcelerometrů, gyroskopů a někdy i magnetometrů. Akcelerometry měří lineární zrychlení (specifickou sílu) podél jedné nebo více os, gyroskopy měří úhlovou rychlost (rychlost rotace) a magnetometry měří sílu magnetického pole pro určení směru vůči magnetickému severu. Integrací dat z těchto senzorů může IMU vypočítat parametry, jako je rychlost, orientace (náklon) a posunutí, což je proces známý jako dead reckoning (odhad polohy).

V systémech 3GPP je role IMU definována v rámci požadavků na služby a architektury pro vylepšené lokalizační služby. Například v provozu dronů (UAS) IMU poskytuje kritická pohybová data, která doplňují nebo nahrazují určování polohy pomocí globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)). Když jsou signály GNSS slabé, nedostupné nebo nespolehlivé (např. v městských kaňonech, uvnitř budov nebo při rušení signálu), může IMU poskytovat nepřetržité odhady polohy a náklonu. Zařízení nebo síťový aplikační server může fúzovat data z IMU s měřeními z mobilní sítě (jako je například [OTDOA](/mobilnisite/slovnik/otdoa/) – Observed Time Difference of Arrival) nebo s daty z jiných senzorů, aby udržel přesné a spolehlivé určení polohy.

Integrace dat z IMU do architektur 3GPP je specifikována pro podporu různých vertikál. Specifikace jako TS 22.104 (Service Requirements for Cyber-Physical Control Applications) a TS 22.261 (Service Requirements for the 5G System) nastiňují scénáře, které vyžadují přesné a spolehlivé snímání pohybu. TS 26.928 (Extended Reality ([XR](/mobilnisite/slovnik/xr/)) in 5G) uvažuje IMU pro sledování polohy hlavy a ovladačů v aplikacích XR. TS 37.857 (Study on Enhanced LTE and NR support for Aerial Vehicles) podrobně popisuje, jak mohou být data IMU z dronů hlášena síti pro vylepšené monitorování letové trasy a geofencing. Data z IMU jsou typicky hlášena prostřednictvím aplikačních protokolů nebo, v některých architekturách, mohou být přenášena signalizací v uživatelské rovině nebo řídicí rovině pro síťově asistované určování polohy.

Funkce IMU je klíčová pro bezpečnost, automatizaci a vylepšený uživatelský zážitek. V autonomních nebo dálkově řízených vozidlech IMU poskytuje nezbytná data pro navigaci a stabilizaci. Pro rozšířenou a virtuální realitu jsou nízkolatenční, vysoce přesná data z IMU nezbytná pro přesné vykreslování a interakci s uživatelem. Práce na standardech 3GPP zajišťuje, že data z IMU mohou být v rámci ekosystému mobilních sítí spolehlivě sbírána, přenášena a zpracovávána, což umožňuje nové služby závislé na robustním povědomí o pohybu.

## K čemu slouží

Účelem standardizace role IMU v rámci 3GPP je umožnit a vylepšit služby založené na poloze a pohybu, které vyžadují kontinuitu a spolehlivost nad rámec toho, co může poskytnout samostatný [GNSS](/mobilnisite/slovnik/gnss/). GNSS, ačkoli je přesný v podmínkách volného výhledu na oblohu, trpí blokováním signálu, mnohocestným rušením v městském prostředí a zranitelností vůči úmyslnému rušení nebo podvržení. Pro kritické aplikace, jako je řízení letu dronů, autonomní řízení a průmyslová automatizace, jsou takové mezery v dostupnosti určování polohy nepřijatelné a představují bezpečnostní rizika.

Historicky byly IMU používány v samostatných, špičkových navigačních systémech (např. v letectví a kosmonautice). Jejich integrace do spotřebitelských zařízení a zařízení IoT vytvořila příležitost ke zlepšení mobilního určování polohy. 3GPP toto uznalo s rozšířením podpory vertikálních průmyslů počínaje Release 13 a dále. Počáteční motivací byla podpora vznikajících případů užití, jako je komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)) a bezpilotní letouny ([UAV](/mobilnisite/slovnik/uav/)), kde je přesné a kontinuální určování polohy prvořadé pro prevenci kolizí, plánování trasy a dodržování předpisů (např. geofencing).

Definováním způsobu, jakým data z IMU komunikují s mobilní sítí, 3GPP řeší omezení spočívající ve spoléhání se pouze na síťové nebo satelitní určování polohy. Umožňuje techniky fúze senzorů, při kterých jsou silné stránky buněčného určování polohy (pokrytí široké oblasti, relativní určování polohy) kombinovány se silnými stránkami inerciální navigace (krátkodobá přesnost, vysoká obnovovací frekvence, nezávislost na externích signálech). Tento hybridní přístup vytváří odolnější, přesnější a dostupnější řešení pro určování polohy, což je základním požadavkem pro mnoho vertikálních aplikací 5G a budoucích generací.

## Klíčové vlastnosti

- Měří specifickou sílu (zrychlení) pomocí akcelerometrů
- Měří úhlovou rychlost (rotaci) pomocí gyroskopů
- Často zahrnuje magnetometry pro určení směru (heading)
- Umožňuje dead reckoning pro odhad polohy, když není dostupný GNSS
- Poskytuje vysokofrekvenční, nízkolatenční pohybová data
- Podporuje fúzi senzorů s metodami buněčného a GNSS určování polohy

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 22.104** (Rel-19) — Service requirements for cyber-physical control apps
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 26.113** (Rel-19) — 5G Real-Time Media Communication Procedures & APIs
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [IMU na 3GPP Explorer](https://3gpp-explorer.com/glossary/imu/)
