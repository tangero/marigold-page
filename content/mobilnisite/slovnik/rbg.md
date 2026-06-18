---
slug: "rbg"
url: "/mobilnisite/slovnik/rbg/"
type: "slovnik"
title: "RBG – Resource Block Group"
date: 2025-01-01
abbr: "RBG"
fullName: "Resource Block Group"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rbg/"
summary: "Resource Block Group (RBG) je souvislá skupina fyzických bloků zdrojů (PRB), které jsou přidělovány jako jediná jednotka pro účely plánování v LTE a NR. RBG se používají ke snížení signalizační režie"
---

RBG je souvislá skupina fyzických bloků zdrojů (Physical Resource Blocks), která je přidělována jako jediná jednotka pro plánování v LTE a NR za účelem snížení režie signalizace v downlinku; její velikost je konfigurovatelná na základě šířky pásma systému.

## Popis

Resource Block Group (RBG) je základní jednotka pro přidělování zdrojů ve frekvenční oblasti v rámci rozhraní LTE a 5G NR založeného na [OFDMA](/mobilnisite/slovnik/ofdma/). Fyzický blok zdrojů ([PRB](/mobilnisite/slovnik/prb/)) je nejmenší jednotka zdroje, kterou lze přidělit uživateli, a je definována jako 12 po sobě jdoucích podnosných po dobu jednoho slotu (0,5 ms v LTE). Signalizace přidělení jednotlivých PRB pro každého uživatele v každém podrámci by však vytvořila nadměrnou režii řídicího kanálu. Aby se tomu zabránilo, standard definuje RBG, kde je skupina souvislých PRB považována za jedinou přidělitelnou entitu. Plánovač v gNB (nebo [eNB](/mobilnisite/slovnik/enb/)) přidělí jednomu nebo více RBG uživatelskému zařízení (UE) pomocí bitmapy v downlink control information ([DCI](/mobilnisite/slovnik/dci/)).

Velikost RBG (P) není pevná; je funkcí šířky pásma systému. Specifikace 3GPP 36.213 definuje tabulku mapující počet downlink bloků zdrojů (šířka pásma systému) na velikost RBG. Například pro šířku pásma systému 10 MHz (50 PRB) je velikost RBG typicky 3 PRB. To vede k přibližně 17 RBG (50/3, zaokrouhleno nahoru). Formát DCI pro typ přidělení zdrojů 0 používá bitmapu, kde každý bit odpovídá jednomu RBG. Bit nastavený na '1' znamená, že příslušný RBG je přidělen uživatelskému zařízení (UE). Tato metoda, známá jako Resource Allocation Type 0, poskytuje kompaktní reprezentaci. Pro menší šířky pásma nebo jemněji granulované přidělení umožňuje Resource Allocation Type 1 přidělení podmnožiny PRB v rámci RBG, ale stále používá RBG jako referenční strukturu.

Přidělování založené na RBG přímo ovlivňuje flexibilitu a efektivitu plánování. Větší velikosti RBG snižují režii DCI, ale snižují granularitu plánování, což může vést k neefektivnímu využití zdrojů, zejména pro uživatele s malými datovými pakety nebo na okraji buňky vyžadující zisk z frekvenčně selektivního plánování. Menší velikosti RBG nabízejí jemnější granularitu, ale zvyšují signalizační náklady. Síť může nakonfigurovat preferovaný typ přidělení. V 5G NR je tento koncept zachován a vylepšen. NR definuje velikost Resource Block Group pro plánování založené na bandwidth part ([BWP](/mobilnisite/slovnik/bwp/)) a DCI může indikovat přidělení zdrojů pomocí resource indication value ([RIV](/mobilnisite/slovnik/riv/)) pro souvislá přidělení nebo bitmapy pro nesouvislá, přičemž granularita je vázána na PRB a nakonfigurovaný BWP.

## K čemu slouží

Mechanismus Resource Block Group byl vytvořen, aby vyřešil kritický problém režie řídicího kanálu v buňkových systémech založených na [OFDMA](/mobilnisite/slovnik/ofdma/), jako jsou LTE a NR. Tyto systémy nabízejí vysokou flexibilitu tím, že umožňují dynamické přidělování frekvenčních zdrojů ([PRB](/mobilnisite/slovnik/prb/)) více uživatelům v každém transmission time interval (TTI). Signalizace přesné sady PRB pro každého uživatele by vyžadovala velký počet bitů v downlink řídicím kanálu (PDCCH), což by spotřebovalo značné zdroje, které by jinak mohly být použity pro přenos dat, a omezilo by počet uživatelů, kteří mohou být plánováni současně. RBG poskytují praktický kompromis mezi granularitou plánování a efektivitou signalizace.

Zavedené v LTE Release 8 řešily RBG omezení jednodušších schémat přidělování používaných v předchozích technologiích. 3G UMTS používalo kódový multiplex (CDMA) s rozprostíracími faktory, které měly odlišné charakteristiky režie. Přechod na OFDMA v LTE vyžadoval novou metodu pro efektivní indikaci zdrojů ve frekvenční oblasti. Koncept RBG umožnil síti volit mezi jemně granulovaným, frekvenčně selektivním plánováním (výhodným pro plánování s ohledem na stav kanálu v podmínkách frekvenčně selektivního útlumu) a kapacitou řídicího kanálu. Umožnil podporu širších šířek pásma systému (až 20 MHz v LTE Rel-8) bez proporcionálního nárůstu signalizační režie.

V 5G NR (od Release 15) zůstává účel RBG zachován, ale v rámci flexibilnější architektury. NR podporuje mnohem širší šířky pásma (až 400 MHz) a rozmanité use cases. Koncept RBG je aplikován v rámci Bandwidth Part (BWP), což je podmnožina celkové šířky pásma nosné nakonfigurovaná pro uživatelské zařízení (UE). To umožňuje efektivní plánování i pro uživatelská zařízení, která nepodporují plnou šířku pásma nosné. Konfigurovatelná velikost RBG v rámci BWP umožňuje operátorům optimalizovat kompromis mezi režií a granularitou konkrétně pro služby (např. massive IoT s malými pakety vs. eMBB s velkými dávkami) aktivní na daném BWP, což je zásadní pro network slicing a optimalizaci specifickou pro službu.

## Klíčové vlastnosti

- Snížení režie: Seskupuje více PRB do jedné plánovatelné jednotky, což výrazně snižuje počet bitů potřebných v DCI pro přidělení zdrojů.
- Konfigurovatelná velikost: Velikost RBG (P) je určena šířkou pásma systému (LTE) nebo velikostí bandwidth part (NR), což umožňuje kompromis mezi granularitou a režií.
- Přidělování založené na bitmapě: V Resource Allocation Type 0 jednoduchá bitmapa v DCI, kde každý bit představuje jeden RBG, indikuje nesouvislá přidělení zdrojů.
- Definice závislá na šířce pásma: Počet RBG v systému se škáluje s celkovou dostupnou šířkou pásma, čímž udržuje konzistentní škálování režie.
- Základ pro plánování: Umožňuje jak souvislé, tak nesouvislé strategie plánování ve frekvenční oblasti v rámci omezení řídicího kanálu.
- Vylepšení v NR: Aplikováno v kontextu Bandwidth Part (BWP) v 5G NR, což poskytuje flexibilitu pro uživatelským zařízením specifické konfigurace šířky pásma a network slicing.

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [RBG na 3GPP Explorer](https://3gpp-explorer.com/glossary/rbg/)
