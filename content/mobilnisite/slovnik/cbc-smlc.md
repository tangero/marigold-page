---
slug: "cbc-smlc"
url: "/mobilnisite/slovnik/cbc-smlc/"
type: "slovnik"
title: "CBC-SMLC – Cell Broadcast Centre - Serving Mobile Location Centre Interface"
date: 2025-01-01
abbr: "CBC-SMLC"
fullName: "Cell Broadcast Centre - Serving Mobile Location Centre Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbc-smlc/"
summary: "CBC-SMLC je standardizované rozhraní definované v 3GPP pro komunikaci mezi Cell Broadcast Centre (CBC) a Serving Mobile Location Centre (SMLC). Umožňuje CBC vyžádat si od SMLC polohové informace pro s"
---

CBC-SMLC je standardizované rozhraní 3GPP mezi Cell Broadcast Centre a Serving Mobile Location Centre, které umožňuje CBC vyžádat si polohové informace pro geograficky cílené vysílací služby, jako jsou veřejná varování.

## Popis

Rozhraní CBC-SMLC je kritickou součástí architektury 3GPP, která zprostředkovává interakci mezi dvěma odlišnými síťovými entitami: Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), odpovědným za správu a distribuci zpráv buňkového vysílání, a Serving Mobile Location Centre (SMLC), odpovědným za určování polohy mobilních zařízení. Toto rozhraní je formálně specifikováno v 3GPP Technical Specification (TS) 43.059. Funguje jako point-to-point rozhraní, typicky využívající protokoly jako Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) nebo Diameter v závislosti na generaci jádra sítě (např. GSM/UMTS vs. LTE/5GC), pro přenos potřebných signalizačních zpráv.

Architektonicky se CBC-SMLC nachází v doméně jádra sítě a propojuje servisní vrstvu (CBC) s vrstvou lokalizačních služeb (SMLC). Když CBC potřebuje vyslat zprávu do specifické geografické oblasti – například do okresu nebo zóny kolem místa mimořádné události – samo o sobě nemá mapování mezi geografickými souřadnicemi a buňkami rádiové sítě (např. základnovými stanicemi, [eNB](/mobilnisite/slovnik/enb/), gNB), které tuto oblast pokrývají. CBC použije rozhraní CBC-SMLC k odeslání žádosti o polohu do SMLC. Tato žádost obsahuje popis cílové geografické oblasti, což může být například elipsoidní bod s kruhem nejistoty, polygon nebo seznam předdefinovaných servisních oblastí.

SMLC tuto žádost zpracuje přeložením poskytnutého geografického popisu na seznam relevantních identifikátorů buněk. Tento překlad se opírá o znalost topologie rádiové sítě a map pokrytí, kterou SMLC disponuje. SMLC poté vrátí tento seznam identifikátorů buněk (např. [CGI](/mobilnisite/slovnik/cgi/), [ECI](/mobilnisite/slovnik/eci/), [NCI](/mobilnisite/slovnik/nci/)) zpět CBC přes stejné rozhraní. Vyzbrojeno tímto seznamem buněk může CBC následně instruovat příslušné uzly Radio Access Network (RAN) – přes jiná rozhraní jako [CBC-BSC](/mobilnisite/slovnik/cbc-bsc/), CBC-RNC nebo CBC-eNB/gNB – aby zprávu vysílaly pouze v těchto konkrétních buňkách, čímž dosáhne přesného geografického cílení. Tento proces zajišťuje efektivitu sítě tím, že se vyhne zbytečnému vysílání v necílených buňkách, a je zásadní pro regulatorní systémy veřejného varování jako EU-Alert nebo [CMAS](/mobilnisite/slovnik/cmas/).

Rozhraní podporuje různé typy žádostí o polohu, včetně okamžitých žádostí pro jednorázové vysílání a odložených žádostí pro naplánované vysílání. Zvládá také chybové scénáře, například když SMLC není schopno oblast přeložit nebo když je požadovaná oblast příliš rozsáhlá. Bezpečnostní hlediska jsou prvořadá, protože rozhraní může přenášet citlivé polohové informace; proto často využívá bezpečnostní mechanismy jako firewally a zabezpečená spojení protokolů, aby zabránilo neoprávněnému přístupu nebo úniku dat.

## K čemu slouží

Rozhraní CBC-SMLC bylo vytvořeno k řešení problému geograficky cíleného vysílání v mobilních sítích. Před jeho standardizací byly služby buňkového vysílání z velké části omezeny na vysílání v rámci celé sítě nebo na úrovni buněk, bez efektivního mechanismu pro cílení na konkrétní geografickou oblast definovanou souřadnicemi (např. záplavová zóna). Toto omezení bylo obzvláště kritické pro systémy veřejného varování (PWS), kde musí být nouzové výstrahy doručeny pouze ohrožené populaci, čímž se zabrání zbytečné panice nebo informačnímu přetížení v bezpečných oblastech.

Historicky, bez tohoto rozhraní, vyžadovala implementace vysílání na základě polohy proprietární, neinteroperabilní řešení nebo manuální konfiguraci seznamů buněk operátory, což bylo náchylné k chybám, pomalé a neškálovatelné. Zavedení CBC-SMLC v 3GPP Release 8, jako součást vylepšené služby buňkového vysílání (eCBS) a funkcí Earthquake and Tsunami Warning System (ETWS), poskytlo standardizovaný, automatizovaný způsob, jak může CBC dynamicky získat správný seznam buněk z lokalizační infrastruktury sítě. Tím se vyřešila omezení předchozích přístupů tím, že bylo umožněno přesné geografické cílení v reálném čase založené na vlastním a aktuálním porozumění pokrytí buněk v síti.

Motivace vycházela z regulatorních požadavků (např. FCC CMAS, EU EU-Alert), které ukládají mobilním operátorům povinnost doručovat geograficky cílené nouzové výstrahy. Rozhraní umožňuje systému varování (připojenému k CBC) specifikovat oblast na mapě a mobilní síť automaticky zvládne technický překlad na rádiové buňky. Toto oddělení odpovědností – kde CBC zpracovává obsah zpráv a plánování a SMLC se stará o rádiovou geografii – vytváří flexibilní, efektivní a do budoucna připravenou architekturu, která podporuje vyvíjející se lokalizační technologie a nasazení RAN.

## Klíčové vlastnosti

- Standardizovaný překlad geografické oblasti na seznam buněk
- Podpora více tvarů geografických oblastí (např. bod s poloměrem, polygon)
- Podpora protokolů MAP (GSM/UMTS) a Diameter (EPS/5GS)
- Zpracování jak okamžitých, tak odložených žádostí o polohu
- Zpracování chyb pro nerozpoznané nebo příliš rozsáhlé požadavky na oblast
- Umožňuje systémy veřejného varování (PWS) vyhovující regulatorním požadavkům

## Definující specifikace

- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [CBC-SMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbc-smlc/)
