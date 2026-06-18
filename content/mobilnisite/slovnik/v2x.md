---
slug: "v2x"
url: "/mobilnisite/slovnik/v2x/"
type: "slovnik"
title: "V2X – Vehicle-to-Everything Application Server"
date: 2025-01-01
abbr: "V2X"
fullName: "Vehicle-to-Everything Application Server"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/v2x/"
summary: "V2X aplikační server (AS) je síťová funkce, která hostuje a spravuje V2X aplikace a služby. Umožňuje komunikaci mezi vozidly, infrastrukturou, chodci a sítěmi, čímž podporuje případy užití v oblasti b"
---

V2X je aplikační server (Application Server), který hostuje a spravuje aplikace umožňující komunikaci mezi vozidly, infrastrukturou, chodci a sítěmi za účelem zvýšení bezpečnosti, efektivity provozu a poskytování infotainmentu v rámci systémů 3GPP.

## Popis

Aplikační server pro komunikaci vozidlo-se-vším (V2X [AS](/mobilnisite/slovnik/as/)) je klíčová síťová entita v rámci architektury založené na službách (service-based architecture) 3GPP, speciálně navržená pro podporu služeb V2X komunikace. Funguje v aplikační vrstvě jádra sítě a rozhraní se dalšími síťovými funkcemi, jako je Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a V2X Control Function. V2X AS hostuje aplikační logiku pro různé V2X služby, jako jsou zprávy o kooperativním povědomí ([CAM](/mobilnisite/slovnik/cam/)), decentralizované zprávy o stavu prostředí ([DENM](/mobilnisite/slovnik/denm/)) a další funkce specifické pro V2X aplikace. Je zodpovědný za autorizaci služeb, správu konfigurace pro UE zapojená do V2X komunikace a potenciálně za směrování nebo zpracování zpráv na aplikační vrstvě, zejména pro síťově asistované režimy V2X komunikace.

Z architektonického hlediska může V2X AS podporovat různé režimy V2X komunikace definované 3GPP: přímou komunikaci (rozhraní PC5) a komunikaci zprostředkovanou sítí (rozhraní Uu). U komunikace založené na PC5 poskytuje V2X AS, často ve spolupráci s V2X Control Function, nezbytné parametry pro UE, jako jsou autorizační politiky, prioritu [ProSe](/mobilnisite/slovnik/prose/) na paket ([PPPP](/mobilnisite/slovnik/pppp/)) a konfiguraci pro sidelink rádiové rozhraní. U komunikace založené na Uu může fungovat jako aplikační server, který komunikuje s UE prostřednictvím sítě, což umožňuje širší distribuci zpráv nebo přístup k V2X službám v cloudu. V2X AS se rozhraní s UDM pro získání předplatitelských dat pro autorizaci V2X služeb a s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro vynucování politik souvisejících s V2X službami.

Jeho role se rozšiřuje na správu oblasti V2X služby (V2X service area), která definuje geografickou oblast, kde je UE autorizováno provádět V2X komunikaci. V2X AS může také komunikovat s externími poskytovateli V2X aplikací nebo s V2X Control Function, aby převedl požadavky služeb na síťové politiky. V pozdějších vydáních se jeho funkce rozvinuly, aby podporovaly pokročilejší služby, včetně kolektivního vnímání prostředí a koordinovaných manévrů, což vyžaduje sofistikovanější schopnosti agregace, zpracování a distribuce dat s nízkou latencí. V2X AS tedy není jen jednoduchý server, ale klíčový orchestrátor, který propojuje požadavky V2X aplikací s možnostmi sítě 3GPP a zajišťuje bezpečné, spolehlivé a efektivní poskytování služeb pro propojená vozidla.

## K čemu slouží

V2X AS byl vytvořen, aby poskytoval standardizovanou, síťovou platformu pro hostování a správu V2X aplikací v rámci celulárního ekosystému. Před jeho specifikací byla V2X komunikace primárně založena na standardech pro vyhrazenou krátkou komunikaci (DSRC), jako je IEEE 802.11p, kterým chyběla bezproblémová integrace s celulárními sítěmi široké oblasti pro správu služeb, zabezpečení a škálovatelnost. Integrace V2X služeb do architektury 3GPP, počínaje vydáním 14, byla motivována potřebou automobilového průmyslu po globálním, budoucím řešení, které využívá všudypřítomné celulární pokrytí, síťové bezpečnostní rámce a rozvíjející se schopnosti 5G pro pokročilé automatizované řízení.

V2X AS řeší problém, jak efektivně autorizovat, konfigurovat a spravovat obrovské množství vozidlových UE (V-UE) a jejich V2X služeb. Poskytuje centralizovaný bod pro aplikační logiku a vynucování politik, což je klíčové pro bezpečnostně kritické aplikace. Bez takové síťové funkce by správa servisních parametrů, bezpečnostních přihlašovacích údajů a geografických oblastí služeb pro miliony vozidel byla velmi neefektivní a nejistá. V2X AS umožňuje síťovým operátorům a poskytovatelům služeb nabízet diferencované V2X služby, zajišťuje, že UE fungují pouze tam, kde jsou k tomu autorizována, a připravuje cestu pro síťově asistovanou a síťově plánovanou V2X komunikaci, která ve srovnání s čistě distribuovanými ad-hoc přístupy zlepšuje spolehlivost a využití zdrojů.

## Klíčové vlastnosti

- Hostuje aplikační logiku pro V2X služby (např. CAM, DENM)
- Poskytuje autorizaci V2X služeb a správu konfigurace pro UE
- Spravuje oblasti V2X služeb a související parametry
- Rozhraní se základními síťovými funkcemi (UDM, PCF, NEF) pro politiky a předplatné
- Podporuje jak přímý (PC5), tak síťový (Uu) režim V2X komunikace
- Může usnadňovat směrování a agregaci zpráv pro síťově asistovanou V2X komunikaci

## Definující specifikace

- **TS 23.786** (Rel-16) — Study on V2X architecture enhancements for EPS and 5GS
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.846** (Rel-18) — Technical Report
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [V2X na 3GPP Explorer](https://3gpp-explorer.com/glossary/v2x/)
