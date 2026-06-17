---
slug: "f-tpich"
url: "/mobilnisite/slovnik/f-tpich/"
type: "slovnik"
title: "F-TPICH – Fractional Transmitted Precoding Indicator Channel"
date: 2025-01-01
abbr: "F-TPICH"
fullName: "Fractional Transmitted Precoding Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/f-tpich/"
summary: "Downlinkový fyzický kanál v 3GPP UTRA (UMTS Terrestrial Radio Access) používaný v souvislosti s MIMO (Multiple-Input Multiple-Output) k signalizaci prekódovacích informací z Node B k uživatelskému zař"
---

F-TPICH je downlinkový fyzický kanál v 3GPP UTRA, který signalizuje informace o prekódovací matici z Node B k UE, aby umožnil MIMO operace, jako je uzavřená smyčka pro diverzitu vysílání a prostorové multiplexování.

## Popis

Fractional Transmitted Precoding Indicator Channel (F-TPICH) je vyhrazený downlinkový fyzický kanál definovaný v 3GPP UTRA (Universal Terrestrial Radio Access), konkrétně pro systémy UMTS (WCDMA). Funguje v kontextu [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) přenosů, kde se na straně Node B (základnové stanice) i uživatelského zařízení (UE) používají víceanténové systémy ke zvýšení výkonu. Primární funkcí F-TPICH je přenášet Transmitted Precoding Indicator (TPI), což je řídicí signál, který informuje UE o prekódovací matici aplikované Node B na downlinkových datových kanálech. Prekódování je technika, při níž jsou vysílané signály váženy napříč anténami za účelem vytvarování vyzařovacího diagramu a optimalizace kvality signálu na přijímací straně na základě stavu kanálu.

Z architektonického hlediska je F-TPICH vysílán spolu s dalšími downlinkovými kanály, jako je [DPCH](/mobilnisite/slovnik/dpch/) (Dedicated Physical Channel) nebo [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/) (High-Speed Physical Downlink Shared Channel), když je konfigurováno MIMO. Kanál je charakterizován svým rozprostíracím kódem a časováním vůči přidruženému datovému kanálu. Node B vypočítá optimální prekódovací matici na základě informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) od UE (např. prostřednictvím pole [FBI](/mobilnisite/slovnik/fbi/) v uplinku). Tuto matici pak aplikuje na datový přenos a současně odešle odpovídající hodnotu TPI na F-TPICH. UE přijme F-TPICH, dekóduje TPI a použije jej ke správné demodulaci a dekódování prekódovaných datových signálů. Tento proces umožňuje uzavřenou smyčku MIMO operací, kde se vysílač přizpůsobuje kanálu v reálném čase.

F-TPICH podporuje dva hlavní MIMO režimy: uzavřenou smyčku pro diverzitu vysílání ([CLTD](/mobilnisite/slovnik/cltd/)) a prostorové multiplexování (SM). V CLTD prekódování zlepšuje zisk diverzity, potlačuje úniky a zvyšuje pokrytí. V SM pomáhá oddělit více datových proudů, čímž zvyšuje propustnost. Kanál je „fractional“ (částečný), protože nemusí být vysílán nepřetržitě; může být přerušován nebo snížen jeho výkon, když není potřeba, čímž šetří zdroje. Mezi klíčové parametry patří délka TPI bitů (např. 2 nebo 4 bity, definující až 4 nebo 16 prekódovacích matic) a výkonový offset vůči pilotnímu kanálu. F-TPICH je nedílnou součástí pokročilých funkcí UTRA, jako je [HSDPA](/mobilnisite/slovnik/hsdpa/) MIMO, umožňující vyšší datové rychlosti a robustní výkon v mobilních scénářích.

## K čemu slouží

F-TPICH byl zaveden, aby řešil potřebu efektivní signalizace prekódovacích informací v UTRA [MIMO](/mobilnisite/slovnik/mimo/) systémech a umožnil uzavřenou smyčku prostorového zpracování. Před jeho zavedením se MIMO implementace spoléhaly na techniky s otevřenou smyčkou nebo omezené zpětnovazební mechanismy, které byly méně adaptivní na rychle se měnící rádiové podmínky. F-TPICH poskytuje vyhrazený kanál s nízkou latencí pro předání přesné prekódovací matice aplikované Node B, což umožňuje UE přesně obnovit vysílaná data bez explicitní znalosti matice kanálu. Tím řeší problém složitosti přijímače a degradace výkonu v MIMO prostředích.

Jeho vytvoření ve verzi Release 11 bylo motivováno vývojem UMTS směrem k vyšším datovým rychlostem a lepší spektrální efektivitě, zejména s vylepšeními HSDPA. F-TPICH umožňuje pokročilé anténní technologie, které se staly proveditelné s výkonnějšími základnovými stanicemi a zařízeními. Tím, že umožňuje uzavřenou smyčku MIMO, umožňuje sítím efektivněji využívat prostorové dimenze, čímž zvyšuje kapacitu a uživatelskou propustnost. Návrh kanálu vyvažuje režii a výkon – jeho částečná povaha minimalizuje spotřebu zdrojů a zároveň poskytuje včasné aktualizace. F-TPICH tak hrál klíčovou roli v prodloužení životnosti 3G sítí a překlenul mezeru směrem k 4G LTE, které pro podobné účely používá odlišné struktury referenčních signálů.

## Klíčové vlastnosti

- Vyhrazený downlinkový fyzický kanál pro přenos prekódovacího indikátoru
- Podporuje režimy uzavřené smyčky MIMO (diverzita vysílání a prostorové multiplexování)
- Přenáší bity Transmitted Precoding Indicator (TPI) (např. 2 nebo 4 bity)
- Částečný přenos umožňuje efektivitu zdrojů prostřednictvím přerušování
- Umožňuje UE správně demodulovat prekódované datové kanály
- Nedílná součást vylepšení UTRA HSDPA MIMO

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [F-TPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/f-tpich/)
