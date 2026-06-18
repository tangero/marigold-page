---
slug: "sho"
url: "/mobilnisite/slovnik/sho/"
type: "slovnik"
title: "SHO – Selected Home Operator"
date: 2025-01-01
abbr: "SHO"
fullName: "Selected Home Operator"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sho/"
summary: "Selected Home Operator (SHO, tj. vybraný domácí operátor) je koncept správy sítě používaný v roamujících scénářích. Identifikuje konkrétního domácího operátora, ke kterému je roamující účastník přidru"
---

SHO je konkrétní domácí operátor, ke kterému je roamující účastník přidružen, což umožňuje přesné účtování, poskytování služeb a vynucování politik v mobilních sítích.

## Popis

Selected Home Operator (SHO, tj. vybraný domácí operátor) je klíčový identifikátor v architektuře správy sítí 3GPP, primárně využívaný v roamujících a mezifunkčních scénářích. Funguje jako klíčový parametr, který jednoznačně určuje domácí veřejnou pozemní mobilní síť ([HPLMN](/mobilnisite/slovnik/hplmn/)) roamujícího účastníka. Toto určení není pouhým označením; je nedílnou součástí provozní a obchodní logiky navštívených sítí. Když se uživatelské zařízení (UE) připojí k navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), síťové elementy, zejména ty zapojené do účtování a řízení politik, musí identifikovat domácího operátora účastníka, aby mohly aplikovat správné obchodní a servisní dohody.

Technická implementace SHO zasahuje několik síťových domén. V doméně účtování, specifikované v 3GPP TS 32.405, je SHO zahrnuto do záznamů účtovacích dat ([CDR](/mobilnisite/slovnik/cdr/)) generovaných navštívenou sítí. To umožňuje přesnou korelaci dat o využití s konkrétním domácím operátorem pro zúčtování plateb. Z pohledu zabezpečení a síťového přístupu, jak je popsáno v TS 33.812, hraje SHO roli v procedurách autentizace a autorizace, čímž zajišťuje, že roamujícím účastníkům je přístup povolen na základě dohod mezi VPLMN a identifikovanou HPLMN. Tento koncept je také relevantní v kontextu sdílení sítí a architektur Multi-Operator Core Network ([MOCN](/mobilnisite/slovnik/mocn/)), kde je jeden přístupový rádiový síť sdílen více operátory jádrové sítě.

Z architektonického hlediska je SHO propagováno přes různé referenční body. Typicky je odvozeno z International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) nebo je explicitně signalizováno během procedur připojení k síti a zřizování relace. Síťové elementy, jako je Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Policy and Charging Rules Function (PCRF) v navštívené síti, používají tento identifikátor k výběru příslušných směrovacích agentů Diameter nebo mezifunkčních rozhraní pro komunikaci se systémy domácí sítě, jako je Home Subscriber Server (HSS) nebo Online Charging System (OCS). Jeho role je tedy zásadní pro bezproblémový, bezpečný a účtovatelný provoz globálního mobilního roamingu.

## K čemu slouží

Koncept Selected Home Operator (SHO) byl zaveden, aby řešil složitosti moderního roamingu, sdílení sítí a prostředí s více operátory. Před jeho formalizací mohla být identifikace přesného domácího operátora pro roamujícího účastníka nejednoznačná, zejména s nástupem mobilních virtuálních operátorů (MVNO) a složitých dohod o sdílení sítí. Tato nejednoznačnost představovala významné výzvy pro přesné účtování, prevenci podvodů a konzistentní aplikaci smluv o úrovni služeb (SLA) mezi operátory.

Jeho vytvoření bylo motivováno potřebou standardizovaného, spolehlivého mechanismu v systémech správy sítě a účtování, který by přesně určil odpovědného domácího operátora. To není pouze technický požadavek, ale klíčový obchodní požadavek. Zúčtování příjmů z roamingu mezi operátory závisí na přesném připsání využití účastníka. Dále, jak se regulační rámce vyvíjely a nařizovaly spravedlivý přístup a roaming, se stalo mít jasný identifikátor SHO nezbytným pro dodržování předpisů, což umožňuje navštíveným sítím aplikovat správné politiky pro kvalitu služeb, řízení přístupu a nouzové služby na základě konkrétní dohody s domácím operátorem. Řeší problém identifikace operátora v prostředí, kde může být IMSI účastníka spojeno s prodejcem (MVNO) spíše než se základním poskytovatelem infrastruktury, a zajišťuje, že obchodní a provozní řetězec zůstává jasný a proveditelný.

## Klíčové vlastnosti

- Jednoznačná identifikace domácí PLMN účastníka v roamujících scénářích
- Integrace do záznamů účtovacích dat (CDR) pro přesné mezifunkční účtování
- Podpora procedur autentizace a autorizace v navštívených sítích
- Nezbytnost pro vynucování politik založených na konkrétních mezifunkčních dohodách
- Umožňuje správné směrování signalizačních zpráv do příslušné domácí sítě
- Umožňuje provoz v architekturách se sdílením sítí (MOCN, GWCN) a s MVNO

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)

## Definující specifikace

- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security

---

📖 **Anglický originál a plná specifikace:** [SHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sho/)
