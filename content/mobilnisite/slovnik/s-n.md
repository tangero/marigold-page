---
slug: "s-n"
url: "/mobilnisite/slovnik/s-n/"
type: "slovnik"
title: "S/N – Signal to Noise Ratio"
date: 2025-01-01
abbr: "S/N"
fullName: "Signal to Noise Ratio"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/s-n/"
summary: "Poměr signálu k šumu (Signal to Noise Ratio, S/N nebo SNR) je základní metrika v telekomunikacích, která měří sílu užitečného signálu vzhledem k úrovni šumu na pozadí. Je klíčovým faktorem pro kvalitu"
---

S/N je základní metrika, která měří sílu užitečného signálu vzhledem k úrovni šumu na pozadí v telekomunikačním spoji.

## Popis

Poměr signálu k šumu (Signal to Noise Ratio, S/N nebo [SNR](/mobilnisite/slovnik/snr/)) je bezrozměrná kvantitativní míra hojně využívaná v bezdrátových i kabelových komunikačních systémech k posouzení kvality přijímaného signálu. Je definován jako poměr výkonu smysluplného signálu („signál“) k výkonu šumu na pozadí a rušení („šum“) přítomnému v systému, a je typicky vyjadřován v decibelech (dB). Matematicky SNR (dB) = 10 * log10(Psignal / Pnoise). Vyšší SNR indikuje čistší a silnější signál vzhledem k šumovému prahu, což umožňuje použití složitějších modulačních schémat (např. 256-QAM oproti [QPSK](/mobilnisite/slovnik/qpsk/)) a vyšších kódovacích rychlostí, čímž se zvyšuje spektrální účinnost a dosažitelná datová propustnost. Naopak nízké SNR nutí systém používat robustní, ale méně účinnou modulaci a kódování, což snižuje přenosové rychlosti za účelem zachování spolehlivého spojení.

V kontextu systémů 3GPP ([UTRAN](/mobilnisite/slovnik/utran/), [E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN) je SNR kritickým měřením fyzické vrstvy prováděným uživatelským zařízením (UE) a základnovou stanicí (NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB). UE neustále měří výkon referenčního signálu (např. Cell-Specific Reference Signal v LTE, Synchronization Signal Block v NR) a odhaduje výkon šumu v šířce přenosového pásma. Toto změřené SNR, často hlášené jako indikátor kvality kanálu (Channel Quality Indicator, [CQI](/mobilnisite/slovnik/cqi/)), je zasíláno zpět do sítě. Plánovač sítě využívá tuto zpětnou vazbu CQI, která je odvozena od SNR, k rozhodování o adaptivní modulaci a kódování (Adaptive Modulation and Coding, [AMC](/mobilnisite/slovnik/amc/)). Vybere nejúčinnější modulační a kódovací schéma (Modulation and Coding Scheme, [MCS](/mobilnisite/slovnik/mcs/)), které může být za daných podmínek kanálu úspěšně dekódováno UE, čímž optimalizuje kompromis mezi přenosovou rychlostí a mírou chybovosti bloků (Block Error Rate, BLER).

Role SNR přesahuje adaptaci spoje. Je základním vstupem pro procedury správy rádiových prostředků (Radio Resource Management, RRM), jako je předávání spojení (handover) a výběr/převýběr buňky. Například UE používá měření síly signálu (Reference Signal Received Power, RSRP) a kvality (Reference Signal Received Quality, RSRQ, na kterou má SNR vliv) k rozhodnutí, kdy se předat do sousední buňky. V systémech s masivním MIMO a beamformingem v 5G NR se měření SNR na různých paprscích používá k výběru optimálního paprsku pro přenos. Dále pokročilé techniky jako hybridní automatické opakování žádosti (Hybrid Automatic Repeat Request, HARQ) a výpočty rozpočtu útlumu pro plánování sítě se všechny opírají o pochopení charakteristik SNR rádiového spoje. SNR je primárním fyzikálním omezením, které Shannonova věta o kapacitě kanálu přímo spojuje s maximální možnou rychlostí přenosu dat bez chyb v komunikačním kanálu.

## K čemu slouží

SNR existuje jako základní koncept, protože všechny reálné komunikační kanály jsou degradovány šumem, což je nevyhnutelný fyzikální jev vznikající z tepelného pohybu elektronů v vodičích, kosmického záření a umělého rušení. Základním problémem telekomunikací je spolehlivě přenášet informace za přítomnosti tohoto šumu. Před digitální komunikací bylo SNR klíčové pro analogové systémy (jako FM rádio) k určení přijatelné kvality poslechu. S příchodem digitálních systémů se SNR stalo klíčovým parametrem, který určuje dosažitelnou míru bitových chyb (Bit Error Rate, BER) pro dané modulační schéma, jak popisují teoretické modely jako křivky BER v závislosti na Eb/N0.

Motivací pro neustálé měření a optimalizaci SNR v systémech 3GPP je maximalizace spektrální účinnosti – počtu bitů přenesených za sekundu na hertz šířky pásma – což je vzácný a drahý zdroj. Rané celulární systémy používaly pevnou modulaci, která byla neefektivní při změně podmínek kanálu. Zavedení adaptivní modulace a kódování (Adaptive Modulation and Coding, AMC), které závisí na zpětné vazbě SNR, byl revoluční krok, který umožnil systémům dynamicky přizpůsobovat přenosové parametry aktuální kvalitě kanálu. Tím se přímo řeší časově proměnná a na umístění závislá povaha bezdrátového kanálu, čímž se odstraňuje problém plýtvání kapacitou (použití příliš robustního schématu za dobrých podmínek) nebo vysoké chybovosti (použití příliš agresivního schématu za špatných podmínek).

Navíc, jak se standardy 3GPP vyvíjely směrem k modulacím vyšších řádů (až po 1024-QAM v 5G NR) pro zvýšení přenosových rychlostí, se požadované prahové hodnoty SNR zpřísnily. Řízení SNR je proto ústředním prvkem pro umožnění těchto pokročilých funkcí. Techniky jako koordinace rušení (Inter-Cell Interference Coordination, ICIC; enhanced ICIC, eICIC), pokročilé anténní systémy (beamforming) a agregace nosných byly vyvinuty částečně za účelem zlepšení efektivního SNR, které zažívají uživatelé. V podstatě celý vývoj technologie fyzické vrstvy v celulárních standardech je příběhem vývoje metod pro dosažení vyššího a stabilnějšího SNR, které odemyká vyšší kapacitu kanálu a lepší uživatelský zážitek.

## Klíčové vlastnosti

- Základní metrika definující kvalitu přijímaného signálu jako poměr výkonu signálu k výkonu šumu
- Přímo určuje použitelné modulační a kódovací schéma (MCS) a spektrální účinnost
- Měřeno UE a základnovou stanicí, často hlášeno jako zpětná vazba indikátoru kvality kanálu (CQI)
- Klíčový vstup pro algoritmy adaptivní modulace a kódování (AMC) a adaptace spoje
- Ovlivňuje rozhodování správy rádiových prostředků, jako je předání spojení a výběr paprsku
- Tvoří základ teoretických limitů kapacity kanálu definovaných Shannonovou větou

## Definující specifikace

- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements

---

📖 **Anglický originál a plná specifikace:** [S/N na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-n/)
