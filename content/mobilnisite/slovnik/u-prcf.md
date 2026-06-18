---
slug: "u-prcf"
url: "/mobilnisite/slovnik/u-prcf/"
type: "slovnik"
title: "U-PRCF – UTRAN Position Radio Co-ordination Function"
date: 2025-01-01
abbr: "U-PRCF"
fullName: "UTRAN Position Radio Co-ordination Function"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-prcf/"
summary: "Funkce UTRAN, která koordinuje a spravuje rádiové prostředky a procedury vyžadované pro měření pro určování polohy. Funguje jako zprostředkovatel mezi funkcí pro výpočet polohy a rádiovou sítí za účel"
---

U-PRCF je funkce UTRAN, která koordinuje rádiové prostředky a procedury pro určování polohy tím, že funguje jako zprostředkovatel mezi funkcí pro výpočet polohy a rádiovou sítí za účelem sběru měřicích dat.

## Popis

[UTRAN](/mobilnisite/slovnik/utran/) Position Radio Co-ordination Function (U-PRCF) je klíčová řídicí entita v podsystému pro určování polohy UTRAN, která sídlí v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Jejím hlavním úkolem je koordinovat všechny rádiové činnosti nezbytné pro určení polohy UE. Když je přijat požadavek na určení polohy (např. od [U-PCF](/mobilnisite/slovnik/u-pcf/) nebo jádra sítě), U-PRCF určí požadovaný typ měření (např. [OTDOA](/mobilnisite/slovnik/otdoa/), UE-assisted nebo UE-based [A-GNSS](/mobilnisite/slovnik/a-gnss/)) a řídí příslušnou proceduru. To zahrnuje vydávání příkazů příslušným Node B k vysílání referenčních signálů pro určování polohy (např. pro OTDOA), instruování UE k provedení specifických měření a sběr výsledných měřicích dat. U-PRCF spravuje rádiové prostředky vyčleněné pro určování polohy a zajišťuje, aby činnosti spojené s určováním polohy nepřiměřeně nenarušovaly běžné komunikační služby. Rozhraní s U-PCF využívá k přijímání požadavků na výpočet a k poskytování sebraných měřicích dat. Interaguje také s funkcí UTRAN Position Radio Resource Management ([U-PRRM](/mobilnisite/slovnik/u-prrm/)) pro rozhodnutí o přidělení prostředků. V podstatě U-PRCF převádí požadavek na výpočet polohy na řadu konkrétních příkazů na rádiové vrstvě a úkolů pro sběr dat, čímž abstrahuje rádiovou komplexitu od výpočetního modulu.

## K čemu slouží

U-PRCF byla vytvořena, aby řešila složitost koordinovaného a efektivního sběru rádiových měření pro určování polohy v rámci [UTRAN](/mobilnisite/slovnik/utran/) z hlediska využití prostředků. Bez vyčleněné koordinační funkce by požadavky na určení polohy vyžadovaly ad-hoc, rušivé interakce s více prvky rádiové sítě (UE a Node B), což by vedlo k potenciálním konfliktům, neefektivnímu využití prostředků a zvýšené latenci. U-PRCF poskytuje centralizovaný řídicí bod pro všechny rádiové procedury související s určováním polohy. Řeší problém, jak efektivně získat synchronizovaná měření z více buněk (pro [OTDOA](/mobilnisite/slovnik/otdoa/)) nebo jak spravovat doručování asistovaných dat GNSS pro UE-based režim. Oddělením rádiové koordinace od výpočtu polohy (U-PCF) a správy prostředků (U-PRRM) dosahuje architektura 3GPP čistého funkčního rozdělení, které zvyšuje modularitu, škálovatelnost a schopnost zavádět nové metody určování polohy. Její vytvoření bylo motivováno potřebou spolehlivého určování polohy s nízkou latencí, aby byly splněny požadavky služeb tísňového volání a podpořeny komerční aplikace LBS.

## Klíčové vlastnosti

- Koordinuje rádiové procedury pro různé metody určování polohy (OTDOA, A-GNSS)
- Přikazuje Node B vysílat referenční signály pro určování polohy (PRS) pro OTDOA měření
- Instruuje UE k provedení a hlášení specifických rádiových měření (např. RTT, data GNSS)
- Sbírá a sestavuje měřicí data z UE a více Node B
- Poskytuje rozhraní k U-PCF pro vyřizování požadavků na určení polohy a doručování měřicích souborů
- Interaguje s U-PRRM pro přidělení a správu rádiových prostředků pro určování polohy

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [U-PCF – UTRAN Position Calculation Function](/mobilnisite/slovnik/u-pcf/)
- [U-PRRM – UTRAN Position Radio Resource Management](/mobilnisite/slovnik/u-prrm/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-PRCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-prcf/)
