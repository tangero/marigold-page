---
slug: "ppp"
url: "/mobilnisite/slovnik/ppp/"
type: "slovnik"
title: "PPP – Priority Precedence Preemption"
date: 2025-01-01
abbr: "PPP"
fullName: "Priority Precedence Preemption"
category: "QoS"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ppp/"
summary: "PPP je mechanismus Quality of Service (QoS), který spravuje přidělování prostředků při přetížení sítě tím, že upřednostňuje datové toky. Umožňuje relacím s vysokou prioritou vytěsnit relace s nižší pr"
---

PPP je mechanismus QoS, který spravuje přidělování prostředků při přetížení tím, že upřednostňuje datové toky a umožňuje relacím s vysokou prioritou vytěsnit relace s nižší prioritou.

## Popis

Priority Precedence Preemption (PPP) je komplexní rámec pro správu Quality of Service (QoS) definovaný v řadě specifikací 3GPP. Funguje v rámci core networku a radio access networku k vynucování přidělování prostředků na základě politik, zejména za podmínek přetížení nebo omezené kapacity. Mechanismus je postaven na třech vzájemně propojených konceptech: Priority (relativní úroveň důležitosti přiřazená beareru nebo relaci), Precedence (pořadí, ve kterém jsou relace zřizovány nebo udržovány) a Preemption (akt ukončení nebo degradace relace s nižší prioritou za účelem uvolnění prostředků pro relaci s vyšší prioritou). Politiky PPP jsou typicky konfigurovány operátorem sítě a vynucovány síťovými funkcemi jako Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a gNB/Node B.

Z architektonického hlediska je PPP integrován do procedur zřizování relací a mobility. Když dorazí nový požadavek na relaci (např. zřízení [PDN](/mobilnisite/slovnik/pdn/) připojení nebo zřízení [PDU](/mobilnisite/slovnik/pdu/) session v 5G), síť kontroluje požadované parametry QoS, včetně hodnot Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)). ARP obsahuje úroveň priority, indikátor schopnosti vytěsnit a indikátor zranitelnosti vůči vytěsnění. Síťové entity používají tyto hodnoty ARP k rozhodování o řízení přístupu. Pokud jsou prostředky nedostatečné, síť může zamítnout nový požadavek s nízkou prioritou, nebo pokud má nový požadavek vysokou prioritu a schopnost vytěsnit, může spustit vytěsnění existující, zranitelné relace s nižší prioritou. Proces preempece zahrnuje síťově iniciované procedury modifikace nebo uvolnění beareru/relace za účelem získání prostředků zpět.

Fungování PPP zahrnuje kontinuální monitorování a rozhodování. Během handoverových scénářů, zejména do buněk s omezenou kapacitou, PPP zajišťuje úspěšný handover relací s vysokou prioritou, potenciálně na úkor zrušení relací s nižší prioritou. V systému 5G je logika PPP zabudována v rámci Network Slice Admission Control Function ([NSACF](/mobilnisite/slovnik/nsacf/)) a Access and Mobility Policy Control Function (AM-PCF) pro detailnější kontrolu. Klíčové specifikace jako TS 23.501 (5G System Architecture) a TS 23.203 (Policy and Charging Control) detailně popisují tyto procedury. PPP je klíčový pro umožnění diferenciace služeb a zajištění, že služby kritické pro činnost, jako jsou komunikace pro veřejnou bezpečnost ([MCPTT](/mobilnisite/slovnik/mcptt/)) nebo nouzové služby, mají zaručený přístup k síti i během katastrof nebo špičkových událostí, čímž podporuje spolehlivost sítě a společenské potřeby.

## K čemu slouží

PPP existuje, aby řešil základní problém správy omezených síťových prostředků spravedlivým a prioritním způsobem, zejména při přetížení. Jak se mobilní sítě vyvíjely, aby podporovaly různorodou směs služeb – od hlasových hovorů a prohlížení webu po služby kritické pro činnost IoT a nouzové komunikace – jednoduchý model přidělování prostředků 'kdo dřív přijde, ten dřív mele' se stal nedostatečným. Operátoři sítí potřebovali standardizovaný mechanismus, aby zajistili, že nejdůležitější služby se vždy dostanou na řadu, i kdy to znamenalo vytěsnění méně důležitého provozu. To bylo motivováno regulatorními požadavky (např. pro nouzová volání), komerčními potřebami (nabízení prémiových úrovní služeb) a technickými požadavky nových případů užití, jako jsou vozidlové komunikace a průmyslová automatizace.

Historicky měly rané celulární systémy omezenou diferenciaci QoS. Vytvoření PPP, zejména jako součást architektury Policy and Charging Control (PCC) zavedené ve 3GPP Release 7, poskytlo robustní, politikami řízený rámec. Odstranilo omezení dřívějších, statičtějších schémat priorit dynamickou integrací preempece do procedur správy relací a mobility. To umožňuje sítím být jak efektivní (plně využívat prostředky), tak odolné, a zajišťuje, že základní služby jsou udržovány při zatížení sítě, což je kritický požadavek pro moderní veřejnou bezpečnost a komerční závazky Grade of Service (GoS).

## Klíčové vlastnosti

- Řízení přístupu na základě politik využívající Allocation and Retention Priority (ARP)
- Dynamické vytěsnění existujících relací pro přijetí relací s vyšší prioritou
- Integrace do handoverových procedur pro správu přetížení
- Podpora více úrovní priority napříč různými typy služeb
- Vynucování napříč Core Network (CN) a Radio Access Network (RAN)
- Nezbytnost pro umožnění Mission Critical Services a záruk QoS u síťového sliceování

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TR 22.829** (Rel-17) — Enhancement for UAVs; Stage 1
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.841** (Rel-6) — Presence Service Architecture Specification
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- … a dalších 23 specifikací

---

📖 **Anglický originál a plná specifikace:** [PPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppp/)
