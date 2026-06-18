---
slug: "pcfich"
url: "/mobilnisite/slovnik/pcfich/"
type: "slovnik"
title: "PCFICH – Physical Control Format Indicator Channel"
date: 2025-01-01
abbr: "PCFICH"
fullName: "Physical Control Format Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pcfich/"
summary: "Downlinkový fyzický kanál v LTE a NR, který přenáší indikátor formátu řízení (Control Format Indicator, CFI), udávající počet OFDM symbolů využitých pro PDCCH v subrámci. Je klíčový pro to, aby uživat"
---

PCFICH je kanál pro indikaci formátu fyzického řídicího kanálu (Physical Control Format Indicator Channel), což je downlinkový kanál v LTE a NR, který přenáší CFI, aby indikoval počet OFDM symbolů využitých pro PDCCH v subrámci.

## Popis

Kanál pro indikaci formátu fyzického řídicího kanálu (Physical Control Format Indicator Channel, PCFICH) je základní downlinkový fyzický kanál zavedený v LTE a přenesený do NR. Je vysílán v prvním [OFDM](/mobilnisite/slovnik/ofdm/) symbolu každého downlinkového subrámce a je vždy přítomen, bez ohledu na to, zda je subrámec využit pro přenos dat či nikoliv. PCFICH přenáší indikátor formátu řízení (Control Format Indicator, [CFI](/mobilnisite/slovnik/cfi/)), což je hodnota signalizující počet OFDM symbolů (typicky 1, 2 nebo 3, a v některých konfiguracích NR rozšířených na 4) přidělených pro fyzický downlinkový řídicí kanál (Physical Downlink Control Channel, [PDCCH](/mobilnisite/slovnik/pdcch/)) v daném konkrétním subrámci. Tato informace je zásadní pro to, aby uživatelské zařízení (UE) mohlo správně zpracovat řídicí oblast subrámce.

Fungování PCFICH zahrnuje specifické mapování zdrojů. Hodnota CFI (1-4) je zakódována do 32bitového kódového slova pomocí (32, 2) blokového kódu. Toto kódové slovo je následně modulováno kvadraturní fázovou modulací (Quadrature Phase Shift Keying, [QPSK](/mobilnisite/slovnik/qpsk/)), což vede k 16 komplexním modulačním symbolům. Tyto symboly jsou namapovány na 16 prvků zdrojů (resource elements, [RE](/mobilnisite/slovnik/re/)), které jsou rozloženy přes systémovou šířku pásma. Mapování následuje specifický vzor, který rozděluje 16 RE do čtyř skupin, z nichž každá obsahuje čtyři prvky zdrojů. Tyto skupiny jsou rozmístěny přibližně rovnoměrně napříč frekvenční doménou v rámci prvního OFDM symbolu, aby bylo dosaženo frekvenční diverzity a robustního příjmu i při útlumech.

Při příjmu subrámce musí UE nejprve slepě detekovat a dekódovat PCFICH, aby určilo CFI. Tento počáteční krok je kritický, protože velikost řídicí oblasti (PDCCH) je proměnná a mění se pro každý subrámec na základě vytížení provozu a rozhodnutí plánovače. Bez správného dekódování PCFICH nemůže UE vědět, kde PDCCH končí a kde začíná oblast fyzického downlinkového sdíleného kanálu (Physical Downlink Shared Channel, [PDSCH](/mobilnisite/slovnik/pdsch/)), což vede k selhání příjmu downlinkové řídicí informace (Downlink Control Information, [DCI](/mobilnisite/slovnik/dci/)) a následně i downlinkových dat. Konstrukce PCFICH upřednostňuje robustnost; jeho vysílací výkon je často zvýšený ve srovnání s jinými kanály a jeho distribuované mapování zdrojů poskytuje inherentní frekvenční diverzitu, aby byl zajištěn spolehlivý příjem i na okraji buňky.

V síťové architektuře je PCFICH generován a vysílán eNodeB v LTE nebo gNB v NR. Jeho hodnota je určena plánovačem na základě okamžité potřeby řídicí signalizace. Vyšší hodnota CFI přiděluje více zdrojů pro PDCCH, což umožňuje naplánovat více UE nebo přenést složitější formáty DCI v rámci daného subrámce. Naopak nižší hodnota CFI minimalizuje režii řízení a uvolňuje více zdrojů pro přenos uživatelských dat na PDSCH. PCFICH tedy funguje jako dynamický ukazatel, který umožňuje flexibilní a efektivní využití časově-frekvenční mřížky.

## K čemu slouží

PCFICH byl vytvořen, aby vyřešil základní problém v systémech založených na [OFDMA](/mobilnisite/slovnik/ofdma/), jako jsou LTE a NR: dynamickou a proměnnou velikost řídicí oblasti. V dřívějších celulárních systémech byla struktura řídicího kanálu často pevná nebo polostatická, což mohlo vést k neefektivitě. Pokud by byla řídicí oblast dimenzována pro špičkové zatížení, plýtvala by zdroji během období nízkého provozu. Pokud by byla dimenzována pro průměrné zatížení, mohla by se stát úzkým hrdlem během scénářů s vysokým provozem, což by omezovalo kapacitu plánování.

Zavedení PCFICH umožnilo přizpůsobení řídicí oblasti na úrovni každého subrámce. Tato dynamická alokace byla klíčovou inovací pro efektivitu LTE. Umožňuje síti přesně přizpůsobit alokaci řídicích zdrojů okamžitým požadavkům plánování. Tato flexibilita je zásadní pro podporu funkcí, jako je víceuživatelský MIMO, agregace nosných a pokročilé zpracování QoS, kde se množství potřebné řídicí signalizace může výrazně měnit z jedné milisekundy na druhou.

Navíc tím, že explicitně signalizuje velikost řídicí oblasti na vyhrazeném, robustním kanálu, PCFICH zjednodušuje konstrukci přijímače UE. UE nemusí slepě hledat hranici PDCCH; má jasný, spolehlivě dekódovatelný indikátor. Tím se snižuje složitost UE a spotřeba baterie a zároveň je zajištěn spolehlivý provoz systému. PCFICH je tedy malým, ale kritickým prvkem, který umožňuje vysokou spektrální účinnost a flexibilitu plánování, jež definují moderní 4G a 5G rádiové přístupové sítě.

## Klíčové vlastnosti

- Přenáší indikátor formátu řízení (Control Format Indicator, CFI) definující délku PDCCH (1-4 OFDM symbolů)
- Je vysílán v prvním OFDM symbolu každého downlinkového subrámce
- Pro robustnost používá pevné 32bitové kódování a QPSK modulaci
- Prvky zdrojů (RE) jsou rozloženy napříč frekvencí pro zisk diverzity
- Umožňuje dynamické přizpůsobení režie řízení pro každý subrámec
- Je zásadní pro to, aby UE mohlo správně lokalizovat oblasti PDCCH a PDSCH

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [CFI – Control Format Indicator](/mobilnisite/slovnik/cfi/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TR 36.976** (Rel-19) — LTE-based 5G Terrestrial Broadcast Overview
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PCFICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcfich/)
