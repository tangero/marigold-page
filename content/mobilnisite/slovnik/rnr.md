---
slug: "rnr"
url: "/mobilnisite/slovnik/rnr/"
type: "slovnik"
title: "RNR – Receive Not Ready"
date: 2025-01-01
abbr: "RNR"
fullName: "Receive Not Ready"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rnr/"
summary: "Typ rámce používaný v protokolech vrstvy datového spoje, zejména v GSM/UMTS, k indikaci dočasné neschopnosti přijímat příchozí datové rámce. Jde o mechanismus řízení toku, který signalizuje zahlcení v"
---

RNR je typ rámce vrstvy datového spoje používaný v GSM/UMTS pro řízení toku dat. Signalizuje dočasnou neschopnost přijímat data z důvodu zahlcení vyrovnávací paměti, čímž vysílateli nařídí pozastavit přenos.

## Popis

Receive Not Ready (RNR) je typ dozorovacího rámce definovaný v protokolech vrstvy datového spoje, jako jsou ty specifikované v 3GPP pro sítě GSM a UMTS. Funguje jako součást protokolového zásobníku vrstvy 2 (Layer 2), často v rámci Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) nebo Link Access Protocol ([LAP](/mobilnisite/slovnik/lap/)), pro řízení toku dat mezi partnerskými entitami. Hlavní funkcí RNR rámce je signalizovat od přijímače k vysílači, že přijímač je dočasně neschopen přijímat nové datové rámce. Tento stav obvykle nastává kvůli vnitřnímu zahlcení vyrovnávací paměti, vysokému vytížení procesoru nebo jiným dočasným omezením, která brání přijímači zpracovat další data bez rizika přetečení nebo ztráty.

Když přijímač odešle RNR rámec, výslovně tím vysílateli nařídí zastavit přenos informačních rámců (I-rámců). Vysílač po přijetí RNR přejde do klidového stavu, ve kterém přestane posílat nové I-rámce, ale může pokračovat v odesílání dozorovacích rámců, jako je Receiver Ready ([RR](/mobilnisite/slovnik/rr/)), nebo jiných řídicích signálů pro udržení spojení. RNR rámec obsahuje nezbytné řídicí informace, jako je sekvenční číslo přijímače, pro identifikaci kontextu komunikace. Tento mechanismus je klíčový v poloduplexních nebo potvrzovacích protokolech, aby zabránil vysílateli přetížit přijímač, a tím se předešlo vyřazení rámců a retransmisím, které by snížily propustnost a zvýšily latenci.

Stav RNR je typicky zrušen, když přijímač odešle rámec Receiver Ready (RR), čímž signalizuje, že je připraven obnovit příjem dat. V některých implementacích může být se stavem RNR spojen časovač, aby se předešlo uváznutí; pokud přijímač neodešle RR v určeném časovém úseku, může vysílač zahájit procedury obnovy. RNR je nedílnou součástí procedur pro obnovu po chybě a řízení toku definovaných ve specifikacích jako 24.022 (rozhraní mobilní stanice – základnová stanice) a 44.064 (General Packet Radio Service; rozhraní mobilní stanice – Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node). Jeho úloha zajišťuje, že protokoly vrstvy datového spoje se mohou přizpůsobit dynamickým podmínkám sítě, čímž udržují spolehlivost a efektivitu bezdrátové komunikace.

## K čemu slouží

Typ rámce Receive Not Ready (RNR) byl zaveden, aby řešil potřebu robustního řízení toku v protokolech vrstvy datového spoje v rámci systémů 3GPP, zejména pro GSM a UMTS. Před jeho standardizací jednodušší protokoly postrádaly explicitní mechanismy pro zvládnutí zahlcení přijímače, což vedlo ke ztrátě dat, zbytečným retransmisím a snížené síťové efektivitě, když se přijímač dočasně stal neschopným zpracovávat příchozí rámce. RNR poskytuje standardizovaný způsob, jak může přijímač signalizovat svůj stav, což umožňuje proaktivní správu toku.

V bezdrátovém prostředí mohou faktory jako proměnlivé rádiové podmínky, zpoždění zpracování a omezení vyrovnávací paměti způsobit dočasnou nedostupnost přijímače. Bez RNR by vysílač mohl pokračovat v přenosu, což by způsobilo přetečení vyrovnávací paměti a vyřazení rámců, což by spustilo procedury retransmise a zvýšilo latenci. Tím, že RNR umožňuje přijímači explicitně indikovat svůj stav „not-ready“, pomáhá těmto problémům předcházet a optimalizuje tak propustnost a využití zdrojů. Je klíčovou součástí potvrzovacích protokolů, které zajišťují spolehlivé doručování dat přes nespolehlivá rádiová spojení.

Vznik RNR byl motivován vývojem směrem ke složitějším datovým službám v mobilních sítích, kde se efektivní řízení toku stalo kritickým pro podporu aplikací, jako je přepojování paketů. Řeší omezení dřívějších přístupů, které se spoléhaly pouze na řízení toku založené na okně nebo na implicitní signalizaci, které mohly být méně citlivé na náhlé zahlcení. RNR zvyšuje adaptabilitu vrstvy datového spoje a přispívá tak k celkové kvalitě služby v sítích 3GPP.

## Klíčové vlastnosti

- Explicitní signalizace řízení toku pro pozastavení přenosu dat
- Zabraňuje přetečení vyrovnávací paměti přijímače a ztrátě dat
- Integruje se s protokoly dozorovacích rámců, jako jsou LAP a RLC
- Obsahuje sekvenční číslo pro identifikaci kontextu
- Stav je zrušen odesláním rámce Receiver Ready (RR) pro obnovení komunikace
- Podporuje obnovu založenou na časovači, aby se předešlo uváznutí

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [RNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnr/)
