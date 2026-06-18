---
slug: "cho"
url: "/mobilnisite/slovnik/cho/"
type: "slovnik"
title: "CHO – Conditional Handover"
date: 2026-01-01
abbr: "CHO"
fullName: "Conditional Handover"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cho/"
summary: "Procedura předání spojení, kde probíhá příprava předem, ale provedení je podmíněno splněním specifických rádiových podmínek na straně UE. Zvyšuje spolehlivost předání a snižuje selhání v náročných mob"
---

CHO (Conditional Handover) je procedura předání spojení, při níž je příprava provedena předem, ale samotné provedení nastane pouze tehdy, pokud jsou na straně UE splněny specifické rádiové podmínky, což zvyšuje spolehlivost v náročných mobilních scénářích.

## Popis

Conditional Handover (CHO) je pokročilý mobilní postup zavedený ve specifikaci 3GPP Release 16 za účelem zvýšení robustnosti předání spojení, zejména ve scénářích s vysokou mobilitou a vysokými kmitočty (např. pásmo mmWave), které jsou náchylné k výpadkům rádiového spoje. Na rozdíl od konvenčních předání, která jsou nařízena sítí a provedena okamžitě, CHO odděluje fázi přípravy předání od fáze provedení. Obsluhující gNB (nebo ng-eNB) předem připraví jednu nebo více kandidátních cílových buněk provedením řízení přístupu (admission control) a rezervací prostředků. Poté poskytne UE konfiguraci CHO obsahující identifikace těchto kandidátních buněk a sadu podmínek provedení, typicky založených na rádiových měřeních (např. události [A3](/mobilnisite/slovnik/a3/)/A5 s posuny a časem do spuštění). UE tuto konfiguraci uloží a průběžně monitoruje rádiové podmínky obsluhující a kandidátních buněk.

Když UE zjistí, že přednastavená podmínka provedení pro konkrétní kandidátní buňku je splněna – a zároveň je spojení s obsluhující buňkou stále životaschopné – autonomně zahájí provedení předání do této cílové buňky. UE provede náhodný přístup (random access) do zvolené cílové buňky za použití předem přidělených prostředků (jako je vyhrazený [RACH](/mobilnisite/slovnik/rach/) preambule) a odešle zprávu [RRC](/mobilnisite/slovnik/rrc/) Reconfiguration Complete. To vyvolá informování obsluhující buňky o úspěšném předání ze strany cílové buňky přes rozhraní Xn, čímž se spustí přepojení cesty (path switch) a uvolnění starého kontextu UE. Klíčové architektonické komponenty zapojené do procesu jsou UE (které vyhodnocuje podmínky a autonomně provádí), obsluhující RAN uzel (který připravuje CHO a poskytuje konfiguraci), kandidátní cílové RAN uzly (které provádějí řízení přístupu a rezervaci prostředků) a jádro sítě, které je po provedení aktualizováno přes rozhraní [NG](/mobilnisite/slovnik/ng/).

Úlohou CHO v síti je fungovat jako proaktivní bezpečnostní síť pro mobilitu. Přípravou záložních možností předtím, než se rádiový spoj kriticky zhorší, výrazně snižuje pravděpodobnost selhání předání ([HOF](/mobilnisite/slovnik/hof/)) a výpadků rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)). To je obzvláště důležité pro služby vyžadující ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a v nasazeních využívajících vysokofrekvenční pásma s rychlými výkyvy signálu. Procedura je řízena pomocí signalizace RRC (zpráva RRCReconfiguration nese konfiguraci CHO) a koordinace mezi uzly přes rozhraní Xn (pro přípravu a dokončení). CHO může být nakonfigurováno s více kandidátními buňkami a UE vybere první, jejíž podmínky jsou splněny, čímž se do mobilního procesu přidává vrstva diverzity a redundance.

## K čemu slouží

CHO bylo vytvořeno za účelem řešení omezení konvenčních 'nařízených sítí' (network-commanded) předání v sítích 5G a novějších, zejména s rozšiřováním nasazení do kmitočtových pásem nad 6 GHz (FR2). V těchto vysokofrekvenčních pásmech jsou rádiové signály náchylnější k překážkám a rychlému útlumu, což činí časově kritické okno pro úspěšné předání nařízené sítí velmi úzké. Tradiční předání spoléhají na měřicí hlášení od UE, rozhodnutí zdrojového uzlu a povel k předání – proces, který může selhat, pokud se rádiový spoj zhorší rychleji, než lze tento signalizační cyklus dokončit, což vede k přerušení služby.

Primární problém, který CHO řeší, je snížení selhání předání a následných výpadků rádiového spoje v náročných mobilních podmínkách. To zahrnuje scénáře s vysokou rychlostí (např. vysokorychlostní železnice, vozidla), okrajové části buněk s překrývajícím se pokrytím a prostředí s vysokým stíněním nebo přerušovanými překážkami. Přesunutím rozhodnutí o provedení na UE na základě přednastavených lokálních podmínek CHO eliminuje kritické zpoždění obsažené v rozhodovacím a signalizačním cyklu sítě. To činí spouštěč předání citlivějším na okamžité rádiové prostředí, jak jej vnímá UE. Historicky, před CHO, vylepšení jako Early Handover nebo Dual Connectivity částečně řešila robustnost, ale přidávala složitost. CHO poskytuje přímočařejší, na přípravě založený přístup, který zlepšuje spolehlivost pro služby citlivé na latenci a služby klíčové pro bezpečnost (mission-critical), což byl klíčový motiv pro jeho standardizaci jako součást podpory vylepšeného mobilního širokopásmového přístupu (eMBB) a [URLLC](/mobilnisite/slovnik/urllc/) v 5G.

## Klíčové vlastnosti

- Odděluje přípravu předání od provedení
- UE autonomně provádí předání na základě přednastavených rádiových podmínek
- Podporuje konfiguraci více kandidátních cílových buněk
- Používá vyhrazené RACH prostředky v cílových buňkách ke snížení kontence
- Snižuje pravděpodobnost selhání předání a výpadků rádiového spoje
- Zvyšuje robustnost mobility ve scénářích s vysokými kmitočty a vysokou rychlostí

## Definující specifikace

- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 28.313** (Rel-20) — Management and orchestration; SON for 5G networks
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.877** (Rel-18) — Technical Report on Security Aspects of AI/ML in RAN
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [CHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/cho/)
