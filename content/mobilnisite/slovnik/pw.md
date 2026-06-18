---
slug: "pw"
url: "/mobilnisite/slovnik/pw/"
type: "slovnik"
title: "PW – Prediction Window"
date: 2025-01-01
abbr: "PW"
fullName: "Prediction Window"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pw/"
summary: "Časový interval nebo vyrovnávací paměť používaná v algoritmech bezdrátové komunikace, zejména pro predikci informace o stavu kanálu (CSI) a adaptaci spojení. Umožňuje síti nebo uživatelskému zařízení"
---

PW (Prediction Window) je časový interval využívaný v bezdrátových algoritmech k predikci budoucích podmínek rádiového kanálu na základě historických dat, což umožňuje proaktivní úpravy vysílacích parametrů pro spolehlivou komunikaci.

## Popis

Prediction Window (PW) je časový koncept používaný v pokročilém řízení rádiových prostředků a zpracování fyzické vrstvy v rámci standardů 3GPP. Odkazuje na definované budoucí časové rozpětí, po které jsou charakteristiky kanálu, jako je síla signálu, interference nebo Dopplerův posuv, předpovídány pomocí prediktivních algoritmů. Toto okno je zásadní pro systémy pracující v dynamickém prostředí, jako jsou scénáře s vysokou mobilitou (např. komunikace s vozidly) nebo rychle se měnící kanály, kde aktuální informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) mohou zastarat v době jejich využití pro plánování nebo adaptaci. PW umožňuje schopnost „pohledu dopředu“, což umožňuje vysílačům a přijímačům proaktivně, nikoli reaktivně, optimalizovat své strategie.

Z architektonického hlediska je PW integrována do funkcí, jako je odhad kanálu, hlášení CSI a moduly adaptace spojení jak v gNB (v 5G) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE), tak v uživatelském zařízení (UE). Klíčové komponenty zahrnují prediktivní algoritmus (např. založený na lineárních prediktorech, Kalmanových filtrech nebo modelech strojového učení), databázi historických CSI použitou pro trénink nebo vstup a řídicí logiku, která aplikuje předpovědi k úpravě vysílacích parametrů. Například při predikci CSI pro Massive [MIMO](/mobilnisite/slovnik/mimo/) může gNB použít minulé CSI reporty od UE k předpovědi matice kanálu na několik následujících milisekund (PW), a podle toho předkódovat downlinkové signály, aby udržel zisk beamformingu. Podobně v uplinku může UE předpovídat svou rezervu výkonu nebo kvalitu kanálu v rámci PW, aby podpořila přístup bez udělení grantu (grant-free) nebo řízení výkonu.

Operačně PW funguje nepřetržitým sledováním měření kanálu (např. [RSRP](/mobilnisite/slovnik/rsrp/), [SINR](/mobilnisite/slovnik/sinr/)) a aplikací analýzy časových řad nebo technik založených na modelech pro extrapolaci budoucích hodnot. Délka PW je konfigurovatelný parametr, který hledá rovnováhu mezi přesností předpovědi (kratší okna jsou obecně přesnější) a potřebou dostatečného předstihu pro implementaci úprav (delší okna umožňují více plánování). Během PW systém může předpočítat modulace a kódová schémata ([MCS](/mobilnisite/slovnik/mcs/)), upravit váhy beamformingu nebo rezervovat prostředky pro zmírnění očekávaného zhoršení. To je zvláště zásadní pro komunikaci s ultra spolehlivým nízkým zpožděním ([URLLC](/mobilnisite/slovnik/urllc/)) a scénáře vysokorychlostních vlaků, kde omezení latence neumožňují čekat na aktualizovaná měření. Úlohou PW je zvýšit spektrální účinnost a spolehlivost snížením nesouladu mezi skutečnými podmínkami kanálu a podmínkami předpokládanými při rozhodování o vysílání.

## K čemu slouží

Prediction Window existuje za účelem překonání inherentní latence a zpoždění zpětné vazby v bezdrátových systémech, které mohou při rychlé změně podmínek kanálu vést ke zhoršení výkonu. Tradiční adaptace spojení a plánování spoléhají na [CSI](/mobilnisite/slovnik/csi/) reporty odrážející minulé stavy; v době, kdy k vysílání dojde, se kanál mohl změnit, což vede k suboptimálnímu výběru MCS, zvýšené chybovosti bloků nebo plýtvání prostředky. PW řeší tento problém tím, že umožňuje prediktivní řízení, čímž umožňuje systému „nahlédnout do blízké budoucnosti“ a činit informovanější rozhodnutí, což zlepšuje propustnost a spolehlivost, zejména v aplikacích s vysokou mobilitou nebo náročných na čas.

Z historického hlediska, jak se 3GPP vyvíjelo z LTE na 5G, požadavky na vyšší přenosové rychlosti, nižší latenci a podporu vozidel a průmyslového IoT poháněly potřebu pokročilejších prediktivních technik. Starší verze používaly jednodušší, reaktivní metody s pevnými rezervami, které byly při rychlém útlumu neefektivní. Zavedení konceptů PW, zejména od verze Rel-15 s 5G NR, bylo motivováno potřebou podporovat rozšířené mobilní širokopásmové připojení (eMBB) a URLLC v náročných prostředích. Řeší omezení způsobená zpožděnou zpětnou vazbou CSI integrací predikce do standardů, jako jsou vylepšení hlášení CSI a uplink bez grantu (grant-free), což umožňuje proaktivní přidělování prostředků a snižuje opakované přenosy. To je v souladu s cíli 5G v oblasti síťové inteligence a automatizace, kde se prediktivní analytika stává klíčem k udržování QoS v dynamických rádiových podmínkách.

## Klíčové vlastnosti

- Umožňuje proaktivní adaptaci spojení a plánování na základě předpovědi kanálu
- Konfigurovatelná časová délka, která vyvažuje přesnost a předstih potřebný pro úpravy
- Integruje se s algoritmy predikce CSI pro Massive MIMO a správu beamformingových svazků
- Podporuje scénáře s vysokou mobilitou, jako jsou komunikace s vozidly a vysokorychlostní vlaky
- Snižuje dopad latence ze zpoždění zpětné vazby CSI tím, že předvídá změny
- Zvyšuje spolehlivost a spektrální účinnost pro služby URLLC a eMBB

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 38.744** (Rel-19) — AI/ML for NR Mobility Study

---

📖 **Anglický originál a plná specifikace:** [PW na 3GPP Explorer](https://3gpp-explorer.com/glossary/pw/)
