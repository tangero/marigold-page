---
slug: "dnu"
url: "/mobilnisite/slovnik/dnu/"
type: "slovnik"
title: "DNU – Do Not Use"
date: 2025-01-01
abbr: "DNU"
fullName: "Do Not Use"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dnu/"
summary: "DNU je značka nebo indikátor v rámci specifikací 3GPP, zejména v lokalizačních službách, který označuje, že konkrétní parametr, pole nebo hodnota by neměla být používána. Slouží k vyřazení zastaralých"
---

DNU je značka v rámci specifikací 3GPP, která označuje, že konkrétní parametr, pole nebo hodnota by neměla být používána. Slouží k vyřazení zastaralých prvků při zachování zpětné kompatibility.

## Popis

Do Not Use (DNU) je označení používané v technických specifikacích 3GPP k označení určitých parametrů, informačních prvků nebo hodnot jako zastaralých, vyhrazených pro budoucí použití nebo chybných. Hlavně se vyskytuje v TS 38.305, která definuje funkční specifikaci fáze 2 pro určování polohy uživatelského zařízení (UE) v NG-RAN. V tomto kontextu může být DNU použito u konkrétních lokalizačních metod, typů měření nebo signalizačních parametrů, které již nejsou doporučovány pro implementaci nebo které byly chybně definovány v dřívějších vydáních. Značka instruuje implementátory, aby se vyvarovali použití označené položky v nových nasazeních nebo návrzích, ačkoli může v dokumentaci stále být přítomna, aby byla zajištěna zpětná kompatibilita se stávajícími systémy nebo aby se zabránilo opětovnému použití identifikátoru pro jiný účel. Specifikace obvykle objasňuje důvod pro označení DNU, například nahrazení lepší metodou, odhalení technických nedostatků nebo sladění s aktualizovanými architektonickými principy. Z pohledu protokolu by síťový prvek nebo UE přijímající zprávu obsahující parametr označený DNU měl tento parametr buď ignorovat, považovat za chybu, nebo použít definované záložní chování podle specifikace. Zpracování prvků DNU je klíčové pro interoperabilitu, neboť zabraňuje šíření zastaralých funkcí do nových síťových implementací a zároveň umožňuje provoz starších zařízení. Proces standardizace v 3GPP používá DNU jako nástroj pro řízení vývoje protokolů, což zajišťuje, že specifikace zůstává přesná a jednoznačná v průběhu více vydání.

## K čemu slouží

Značka DNU byla vytvořena, aby řešila problém řízení vývoje protokolů a udržování srozumitelnosti specifikací v průběhu více vydání 3GPP. S vývojem mobilních standardů se některé funkce, parametry nebo metody měření stávají zastaralými v důsledku technologického pokroku, jsou shledány technicky vadnými nebo jsou nahrazeny efektivnějšími alternativami. Pouhé odstranění těchto prvků ze specifikací by mohlo narušit zpětnou kompatibilitu a způsobit problémy s interoperabilitou se staršími zařízeními již nasazenými v síti. Označení DNU poskytuje formální mechanismus pro vyřazení takových prvků bez jejich fyzického odstranění, což signalizuje implementátorům, že by neměly být používány v nových vývoji. To pomáhá zabránit přetrvávání zastaralých nebo nesprávných implementací, snižuje složitost testování a směruje průmysl k doporučeným postupům. Je to zvláště důležité ve složitých oblastech, jako je určování polohy, kde koexistuje více metod a přesnost je kritická. Označováním prvků jako DNU zajišťuje 3GPP, že specifikace zůstává spolehlivou referencí a zároveň přizpůsobuje přirozený životní cyklus funkcí protokolu.

## Klíčové vlastnosti

- Označuje konkrétní parametry, informační prvky nebo hodnoty ve specifikacích 3GPP jako zastaralé nebo vyhrazené
- Hlavně dokumentováno v TS 38.305 pro parametry určování polohy UE v NG-RAN
- Instruuje implementátory, aby se vyvarovali použití označené položky v nových návrzích nebo nasazeních
- Zachovává zpětnou kompatibilitu tím, že prvek zůstává ve specifikaci
- Zabraňuje opětovnému použití identifikátorů pro konfliktní účely v budoucích vydáních
- Objasňuje vývoj protokolu formálním označením zastaralých funkcí

## Definující specifikace

- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [DNU na 3GPP Explorer](https://3gpp-explorer.com/glossary/dnu/)
