---
slug: "xram"
url: "/mobilnisite/slovnik/xram/"
type: "slovnik"
title: "XRAM – Extended RAM"
date: 2025-01-01
abbr: "XRAM"
fullName: "Extended RAM"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/xram/"
summary: "Testovací metodologie definovaná 3GPP pro hodnocení výkonu paměti rádiového přístupu v uživatelských zařízeních a základnových stanicích. Rozšiřuje tradiční testování RAM o pokročilé scénáře, jako je"
---

XRAM je testovací metodologie 3GPP pro hodnocení výkonu paměti rádiového přístupu v uživatelských zařízeních a základnových stanicích, která rozšiřuje tradiční testy o pokročilé scénáře, jako je agregace nosných a masivní MIMO.

## Popis

Extended [RAM](/mobilnisite/slovnik/ram/) (XRAM) je rámec pro testování shody specifikovaný v 3GPP TS 35.909, navržený k posouzení výkonu paměťového subsystému komponent rádiové přístupové sítě, zejména uživatelských zařízení (UE) a vysílačů [eNB](/mobilnisite/slovnik/enb/) nebo gNB. Zaměřuje se na operační paměť (RAM) používanou v těchto zařízeních a přesahuje rámec základních funkčních testů k vyhodnocení chování ve stresových, reálných podmínkách. Metodologie simuluje vysoké provozní zatížení, složité konfigurace a dlouhodobý provoz za účelem identifikace potenciálních problémů, jako jsou úniky paměti, fragmentace nebo přetečení, které by mohly degradovat výkon sítě.

Z architektonického hlediska zahrnuje testování XRAM specializované testovací zařízení, které emuluje síťové scénáře a zároveň monitoruje využití paměti zařízení. Mezi klíčové komponenty patří generátory provozu pro vytváření datových toků, simulátory protokolů pro napodobení síťové signalizace a profiler paměti pro sledování alokací a dealokací. Testy se provádějí v řízených laboratorních prostředích, často jako součást testovací sady pro shodu rádiové přístupové sítě (RAN) 3GPP. Pokrývají různé vrstvy, od zpracování fyzické vrstvy po protokoly vyšších vrstev, a zajišťují robustní správu paměti v celém zásobníku.

V praxi testy XRAM vystavují zařízení dlouhodobému provozu s konfiguracemi, jako je agregace nosných, vícevrstvé [MIMO](/mobilnisite/slovnik/mimo/) a předávání spojení mezi buňkami. Například uživatelskému zařízení může být uložen úkol nepřetržitě přijímat a vysílat data přes agregované nosné při provádění mobilních procedur, přičemž testery měří spotřebu paměti v čase. Cílem je ověřit, že využití paměti zůstává stabilní bez neomezeného růstu, který by mohl vést k pádům systému nebo snížení propustnosti. Specifikace definují kritéria úspěšnosti/neúspěšnosti na základě metrik, jako jsou špičky využití paměti a zotavení po stresových událostech.

Role XRAM je klíčová pro zajištění spolehlivosti zařízení v nasazených sítích, zejména s nástupem složitějších funkcí v 4G a 5G. Identifikací problémů souvisejících s pamětí v rané fázi pomáhá výrobcům zlepšit návrh softwaru a hardwaru a snížit výpadky v provozu. Metodologie se vyvíjí s každou verzí 3GPP, aby reagovala na nové technologie, jako jsou širší šířky pásma 5G NR a síťové řezy, a zajistila, že testování paměti drží krok s pokrokem sítí. To přispívá k celkové stabilitě systému a uživatelskému zážitku.

## K čemu slouží

XRAM byl vytvořen, aby řešil rostoucí složitost využití paměti v zařízeních rádiového přístupu, která se stala výraznější s příchodem LTE-Advanced a 5G. Dřívější testování se zaměřovalo na základní funkčnost, ale s nárůstem požadavků na zpracování u funkcí, jako je agregace nosných a masivní [MIMO](/mobilnisite/slovnik/mimo/), se problémy související s pamětí – například úniky z dlouhodobých relací – staly otázkou spolehlivosti. Tyto problémy mohly způsobit restartování zařízení nebo ztrátu spojení, což ovlivnilo výkon sítě a spokojenost uživatelů.

Jeho vývoj byl motivován potřebou standardizované, důkladné testovací metodologie, která jde nad rámec tradičních kontrol [RAM](/mobilnisite/slovnik/ram/). Předchozí přístupy byly často ad-hoc nebo omezené na krátkodobé testy, které přehlížely jemné problémy s pamětí projevující se v čase. XRAM poskytuje komplexní rámec pro simulaci reálného stresu a zajišťuje, že zařízení zvládnou pokročilé konfigurace bez degradace. To je obzvláště důležité pro operátory nasazující husté sítě, kde zařízení musí nepřetržitě pracovat pod vysokým zatížením.

Historicky byl XRAM představen v 3GPP Release 8 spolu s LTE, což odráželo přechod na plně IP sítě a softwarem definované rádio. S postupem verzí se vyvíjel, aby pokryl nové scénáře, jako jsou HetNety a 5G NR, a řešil paměťové výzvy zvýšené propustnosti a nižší latence. Standardizací těchto testů umožňuje 3GPP konzistentní certifikaci napříč dodavateli, podporuje interoperabilitu a spolehlivost v nasazeních s více dodavateli. To pomáhá zmírnit rizika spojená se složitou správou paměti v moderních bezdrátových systémech.

## Klíčové vlastnosti

- Hodnotí výkon paměti při dlouhodobém vysokém zatížení
- Simuluje reálné scénáře, jako je agregace nosných a předávání spojení
- Detekuje problémy s úniky paměti, fragmentací a přetečením
- Integruje se s testováním shody 3GPP pro uživatelská zařízení a základnové stanice
- Podporuje testování napříč více protokolovými vrstvami
- Přizpůsobuje se novým technologiím v každé verzi 3GPP

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [eNB – Evolved Node B](/mobilnisite/slovnik/enb/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [XRAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/xram/)
