---
slug: "tma"
url: "/mobilnisite/slovnik/tma/"
type: "slovnik"
title: "TMA – Tower Mounted Amplifier"
date: 2025-01-01
abbr: "TMA"
fullName: "Tower Mounted Amplifier"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tma/"
summary: "Zesilovač s nízkým šumem instalovaný na vrcholu stožáru základnové stanice, blízko přijímacích antén, pro zlepšení citlivosti v uplinku. Zesiluje slabé signály od uživatelských zařízení dříve, než je"
---

TMA je zesilovač s nízkým šumem umístěný poblíž přijímacích antén základnové stanice, který zesiluje slabé signály v uplinku před ztrátami v kabelu, čímž zlepšuje pokrytí, kapacitu a výkon sítě.

## Popis

Tower Mounted Amplifier (TMA) je aktivní vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) komponenta nasazovaná v podsystému základnové stanice mobilní sítě. Jejím hlavním účelem je zesílení signálů v uplinku (od UE k základnové stanici) přijímaných anténami základnové stanice dříve, než jsou tyto signály vystaveny ztrátám inherentním v koaxiálním feeder kabelu, který vede dolů po stožáru k základnové jednotce ([BBU](/mobilnisite/slovnik/bbu/)) nebo rádiové jednotce. TMA je umístěna přímo v místě antény, typicky integrována do anténního souboru nebo umístěna bezprostředně vedle něj. Jedná se o zesilovač s nízkým šumem ([LNA](/mobilnisite/slovnik/lna/)), což znamená, že je navržen tak, aby poskytoval významné zesílení při přidání minimálního dodatečného šumu do signálu, což je klíčové pro udržení dobrého poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)).

TMA funguje tak, že zachytí dráhu RF signálu mezi anténním portem a feeder kabelem. Slabý signál přijatý od vzdálené UE nejprve prochází TMA, kde je zesílen. Tento zesílený signál pak putuje dolů ztrátovým feeder kabelem. Protože je signál v místě vstupu do kabelu silnější, má následná kabelová ztráta proporcionálně menší degradační účinek na celkový rozpočet spoje. Na úpatí stožáru vstupuje signál do přijímače základnové stanice. Klíčovým přínosem je zlepšení šumového čísla systému. Šumové číslo první komponenty v přijímacím řetězci dominuje celkovému šumovému číslu systému. Umístěním zesilovače s nízkým šumem na první místo se TMA efektivně stává „prvním“ stupněm, nastavuje velmi nízkou hladinu šumu, která maskuje vyšší šumový příspěvek feeder kabelu a vlastního přijímače základnové stanice.

Z architektonického hlediska systém TMA zahrnuje zesilovací jednotku, napájecí zdroj a často diplexer nebo cirkulátor. Diplexer je klíčový, protože odděluje vysílací a přijímací dráhy, což umožňuje TMA zesilovat pouze přijímané signály bez interference s vysokoenergetickými vysílacími signály v downlinku ze základnové stanice. Napájení je k TMA obvykle dodáváno prostřednictvím stejného koaxiálního feeder kabelu, který přenáší RF signály, pomocí techniky zvané Remote Electrical Tilt ([RET](/mobilnisite/slovnik/ret/)) napájení nebo pomocí samostatné jednotky vkládání napájení na úpatí. Nasazení TMA je klíčovým rozhodnutím při plánování rádiové sítě, protože přímo ovlivňuje poloměr pokrytí buňky, přenosové rychlosti v uplinku a celkovou kvalitu sítě, zejména ve scénářích omezených pokrytím, jako jsou venkovské oblasti nebo při použití vyšších kmitočtových pásem, kde jsou ztráty ve feeder kabelu výraznější.

## K čemu slouží

Tower Mounted Amplifier byl vyvinut k řešení základního fyzikálního omezení v návrhu buněčných základnových stanic: ztráty signálu v koaxiálním feeder kabelu spojujícím anténu s rádiovou jednotkou základnové stanice. Tato ztráta, která roste s délkou kabelu a frekvencí, vážně degraduje citlivost v uplinku, což omezuje pokrytí a kapacitu buňky. Před zavedením TMA byly jediným řešením použití velmi drahých kabelů s nízkými ztrátami (které jsou těžké a obtížně instalovatelné) nebo umístění celé rádiové jednotky na vrchol stožáru (což vytváří výzvy pro údržbu, napájení a chlazení). TMA poskytuje elegantní a nákladově efektivní alternativu.

Jejím primárním účelem je zlepšit rozpočet spoje v uplinku, který je často limitujícím faktorem pokrytí sítě, zejména pro datové služby a v suburbánních nebo venkovských nasazeních. Zesílením signálu předtím, než dojde ke kabelové ztrátě, TMA efektivně „vyruší“ část této ztráty. To vede k nižšímu celkovému šumovému číslu systému, což se přímo projevuje tím, že základnová stanice dokáže přijímat slabší signály od vzdálených uživatelských zařízení. Tím se rozšiřuje praktický poloměr buňky, zlepšují se přenosové rychlosti na jejím okraji a může se snížit počet základnových stanic potřebných k pokrytí dané oblasti, což vede k významným úsporám kapitálových výdajů ([CAPEX](/mobilnisite/slovnik/capex/)) pro síťové operátory.

Motivace pro přijetí TMA zesílila se zavedením systémů 3G/[WCDMA](/mobilnisite/slovnik/wcdma/) a pozdějších technologií. Tyto systémy jsou často limitovány uplinkem kvůli nižšímu vysílacímu výkonu rukou ve srovnání se základnovými stanicemi a použití vyšších kmitočtových pásem (jako 2100 MHz), kde jsou ztráty ve feeder kabelu vyšší. Dále technologie jako LTE a 5G, které využívají modulaci vyššího řádu (např. 256-QAM) v uplinku, vyžadují pro svou funkci vynikající [SNR](/mobilnisite/slovnik/snr/). TMA poskytuje potřebné zlepšení SNR k umožnění těchto pokročilých funkcí. Také pomáhá dosáhnout vyvážených rozpočtů spoje, což zajišťuje, že pokrytí buňky není zbytečně omezeno uplinkem, a umožňuje operátorům plně využít downlinkové kapacit jejich sítí. V podstatě je TMA klíčovým nástrojem pro optimalizaci rádiové sítě, který umožňuje lepší kvalitu služeb a efektivnější využití spektra a infrastruktury.

## Klíčové vlastnosti

- Zesilovač s nízkým šumem (LNA) instalovaný u antény pro zlepšení citlivosti v uplinku
- Kompensuje ztrátu signálu ve feeder kabelu mezi anténou a základnovou stanicí
- Zlepšuje celkové šumové číslo systému, rozšiřuje pokrytí a kapacitu buňky
- Typicky obsahuje diplexer pro oddělení vysílacích a přijímacích drah signálu
- Často napájen vzdáleně prostřednictvím koaxiálního feeder kabelu (napájení Remote Electrical Tilt)
- Kritický pro vyvážení výkonu uplink/downlink, zejména ve vyšších kmitočtových pásmech

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 28.652** (Rel-19) — UTRAN Network Resource Model (NRM) IRP Information Service
- **TS 28.662** (Rel-19) — Generic RAN Network Resource Model (NRM) IRP IS
- **TS 32.642** (Rel-11) — UTRAN Network Resource Model for Configuration Management
- **TS 32.792** (Rel-11) — Generic RAN Network Resource Model (NRM) IRP
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 37.460** (Rel-19) — Iuant Interface Introduction
- **TS 37.461** (Rel-19) — Iuant Interface Layer 1 Specification
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 37.466** (Rel-19) — Iuant Interface Introduction & RETAP/TMAAP
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [TMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tma/)
