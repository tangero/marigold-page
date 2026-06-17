---
slug: "mcch-rnti"
url: "/mobilnisite/slovnik/mcch-rnti/"
type: "slovnik"
title: "MCCH-RNTI – MBS Control Channel RNTI"
date: 2025-01-01
abbr: "MCCH-RNTI"
fullName: "MBS Control Channel RNTI"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcch-rnti/"
summary: "Dočasný identifikátor rádiové sítě (RNTI) zavedený v 5G NR pro specifický účel skramblování a identifikace PDCCH přenosů, které nesou přidělení zdrojů pro Multicast Control Channel (MCCH). Umožňuje UE"
---

MCCH-RNTI je dočasný identifikátor rádiové sítě používaný v 5G NR pro skramblování a identifikaci PDCCH přenosů, které nesou přidělení zdrojů pro Multicast Control Channel (MCCH).

## Popis

[MBS](/mobilnisite/slovnik/mbs/) Control Channel RNTI (MCCH-RNTI) je specializovaný identifikátor v systému 5G New Radio (NR), který spadá do širší třídy Radio Network Temporary Identifiers (RNTI). RNTI je v podstatě číslo používané jako identifikátor pro zprávy na fyzických a transportních kanálech, které primárně slouží jako skramblovací kód pro bity cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) připojené ke zprávám Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) vysílaným na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). MCCH-RNTI má jediný, vyhrazený účel: signalizovat plánovací informace pro Multicast Control Channel ([MCCH](/mobilnisite/slovnik/mcch/)), což je logický kanál nesoucí řídicí informace pro služby multicast a broadcast (MBS) založené na NR.

V proceduře fyzické vrstvy NR gNB (základnová stanice) naplánuje přenos transportního bloku MCCH na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)). Aby informovala UE o tomto plánu – specifikujícím časové/frekvenční zdroje a modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) – vysílá gNB zprávu formátu DCI 1_0 nebo 1_1 na PDCCH. Před přenosem gNB skrambluje bity CRC této DCI zprávy pomocí hodnoty MCCH-RNTI. Tento proces skramblování je klíčovou funkcí; 'adresuje' DCI zprávu všem UE, které mají zájem o MBS. UE nakonfigurovaná pro příjem služeb MBS budou mít zřízenu hodnotu MCCH-RNTI, typicky získanou ze systémové informace (SIB20).

Na straně UE provádí fyzická vrstva slepé dekódování na kandidátních pozicích PDCCH v rámci nakonfigurovaného prohledávacího prostoru. Pro každého kandidáta se pokouší dekódovat DCI a poté deskrambluje CRC pomocí své známé sady RNTI. Pokud kontrola CRC projde pomocí MCCH-RNTI, UE ví, že úspěšně dekódovala DCI zprávu určenou pro plánování MCCH. UE poté extrahuje plánovací parametry (jako přiřazení zdrojových bloků a MCS) z DCI a použije je k příjmu a dekódování odpovídajícího transportního bloku PDSCH, který obsahuje informace logického kanálu MCCH. Tento proces je vysoce efektivní, protože umožňuje jedné DCI zprávě naplánovat MCCH pro neomezený počet UE současně.

MCCH-RNTI je kritickou součástí řídicí roviny MBS v NR. Funguje spolu s dalšími RNTI souvisejícími s MBS, jako je [G-RNTI](/mobilnisite/slovnik/g-rnti/) (Group RNTI) používaný pro plánování Multicast Traffic Channel (MTCH). Použití vyhrazeného RNTI odděluje signalizaci řízení MBS od jiných typů plánování (např. UE-specifické C-RNTI, SI-RNTI pro systémovou informaci). Toto oddělení poskytuje jasnou kanalizaci, snižuje nejednoznačnost pro UE během slepého dekódování a umožňuje nezávislou konfiguraci a řízení výkonu plánovacích zpráv MBS. Jeho hodnota je pevně stanovena specifikací 3GPP, což zajišťuje interoperabilitu, a je používána v rámci specifického prohledávacího prostoru pro MBS nakonfigurovaného pro UE, což dále zefektivňuje proces monitorování.

## K čemu slouží

MCCH-RNTI byl zaveden v 3GPP Release 17, aby řešil specifickou mezeru v návrhu řídicí signalizace pro nové služby multicast a broadcast (MBS) založené na NR. V předchozím systému LTE eMBMS byly plánovací informace pro MCCH indikovány pomocí M-RNTI (MBMS RNTI) nebo prostřednictvím specifického plánování systémové informace. Návrh NR však klade důraz na flexibilitu, explicitní konfiguraci a jednotný rámec pro monitorování řídicích kanálů. Byl potřeba vyhrazený identifikátor, aby se řídicí plánování MBS čistě integrovalo do existujícího rámce NR DCI a PDCCH.

Bez vyhrazeného RNTI, jako je MCCH-RNTI, by síť musela používat méně efektivní metody. Například by mohla použít systémovou informaci ke statickému definování zdrojů MCCH, což postrádá plánovací flexibilitu, nebo by mohla nesprávně použít jiné RNTI (jako SI-RNTI), což by způsobilo zmatení a potenciální konflikty v chování UE. MCCH-RNTI poskytuje standardizovaný, jednoznačný mechanismus pro UE, aby objevila a dekódovala dynamický plán MCCH. To je klíčové, protože obsah MCCH (konfigurace MBS) se může měnit a jeho přenos nemusí být dokonale periodický, což vyžaduje dynamické plánování.

Vytvoření MCCH-RNTI bylo motivováno potřebou škálovatelného a efektivního řídicího mechanismu pro broadcastové služby v 5G. Řeší problém 'adresování' řídicí zprávy velké, dynamické skupině UE. Použitím společného, známého identifikátoru každé UE se zájmem o MBS monitoruje stejnou DCI skramblovanou s MCCH-RNTI. To je inherentně škálovatelnější než unicastová signalizace a dokonale zapadá do skupinové povahy MBS. Také zajišťuje budoucí odolnost návrhu, umožňujíc potenciální vylepšení v pozdějších releasech, kde by mohly být zavedeny více instancí MCCH nebo různé typy řídicích informací MBS, z nichž každá by mohla být adresována různými hodnotami RNTI odvozenými ze společné skupiny.

## Klíčové vlastnosti

- Pevná, standardizovaná hodnota RNTI definovaná v 3GPP TS 38.321 pro skramblování DCI souvisejícího s plánováním MCCH.
- Umožňuje skupinově adresované plánování, což dovoluje jedné DCI informovat všechna MBS-kompatibilní UE o zdrojích MCCH.
- Používá se výhradně pro PDCCH příkazy, které plánují PDSCH nesoucí informace logického kanálu MCCH.
- Integruje signalizaci řízení MBS do standardních procedur slepého dekódování a prohledávacích prostorů NR UE.
- Jeho hodnota je získána UE z MBS související systémové informace (např. SIB20).
- Funguje ve spojení s konfigurací prohledávacího prostoru specifického pro MBS pro efektivní monitorování UE.

## Související pojmy

- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)
- [G-RNTI – GERAN Radio Network Temporary Identity](/mobilnisite/slovnik/g-rnti/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MCCH-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcch-rnti/)
