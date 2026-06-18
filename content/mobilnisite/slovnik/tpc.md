---
slug: "tpc"
url: "/mobilnisite/slovnik/tpc/"
type: "slovnik"
title: "TPC – Transmit Power Control Command Error Rate"
date: 2025-01-01
abbr: "TPC"
fullName: "Transmit Power Control Command Error Rate"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tpc/"
summary: "Výkonnostní metrika měřící chybovost příkazů řízení vysílacího výkonu přenášených přes rozhraní rádiového rozhraní. Je klíčová pro hodnocení spolehlivosti signalizace řízení výkonu, která přímo ovlivň"
---

TPC (chybovost příkazů řízení vysílacího výkonu) je chybovost příkazů řízení vysílacího výkonu přenášených přes rozhraní rádiového rozhraní, což je metrika klíčová pro hodnocení spolehlivosti signalizace řízení výkonu v systémech UMTS a LTE.

## Popis

Chybovost příkazů řízení vysílacího výkonu (TPC [CER](/mobilnisite/slovnik/cer/)) je klíčový ukazatel výkonnosti definovaný ve specifikacích 3GPP pro systémy UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) a LTE. Kvantifikuje pravděpodobnost, že příkaz řízení vysílacího výkonu (TPC), přenášený na fyzické vrstvě, je přijat s chybou zamýšleným přijímačem (uživatelským zařízením nebo NodeB). Příkazy TPC jsou nezbytné pro uzavřenou smyčku řízení výkonu, kde přijímač instruuje vysílač, aby zvýšil nebo snížil svůj výstupní výkon pro udržení cílové kvality signálu, typicky měřené jako poměr signálu k interferenci ([SIR](/mobilnisite/slovnik/sir/)). TPC CER se vypočítá jako poměr chybně dekódovaných příkazů TPC k celkovému počtu odeslaných příkazů TPC za definované měřicí období za specifických podmínek kanálu.

Při provozu jsou příkazy TPC vloženy do vyhrazených fyzických kanálů. Například v UMTS [FDD](/mobilnisite/slovnik/fdd/) jsou bity TPC součástí uplinkového [DPCCH](/mobilnisite/slovnik/dpcch/) a downlinkového [DPCH](/mobilnisite/slovnik/dpch/). Přijímač (NodeB v uplinku, UE v downlinku) tyto bity dekóduje, aby určil příkaz úpravy výkonu. Chyby mohou nastat v důsledku zhoršení kanálu, jako je útlum, interference nebo šum, což vede k nesprávným úpravám výkonu. Vysoká TPC CER snižuje účinnost řízení výkonu, což způsobuje, že vysílač používá suboptimální úrovně výkonu. To může mít za následek zvýšenou interferenci pro ostatní uživatele, sníženou kvalitu spojení, vyšší spotřebu baterie v UE a celkové zhoršení kapacity a pokrytí systému. Proto je TPC CER kritickým parametrem pro plánování sítě, optimalizaci a testování shody UE a základnových stanic.

Měření TPC CER je specifikováno za různých testovacích podmínek v dokumentech 3GPP TS 25.101 (vysílání a příjem rádiového signálu UE), TS 25.104 (vysílání a příjem rádiového signálu NodeB) a podobných specifikacích pro LTE. Ty definují referenční měřicí kanály, podmínky šíření (např. profily vícecestného útlumu) a požadované výkonnostní prahové hodnoty. Například UE musí dosáhnout TPC CER pod určitou hodnotou (např. 10^-2 nebo 10^-3) při specifikovaných poměrech signálu k šumu, aby byla shodná. Metrika se používá nejen pro certifikaci, ale také v drive testech a nástrojích pro monitorování sítě k posouzení reálného výkonu řízení výkonu. Zajištěním nízké TPC CER mohou operátoři udržovat efektivní správu rádiových zdrojů, minimalizovat interferenci a poskytovat konzistentní kvalitu služeb.

## K čemu slouží

TPC [CER](/mobilnisite/slovnik/cer/) existuje jako standardizovaná míra pro zajištění spolehlivosti signalizace řízení vysílacího výkonu, která je zásadní pro provoz systémů založených na [CDMA](/mobilnisite/slovnik/cdma/), jako je UMTS, a systémů založených na OFDMA, jako je LTE s funkcemi řízení výkonu. V těchto systémech je přesné řízení výkonu klíčové pro potlačení problému blízko-daleko, správu intracelulární a intercelulární interference a šetření životnosti baterie UE. Bez přesného doručení příkazu TPC se smyčky řízení výkonu stanou nestabilními, což vede ke zhoršení výkonu sítě. Před standardizací byl výkon řízení výkonu hodnocen nepřímo prostřednictvím celkových metrik kvality spojení, ale pro přesné inženýrství a validaci zařízení byla potřebná přímá metrika chybovosti příkazů.

Specifikace TPC CER řeší potřebu kvantifikovatelného, testovatelného parametru, který výrobci zařízení a síťoví operátoři mohou používat k zajištění, že mechanismy řízení výkonu fungují podle záměru za různých podmínek kanálu. Umožňuje konzistentní testování shody napříč zařízeními různých dodavatelů, čímž zajišťuje interoperabilitu a spolehlivý provoz sítě. Definováním přijatelných chybovostí 3GPP zajišťuje, že příkazy řízení výkonu jsou dostatečně robustní, což sítím umožňuje udržovat optimální úrovně vysílacího výkonu, maximalizovat kapacitu a poskytovat konzistentní uživatelský zážitek i v náročných rádiových prostředích.

## Klíčové vlastnosti

- Měří chybovost příkazů řízení výkonu na fyzické vrstvě
- Definována pro uplinkový i downlinkový směr
- Používá se při testování shody pro UE a NodeB/gNB
- Kritická pro stabilitu uzavřené smyčky řízení výkonu
- Specifikována za různých modelů šířicích kanálů
- Ovlivňuje interferenci v síti a výkonnost kapacity

## Související pojmy

- [SIR – Signal-to-Interference Ratio](/mobilnisite/slovnik/sir/)
- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [TPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpc/)
