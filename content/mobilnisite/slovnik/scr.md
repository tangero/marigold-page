---
slug: "scr"
url: "/mobilnisite/slovnik/scr/"
type: "slovnik"
title: "SCR – Source Controlled Rate operation"
date: 2025-01-01
abbr: "SCR"
fullName: "Source Controlled Rate operation"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/scr/"
summary: "Režim provozu hlasového kodeku, známý také jako zdrojová nespojitá vysílání (DTX), při kterém kodér snižuje svou výstupní přenosovou rychlost během období nečinnosti řeči (ticho). Tím se šetří rádiové"
---

SCR je režim provozu hlasového kodeku, ve kterém kodér snižuje svou výstupní přenosovou rychlost během nečinnosti řeči, aby šetřil rádiové prostředky a energii baterie, a to přenosem pouze parametrů komfortního šumu.

## Popis

Provoz se zdrojově řízenou přenosovou rychlostí (SCR) je základní funkcí řečových kodeků používaných v mobilních komunikačních systémech, především v kodecích Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a AMR-Wideband. Jedná se o režim provozu kodeku, při kterém je rychlost kódování dynamicky řízena na základě přítomnosti nebo nepřítomnosti aktivní řeči ze zdroje (mluvčího). Během aktivních řečových segmentů kodek pracuje na plné, určené přenosové rychlosti, aby udržel vysokou kvalitu hlasu. Během období ticha nebo šumu na pozadí – která statisticky tvoří přes 50 % typického hovoru – však kodek přepne do režimu výrazně nižší přenosové rychlosti. V tomto režimu s nízkou rychlostí kodér nepřenáší plné řečové rámce, ale místo toho v pravidelných intervalech vysílá rámce popisovače ticha ([SID](/mobilnisite/slovnik/sid/)). Tyto SID rámce obsahují parametry, které umožňují dekodéru na přijímací straně generovat komfortní šum – umělý šum na pozadí napodobující akustické charakteristiky prostředí volajícího, čímž se posluchači zabrání nepřirozenému „hluchému tichu“.

Z architektonického hlediska SCR zahrnuje úzkou koordinaci mezi detektorem hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)) a řečovým kodekem v rámci mobilního terminálu nebo síťového transkodéru. VAD analyzuje vstupní zvukový signál a klasifikuje každý rámec jako obsahující aktivní řeč či nikoli. Tato klasifikace je předána kodeku, který poté vybere příslušný kódovací algoritmus a typ rámce. Systém také zahrnuje generátor komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) na přijímací straně, který využívá parametry v SID rámcích k syntéze šumu. Provoz je řízen pomocí signalizace v pásmu ve struktuře řečového rámce samotného, která označuje, zda je rámec řečový, SID rámec nebo značka konce období ticha.

Úloha SCR v síti je především otázkou efektivity. Díky drastickému snížení průměrné přenosové rychlosti hlasového hovoru se snižuje zatížení rádiového rozhraní. To přímo vede ke zvýšení systémové kapacity, protože na stejných rádiových prostředcích může být podporováno více uživatelů. Pro uživatele přináší významný benefit v podobě prodloužené výdrže baterie mobilního terminálu, protože vysílač může být během období ticha vypnut nebo pracovat na nižším výkonu. Jedná se o klíčovou součást mechanismů přizpůsobení provozu a úspory energie definovaných ve specifikacích 3GPP, což činí hlasové služby spektrálně efektivnějšími a uživatelsky přívětivějšími.

## K čemu slouží

SCR byl vyvinut, aby řešil inherentní neefektivitu přenosu audio signálu s konstantní přenosovou rychlostí během hlasové konverzace, kdy její významnou část tvoří ticho nebo šum s nízkou aktivitou. Rané digitální hlasové systémy přenášely nepřetržitý tok bitů bez ohledu na řečovou aktivitu, což plýtvalo cenným rádiovým spektrem a zbytečně vybíjelo baterie mobilních telefonů. Motivace pro SCR byla dvojí: zvýšit kapacitu celulárních sítí – což byl klíčový komerční faktor – a zlepšit dobu hovoru terminálů, což je zásadní prvek uživatelského zážitku.

Tato technologie řeší problém plýtvání prostředky během řečových pauz. Zavedením mechanismu nespojitého vysílání ([DTX](/mobilnisite/slovnik/dtx/)) řízeného samotným zdrojovým signálem umožňuje síti přerozdělit uvolněné rádiové prostředky (časové sloty, kódy nebo šířku pásma) jiným uživatelům. To bylo zvláště důležité pro GSM a jeho vývoj, kde bylo spektrum omezeným a drahým zbožím. SCR v kombinaci s adaptabilitou kodeku [AMR](/mobilnisite/slovnik/amr/) se stal základním kamenem pro poskytování vysoce kvalitní hlasové služby při optimalizaci využití celého systému. Představoval posun od zacházení s hlasem jako s proudem s konstantní přenosovou rychlostí k zacházení s ním jako se službou s proměnnou rychlostí, která se přizpůsobuje skutečnému informačnímu obsahu.

## Klíčové vlastnosti

- Dynamicky přepíná přenosovou rychlost kodeku na základě detekce hlasové aktivity (VAD)
- Přenáší rámce popisovače ticha (SID) s nízkou přenosovou rychlostí během ticha
- Umožňuje generování komfortního šumu na přijímači, aby se zabránilo hluchému tichu
- Významně snižuje průměrnou přenosovou rychlost a spotřebu rádiových prostředků
- Prodlužuje výdrž baterie mobilního terminálu tím, že umožňuje vypnutí vysílače
- Nedílná součást specifikací řečových kodeků AMR a AMR-WB

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure
- **TS 26.092** (Rel-19) — AMR Comfort Noise for SCR Operation
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.101** (Rel-19) — Generic frame format for AMR and GSM-EFR speech codecs
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 26.201** (Rel-19) — AMR-WB Speech Codec Frame Format
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [SCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/scr/)
