---
slug: "mnrr"
url: "/mobilnisite/slovnik/mnrr/"
type: "slovnik"
title: "MNRR – Mobile station Not Reachable Reason"
date: 2025-01-01
abbr: "MNRR"
fullName: "Mobile station Not Reachable Reason"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mnrr/"
summary: "Parametr udávající důvod, proč je UE v SGSN označena jako nedosažitelná (např. implicitní odpojení). Poskytuje diagnostické informace pro správu sítě a pomáhá rozlišovat typy nedosažitelnosti pro lepš"
---

MNRR je parametr udávající důvod, proč je mobilní stanice označena jako nedosažitelná, a poskytuje diagnostické informace pro správu sítě, aby bylo možné rozlišit typy nedosažitelnosti.

## Popis

Mobile station Not Reachable Reason (MNRR, důvod nedosažitelnosti mobilní stanice) je informační parametr definovaný v 3GPP TS 23.060, který je spolu s příznakem [MNRG](/mobilnisite/slovnik/mnrg/) uložen v kontextu správy mobility (Mobility Management context) pro UE v [SGSN](/mobilnisite/slovnik/sgsn/). Zatímco MNRG je jednoduchý příznak označující, *že* je UE pro [GPRS](/mobilnisite/slovnik/gprs/) nedosažitelná, MNRR poskytuje konkrétní důvod, *proč* ji SGSN považuje za nedosažitelnou. Tím přidává podrobnost do stavu nedosažitelnosti, což umožňuje inteligentnější chování sítě a lepší diagnostiku.

MNRR může nabývat hodnot jako 'IMPLICIT_DETACH' nebo 'PURGED'. Nejběžnější hodnotou je 'IMPLICIT_DETACH', která značí, že síť UE implicitně odpojila z důvodu vypršení 'mobile reachable timeru' bez jakéhokoli kontaktu ze strany UE. Tento časovač se spustí, když UE přejde do nečinného stavu (PMM-IDLE), a jeho vypršení naznačuje, že UE mohla opustit oblast pokrytí nebo byla vypnuta bez řádného odpojení. Další možnou hodnotou může být důvod související s administrativním vymazáním (purge). MNRR je nastaven současně s příznakem MNRG při výskytu spouštěcí podmínky.

Tento důvodový kód je interně používán SGSN a může být také v určitých scénářích předán dalším síťovým entitám. Například když [HLR](/mobilnisite/slovnik/hlr/) provádí proceduru obnovy SGSN nebo když je kontext přenášen mezi SGSN, může MNRR poskytnout kontext o předchozím stavu UE. Pomáhá při správě sítě a odstraňování problémů tím, že umožňuje operátorům rozlišit mezi UE, která neodpověděla na volání (což může nastavit MNRG, ale ne nutně podrobný MNRR), a UE, která byla implicitně odpojena z důvodu dlouhé nečinnosti. MNRR v kombinaci s MNRG vytváří úplnější obraz o stavu správy mobility UE, což umožňuje optimalizované procedury pro opětovné připojení a obnovu služeb, když se UE opět stane dosažitelnou.

## K čemu slouží

MNRR byl zaveden jako doplněk k příznaku [MNRG](/mobilnisite/slovnik/mnrg/) za účelem poskytnutí informace o příčině stavu nedosažitelnosti UE. Jednoduchý binární příznak (MNRG) postačuje pro základní řízení toku k zastavení volání, ale nenabízí žádný vhled pro síťové operace, správu chyb nebo pokročilé procedury. Znalost důvodu nedosažitelnosti umožňuje síti inteligentněji zpracovávat následné události.

Například, pokud UE označená jako nedosažitelná z důvodu 'IMPLICIT_DETACH' náhle provede aktualizaci směrovací oblasti (Routing Area Update), [SGSN](/mobilnisite/slovnik/sgsn/) ví, že se jedná o opětovné připojení dříve ztracené UE, a může proceduru odpovídajícím způsobem zpracovat, případně vyžadovat opětovné ověření. Pomáhá také ve scénářích selhání a obnovy síťových uzlů; pokud se SGSN restartuje a obnoví kontext ze zálohy, MNRR indikuje, zda byla UE aktivně odpojena, nebo pouze dočasně nedosažitelná. Tato podrobnost pomáhá rozlišit mezi normálně vypnutou UE a UE, která může mít problémy s rádiovým signálem. Odstraňuje tak omezení jednoduchého příznaku přidáním diagnostické a procedurální vrstvy, což je cenné pro spolehlivost sítě, správu zákaznické zkušenosti a operační podpůrné systémy v komplexních sítích [GPRS](/mobilnisite/slovnik/gprs/)/UMTS.

## Klíčové vlastnosti

- Důvodový kód uložený pro každou UE v SGSN spolu s příznakem MNRG
- Poskytuje konkrétní příčinu nedosažitelnosti v paketové doméně (např. IMPLICIT_DETACH)
- Vylepšuje síťovou diagnostiku a správu chyb
- Používán interně SGSN pro správu stavu a zpracování procedur
- Může být předáván během přenosu kontextu mezi SGSN nebo procedur obnovy
- Doplňuje binární příznak MNRG podrobnou informací o příčině

## Související pojmy

- [MNRG – Mobile station Not Reachable for GPRS flag](/mobilnisite/slovnik/mnrg/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [MNRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnrr/)
