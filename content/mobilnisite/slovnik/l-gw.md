---
slug: "l-gw"
url: "/mobilnisite/slovnik/l-gw/"
type: "slovnik"
title: "L-GW – Local PDN Gateway"
date: 2025-01-01
abbr: "L-GW"
fullName: "Local PDN Gateway"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/l-gw/"
summary: "Síťová funkce, která poskytuje místní přístup k IP síti a bránové funkce pro přenosovou rovinu, typicky nasazená v blízkosti rádiové přístupové sítě. Umožňuje služby s nízkou latencí, odlehčuje přenos"
---

L-GW je funkce místní brány, která poskytuje přímý přístup k IP síti v blízkosti rádiové sítě, aby umožnila služby s nízkou latencí, odlehčila přenosovou zátěž jádra sítě a podporovala funkce jako LIPA a SIPTO.

## Popis

Local [PDN](/mobilnisite/slovnik/pdn/) Gateway (L-GW) je funkce přenosové roviny jádra sítě, která slouží jako brána mezi uživatelským zařízením (UE) a místní datovou sítí nebo internetem, ale je nasazena decentralizovaně, často na okraji sítě poblíž rádiové základnové stanice (např. eNodeB v LTE, gNB v 5G). Architektonicky zahrnuje funkce tradiční PDN Gateway ([PGW](/mobilnisite/slovnik/pgw/)), jako je přidělování IP adres, filtrování paketů, vynucování politik a účtování, ale v lokálním rozsahu. V LTE se jedná o logickou komponentu, která může být umístěna společně s HeNB (Home eNodeB) v rezidenčním nebo podnikovém prostředí pro [LIPA](/mobilnisite/slovnik/lipa/), nebo nasazena v síťovém agregačním bodě pro [SIPTO](/mobilnisite/slovnik/sipto/). V 5G jsou její funkce pohlceny funkcí User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) při nasazení na okraji sítě, kde Local UPF je ekvivalentní entitou.

Jak to funguje, závisí na scénáři nasazení. Pro Local IP Access (LIPA) je L-GW integrována s HeNB Gateway nebo samotnou HeNB. Když se UE připojí a požádá o LIPA spojení, Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) vybere společně umístěnou L-GW a přenosová data přenosové roviny jsou směrována přímo z HeNB na L-GW a poté do místní sítě (např. domácí nebo podnikové [LAN](/mobilnisite/slovnik/lan/)), aniž by procházela operátorovou jádrovou sítí. To poskytuje nízkou latenci a odlehčuje místní provoz. Pro Selected IP Traffic Offload (SIPTO) je L-GW nasazena v síťovém agregačním bodě (jako regionální datové centrum). MME nebo [SGSN](/mobilnisite/slovnik/sgsn/) vybere tuto L-GW na základě politik směrování provozu, což umožňuje, aby specifický IP provoz (např. internetový) vystupoval do internetu lokálně, čímž se sníží zátěž centrální PGW a přenosové části jádra sítě.

Klíčové komponenty a rozhraní zahrnují rozhraní S5/S8 (založené na GTP) pro komunikaci se Serving Gateway (SGW) v architekturách 3GPP, ačkoli v lokalizovaných nasazeních jako LIPA může být tato cesta interní. Dále implementuje rozhraní Gi směrem k externí PDN (Packet Data Network). L-GW provádí zpracování paketů na úrovni přenosového kanálu, aplikuje politiky Quality of Service (QoS) a komunikuje s Policy and Charging Rules Function (PCRF) pro dynamické řízení politik. Její role je klíčová pro umožnění edge computingu, aplikací s nízkou latencí (jako průmyslový IoT, AR/VR) a efektivního řízení provozu tím, že přináší bránové funkce blíže k uživateli.

## K čemu slouží

L-GW byla vytvořena, aby řešila problémy zahlcení sítě, latence a neefektivního směrování místního provozu. V tradičních mobilních architekturách byl veškerý provoz přenosové roviny, dokonce i provoz určený pro místní síť ve stejné budově jako základnová stanice, směrován přes centralizovanou PGW hluboko v jádru sítě. Tento 'trombónový' efekt přinášel zbytečnou latenci, spotřebovával přenosové kapacity backhaulových spojů a zdroje jádra sítě a byl neefektivní pro aplikace náročné na šířku pásma nebo citlivé na zpoždění.

Počáteční motivací ve verzi Release 10 byla podpora rezidenčních a podnikových nasazení femtobuněk (HeNB) s Local IP Access (LIPA), což umožnilo UE přistupovat k místním zdrojům (např. tiskárnám, mediálním serverům) přímo bez dopadu na makro síť. Tím se vyřešilo omezení předchozích architektur femtobuněk, které stále přenášely veškerý provoz do jádra sítě. Následně byl koncept rozšířen o Selected IP Traffic Offload (SIPTO) na okraji sítě, aby se odlehčil internetový provoz, snížila se zátěž centrálních bran a zlepšil uživatelský zážitek u služeb jako streamování videa.

Historicky L-GW připravila cestu pro inteligenci na okraji sítě a lokalizaci provozu. Reagovala na rostoucí poptávku po mobilních datech a potřebu efektivnějších síťových architektur. Omezení čistě centralizovaného modelu brány se stala zřejmými s nástupem IoT a aplikací v reálném čase. L-GW a její evoluce do Local UPF v 5G přímo motivovaly posun směrem k distribuované přenosové rovině a edge computingu, které jsou základem slibů 5G ohledně nízké latence a vysoké efektivity.

## Klíčové vlastnosti

- Místní přístup k IP síti pro přímý přístup k blízkým sítím (LIPA)
- Vybraný odlehčený IP provoz (SIPTO) na okraji sítě
- Společné umístění s přístupovými uzly (např. HeNB) pro ultranízkou latenci
- Standardní funkce PGW (přidělování IP, vynucování politik, účtování) v lokální instanci
- Snižuje zahlcení backhaulových spojů a jádra sítě
- Umožňuje edge computing a scénáře služeb s nízkou latencí

## Související pojmy

- [LIPA – Local IP Access](/mobilnisite/slovnik/lipa/)
- [SIPTO – Selected IP Traffic Offload](/mobilnisite/slovnik/sipto/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [HENB – Home Enhanced Node B](/mobilnisite/slovnik/henb/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.875** (Rel-13) — Dual Connectivity Extension Requirements

---

📖 **Anglický originál a plná specifikace:** [L-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/l-gw/)
