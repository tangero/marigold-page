---
slug: "uau"
url: "/mobilnisite/slovnik/uau/"
type: "slovnik"
title: "UAU – Unnumbered Acknowledgement"
date: 2025-01-01
abbr: "UAU"
fullName: "Unnumbered Acknowledgement"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/uau/"
summary: "Řídicí rámec používaný v protokolech vrstvy spojení dat (jako např. v 3GPP TS 27.010) k potvrzení přijetí rámců bez použití sekvenčních čísel. Poskytuje jednoduchý a efektivní mechanismus potvrzování"
---

UAU (Unnumbered Acknowledgement, nečíslované potvrzení) je řídicí rámec používaný v protokolech vrstvy spojení dat k zajištění jednoduchého a efektivního mechanismu potvrzování pro spolehlivý přenos dat bez použití sekvenčních čísel.

## Popis

Unnumbered Acknowledgement (UAU, nečíslované potvrzení) je specifický typ řídicího rámce definovaný v protokolech vrstvy spojení dat, jako je například protokol specifikovaný v 3GPP TS 27.010 pro sériovou datovou komunikaci. Funguje jako součást rámcové struktury protokolu, která typicky zahrnuje informační rámce (I-rámce) přenášející uživatelská data a dozorovací rámce (S-rámce), jako je UAU, pro řídicí účely. Příjemce odesílá UAU rámec za účelem kladného potvrzení správného přijetí jednoho nebo více dříve přenesených I-rámců, ale na rozdíl od standardního dozorovacího rámce Receive Ready ([RR](/mobilnisite/slovnik/rr/)) neobsahuje sekvenční číslo (N(R)).

Při provozu UAU poskytuje jednoduchý mechanismus potvrzování. Když příjemce odešle UAU, signalizuje, že všechny rámce až do určitého bodu byly přijaty správně, čímž často implicitně potvrzuje poslední přijatý rámec. To je zvláště užitečné ve scénářích, kde protokol používá spojovaný, spolehlivý přenosový režim, ale může využívat zjednodušené schéma potvrzování pro vyšší efektivitu. Odeslání UAU rámce resetuje na straně odesílatele jakýkoli časovač související s čekáním na potvrzení.

Jeho role v síti dle TS 27.010 spočívá v kontextu okruhově přepínaných datových služeb a adaptace terminálu, kde zajišťuje spolehlivý přenos dat přes sériové rozhraní (např. mezi terminálovým zařízením ([TE](/mobilnisite/slovnik/te/)) a mobilní ukončovací jednotkou ([MT](/mobilnisite/slovnik/mt/))). UAU spolupracuje s dalšími typy rámců, jako jsou Unnumbered Information ([UI](/mobilnisite/slovnik/ui/)) a Set Asynchronous Balanced Mode ([SABM](/mobilnisite/slovnik/sabm/)), při navazování, udržování a ukončování datových spojení, čímž poskytuje řízení toku a obnovu po chybách na vrstvě spojení dat pro pomocné služby.

## K čemu slouží

Mechanismus UAU existuje, aby poskytoval odlehčenou a efektivní metodu pro kladné potvrzování v protokolech vrstvy spojení dat, zejména v prostředích, kde je minimalizace režie výhodná. Řeší potřebu spolehlivého přenosu dat bez neustálého používání potvrzení se sekvenčními čísly, které mohou zvyšovat režii záhlaví. V kontextu 3GPP TS 27.010, která definuje sériový datový protokol pro použití s mobilními stanicemi, je taková efektivita cenná pro pomocné datové služby.

Historicky, jak se mobilní systémy vyvíjely k podpoře datových služeb nad rámec hlasu, byly protokoly jako ten v TS 27.010 adaptovány zavedenými standardy (např. založenými na principech [HDLC](/mobilnisite/slovnik/hdlc/)) pro správu komunikace přes sériové linky. UAU nabízí alternativu k číslovaným potvrzením (jako je [RR](/mobilnisite/slovnik/rr/) s N(R)), čímž zjednodušuje logiku příjemce v určitých provozních režimech nebo stavech. Řeší problém poskytování potvrzení spolehlivého doručení při zachování adaptability protokolu pro různé požadavky služeb, podporuje jak potvrzované, tak nepotvrzované provozní režimy definované ve specifikaci.

## Klíčové vlastnosti

- Typ řídicího rámce pro kladné potvrzení bez sekvenčního čísla
- Používán v protokolech vrstvy spojení dat dle 3GPP TS 27.010
- Signalizuje úspěšné přijetí informačních rámců
- Pomáhá v procedurách řízení toku a obnovy po chybách
- Lze použít v určitých režimech protokolu ke zjednodušení potvrzování
- Spolupracuje s dalšími nečíslovanými a dozorovacími rámci

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)
- [SABM – Set Asynchronous Balanced Mode frame](/mobilnisite/slovnik/sabm/)

## Definující specifikace

- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface

---

📖 **Anglický originál a plná specifikace:** [UAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/uau/)
