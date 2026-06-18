---
slug: "dai"
url: "/mobilnisite/slovnik/dai/"
type: "slovnik"
title: "DAI – Downlink Assignment Index"
date: 2025-01-01
abbr: "DAI"
fullName: "Downlink Assignment Index"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dai/"
summary: "DAI je čítačové pole v downlink řídicí informaci (DCI) LTE a NR, které udává kumulativní počet downlink přiřazení přenášených k UE. Umožňuje UE detekovat zmeškané DCI a udržovat přesnou HARQ-ACK zpětn"
---

DAI je čítačové pole v downlink řídicí informaci LTE a NR, které udává kumulativní počet downlink přiřazení, aby pomohlo UE detekovat zmeškané povolení (grants) a udržovat přesnou HARQ-ACK zpětnou vazbu.

## Popis

Downlink Assignment Index (DAI) je základní mechanismus ve specifikacích 3GPP LTE a NR, který řeší problém detekce zmeškané downlink řídicí informace v procedurách [HARQ-ACK](/mobilnisite/slovnik/harq-ack/) zpětné vazby. Ve struktuře řídicího kanálu fyzické vrstvy je DAI vloženo do formátů Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)), které plánují přenosy na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)). Toto čítačové pole funguje specificky ve scénářích vyžadujících zpětnou vazbu za více podrámců nebo více slotů, nejvýznamněji v konfiguracích Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)), kde může být více downlink přiřazení potvrzeno v jediném uplink podrámci.

Architektonicky DAI funguje uvnitř řetězce zpracování fyzické vrstvy UE, konkrétně v modulu generování HARQ-ACK. Když UE přijme DCI obsahující hodnotu DAI, interpretuje ji jako indikátor toho, kolik downlink přiřazení bylo do daného okamžiku přeneseno v rámci specifického sdružovacího okna (bundling window). UE udržuje interní čítač, který sleduje přijaté hodnoty DAI, což jí umožňuje detekovat nesrovnalosti indikující zmeškaná DCI. Tato schopnost detekce je klíčová, protože zmeškaná plánovací přiřazení by jinak vedly k nesprávné HARQ-ACK zpětné vazbě, což by mohlo způsobit zbytečné retransmise nebo selhání protokolu.

Technická implementace se mezi LTE a NR liší, ale sleduje podobné principy. V LTE má DAI typicky 2 bity pro TDD konfigurace a počítá modulo-4 v rámci sdružovacího okna. V NR je mechanismus sofistikovanější s poli counter-DAI a total-DAI v některých formátech DCI, což poskytuje zvýšenou spolehlivost pro scénáře plánování více PDSCH. Konstrukce HARQ-ACK kodebooku (codebook) UE přímo závisí na správné interpretaci hodnot DAI, aby určila, které HARQ-ACK bity zahrnout a jejich správné pořadí v payload zpětné vazby.

Role DAI přesahuje pouhou detekci chyb a umožňuje efektivní využití spektra. Tím, že umožňuje přesnou HARQ-ACK zpětnou vazbu i při zmeškání některých DCI, zabraňuje vrstvě řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) v iniciování zbytečných retransmisí za správně přijatá data. Tato optimalizace je obzvláště cenná v TDD systémech s asymetrickými poměry downlink/uplink, kde je příležitost pro zpětnou vazbu omezená vzhledem k počtu potenciálních downlink přenosů. Mechanismus tak přímo přispívá k propustnosti systému a výkonu z hlediska latence v reálných nasazeních sítě.

## K čemu slouží

DAI bylo zavedeno, aby vyřešilo zásadní problém spolehlivosti [HARQ-ACK](/mobilnisite/slovnik/harq-ack/) zpětné vazby: když UE zmešká downlink přiřazení ([DCI](/mobilnisite/slovnik/dci/)), nemůže vygenerovat správnou HARQ-ACK zpětnou vazbu pro odpovídající přenos [PDSCH](/mobilnisite/slovnik/pdsch/). Před implementací DAI by zmeškaná DCI způsobila, že UE sestaví neúplný HARQ-ACK kodebook, což vede k nesouladu mezi zpětnou vazbou UE a očekáváním gNB. Tento nesoulad mohl způsobit několik problémů: zbytečné retransmise správně přijatých dat (plýtvání rádiovými zdroji), selhání retransmise nesprávně přijatých dat (snížení spolehlivosti) a potenciální timeouty protokolu nebo selhání rádiového spoje.

Historický kontext vzniku DAI spočívá ve vývoji od systémů Frequency Division Duplex (FDD) ke složitějším nasazením Time Division Duplex (TDD) v LTE. V systémech FDD je načasování HARQ-ACK pevné a předvídatelné, přičemž každý downlink přenos má vyhrazenou příležitost pro uplink zpětnou vazbu. Konfigurace TDD s asymetrickými poměry downlink/uplink (jako konfigurace 2 s více downlink než uplink podrámci) však vyžadovaly sdružení (bundling) více downlink HARQ-ACK odpovědí do jediného uplink podrámce. Toto sdružení vytvořilo možnost, že UE může zmeškat některá DCI, zatímco jiná přijme, aniž by existoval mechanismus pro detekci těchto zmeškaných příkazů.

DAI tyto limity řešilo poskytnutím explicitní signalizace, která umožňuje UE detekovat chybějící přiřazení a podle toho sestavit HARQ-ACK kodebook. Řešení bylo motivováno zejména potřebou podpory efektivního provozu TDD v LTE Release 8, kde byla klíčovým požadavkem flexibilita spektra. Tím, že DAI umožnilo spolehlivou HARQ-ACK zpětnou vazbu v náročných rádiových podmínkách, kde může být příjem řídicího kanálu nedokonalý, přispělo k celkové robustnosti systému LTE a připravilo cestu pro ještě flexibilnější mechanismy plánování v následujících specifikacích NR.

## Klíčové vlastnosti

- Umožňuje detekci zmeškaných downlink přiřazení UE prostřednictvím signalizace čítače
- Podporuje přesnou konstrukci HARQ-ACK kodebooku pro zpětnou vazbu za více podrámců v TDD
- Zabraňuje zbytečným retransmisím udržováním souladu mezi stavy UE a gNB
- Funguje s dynamickými i semi-statickými konfiguracemi HARQ-ACK kodebooku
- Zvyšuje spolehlivost v náročných rádiových podmínkách, kde může selhat příjem řídicího kanálu
- Podporuje efektivní využití spektra v asymetrických TDD konfiguracích

## Související pojmy

- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)

## Definující specifikace

- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [DAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dai/)
