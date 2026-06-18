---
slug: "prg"
url: "/mobilnisite/slovnik/prg/"
type: "slovnik"
title: "PRG – Precoding Resource Block Group"
date: 2025-01-01
abbr: "PRG"
fullName: "Precoding Resource Block Group"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prg/"
summary: "Skupina sousedních fyzických bloků zdrojů (PRB) používaná jako granularita pro aplikaci stejné předkódovací matice v 5G NR MIMO přenosech. Optimalizuje režii beamformingu a předkódování tím, že umožňu"
---

PRG je skupina sousedních fyzických bloků zdrojů (PRB), která slouží jako granularita pro aplikaci stejné předkódovací matice v 5G NR MIMO, čímž optimalizuje režii beamformingu a efektivitu signalizace.

## Popis

Precoding Resource Block Group (PRG) je základní koncept ve fyzické vrstvě 5G New Radio (NR), konkrétně v kontextu hlášení informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a předkódování pro vícevstupně-výstupní ([MIMO](/mobilnisite/slovnik/mimo/)) přenosy. V downlinku používá gNB (základnová stanice) předkódování k formování a nasměrování přenosových paprsků k uživatelskému zařízení (UE), čímž optimalizuje kvalitu signálu a propustnost. PRG definuje granularitu, na které lze aplikovat stejnou předkódovací matici na skupinu sousedních fyzických bloků zdrojů ([PRB](/mobilnisite/slovnik/prb/)) ve frekvenční oblasti. Toto seskupení je klíčové, protože podmínky bezdrátového kanálu se mohou s frekvencí měnit; aplikace jedné předkódovací matice na příliš široké pásmo může vést k suboptimálnímu výkonu, zatímco předkódování na úrovni jednotlivých PRB by znamenalo nadměrnou signalizační režii.

Velikost PRG je konfigurovatelná sítí a může být přizpůsobena na základě podmínek kanálu, schopností UE a šířky pásma systému. Specifikace jako 3GPP TS 38.213 a 38.214 definují, jak jsou velikosti PRG signalizovány UE, typicky prostřednictvím konfigurace vyšší vrstvy [RRC](/mobilnisite/slovnik/rrc/) nebo dynamických indikací [DCI](/mobilnisite/slovnik/dci/). UE provádí měření kanálu a hlásí doporučené předkódovací matice (Precoding Matrix Indicators, [PMI](/mobilnisite/slovnik/pmi/)) pro tyto segmenty o velikosti PRG. gNB následně použije tato hlášení k výběru a aplikaci vhodného předkódování napříč určenými PRG. Tento proces umožňuje efektivní uzavřenou smyčku MIMO operací, kde je režie zpětné vazby řízena seskupováním PRB, u kterých se očekávají podobné charakteristiky kanálu.

Z architektonického hlediska PRG interaguje s dalšími komponentami fyzické vrstvy, jako jsou [CSI-RS](/mobilnisite/slovnik/csi-rs/) (Channel State Information Reference Signals) pro odhad kanálu a [PDSCH](/mobilnisite/slovnik/pdsch/) (Physical Downlink Shared Channel) pro přenos dat. Volba velikosti PRG představuje kompromis: větší PRG snižují režii CSI zpětné vazby a složitost předkódování, ale nemusí zachytit jemně rozlišenou frekvenční selektivitu, což může potenciálně degradovat výkon ve vysoce frekvenčně selektivních kanálech. Menší PRG nabízejí přesnější předkódování za cenu vyšší signalizace. V systémech massive MIMO (mMIMO) je efektivní konfigurace PRG zásadní pro využití zisků beamformingu napříč širokými pásmy, jako například v pásmech FR2 (mmWave), kde je správa paprsků kritická.

## K čemu slouží

PRG bylo zavedeno v 5G NR (Release 15) k řešení omezení granularity předkódování v LTE a k podpoře širších šířek pásma a pokročilých MIMO schémat 5G. V LTE se předkódování typicky aplikovalo s granularitou vázanou na subpásma nebo celé systémové pásmo, což mohlo být neefektivní pro větší šířky pásma (až 400 MHz v NR) a rozmanitější scénáře nasazení 5G. Motivací bylo vytvořit flexibilní mechanismus, který vyvažuje kompromis mezi přesností předkódování a signalizační režií, což umožňuje efektivní beamforming a prostorové multiplexování.

Bez PRG by síť čelila dilematu: buď použít jedinou předkódovací matici pro celé pásmo, což vede ke ztrátě výkonu ve frekvenčně selektivních kanálech s úniky, nebo signalizovat informace o předkódování pro každý PRB, což by vedlo k nepřijatelné režii řídicího kanálu. PRG poskytuje střední, konfigurovatelnou granularitu, která umožňuje gNB přizpůsobit se koherenční šířce pásma kanálu. To je obzvláště důležité pro podporu různých případů užití v 5G, od rozšířeného mobilního širokopásmového připojení (eMBB) vyžadujícího vysokou propustnost až po ultra-spolehlivou komunikaci s nízkou latencí (URLLC), která potřebuje robustní adaptaci spojení.

Vytvoření PRG bylo hnací silou potřeby optimalizace operací massive MIMO, kde je přesný beamforming klíčem k kapacitě a pokrytí. Seskupením PRB systém snižuje velikost užitečného zatížení pro CSI zpětnou vazbu (jako PMI a CQI) a signalizaci downlinkového řízení, čímž šetří uplinkové a downlinkové zdroje. Tato efektivita umožňuje škálovatelná nasazení MIMO napříč spektry FR1 (pod 6 GHz) a FR2 (mmWave) a podporuje funkce jako multi-user MIMO (MU-MIMO) a koherentní společný přenos, které jsou základem výkonnostních cílů 5G.

## Klíčové vlastnosti

- Konfigurovatelná granularita pro aplikaci předkódování napříč frekvencí
- Snižuje režii CSI zpětné vazby seskupováním PRB s podobnými podmínkami kanálu
- Podporuje flexibilní adaptaci na koherenční šířku pásma kanálu
- Umožňuje efektivní beamforming pro širokopásmové přenosy 5G NR
- Integruje se s mechanismy hlášení CSI (např. PMI, CQI)
- Usnadňuje škálovatelné operace massive MIMO a MU-MIMO

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/prg/)
