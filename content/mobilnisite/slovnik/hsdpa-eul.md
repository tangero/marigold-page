---
slug: "hsdpa-eul"
url: "/mobilnisite/slovnik/hsdpa-eul/"
type: "slovnik"
title: "HSDPA/EUL – High Speed Downlink Packet Access / Enhanced Uplink"
date: 2025-01-01
abbr: "HSDPA/EUL"
fullName: "High Speed Downlink Packet Access / Enhanced Uplink"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hsdpa-eul/"
summary: "HSDPA/EUL jsou vylepšení 3GPP UMTS pro vysokorychlostní paketová data. HSDPA zvyšuje rychlost na downlinku pomocí adaptivní modulace a sdílených kanálů. EUL (HSUPA) zlepšuje kapacitu a latenci na upli"
---

HSDPA/EUL je dvojice vylepšení 3GPP UMTS, kde HSDPA zvyšuje rychlost na downlinku a EUL zlepšuje kapacitu a latenci na uplinku pro vysokorychlostní paketová data.

## Popis

High Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) a Enhanced Uplink (EUL), známé také jako High Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)), jsou klíčová vylepšení rádiové přístupové sítě UMTS (Universal Mobile Telecommunications System) definovaná 3GPP. Společně tvoří [HSPA](/mobilnisite/slovnik/hspa/) (High Speed Packet Access), což výrazně zlepšuje výkon sítí 3G pro paketově přepínané datové služby. Tyto technologie byly zavedeny, aby uspokojily rostoucí poptávku po mobilním širokopásmovém připojení a multimediálních aplikacích.

HSDPA zásadně mění schéma downlinkového přenosu oproti UMTS Release 99. Nahrazuje vyhrazené kanály ([DCH](/mobilnisite/slovnik/dch/)) vysokorychlostním, časově sdíleným transportním kanálem zvaným High-Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)). Mezi klíčové techniky patří Adaptive Modulation and Coding ([AMC](/mobilnisite/slovnik/amc/)), kde NodeB rychle upravuje modulační schéma (QPSK, [16QAM](/mobilnisite/slovnik/16qam/)) a kódovací rychlost na základě okamžitých hlášení o kvalitě kanálu od uživatelského zařízení (UE). Fast Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) je implementován v NodeB, což umožňuje rychlé retransmise a kombinaci neúspěšných paketů bez zapojení vyšších vrstev, a tím snižuje latenci. Rychlé plánování (scheduling) je také přesunuto z řadiče rádiové sítě (RNC) do NodeB, což umožňuje rozhodování na úrovni milisekund na základě reálných podmínek kanálu a kritérií spravedlnosti.

Enhanced Uplink (EUL) aplikuje podobné principy na uplink. Zavádí nový transportní kanál, Enhanced Dedicated Channel (E-DCH), který podporuje funkce jako kratší přenosové časové intervaly (TTI), rychlé plánování řízené NodeB a HARQ na uplinku. V modelu plánování UE žádá o povolení k přenosu dat odesláním plánovacích informací do NodeB, který následně přiděluje uplinkové zdroje prostřednictvím absolutních nebo relativních povolení. To umožňuje efektivnější využití zdroje výkonu na uplinku, což je kritické omezení, a snižuje přenosová zpoždění. Architektura také zavádí nové MAC entity jak v UE (MAC-e/es), tak v NodeB (MAC-e) pro zpracování rychlého plánování a HARQ procesů.

Kombinované nasazení HSDPA a EUL mění UMTS na vysoce efektivní paketově přepínanou přístupovou síť. Poskytuje základ pro mobilní širokopásmové služby a podporuje aplikace jako vysokorychlostní prohlížení webu, streamování videa a stahování velkých souborů. Zlepšení výkonu – vyšší špičkové datové rychlosti, zvýšená spektrální účinnost a nižší latence – byla klíčová pro konkurenceschopnost sítí 3G vůči vyvíjejícím se pevným širokopásmovým sítím a jiným bezdrátovým technologiím. Vývoj HSPA pokračoval v následujících vydáních 3GPP s funkcemi jako MIMO, modulace vyššího řádu a vícekanálový provoz, což prodloužilo jeho relevanci hluboko do éry 4G.

## K čemu slouží

HSDPA a EUL byly vyvinuty k řešení základních omezení původních specifikací UMTS Release 99 pro paketové datové služby. Zatímco UMTS Release 99 zavedlo WCDMA pro hlas a data, jeho paketově přepínané schopnosti byly limitovány inherentními neefektivitami. Použití vyhrazených kanálů (DCH) pro data znamenalo, že rádiové zdroje byly staticky přiděleny na dobu trvání spojení, což vedlo ke špatnému využití zdrojů pro trhavý (bursty) provoz. Plánování sídlilo v RNC, daleko od rádiového rozhraní, což mělo za následek pomalé reakční časy (stovky milisekund) na měnící se rádiové podmínky. To způsobovalo nízkou spektrální účinnost a omezené dosažitelné datové rychlosti.

Primární motivací pro HSDPA bylo umožnit nákladově efektivní, vysokorychlostní downlink pro datově orientované služby, jako je prohlížení webu a streamování videa, které jsou typicky asymetrické. Cílem bylo dramaticky zvýšit špičkové datové rychlosti, zlepšit spektrální účinnost a snížit latenci. EUL byl následně vyvinut k řešení úzkého hrdla na uplinku, protože interaktivní aplikace (videokonference, online hry, nahrávání velkých souborů) a peer-to-peer služby vyžadovaly lepší výkon na uplinku. Stávající uplink trpěl vysokou latencí a nízkou kapacitou kvůli centralizovanému plánování v RNC a absenci rychlých retransmisních mechanismů na fyzické vrstvě.

Historicky tyto vylepšení představovaly konkurenční reakci 3GPP na jiné vyvíjející se bezdrátové datové technologie a byly klíčové pro obchodní případ operátorů. Umožnily sítím UMTS nabídnout skutečný mobilní širokopásmový zážitek a překlenout mezeru mezi 3G a nadcházejícím standardem 4G LTE. Přesunutím klíčových funkcí správy rádiových zdrojů, jako je plánování a HARQ, do NodeB využilo HSPA konceptu 'chytré antény', díky čemuž se rozhraní vzduchu stalo adaptivnějším a efektivnějším, což se stalo základním konstrukčním principem pro všechny budoucí generace mobilních sítí.

## Klíčové vlastnosti

- High-Speed Downlink Shared Channel (HS-DSCH) pro efektivní sdílení zdrojů mezi uživateli
- Adaptive Modulation and Coding (AMC) založené na rychlé zpětné vazbě Channel Quality Indicator (CQI)
- Fast Hybrid ARQ (HARQ) s měkkým kombinováním (soft combining) na fyzické vrstvě
- Rychlé paketové plánování (scheduling) umístěné v NodeB (základnové stanici) pro rozhodování na úrovni milisekund
- Enhanced Dedicated Channel (E-DCH) pro uplink s plánováním řízeným NodeB
- Možnost kratšího 2ms přenosového časového intervalu (TTI) pro snížení latence

## Související pojmy

- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [H-ARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/h-arq/)
- [AMC – Adaptive Modulation and Coding](/mobilnisite/slovnik/amc/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [HSDPA/EUL na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsdpa-eul/)
