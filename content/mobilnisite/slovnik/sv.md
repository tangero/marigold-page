---
slug: "sv"
url: "/mobilnisite/slovnik/sv/"
type: "slovnik"
title: "SV – ID Space Vehicle Identification"
date: 2026-01-01
abbr: "SV"
fullName: "ID Space Vehicle Identification"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/sv/"
summary: "SV (ID Space Vehicle Identification) je jedinečný identifikátor pro satelity v satelitních polohovacích systémech jako GPS, GLONASS, Galileo a BeiDou, integrovaný do standardů 3GPP. Používá jej uživat"
---

SV je jedinečný identifikátor pro satelity v systémech jako GPS nebo Galileo, používaný mobilními zařízeními k měření a hlášení signálů od konkrétních satelitů pro síťové lokalizační služby.

## Popis

SV, neboli Space Vehicle Identification, je číselný identifikátor přiřazený každému satelitu v rámci konstelace globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)). Ve specifikacích 3GPP se tento identifikátor používá v polohovacích protokolech a měřicích hlášeních k jednoznačnému odkazování na konkrétní satelit. UE při provádění lokalizačních měření používá ID SV ke korelaci pozorovaných satelitních signálů s asistenčními daty poskytnutými sítí nebo k hlášení měření pro konkrétní satelity zpět do sítě. Specifikace, jako je TS 36.355 (LTE Positioning Protocol) a TS 37.571 (UE konformita pro určování polohy), podrobně popisují, jak jsou ID SV formátována a používána v zprávách mezi UE a lokalizačním serverem (např. [E-SMLC](/mobilnisite/slovnik/e-smlc/) nebo [LMF](/mobilnisite/slovnik/lmf/)).

Architektura zahrnuje GNSS přijímač UE, obsluhující mobilní síť a samotné GNSS konstelace. Lokalizační server sítě může poskytnout UE asistenční data, která zahrnují almanach a efemeridy klíčované podle ID SV, aby pomohla UE rychleji zachytit satelity ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Když UE provádí měření – jako je fáze kódu, Dopplerův posun nebo fáze nosné – hlásí tato měření ve struktuře, která obsahuje odpovídající ID SV pro každý měřený satelit. Různé GNSS konstelace mají různá schémata číslování ID SV. Například ID SV pro [GPS](/mobilnisite/slovnik/gps/) jsou v rozsahu 1 až 32, zatímco Galileo používá jiný rozsah. Specifikace 3GPP definují mapování a informační prvky pro zpracování těchto různých systémů.

Fungování je nedílnou součástí polohovacích procedur. Například v zprávě [LPP](/mobilnisite/slovnik/lpp/) (LTE Positioning Protocol) Provide Assistance Data může server odeslat efemeridová data pro satelity s ID 5, 12 a 19 (GPS). UE se poté pokusí zachytit signály od těchto konkrétních satelitů. V následné zprávě LPP Provide Location Information UE hlásí naměřené pseudovzdálenosti pro satelity, které detekovala, opět s použitím jejich ID SV. Polohovací algoritmus na straně sítě používá tato označená měření k výpočtu polohy UE. ID SV je tedy klíčovým metadatovým prvkem, který spojuje surová měření signálu s orbitální dynamikou konkrétního satelitu, což umožňuje přesné geometrické výpočty pro určení polohy.

## K čemu slouží

Systém identifikace SV existuje, aby umožnil standardizované a efektivní satelitní určování polohy v rámci sítí 3GPP. Jeho primárním účelem je řešit problém jednoznačné komunikace mezi UE a sítí ohledně toho, které satelity jsou používány pro výpočty polohy. Bez společného identifikátoru by síť nemohla poskytovat cílená asistenční data ani správně interpretovat měřicí hlášení od UE, čímž by se Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) stalo neúčinným.

Historicky, když mobilní sítě začaly integrovat služby založené na poloze (LBS) ve 3GPP Release 99 a později, vznikla potřeba podpořit nové spotřebitelské a regulační požadavky, jako je E-911. Rané metody jako Cell-ID nebyly dostatečně přesné. Integrace GNSS schopností vyžadovala způsob, jak propojit svět satelitní navigace (s vlastními identifikačními schématy) se světem protokolů buněčné signalizace. Zavedení ID SV do specifikací 3GPP tento most poskytlo, což umožnilo mobilním sítím využívat vysokou přesnost GNSS.

Motivace byla hnána poptávkou po přesných lokalizačních službách pro tísňová volání, navigaci, sledování majetku a aplikace založené na poloze. Standardizací použití ID SV napříč všemi implementacemi UE a síťových dodavatelů zajistila 3GPP interoperabilitu. Umožnila jakémukoli kompatibilnímu UE pracovat s lokalizačním serverem jakékoli kompatibilní sítě, bez ohledu na podkladový GNSS čipset nebo preference konstelace. To bylo klíčové pro globální zavedení spolehlivého, síťově asistovaného určování polohy, které ve srovnání s autonomním provozem GNSS snižuje spotřebu energie UE a čas do prvního určení polohy.

## Klíčové vlastnosti

- Jedinečný číselný identifikátor pro jednotlivé GNSS satelity
- Používán napříč více GNSS konstelacemi (GPS, GLONASS, Galileo, BeiDou)
- Nedílná součást 3GPP polohovacích protokolů, jako je LPP a hlášení měření RRC
- Umožňuje cílené doručování GNSS asistenčních dat (efemeridy, almanach)
- Umožňuje přesné hlášení měření specifických pro satelit (pseudovzdálenost, Dopplerův posun)
- Základní pro provoz Assisted-GNSS (A-GNSS) v UE

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [SV na 3GPP Explorer](https://3gpp-explorer.com/glossary/sv/)
