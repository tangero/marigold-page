---
slug: "mos"
url: "/mobilnisite/slovnik/mos/"
type: "slovnik"
title: "MOS – Mean Opinion Score"
date: 2025-01-01
abbr: "MOS"
fullName: "Mean Opinion Score"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mos/"
summary: "Standardizované subjektivní měřítko vnímané lidské kvality hlasových, zvukových nebo video služeb. Je odvozeno z průměru názorů mnoha lidských posluchačů nebo diváků, kteří kvalitu hodnotí na škále od"
---

MOS je standardizované subjektivní měřítko vnímané lidské kvality hlasových, zvukových nebo video služeb, získané jako průměr uživatelských hodnocení na škále od 1 do 5 za účelem kvantifikace kvality uživatelského prožitku (QoE).

## Popis

Mean Opinion Score (MOS) je základní kvantitativní měřítko vnímané kvality přenášeného hlasového, zvukového nebo video signálu, jak ji prožívá koncový uživatel. Je definováno v doporučeních [ITU-T](/mobilnisite/slovnik/itu-t/) řady P a je rozsáhle přijato a rozpracováno ve specifikacích 3GPP pro srovnávání kvality služeb. Základní metodologie spočívá v subjektivním poslechovém nebo vizuálním testu, kdy panel lidských subjektů hodnotí kvalitu zpracovaných audio/video vzorků za kontrolovaných podmínek. Každý subjekt udělí známku na absolutní kategorizační škále, typicky: 5=vynikající, 4=dobrá, 3=uspokojivá, 2=špatná, 1=nevyhovující. MOS je aritmetický průměr všech získaných známek pro danou testovací podmínku, což vede k jedinému číslu mezi 1,0 a 5,0.

Proces získání MOS je vysoce standardizovaný, aby byla zajištěna reprodukovatelnost a srovnatelnost. Testované osoby jsou vybírány na základě specifických kritérií (např. normální sluch) a poslouchají nebo sledují sekvence zpracovaných médií v tiché místnosti za použití standardizovaného vybavení. Testovací materiál zahrnuje čisté zdrojové vzorky a vzorky degradované kodekem, ztrátou paketů, zpožděním, chvěním (jitter) nebo jinými poruchami sítě. Subjekty nejsou odborníci, ale reprezentují typické uživatele. Přísná kontrola environmentálních, hardwarových a procedurálních proměnných je klíčová pro izolaci vlivu testovaného systému na vnímanou kvalitu. Výsledné MOS poskytuje přímý, na člověka zaměřený spojovací článek mezi technickými síťovými parametry a spokojeností uživatele.

V rámci architektury 3GPP není MOS přímo měřitelným klíčovým výkonnostním ukazatelem ([KPI](/mobilnisite/slovnik/kpi/)) sítě, ale je konečným etalonem, vůči kterému se kalibrují objektivní prediktivní modely. Specifikace 3GPP definují výkonnostní požadavky na kodeky, síťové zpoždění, odolnost vůči ztrátě paketů a další faktory s cílem dosáhnout cílového MOS za specifických podmínek. Například specifikace může vyžadovat, aby hlasový kodek dosáhl MOS 4,0 nebo vyššího při definovaném scénáři ztráty paketů. Plánování sítě, výběr kodeku a ladění parametrů QoS jsou nakonec zaměřeny na maximalizaci MOS pro koncového uživatele. Překlenuje propast mezi technickými metrikami (např. latence, chvění) a subjektivním lidským prožitkem, což jej činí nepostradatelným pro správu kvality služeb a standardizaci.

## K čemu slouží

MOS byl vytvořen k řešení základního problému kvantifikace něčeho inherentně subjektivního: kvality komunikačního prožitku. Před jeho standardizací bylo srovnávání hlasových kodeků nebo výkonnosti sítě obtížné a často založené na nekonzistentních proprietárních poslechových testech. Inženýři potřebovali spolehlivou, opakovatelnou metodu k vyhodnocení, jak technické vady (jako omezení šířky pásma, komprese nebo ztráta paketů) skutečně ovlivňují vnímání uživatele. MOS poskytl tuto společnou měnu kvality.

Jeho přijetí organizacemi 3GPP a dalšími standardizačními orgány bylo motivováno potřebou definovat minimální výkonnostní požadavky pro digitální buněčné systémy (GSM, 3G, 4G, 5G). Jak se sítě vyvíjely z analogových na digitální a zaváděly ztrátové kompresní kodeky pro úsporu šířky pásma, stalo se kritickým zajistit, aby tyto technologické pokroky nesnížily kvalitu hlasu pod přijatelnou mez. MOS poskytl definitivní škálu pro stanovení těchto mezí (např. 'toll quality' je často spojována s MOS ~4,0). Umožňuje objektivní srovnání zcela odlišných technologických přístupů (např. kodek [AMR-NB](/mobilnisite/slovnik/amr-nb/) vs. [EVS](/mobilnisite/slovnik/evs/)) na základě jejich konečného dopadu na lidského posluchače, což pohání neustálé zlepšování kvality řeči a zvuku pro mobilní služby.

## Klíčové vlastnosti

- Subjektivní měření kvality založené na lidském vnímání
- Používá standardizovanou 5bodovou absolutní kategorizační škálu (ACR)
- Odvozeno ze statisticky významných panelů posluchačů/diváků za kontrolovaných laboratorních podmínek
- Slouží jako referenční etalon pro kalibraci objektivních prediktivních modelů kvality (např. PESQ, POLQA)
- Definuje cíle kvality pro výkon kodeků a sítě ve specifikacích 3GPP
- Aplikovatelné na řeč, zvuk, video a audiovizuální multimediální služby

## Související pojmy

- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [PESQ – Perceptual Evaluation of Speech Quality](/mobilnisite/slovnik/pesq/)
- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.925** (Rel-4) — UMTS QoS and Network Performance Parameters
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.909** (Rel-19) — QoE Enhancement for Streaming Services
- **TR 26.921** (Rel-19) — UE Performance in Ambient Noise
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [MOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mos/)
