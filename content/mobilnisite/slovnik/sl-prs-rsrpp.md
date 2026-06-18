---
slug: "sl-prs-rsrpp"
url: "/mobilnisite/slovnik/sl-prs-rsrpp/"
type: "slovnik"
title: "SL-PRS-RSRPP – Sidelink Positioning Reference Signal based Reference Signal Received Path Power"
date: 2025-01-01
abbr: "SL-PRS-RSRPP"
fullName: "Sidelink Positioning Reference Signal based Reference Signal Received Path Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-prs-rsrpp/"
summary: "Měření přijímaného výkonu na dráze u pozicních referenčních signálů pro postranní spojení (SL-PRS) s uvážením více šířicích drah. Poskytuje přehled o rozložení výkonu napříč různými zpožďovacími větve"
---

SL-PRS-RSRPP je měření přijímaného výkonu na dráze u pozicních referenčních signálů pro postranní spojení (Sidelink Positioning Reference Signals) přes více šířicích drah, což napomáhá charakterizaci vícecestného šíření a zvyšuje přesnost určování polohy.

## Popis

SL-PRS-RSRPP je pokročilé měření fyzické vrstvy definované ve specifikacích 3GPP 37.571, 38.305 a 38.355. Rozšiřuje koncept [RSRP](/mobilnisite/slovnik/rsrp/) tím, že měří přijímaný výkon [SL-PRS](/mobilnisite/slovnik/sl-prs/) pro každou dráhu zvlášť, čímž zachycuje příspěvek výkonu od jednotlivých komponent vícecestného šíření. Na rozdíl od [SL-PRS-RSRP](/mobilnisite/slovnik/sl-prs-rsrp/), které poskytuje agregované měření výkonu, SL-PRS-RSRPP rozkládá přijímaný signál na jednotlivé dráhy na základě jejich zpožďovacích profilů, čímž nabízí podrobnější pohled na impulsní odezvu kanálu. To je zvláště cenné pro pozicní techniky využívající informace o vícecestném šíření, jako je otiskování rádiového prostředí (fingerprinting) nebo vylepšené odhady času příchodu (ToA).

Proces měření zahrnuje přijímající UE, které provádí odhad kanálu pomocí známých sekvencí SL-PRS. K identifikaci a izolaci jednotlivých šířicích drah ze složeného přijímaného signálu se používají pokročilé algoritmy, jako je detekce založená na korelaci nebo zpracování inverzní rychlou Fourierovou transformací ([IFFT](/mobilnisite/slovnik/ifft/)). Pro každou detekovatelnou dráhu UE vypočítá přijímaný výkon, přičemž typicky hlásí nejsilnější dráhy nebo ty, které překročily určitou prahovou hodnotu. Výsledky mohou zahrnovat parametry jako výkon dráhy, zpoždění a případně i úhlové informace, což poskytuje bohatou datovou sadu pro pozicní algoritmy.

Z architektonického hlediska vyžaduje měření SL-PRS-RSRPP sofistikované schopnosti zpracování signálu ve fyzické vrstvě UE, často zahrnující jednotky pro zpracování základního pásma a vyhrazený hardware pro korelaci a Fourierovy transformace. Mezi klíčové komponenty patří konfigurace SL-PRS, algoritmus odhadu kanálu a kritéria pro detekci drah. Jeho úlohou je umožnit vysokorozlišovací určování polohy prostřednictvím využití diverzity vícecestného šíření. Analýzou výkonu a zpoždění více drah mohou pozicní algoritmy lépe rozlišit podmínky přímé viditelnosti ([LOS](/mobilnisite/slovnik/los/)) a nepřímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)), zmírnit chyby způsobené vícecestným šířením a zlepšit přesnost určení polohy v městských kaňonech, vnitřních prostorech a dalších složitých scénářích šíření.

## K čemu slouží

SL-PRS-RSRPP bylo zavedeno v Release 18, aby řešilo omezení agregovaných měření výkonu v prostředích bohatých na vícecestné šíření, což je běžné ve scénářích postranního spojení, jako je městský [V2X](/mobilnisite/slovnik/v2x/) nebo provozy továren. Tradiční měření [RSRP](/mobilnisite/slovnik/rsrp/) nedokázala rozlišit různé šířicí dráhy, což vedlo k chybám v určování polohy, když silné odražené dráhy zastínily skutečnou přímou dráhu nebo když bylo vícecestné šíření mylně interpretováno jako pohyb.

Jeho vytvoření bylo motivováno potřebou dosáhnout přesnosti určování polohy na úrovni pod metr v pokročilých případech užití, jako je manévrování autonomních vozidel nebo rojení dronů. Předchozí přístupy, spoléhající na měření výkonu jedné dráhy, selhávaly v NLOS podmínkách a prostředích s hustým vícecestným šířením. Poskytnutím měření výkonu pro každou dráhu zvlášť umožňuje SL-PRS-RSRPP sofistikovanějším pozicním algoritmům identifikovat a využít více signálových drah, čímž zvyšuje odolnost vůči útlumu z vícecestného šíření, zlepšuje detekci NLOS a v konečném důsledku poskytuje vyšší přesnost a spolehlivost určení polohy.

## Klíčové vlastnosti

- Měří přijímaný výkon SL-PRS pro každou dráhu zvlášť
- Zachycuje komponenty vícecestného šíření s odlišnými zpožďovacími profily
- Napomáhá rozlišovat podmínky šíření s přímou (LOS) a nepřímou (NLOS) viditelností
- Podporuje pokročilé pozicní algoritmy, jako je otiskování prostředí (fingerprinting) a určování polohy asistované vícecestným šířením
- Zvyšuje přesnost v náročných prostředích s bohatým rozptylem
- Poskytuje podrobné informace o impulsní odezvě kanálu pro postranní spojení

## Související pojmy

- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [SL-PRS-RSRP – Sidelink Positioning Reference Signal based Reference Signal Received Power](/mobilnisite/slovnik/sl-prs-rsrp/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-PRS-RSRPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-prs-rsrpp/)
