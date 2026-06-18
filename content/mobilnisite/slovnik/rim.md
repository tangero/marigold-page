---
slug: "rim"
url: "/mobilnisite/slovnik/rim/"
type: "slovnik"
title: "RIM – Remote Interference Management"
date: 2026-01-01
abbr: "RIM"
fullName: "Remote Interference Management"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rim/"
summary: "Soubor technik v TDD sítích pro detekci a zmírnění rušení způsobeného vzdálenými základnovými stanicemi v důsledku dlouhých zpoždění šíření signálu. Je klíčový pro udržení výkonu uplinku ve velkých TD"
---

RIM je soubor technik v TDD sítích pro detekci a zmírnění rušení ze vzdálených základnových stanic, což je klíčové pro udržení výkonu uplinku ve velkých nasazeních.

## Popis

Remote Interference Management (RIM) je klíčová funkce v rádiových přístupových sítích založených na duplexu s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)), včetně LTE a NR (5G). Řeší specifický scénář rušení, kdy je příjem uplinku na postižené základnové stanici (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) degradován downlinkovými přenosy ze vzdálené rušící základnové stanice. K tomu dochází, protože rádiové signály se šíří konečnou rychlostí; na velmi dlouhé vzdálenosti (např. přes 100 km) může být přenosové zpoždění významné. V TDD systému všechny základnové stanice synchronizují své periody přenosu pro uplink a downlink. Pokud však zpoždění šíření od rušící základnové stanice je delší než ochranná perioda ([GP](/mobilnisite/slovnik/gp/)) nebo specifické časové mezery, její downlinkový signál může dorazit na postiženou základnovou stanici během jejího slotu pro příjem uplinku, což způsobí závažné rušení uplinkovým signálům od jejích vlastních blízkých uživatelských zařízení (UE).

Architektura RIM zahrnuje mechanismy pro detekci, měření, hlášení a zmírnění. Proces začíná tím, že postižená základnová stanice detekuje anomální vzorce rušení uplinku, které naznačují vzdálené rušení. Pro tento účel jsou definovány speciální referenční signály, jako je RIM Reference Signal ([RIM-RS](/mobilnisite/slovnik/rim-rs/)) v 5G NR. Postižený uzel měří charakteristiky rušení, které mohou zahrnovat odhad zpoždění šíření rušícího signálu. Tyto měřené informace pak mohou být nahlášeny rušícímu uzlu, a to přímo přes rozhraní Xn (mezi gNB v 5G) nebo nepřímo přes signalizaci v jádru sítě (např. přes rozhraní S1 nebo [NG](/mobilnisite/slovnik/ng/) v určitých scénářích).

Po obdržení hlášení o rušení může rušící základnová stanice zahájit zmírňující akce. Primární zmírňující technika zahrnuje dynamické upravení časování jejího přenosu, konkrétně posunutím nebo prodloužením její ochranné periody. Toto časové přizpůsobení zajišťuje, že její downlinkové přenosy neproniknou do okna příjmu uplinku vzdálené postižené stanice. Koordinace může být autonomní nebo s podporou sítě. Postupy RIM jsou detailně popsány napříč více specifikacemi vrstev 3GPP: fyzická vrstva (38.211 pro signály), vrstva 2/3 (38.321, 38.331 pro protokoly) a protokol XnAP (38.423, 38.473) pro signalizaci mezi uzly, která přenáší RIM informace. Tento vícevrstvý přístup zajišťuje, že vzdálené rušení je efektivně identifikováno a vyřešeno, čímž se zachovává kapacita uplinku a kvalita služby napříč rozlehlými TDD sítěmi.

## K čemu slouží

RIM byl vytvořen, aby vyřešil základní fyzické omezení velkých, synchronizovaných nasazení [TDD](/mobilnisite/slovnik/tdd/) sítí. Když mobilní operátoři chtěli využít TDD spektrum pro pokrytí širokých oblastí, často nasazovali základnové stanice na velmi vysoké stožáry (např. na horách nebo vysokých budovách) pro maximalizaci dosahu, narazili na neočekávané rušení uplinku. Toto rušení nepocházelo od sousedních buněk, ale od základnových stanic stovky kilometrů vzdálených. Hlavní příčinou je rychlost světla: signál z downlinku vzdálené základnové stanice může putovat několik set mikrosekund, což způsobí, že dorazí pozdě a narazí do místního uplinkového rámce na postiženém místě. Tradiční koordinace rušení (jako [ICIC](/mobilnisite/slovnik/icic/)/eICIC) se zaměřuje na blízké buňky a je pro tyto scénáře s extrémním zpožděním neúčinná.

Problém se stal akutnějším s adopcí vyšších TDD frekvencí (jako 2,3 GHz, 2,6 GHz a později mmWave v 5G) a snahou o větší velikosti buněk. Ochranné periody definované v dřívějších standardech byly pro tyto ultra-dlouhé interferenční dráhy nedostatečné. RIM poskytuje systematický rámec pro detekci tohoto specifického typu rušení, měření jeho charakteristik (jako zpoždění) a koordinaci řešení mezi zasaženými základnovými stanicemi. Řeší omezení statického návrhu struktury rámce tím, že umožňuje dynamické přizpůsobení časování přenosu na základě reálných interferenčních podmínek v síti.

Historicky zavedený v 3GPP Rel-5 pro základní koncepty a významně vylepšený v pozdějších vydáních, význam RIM rostl s globální expanzí TDD LTE a základní rolí TDD v 5G NR. Umožňuje operátorům nasazovat homogenní, synchronizované TDD sítě přes velké geografické oblasti, aniž by je omezovalo sporadické, obtížně diagnostikovatelné rušení uplinku, a tím odemyká plný potenciál pokrytí a kapacity pásem TDD spektra.

## Klíčové vlastnosti

- Detekuje rušení uplinku způsobené downlinkovými přenosy z velmi vzdálených TDD základnových stanic
- Využívá specializované referenční signály (např. RIM-RS) pro měření a identifikaci rušení
- Podporuje hlášení měření zpoždění a výkonu rušení rušícímu uzlu
- Umožňuje dynamické upravení časování přenosu nebo ochranné periody u rušiče pro zmírnění
- Definuje signalizační postupy přes rozhraní mezi základnovými stanicemi (Xn) a rozhraní jádra sítě
- Klíčový pro umožnění velkých, synchronizovaných nasazení TDD s vysokými základnovými stanicemi

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [RIM-RS – Remote Interference Management Reference Signal](/mobilnisite/slovnik/rim-rs/)
- [ICIC – Inter-Cell Interference Coordination](/mobilnisite/slovnik/icic/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 37.813** (Rel-12) — LTE-HRPD SON Use Cases & Solutions
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [RIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rim/)
