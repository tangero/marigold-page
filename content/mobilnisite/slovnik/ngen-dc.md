---
slug: "ngen-dc"
url: "/mobilnisite/slovnik/ngen-dc/"
type: "slovnik"
title: "NGEN-DC – E-UTRA NR Dual Connectivity with E-UTRAN connected to 5GC"
date: 2026-01-01
abbr: "NGEN-DC"
fullName: "E-UTRA NR Dual Connectivity with E-UTRAN connected to 5GC"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ngen-dc/"
summary: "Režim duální konektivity, ve kterém je uživatelské zařízení (UE) současně připojeno k LTE základnové stanici (eNodeB) a 5G NR základnové stanici (gNB), přičemž LTE uzel vystupuje jako hlavní uzel přip"
---

NGEN-DC je režim duální konektivity, ve kterém je uživatelské zařízení (UE) současně připojeno k LTE eNodeB a 5G NR gNB, přičemž LTE uzel funguje jako hlavní uzel připojený k 5G Core pro účely migrace.

## Popis

NGEN-DC, což znamená [E-UTRA](/mobilnisite/slovnik/e-utra/) NR Dual Connectivity with [E-UTRAN](/mobilnisite/slovnik/e-utran/) connected to 5GC (duální konektivita E-UTRA a NR s E-UTRAN připojeným k 5GC), je specifická architektura duální konektivity ([DC](/mobilnisite/slovnik/dc/)) definovaná 3GPP. V této konfiguraci si uživatelské zařízení (UE) udržuje současná spojení se dvěma různými uzly rádiového přístupu: Hlavním uzlem ([MN](/mobilnisite/slovnik/mn/)), kterým je LTE eNodeB (E-UTRA), a Sekundárním uzlem (SN), kterým je 5G NR gNB. Kritickým architektonickým aspektem NGEN-DC je, že hlavní eNodeB je připojen k 5G Core síti (5GC) přes rozhraní [NG](/mobilnisite/slovnik/ng/), nikoli k zastaralému Evolved Packet Core (EPC). To jej odlišuje od [EN-DC](/mobilnisite/slovnik/en-dc/), kde je eNodeB připojen k EPC. LTE uzel poskytuje kotvu řídicí roviny (přes něj je vedeno NR [RRC](/mobilnisite/slovnik/rrc/) spojení), zatímco oba uzly mohou dodávat data uživatelské roviny do UE a agregovat tak rádiové zdroje pro vyšší propustnost a spolehlivost.

Fungování NGEN-DC zahrnuje sofistikovanou koordinaci mezi hlavním eNodeB a sekundárním gNB. UE se nejprve připojí k LTE síti, která je nakonfigurována tak, aby podporovala připojení k 5GC (tzv. LTE kotva v 5GC). Když jsou podmínky příznivé (např. je dostupný silný NR signál), hlavní eNodeB může iniciovat přidání sekundárního gNB pro dané UE. Tento proces zahrnuje signalizaci mezi eNodeB a gNB přes rozhraní Xn (mezibázové rozhraní v 5G). Hlavní uzel si zachovává kontrolu nad RRC spojením (Radio Resource Control) UE a spravuje připojení k funkci [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) v 5GC. Sekundární uzel poskytuje dodatečné rádiové zdroje (sekundární skupinu buněk, SCG) pro přenos dat. Data mohou být rozdělena na vrstvě PDCP (architektury možnosti 3 nebo 3a/3x), kde PDCP vrstva hlavního uzlu zajišťuje směrování paketů buď do své vlastní RLC vrstvy (pro přenos přes LTE), nebo do RLC vrstvy sekundárního uzlu (pro přenos přes NR).

Klíčové komponenty NGEN-DC zahrnují UE podporující obě rádiové rozhraní E-UTRA a NR, LTE eNodeB fungující jako hlavní uzel (MN), NR gNB fungující jako sekundární uzel (SN) a 5G Core síť. Zapojená rozhraní jsou NG rozhraní mezi MN a 5GC, Xn rozhraní mezi MN a SN pro koordinaci a Uu rádiové rozhraní pro LTE i NR. UE musí podporovat potřebný protokolový zásobník, včetně duálních PDCP entit pro provoz split přenašeče. Úloha NGEN-DC v síti spočívá v poskytnutí klíčové migrační cesty pro operátory zavádějící 5G. Umožňuje jim zavádět pokrytí 5G NR v hotspotech nebo nových kmitočtových pásmech, přičemž se mohou spolehnout na všudypřítomnou LTE síť pro širokoplošné pokrytí a spolehlivost řídicí roviny. To uživatelům poskytuje časné zvýšení přenosové rychlosti 5G v podporovaných oblastech a zároveň zajišťuje plynulou mobilitu a kontinuitu služeb na LTE vrstvě.

## K čemu slouží

NGEN-DC byl vytvořen, aby usnadnil flexibilní a efektivní migraci ze sítí 4G LTE k plnohodnotným 5G standalone (SA) sítím. Před 5G SA využívala počáteční nasazení 5G architekturu Non-Standalone (NSA), konkrétně EN-DC, kde NR gNB byl přídavkem k LTE síti připojené k EPC. Zatímco EN-DC poskytovalo zvýšení rychlosti 5G, neumožňovalo přístup k novým schopnostem 5GC, jako je síťové dělení (network slicing) nebo pokročilá QoS. NGEN-DC tento problém řeší tím, že umožňuje samotné LTE síti připojit se k novému 5GC, což operátorům umožňuje nasadit a testovat 5G core, zatímco stále využívají své rozsáhlé rádiové prostředky LTE jako primární vrstvu pokrytí.

Řeší problém "slepice a vejce" při nasazování 5G: vybudování celonárodní vrstvy pokrytí 5G NR je časově náročné a drahé. NGEN-DC umožňuje operátorům spustit služby 5G (přes 5GC) mnohem rychleji díky využití jejich stávající LTE rádiové přístupové sítě (RAN) jako hlavní vrstvy pokrytí. Poskytuje střední cestu mezi čistě NSA (EN-DC s EPC) a čistě SA (NR připojené k 5GC). To umožňuje účastníkům těžit z nových služeb 5G core a potenciálně vyšších přenosových rychlostí přes NR sekundární buňky, dokonce i v oblastech, kde je pokrytí 5G NR řídké nebo neexistující.

Historicky řeší omezení EN-DC, které vázalo inovace 5G rádia na zastaralý EPC. NGEN-DC toto odděluje tím, že připojuje LTE RAN k 5GC, čímž činí LTE síť "5GC-aware". Toto byl strategický krok v 3GPP Release 15, který umožnil postupnější přechod, při kterém mohla být základní síť modernizována nezávisle na dosažení plného NR pokrytí. Motivovalo to operátory začít nasazovat infrastrukturu 5GC a testovat nové služby bez čekání na dokončení výstavby NR, čímž se urychlil celkový vývoj 5G ekosystému.

## Klíčové vlastnosti

- Duální konektivita s LTE eNodeB jako hlavním uzlem (MN) a NR gNB jako sekundárním uzlem (SN)
- Hlavní eNodeB je připojen k 5G Core síti (5GC) přes rozhraní NG
- Poskytuje spolehlivost řídicí roviny a pokrytí přes LTE, s navýšením kapacity přes NR
- Podporuje rozdělení uživatelské roviny na vrstvě PDCP (možnosti 3/3a/3x) pro agregaci dat
- Využívá rozhraní Xn pro koordinaci mezi LTE eNodeB a NR gNB
- Umožňuje přístup k nativním službám 5GC (např. síťové dělení) při kotvení na LTE

## Související pojmy

- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)
- [MR-DC – Multi-Radio Dual Connectivity](/mobilnisite/slovnik/mr-dc/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 28.657** (Rel-19) — E-UTRAN NRM IRP Requirements
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.473** (Rel-19) — W1 Application Protocol (W1AP) Specification
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.508** (Rel-19) — 5G NR UE Radio Transmission & Reception
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [NGEN-DC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngen-dc/)
