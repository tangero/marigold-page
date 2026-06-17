---
slug: "masa1"
url: "/mobilnisite/slovnik/masa1/"
type: "slovnik"
title: "MASA1 – MASA with 1 TC (mono-MASA)"
date: 2025-01-01
abbr: "MASA1"
fullName: "MASA with 1 TC (mono-MASA)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/masa1/"
summary: "Specifický profil standardu MASA, kde základní zvuk je jediný monofonní transportní kanál (TC). Prostorová zvuková scéna je plně popsána přidruženými metadaty, která instruují renderer, jak monofonní"
---

MASA1 je specifický profil MASA, kde základní zvuk je jediný monofonní transportní kanál a prostorový zvuk je vytvořen výhradně metadaty, která instruují renderer, aby tento monofonní signál prostorově zpracoval.

## Popis

MASA1, neboli mono-MASA, je definovaný profil ve standardu Metadata-Assisted Spatial Audio, kde je podkladová zvuková podstata zakódována jako jediný monofonní transportní kanál (TC). Tento jediný zvukový kanál obsahuje součet všech zvukových prvků ve scéně. Kompletní prostorová informace – včetně pozice, šířky a pohybu jednotlivých zvukových zdrojů – je přenášena výhradně v samostatném datovém proudu [MASA](/mobilnisite/slovnik/masa/) metadat. Při dekódování renderer v přijímači zpracuje monofonní zvukový signál a aplikuje prostorové parametry z metadat, čímž vytvoří vícerozměrný, imerzivní zvukový obraz. Architektura využívá pokročilé techniky zpracování signálu, jako je filtrování a panoramování amplitudy, které jsou diktovány metadaty k 'umístění' zvuků kolem posluchače. Klíčové komponenty jsou totožné se základním rámcem MASA, ale pracují se vstupem z jediného zvukového kanálu. Jeho úlohou je poskytnout nejefektivnější metodu z hlediska spektrální účinnosti pro doručování základních prostorových zvukových scén, ideální pro aplikace s nižší zvukovou složitostí nebo s omezenou šířkou pásma, přičemž stále nabízí významné vylepšení oproti prostému monofonnímu zvuku přidáním prostorového rozměru.

## K čemu slouží

MASA1 byl definován jako základní profil s minimální složitostí pro ekosystém [MASA](/mobilnisite/slovnik/masa/). Řeší potřebu přidání prostorové imerze službám, kde původní zvuk může být monofonní (např. podcast, hovor nebo starší zvukový materiál), nebo kde je primárním omezením ultra-nízký datový tok. Před MASA by povýšení monofonní služby na prostorový zvuk vyžadovalo kompletní překódování obsahu do vícekanálového nebo objektového formátu, což by významně zvýšilo datový tok. MASA1 to řeší tím, že umožňuje stávající monofonní zvuk repurpovat pomocí lehkých metadat, což umožňuje prostorový zážitek bez nákladů na šířku pásma spojených s přenosem více diskrétních zvukových kanálů. Poskytuje jasnou cestu migrace pro poskytovatele služeb k vylepšení stávajících služeb založených na monu o imerzivní funkce.

## Klíčové vlastnosti

- Základní zvuk se skládá z jediného monofonního transportního kanálu (TC)
- Úplný popis prostorové scény je delegován na stopu metadat
- Nejnižší požadavek na datový tok mezi profily MASA
- Umožňuje prostorové zpracování staršího monofonního obsahu
- Používá renderování založené na HRTF nebo panoramování pro přehrávání přes sluchátka a reproduktory
- Slouží jako základ pro složitější profily MASA

## Související pojmy

- [MASA – Metadata-Assisted Spatial Audio](/mobilnisite/slovnik/masa/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [MASA1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/masa1/)
