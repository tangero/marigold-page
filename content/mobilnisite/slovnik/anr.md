---
slug: "anr"
url: "/mobilnisite/slovnik/anr/"
type: "slovnik"
title: "ANR – Automatic Neighbour Relationship"
date: 2026-01-01
abbr: "ANR"
fullName: "Automatic Neighbour Relationship"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/anr/"
summary: "ANR je funkce samo-organizující sítě (SON), která automatizuje vytváření, údržbu a optimalizaci seznamů sousedních buněk v mobilních sítích. Odstranňuje potřebu ruční konfigurace, čímž snižuje provozn"
---

ANR je funkce samo-organizující sítě, která automatizuje vytváření, údržbu a optimalizaci seznamů sousedních buněk za účelem zlepšení předávání hovorů a stability sítě.

## Popis

Automatic Neighbour Relationship (ANR) je klíčová funkce samo-organizující sítě ([SON](/mobilnisite/slovnik/son/)) definovaná ve standardech 3GPP, primárně pro rádiový přístupový síť (RAN). Jejím hlavním operačním doménou je základnová stanice (eNodeB v LTE, gNB v NR), která hostuje funkci ANR. Proces je zásadně řízen uživatelským zařízením (UE). UE průběžně provádí měření na detekovaných buňkách, včetně těch, které nejsou uvedeny v jeho aktuální tabulce sousedních vztahů ([NRT](/mobilnisite/slovnik/nrt/)). Když UE nahlásí silnou, dosud neznámou buňku (identifikovanou svým Physical Cell ID ([PCI](/mobilnisite/slovnik/pci/)) a, což je klíčové, jejím globálně jedinečným identifikátorem [E-UTRAN](/mobilnisite/slovnik/e-utran/) Cell Global Identifier ([ECGI](/mobilnisite/slovnik/ecgi/)) nebo ekvivalentem), funkce ANR obsluhující základnové stanice spustí proceduru k navázání sousedního vztahu.

Toto navázání zahrnuje několik klíčových kroků. Nejprve obsluhující buňka nařídí UE, aby přečetlo systémový informační blok typu 1 ([SIB1](/mobilnisite/slovnik/sib1/)) nebo ekvivalentní vysílané informace z nově detekované buňky, aby získalo její globální identifikátor (ECGI/[NCGI](/mobilnisite/slovnik/ncgi/)) a kód sledovací oblasti ([TAC](/mobilnisite/slovnik/tac/)). Jakmile jsou tyto informace získány a nahlášeny, může obsluhující buňka použít rozhraní X2 (v LTE) nebo Xn (v NR) k navázání přímého signalizačního spojení se základnovou stanicí sousední buňky. Po úspěšném nastavení je záznam sousedního vztahu (NR) automaticky přidán do NRT. Tento záznam obsahuje atributy definující vztah, jako například zda se jedná o kandidáta pro předání hovoru (No Remove, No HO) a zda se jedná o souseda pro pokrytí nebo kapacitu.

Funkce ANR spravuje celý životní cyklus sousedních vztahů. Nejenže přidává nové vztahy, ale také sleduje jejich využití a výkon. Vztahy, které nejsou nikdy použity pro úspěšná předání hovorů nebo které konzistentně vedou k selháním předání, mohou být automaticky odstraněny nebo sníženy v prioritě, čímž se NRT v čase optimalizuje. Toto dynamické řízení je nezbytné v moderních sítích s funkcemi jako je Carrier Aggregation (CA), Dual Connectivity (DC) a hustá nasazení malých buněk, kde se rádiové prostředí a optimální sady sousedů často mění. ANR tak zajišťuje, že tabulka sousedních vztahů je vždy relevantní, přesná a optimalizovaná pro bezproblémovou mobilitu, a tvoří tak základní automatizační vrstvu pro moderní provoz RAN.

## K čemu slouží

ANR byl vytvořen, aby vyřešil významnou provozní zátěž a výkonnostní omezení spojená s ruční konfigurací seznamů sousedních buněk v mobilních sítích. Před érou SON a ANR museli síťoví inženýři ručně definovat každou potenciální sousední buňku pro každou základnovou stanici na základě testů v terénu a predikcí šíření signálu. Tento proces byl extrémně časově náročný, drahý a náchylný k lidské chybě. Nepřesné nebo chybějící sousední vztahy přímo způsobovaly přerušení hovorů, selhání předání a špatný uživatelský zážitek. Navíc, jak se sítě vyvíjely s více kmitočtovými pásmy, heterogenními nasazeními (makro, mikro, piko buňky) a dynamickými topologiemi, se ruční správa stala naprosto neudržitelnou.

Zavedení ANR v 3GPP Release 8, spolu se systémem LTE, bylo základním kamenem vize samo-organizující sítě. Řešilo kritickou potřebu snížení provozních výdajů (OPEX) a robustnosti sítě. Automatizací objevování a správy sousedů ANR eliminuje chyby v konfiguraci, dramaticky urychluje nasazení a optimalizaci sítě a umožňuje síti samostatně se přizpůsobovat změnám, jako je přidání nových buněk nebo změny rádiových podmínek. Tato automatizace není pouze pohodlností, ale nutností pro škálovatelnost a spolehlivost moderních a budoucích sítí, včetně 5G NR, kde je hustota a složitost sítě řádově větší než u starších systémů.

## Klíčové vlastnosti

- Automatizované objevování nových sousedních buněk prostřednictvím hlášení měření od UE
- Automatické získávání globálních identifikátorů buněk (ECGI/NCGI) instruováním UE ke čtení systémových informací
- Dynamická správa tabulky sousedních vztahů (NRT) včetně přidávání, úprav a odstraňování záznamů
- Integrace s nastavením rozhraní X2/Xn pro automatické navazování spojení mezi základnovými stanicemi
- Podpora správy sousedních vztahů pro Carrier Aggregation a Dual Connectivity
- Snížení ručních provozních úloh a s nimi spojených konfiguračních chyb

## Definující specifikace

- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 28.313** (Rel-20) — Management and orchestration; SON for 5G networks
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.511** (Rel-19) — ANR Management Concepts & Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.896** (Rel-14) — Study on Flexible eNB-ID and Cell-ID in E-UTRAN
- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study

---

📖 **Anglický originál a plná specifikace:** [ANR na 3GPP Explorer](https://3gpp-explorer.com/glossary/anr/)
