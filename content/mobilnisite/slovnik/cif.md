---
slug: "cif"
url: "/mobilnisite/slovnik/cif/"
type: "slovnik"
title: "CIF – Common Intermediate Format"
date: 2025-01-01
abbr: "CIF"
fullName: "Common Intermediate Format"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cif/"
summary: "CIF je schéma přidělování prostředků v LTE a NR, které rozděluje systémovou přenosovou kapacitu na podrámce, umožňující dynamické plánování přes komponentní nosiče při agregaci nosičů. Umožňuje efekti"
---

CIF je Common Intermediate Format, schéma přidělování prostředků v LTE a NR, které rozděluje přenosovou kapacitu na podrámce pro dynamické plánování přes nosiče při agregaci nosičů, což umožňuje efektivní využití fragmentovaného spektra.

## Popis

Common Intermediate Format (CIF) je základní mechanismus v specifikacích 3GPP LTE a NR, speciálně navržený pro podporu agregace nosičů ([CA](/mobilnisite/slovnik/ca/)). Funguje na [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) vrstvě a je integrální součástí řídicí informace pro downlink ([DCI](/mobilnisite/slovnik/dci/)) přenášené přes kanál [PDCCH](/mobilnisite/slovnik/pdcch/) (Physical Downlink Control Channel). CIF zavádí 3bitové pole ve formátu DCI, které explicitně indikuje index komponentního nosiče ([CC](/mobilnisite/slovnik/cc/)), na kterém bude probíhat plánovaný datový přenos (na [PDSCH](/mobilnisite/slovnik/pdsch/) nebo [PUSCH](/mobilnisite/slovnik/pusch/)). To umožňuje, aby jediný plánovací příkaz, odeslaný na jednom CC (plánující buňka), přidělil prostředky na jiném CC (plánovaná buňka), centralizuje tak řízení a snižuje režii řídicích kanálů.

Architektonicky CIF umožňuje plánování přes nosiče (cross-carrier scheduling), klíčovou vlastnost agregace nosičů. Bez CIF každý komponentní nosič potřebuje vlastní PDCCH pro plánování svého datového kanálu, což vede k potenciálnímu zahlcení řídicích kanálů a neefektivnímu využití řídicích prostředků. S CIF může uživatelské zařízení (UE) nakonfigurované s více agregovanými nosičemi být plánováno přes tyto nosiče pomocí řídicí signalizace přenášené primárně na jedné určené primární buňce (PCell) nebo sekundární buňce (SCell). MAC vrstva používá hodnotu CIF k mapování přijatého povolení na správnou zpracovatelskou řadu transportního bloku příslušného komponentního nosiče.

Z pohledu fyzické vrstvy je přítomnost pole CIF konfigurována semistaticky pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). Pokud je plánování přes nosiče aktivované, formáty DCI (např. Format 1_1 v NR) obsahují CIF. UE při dekódování DCI zkoumá CIF k identifikaci indexu servisní buňky (jak nakonfigurovalo RRC) a následně aplikuje přidělení prostředků (RB assignment, MCS, HARQ info) obsahované v tom samém DCI na tento specifický komponentní nosič. To odděluje místa řídicí a datové transmise, poskytuje významnou flexibilitu při řízení interference, vyvažování zatížení a využití fragmentů spektra, které mohou mít různé charakteristiky propagace nebo podmínky interference.

Role CIF sahá za prostou indikaci plánování. Je klíčová pro pokročilé funkce CA jako doplňkový uplink (SUL), kde uplink nosiče mohou být agregované z různých frekvenčních pásem, a pro frameworky duální konektivity (DC), avšak v DC existují komplexnější interakce s C-RNTI (Cell Radio Network Temporary Identifier) a oddělenými MAC entitami. V NR jsou principy CIF rozšířené pro podporu širších přenosových kapacit, více komponentních nosičů (až 16 v novějších releasách) a integrace s operací části přenosové kapacity (BWP), kde plánování může také indikovat specifický BWP na cílovém nosiči.

## K čemu slouží

CIF byl zaváděn k řešení kritických problémů vznikajících při nasazení agregace nosičů v LTE-Advanced (Rel-10). Primární motivací byla efektivní a flexibilní řídicí signalizace v prostředí s více nosiči. Rané LTE systémy fungovaly na jednom souvislém bloku spektra. Jak operátoři získali fragmentované licence spektra přes více frekvenčních pásem (např. 700 MHz, 1800 MHz, 2.6 GHz), byl potřebný mechanismus k spojení těchto nesouvislých bloků do jediného, logického vysokokapacitního kanálu pro uživatele. Pouhé vysílání nezávislých řídicích kanálů na každém fragmentu bylo nehospodárné a mohlo vést k blokování řídicích kanálů, což limituje zisky plánování více uživatelů.

Před CIF a plánováním přes nosiče bylo plánování samo-plánované — každý komponentní nosič zpracovával své vlastní řízení a data. To představovalo významné problémy při nasazení heterogenních sítí (HetNet) s rozšířením dosahu buňky. UE na okraji malé buňky (používající jeden nosič) mohlo trpět silnou interferencí na řídicím kanálu (PDCCH) od silné makro buňky na stejné nosné frekvenci, což znemožňovalo přijímání plánovacích povolení. CIF umožnil plánování přes nosiče, dovolující malé buňce plánovat datový přenos UE na svém nosiči pomocí řídicího kanálu vysílaného na jiném, neinterferovaném nosiči (např. makro nosič nižší frekvence). To byl průlom pro koordinaci interference a výkon HetNet.

Dále CIF snižuje režii řídicích kanálů a spotřebu energie UE. Namísto monitorování PDCCH na každém nakonfigurovaném komponentním nosiči (což vyžaduje nepřetržité zpracování přijímače) může být UE nakonfigurováno primárně monitorovat PDCCH na jediném nosiči (plánující buňka), i když jsou data přenášená na více nosičích. To zjednodušuje implementaci UE, šetří život baterie a umožňuje síti dynamicky řídit přidělování řídicích prostředků. Účel CIF je tedy hluboce spojený s umožněním škálovatelného, robustního a efektivního využití fragmentovaných a heterogenních spektrálních zdrojů, což je základním pilířem kapacitních a pokrytových strategií 4G a 5G.

## Klíčové vlastnosti

- Umožňuje plánování přes nosiče pomocí 3bitového indexu v DCI
- Odděluje místo transmise PDCCH od místa prostředků PDSCH/PUSCH
- Snižuje režii řídicích kanálů a komplexitu blind dekódování UE
- Klíčové pro mitigaci interference v scénářích HetNet a rozšíření dosahu buňky
- Semistaticky konfigurovatelné pomocí signalizace RRC pro UE a skupinu buňek
- Podporuje agregaci nesouvislých spektrálních pásem s různými charakteristikami propagace

## Definující specifikace

- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [CIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cif/)
