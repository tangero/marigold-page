---
slug: "eab"
url: "/mobilnisite/slovnik/eab/"
type: "slovnik"
title: "EAB – Extended Access Barring"
date: 2025-01-01
abbr: "EAB"
fullName: "Extended Access Barring"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eab/"
summary: "Extended Access Barring (EAB) je mechanismus řízení zahlcení sítě zavedený v 3GPP pro správu pokusů o náhodný přístup od nízkoprioritních nebo strojových zařízení za podmínek přetížení. Zabráněním pří"
---

EAB je mechanismus řízení zahlcení sítě, který za přetížení blokuje přístup nízkoprioritním nebo strojovým zařízením, aby se zabránilo přetížení sítě a zajistila dostupnost kritických služeb.

## Popis

Extended Access Barring (EAB) je funkce standardizovaná 3GPP, která poskytuje vylepšenou kontrolu nad přístupem k síti za situací zahlcení, což je zvláště relevantní pro sítě s vysokou hustotou zařízení pro strojovou komunikaci ([MTC](/mobilnisite/slovnik/mtc/)). Funguje tak, že síť může vysílat informace o blokování v blocích systémových informací (SIB), konkrétně v SIB14 v LTE a SIB14/SIB15 v NR. Tyto informace definují, které kategorie uživatelských zařízení (UE) jsou dočasně vyloučeny z iniciování přístupu k síti. UE jsou konfigurovány s kategorií EAB, která může být založena na jejich profilu předplatného (např. 'EAB pro MTC zařízení') nebo jiných kritériích. Po přečtení parametrů EAB vysílaných sítí UE provede kontrolu blokování před zahájením jakéhokoli přístupového postupu pro volání iniciovaná mobilním zařízením, požadavky na relaci nebo signalizaci, s výjimkou nouzových služeb nebo přístupových tříd s vysokou prioritou.

Architektura pro EAB zahrnuje jak přístupovou síť (RAN), tak jádro sítě (CN). CN, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPS nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GS, může poskytnout konfigurační data EAN uzlům RAN ([eNB](/mobilnisite/slovnik/enb/)/gNB). RAN pak tyto informace začlení do vysílaných systémových informací. Parametry blokování zahrnují faktor blokování a dobu blokování, podobně jako u tradičního Access Class Barring (ACB), ale jsou aplikovány specificky na nakonfigurované kategorie EAB. Z pohledu sítě je mechanismus po vysílání bezstavový, protože blokování autonomně vynucuje samotné UE.

Role EAB v síti je klíčová pro řízení přetížení a zahlcení, zejména v kontextu nasazení IoT a MTC, kde může obrovské množství zařízení současně pokoušet o přístup a potenciálně způsobit signalizační bouři. Selektivním blokováním nízkoprioritních nebo na zpoždění tolerantních zařízení EAB zajišťuje, že rádiové a jádrové síťové zdroje jsou zachovány pro lidské uživatele, nouzové služby a další komunikace s vysokou prioritou. Představuje podrobnější a flexibilnější přístup ve srovnání s tradičním ACB, který rozlišuje primárně na základě pevné sady 16 přístupových tříd.

## K čemu slouží

EAB byl zaveden, aby řešil specifickou výzvu zahlcení sítě způsobeného masivním přílivem pokusů o přístup od zařízení pro strojovou komunikaci ([MTC](/mobilnisite/slovnik/mtc/)), což je klíčový scénář v internetu věcí (IoT). Tradiční mechanismy řízení zahlcení, jako je Access Class Barring (ACB), byly navrženy primárně pro provoz orientovaný na člověka a nabízely omezenou granularitu. ACB používá 16 přístupových tříd (0-9 pro běžné uživatele, 10 pro nouzové služby, 11-15 pro specifické uživatele s vysokou prioritou, jako je personál sítě), což se ukázalo jako nedostatečné pro efektivní správu různorodých kategorií IoT zařízení s různými prioritami a požadavky na služby.

Vytvoření EAB bylo motivováno potřebou sofistikovanějšího mechanismu blokování založeného na předplatném. Umožňuje operátorům definovat politiky na základě typu zařízení, profilu předplatného nebo charakteristik služeb, nikoli pouze na statické třídě. To operátorům umožňuje chránit síť během událostí přetížení – například po obnovení napájení po výpadku, kdy se miliony chytrých měřičů pokoušejí znovu připojit – blokováním pouze nízkoprioritních MTC zařízení, zatímco přístup je povolen pro běžné smartphony a kritické služby. EAB tak řeší problém signalizačního přetížení z masivních nasazení MTC a zajišťuje spolehlivost sítě a dostupnost služeb pro všechny uživatele.

## Klíčové vlastnosti

- Informace o blokování založené na vysílání, přenášené v SIB14 (LTE) a SIB14/SIB15 (NR)
- Konfigurovatelné blokování pro specifické kategorie UE na základě předplatného (např. MTC zařízení)
- Autonomní vynucování na straně UE po přečtení systémových informací
- Výjimka pro nouzové relace a přístupové třídy s vysokou prioritou
- Parametry zahrnují faktor blokování (pravděpodobnost) a dobu trvání blokování
- Podpora v architekturách EPS (LTE) i 5GS (NR)

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.011** (Rel-19) — Service Accessibility Procedures
- **TS 22.806** (Rel-13) — Application Specific Congestion Control for Data
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.704** (Rel-12) — Study on Enhanced Broadcast of System Information
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/eab/)
