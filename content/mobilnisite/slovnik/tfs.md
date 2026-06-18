---
slug: "tfs"
url: "/mobilnisite/slovnik/tfs/"
type: "slovnik"
title: "TFS – Transport Format Set"
date: 2025-01-01
abbr: "TFS"
fullName: "Transport Format Set"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfs/"
summary: "Konfigurovaná sada všech platných kombinací transportních formátů, které lze použít na transportním kanálu v UMTS. Definuje možné velikosti datových bloků, kódovací schémata a časování pro přenos, čím"
---

TFS je konfigurovaná sada všech platných kombinací transportních formátů, která definuje možné velikosti datových bloků, kódovací schémata a časování pro transportní kanál UMTS, aby umožnila dynamickou adaptaci přenosové rychlosti.

## Popis

Transport Format Set (TFS) je klíčový konfigurační koncept ve vrstvě 2 (Layer 2) rozhraní UMTS, konkrétně pro vrstvu řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Každý vyhrazený nebo společný transportní kanál (TrCH) je nakonfigurován s TFS, což je soubor povolených transportních formátů ([TF](/mobilnisite/slovnik/tf/)). Samotný transportní formát je kombinací semistatických a dynamických atributů, které plně popisují, jak je transportní blok ([TB](/mobilnisite/slovnik/tb/)) nebo sada transportních bloků předána fyzické vrstvě k přenosu v daném přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)). Semistatická část zahrnuje parametry jako délka TTI, typ kanálového kódování (např. konvoluční, turbo), kódovací rychlost a velikost [CRC](/mobilnisite/slovnik/crc/). Dynamická část specifikuje počet transportních bloků (TB) a jejich velikost.

Z architektonického hlediska je TFS definován a signalizován uživatelskému zařízení (UE) radiovým síťovým řadičem ([RNC](/mobilnisite/slovnik/rnc/)) prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) během nastavování nebo rekonfigurace rádiového přenosového kanálu. Je součástí informačního prvku transportního kanálu. Vrstva MAC jak v UE, tak v [UTRAN](/mobilnisite/slovnik/utran/) (Node B/RNC) používá tuto sadu jako omezení. Pro každý TTI vybere plánovač MAC jednu konkrétní kombinaci transportních formátů (TFC) z povolené sady, což je platná kombinace transportních formátů napříč všemi aktivními transportními kanály UE. Tento výběr je založen na dostupných datech, prioritě a přidělených prostředcích.

Jak to funguje, zahrnuje dvoustupňový proces: konfiguraci a dynamický výběr. Nejprve RNC předdefinuje TFS, čímž zajistí, že všechny možné datové rychlosti a formáty potřebné pro QoS služby jsou k dispozici, ale v rámci možností fyzické vrstvy. Za druhé, během provozu dynamicky vybere entita MAC pro každý TTI TF z této sady. Ve verzi 99/4 byl tento výběr z velké části řízen RNC prostřednictvím signalizace TFCI. V pozdějších verzích s HSDPA/EUL je TFS pro vysokorychlostní kanály stále konfigurován RNC, ale dynamický výběr (indikovaný TFRI) provádí rychlý plánovač Node B. TFS tedy poskytuje základní 'menu' přenosových možností, které umožňují adaptaci rychlosti a zároveň zajišťují, že přenosy zůstanou v předdefinovaných, síťově řízených mezích pro správu rušení a prostředků.

## K čemu slouží

Koncept TFS byl vytvořen, aby poskytl flexibilní, ale řízený rámec pro přenos dat s proměnnou rychlostí přes rozhraní UMTS, což představuje posun oproti kanálům s pevnou rychlostí v systémech 2G, jako je GSM. Řeší základní výzvu podpory multimediálních služeb s různorodými a kolísavými požadavky na šířku pásma (např. hlas, video streamování, prohlížení webu) na sdílených rádiových prostředcích. Bez předdefinované sady formátů by dynamická adaptace rychlosti byla neomezená a mohla by vést k nekontrolovanému rušení nebo nekompatibilitám fyzické vrstvy mezi vysílačem a přijímačem.

V architektuře UMTS před HSDPA (verze 99) umožňoval TFS RNC staticky definovat možné datové rychlosti pro rádiový přenosový kanál, zatímco vrstva MAC mezi nimi mohla dynamicky přepínat na základě objemu provozu. Tím bylo vyřešeno problém efektivního multiplexování více služeb s různými bitovými rychlostmi na jeden složený kódovaný transportní kanál (CCTrCh). Konfigurace TFS zahrnuje kompromisy mezi špičkovou datovou rychlostí, granularitou adaptace rychlosti a signalizační režií. Jeho vytvoření bylo motivováno potřebou standardizované, efektivní metody pro správu složitého mapování mezi datovými toky logických kanálů a přenosovými schopnostmi fyzické vrstvy ve širokopásmovém systému CDMA.

## Klíčové vlastnosti

- Definuje všechny platné přenosové formáty pro transportní kanál
- Zahrnuje semistatické parametry (TTI, typ kódování) a dynamické parametry (velikost TB, počet)
- Konfigurován RNC prostřednictvím signalizace RRC
- Umožňuje dynamickou adaptaci rychlosti v síťově řízených mezích
- Základní pro výběr kombinace transportních formátů (TFC)
- Poskytuje základ pro signalizaci indikátoru kombinace transportních formátů (TFCI) nebo TFRI

## Související pojmy

- [TFC – Transport Format Combination](/mobilnisite/slovnik/tfc/)
- [TFCI – Transport Format Combination Indicator](/mobilnisite/slovnik/tfci/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [TFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfs/)
