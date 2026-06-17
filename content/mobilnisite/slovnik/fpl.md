---
slug: "fpl"
url: "/mobilnisite/slovnik/fpl/"
type: "slovnik"
title: "FPL – Free Path Loss"
date: 2025-01-01
abbr: "FPL"
fullName: "Free Path Loss"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fpl/"
summary: "Free Path Loss (FPL) je teoretický model útlumu rádiových vln v dokonalém vakuu, představující ztrátu výkonu signálu způsobenou pouze sférickým šířením s rostoucí vzdáleností. Slouží jako základní ref"
---

FPL je teoretická ztráta výkonu rádiového signálu v dokonalém vakuu, způsobená pouze vzdáleností a sférickým šířením, která slouží jako základní referenční hodnota při výpočtech rozpočtu rádiového spojení.

## Popis

Free Path Loss (FPL), často synonymní s Free-Space Path Loss (FSPL), je základním konceptem ve fyzice šíření rádiových vln a je odkazován ve specifikacích 3GPP, jako je TS 45.050 pro GSM/[EDGE](/mobilnisite/slovnik/edge/). Modeluje útlum elektromagnetické vlny při jejím šíření ideálním, nerušeným prostředím (volným prostorem) od izotropního vysílače k izotropnímu přijímači. Ztráta není způsobena absorpcí nebo rozptylem, ale čistě geometrickým rozptylem energie, jak se vlnoplocha sféricky šíří z bodového zdroje. Hustota výkonu, a následně výkon zachycený přijímací anténou s danou efektivní plochou, klesá s druhou mocninou vzdálenosti.

Výpočet FPL je dán Friisovým vzorcem pro přenos. V nejjednodušší logaritmické podobě pro praktické inženýrství je útlum (L) v decibelech dán vztahem L (dB) = 20log10(d) + 20log10(f) + 20log10(4π/c) – Gt – Gr, kde 'd' je vzdálenost, 'f' je frekvence, 'c' je rychlost světla a Gt a Gr jsou zisky antén vysílače a přijímače v dBi. Při předpokladu izotropních antén (Gt=Gr=0 dBi) se vzorec zjednoduší na standardní výraz: FSPL (dB) = 20log10(d) + 20log10(f) + 92,45 (kde d je v km a f v GHz). Tato hodnota představuje minimální teoretickou ztrátu mezi dvěma ideálními anténami.

V návrhu a testování systémů 3GPP slouží FPL jako klíčový referenční bod. Analýza rozpočtu spojení vždy začíná výpočtem FPL pro danou vzdálenost a frekvenci. Inženýři poté přidávají rezervy pro různé další, neideální ztráty a zisky: ztráty prostupem, stínový únik (log-normální), vícecestný únik (Rayleighův/Riceův), atmosférickou absorpci a ztráty způsobené deštěm, stejně jako zisky z anténní směrovosti a diverzity. FPL poskytuje deterministické, na vzdálenosti závislé jádro modelu šíření. Je zásadní pro určení maximálního dosahu buňky, potřebného výkonu vysílače, citlivosti přijímače a pro nastavení parametrů v algoritmech správy rádiových zdrojů. V testování shody (např. pro výstupní výkon [MS](/mobilnisite/slovnik/ms/)) mohou scénáře předpokládat podmínky FPL, aby izolovaly konkrétní výkon zařízení od proměnných prostředí.

## K čemu slouží

Koncept Free Path Loss existuje proto, aby stanovil základní, předvídatelnou fyzikální mez pro dosah rádiové komunikace v ideálním prostředí. Ještě předtím, než se vezmou v úvahu složitosti šíření v reálném světě – jako jsou odrazy, difrakce a absorpce – potřebují inženýři základní model odvozený z prvních principů fyziky. Tento model odpovídá na otázku: 'O kolik by se signál se vzdáleností zeslabil, kdyby mu nic jiného nestálo v cestě?'

Historicky, a při vývoji celulárních standardů, jako jsou ty od 3GPP, byla tato základní hodnota klíčová pro počáteční dimenzování systému a teoretické výkonnostní limity. Řeší problém pochopení vnitřního, nevyhnutelného faktoru ztráty v jakémkoli bezdrátovém spoji. Bez tohoto modelu by bylo nemožné čistě oddělit výkon zařízení (např. výkon vysílače, šumové číslo přijímače) od vlivů prostředí. Model FPL zdůraznil potřebu anténního zisku, vyššího vysílaného výkonu a citlivých přijímačů k překonání i této základní geometrické ztráty. Také ukazuje dopad volby frekvence, protože vyšší frekvence trpí při stejné vzdálenosti větším FPL, což je klíčový aspekt při plánování sítí pro 3G, 4G a nasazení 5G v mmWave pásmech. Slouží jako referenční bod 'dokonalého světa', vůči kterému se měří a zmírňuje degradace způsobená reálným světem.

## Klíčové vlastnosti

- Modeluje útlum signálu způsobený čistě sférickou expanzí vlnoplochy ve vakuu
- Ztráta roste s druhou mocninou vzdálenosti (20 dB/dekáda) a druhou mocninou frekvence (20 dB/dekáda)
- Odvozeno z Friisova přenosového vzorce a základní elektromagnetické teorie
- Poskytuje deterministickou, vypočítatelnou základní hodnotu pro jakoukoli kombinaci vzdálenosti a frekvence
- Předpokládá izotropní antény a žádné překážky, absorpci nebo odraz
- Základní součást všech výpočtů rozpočtu rádiového spojení a základů modelů šíření

## Definující specifikace

- **TS 45.050** (Rel-19) — Background on GSM RF Requirements Derivation

---

📖 **Anglický originál a plná specifikace:** [FPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/fpl/)
