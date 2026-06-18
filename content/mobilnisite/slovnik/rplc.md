---
slug: "rplc"
url: "/mobilnisite/slovnik/rplc/"
type: "slovnik"
title: "RPLC – Reference Picture List Construction"
date: 2025-01-01
abbr: "RPLC"
fullName: "Reference Picture List Construction"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rplc/"
summary: "Proces ve video kódování (např. v Enhanced Voice Services od 3GPP), který vytváří uspořádané seznamy referenčních snímků používaných pro inter predikci. Určuje, které dříve dekódované snímky jsou k di"
---

RPLC je proces ve video kódování, který vytváří uspořádané seznamy dříve dekódovaných referenčních snímků pro použití v pohybové kompenzaci během inter predikce.

## Popis

Reference Picture List Construction (RPLC, konstrukce seznamu referenčních snímků) je základní procedura ve standardech video komprese přijatých 3GPP pro multimediální služby, jako jsou ty specifikované v TS 26.906 pro Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) s videem. Zahrnuje vytváření a správu uspořádaných seznamů – typicky Seznam 0 a Seznam 1 – které obsahují referenční snímky (dříve dekódované video snímky) používané pro inter predikci během kódování a dekódování videa. Inter predikce redukuje redundanci tím, že kóduje aktuální snímek vzhledem k referenčním snímkům, přičemž používá pohybové vektory k popisu posunů. RPLC definuje, jak jsou tyto referenční snímky vybírány, řazeny a indexovány, což přímo ovlivňuje účinnost kódování, odolnost proti chybám a složitost dekodéru.

Z architektonického hlediska RPLC funguje v rámci predikčního rámce video kodeku, jako jsou kodeky H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/) používané v systémech 3GPP. Během kódování kodér rozhoduje, které referenční snímky uložit do Decoded Picture Buffer ([DPB](/mobilnisite/slovnik/dpb/)), a signalizuje příkazy RPLC dekodéru prostřednictvím bitového toku. Tyto příkazy instruují dekodér, jak sestavit identické seznamy referenčních snímků, čímž zajišťují synchronizaci. Seznamy mohou zahrnovat krátkodobé a dlouhodobé referenční snímky, s řazením založeným na picture order count, časové vzdálenosti nebo jiných kritériích. Mechanismy RPLC zvládají operace jako označování snímků (jako 'použitý pro referenci' nebo 'nepoužitý'), modifikaci seznamu a výchozí inicializaci seznamu na základě hlaviček řezů nebo sad parametrů sekvence.

V provozu je RPLC klíčový pro normální přehrávání i odolnost proti chybám. Například v prediktivním video kódování může P-slice použít Seznam 0 (pro dopřednou predikci) k odkazování na minulé snímky, zatímco B-slice může použít oba Seznam 0 a Seznam 1 (pro obousměrnou predikci) k odkazování na minulé a budoucí snímky. Proces konstrukce určuje, které reference jsou nejrelevantnější, což ovlivňuje účinnost hledání pohybu a výkon rate-distortion. V prostředích mobilních sítí náchylných k chybám lze RPLC nakonfigurovat pro zvýšení robustnosti – např. upřednostňováním referenčních snímků, které s vyšší pravděpodobností dorazí správně, nebo použitím redundantní správy referencí. To pomáhá maskovat ztráty paketů a udržovat kvalitu videa za různých síťových podmínek.

## K čemu slouží

RPLC byl standardizován v rámci 3GPP za účelem optimalizace přenosu videa přes bezdrátové sítě, kde je šířka pásma omezená a kanály jsou náchylné k chybám. Rané video kodeky měly jednodušší správu referenčních snímků, což mohlo vést k neefektivitě komprese nebo špatné obnově po chybách. RPLC poskytuje flexibilní, standardizovanou metodu pro konstrukci referenčních seznamů, což umožňuje lepší adaptaci na charakteristiky obsahu (např. pohyb, změny scény) a síťové podmínky, a tím zlepšuje celkovou kvalitu uživatelského zážitku u multimediálních služeb.

Historicky, s růstem používání mobilního videa, začlenilo 3GPP pokročilé video kodeky jako H.264 do specifikací, jako je [EVS](/mobilnisite/slovnik/evs/), pro podporu kvalitních hlasových a video hovorů. RPLC řeší omezení schémat s pevnými referenčními snímky tím, že umožňuje dynamickou konstrukci seznamů, což zlepšuje kompresi přesnější pohybovou predikcí a podporuje funkce jako hierarchické kódovací struktury. To je zvláště důležité pro komunikaci v reálném čase, kde je vyžadována nízká latence a vysoká odolnost.

Dále RPLC usnadňuje techniky odolnosti proti chybám, jako je výběr referenčního snímku, kde dekodéry mohou přepnout na alternativní reference, pokud jsou primární ztraceny. To snižuje vizuální artefakty a přerušení hovorů v proměnlivých rádiových podmínkách. Jeho zavedení ve verzi 12, jako součást vylepšených profilů video kodeků, odráží zaměření 3GPP na zlepšení multimediálního výkonu v LTE a novějších sítích, což zajišťuje efektivní využití spektra a síťových zdrojů při zachování spokojenosti uživatelů.

## Klíčové vlastnosti

- Vytváří uspořádané seznamy referenčních snímků pro inter predikci ve video kódování
- Podporuje jak dopředné (Seznam 0), tak obousměrné (Seznam 0/Seznam 1) predikční režimy
- Umožňuje dynamickou správu krátkodobých a dlouhodobých referenčních snímků
- Zvyšuje účinnost komprese optimalizovaným výběrem referencí
- Usnadňuje odolnost proti chybám tím, že umožňuje redundantní nebo alternativní referenční snímky
- Signalizováno prostřednictvím příkazů v bitovém toku pro zajištění synchronizace kodéru a dekodéru

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [RPLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rplc/)
