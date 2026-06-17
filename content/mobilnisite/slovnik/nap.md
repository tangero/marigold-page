---
slug: "nap"
url: "/mobilnisite/slovnik/nap/"
type: "slovnik"
title: "NAP – Network Access Provider"
date: 2025-01-01
abbr: "NAP"
fullName: "Network Access Provider"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nap/"
summary: "Subjekt, který vlastní a provozuje fyzickou a logickou infrastrukturu rádiové přístupové sítě (RAN), přes kterou se uživatel připojuje. Poskytuje bezdrátové připojení, ale může být oddělený od poskyto"
---

NAP (poskytovatel síťového přístupu) je subjekt, který vlastní a provozuje infrastrukturu rádiové přístupové sítě poskytující bezdrátové připojení, a který může být oddělený od poskytovatele služeb.

## Popis

Network Access Provider (NAP, poskytovatel síťového přístupu) je logický a často i právní subjekt v architektuře 3GPP, který je odpovědný za poskytování infrastruktury rádiové přístupové sítě (RAN). To zahrnuje základnové stanice (NodeBs, eNodeBs, gNBs), rádiové řadiče a přenosovou síť, která je spojuje s jádrem sítě. NAP vlastní nebo pronajímá rádiové spektrum a provozuje zařízení, které vytváří počáteční bezdrátové spojení s uživatelským zařízením (UE). Zásadní je, že NAP je odlišný od Network Service Provider (NSP) nebo Home PLMN ([HPLMN](/mobilnisite/slovnik/hplmn/)), který poskytuje samotné předplatné, autentizaci a služby koncovému uživateli.

Operační vztah funguje následovně: Když se UE pokouší připojit k síti, nejprve se připojí k rádiové infrastruktuře provozované NAP. Tento NAP může být domácím operátorem účastníka (kde jsou NAP a NSP stejný subjekt) nebo navštíveným operátorem (v roamingových scénářích). RAN NAP přepošle požadavek na připojení do jádra sítě. V moderních architekturách je to často usnadněno mechanismy sdílení sítě, jako je MORAN (Multi-Operator Radio Access Network) nebo [MOCN](/mobilnisite/slovnik/mocn/) (Multi-Operator Core Network). Ve scénáři MOCN je jedna RAN (provozovaná jedním NAP) sdílena a připojena k jádrovým sítím více NSP. RAN vysílá PLMN ID všech podporovaných NSP a UE si jedno vybere.

Role NAP je primárně na přístupové vrstvě (Access Stratum, [AS](/mobilnisite/slovnik/as/)). Spravuje přidělování rádiových prostředků, plánování, provádění předávání hovorů (handover) a fyzickou vrstvu pro přenos/příjem pro UE. Z obchodního a signalizačního hlediska je NAP identifikován v protokolech a dohodách. Pro účtování a vyúčtování, zejména v roamingu, je klíčové sledovat, který NAP poskytl rádiový přístup. Toto rozlišení je vysoce relevantní pro Mobile Virtual Network Operators ([MVNO](/mobilnisite/slovnik/mvno/)), kteří fungují jako NSP, ale nevlastní žádnou RAN; kupují hromadný přístup od hostitelského NAP. Specifikace 3GPP definují rozhraní a procedury (např. přes rozhraní S1, [N2](/mobilnisite/slovnik/n2/), X2), které umožňují RAN NAP komunikovat s potenciálně více oddělenými jádrovými sítěmi provozovanými různými NSP.

## K čemu slouží

Koncept Network Access Provider (NAP) byl formalizován, aby oddělil vlastnictví infrastruktury rádiové sítě od poskytování služeb účastníkům. Toto oddělení řeší několik ekonomických a provozních výzev v telekomunikačním průmyslu. Primární motivací je umožnit nové obchodní modely, nejvýznamněji Mobile Virtual Network Operators ([MVNO](/mobilnisite/slovnik/mvno/)) a rozsáhlé dohody o sdílení sítě, aniž by musel každý poskytovatel služeb investovat miliardy do výstavby celostátní fyzické sítě.

Historicky byli operátoři vertikálně integrovaní, vlastnili jak RAN, tak jádrovou síť. To vytvářelo vysoké bariéry vstupu na trh. Model NAP/NSP tyto bariéry snižuje tím, že umožňuje subjektu (NSP) nabízet mobilní služby pronájmem kapacity rádiového přístupu od vlastníka infrastruktury (NAP). To podporuje konkurenci a rozmanitost služeb. Dále ve scénářích, jako je pokrytí venkovských oblastí nebo nová nasazení 5G, jsou náklady na výstavbu hustých sítí pro jediného operátora prohibitivní. Sdílení sítě, kdy jeden NAP vybuduje infrastrukturu a více operátorů ji využívá, se stává ekonomicky životaschopným. Koncept NAP poskytuje architektonický a smluvní rámec pro toto. Také objasňuje role v roamingu: navštívená síť funguje jako NAP pro roamingového účastníka a poskytuje rádiový přístup, zatímco domácí síť zůstává NSP a řeší autentizaci a účtování. Toto jasné oddělení je nezbytné pro přesné velkoobchodní účtování a vyúčtování mezi operátory.

## Klíčové vlastnosti

- Vlastní a provozuje fyzickou infrastrukturu rádiové přístupové sítě (RAN)
- Drží licenci pro a spravuje rádiové spektrum
- Může být samostatný subjekt od Network Service Provider (NSP)
- Umožňuje obchodní modely jako MVNO a sdílení sítě (MOCN/MORAN)
- Identifikován v dohodách o sdílení sítě a roamingu
- Spravuje spojení na přístupové vrstvě (AS) pro UE

## Související pojmy

- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.333** (Rel-19) — ProSe Management Objects for UE Configuration

---

📖 **Anglický originál a plná specifikace:** [NAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nap/)
