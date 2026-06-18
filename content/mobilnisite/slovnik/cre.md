---
slug: "cre"
url: "/mobilnisite/slovnik/cre/"
type: "slovnik"
title: "CRE – Call Re-establishment"
date: 2025-01-01
abbr: "CRE"
fullName: "Call Re-establishment"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cre/"
summary: "Procedura řízení rádiových prostředků (RRC), která umožňuje uživatelskému zařízení (UE) rychle obnovit přerušené rádiové spojení a navázat na probíhající hovor nebo datovou relaci. Je spuštěna při sel"
---

CRE (Call Re-establishment) je procedura řízení rádiových prostředků (RRC), která umožňuje uživatelskému zařízení (UE) rychle obnovit přerušené rádiové spojení a pokračovat v probíhajícím hovoru nebo relaci po selhání rádiového spoje.

## Popis

Call Re-establishment (CRE) je klíčová procedura řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) definovaná ve specifikacích 3GPP, primárně pro LTE a dále rozvinutá v 5G NR, navržená k zotavení z selhání rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)). Proceduru zahájí uživatelské zařízení (UE) ve chvíli, kdy detekuje selhání rádiového spoje s obsluhující buňkou, ale předpokládá, že kontext spojení na straně sítě (konkrétně na eNodeB v LTE nebo gNB v NR) může být stále platný. Tato detekce je založena na měřeních fyzické vrstvy, například když kvalita rádiového signálu na downlinku klesne pod stanovený práh, což vede k indikacím 'out-of-sync'. Po detekci RLF spustí UE časovač (T311 v LTE) a pokusí se vybrat vhodnou buňku pro opětovné zřízení spojení. Tou může být původní buňka nebo jiná buňka, pokud patří stejnému eNodeB nebo je připravena jako sousední. UE poté vyšle do vybrané buňky zprávu RRC Connection Re-establishment Request, která obsahuje identitu UE ([C-RNTI](/mobilnisite/slovnik/c-rnti/)) a krátký kód integrity (shortMAC-I) pro bezpečnostní ověření.

Přijímající eNodeB zkontroluje, zda uchovává kontext UE. Pokud je kontext k dispozici a bezpečnostní kontrola projde, eNodeB odpoví zprávou RRC Connection Re-establishment, která znovu aktivuje zabezpečení a překonfiguruje rádiové přenosové kanály. To umožní UE pokračovat v datové relaci bez nutnosti úplného zřízení RRC spojení z režimu nečinnosti (idle), čímž se významně zkrátí doba přerušení. Pokud kontext není nalezen (například protože byl po detekci RLF vymazán) nebo bezpečnostní kontrola selže, síť žádost odmítne zprávou RRC Connection Re-establishment Reject, což donutí UE přejít do stavu RRC_IDLE a zahájit nový postup zřízení spojení, což je pomalejší a může být vnímáno jako spadnutí hovoru.

Z architektonického hlediska CRE funguje ve vrstvě protokolu RRC v řídicí rovině a zahrnuje koordinaci mezi UE a eNodeB (nebo gNB v NR). Mezi klíčové komponenty patří mechanismy detekce RLF ve fyzické vrstvě UE, správa stavů RRC a udržování kontextu v základnové stanici sítě. Procedura spoléhá na to, že síť udržuje kontext UE po krátkou dobu po RLF, což je řízeno časovači, například časovačem pro uchování kontextu UE na eNodeB. CRE je úzce integrováno s dalšími procedurami mobility, jako je předávání spojení (handover), protože může být spuštěno při selhání handoveru a poskytuje záložní mechanismus pro obnovení spojení.

V širším kontextu sítě CRE zlepšuje robustnost mobility, zejména v náročných rádiových podmínkách, jako jsou okraje buněk nebo prostředí s vysokou interferencí. Snižuje míru spadnutí hovorů a zlepšuje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je míra spadnutí hovorů a kontinuita služby. Procedura je základním aspektem zotavení z selhání rádiového spoje a doplňuje další mechanismy, jako je opětovné připojení bez kontextu nebo překonfigurace spojení. Její účinnost závisí na faktorech, jako je připravenost buněk, vztahy sousedních buněk a nastavení časovačů, které jsou optimalizovány při plánování a provozu sítě.

## K čemu slouží

CRE bylo zavedeno, aby řešilo kritický problém přerušení služby způsobeného selháním rádiového spoje, což bylo v mobilních sítích běžné, zvláště když se s nástupem 3G a LTE rozšířily datové služby. Před zavedením CRE selhání rádiového spoje typicky přinutilo UE zcela ukončit hovor nebo datovou relaci a vyžadovalo úplné nové připojení od začátku. To vedlo ke špatnému uživatelskému zážitku, zvýšené signalizační zátěži sítě a vyšší míře spadnutí hovorů. Motivací bylo vytvořit rychlý mechanismus obnovy, který by dokázal zachránit probíhající relaci využitím zachovaného kontextu na straně sítě, a tím minimalizovat přerušení a zlepšit vnímanou spolehlivost.

Historicky měly starší celulární systémy omezené možnosti obnovy a často spoléhaly na jednoduché postupy opětovného připojení, které byly pomalé a neefektivní. S přechodem na paketové sítě ve 3GPP Release 5 a novějších rostla potřeba robustního řízení mobility, protože datové relace (např. VoIP, streamování) vyžadovaly nízkou latenci a kontinuitu. CRE tento problém řešilo poskytnutím standardizované procedury, která umožňuje rychlé opětovné zřízení spojení během vteřin, čímž se zkracuje doba, po kterou je UE v výpadku. Cílí konkrétně na scénáře, kdy rádiový spoj dočasně selže, například kvůli útlumu, interferenci nebo selhání handoveru, ale spojení v jaderné síti zůstává neporušeno.

Vytvoření CRE bylo hnací silou omezení předchozích přístupů, kterým chyběla obnova spojení s využitím kontextu. Bez CRE čelily sítě zvýšené signalizační režii z častých úplných opětovných připojení a zhoršené kvalitě služeb (QoS) pro služby v reálném čase. Tím, že umožňuje uchování a ověření kontextu, CRE umožňuje síti efektivně navázat na přerušené relace a řeší tak výzvy v oblasti mobility a řízení rádiových prostředků. Stalo se klíčovou funkcí v LTE a NR pro zajištění kontinuity služeb, což je v souladu s cíli 3GPP v oblasti vysoké spolehlivosti a bezproblémové mobility ve vyvíjejících se celulárních standardech.

## Klíčové vlastnosti

- Obnovuje spojení po selhání rádiového spoje (RLF) prostřednictvím opětovného zřízení RRC spojení.
- Pro rychlé navázání na relaci využívá uchování kontextu UE na eNodeB/gNB.
- Zahrnuje bezpečnostní ověření pomocí shortMAC-I, aby zabránilo neoprávněnému přístupu.
- Snižuje dobu přerušení služby ve srovnání s úplným novým připojením z režimu nečinnosti.
- Integruje se s procedurami mobility, jako je obnova po selhání předání spojení.
- Funguje na úrovni buňky, umožňuje opětovné zřízení spojení ke stejné nebo jiné připravené buňce.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers

---

📖 **Anglický originál a plná specifikace:** [CRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cre/)
