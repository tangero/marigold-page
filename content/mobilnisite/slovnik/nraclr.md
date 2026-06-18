---
slug: "nraclr"
url: "/mobilnisite/slovnik/nraclr/"
type: "slovnik"
title: "NRACLR – New Radio Adjacent Channel Leakage Ratio"
date: 2025-01-01
abbr: "NRACLR"
fullName: "New Radio Adjacent Channel Leakage Ratio"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/nraclr/"
summary: "NRACLR je klíčový požadavek na vysílač v rádiovém rozhraní (RF) pro 5G NR, který měří poměr filtrovaného středního výkonu v centru přiděleného kmitočtu kanálu k filtrovanému střednímu výkonu v centru"
---

NRACLR je měření vysílače v 3GPP 5G NR, které kvantifikuje nežádoucí únik signálu do přilehlého kanálu a vyjadřuje ho jako poměr výkonu v přiděleném kanálu k výkonu, který do něj uniká, čímž se předchází interferenci.

## Popis

New Radio Adjacent Channel Leakage Ratio (NRACLR) je kritický parametr testu konformity v rádiovém rozhraní ([RF](/mobilnisite/slovnik/rf/)) definovaný ve specifikacích 3GPP pro uživatelská zařízení (UE) a základnové stanice (gNB) 5G New Radio (NR). Jedná se o míru schopnosti vysílače udržet svůj vysílaný výkon v rámci přiděleného kmitočtového pásma, a tím minimalizovat nežádoucí emise do přilehlých kmitočtových kanálů. Tento parametr je zásadní pro udržení spektrální efektivity a zajištění koexistence mezi různými síťovými operátory nebo mezi různými nosnými signály ve spektru téhož operátora. Měření se provádí aplikací specifického měřicího filtru, definovaného šířkou kanálu a rozestupem subnosných, na vysílaný signál. Výkon se měří nejprve v rámci šířky pásma přiděleného kanálu a poté v rámci šířky pásma přilehlého kanálu, přičemž poměr je vyjádřen v decibelech (dB). Nižší hodnota [ACLR](/mobilnisite/slovnik/aclr/) znamená lepší výkon vysílače, tedy menší únik výkonu do sousedního kanálu.

Z pohledu architektury je testování NRACLR integrováno do sady RF konformních testů pro základnové stanice i uživatelská zařízení, jak je podrobně popsáno ve specifikacích jako 38.141 a 38.521. Testovací sestava zahrnuje signálový generátor pro vytvoření NR testovacího modelu a spektrální analyzátor nebo specializované testovací zařízení pro provedení měření filtrovaného výkonu. Požadavky se liší na základě faktorů, jako je pracovní kmitočtové pásmo (FR1 nebo FR2), šířka kanálu, modulační schéma a výkonová třída zařízení. U základnových stanic požadavky na ACLR zajišťují, aby přenos gNB nezpůsoboval škodlivou interferenci uživatelským zařízením připojeným k sousední buňce na přilehlém kmitočtu. U uživatelských zařízení zajišťuje, aby zařízení vysílající na jednom nosném signálu neznepřístupnilo přijímač blízkého zařízení nebo základnové stanice pracující na přilehlém nosném signálu.

Role NRACLR v síti je základní pro správu spektra a plánování sítě. Přímo ovlivňuje možnost nasazení nosných signálů s úzkými ochrannými pásmy, což umožňuje vyšší celkové využití spektra. Přísným definováním a testováním ACLR 3GPP zajišťuje, že zařízení od různých výrobců mohou v hustých prostředích s více nosnými signály vzájemně spolupracovat, aniž by si způsobovala vzájemné rušení. To je zvláště důležité pro scénáře sdílení spektra, jako je dynamické sdílení spektra (DSS) nebo provoz ve sdílených a nelicencovaných pásmech, kde jsou vysílače různých technologií nebo operátorů v těsné spektrální blízkosti. Dodržování specifikací NRACLR je proto povinnou součástí procesu schvalování typu a certifikace veškeré NR rádiové techniky, což zaručuje základní úroveň spektrální čistoty pro celý ekosystém.

## K čemu slouží

Účelem definování metriky NRACLR je stanovit standardizovaný, kvantifikovatelný limit pro mimokanálové emise vysílačů 5G NR. Bez takového požadavku by vysílače mohly vyzařovat nadměrný výkon mimo přidělené pásmo, což by způsobovalo interferenci přijímačům naladěným na přilehlé kanály. Tato interference, známá jako přilehlá kanálová interference ([ACI](/mobilnisite/slovnik/aci/)), může zhoršit poměr signálu k šumu a rušení ([SINR](/mobilnisite/slovnik/sinr/)) pro zasažené přijímače, což vede ke sníženým datovým rychlostem, zvýšeným poměrům chybových bloků a v konečném důsledku ke zhoršení celkové kapacity sítě a uživatelské zkušenosti. Problém je umocněn v moderních celulárních sítích, které využívají velké šířky kanálů (např. až 100 MHz v FR1 a 400 MHz ve FR2) a hustou agregaci nosných signálů, což ponechává minimální ochranná pásma mezi kanály.

Historicky existovaly podobné metriky jako [ACLR](/mobilnisite/slovnik/aclr/) pro UMTS a LTE, ale přechod na 5G NR přinesl nové výzvy, které si vyžádaly přepracování specifikace. 5G NR podporuje mnohem širší škálu kmitočtů nosných signálů (od pásem pod 1 GHz až po milimetrové vlny), nové parametry signálu (jako je flexibilní členění s proměnným rozestupem subnosných) a složitější architektury výkonových zesilovačů pro massive [MIMO](/mobilnisite/slovnik/mimo/). Předchozí definice a testovací modely ACLR pro LTE již nedostačovaly k přesné charakterizaci chování úniku těchto nových NR signálů. Proto 3GPP vyvinulo specifické požadavky na ACLR pro NR (NRACLR) ve vydání 15, aby poskytlo konzistentní a přísný rámec pro hodnocení výkonu vysílače v celém prostoru návrhu 5G NR. Tím je zajištěno, že pokročilé sliby spektrální efektivity 5G mohou být v praxi realizovány, aniž by byly ohroženy interferencí mezi nosnými signály.

## Klíčové vlastnosti

- Definuje limity pro nežádoucí emise vysílače do přilehlých kanálů.
- Měření využívá specifický NR měřicí filtr sladěný se šířkou kanálu a rozestupem subnosných.
- Požadavky jsou specifikovány samostatně pro uživatelská zařízení (UE) a základnové stanice (gNB).
- Hodnoty závisí na kmitočtovém rozsahu (FR1 nebo FR2), šířce pásma a modulaci.
- Kritické pro umožnění úzkých ochranných pásem a efektivní využití spektra.
- Klíčový parametr pro testování konformity a certifikaci zařízení.

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.793** (Rel-19) — Simultaneous Rx/Tx Band Combinations TR
- **TS 38.817** — 3GPP TR 38.817
- **TS 38.887** (Rel-16) — NR Band n259 Specification (39.5-43.5 GHz)

---

📖 **Anglický originál a plná specifikace:** [NRACLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nraclr/)
