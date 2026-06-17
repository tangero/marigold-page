---
slug: "mocn"
url: "/mobilnisite/slovnik/mocn/"
type: "slovnik"
title: "MOCN – Multiple Operator Core Network"
date: 2026-01-01
abbr: "MOCN"
fullName: "Multiple Operator Core Network"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mocn/"
summary: "Architektura sdílení sítě, ve které více mobilních operátorů (MNO) sdílí stejnou infrastrukturu rádiového přístupového sítě (RAN), včetně základnových stanic a rádiových prostředků, při zachování nezá"
---

MOCN je architektura sdílení sítě, ve které více mobilních operátorů sdílí stejnou infrastrukturu rádiového přístupového sítě při zachování nezávislých jádrových sítí.

## Popis

MOCN je standardizovaná architektura sdílení sítě podle 3GPP, která umožňuje dvěma nebo více mobilním operátorům ([MNO](/mobilnisite/slovnik/mno/)) sdílet společnou rádiovou přístupovou síť (RAN). V tomto modelu je sdílená RAN, zahrnující NodeB v UMTS nebo eNodeB/gNB v LTE/5G, připojena k samostatným jádrovým sítím každého zúčastněného operátora. Sdílená RAN vysílá více identit veřejné pozemní mobilní sítě (PLMN), což umožňuje uživatelskému zařízení (UE) objevit a vybrat síť svého domovského operátora. Klíčovou architektonickou součástí je schopnost uzlu RAN směrovat počáteční požadavky na přístup UE ke správné jádrové síti na základě vybraného identifikátoru PLMN, typicky pomocí mechanismů jako je funkce výběru síťového uzlu založená na RAN (RAN-NNSF) nebo asistence jádrové sítě.

Operační tok začíná, když UE schopné výběru sítě identifikuje dostupné PLMN z systémových informací vysílaných sdílenou buňkou. Po výběru své domovské PLMN zahájí UE připojení. Uzel RAN (např. gNB v 5G) použije vybraný identifikátor PLMN, často ve spojení s informací pro pomoc při výběru síťového řezu (NSSAI) v 5G, aby určil příslušného operátora jádrové sítě a odpovídajícím způsobem směroval signalizaci ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)). Toto směrování je zásadní a je řízeno přes sdílená rozhraní, jako je rozhraní [N2](/mobilnisite/slovnik/n2/) (NG-C) v 5G, kde jeden uzel RAN udržuje samostatná logická spojení k funkcím správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) různých operátorů.

MOCN zahrnuje několik klíčových technických komponent: sdílený hardware a software RAN, vysílání více identifikátorů PLMN v blocích systémových informací (SIB) a funkci směrování v RAN s ohledem na PLMN. Vyžaduje také podporu výběru více PLMN v UE. Sdílená RAN musí spravovat rádiové prostředky (jako nosné a buňky) způsobem, který může obsluhovat účastníky všech sdílejících operátorů, případně na základě dohodnutých smluv o úrovni služeb (SLA) týkajících se rozdělení kapacity nebo stanovení priorit. Z pohledu jádrové sítě zůstává síť každého operátora zcela nezávislá, samostatně řešící autentizaci účastníků, řízení politik, účtování a směrování dat. Toto oddělení zajišťuje provozní autonomii a bezpečnost při maximalizaci efektivity nákladné infrastruktury RAN.

## K čemu slouží

MOCN byl vytvořen k řešení vysokých kapitálových ([CAPEX](/mobilnisite/slovnik/capex/)) a provozních ([OPEX](/mobilnisite/slovnik/opex/)) výdajů spojených s nasazením a údržbou hustých rádiových přístupových sítí, zejména s explozivním růstem poptávky po mobilních datech. Historicky každý operátor nasazoval svou vlastní exkluzivní RAN, což vedlo k duplikaci infrastruktury, zvýšeným nákladům na získávání lokalit a vyšší spotřebě energie. Pro nové hráče na trhu nebo menší operátory představovaly tyto náklady významnou překážku vstupu na trh a konkurenceschopného zavádění služeb. MOCN poskytuje standardizované řešení pro sdílení RAN, které operátorům umožňuje sdružovat své zdroje.

Primární problémy, které MOCN řeší, jsou neefektivní využití spektra a nadbytečná infrastruktura. Sdílením fyzických lokalit, antén a jednotek základnového pásma mohou operátorům výrazně snížit náklady na nasazení a údržbu. Umožňuje také rychlejší rozvoj sítě, zejména ve venkovských nebo nedostatečně pokrytých oblastech, kde by obchodní případ pro jednoho operátora mohl být slabý. Dále, ve scénářích s nedostatkem spektra, může MOCN umožnit operátorům sdílet licencovaná frekvenční pásma, což vede k lepší celkové spektrální účinnosti a zlepšenému uživatelskému zážitku díky kombinovanému pokrytí a kapacitě.

Před MOCN se mohli operátorům zapojit do sdílení lokalit (sdílení fyzického stožáru a napájení), ale postrádali standardizovanou metodu pro hluboké sdílení RAN, včetně sdíleného rádiového vybavení a spektra. Existovala proprietární řešení, ale ta vedla k závislosti na dodavateli a problémům s interoperabilitou. Standardizace MOCN organizací 3GPP, počínaje Release 6, poskytla dodavatelům neutrální, interoperabilní rámec. To bylo klíčové pro přijetí regulátory a pro umožnění složitých provozních modelů, jako je národní roamování nebo joint ventures, což zajišťuje spravedlivou konkurenci a zároveň podporuje zhušťování sítě a celkovou udržitelnost odvětví.

## Klíčové vlastnosti

- Sdílená infrastruktura RAN vysílající více identifikátorů PLMN
- Směrování počátečního přístupu UE ke správné jádrové síti s ohledem na PLMN
- Podpora nezávislých jádrových sítí pro každého operátora
- Standardizovaná rozhraní (Iu, S1, N2) pro připojení více operátorů
- Schopnost UE vybrat síť ze sdílených buněk
- Flexibilní správa prostředků a potenciální rozdělení na základě SLA

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study
- **TS 22.805** (Rel-12) — RAN User Plane Congestion Management
- **TR 22.851** (Rel-19) — Feasibility Study on Network Sharing Aspect
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 24.007** (Rel-19) — GSM Um Interface Layer 3 Architecture
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [MOCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mocn/)
