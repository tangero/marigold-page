---
slug: "pout"
url: "/mobilnisite/slovnik/pout/"
type: "slovnik"
title: "Pout – Output Power"
date: 2025-01-01
abbr: "Pout"
fullName: "Output Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pout/"
summary: "Pout je úroveň výstupního výkonu RF vysílaná základnovou stanicí nebo uživatelským zařízením, měřená ve wattech nebo dBm. Je to klíčový parametr v 3GPP rádiových specifikacích, ovlivňující pokrytí, in"
---

Pout je úroveň výstupního výkonu RF vysílaná základnovou stanicí nebo uživatelským zařízením, jak je definováno v 3GPP rádiových specifikacích.

## Popis

Výstupní výkon (Pout) označuje úroveň rádiového ([RF](/mobilnisite/slovnik/rf/)) výkonu vysílaného vysílačem, jako je základnová stanice (Node B, eNodeB, gNB) nebo uživatelské zařízení (UE), v mobilní síti. Typicky se měří ve wattech (W) nebo decibelech vzhledem k jednomu miliwattu (dBm) a je základním parametrem definovaným v technických specifikacích 3GPP pro rádiové přístupové sítě. Pout určuje sílu signálu přijímaného protějškovým zařízením a přímo ovlivňuje oblast pokrytí, kvalitu spoje a celkovou kapacitu sítě. Ve specifikacích jako TS 25.104 ([UTRA](/mobilnisite/slovnik/utra/) [FDD](/mobilnisite/slovnik/fdd/) Base Station) a TS 25.105 (UTRA [TDD](/mobilnisite/slovnik/tdd/) Base Station) je Pout specifikován spolu s tolerancemi, měřicími metodami a požadavky, aby byla zajištěna konzistentní výkonnost zařízení od různých výrobců.

Architektura správy Pout zahrnuje několik klíčových komponent: výkonový zesilovač ve vysílači, který zesiluje signál na požadovanou úroveň; algoritmy řízení výkonu, které dynamicky upravují Pout na základě stavu kanálu; a měřicí jednotky, které ověřují shodu s normami 3GPP. U základnových stanic je Pout definován pro každou nosnou a anténní port, přičemž požadavky se liší podle kmitočtového pásma a scénáře nasazení (např. makro, mikro nebo piko buňky). U uživatelských zařízení je Pout řízen tak, aby se minimalizovaly interference a šetřila životnost baterie, přičemž maximální limity jsou nastaveny pro zajištění bezpečnosti a regulatorní shody. Mechanismus řízení výkonu, jako je vnitřní smyčka řízení výkonu ve [WCDMA](/mobilnisite/slovnik/wcdma/), průběžně upravuje Pout pro udržení cílového poměru signálu k šumu ([SIR](/mobilnisite/slovnik/sir/)) na přijímači.

Pout hraje klíčovou roli v plánování a optimalizaci sítě. Inženýři jej používají k výpočtu pokrytí, predikci hranic buněk a správě mezibuněčných interferencí. Vyšší Pout může rozšířit pokrytí, ale může také zvýšit interference se sousedními buňkami, což vyžaduje pečlivé nastavení výkonu. V vícekanálových a [MIMO](/mobilnisite/slovnik/mimo/) systémech je Pout řízen na každou anténu a každou komponentní nosnou, aby se optimalizovala prostorová účinnost a propustnost. Specifikace 3GPP definují nejen nominální Pout, ale také aspekty jako dynamiku výstupního výkonu během přenosových mezer, náběh výkonu a parazitní emise, čímž zajišťují, že vysílače pracují efektivně bez degradace výkonu sítě nebo porušování regulatorních limitů.

## K čemu slouží

Pout je specifikován v normách 3GPP, aby byla zajištěna konzistentní a spolehlivá rádiová transmise v mobilních sítích, čímž se řeší potřeba interoperability a předvídatelného výkonu. V raných celulárních systémech by neregulovaný výstupní výkon mohl vést k nadměrným interferencím, snížené kapacitě a poškození zařízení. Definováním přesných požadavků na Pout umožňuje 3GPP výrobcům vyrábět kompatibilní zařízení a základnové stanice, které bezproblémově fungují v globálních sítích.

Parametr řeší kritické problémy v návrhu rádiových sítí, jako jsou díry v pokrytí a správa interferencí. Bez standardizovaného Pout by základnové stanice od různých výrobců mohly vysílat na různých úrovních výkonu, což by způsobovalo nerovnoměrné pokrytí a selhání předávání hovorů. U uživatelského zařízení řízený Pout zabraňuje zařízením v přetěžování uplinku a vzniku problémů typu near-far v systémech založených na [CDMA](/mobilnisite/slovnik/cdma/), jako je UMTS. Tím je zajištěno spravedlivé sdílení zdrojů a udržována stabilita sítě.

Historický kontext ukazuje, že jak se sítě vyvíjely od GSM k UMTS, význam přesného řízení Pout rostl kvůli rozprostřené povaze spektra ve WCDMA, kde výkon přímo ovlivňuje kapacitu. Zařazení podrobných specifikací Pout do vydání 3GPP, jako je Rel-4, poskytlo základ pro pokročilé mechanismy řízení výkonu, umožňující efektivní využití spektra a podporující zavedení 3G služeb s robustním výkonem a kvalitou služeb.

## Klíčové vlastnosti

- Definuje úroveň výstupního výkonu RF pro základnové stanice a uživatelská zařízení (UE)
- Měří se ve wattech nebo dBm se specifikovanými tolerancemi
- Integruje se s algoritmy řízení výkonu pro dynamické přizpůsobování
- Ovlivňuje pokrytí, interference a kapacitu sítě
- Zahrnuje požadavky na náběh výkonu a parazitní emise
- Liší se podle kmitočtového pásma, scénáře nasazení a konfigurace antény

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements

---

📖 **Anglický originál a plná specifikace:** [Pout na 3GPP Explorer](https://3gpp-explorer.com/glossary/pout/)
