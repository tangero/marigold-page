---
slug: "mvepp"
url: "/mobilnisite/slovnik/mvepp/"
type: "slovnik"
title: "MVEPP – MCVideo Emergency Private Priority"
date: 2025-01-01
abbr: "MVEPP"
fullName: "MCVideo Emergency Private Priority"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvepp/"
summary: "Specifická úroveň priority QoS a související postupy v rámci služby MCVideo, které zajišťují, že nouzové privátní videohovory získají nejvyšší možné přidělení síťových zdrojů a možnosti vytěsnění. Je"
---

MVEPP je specifická úroveň priority QoS a související postupy v rámci služby MCVideo, které zajišťují, že nouzové privátní videohovory získají nejvyšší přidělení síťových zdrojů a možnosti vytěsnění.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Emergency Private Priority (MVEPP) není samostatná služba, ale kritický atribut kvality služeb (QoS) a procedurální rámec definovaný ve specifikacích 3GPP pro MCVideo. Představuje nejvyšší úroveň priority pro privátní hovory MCVideo, speciálně navrženou pro zaručení výkonu relací MCVideo Emergency Private Call ([MVEPC](/mobilnisite/slovnik/mvepc/)). MVEPP řídí, jak síť rezervuje, přiděluje a chrání potřebnou šířku pásma, latenci a spolehlivost pro tyto životně důležité videoproudy od konce ke konci.

Technicky je MVEPP implementován kombinací standardizovaných parametrů QoS a síťových politik. V LTE se mapuje na specifické QoS Class Identifiers (QCIs) s charakteristikami vhodnými pro konverzační video v reálném čase, ale s dodatečným atributem přidělení pro použití v 'Mission Critical'. V systémech 5G se mapuje na standardizované 5G QoS Indicators (5QIs), které definují podobný rozpočet zpoždění paketů, míru chybovosti paketů a úroveň priority. Klíčovým rozlišovacím znakem MVEPP je jeho úroveň priority, která je nastavena vyšší než u jakékoli komerční služby a dokonce vyšší než u jiného ne-nouzového provozu pro kritickou infrastrukturu. Tato priorita je signalizována během procedury zřizování relace (definované v TS 24.281) od klienta [MC](/mobilnisite/slovnik/mc/) k serveru MCVideo, který následně interaguje s architekturou Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) v jádru sítě.

Architektura PCC, zahrnující Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), převádí požadavek služby MVEPP na konkrétní síťová pravidla. Tato pravidla jsou vynucována na User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC nebo na [PGW](/mobilnisite/slovnik/pgw/) v EPC pro filtrování paketů a označování QoS, a klíčově také v Radio Access Network (RAN). RAN tato pravidla používá pro plánování v uplinku a downlinku, čímž zajišťuje, že pakety pro relaci MVEPP jsou obslouženy před ostatními. Dále MVEPP umožňuje možnosti vytěsnění. V situacích silného zahlcení může být síť autorizována k vytěsnění (tj. snížení priority nebo odpojení) zdrojů od stávajících relací s nižší prioritou (jako je komerční videoproud) za účelem přijetí nebo udržení příchozí relace MVEPC založené na MVEPP. Tento řetězec vynucování od konce ke konci – od signalizace na úrovni služby přes politiky v jádru sítě až po plánování v RAN – je tím, co definuje a implementuje MVEPP.

## K čemu slouží

Účelem MVEPP je poskytnout technickou 'průraznost' službě MCVideo Emergency Private Call. Definovat službu jako MVEPC je nedostatečné, pokud síť zachází s jejími datovými pakety se stejnou best-effort prioritou jako s videem na sociální síti. MVEPP existuje pro řešení základního problému nedostatku zdrojů a soupeření o ně během nouzových situací, aby bylo zajištěno, že kritická videokomunikace není degradována nebo blokována síťovým zahlcením.

Historicky používaly sítě pro veřejnou bezpečnost vyhrazené úzkopásmové spektrum, které inherentně upřednostňovalo jejich provoz, ale postrádalo možnosti vysoké šířky pásma jako video. Když veřejná bezpečnost přešla na širokopásmové LTE a 5G a sdílela infrastrukturu s komerčními uživateli, byl potřebný mechanismus pro replikaci a překonání garantovaného přístupu tradičních systémů. MVEPP byl vytvořen jako takový mechanismus v rámci standardů 3GPP. Řeší omezení dřívějších schémat priority, která nebyla specificky přizpůsobena nebo garantována pro jedinečné požadavky nouzového privátního videa – požadavky, které zahrnují nejen vysokou prioritu, ale také striktní limity latence pro interaktivitu a spolehlivost pro povědomí o situaci. Zajišťuje, že slib 'mission-critical' na sítích komerční třídy je technicky vynutitelný a spolehlivý.

## Klíčové vlastnosti

- Definuje nejvyšší úroveň priority QoS pro privátní relace MCVideo
- Mapuje se na standardizované QCIs (LTE) a 5QIs (5G) s vysokou prioritou pro video pro kritickou infrastrukturu
- Integrováno s architekturou PCC 3GPP pro dynamické vynucování politik
- Umožňuje vytěsnění zdrojů od relací s nižší prioritou během zahlcení
- Signalizováno jako součást procedury zřizování relace MCVideo
- Zajišťuje end-to-end garanci síťových zdrojů od jádra sítě po RAN

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [MVEPC – MCVideo Emergency Private Call](/mobilnisite/slovnik/mvepc/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVEPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvepp/)
