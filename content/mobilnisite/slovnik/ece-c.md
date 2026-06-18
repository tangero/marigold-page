---
slug: "ece-c"
url: "/mobilnisite/slovnik/ece-c/"
type: "slovnik"
title: "Ec – Average energy per PN chip"
date: 2025-01-01
abbr: "Ec"
fullName: "Average energy per PN chip"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ece-c/"
summary: "Ec je průměrná energie na čip pseudonáhodného kódu (PN čip), základní měření fyzické vrstvy v systémech 3GPP založených na CDMA, jako je UMTS. Kvantifikuje sílu signálu rozprostíracího kódu konkrétníh"
---

Ec je průměrná energie na čip pseudonáhodného kódu (PN čip), základní měření v CDMA, které kvantifikuje sílu signálu konkrétního kanálu vzhledem k celkovému přijímanému výkonu.

## Popis

Ec, představující průměrnou energii na [PN](/mobilnisite/slovnik/pn/) čip, je klíčový parametr fyzické vrstvy definovaný ve specifikacích 3GPP pro systémy s vícečetným přístupem s kódovým dělením ([CDMA](/mobilnisite/slovnik/cdma/)), především pro Univerzální mobilní telekomunikační systém (UMTS). Jde o naměřenou veličinu, nikoli o úroveň vysílaného výkonu. V CDMA jsou uživatelská data rozprostřena přes širší šířku pásma pomocí vysokorychlostního pseudonáhodného (PN) rozprostíracího kódu. Ec konkrétně měří příspěvek přijaté energie jednoho čipu této rozprostírací posloupnosti pro určitý fyzický kanál. Měření typicky provádí uživatelské zařízení (UE) na downlinku, například pro kanál Primárního společného pilotního kanálu ([P-CPICH](/mobilnisite/slovnik/p-cpich/)), ale může být relevantní i pro měření na síťové straně. Tato hodnota je zásadní, protože izoluje sílu signálu rozprostíracího kódu konkrétního kanálu od celkového přijímaného signálu, který zahrnuje interferenci a šum. Tato izolace umožňuje přesnou charakterizaci kvality kanálu.

Měření Ec je neodmyslitelně spojeno s dalšími klíčovými [RF](/mobilnisite/slovnik/rf/) měřeními. Nejvýznamněji je používáno při výpočtu poměru Ec/Io (energie na čip k spektrální hustotě výkonu interference) a Ec/No (energie na čip k spektrální hustotě šumového výkonu). Io představuje celkovou spektrální hustotu přijímaného výkonu včetně všech signálů, interference a šumu. Platí tedy Ec/Io = Ec / Io. Tento poměr je primární metrikou pro posouzení kvality CDMA signálu. Vyšší Ec/Io znamená silnější požadovaný signál vzhledem k celkové interferenci a šumu, což vede k lepší demodulační výkonnosti a nižší chybovosti. UE kontinuálně měří Ec/Io pro obsluhující i sousední buňky za účelem podpory procedur mobility, jako je předání spojení (handover) a překládka buňky (reselection).

Z pohledu provozu sítě jsou měření Ec základem několika klíčových funkcí správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)). Při počátečním výběru buňky a překládce používá UE naměřené Ec/Io pro P-CPICH k seřazení kandidátních buněk. Pro předání spojení jsou měření Ec/Io pro buňky aktivní sady a monitorované sady hlášena síti ([UTRAN](/mobilnisite/slovnik/utran/)) ke spuštění měkkých/tvrdších (soft/softer) nebo tvrdých (hard) handoverů. Dále tato měření vstupují do algoritmů vnitřní a vnější smyčky řízení výkonu. Sledováním přijímaného Ec/Io může UTRAN přikázat UE upravit svůj vysílací výkon na uplinku a naopak, aby se udržela cílová kvalita signálu při minimalizaci interference – což je základní princip CDMA. Přesné měření Ec je proto nezbytné pro stabilitu sítě, kapacitu, optimalizaci pokrytí a celkovou kvalitu služeb.

## K čemu slouží

Účelem definice a standardizace měření Ec bylo poskytnout základní, jednoznačnou metriku pro sílu signálu v prostředí s rozprostřeným spektrem a [CDMA](/mobilnisite/slovnik/cdma/). Dřívější buňkové systémy, jako GSM, se spoléhaly na měření ukazatele síly přijímaného signálu ([RSSI](/mobilnisite/slovnik/rssi/)) pro výkon nosné. V systému CDMA, kde více uživatelů sdílí stejnou frekvenci současně pomocí jedinečných kódů, však prosté měření celkového výkonu nestačí. Nerozlišuje výkon požadovaného signálu od interference generované ostatními uživateli (vícepřístupová interference) a šumu. Ec byl zaveden, aby tento problém vyřešil poskytnutím měření energie specifického pro konkrétní kód.

Toto měření specifické pro kód bylo klíčové pro praktickou implementaci řízení výkonu a měkkého předání spojení – dvou určujících vlastností UMTS, které maximalizují kapacitu a zlepšují mobilitu. Bez přesného měření energie na čip pro konkrétní kanál (jako je pilot) nemůže síť spolehlivě určit poměr signálu k interferenci (Ec/Io), což je skutečný determinant kvality spoje v interferencí omezeném CDMA systému. Standardizace Ec ve specifikacích 3GPP zajistila, že všechna UE a síťové vybavení budou tento parametr měřit a hlásit konzistentně, což umožnilo interoperabilní a efektivní RRM algoritmy. Odstranila omezení měření nespecifických pro kód a umožnila systému přesně řídit úroveň interference a optimalizovat kompromis mezi kvalitou jednotlivého uživatele a celkovou kapacitou sítě.

## Klíčové vlastnosti

- Měření energie specifické pro kód u signálů s rozprostřeným spektrem
- Základní vstup pro výpočet poměrů Ec/Io a Ec/No
- Kritická metrika pro procedury výběru a překládky buňky (cell selection/reselection) na straně UE
- Nezbytná pro spouštění a provedení měkkých (soft) a tvrdých (hard) handoverů v CDMA
- Klíčový parametr pro algoritmy řízení výkonu ve vnitřní a vnější smyčce
- Standardizované měření zajišťující interoperabilitu mezi UE a sítí

## Související pojmy

- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [RSSI – Received Signal Strength Indication](/mobilnisite/slovnik/rssi/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [Ec na 3GPP Explorer](https://3gpp-explorer.com/glossary/ece-c/)
