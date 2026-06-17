---
slug: "mcot"
url: "/mobilnisite/slovnik/mcot/"
type: "slovnik"
title: "MCOT – Maximum Channel Occupancy Time"
date: 2025-01-01
abbr: "MCOT"
fullName: "Maximum Channel Occupancy Time"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcot/"
summary: "Regulační a technický parametr v LTE a NR pro nelicencované/sdílené spektrum (např. 5 GHz, 6 GHz). Definuje maximální nepřerušovanou dobu, po kterou může zařízení nebo základnová stanice vysílat po ús"
---

MCOT je maximální nepřerušovaná doba, po kterou může zařízení nebo základnová stanice vysílat na nelicencovaném spektru po úspěšném získání přístupu k kanálu, což zajišťuje spravedlivé soužití s ostatními systémy.

## Popis

Maximum Channel Occupancy Time (MCOT) je klíčový parametr definovaný ve specifikacích 3GPP pro LTE License Assisted Access ([LAA](/mobilnisite/slovnik/laa/)), LTE-WLAN Aggregation ([LWA](/mobilnisite/slovnik/lwa/)), [NR-U](/mobilnisite/slovnik/nr-u/) (New Radio v nelicencovaném spektru) a další operace ve sdílených kmitočtových pásmech. Představuje horní limit pro dobu, po kterou může vysílací uzel (gNB v NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE) nepřetržitě obsazovat kanál poté, co úspěšně získal přístup prostřednictvím procedury Listen-Before-Talk ([LBT](/mobilnisite/slovnik/lbt/)). Časovač MCOT se spustí při zahájení vysílání po úspěšném LBT. Jakmile tento časovač vyprší, uzel musí vysílání ukončit a provést novou proceduru LBT, než se pokusí o přístup k kanálu znovu, a to i v případě, že má ve vyrovnávací paměti další data.

Hodnota MCOT není pevná; liší se v závislosti na kategorii zařízení (Frame-Based Equipment nebo Load-Based Equipment), prioritační třídě provozu a regionálních regulačních požadavcích definovaných orgány jako [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/). Například v pásmu 5 GHz se typické hodnoty MCOT pohybují od 4 ms do 10 ms. Síť plánuje svá vysílání v rámci tohoto MCOT okna. To zahrnuje nejen uživatelská data, ale také nezbytné řídicí signalizaci a případné mezery. Plánovací algoritmus musí zajistit, aby všechna vysílání byla obsažena v limitu MCOT, aby byla zachována shoda s předpisy a spravedlivé soužití.

Z architektonického hlediska je správa MCOT implementována ve vrstvě [MAC](/mobilnisite/slovnik/mac/) gNB/eNB. Po úspěšném LBT je plánovači přidělena vysílací příležitost (TXOP), jejíž maximální doba trvání je omezena platnou hodnotou MCOT. Plánovač přiděluje prostředky uživatelským zařízením (UE) a zasílá Downlink Control Information (DCI), aby je informoval o přidělených prostředcích. Uzel musí monitorovat svá vlastní vysílání, aby zajistil, že nepřekročí MCOT. Tento mechanismus je zásadní pro 'zdvořilý' provoz systémů 3GPP v nelicencovaném spektru, protože zajišťuje, že nebudou monopolizovat kanál, a umožňuje jiným technologiím, jako je Wi-Fi, spravedlivý přístup, což je klíčový požadavek pro regulační schválení a harmonické sdílení spektra.

## K čemu slouží

MCOT byl zaveden, aby umožnil LTE a 5G NR fungovat spravedlivě a v souladu s předpisy v nelicencovaných nebo sdílených kmitočtových pásmech, jako jsou pásma 5 GHz a 6 GHz. Hlavním problémem bylo, že tradiční buněčné protokoly jsou navrženy pro licencované, exkluzivní spektrum, kde základnová stanice řídí načasování vysílání bez soutěžení. V nelicencovaných pásmech předpisy vyžadují soužití se stávajícími systémy, jako je Wi-Fi. Bez omezení nepřetržitého vysílání by buněčná základnová stanice mohla dominovat kanálu, což by způsobilo vážné zhoršení výkonu a nespravedlnost vůči sítím Wi-Fi, což by porušovalo regulační principy spravedlivého přístupu.

Účelem definice MCOT je uvalit samo vynucované omezení na obsazení kanálu. Je to klíčová součást rámce Listen-Before-Talk (LBT) a přístupu ke kanálu, který 3GPP převzal z regulací jako ETSI EN 301 893. Tím, že omezuje vysílací bursty, MCOT zajišťuje, že po období obsazení je kanál uvolněn, což nutí buněčný systém znovu soutěžit o přístup. To dává jiným zařízením (Wi-Fi přístupovým bodům, jiným LAA uzlům) šanci získat přístup ke kanálu. MCOT v kombinaci s LBT řeší kritiku, že by buněčné technologie byly v nelicencovaném spektru 'špatnými sousedy'. Byla to nezbytná technická adaptace pro rozšíření kapacity buněčných sítí prostřednictvím agregace nosných s nelicencovanými nosnými (LAA, NR-U) při dodržování globálních pravidel soužití a usnadnění komerčního nasazení technologií jako LTE-LAA a 5G NR-U.

## Klíčové vlastnosti

- Definuje maximální nepřetržitou dobu vysílání po úspěšném získání přístupu ke kanálu (LBT)
- Hodnota závisí na kategorii zařízení, prioritě provozu a regionálních předpisech
- Časovač se spustí na začátku vysílacího burstu a omezuje vysílací příležitost (TXOP)
- Po překročení doby MCOT vyžaduje provedení nové procedury LBT
- Klíčové pro zajištění spravedlivého soužití s Wi-Fi a dalšími systémy v nelicencovaných pásmech
- Implementováno v plánování vrstvy MAC eNB (LTE) a gNB (NR)

## Související pojmy

- [LBT – Listen Before Talk](/mobilnisite/slovnik/lbt/)
- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)
- [LAA – Licensed-Assisted Access](/mobilnisite/slovnik/laa/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.789** (Rel-13) — LAA Multi-Node Coexistence Test Methodology
- **TS 37.213** (Rel-19) — Shared Spectrum Physical Layer Procedures
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [MCOT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcot/)
