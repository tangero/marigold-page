---
slug: "mr-acelp"
url: "/mobilnisite/slovnik/mr-acelp/"
type: "slovnik"
title: "MR-ACELP – Multi-Rate Algebraic Code-Excited Linear Prediction"
date: 2025-01-01
abbr: "MR-ACELP"
fullName: "Multi-Rate Algebraic Code-Excited Linear Prediction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mr-acelp/"
summary: "MR-ACELP je vícerychlostní hlasový kodek definovaný organizací 3GPP, založený na algoritmu Algebraic Code-Excited Linear Prediction (ACELP). Umožňuje efektivní kompresi řeči s proměnnou přenosovou ryc"
---

MR-ACELP je vícerychlostní hlasový kodek založený na algoritmu ACELP, který umožňuje efektivní kompresi řeči s proměnnou přenosovou rychlostí za účelem optimalizace hlasové kvality a využití šířky pásma v mobilních sítích 3GPP.

## Popis

Multi-Rate Algebraic Code-Excited Linear Prediction (MR-ACELP) je standard pro kódování řeči specifikovaný organizací 3GPP pro digitální přenos hlasu v celulárních sítích. Funguje na principu Algebraic Code-Excited Linear Prediction, což je sofistikovaný algoritmus modelující lidský hlasový trakt za účelem komprese řečových signálů. Kodek podporuje více přenosových rychlostí, což mu umožňuje dynamicky upravovat kódovací rychlost na základě faktorů, jako je síťová kongesce, kvalita kanálu a požadavky služby. Tato přizpůsobivost je dosažena prostřednictvím struktury s proměnnou rychlostí, kde enkodér může vybírat z předdefinovaných přenosových rychlostí (např. od nižších rychlostí pro efektivní využití šířky pásma po vyšší rychlosti pro lepší hlasovou kvalitu). Technická implementace zahrnuje lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)) pro odhad spektrálních parametrů v kombinaci s algebraickým kodebookem pro reprezentaci excitačního signálu, což vede k vysoce kvalitní reprodukci řeči při snížených datových rychlostech.

Z architektonického hlediska je MR-ACELP integrován do řetězce zpracování hlasu v uživatelském zařízení (UE) a síťových prvcích, jako je Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo uzly IP Multimedia Subsystem (IMS). Funguje ve vrstvě hlasového kodeku protokolového zásobníku, rozhraní s transportními vrstvami pro paketizaci ve scénářích VoIP nebo s okruhově přepínanými přenosovými cestami v legacy systémech. Klíčové komponenty zahrnují enkodér, který převádí analogové řečové signály na komprimované digitální rámce, a dekodér, který řeč na přijímací straně rekonstruuje. Kodek využívá techniky jako detekce hlasové aktivity (VAD) a generování komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) k další optimalizaci šířky pásma během období ticha, čímž zvyšuje celkovou efektivitu sítě.

Jeho role v síti je klíčová pro poskytování hlasových služeb, včetně tradičních okruhově přepínaných hovorů a Voice over LTE (VoLTE) nebo Voice over NR (VoNR). MR-ACELP zajišťuje konzistentní hlasovou kvalitu za různých rádiových podmínek přizpůsobováním přenosové rychlosti, čímž vyvažuje srozumitelnost a využití zdrojů. Podporuje interoperabilitu mezi různými generacemi sítí a výrobci zařízení díky dodržování specifikací 3GPP. Kodek také umožňuje funkce jako tandem-free operation (TFO) a transcoder-free operation (TrFO), které snižují degradaci kvality způsobenou vícenásobnými fázemi kódování a dekódování v koncových hovorech.

## K čemu slouží

MR-ACELP byl vyvinut k řešení omezení hlasových kodeků s pevnou přenosovou rychlostí v mobilních sítích, které se nemohly efektivně přizpůsobovat měnícím se síťovým podmínkám a dostupné šířce pásma. Předchozí kodeky, jako například full-rate nebo enhanced full-rate kodeky v sítích 2G/3G, pracovaly s konstantní přenosovou rychlostí, což vedlo buď k nadměrné spotřebě šířky pásma, nebo ke špatné hlasové kvalitě při omezeních. Vícerychlostní schopnost MR-ACELP tento problém řeší tím, že umožňuje dynamické přizpůsobení, optimalizující jak kvalitu, tak spektrální efektivitu, což je klíčové pro podporu rostoucího hlasového provozu a přechodu na paketově přepínané sítě.

Historicky vývoj směrem k sítím 3G a 4G kladl důraz na datovou efektivitu a kvalitu služby (QoS) pro multimediální aplikace. Vytvoření MR-ACELP bylo motivováno potřebou univerzálního hlasového kodeku, který by mohl fungovat napříč okruhově i paketově přepínanými doménami, což by umožnilo bezproblémové hlasové služby v LTE a dalších sítích. Řeší problémy jako síťová kongesce a proměnlivé podmínky kanálu snížením přenosové rychlosti při špatném spojení bez výrazné ztráty kvality, čímž zlepšuje uživatelský zážitek a kapacitu sítě.

MR-ACELP navíc podporuje snahu průmyslu o vyšší standardy hlasové kvality a interoperabilitu. Standardizací vícerychlostního kodeku založeného na [ACELP](/mobilnisite/slovnik/acelp/) zajistila organizace 3GPP, aby mohli mobilní operátoři nasazovat efektivní hlasové služby při zachování zpětné kompatibility a usnadnění globálního roamingu. Tento kodek také položil základy pro pokročilé hlasové funkce v 5G, jako jsou enhanced voice services ([EVS](/mobilnisite/slovnik/evs/)), tím, že demonstroval výhody adaptivního řízení rychlosti a robustních kompresních algoritmů.

## Klíčové vlastnosti

- Provoz s proměnnou přenosovou rychlostí pro adaptivní kompresi řeči
- Založen na algoritmu Algebraic Code-Excited Linear Prediction (ACELP)
- Podporuje více předdefinovaných kódovacích rychlostí pro flexibilitu
- Integruje detekci hlasové aktivity a generování komfortního šumu
- Umožňuje tandem-free a transcoder-free operaci pro zachování kvality
- Soulad se specifikacemi 3GPP pro interoperabilitu

## Související pojmy

- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [MR-ACELP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mr-acelp/)
