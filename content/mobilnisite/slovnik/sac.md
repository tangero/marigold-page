---
slug: "sac"
url: "/mobilnisite/slovnik/sac/"
type: "slovnik"
title: "SAC – Semi Anechoic Chamber"
date: 2025-01-01
abbr: "SAC"
fullName: "Semi Anechoic Chamber"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sac/"
summary: "Semi Anechoic Chamber (SAC) je stíněné testovací prostředí používané pro Over-the-Air (OTA) měření bezdrátových zařízení, včetně UE a základnových stanic. Má absorbéry na stěnách a stropě, ale reflexi"
---

SAC je stíněná testovací komora s absorbéry na stěnách a reflexivní podlahou, používaná pro Over-the-Air (OTA) měření výkonu bezdrátových zařízení simulací reálných rádiových podmínek.

## Popis

Semi Anechoic Chamber (SAC) je specializované elektromagnetické testovací zařízení klíčové pro Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)) hodnocení výkonu rádiových zařízení, jako je uživatelské zařízení (UE) a základnové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), podle specifikací 3GPP pro testování shody. Na rozdíl od plné anechoické komory ([FAC](/mobilnisite/slovnik/fac/)), která je absorbující na všech površích, má SAC na stěnách a stropě radiofrekvenční ([RF](/mobilnisite/slovnik/rf/)) absorpční materiál pro minimalizaci odrazů, ale podlaha tvoří reflexivní kovovou zemní rovinu. Tento návrh záměrně vytváří řízený odraz od podlahy, aby simuloval realistické prostředí šíření s odrazem od země, podobné typickým reálným scénářům, kdy zařízení pracují nad úrovní terénu. Komora je také plně stíněná proti vnějšímu RF rušení, což zajišťuje, že měření nejsou ovlivněna vnějšími signály.

Architektura SAC zahrnuje stíněný prostor, pyramidální nebo klínové RF absorbéry pokrývající vnitřní povrchy (kromě podlahy), otočný stůl pro rotaci testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)) a pevnou nebo pohyblivou měřicí anténu připojenou k vektorovému síťovému analyzátoru nebo komunikačnímu testeru. Reflexivní zemní rovina je typicky velký, hladký kovový povrch. Během testování je DUT umístěno na otočný stůl v určité výšce nad zemní rovinou. Měřicí anténa, umístěná v pevné vzdálenosti, vysílá nebo přijímá signály. Při rotaci otočného stolu systém měří vyzařovací diagram, celkový vyzařovaný výkon ([TRP](/mobilnisite/slovnik/trp/)) a celkovou izotropní citlivost (TIS) DUT. Reflexivní podlaha vytváří vzor konstruktivní a destruktivní interference (vícecestné šíření), který musí být charakterizován, díky čemuž jsou měření reprezentativnější pro skutečné použití než v případě FAC.

SAC jsou široce používány pro 3GPP RF testy shody, zejména pro [MIMO](/mobilnisite/slovnik/mimo/) OTA hodnocení výkonu v LTE a 5G NR. Podporují testování klíčových metrik, jako je sférické pokrytí, zisk beamformingu a emulace prostorového kanálu. Komora musí být pečlivě kalibrována, aby zohlednila útlum na dráze a odrazy v komoře. Přítomnost zemní roviny znamená, že změřený vyzařovací diagram zahrnuje jak přímou dráhu, tak jednu odraženou dráhu, což je zjednodušený, ale pro mnoho nasazovacích prostředí hodnotný model. Díky tomu představuje testování v SAC rovnováhu mezi řízenou jednoduchostí FAC a komplexním realismem reverbní komory a poskytuje opakovatelné a standardizované výsledky pro regulační typové schvalování a certifikaci zařízení.

## K čemu slouží

Semi Anechoic Chamber existuje za účelem poskytnutí standardizovaného, opakovatelného testovacího prostředí pro [OTA](/mobilnisite/slovnik/ota/) měření výkonu bezdrátových zařízení, které věrně odráží běžnou reálnou podmínku šíření: provoz s odrazem od země. Před zavedením standardizovaného OTA testování byla zařízení často hodnocena pouze pomocí vedených testů (kabelové spojení), které ignorovaly vliv antén a pouzdra zařízení na skutečný vyzařovaný výkon. Tato mezera znamenala, že zařízení mohla projít laboratorními testy, ale v reálném provozu podávat špatný výkon. SAC bylo přijato, aby tento problém vyřešilo tím, že umožňuje realistické, ale přitom řízené, testování vyzařovaných vlastností.

Motivace pro standardizaci SAC v 3GPP vycházela z potřeby zajistit konzistentní kvalitu zařízení a výkon sítě s vývojem mobilních systémů využívajících MIMO a pokročilé anténní systémy. Plná anechoická komora (FAC) eliminuje všechny odrazy, což je ideální podmínka volného prostoru, která není typická pro použití UE v ruce. Reflexivní zemní rovina SAC zavádí řízený prvek vícecestného šíření, čímž je vhodnější pro testování zařízení v situaci, kdy jsou typicky držena nebo umístěna nad povrchem. Odstraňuje tak omezení FAC tím, že poskytuje testovací prostředí, které vyvažuje reprodukovatelnost s realističtějším fyzikálním modelem, což je klíčové pro hodnocení metrik jako TRP a TIS, které přímo ovlivňují uživatelský zážitek a pokrytí sítě. Její specifikace napříč více technickými zprávami 3GPP (např. 38.113 pro NR) zajišťuje globální harmonizaci v certifikaci zařízení.

## Klíčové vlastnosti

- Obsahuje RF absorbéry na stěnách/stropě a reflexivní kovovou podlahu ve formě zemní roviny
- Simuluje realistické prostředí šíření rádiové vlny s odrazem od země pro OTA testování
- Poskytuje stíněné prostředí bez vnějšího elektromagnetického rušení
- Umožňuje měření celkového vyzařovaného výkonu (TRP) a celkové izotropní citlivosti (TIS)
- Podporuje měření sférických vyzařovacích diagramů pomocí rotačního otočného stolu
- Používá se pro 3GPP testy shody MIMO OTA výkonu pro zařízení LTE a 5G NR

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface
- **TS 29.523** (Rel-19) — 5G Policy Control Event Exposure Service
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification

---

📖 **Anglický originál a plná specifikace:** [SAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sac/)
