---
slug: "mmtp"
url: "/mobilnisite/slovnik/mmtp/"
type: "slovnik"
title: "MMTP – MPEG Media Transport Protocol"
date: 2025-01-01
abbr: "MMTP"
fullName: "MPEG Media Transport Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmtp/"
summary: "MMTP je doručovací protokol ve standardu MMT, používaný pro přenos multimediálních dat přes IP sítě. Zpracovává paketizaci, multiplexování a časovou synchronizaci mediálních streamů, čímž zajišťuje ef"
---

MMTP je MPEG Media Transport Protocol používaný ve standardu MMT pro doručování multimédií přes IP sítě, který zajišťuje paketizaci, multiplexování a časovou synchronizaci pro efektivní streamování.

## Popis

[MPEG](/mobilnisite/slovnik/mpeg/) Media Transport Protocol (MMTP) je klíčovou součástí standardu MPEG Media Transport ([MMT](/mobilnisite/slovnik/mmt/)), specifikovaný jako doručovací protokol pro přenos multimediálního obsahu ve formátu MMT přes paketové sítě. MMTP pracuje na aplikační vrstvě a je navržen pro efektivní a synchronizovaný přenos mediálních dat, signalizačních zpráv a metadat. Funguje tak, že zapouzdřuje mediální data, organizovaná do MMT Payload Units ([MPU](/mobilnisite/slovnik/mpu/)), do MMTP Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)) pro přenos přes transportní protokoly jako [UDP](/mobilnisite/slovnik/udp/)/IP. MMTP podporuje multiplexování více mediálních komponent (např. video, audio, titulky) do jediného toku, což umožňuje synchronizované přehrávání na přijímací straně. Protokol zahrnuje mechanismy pro časování a synchronizaci, využívá časová metadata a Composition Information ([CI](/mobilnisite/slovnik/ci/)), aby zajistil správné časové prezentování mediálních komponent. MMTP také poskytuje funkce pro odolnost proti chybám, včetně podpory Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)) a volitelné retransmise, pro udržení kvality služby v podmínkách ztrátových sítí. Mezi klíčové architektonické prvky patří MMTP Sender, který paketizuje a vysílá data, a MMTP Receiver, který znovu sestavuje a zpracovává příchozí PDU. MMTP používá strukturu paketů obsahující hlavičku s poli pro identifikaci paketu, pořadová čísla a časové informace, následovanou datovou částí obsahující mediální nebo signalizační data. Protokol je navržen jako flexibilní, podporuje jak streamovací, tak stahovací režimy doručování a dokáže se přizpůsobit různým šířkám pásma sítě. V kontextech 3GPP je MMTP odkazován pro multimediální streamovací aplikace, zejména ve specifikacích týkajících se doručování médií přes mobilní sítě. Umožňuje efektivní přenos kvalitního videa a audia, což usnadňuje služby jako živé streamování, video na vyžádání a vysílací služby. Návrh MMTP umožňuje doručování s nízkou latencí, což jej činí vhodným pro interaktivní aplikace, a integruje se s MMT signalizací pro správu relací a popis médií.

## K čemu slouží

MMTP byl vyvinut, aby řešil potřebu robustního a efektivního protokolu pro doručování multimediálního obsahu přes IP sítě, zejména ve scénářích vyžadujících vysokou kvalitu a synchronizaci. Předchozí protokoly jako [RTP](/mobilnisite/slovnik/rtp/) byly široce používány pro přenos médií v reálném čase, ale postrádaly integrovanou podporu pro multiplexování, časování a obnovu po chybách standardizovaným způsobem. MMTP poskytuje jednotné řešení v rámci architektury MMT, optimalizující doručování médií pro moderní sítě včetně mobilních, vysílacích a širokopásmových. Vytvoření MMTP bylo motivováno konvergencí vysílacích a širokopásmových služeb, kde je třeba obsah doručovat bezproblémově napříč různými typy sítí. Tradiční vysílací protokoly jako MPEG-2 TS nebyly navrženy pro IP sítě, což vedlo k neefektivitám a problémům s kompatibilitou. MMTP tuto mezeru zaplňuje tím, že nabízí paketový protokol podporující funkce jako FEC pro odolnost proti chybám a přesné časování pro synchronizaci, což je nezbytné pro obsah ve vysokém a ultra-vysokém rozlišení. Dále MMTP umožňuje adaptivní streamování tím, že dovoluje dynamické přizpůsobení mediálních streamů na základě síťových podmínek, čímž zlepšuje uživatelský zážitek. Je zvláště relevantní pro 3GPP, protože mobilní sítě se vyvíjejí pro podporu bohatých mediálních služeb, a poskytuje standardizovanou metodu pro efektivní přenos médií, která spolupracuje s dalšími technologiemi 3GPP jako DASH a služby založené na IMS.

## Klíčové vlastnosti

- Paketizace a přenos MMT Payload Units (MPU) v MMTP PDU
- Multiplexování více mediálních komponent (video, audio, metadata) do jediného streamu
- Podpora časování a synchronizace využívající časová metadata a Composition Information (CI)
- Mechanismy odolnosti proti chybám včetně Forward Error Correction (FEC) a volitelné retransmise
- Podpora jak streamovacích, tak stahovacích režimů doručování přes UDP/IP
- Návrh s nízkou latencí vhodný pro interaktivní a aplikace v reálném čase

## Související pojmy

- [MMT – MPEG Media Transport](/mobilnisite/slovnik/mmt/)
- [MPEG – Moving Pictures Experts Group](/mobilnisite/slovnik/mpeg/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [MMTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmtp/)
