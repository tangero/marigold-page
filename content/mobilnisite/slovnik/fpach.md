---
slug: "fpach"
url: "/mobilnisite/slovnik/fpach/"
type: "slovnik"
title: "FPACH – Fast Physical Access Channel"
date: 2025-01-01
abbr: "FPACH"
fullName: "Fast Physical Access Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fpach/"
summary: "TDD-specifický (pouze pro duplex s dělením času) uplinkový kanál v UTRA (3G) používaný pro přenos rychlých přístupových preambulí a časové zarovnání. Umožňuje rychlé procedury náhodného přístupu a sni"
---

FPACH je TDD-specifický (pouze pro duplex s dělením času) uplinkový kanál v UTRA (3G) používaný pro přenos rychlých přístupových preambulí a časové zarovnání, který umožňuje rychlé procedury náhodného přístupu v režimu Time Division Duplex.

## Popis

Fast Physical Access Channel (FPACH) je kanál fyzické vrstvy definovaný v 3GPP UTRA (UMTS Terrestrial Radio Access) v režimu TDD (Time Division Duplex), specifikovaný v TS 25.433 (rozhraní UTRAN Iub) a TS 37.320 (sběr rádiových měření). Funguje výhradně v TDD variantě UMTS (3G) a nepoužívá se v režimu [FDD](/mobilnisite/slovnik/fdd/) (Frequency Division Duplex). FPACH je uplinkový kanál využívaný během procedury náhodného přístupu k usnadnění rychlé synchronizace a udělení přístupu pro uživatelské zařízení (UE), které se pokouší navázat spojení se sítí.

Z architektonického hlediska je FPACH vysílán Node B (základnovou stanicí) jako odpověď na přístupové preambule odeslané UE na Physical Random Access Channel (PRACH). Když chce UE zahájit komunikaci, odešle náhodně vybranou preambuli. Node B tuto preambuli detekuje a odpoví informací o časovém přizpůsobení a udělením přístupu na FPACH. To umožňuje UE rychle zarovnat časování svého přenosu se sítí, což je v TDD systémech klíčové, protože přesné časování je nezbytné k zabránění interference mezi uplinkovými a downlinkovými časovými sloty.

Kanál funguje jako mechanismus zpětné vazby s nízkou latencí. Po přijetí platné preambule Node B vypočítá potřebný timing advance na základě změřeného zpoždění šíření a tuto informaci spolu s detaily alokace prostředků odešle prostřednictvím FPACH. UE následně podle toho upraví časování svého vysílání a pokračuje odesláním vlastní zprávy náhodného přístupu na přidělených prostředcích. Tento dvoukrokový proces (preambule + odpověď přes FPACH) snižuje pravděpodobnost kolizí a urychluje přístup ve srovnání s konkurenčními metodami bez zpětné vazby.

Mezi klíčové součásti zapojené do procesu patří jednotka fyzické vrstvy UE, přijímač a plánovač Node B a algoritmy správy rádiových prostředků, které spravují alokace FPACH. FPACH hraje zásadní roli v optimalizaci výkonu TDD systémů minimalizací přístupových zpoždění a zlepšením přesnosti synchronizace uplinku. Je obzvláště důležitý ve scénářích s vysokou hustotou uživatelů nebo mobilitou, kde dochází k častým pokusům o přístup. Jeho návrh odráží jedinečné požadavky provozu TDD, kde jsou časové vztahy mezi uplinkem a downlinkem přísně řízeny.

## K čemu slouží

FPACH byl vytvořen k řešení specifických výzev náhodného přístupu v režimu UTRA TDD, kde je přesné časové zarovnání kritičtější než v [FDD](/mobilnisite/slovnik/fdd/) kvůli časově sdílenému uplinkovému/downlinkovému přenosu. V raných návrzích TDD systémů bez rychlé zpětné vazby trpěly procedury náhodného přístupu vysokou latencí a mírou kolizí, zejména v buňkách s velkým zpožděním šíření nebo mnoha simultánními uživateli. FPACH poskytl mechanismus pro okamžitou časovou korekci, což umožnilo rychlejší a spolehlivější navázání spojení.

Historicky, když 3GPP vyvíjelo UMTS TDD jako alternativu k FDD, potřebovalo optimalizované procedury k využití výhod TDD, jako je flexibilní využití spektra. Proces náhodného přístupu ve FDD spoléhal na jiné mechanismy, které byly méně citlivé na časové chyby. FPACH byl zaveden, aby přizpůsobil přístupovou proceduru charakteristikám TDD a vyřešil problémy jako časová nezarovnanost, která mohla způsobit interference mezi následnými časovými sloty. Umožnil UE rychle synchronizovat své přenosy, což snížilo potřebu prodloužených sekvencí preambulí a zlepšilo celkovou kapacitu systému.

Motivace pro FPACH vycházela z touhy dosáhnout přístupu s nízkou latencí srovnatelného s FDD, navzdory inherentním časovým omezením TDD. Řešil omezení jednodušších přístupových metod, které vyžadovaly více opakování preambulí nebo složité řešení kolizí. Poskytnutím přímé zpětné vazby z Node B FPACH minimalizoval čas mezi pokusem o přístup a jeho udělením, čímž zlepšil uživatelský zážitek u služeb jako hovory nebo instant messaging. Také zlepšil efektivitu sítě snížením signalizační režie a plýtvání prostředky z neúspěšných pokusů o přístup.

## Klíčové vlastnosti

- TDD-specifický (pouze pro duplex s dělením času) uplinkový kanál pro odpověď na náhodný přístup
- Nese informaci o timing advance pro synchronizaci UE
- Přenáší udělení přístupu a alokace prostředků
- Snižuje latenci náhodného přístupu a pravděpodobnost kolizí
- Funguje ve spojení s PRACH (Physical Random Access Channel)
- Umožňuje rychlé časové zarovnání uplinku v režimu TDD

## Definující specifikace

- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [FPACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/fpach/)
