---
slug: "sid"
url: "/mobilnisite/slovnik/sid/"
type: "slovnik"
title: "SID – Silence Insertion Descriptor"
date: 2025-01-01
abbr: "SID"
fullName: "Silence Insertion Descriptor"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sid/"
summary: "Typ rámce používaný v adaptivních vícerychlostních kodecích (AMR) a adaptivním vícerychlostním širokopásmovém kodeku (AMR-WB) pro efektivní reprezentaci období ticha během hlasových hovorů. Nahrazuje"
---

SID je typ rámce používaný v kodecích AMR a AMR-WB, který efektivně reprezentuje ticho v hlasových hovorech nahrazením řeči kompaktními deskriptory za účelem snížení šířky pásma.

## Popis

Deskriptor pro vkládání ticha (SID) je základní součástí řečových kodeků Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a AMR-Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) standardizovaných 3GPP. Během hlasového hovoru obsahuje lidská řeč přirozené pauzy a období ticha, která mohou tvořit až 60 % konverzace. Přenášení těchto tichých segmentů jako běžných řečových rámců by bylo vysoce neefektivní. Místo toho kodek na vysílací straně využívá algoritmus detekce hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)) k identifikaci těchto intervalů bez řeči. Po detekci ticha kodér přestane generovat konvenční řečové rámce a vytvoří speciální SID rámec. Tento SID rámec je kompaktní datová struktura obsahující klíčové parametry pro charakterizaci šumu na pozadí, jako jsou informace o spektrální obálce a úrovních energie, což umožňuje přijímači generovat útulný šum (CN), který odpovídá akustickému prostředí volajícího.

Architektura pro generování a zpracování SID rámců je integrována do provozních režimů řečového kodeku. Kodér po přechodu z aktivní řeči na ticho spuštěném VAD přenese počáteční SID rámec (často nazývaný 'první SID'), aby stanovil parametry šumu. Následně během prodlouženého období ticha může kodér vysílat periodické aktualizační SID rámce s mnohem nižší rychlostí (např. každých 160 ms nebo 320 ms) ve srovnání s běžnou rychlostí řečových rámců 20 ms, aby sledoval případné změny šumu na pozadí. Tento mechanismus nespojitého přenosu ([DTX](/mobilnisite/slovnik/dtx/)), při kterém jsou SID rámce vysílány sporadicky, je jádrem úspor šířky pásma. Dekodér přijímače využívá informace v přijatých SID rámcích k syntéze útulného šumu pomocí funkce generování šumu, čímž zabraňuje nepřirozenému 'hluchému tichu', které by jinak posluchač vnímal, a zachovává přirozený zážitek z hovoru.

Technická implementace SID rámců zahrnuje specifické bitové vzory a typy rámců definované v kodekových specifikacích. Pro AMR existují různé typy SID rámců odpovídající různým režimům kodeku. SID rámec je mnohem menší než plný řečový rámec; například řečový rámec režimu AMR 12,2 kbps má 244 bitů, zatímco SID rámec může mít pouhých 35 bitů. Toto drastické snížení velikosti přenášených dat je tím, co šetří rádiové prostředky a životnost baterie. Mechanismus SID funguje v součinnosti s transportními protokoly rádiové přístupové sítě, které musí tyto speciální rámce správně identifikovat a zpracovat, aby se zajistilo, že nebudou zaměněny za poškozená data. Role SID je tedy klíčová v celém řetězci hlasové služby, neboť umožňuje efektivní využití kanálu při zachování vysoce kvalitního a přirozeně znějícího uživatelského zážitku, což je klíčový požadavek pro mobilní telefonii.

## K čemu slouží

Primárním účelem deskriptoru pro vkládání ticha (SID) je umožnit efektivní využití šířky pásma během hlasových hovorů odstraněním plýtvavého přenosu ticha. V raných digitálních hlasových systémech by i během pauz v řeči zůstal kanál obsazen daty reprezentujícími šum na pozadí nebo pouhé digitální ticho, což spotřebovávalo cenné rádiové spektrum a kapacitu sítě. To bylo obzvláště problematické pro mobilní sítě, kde je spektrum vzácným a drahým zdrojem. Mechanismus SID jako součást funkce [DTX](/mobilnisite/slovnik/dtx/) byl vytvořen k vyřešení tohoto problému, přímo zvyšuje počet současných hovorů, které buňka zvládne, a snižuje rušení v systému.

Historicky, před sofistikovanými kodeky jako je [AMR](/mobilnisite/slovnik/amr/), některé systémy používaly jednoduchý zapínací/vypínací DTX, což mohlo vést k nepříjemnému přepínacímu efektu, kdy šum na pozadí náhle mizel a znovu se objevoval, což vytvářelo 'trhaný' sluchový zážitek. Inovací SID bylo poskytnutí deskriptoru, který umožňuje přijímací straně rekonstruovat věrohodnou aproximaci šumu na pozadí odesílatele. Tím se řeší klíčové omezení předchozích přístupů DTX: potřeba zachovat akustickou kontinuitu a přirozenost hovoru. Odesíláním kompaktního matematického popisu šumu namísto samotného šumu systém dosahuje dvojího cíle efektivity a kvality.

Motivace pro jeho vytvoření v rámci 3GPP byla nedílnou součástí vývoje kodeku AMR pro GSM a později UMTS. Jak se sítě vyvíjely, aby podporovaly více uživatelů a datové služby, optimalizace každého aspektu hlasového provozu se stala prvořadou. SID je klasickým příkladem percepční optimalizace – využívá charakteristik lidského sluchu a konverzačních vzorců k návrhu efektivnějšího technického systému, aniž by uživatel vnímal jakýkoli negativní dopad, čímž se zvyšuje celkový výkon sítě a její ekonomická životaschopnost.

## Klíčové vlastnosti

- Umožňuje nespojitý přenos (DTX) nahrazením ticha kompaktními rámci
- Nese parametry pro charakterizaci šumu na pozadí (spektrální obálka, energie)
- Spouští generování útulného šumu (CN) na přijímači pro zachování přirozenosti hovoru
- Významně snižuje velikost přenášených dat ve srovnání s aktivními řečovými rámci (např. ~35 bitů vs. 244 bitů)
- Funguje s detekcí hlasové aktivity (VAD) pro automatickou klasifikaci ticha/řeči
- Podporuje periodickou aktualizaci během dlouhého ticha pro sledování změn šumu

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure
- **TS 26.092** (Rel-19) — AMR Comfort Noise for SCR Operation
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.101** (Rel-19) — Generic frame format for AMR and GSM-EFR speech codecs
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 26.201** (Rel-19) — AMR-WB Speech Codec Frame Format
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 26.250** (Rel-19) — IVAS Codec Introduction
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [SID na 3GPP Explorer](https://3gpp-explorer.com/glossary/sid/)
