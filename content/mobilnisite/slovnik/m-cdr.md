---
slug: "m-cdr"
url: "/mobilnisite/slovnik/m-cdr/"
type: "slovnik"
title: "M-CDR – Mobility management generated - Charging Data Record"
date: 2025-01-01
abbr: "M-CDR"
fullName: "Mobility management generated - Charging Data Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/m-cdr/"
summary: "M-CDR je specifický typ záznamu účtovacích dat generovaný síťovými funkcemi jako MME nebo AMF k zaznamenání událostí souvisejících s mobilitou. Je klíčovou součástí offline účtování a poskytuje podrob"
---

M-CDR (Mobility management generated - Charging Data Record) je záznam účtovacích dat generovaný funkcemi jako MME nebo AMF k zaznamenání událostí mobility, jako je předání spojení, a poskytuje auditní stopu pro offline účtování, fakturaci a analýzy.

## Popis

Mobility management generated - Charging Data Record (M-CDR) je standardizovaná datová struktura definovaná v řadě specifikací 3GPP, včetně TS 32.251, 32.272, 32.273 a 32.278. Jedná se o podtyp záznamu účtovacích dat ([CDR](/mobilnisite/slovnik/cdr/)) vytvářený specificky uzly jádra sítě zodpovědnými za správu mobility. V Evolved Packet Core (EPC) generuje M-CDR entita Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), zatímco v 5G Core (5GC) tuto roli přebírá funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)).

M-CDR funguje tak, že zaznamenává jednotlivé události správy mobility při jejich výskytu během relace účastníka. Účtovací funkce v rámci MME nebo AMF je spouštěna specifickými signalizačními procedurami. Pro každou významnou událost mobility otevře nový M-CDR nebo aktualizuje stávající a naplní jej řadou strukturovaných informací. Ty zahrnují [IMSI](/mobilnisite/slovnik/imsi/) nebo SUPI účastníka, typ události (např. 'Attach', 'Tracking Area Update', 'Handover'), časová razítka začátku a konce události, identifikátory obsluhující buňky a polohové/směrovací oblasti a také identifikaci zúčastněného síťového prvku (např. zdrojový a cílový eNodeB/gNodeB při předání spojení).

Klíčovými komponentami při jeho generování jsou funkce spouštějící účtování (Charging Trigger Function - [CTF](/mobilnisite/slovnik/ctf/)) integrovaná v MME/AMF a systém offline účtování ([OFCS](/mobilnisite/slovnik/ofcs/)). CTF detekuje účtovatelné události, shromáždí relevantní data do jednotky CDR a přepošle je přes referenční bod Rf/Ga k funkci Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)). CDF pak data naformátuje do finálního souboru M-CDR pro fakturační doménu. Úlohou M-CDR je poskytnout neběžný, podrobný záznam 'řídicích rovinových' aktivit mobility. Neúčtuje objem přenesených uživatelských dat, ale využití síťových zdrojů spojené se zpracováním mobility. Tento záznam je pro operátory zásadní pro porozumění vzorcům pohybu účastníků, provádění roamingových vyúčtování, plnění zákonných požadavků a implementaci určitých fakturačních modelů zohledňujících mobilitu (např. regionální tarify).

## K čemu slouží

M-CDR existují, aby naplnily kritickou provozní a komerční potřebu účtovat signalizaci správy mobility jako účtovatelnou síťovou službu. V časných mobilních sítích se účtování primárně zakládalo na minutách hovoru nebo jednoduchém objemu dat. Jak se sítě vyvinuly v paketově orientované architektury s komplexní podporou mobility (předání spojení mezi buňkami, aktualizace směrovací oblasti atd.), tyto signalizační procedury začaly spotřebovávat významné procesní zdroje v jádru sítě.

Problém spočíval v tom, že tuto spotřebu zdrojů nezachycovaly tradiční S-CDR (Session [CDR](/mobilnisite/slovnik/cdr/)) nebo G-CDR (Gateway CDR), které se zaměřovaly na aktivitu datové relace a objem provozu. Operátoři neměli standardizovaný způsob, jak sledovat, zaznamenávat a případně účtovat náklady spojené se správou vysoce mobilního účastníka. Vytvoření M-CDR ve 3GPP Release 8 spolu s EPS tuto mezeru zaplnilo. Bylo motivováno požadavkem na detailní, standardizovaná účtovací data pro všechny síťové služby, což umožňuje spravedlivější alokaci nákladů, podrobné analýzy zatížení sítě způsobeného mobilitou a přesné roamingové poplatky mezi operátory za události mobility. Poskytuje auditní stopu nezbytnou pro systémy podpory podnikání a provozu (BSS/OSS) v moderní paketové mobilní síti.

## Klíčové vlastnosti

- Generován specificky pro události správy mobility (např. připojení, aktualizace polohové oblasti, předání spojení)
- Obsahuje detailní pole pro identitu účastníka (IMSI/SUPI), typ události a polohové informace
- Zahrnuje přesná časová razítka začátku a konce procedury mobility
- Zaznamenává identifikátory zapojených síťových prvků (např. zdrojové/cílové buňky)
- Používá se výhradně v offline (zpětně zpracovávajících) účtovacích systémech
- Standardizovaný formát napříč releasy 3GPP pro interoperabilitu

## Související pojmy

- [G-CDR – GGSN (PDP context) generated - Charging Data Record](/mobilnisite/slovnik/g-cdr/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [M-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-cdr/)
