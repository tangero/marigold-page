---
slug: "enb"
url: "/mobilnisite/slovnik/enb/"
type: "slovnik"
title: "eNB – Evolved Node B"
date: 2025-01-01
abbr: "eNB"
fullName: "Evolved Node B"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/enb/"
summary: "eNB je základnová stanice v sítích LTE (4G) a v raných nesamostatných sítích 5G NR. Zajišťuje všechny funkce související s rádiovým přístupem pro připojená UE, včetně správy rádiových prostředků, říze"
---

eNB je základnová stanice v sítích LTE (4G) a v raných nesamostatných sítích 5G NR, která zajišťuje všechny funkce související s rádiovým přístupem pro připojená zařízení a slouží jako klíčová součást E-UTRAN.

## Popis

Evolved Node B (eNB) je centrální prvek rádiové přístupové sítě Long-Term Evolution (LTE), známé jako [E-UTRAN](/mobilnisite/slovnik/e-utran/). Jedná se o sofistikovanou základnovou stanici, která přebírá většinu funkcí radiového síťového řadiče ([RNC](/mobilnisite/slovnik/rnc/)), jež byly v předchozích sítích 3G UMTS rozděleny mezi samostatné uzly, což vedlo k plošší a efektivnější architektuře. eNB je zodpovědná za celý zásobník protokolů vrstvy 1 (fyzická), vrstvy 2 ([MAC](/mobilnisite/slovnik/mac/), [RLC](/mobilnisite/slovnik/rlc/), [PDCP](/mobilnisite/slovnik/pdcp/)) a vrstvy 3 ([RRC](/mobilnisite/slovnik/rrc/)) směrem k uživatelskému zařízení (UE). Spravuje rádiové rozhraní, včetně modulace, kódování, plánování zdrojů pro uplink a downlink a provádění předávání spojení.

Architektonicky obsluhuje eNB jednu nebo více buněk. K UE se připojuje přes rádiové rozhraní LTE-Uu a k ostatním eNB se připojuje přes rozhraní [X2](/mobilnisite/slovnik/x2/) pro přímou koordinaci, primárně za účelem plynulého předávání spojení a výměny informací o zatížení a interferenci. Připojení k Evolved Packet Core (EPC) je zajištěno přes rozhraní S1, rozdělené na [S1-MME](/mobilnisite/slovnik/s1-mme/) pro signalizaci řídicí roviny k MME a S1-U pro tunelování dat uživatelské roviny k Serving Gateway (S-GW). Toto oddělení umožňuje škálovatelné a flexibilní nasazení sítě.

Mezi klíčové vnitřní komponenty funkcionality eNB patří entita Radio Resource Control (RRC) pro navazování spojení, mobilitu a aktivaci zabezpečení; Packet Data Convergence Protocol (PDCP) pro kompresi hlaviček, šifrování a ochranu integrity; Radio Link Control (RLC) pro segmentaci a ARQ; a Medium Access Control (MAC) pro plánování, hybridní ARQ a multiplexování logických kanálů. Role eNB je klíčová pro zajištění kvality služeb (QoS) prosazováním QoS politik přijatých od základnové sítě a odpovídající správou rádiových přenosových kanálů. V nasazeních 5G Non-Standalone (NSA) eNB (často označované jako ng-eNB při připojení k 5GC) spolupracuje se stanicí 5G NR gNB, přičemž LTE strana slouží jako kotva pro připojení řídicí roviny.

## K čemu slouží

eNB bylo vytvořeno jako součást standardu LTE organizace 3GPP k odstranění omezení architektury sítě 3G UMTS, která využívala samostatný uzel Radio Network Controller (RNC). Distribuovaná architektura RNC-Node B zaváděla latenci v rozhodování o rádiových prostředcích a vytvářela potenciální jediný bod selhání a zahlcení. Hlavní motivací bylo vytvořit plošší, plně IP architekturu, která by snížila latenci, zvýšila uživatelské datové rychlosti a zjednodušila nasazení a správu sítě.

Integrací funkcí RNC do základnové stanice umožňuje eNB rychlejší, lokalizované rozhodování o správě rádiových prostředků a předávání spojení. Tento architektonický posun byl zásadní pro dosažení klíčových výkonnostních cílů LTE, jako je latence uživatelské roviny pod 10 ms a špičkové datové rychlosti přesahující 100 Mbps. Přímé rozhraní eNB (S1) k základnové síti také zjednodušilo datovou cestu, čímž se zlepšila efektivita pro paketově orientované služby. Jeho zavedení představovalo zásadní vývoj od architektury orientované na okruhovou komutaci u 2G/3G směrem k systému optimalizovanému pro paketový přenos, určenému pro éru mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Integruje všechny funkce správy rádiových prostředků (RRM) včetně plánování, předávání spojení a řízení přístupu.
- Ukončuje protokoly rádiového rozhraní LTE-Uu (RRC, PDCP, RLC, MAC, PHY).
- Připojuje se k EPC přes rozhraní S1 (S1-MME pro řídicí rovinu, S1-U pro uživatelskou rovinu).
- Propojuje se se sousedními eNB přes rozhraní X2 pro přímou koordinaci a předávání spojení.
- Spravuje rádiové přenosové kanály a vynucuje QoS politiky pro datové toky uživatelů.
- Podporuje klíčové procedury mobility, jako je předávání spojení v rámci LTE a do/z dědičných systémů 3G/2G.

## Související pojmy

- [E-UTRAN – Evolved Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/e-utran/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions
- **TS 36.523** (Rel-19) — UE Conformance Test Spec for Idle Mode
- **TS 37.571** (Rel-19) — UE Conformance for Positioning

---

📖 **Anglický originál a plná specifikace:** [eNB na 3GPP Explorer](https://3gpp-explorer.com/glossary/enb/)
