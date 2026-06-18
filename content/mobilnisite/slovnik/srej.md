---
slug: "srej"
url: "/mobilnisite/slovnik/srej/"
type: "slovnik"
title: "SREJ – Selected REJect frame"
date: 2025-01-01
abbr: "SREJ"
fullName: "Selected REJect frame"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srej/"
summary: "SREJ je řídicí rámec používaný v protokolech vrstvy spojení dat, jako je LAPDm a LAPD, pro selektivní retransmisi. Vyžádá si retransmisi konkrétního, identifikovaného rámce přijatého mimo pořadí, čímž"
---

SREJ je řídicí rámec používaný v protokolech vrstvy spojení dat, jako je LAPDm, k vyžádání retransmise konkrétního rámce přijatého mimo pořadí, čímž zvyšuje efektivitu oproti zamítnutí všech následujících rámců.

## Popis

Rámec Selected REJect (SREJ) je supervizní rámec definovaný v protokolech vrstvy spojení dat, jako je [LAPD](/mobilnisite/slovnik/lapd/) (Link Access Procedure on the D-channel) a jeho mobilní varianta LAPDm, používané v signalizaci GSM a raných 3GPP systémů. Funguje v kontextu vyváženého, na opravy chyb navrženého spojení vrstvy spojení dat, typicky mezi mobilní stanicí a sítí (např. přes rozhraní Um nebo Abis). Primární funkcí rámce SREJ je implementace mechanismu selektivního odmítnutí [ARQ](/mobilnisite/slovnik/arq/) (Automatic Repeat reQuest). Když přijímač detekuje mezeru v sekvenci příchozích I-rámců (informačních rámců) – což znamená, že přijal rámec N+1, ale chybí mu rámec N – může odeslat rámec SREJ konkrétně žádající o retransmisi chybějícího rámce N. To je v protikladu k rámci [REJ](/mobilnisite/slovnik/rej/) (Reject), který žádá o retransmisi počínaje rámcem N a všech následujících rámců.

Z architektonického hlediska je rámec SREJ generován přijímací stranou entity vrstvy spojení dat. Obsahuje řídicí pole s identifikátorem příkazu SREJ a číslem posloupnosti pro odesílání N(R), které udává číslo sekvence konkrétního I-rámce, který je třeba retransmitovat. Po přijetí platného rámce SREJ musí vysílající entita retransmitovat požadovaný I-rámec s číslem sekvence N(R). Vysílač může pokračovat v odesílání rámců s čísly sekvence vyššími než N(R), zatímco zpracovává retransmisi, protože přijímač je schopen ukládat rámce přijaté mimo pořadí. Toto je klíčový aspekt jeho fungování, který umožňuje vyšší využití přenosového pásma.

Protokol zajišťuje, že v jednom směru přenosu může být současně aktivní pouze jedna podmínka SREJ. Tím se zabraňuje nejednoznačnosti. Mechanismus SREJ funguje ve spojení s dalšími supervizními rámci, jako jsou [RR](/mobilnisite/slovnik/rr/) (Receiver Ready) a [RNR](/mobilnisite/slovnik/rnr/) (Receiver Not Ready), a s procedurami obnovy založenými na časovačích, definovanými v protokolu linkové vrstvy. Jeho úlohou je zvýšit efektivitu procesu obnovy z chyb na potenciálně šumivých rádiových spojích. Tím, že žádá pouze o chybějící rámec, minimalizuje zbytečné retransmise, šetří rádiové zdroje a snižuje latenci ve srovnání se schématy go-back-N ARQ spouštěnými standardním rámcem REJ. Tato efektivita byla klíčová pro signalizační kanály, kde musí být doručování zpráv spolehlivé, ale také včasné.

## K čemu slouží

Rámec SREJ byl zaveden za účelem optimalizace obnovy z chyb ve signalizačních spojích digitálních telekomunikačních systémů, konkrétně pro řešení omezení jednodušších schémat [ARQ](/mobilnisite/slovnik/arq/). V raných digitálních mobilních systémech, jako je GSM, bylo (a stále je) rádiové rozhraní hlavním zdrojem přenosových chyb. Vrstva spojení dat potřebovala robustní, ale zároveň efektivní metodu pro zajištění spolehlivého doručování kritických signalizačních zpráv (např. pro sestavení hovoru, předávání hovoru a správu mobility). Jednoduché schéma Go-Back-N ARQ, spuštěné rámcem [REJ](/mobilnisite/slovnik/rej/), by vynutilo retransmisi všech rámců od bodu chyby, což by plýtvalo přenosovou kapacitou a zvyšovalo zpoždění, zejména pokud byla velikost okna velká nebo byl spoj náchylný k chybám.

Mechanismus selektivního odmítnutí poskytovaný SREJ tento problém vyřešil tím, že umožnil přijímači vyžádat si pouze konkrétní rámec, který byl ztracen nebo poškozen, za předpokladu, že může ukládat následující správně přijaté rámce. Tento přístup, známý jako Selective Repeat ARQ, maximalizuje propustnost na kanálech s nehromadnými chybami. Jeho vytvoření bylo motivováno potřebou co nejefektivnějšího využití vzácného a drahého rádiového spektra vyčleněného pro signalizační kanály. Nižší latence v signalizační výměně přímo zlepšovala metriky uživatelského zážitku, jako je doba sestavení hovoru.

Historicky byl SREJ součástí sady protokolů založených na [ISDN](/mobilnisite/slovnik/isdn/) (Q.921/LAPD) upravené pro mobilní použití (LAPDm). Jeho zařazení odráželo technické kompromisy konce 80. a 90. let: implementace selektivního opakování vyžadovala složitější logiku přijímače (pro ukládání do vyrovnávací paměti a změnu pořadí) než go-back-N, ale přínosy v oblasti výkonu byly považovány za hodné této dodatečné složitosti pro kritickou řídicí rovinu. S vývojem 3GPP přes UMTS a LTE se změnily základní protokoly linkové vrstvy (např. na RLC v rádiovém zásobníku), které používají jiné mechanismy ARQ, což činí SREJ specifickým pro GSM/EDGE Radio Access Network (GERAN) a určité signalizační spoje jádra sítě.

## Klíčové vlastnosti

- Implementuje Selective Repeat ARQ pro efektivní obnovu z chyb
- Vyžaduje retransmisi jediného, konkrétně identifikovaného rámce
- Umožňuje pokračovat v přenosu následujících rámců během čekání na retransmisi
- Definován v rámci formátů řídicího pole LAPD/LAPDm
- Pouze jedna podmínka SREJ je povolena současně v jednom směru přenosu
- Snižuje signalizační zpoždění a plýtvání přenosovou kapacitou ve srovnání s Go-Back-N

## Související pojmy

- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 23.046** (Rel-4) — GSM Facsimile Group 3 Service Procedures
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [SREJ na 3GPP Explorer](https://3gpp-explorer.com/glossary/srej/)
