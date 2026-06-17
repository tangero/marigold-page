---
slug: "fsk"
url: "/mobilnisite/slovnik/fsk/"
type: "slovnik"
title: "FSK – Frequency-Shift Keying"
date: 2025-01-01
abbr: "FSK"
fullName: "Frequency-Shift Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fsk/"
summary: "Digitální modulační schéma, při kterém je informace kódována změnou frekvence nosné vlny. Jedná se o základní, robustní techniku používanou pro přenosy s nízkou přenosovou rychlostí a vysokou energeti"
---

FSK je digitální modulační schéma, při kterém je informace kódována změnou frekvence nosné vlny; používá se pro robustní přenosy s nízkou přenosovou rychlostí v celulárních a IoT systémech.

## Popis

Frekvenční manipulace (FSK) je forma frekvenční modulace, při které se okamžitá frekvence nosného signálu přepíná mezi diskrétními hodnotami, aby reprezentovala digitální data. Ve své nejjednodušší binární podobě, binární FSK (BFSK), jedna frekvence (f1) reprezentuje binární '1' a druhá frekvence (f2) reprezentuje binární '0'. Přechod mezi těmito frekvencemi je řízen základovým pásmovým digitálním signálem. Modulační index, definovaný jako poměr špičkové frekvenční odchylky k modulující frekvenci základního pásma, určuje spektrální charakteristiky a výkon. Modulační index 0,5, známý jako minimální frekvenční manipulace ([MSK](/mobilnisite/slovnik/msk/)), je specifická, spektrálně účinná forma FSK s kontinuální fází (CPFSK), která minimalizuje postranní spektrální laloky a umožňuje přenos s konstantní obálkou.

Demodulace FSK může být prováděna koherentními nebo nekoherentními metodami. Koherentní detekce vyžaduje, aby přijímač měl přesnou znalost fáze nosné, typicky využívá fázově závěsnou smyčku (PLL) pro regeneraci nosné, a koreluje přijímaný signál s lokálně generovanými referenčními signály na frekvencích f1 a f2. Nekoherentní detekce, například pomocí diskriminátoru nebo přizpůsobených filtrů následovaných detektorem obálky, je jednodušší, protože nevyžaduje obnovu fáze nosné, což ji činí vhodnější pro prostředí s fázovým šumem nebo frekvenční nestabilitou, i za cenu mírného snížení výkonu. Klíčovou metrikou výkonu je chybovost bitů ([BER](/mobilnisite/slovnik/ber/)), která pro kanály s aditivním bílým Gaussovským šumem ([AWGN](/mobilnisite/slovnik/awgn/)) závisí na poměru energie na bit k spektrální hustotě výkonu šumu (Eb/N0) a na vzdálenosti mezi signálovými frekvencemi.

V systémech 3GPP byla primární role FKS v ultra-spolehlivých, nízkopříkonových a nízkosložitostních komunikačních spojích. Její vlastnost konstantní obálky je velmi výhodná pro energeticky účinné zesilování, protože umožňuje použití nelineárních, vysoce účinných výkonových zesilovačů (PA) bez výrazného zkreslení signálu. To z ní učinilo kandidáta pro specifické fyzické vrstvové kanály v raných vydáních a později pro IoT technologie. Například v Narrowband IoT (NB-IoT), specifikovaném od vydání 13, je pro uplink použita forma diferenciální [BPSK](/mobilnisite/slovnik/bpsk/)/π/2-BPSK modulace, ale principy jednoduché, robustní modulace podobné FSK byly ústřední pro filozofii návrhu zaměřenou na extrémní pokrytí a životnost baterie zařízení. Specifikace 3GPP popisující FSK, jako jsou TS 38.848 a TS 38.869, ji často zmiňují v kontextu studijních položek, požadavků na výkon a testů koexistence pro nové technologie radiového přístupu, aby bylo zajištěno, že její spektrální vlastnosti nezpůsobí škodlivé rušení jiným systémům.

## K čemu slouží

FSK byla vyvinuta jako základní digitální modulační technika, která poskytuje robustní a jednoduchou metodu pro přenos digitálních dat přes analogové kanály. Jejím primárním účelem je umožnit spolehlivou komunikaci v přítomnosti šumu a poruch kanálu, zejména tam, kde musí být minimalizována složitost přijímače nebo spotřeba energie. Než se rozšířily spektrálně účinnější, ale složitější modulace jako QAM, nabízela FSK dobrou rovnováhu mezi výkonem, náklady na implementaci a odolností vůči nelineárnímu zkreslení ve stupni výkonového zesilovače vysílače.

Historická motivace pro její zařazení do telekomunikačních standardů pramení z jejího vynikajícího výkonu v podmínkách nízkého poměru signál-šum (SNR) a její vnitřní odolnosti vůči šumu ve srovnání s amplitudovou manipulací (ASK). Její charakteristika konstantní obálky řeší problém spektrálního nárůstu a neúčinnosti při použití nelineárních výkonových zesilovačů, což bylo klíčové pro rané mobilní telefony a základnové stanice, kde účinnost zesilovače přímo ovlivňovala životnost baterie a provozní náklady. Zatímco pozdější systémy 3GPP přijaly modulace vyšších řádů pro špičkové přenosové rychlosti, potřeba extrémně spolehlivých, nízkopříkonových spojů pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) oživila zájem o jednoduchost podobnou FSK.

V kontextu vývoje 3GPP řešila FSK omezení složitějších modulačních schémat, která vyžadují vysokou linearitu, přesnou synchronizaci a významné zpracování signálu. Pro specifické případy použití, jako je hluboké vnitřní pokrytí, senzorové sítě a zařízení s ultra-nízkými náklady, jsou tyto požadavky nepřijatelné. FSK poskytuje osvědčenou, nízkosložitostní alternativu, která zajišťuje, že základní konektivita může být zachována i v nejnáročnějších podmínkách, naplňující tak pilíř 'pokrytí' požadavků IoT spolu s latencí a cenou zařízení.

## Klíčové vlastnosti

- Přenos s konstantní obálkou umožňující účinné nelineární výkonové zesílení
- Robustní výkon v prostředích s nízkým poměrem signál-šum (SNR)
- Podpora koherentních i nekoherentních metod demodulace
- Spektrální účinnost může být optimalizována variantami s kontinuální fází, jako je MSK
- Nízká implementační složitost pro vysílače i přijímače
- Efektivní odolnost vůči určitým typům šumu a rušení

## Související pojmy

- [BPSK – Binary Phase Shift Keying](/mobilnisite/slovnik/bpsk/)
- [MSK – Minimum-shift keying](/mobilnisite/slovnik/msk/)

## Definující specifikace

- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TR 38.848** (Rel-18) — Technical Report on Ambient IoT
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [FSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsk/)
