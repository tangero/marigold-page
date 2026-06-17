---
slug: "lcp"
url: "/mobilnisite/slovnik/lcp/"
type: "slovnik"
title: "LCP – Logical Channel Prioritization"
date: 2025-01-01
abbr: "LCP"
fullName: "Logical Channel Prioritization"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lcp/"
summary: "Logical Channel Prioritization (LCP) je procedura podsložky MAC v 3GPP rádiových protokolech, která určuje, jak přidělit rádiové prostředky pro uplink mezi různé logické kanály z UE. Zajišťuje, že dat"
---

LCP je procedura podsložky MAC, která přiděluje rádiové prostředky pro uplink mezi logické kanály UE, zajišťuje, že data s vyšší prioritou jsou přenesena před daty s nižší prioritou, aby byly splněny požadavky QoS.

## Popis

Logical Channel Prioritization (LCP) je základní procedura uvnitř podsložky Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v User Equipment (UE) v systémech 3GPP, včetně LTE a NR. Jejím hlavním úkolem je rozhodnout, jak namapovat data z více logických kanálů na dostupné transportní bloky pro uplink přidělené sítí prostřednictvím povolení pro plánování uplink. Když UE obdrží od gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) povolení pro uplink, které udává dostupné časově-frekvenční prostředky a maximální velikost transportního bloku, je vyvolána procedura LCP. Procedura musí vybrat, která data z kterých logických kanálů zahrnout do nadcházejícího přenosu, při dodržení přísných pravidel, která upřednostňují kritický provoz.

Procedura funguje na základě souboru standardizovaných pravidel a konfigurací poskytovaných sítí prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Každý logický kanál je konfigurován parametry, jako je priorita, Prioritized Bit Rate (PBR) a Bucket Size Duration (BSD). Základní algoritmus typicky běží ve dvou fázích. Nejprve obslouží každý logický kanál v pořadí podle klesající priority a přidělí data až do své nakonfigurované hodnoty PBR. Tím je zajištěno, že každý kanál obdrží minimální garantovanou rychlost. Ve druhé fázi, pokud zůstanou rádiové prostředky, procedura znovu obslouží logické kanály v pořadí podle priority a přidělí zbývající prostředky. Tento dvoufázový přístup vyvažuje garantované minimální rychlosti s efektivním využitím volné kapacity pro provoz s vysokou prioritou.

LCP úzce spolupracuje s dalšími funkcemi MAC, jako je hlášení stavu vyrovnávací paměti a multiplexování. Samotné logické kanály odpovídají různým rádiovým přenosovým okruhům (bearer), z nichž každý přenáší specifické typy provozu, jako je SRB (Signaling Radio Bearer) pro signalizaci RRC/[NAS](/mobilnisite/slovnik/nas/) nebo [DRB](/mobilnisite/slovnik/drb/) (Data Radio Bearer) pro data uživatelské roviny. Konfigurace parametrů LCP je tedy neoddělitelně spojena s charakteristikami QoS přidruženého EPS beareru nebo QoS Flow. Díky dynamickému rozhodování pro každé přidělení je LCP zásadní pro plnění end-to-end QoS, zajištění nízké latence pro kritické služby a efektivní využití vzácného rádiového spektra pro uplink.

## K čemu slouží

LCP bylo zavedeno, aby vyřešilo kritický problém arbitráže prostředků pro uplink uvnitř UE. V mobilní síti typicky běží na UE více aplikací současně, každá s různými požadavky na kvalitu služby – například VoIP hovor vyžadující nízkou latenci a rozkmity, relace prohlížení webu potřebující rychlou odezvu a propustnost a stahování souboru tolerující zpoždění na pozadí. Bez strukturovaného mechanismu prioritizace by vrstva [MAC](/mobilnisite/slovnik/mac/) v UE neměla standardizovaný způsob, jak rozhodnout, která data odeslat, když přijde přidělení, což by mohlo vést ke špatnému uživatelskému zážitku, porušení smluv QoS a neefektivnímu využití rádiového rozhraní.

Před formalizací LCP v 3GPP měly dřívější systémy jednodušší a méně podrobné mechanismy pro zpracování více datových toků. Vytvoření LCP poskytlo flexibilní, sítí řízený rámec, který umožňuje operátorům definovat přesné politiky QoS. Síť konfiguruje parametry LCP pro každý logický kanál, což dává operátorům přímou kontrolu nad tím, jak jsou prostředky pro uplink rozdělovány mezi služby. To umožňuje podporu sofistikovaných služeb s přísnými požadavky na QoS, jako je hlas a video přes IMS, hraní v reálném čase a průmyslový IoT, přes sdílené rádiové rozhraní. Je to základní kámen pro umožnění efektivního multiplexování a plánování s ohledem na QoS na straně UE, což doplňuje plánování na straně sítě pro downlink.

## Klíčové vlastnosti

- Pravidla prioritizace konfigurovaná sítí pro každý logický kanál
- Dvoufázové přidělování zajišťující garance Prioritized Bit Rate (PBR)
- Dynamické rozdělování prostředků pro každé přidělení pro plánování uplink
- Přímá podpora pro plnění parametrů QoS rádiových přenosových okruhů (bearer)
- Integrace s procedurami hlášení stavu vyrovnávací paměti MAC
- Standardizovaný algoritmus zajišťující konzistentní chování UE

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.825** (Rel-16) — Study on NR Industrial IoT

---

📖 **Anglický originál a plná specifikace:** [LCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcp/)
