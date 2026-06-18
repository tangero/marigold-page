---
slug: "tad"
url: "/mobilnisite/slovnik/tad/"
type: "slovnik"
title: "TAD – Traffic Aggregate Description"
date: 2025-01-01
abbr: "TAD"
fullName: "Traffic Aggregate Description"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tad/"
summary: "Traffic Aggregate Description (TAD) je šablona nebo sada pravidel používaná v architektuře Policy and Charging Control (PCC) k identifikaci a klasifikaci skupiny IP toků náležejících k datovému toku s"
---

TAD je šablona nebo sada pravidel používaná v PCC k identifikaci a klasifikaci skupiny IP toků, což umožňuje jednotné zásady QoS a účtování pro agregovaný provoz.

## Popis

Traffic Aggregate Description (TAD) je komponenta v rámci 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), konkrétně definovaná ve specifikacích referenčního bodu Gx. Funguje jako porovnávací pravidlo nebo šablona filtru, kterou Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) poskytuje Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) – typicky umístěné v Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G nebo v Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G. Primární úlohou TAD je definovat sadu filtrů IP paketů, které společně identifikují skupinu jednotlivých IP toků a agregují je do jedné logické entity pro účely vymáhání politik a účtování.

Architektonicky je TAD součástí PCC pravidla. PCC pravidlo obsahuje informace pro detekci datového toku služby, definici přidružených parametrů QoS a specifikaci pravidel účtování. Když se služba (např. relace streamování videa) skládá z více souběžných IP toků (např. video, audio a signalizační provoz), je definování samostatného PCC pravidla pro každý tok neefektivní. Místo toho může jediné PCC pravidlo odkazovat na TAD. Samotný TAD obsahuje jeden nebo více informačních prvků filtru paketů. Každý filtr paketů používá parametry jako zdrojové/cílové IP adresy a čísla portů, typ protokolu (např. TCP/[UDP](/mobilnisite/slovnik/udp/)) a potenciálně i informace z hlubší inspekce paketů (jako např. značky [DSCP](/mobilnisite/slovnik/dscp/)) k porovnání provozu. Všechny IP pakety, které odpovídají libovolnému filtru uvnitř TAD, jsou považovány za součást stejného Traffic Aggregate.

Jak to funguje: PCRF na základě profilu účastníka, informací o službě od Application Function ([AF](/mobilnisite/slovnik/af/)) a politik operátora určí potřebnou QoS a účtování pro službu. Formuluje PCC pravidla. Pro službu s více toky vytvoří PCC pravidlo, které obsahuje TAD s více filtry paketů. Toto PCC pravidlo je zřízeno směrem k PCEF přes rozhraní Gx. PCEF následně nainstaluje tyto filtry paketů do svého motoru pro detekci provozu. Když pakety uživatelské roviny procházejí, PCEF je porovnává proti všem nainstalovaným filtrům. Pakety odpovídající filtrům náležícím ke stejnému TAD jsou agregovány a PCEF aplikuje jedinou sadu akcí QoS (např. přiřazení ke konkrétnímu přenosovému kanálu se zaručenou přenosovou rychlostí, označení DSCP) a akcí účtování (např. počítání bajtů pro offline účtování) definovanou v nadřazeném PCC pravidle na celý agregát. Tím poskytuje jednotný nástroj pro správu politik pro komplexní službu.

## K čemu slouží

Traffic Aggregate Description byl zaveden, aby řešil rostoucí komplexitu moderních IP služeb, které se často skládají z více simultánních datových toků s různými charakteristikami, ale vyžadují jednotné zacházení z hlediska politik. Před koncepty jako TAD bylo vymáhání politik často prováděno na bázi jednotlivých toků, což mohlo vést k nekonzistentnímu zacházení s QoS mezi komponentami jedné služby a vytvářelo pro síť významnou signalizační a správní zátěž. Například hovor založený na IMS může mít samostatné toky pro audio, video a SIP signalizaci; jejich odlišné zacházení s QoS by mohlo degradovat uživatelský zážitek.

TAD to řeší tím, že umožňuje síťovému operátorovi definovat politiku zaměřenou na službu, nikoli na jednotlivý tok. Umožňuje PCRF popsat kompletní provozní stopu služby pomocí jediného pravidla, čímž zjednodušuje zřizování, monitorování a účtování politik. To je zvláště důležité pro sponzorované datové služby, zero-rating a specializované záruky QoS pro podnikové nebo IoT aplikace, kde je logika služby definována více koncovými body a protokoly. Vznik TAD byl motivován evolucí směrem k plně IP sítím v 3GPP Release 8 (EPS), kde se dynamické, na aplikaci zaměřené PCC stalo klíčovým kamenem pro umožnění sofistikované diferenciace služeb a monetizace nad rámec jednoduchého best-effort přístupu k internetu.

## Klíčové vlastnosti

- Šablona obsahující více filtrů paketů k identifikaci skupiny IP toků
- Používá se v rámci PCC pravidla pro detekci datového toku služby
- Umožňuje jednotnou aplikaci zásad QoS a účtování na agregovaný provoz
- Zjednodušuje správu politik pro služby s více toky (např. VoLTE, streamování videa)
- Zřizována PCRF směrem k PCEF přes rozhraní Gx
- Podporuje parametry filtrů jako 5-tici (IP adresy, porty, protokol) a DSCP

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description

---

📖 **Anglický originál a plná specifikace:** [TAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tad/)
