---
slug: "tx"
url: "/mobilnisite/slovnik/tx/"
type: "slovnik"
title: "TX – Transmit Diversity"
date: 2025-01-01
abbr: "TX"
fullName: "Transmit Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tx/"
summary: "TX, neboli Transmit Diversity (diverzita při vysílání), je základní technika rádiového přenosu používaná v systémech 3GPP ke zlepšení spolehlivosti signálu a potlačení útlumu vysíláním stejného signál"
---

TX je základní technika rádiového přenosu v systémech 3GPP, která zlepšuje spolehlivost signálu a bojuje proti útlumu vysíláním stejného signálu přes více antén za účelem zvýšení pokrytí na downlinku a integrity dat.

## Popis

Transmit Diversity (TX) je technika prostorové diverzity uplatňovaná na straně vysílače (typicky základnové stanice, např. gNB nebo eNodeB) v bezdrátových komunikačních systémech. Jejím základním principem je vysílání více kopií stejného informačního signálu prostřednictvím dvou nebo více geograficky oddělených nebo ortogonálně polarizovaných antén. Tyto vícečetné přenosové cesty, neboli větve, zažívají nezávislé podmínky útlumu. Díky využití statistické nezávislosti útlumu na těchto cestách se výrazně snižuje pravděpodobnost, že všechny kopie signálu budou současně degradovány hlubokým útlumem, čímž se zvyšuje spolehlivost signálu přijímaného uživatelským zařízením (UE).

Ve standardech 3GPP bylo definováno a v průběhu releasů vyvinuto několik konkrétních schémat diverzity při vysílání. Základním schématem je Space-Frequency Block Coding (SFBC), široce používaný v LTE a 5G NR pro dvě vysílací antény. V SFBC jsou páry modulačních symbolů kódovány přes dva sousední subnosné a dvě vysílací antény za použití ortogonálního kódu založeného na Alamoutiho algoritmu. Tím vzniká strukturovaná redundance, která přijímači umožňuje kombinovat signály z obou antén tak, že obnoví původní symboly, i když je signál z jedné antény utlumen. Pro čtyři vysílací antény se používají kombinace jako SFBC spojený s Frequency Switched Transmit Diversity (FSTD) nebo Time Switched Transmit Diversity ([TSTD](/mobilnisite/slovnik/tstd/)), aby byla zachována ortogonalita a říditelná složitost přijímače.

Implementace zahrnuje zpracování na fyzické vrstvě základnové stanice. Po kanálovém kódování a modulaci je proud symbolů veden do kodéru diverzity při vysílání, který mapuje symboly na konkrétní resource elementy na různých anténních portech podle zvoleného schématu. Tyto anténní porty jsou logické entity, které po dalším precódování mohou odpovídat fyzickým anténám. Přijímač (UE), který typicky používá jednu nebo více přijímacích antén, používá odpovídající kombinační algoritmus, jako je Maximum Ratio Combining ([MRC](/mobilnisite/slovnik/mrc/)), k optimálnímu sloučení signálů z různých vysílacích cest. Tento proces kombinace efektivně zvyšuje přijímaný poměr signál-šum ([SNR](/mobilnisite/slovnik/snr/)) a zmírňuje dopad vícecestného útlumu.

Diverzita při vysílání je klíčovou součástí rodiny technologie Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)), konkrétně spadá do kategorie open-loop MIMO, kde vysílač nevyžaduje informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). Její role je nejkritičtější pro řídicí kanály a broadcastové kanály (např. Physical Broadcast Channel - [PBCH](/mobilnisite/slovnik/pbch/), Physical Downlink Control Channel - [PDCCH](/mobilnisite/slovnik/pdcch/)), kde je spolehlivost prvořadá, a pro uživatelská zařízení ve scénářích s vysokou mobilitou nebo na okrajích buňky, kde může být zpětná vazba o kanálu nespolehlivá. Tvoří základnu pro robustní přenos, než mohou být aplikovány pokročilejší, na kapacitu orientované techniky, jako je prostorové multiplexování.

## K čemu slouží

Diverzita při vysílání byla zavedena, aby řešila základní problém útlumu signálu v mobilních bezdrátových kanálech bez nutnosti dodatečných přijímacích antén na uživatelském terminálu. V raných buněčných systémech byly diverzitní techniky primárně implementovány na straně přijímače (např. použitím více antén na základnové stanici pro přijímací diverzitu). Vybavení každého mobilního telefonu více anténami pro přijímací diverzitu však bylo nepraktické kvůli omezením nákladů, velikosti a výkonu. Diverzita při vysílání poskytla elegantní řešení přesunutím složitosti a vícečetných antén na stranu sítě (základnové stanice), kde jsou takové zdroje snáze dostupné.

Primárním problémem, který řeší, je zlepšení pokrytí na downlinku a spolehlivosti spojení, zejména pro malá ruční zařízení. Vysíláním redundantních signálů přes prostorově diverzní cesty potlačuje účinky Rayleighova útlumu a stínování, které mohou způsobit výrazné poklesy signálu. To vede ke konzistentnější kvalitě služby, snižuje potřebný vysílací výkon na okraji buňky pro daný výkonnostní cíl a snižuje míru ztráty hovoru. Byla klíčovou enabling technologií pro poskytování spolehlivých vysokorychlostních datových služeb ve 3G ([WCDMA](/mobilnisite/slovnik/wcdma/)) a stala se základním kamenem návrhu fyzické vrstvy LTE a NR.

Historicky její přijetí v 3GPP začalo s Release 99 (WCDMA) s použitím technik jako Space-Time Transmit Diversity (STTD). Jejím motivem bylo zvýšení kapacity downlinku a pokrytí pro datové služby. V LTE (Rel-8) a novějších se stala povinnou pro určité downlinkové kanály, aby byla zajištěna robustní činnost systému. Řešila omezení přenosu s jednou anténou, který byl vysoce náchylný na změny kanálu, a poskytla výkonnostní základnu, která umožnila síťovým operátorům garantovat spolehlivost služby i v neideálních rádiových podmínkách, čímž připravila cestu pro adaptivní použití spektrálně efektivnějších, ale méně robustních technik.

## Klíčové vlastnosti

- Zlepšuje spolehlivost spojení a potlačuje vícecestný útlum bez navyšování vysílacího výkonu
- Implementována jako open-loop operace, nevyžadující zpětnou vazbu o stavu kanálu od UE
- Používá ortogonální kódovací schémata (např. SFBC, Alamoutiho kód) umožňující jednoduché lineární dekódování na přijímači
- Primárně aplikována na kritické downlinkové řídicí a broadcastové kanály pro zaručenou robustnost
- Podporuje konfigurace pro 2 a 4 vysílací anténní porty na základnové stanici
- Zvyšuje pokrytí, zejména na okrajích buňky, a podporuje scénáře s vysokou mobilitou

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description

---

📖 **Anglický originál a plná specifikace:** [TX na 3GPP Explorer](https://3gpp-explorer.com/glossary/tx/)
