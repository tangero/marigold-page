---
slug: "cra"
url: "/mobilnisite/slovnik/cra/"
type: "slovnik"
title: "CRA – Clean Random Access"
date: 2025-01-01
abbr: "CRA"
fullName: "Clean Random Access"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cra/"
summary: "Clean Random Access (CRA) je funkce 3GPP, která snižuje interferenci během počátečního přístupu k síti optimalizací procedur náhodného přístupu. Zlepšuje spolehlivost připojení a snižuje latenci zaříz"
---

CRA je funkce 3GPP, která snižuje interferenci během počátečního přístupu k síti optimalizací procedur náhodného přístupu za účelem zlepšení spolehlivosti připojení a snížení latence zařízení.

## Popis

Clean Random Access (CRA) je standardizovaný mechanismus v rámci specifikací 3GPP, který zvyšuje výkon a spolehlivost procedur náhodného přístupu v celulárních sítích. Tato technologie konkrétně řeší problémy s interferencí, které nastávají, když se více zařízení uživatelského vybavení (UE) pokouší současně o přístup k síti prostřednictvím kanálu fyzického náhodného přístupu ([PRACH](/mobilnisite/slovnik/prach/)). CRA funguje implementací optimalizovaného výběru preambule, časování přenosu a algoritmů přidělování zdrojů, které minimalizují kolize a snižují interferenci během počáteční fáze přístupu.

Z architektonického hlediska CRA funguje v rámci vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a fyzické vrstvy ([PHY](/mobilnisite/slovnik/phy/)) protokolového zásobníku rádiového rozhraní. Systém koordinuje spolupráci mezi UE a základnovou stanicí ([eNB](/mobilnisite/slovnik/enb/) nebo gNB) za účelem implementace procedur náhodného přístupu citlivých na interferenci. Mezi klíčové komponenty patří vylepšené algoritmy detekce preambulí v základnové stanici, optimalizované mechanismy odložení pro retransmise a inteligentní dělení zdrojů, které odděluje pokusy o přístup s podporou CRA od konvenčních pokusů o náhodný přístup. Základnová stanice vysílá konfigurační parametry CRA prostřednictvím systémových informačních bloků ([SIB](/mobilnisite/slovnik/sib/)), což umožňuje kompatibilním UE využívat vylepšené přístupové procedury.

CRA využívá několik technických mechanismů k dosažení svých cílů. Patří mezi ně strategie skupin preambulí, které kategorizují preambule na základě typu zařízení nebo požadavků služby, algoritmy řízení výkonu, které upravují vysílací výkon na základě měření interference, a dělení zdrojů v časové doméně, které přiděluje specifické podrámce nebo sloty pro operace CRA. Systém také implementuje pokročilé techniky detekce a řešení kolizí, které snižují pravděpodobnost, že více UE současně vybere identické preambule. Tyto mechanismy společně vytvářejí 'čistší' prostředí náhodného přístupu se sníženou interferencí a vyšší úspěšností.

V síťovém ekosystému hraje CRA klíčovou roli při zlepšování výkonu počátečního přístupu, zejména ve scénářích hustého nasazení a pro aplikace citlivé na zpoždění. Technologie se integruje s existujícími procedurami náhodného přístupu definovanými ve specifikacích 3GPP a zároveň poskytuje vylepšené možnosti pro správu interference. Implementace CRA vyžaduje koordinaci mezi schopnostmi UE, konfiguracemi základnových stanic a optimalizací síťových parametrů pro dosažení maximálního přínosu. Tato funkce je zvláště cenná v 5G sítích podporujících případy užití masivní komunikace mezi stroji (mMTC) a ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), kde je spolehlivý a včasný počáteční přístup nezbytný.

## K čemu slouží

CRA byl vyvinut pro řešení významných problémů s interferencí, které nastávají během procedur náhodného přístupu v celulárních sítích, zejména s tím, jak se síťová nasazení stávala hustšími a počet zařízení rostl. Tradiční mechanismy náhodného přístupu trpěly vysokou mírou kolizí, když se více zařízení pokoušelo o současný přístup, což vedlo k selhání připojení, zvýšené latenci a snížené síťové efektivitě. Tato omezení se stala zvláště problematickými s nástupem aplikací internetu věcí (IoT), které vyžadují spolehlivé připojení masivního počtu zařízení s minimálním lidským zásahem.

Vytvoření CRA bylo motivováno potřebou podporovat nové případy užití v sítích 5G a dalších generací, včetně průmyslové automatizace, chytrých měst a připojených vozidel, kde je spolehlivý počáteční přístup kritický. Předchozí přístupy k náhodnému přístupu, ačkoli funkční pro tradiční služby mobilního širokopásmového připojení, se ukázaly jako nedostatečné pro scénáře vyžadující masivní konektivitu nebo ultra-spolehlivou komunikaci s nízkou latencí. CRA poskytuje standardizované řešení, které zlepšuje míru úspěšnosti přístupu při zachování zpětné kompatibility s existujícími zařízeními a sítěmi.

Historicky správa interference při náhodném přístupu spoléhala na základní algoritmy odložení a omezené dělení preambulí, což se stalo nedostatečným s rostoucím zatížením sítě. CRA zavedl sofistikovanější techniky zmírňování interference, které se dokážou přizpůsobit měnícím se síťovým podmínkám a typům zařízení. Technologie řeší konkrétní omezení předchozích přístupů tím, že poskytuje dynamické přidělování zdrojů, vylepšenou správu preambulí a strategie přenosu citlivé na interferenci, které společně zlepšují robustnost procedury počátečního přístupu v náročných rádiových prostředích.

## Klíčové vlastnosti

- Výběr a přidělování preambulí citlivé na interferenci
- Dynamické dělení zdrojů v časové doméně pro náhodný přístup
- Vylepšené mechanismy detekce a řešení kolizí
- Optimalizace řízení výkonu pro přenosy náhodného přístupu
- Zpětná kompatibilita s dědícími procedurami náhodného přístupu
- Konfigurace prostřednictvím vysílání systémových informací

## Související pojmy

- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)

## Definující specifikace

- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [CRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cra/)
