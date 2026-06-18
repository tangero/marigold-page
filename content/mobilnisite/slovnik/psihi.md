---
slug: "psihi"
url: "/mobilnisite/slovnik/psihi/"
type: "slovnik"
title: "PSIHI – PDU Set Integrated Handling Information"
date: 2026-01-01
abbr: "PSIHI"
fullName: "PDU Set Integrated Handling Information"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/psihi/"
summary: "Protokolový mechanismus v 5G-Advanced, který poskytuje integrované řídicí informace pro zpracování sad protokolových datových jednotek (PDU) v uživatelské rovině a optimalizuje přenos dat pro aplikace"
---

PSIHI je protokolový mechanismus 5G-Advanced, který poskytuje integrované řídicí informace pro zpracování sad protokolových datových jednotek (PDU) za účelem optimalizace přenosu dat v uživatelské rovině na základě sémantiky aplikační vrstvy.

## Popis

[PDU](/mobilnisite/slovnik/pdu/) Set Integrated Handling Information (PSIHI) je funkce protokolu zavedená ve specifikaci 3GPP Release 18 jako součást vylepšení 5G-Advanced, navržená ke zlepšení zpracování datových jednotek v uživatelské rovině. Odkazuje na řídicí informace, které jsou integrovány se sadou protokolových datových jednotek (PDU), aby poskytovaly instrukce, jak mají být tyto PDU zpracovávány, přenášeny nebo spravovány kolektivně sítí a uživatelským zařízením (UE). PSIHI je přenášeno v rámci datového toku, typicky v hlavičkách paketů nebo přidružených metadatech, a přenáší sémantiku související s aplikačními daty, jako jsou závislosti mezi PDU, termíny zpracování nebo pravidla agregace. To umožňuje systému 5G aplikovat optimalizované strategie zpracování – jako je plánování, duplikace nebo zahození – na základě potřeb aplikace, namísto nezávislého zacházení s každou PDU.

Architektonicky PSIHI funguje ve vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) a potenciálně interaguje s vyššími vrstvami, jako je Service Data Adaptation Protocol ([SDAP](/mobilnisite/slovnik/sdap/)) a aplikační vrstva v zásobníku protokolů 5G. Je generováno aplikací nebo síťovou funkcí (např. edge serverem) a vloženo do sady PDU před přenosem přes rozhraní vzduchu. gNodeB (gNB) a UE tyto informace používají k inteligentním rozhodnutím v rádiové přístupové síti (RAN) a v jádru sítě. Například PSIHI může indikovat, že skupina PDU patří k jednomu snímku videa, což umožňuje RANu je upřednostnit nebo zahodit jako celek pro zachování kvality služby. Mezi klíčové komponenty patří samotné pole PSIHI, které obsahuje příznaky nebo parametry definující pravidla zpracování, a přidružené protokoly, které tyto informace parsují a podle nich jednají, jak je specifikováno v technických specifikacích jako TS 38.300 a TS 38.835.

V praxi PSIHI zvyšuje efektivitu uživatelské roviny tím, že umožňuje zpracování dat s ohledem na kontext. Když sada PDU s PSIHI dorazí do gNB, plánovač může zohlednit integrované informace pro optimalizaci alokace prostředků – například tím, že zajistí kontinuální přenos všech PDU v sadě pro snížení latence u aplikací citlivých na čas. Na straně UE přijímač používá PSIHI ke správnému opětovnému sestavení nebo zpracování PDU, což může snížit nároky na vyrovnávací paměť a zlepšit výkon aplikace. Tento mechanismus je zvláště cenný pro pokročilé případy použití, jako je rozšířená realita ([XR](/mobilnisite/slovnik/xr/)), průmyslový IoT a ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), kde je sémantika dat klíčová pro splnění přísných požadavků. Tím, že PSIHI překlenuje propast mezi záměrem aplikace a chováním sítě, podporuje dynamičtější a efektivnější systémy 5G.

## K čemu slouží

PSIHI bylo vytvořeno, aby řešilo omezení tradičního zpracování [PDU](/mobilnisite/slovnik/pdu/) v sítích 5G, kde je každá datová jednotka zpracovávána nezávisle bez povědomí o kontextu na aplikační úrovni. Předchozí přístupy, ač efektivní pro generický datový provoz, nedokázaly uspokojit složité požadavky vznikajících aplikací, jako je [XR](/mobilnisite/slovnik/xr/), autonomní systémy a hmatový internet, které zahrnují strukturované datové sady s vzájemnými závislostmi a přísnými časovými omezeními. Bez integrovaných informací pro zpracování by síť mohla neúmyslně zahodit nebo zpozdit kritické PDU, což by zhoršilo uživatelský zážitek a spolehlivost.

Hlavním problémem, který PSIHI řeší, je neefektivita ve využívání prostředků a správě kvality služeb pro služby citlivé na aplikaci. Poskytnutím explicitních instrukci pro zpracování v rámci datového toku umožňuje RANu a jádru sítě optimalizovat přenosové strategie na základě sémantické znalosti. To snižuje režii ve srovnání s signalizací mimo pásmo a umožňuje adaptace v reálném čase, jako je seskupování PDU pro společné plánování nebo aplikaci specifických mechanismů obnovy po chybě. Motivace pro PSIHI vychází z vize 5G-Advanced podporovat inteligentnější a flexibilnější sítě, kde jsou vylepšení uživatelské roviny klíčová pro dosažení vyššího výkonu a energetické účinnosti.

Historicky se dřívější specifikace 3GPP spoléhaly na QoS toky a body kódu diferencovaných služeb ([DSCP](/mobilnisite/slovnik/dscp/)) pro diferenciaci provozu, ale tyto mechanismy postrádaly granularitu pro koordinaci na úrovni PDU v rámci toku. PSIHI navazuje na koncepty jako duplikace PDCP a zpracování datových shluků a rozšiřuje je o integrované řízení, aby podpořilo vyvíjející se potřeby vertikálních odvětví. Jeho zavedení v Release 18 bylo motivováno požadavky průmyslu na lepší podporu XR a průmyslových aplikací, jak je dokumentováno ve specifikacích jako TS 26.804 a TS 23.501, kde zpracování mediálních snímků a sad senzorových dat vyžaduje těsnou integraci mezi aplikační a síťovou vrstvou.

## Klíčové vlastnosti

- Integrované řídicí informace vložené do sad PDU pro zpracování s ohledem na aplikaci
- Umožňuje kolektivní plánování, upřednostňování a zahození PDU na základě sémantických pravidel
- Podporuje pokročilé případy použití, jako je XR, URLLC a průmyslový IoT, se strukturovanými datovými závislostmi
- Snižuje signalizační režii tím, že přenáší instrukce pro zpracování v pásmu spolu s uživatelskými daty
- Zvyšuje efektivitu RANu prostřednictvím alokace prostředků a správy chyb s ohledem na kontext
- Usnadňuje zlepšení QoS a uživatelského zážitku sladěním chování sítě s požadavky aplikace

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR

---

📖 **Anglický originál a plná specifikace:** [PSIHI na 3GPP Explorer](https://3gpp-explorer.com/glossary/psihi/)
