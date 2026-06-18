---
slug: "facch-f"
url: "/mobilnisite/slovnik/facch-f/"
type: "slovnik"
title: "FACCH/F – Fast Associated Control Channel/Full rate"
date: 2025-01-01
abbr: "FACCH/F"
fullName: "Fast Associated Control Channel/Full rate"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/facch-f/"
summary: "Plnorychlostní varianta FACCH používaná ve spojení s plnorychlostním kanálem pro přenos (TCH/F) v GSM. Krácí snímky z TCH/F pro přenos naléhavé signalizace a používá stejné schéma kódování kanálu a pr"
---

FACCH/F je plnorychlostní varianta rychlého příslušného řídicího kanálu, která krácuje snímky z plnorychlostního kanálu pro přenos (TCH/F), aby přenášela naléhavé signalizační zprávy během GSM hovoru, přičemž využívá stejné robustní kódování jako plnorychlostní řeč.

## Popis

Rychlý příslušný řídicí kanál s plnou přenosovou rychlostí ([FACCH](/mobilnisite/slovnik/facch/)/F) je konkrétní implementace konceptu FACCH navržená pro spolupráci s plnorychlostním kanálem pro přenos ([TCH/F](/mobilnisite/slovnik/tch-f/)) v systému GSM. TCH/F je kanál přenášející uživatelské informace – typicky digitalizovanou řeč při 13 kbps – využívající plnou kapacitu jednoho fyzického časového slotu na snímek. FACCH/F funguje shodně s obecným FACCH, ale je výslovně vázán na tohoto plnorychlostního přenosového nositele. Jeho fungování je definováno stejným principem 'krácení': když je třeba přenést naléhavou signalizační zprávu vrstvy 3, jsou na TCH/F přerušeny jeden nebo více 20ms bloků (každý nese 260 bitů kódované řeči).

Z technického hlediska tento proces zahrnuje nastavení příznaků krácení v hlavičce normálního výbuchu vysílačem, aby označily, že obsažená data jsou určena pro FACCH. Informační pole FACCH o délce 184 bitů (obsahující zprávu vrstvy 3) je následně zpracováno specifickým řetězcem kódování kanálu. Ten zahrnuje přidání 40bitového Fire kódu pro detekci chyb a 4 koncových bitů, po nichž následuje konvoluční kódování s poměrem 1/2, což vede ke vzniku 456bitového bloku. Tento blok je pak prokládán přes 8 po sobě jdoucích [TDMA](/mobilnisite/slovnik/tdma/) výbuchů, což přesně kopíruje schéma prokládání používané pro plnorychlostní řečový provoz ([TCH/FS](/mobilnisite/slovnik/tch-fs-2/)). Toto sdílené prokládání a kódování zajišťuje, že FACCH/F profituje ze stejné odolnosti proti útlumu a rušení jako samotný hlasový kanál.

V rámci síťové architektury je FACCH/F logický kanál aktivovaný pouze tehdy, když je mobilní stanice v přiděleném režimu na [TCH](/mobilnisite/slovnik/tch/)/F. Je řízen protokolem vrstvy 2 LAPDm jak na straně [MS](/mobilnisite/slovnik/ms/), tak [BTS](/mobilnisite/slovnik/bts/). Jeho primární role spočívá v usnadnění všech časově kritických řídicích funkcí pro plnorychlostní spojení, jako je provedení příkazů k předání řízení, správa změn šifrovacího režimu, odesílání zpráv okamžitého přidělení a přenos výsledků měření. Díky těsnému provázání s TCH/F zajišťuje, že řídicí signalizace pro kvalitní hlasový hovor zachovává podobnou přenosovou spolehlivost a časování, což je klíčové pro udržení integrity hovoru během událostí spojených s mobilitou nebo jiných zásahů sítě.

## K čemu slouží

[FACCH](/mobilnisite/slovnik/facch/)/F existuje proto, aby poskytoval rychlou a spolehlivou signalizační cestu specificky pro spojení využívající plnorychlostní GSM řečový kodek. Vytvoření odlišných variant (FACCH/F a FACCH/H pro poloviční rychlost) bylo motivováno rozdílnou strukturou kanálů a schématy kódování používanými pro plnorychlostní a poloviční kanály pro přenos. Univerzální FACCH by nebyl optimální, protože základní struktura snímků, kapacita bitů a schémata ochrany proti chybám se u podkladového TCH liší.

Historicky, když GSM definovalo svůj plnorychlostní řečový kanál (TCH/FS), potřebovalo odpovídající řídicí kanál, který by mohl plynule krácet část jeho kapacity bez komplikování návrhu přijímače. FACCH/F byl standardizován, aby bylo zajištěno, že mechanismus krácení, kódování a prokládání jsou dokonale sladěny s TCH/F. Tím bylo vyřešeno problém efektivního včlenění naléhavé síťové řídicí komunikace do hlasového proudu, což byl významný pokrok oproti dřívějším celulárním systémům, kde taková řídicí komunikace mohla vyžadovat samostatný paralelní kanál, který by spotřebovával další spektrum a přidával složitost.

Řešil specifickou potřebu signalizace s nízkou latencí spojenou s primární hlasovou službou raných GSM sítí. Přizpůsobením FACCH charakteristikám plnorychlostního kanálu zajistil 3GPP maximální kompatibilitu a výkon, což umožnilo robustní předání řízení a síťovou kontrolu, které byly klíčové pro komerční úspěch a vnímanou kvalitu GSM hlasových hovorů.

## Klíčové vlastnosti

- Specificky asociován s plnorychlostním kanálem pro přenos (TCH/F)
- Používá stejnou 20ms strukturu snímků a mechanismus krácení jako obecný FACCH
- Používá shodné kódování kanálu (konvoluční kód s poměrem 1/2) a prokládání (přes 8 výbuchů) jako TCH/FS
- Přenáší 184bitové zprávy vrstvy 3 pro naléhavé řízení
- Identifikován příznaky krácení v rámci normálního výbuchu
- Klíčový pro správu aktivních plnorychlostních hlasových hovorů

## Související pojmy

- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)
- [TCH/F – Traffic Channel / Full Rate](/mobilnisite/slovnik/tch-f/)
- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)
- [FACCH/H – Fast Associated Control Channel/Half rate](/mobilnisite/slovnik/facch-h/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [FACCH/F na 3GPP Explorer](https://3gpp-explorer.com/glossary/facch-f/)
