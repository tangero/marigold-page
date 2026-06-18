---
slug: "ttcn-3"
url: "/mobilnisite/slovnik/ttcn-3/"
type: "slovnik"
title: "TTCN-3 – Testing and Test Control Notation version 3"
date: 2025-01-01
abbr: "TTCN-3"
fullName: "Testing and Test Control Notation version 3"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ttcn-3/"
summary: "Standardizovaný, platformně nezávislý testovací jazyk pro specifikaci testovacích sad pro komunikační protokoly a systémy. Je klíčový pro zajištění interoperability a shody síťových prvků 3GPP a uživa"
---

TTCN-3 je standardizovaný, platformně nezávislý testovací jazyk používaný k specifikaci automatizovaných testovacích sad pro zajištění interoperability a shody (conformance) komunikačních protokolů a systémů 3GPP.

## Popis

TTCN-3 (Testing and Test Control Notation version 3, Testovací a řídicí notace verze 3) je standardizovaný, vysokoúrovňový a platformně nezávislý programovací jazyk speciálně navržený pro specifikaci testovacích sad pro komunikační protokoly, služby a distribuované systémy. Jeho primární aplikace v rámci 3GPP spočívá v testování shody (conformance testing) síťových prvků a uživatelských zařízení (UE), aby bylo zajištěno, že správně implementují složité standardy. Jazyk je definován Evropským institutem pro telekomunikační standardy ([ETSI](/mobilnisite/slovnik/etsi/)) a přijat organizací 3GPP pro tvorbu testovacích případů, které ověřují chování protokolu, sekvence zpráv a funkční správnost.

Z architektonického hlediska se testovací systém TTCN-3 skládá z několika klíčových komponent. Jádrem je spustitelný kód TTCN-3 (TTCN-3 Executable, [TE](/mobilnisite/slovnik/te/)), což je zkompilovaná testovací sada. Ten komunikuje s testovaným systémem (System Under Test, [SUT](/mobilnisite/slovnik/sut/)) prostřednictvím standardizovaného rozhraní testovacího systému (Test System Interface, [TSI](/mobilnisite/slovnik/tsi/)). TSI je implementováno pomocí adaptéru platformy (Platform Adapter, [PA](/mobilnisite/slovnik/pa/)) a kodeku (Codec), které zpracovávají komunikaci s fyzickými rozhraními SUT a kódování/dekódování protokolových zpráv (např. ASN.1 [PER](/mobilnisite/slovnik/per/), [XML](/mobilnisite/slovnik/xml/)). Adaptér SUT (SUT Adapter, [SA](/mobilnisite/slovnik/sa/)) spravuje přizpůsobení specifickému běhovému prostředí SUT. Tato modulární architektura umožňuje spouštět stejné abstraktní testovací případy TTCN-3 na různých hardwarových a softwarových platformách, což je koncept známý jako přenositelnost testů.

Samotný jazyk podporuje jak zprávově orientovaný, tak procedurálně orientovaný komunikační paradigma, což jej činí vhodným pro testování signalizačních protokolů i API. Obsahuje výkonné datové typy, šablony (templates) pro definování očekávaných a odeslaných zpráv, časovače pro řízení provádění testů a přiřazování verdiktů (pass, fail, inconclusive, error). Testovací případy jsou organizovány do modulů, které mohou importovat definice a být seskupeny do testovacích kampaní. Provádění je řízeno hlavní testovací komponentou (Main Test Component, MTC), která může vytvářet a synchronizovat paralelní testovací komponenty (Parallel Test Components, PTC) pro modelování distribuovaných testovacích scénářů, jako je testování UE interagujícího s více síťovými uzly.

V ekosystému 3GPP jsou testovací sady TTCN-3 vyvíjeny pro různé testovací skupiny, včetně testování shody protokolu (Protocol Conformance Testing, PCT), testování správy rádiových zdrojů (Radio Resource Management, RRM) a testování vývoje interoperability (Interoperability Development Testing, IODT). Tyto testovací sady jsou prováděny v akreditovaných testovacích laboratořích jako součást formálního certifikačního procesu zařízení. Role TTCN-3 je proto zásadní pro celý režim shody a interoperability 3GPP, neboť poskytuje jednoznačnou, spustitelnou specifikaci očekávaného chování systému, která je nezávislá na implementaci jakéhokoli dodavatele.

## K čemu slouží

TTCN-3 byl vytvořen, aby řešil kritickou potřebu rigorózního, automatizovaného a standardizovaného testování složitých telekomunikačních systémů. Před jeho přijetím se testování často provádělo pomocí ad-hoc, proprietárních skriptů a nástrojů, které nebyly přenositelné, obtížně se udržovaly a nemohly zaručit konzistentní pokrytí testů napříč různými dodavateli a testovacími laboratořemi. Tento nedostatek standardizace byl hlavní překážkou pro dosažení skutečné interoperability ve více-dodavatelských sítích, protože drobné rozdíly v implementaci protokolu mohly vést k selhání služeb.

Motivace pro přijetí formálního testovacího jazyka, jako je TTCN-3, v rámci 3GPP vycházela z rostoucí složitosti samotných standardů, od 2G GSM přes 3G UMTS a dále. Manuální testování se stalo nepraktickým. TTCN-3 poskytuje řešení tím, že nabízí doménově specifický jazyk, který umožňuje testovacím inženýrům psát testovací případy na abstraktní úrovni, zaměřující se na logiku protokolu a očekávané chování spíše než na podrobnosti nízkoúrovňové platformy. Tato abstrakce umožňuje vytvoření jediné, autoritativní testovací sady pro daný protokol, kterou musí projít všichni dodavatelé zařízení, čímž je zajištěn konzistentní základ pro shodu.

Jeho zavedení formalizovalo testovací proces, zkrátilo čas uvedení nových funkcí na trh umožněním automatizovaného regresního testování a výrazně zlepšilo kvalitu a spolehlivost nasazených sítí. Tím, že poskytuje společný jazyk pro specifikaci testů, se TTCN-3 stal nepostradatelným nástrojem pro ověřování, že miliardy zařízení a síťových uzlů po celém světě správně implementují specifikace 3GPP, a tím zajišťuje globální interoperabilitu, která definuje moderní mobilní komunikaci.

## Klíčové vlastnosti

- Platformně nezávislý jazyk pro specifikaci testů
- Podpora testování zprávově orientované i procedurálně orientované komunikace
- Modulární architektura s adaptérem platformy (PA) a kodekem pro rozhraní SUT
- Výkonný systém šablon (templates) pro definování očekávaných a odeslaných protokolových datových jednotek (PDU)
- Vestavěná správa časovačů a přiřazování verdiktů (pass, fail, inconclusive, error)
- Podpora souběžných testovacích komponent (PTC) pro modelování distribuovaných systémů

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TTCN-3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttcn-3/)
