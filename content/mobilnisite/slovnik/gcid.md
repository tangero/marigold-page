---
slug: "gcid"
url: "/mobilnisite/slovnik/gcid/"
type: "slovnik"
title: "GCID – GPRS Charging Identifier"
date: 2025-01-01
abbr: "GCID"
fullName: "GPRS Charging Identifier"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gcid/"
summary: "GPRS Charging Identifier (GCID) je jedinečný identifikátor přiřazený každému PDP kontextu (Packet Data Protocol) nebo datové relaci v sítích GPRS, UMTS a EPS. Systémy účtování jej používají ke korelac"
---

GCID je jedinečný identifikátor přiřazený každému PDP kontextu nebo datové relaci v sítích GPRS, UMTS a EPS, který systémy účtování využívají ke korelaci záznamů o účtovaných datech pro přesné vyúčtování.

## Popis

[GPRS](/mobilnisite/slovnik/gprs/) Charging Identifier (GCID) je základním prvkem architektury účtování v paketově spínaných sítích 2G, 3G a 4G. Je to jedinečný identifikátor, který při aktivaci [PDP](/mobilnisite/slovnik/pdp/) kontextu nebo [PDN](/mobilnisite/slovnik/pdn/) připojení přiřadí Gateway GPRS Support Node (GGSN) v GPRS/UMTS nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v Evolved Packet System (EPS). Primární funkcí GCID je poskytnout korelační klíč. Během datové relace generují různé síťové uzly – jako Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a GGSN – záznamy o účtovaných datech ([CDR](/mobilnisite/slovnik/cdr/)), které obsahují podrobnosti o využití prostředků (např. objem dat, doba trvání). Každý uzel zahrne GCID do svých CDR. Systém účtování (např. Charging Gateway Function nebo billingový systém) pak tento společný GCID použije ke sloučení nebo korelaci všech dílčích CDR souvisejících se stejným PDP kontextem/PDN připojením, čímž vytvoří úplný a přesný záznam pro účely vyúčtování. GCID je jedinečný v kontextu GGSN/PGW, který jej vygeneroval, a v určitém časovém období. Jeho struktura a použití jsou definovány v technických specifikacích, jako jsou 3GPP TS 23.815 (Charging and billing) a TS 24.229 (IP multimedia call control protocol). Identifikátor je přenášen mezi síťovými prvky prostřednictvím signalizačních protokolů (např. [GTP](/mobilnisite/slovnik/gtp/)) a je klíčovou součástí pro offline účtování (kde se generují CDR) a má význam i v některých scénářích online účtování pro identifikaci relace.

## K čemu slouží

GCID byl zaveden ve 3GPP Release 5, aby řešil klíčovou výzvu v účtování paketových dat v [GPRS](/mobilnisite/slovnik/gprs/) a UMTS: distribuovanou povahu dat relace. V síti GPRS SGSN i GGSN zpracovávají části uživatelské datové relace a generují samostatné CDR. Bez společného identifikátoru bylo pro billingový systém extrémně obtížné přesně spojit SGSN-CDR a GGSN-CDR patřící ke stejné uživatelské datové relaci, což vedlo k potenciálním chybám ve vyúčtování nebo neúplným záznamům. GCID tento problém korelace řeší tím, že poskytuje jedinečný identifikátor relace vygenerovaný při jejím zřízení a konzistentně používaný všemi zúčastněnými uzly. To zajišťuje, že všechny záznamy o využití pro jeden PDP kontext lze spolehlivě zkombinovat, což umožňuje přesné účtování založené na objemu, čase nebo události. Jeho zavedení bylo motivováno přechodem na paketově spínané služby, kde relace mohly být dlouhodobé a zahrnovat významný přenos dat, což činilo přesné účtování pro operátory klíčovým. GCID zůstává základním konceptem i v pozdějších architekturách, jako je EPS, kde je potřeba podobná korelace mezi SGW-CDR a PGW-CDR.

## Klíčové vlastnosti

- Jedinečný identifikátor přiřazený na každý PDP kontext nebo PDN připojení uzlem GGSN/PGW
- Slouží jako korelační klíč pro záznamy o účtovaných datech (CDR) z různých síťových uzlů
- Nezbytný pro přesné offline účtování a vyúčtování v paketově spínaných sítích
- Obsažen v CDR generovaných uzly SGSN, GGSN, SGW a PGW
- Přenášen v rámci signalizačních protokolů řídicí roviny, jako je GTP-C
- Umožňuje sloučení dílčích záznamů o využití do úplného záznamu relace pro účely vyúčtování

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [GCID na 3GPP Explorer](https://3gpp-explorer.com/glossary/gcid/)
