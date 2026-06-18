---
slug: "idc"
url: "/mobilnisite/slovnik/idc/"
type: "slovnik"
title: "IDC – In-Device Coexistence"
date: 2025-01-01
abbr: "IDC"
fullName: "In-Device Coexistence"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/idc/"
summary: "In-Device Coexistence (IDC) je soubor mechanismů pro správu rádiového rušení mezi různými rádiovými technologiemi (např. LTE, Wi-Fi, Bluetooth, GNSS) fungujícími souběžně v rámci jednoho koncového zař"
---

IDC je soubor mechanismů pro správu rádiového rušení mezi různými technologiemi fungujícími souběžně v rámci jednoho zařízení.

## Popis

In-Device Coexistence (IDC) řeší kritický problém rušení vznikajícího, když více rádiových vysílačů/přijímačů, jako jsou LTE, Wi-Fi, Bluetooth a přijímače globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)), pracuje současně v rámci jednoho uživatelského zařízení (UE). Toto rušení, často označované jako In-Device Coexistence Interference (IDCI), vzniká v důsledku fyzické blízkosti těchto rádiových rozhraní a možnosti vzniku harmonických nebo intermodulačních produktů, stejně jako desenzibilizace přijímače (blokování). Hlavní sledovaný scénář rušení nastává, když vysílač jedné technologie (např. LTE uplink) pracuje v kmitočtovém pásmu, které je harmonicky příbuzné, nebo se prostě nachází velmi blízko, přijímacímu pásmu jiné technologie umístěné ve stejném zařízení (např. Wi-Fi nebo Bluetooth v pásmu [ISM](/mobilnisite/slovnik/ism/)). To může vážně zhoršit citlivost a výkonnost postiženého přijímače.

Architektura IDC dle 3GPP, zavedená ve verzi 11, definuje standardizované postupy umožňující UE a síti toto rušení spravovat společnými silami. Architektura zahrnuje vylepšení především v UE a v [E-UTRAN](/mobilnisite/slovnik/e-utran/) (eNodeB). UE je zodpovědné za detekci IDC problémů na základě své vnitřní rádiové konfigurace a aktivity. Tyto problémy hlásí eNodeB pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/), konkrétně pomocí zprávy `InDeviceCoexIndication`. Tato zpráva může sdělovat ovlivněná kmitočtová pásma, směr rušení (např. LTE uplink rušící příjem Wi-Fi) a preferovanou metodu zmírnění rušení ze strany UE.

Po obdržení IDC indikace může eNodeB použít několik strategií zmírnění rušení definovaných 3GPP. Hlavními metodami jsou multiplexování v časové oblasti ([TDM](/mobilnisite/slovnik/tdm/)) a multiplexování v kmitočtové oblasti ([FDM](/mobilnisite/slovnik/fdm/)). Řešení TDM zahrnují plánovací mezery nebo vzory, kdy je rušivý přenos na okamžik přerušen, aby mohl postižený přijímač pracovat nerušeně. eNodeB může pro LTE nakonfigurovat `IDC-SubframePatterns` pro vytvoření těchto klidových period. Pro FDM může síť iniciovat handover nebo změnit pracovní kmitočet LTE rádiového rozhraní na pásmo, které nezpůsobuje rušení jiné technologii v zařízení. Konečné rozhodnutí o tom, kterou techniku zmírnění použít, činí eNodeB s vyvážením požadavků UE a celkového řízení síťových zdrojů a podmínek zatížení.

Postupy IDC jsou těsně integrovány s protokolovým zásobníkem RRC UE (`36.331`) a správou rádiových zdrojů. Specifikace také pokrývají scénáře pro autonomní popření, kdy může UE v rámci síťově autorizovaných limitů dočasně popřít LTE přenosy na ochranu jiných rádiových rozhraní, a pro přenos asistujících informací od UE k síti. Tento rámec zajišťuje, že rozšíření více-rádiových zařízení nevede k nepřijatelnému zhoršení uživatelského zážitku u žádné z aktivních služeb, ať už jde o mobilní data, Wi-Fi volání, Bluetooth audio nebo satelitní polohování.

## K čemu slouží

IDC bylo vytvořeno k řešení praktického a rostoucího problému rušení rádiových kmitočtů uvnitř moderních smartphonů a tabletů. Jak se tato zařízení vyvíjela a začala zahrnovat stále širší škálu bezdrátových technologií – LTE, 3G, 2G, Wi-Fi (2,4 GHz a 5 GHz), Bluetooth, Near Field Communication (NFC) a [GNSS](/mobilnisite/slovnik/gnss/) ([GPS](/mobilnisite/slovnik/gps/), GLONASS) – všechny umístěné ve velmi kompaktním provedení, potenciál těchto rádiových rozhraní vzájemně se rušit se stal významným. Před standardizací IDC bylo zmírnění rušení ponecháno na jednotlivých výrobcích zařízení, což vedlo k proprietárním, neinteroperabilním řešením, která byla často neefektivní a mohla negativně ovlivnit výkonnost sítě bez vědomí operátora.

Klíčový problém, který IDC řeší, je degradace kvality služeb. Například uživatel provádějící hovor Voice over Wi-Fi při aktivním LTE v pásmu 7 (2500 MHz) může zažít přerušené hovory, protože přenosy LTE uplink (kolem 2500-2570 MHz) mohou generovat harmonické složky padající do pásma ISM 2,4 GHz používaného Wi-Fi, což desenzibilizuje Wi-Fi přijímač. Podobně mohou operace v LTE pásmu 40 (2300 MHz) rušit příjem GNSS. Bez koordinace by zařízení mohlo jednoduše vykazovat špatný výkon nebo by muselo agresivně vypínat jedno rádiové rozhraní, čímž by se popřel smysl více-rádiového zařízení.

3GPP standardizovalo IDC, aby poskytlo jednotné, síťově-aware řešení. To umožňuje síťovým operátorům udržovat kontrolu nad využíváním rádiových zdrojů a zároveň umožňuje optimální výkon zařízení. Vytváří předvídatelné prostředí, kde síť rozumí vnitřním omezením zařízení a může podle toho plánovat zdroje, čímž zlepšuje celkovou efektivitu systému, uživatelský zážitek a zajišťuje, že zavedení nových kmitočtových pásem nebo provedení zařízení nezpůsobí problémy stávající funkcionalitě. Představuje posun od přístupu k UE jako k černé skříňce k více spolupracujícímu modelu správy mezi zařízením a sítí.

## Klíčové vlastnosti

- Hlášení podpory IDC jako součást capability UE
- RRC zpráva InDeviceCoexIndication pro hlášení rušení od UE k eNodeB
- Řízené multiplexování v časové oblasti (TDM) pomocí IDC vzorů podrámců (subframe patterns)
- Řízené multiplexování v kmitočtové oblasti (FDM) pomocí handoveru nebo změny kmitočtu
- Konfigurace mezer pro autonomní popření (autonomous denial gaps), aby UE mohlo chránit ne-3GPP rádiová rozhraní
- Podpora IDC v připojeném stavu, stavu nečinnosti a při mobilitě mezi RAT

## Související pojmy

- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [E-UTRAN – Evolved Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/e-utran/)

## Definující specifikace

- **TR 22.874** (Rel-18) — Technical Report
- **TS 32.423** (Rel-19) — Trace Data Definition and Management
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.880** (Rel-13) — MDT Enhancements Study for E-UTRAN
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [IDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/idc/)
