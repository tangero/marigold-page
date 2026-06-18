---
slug: "wb-cmr"
url: "/mobilnisite/slovnik/wb-cmr/"
type: "slovnik"
title: "WB-CMR – Codec Mode Request for Adaptive Multi-Rate Wideband"
date: 2025-01-01
abbr: "WB-CMR"
fullName: "Codec Mode Request for Adaptive Multi-Rate Wideband"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wb-cmr/"
summary: "WB-CMR je řídicí mechanismus používaný v hovorech s kodekem AMR-WB, kdy přijímač zasílá vysílači požadavky na přepnutí do konkrétního režimu kodeku (přenosové rychlosti). Dynamicky optimalizuje kvalit"
---

WB-CMR je řídicí mechanismus v hovorech s kodekem AMR-WB, kdy přijímač vyžádá od vysílače konkrétní režim kodeku za účelem dynamické optimalizace kvality hlasu a využití šířky pásma.

## Popis

WB-CMR (Codec Mode Request for [AMR-WB](/mobilnisite/slovnik/amr-wb/)) je specifický signalizační mechanismus v rámci přenosu definovaný v rámci standardu 3GPP pro širokopásmový adaptivní vícerychlostní řečový kodek (Adaptive Multi-Rate Wideband, AMR-WB). Funguje během aktivního hlasového hovoru, kde je jako kodek vybrán AMR-WB. Primární funkcí WB-CMR je umožnit přijímací straně hovoru (dekodéru) ovlivnit pracovní režim vysílající strany (kodéru). Kodek AMR-WB má více režimů, z nichž každý odpovídá konkrétní přenosové rychlosti a souvisejícím kompromisům mezi kvalitou řeči a odolností, v rozsahu od 6,60 kbit/s (Režim 0) do 23,85 kbit/s (Režim 8).

Z architektonického hlediska je WB-CMR generován řečovým dekodérem v přijímajícím uživatelském zařízení (UE) nebo síťovém uzlu (např. Media Gateway). Je vložen do datové části paketů [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) přenášejících komprimované řečové rámce, konkrétně do hlavičky datové části [AMR](/mobilnisite/slovnik/amr/). Tato signalizace v rámci přenosu zajišťuje těsné propojení požadavku s mediálním proudem. Když vysílač přijme paket obsahující WB-CMR, interpretuje jej jako doporučení nebo příkaz (v závislosti na implementaci) k přepnutí svého kódování do požadovaného režimu pro následující řečové rámce. Tento mechanismus funguje ve spojení s jinými adaptačními metodami, jako jsou ty založené na měření kvality rádiového spoje z rozhraní Uu.

Klíčovými komponentami jsou samotný kodek AMR-WB s jeho vícerychlostní schopností, formát datové části RTP pro AMR a AMR-WB, který definuje strukturu pro přenos pole [CMR](/mobilnisite/slovnik/cmr/), a end-to-end mediální cesta. Role WB-CMR v síti je klíčová pro dynamické řízení šířky pásma a optimalizaci kvality. Například, pokud přijímač zaznamenává ztrátu paketů nebo zkreslení času (jitter), může požádat o robustnější režim s nižší přenosovou rychlostí, aby se zlepšila odolnost vůči chybám. Naopak za vynikajících podmínek může požadovat režim s vyšší přenosovou rychlostí pro lepší kvalitu řeči. To umožňuje efektivní využití síťových zdrojů při zachování nejlepší možné vnímané kvality hlasu za měnících se podmínek.

## K čemu slouží

WB-CMR existuje, aby řešil základní výzvu kodeku [AMR-WB](/mobilnisite/slovnik/amr-wb/): jak dynamicky vybrat optimální kompromis mezi kvalitou řeči (vyšší přenosová rychlost) a odolností vůči chybám/efektivitou využití šířky pásma (nižší přenosová rychlost) v reálném čase během hovoru. Před existencí takových adaptivních kodeků s zpětnou vazbou od přijímače fungovaly kodeky s pevnou rychlostí nebo se mohly adaptovat pouze na základě lokálních rozhodnutí vysílače (např. na základě hlášení o rádiovém spoji). To bylo suboptimální, protože přijímač má nejlepší znalost skutečné kvality přijímaného mediálního proudu, včetně vzorců ztráty paketů a zkreslení času (jitter).

Motivací pro vytvoření mechanismu [CMR](/mobilnisite/slovnik/cmr/) bylo umožnit adaptaci v uzavřené smyčce na aplikační vrstvě. Tím, že dekodér dostal přímou možnost ovlivnit činnost kodéru, může systém přesněji reagovat na skutečné podmínky end-to-end cesty, které se mohou lišit od rádiových podmínek známých pouze základnové stanici vysílače. Tím se řeší problém nepřiměřené adaptace, kdy vysílač může zvýšit přenosovou rychlost na základě dobrých lokálních rádiových podmínek, ale přijímač trpí přetížením jinde v IP síti. WB-CMR jako součást standardu AMR-WB byla klíčovou inovací, která učinila adaptivní vícerychlostní kodeky skutečně efektivními pro přenos hlasu přes paketovou síť na proměnlivých kanálech, jako byly rané 3G a LTE, a zajišťovala konzistentní kvalitu hovoru a efektivní využití sítě.

## Klíčové vlastnosti

- Signalizace v rámci přenosu uvnitř datové části RTP pro AMR-WB
- Umožňuje přijímači vyžádat si konkrétní režim kodeku AMR-WB (přenosovou rychlost)
- Podporuje dynamickou adaptaci na základě kvality end-to-end cesty
- Definované režimy od 6,60 kbit/s (Režim 0) do 23,85 kbit/s (Režim 8)
- Funguje ve spojení s síťovou adaptací přenosové rychlosti
- Klíčové pro optimalizaci kvality a šířky pásma v hovorech VoLTE/VoNR

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [CMR – Codec Mode Request](/mobilnisite/slovnik/cmr/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 26.453** (Rel-19) — EVS Codec Generic Frame Format for 3G CS Networks
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks

---

📖 **Anglický originál a plná specifikace:** [WB-CMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/wb-cmr/)
