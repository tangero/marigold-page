---
slug: "odb"
url: "/mobilnisite/slovnik/odb/"
type: "slovnik"
title: "ODB – Operator Determined Barring"
date: 2025-01-01
abbr: "ODB"
fullName: "Operator Determined Barring"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/odb/"
summary: "Síťová služba umožňující operátorům omezit konkrétní komunikační služby pro účastníka, například odchozí hovory nebo SMS. Poskytuje nástroj pro správu síťových zdrojů, vynucování politik a řešení neza"
---

ODB je síťová služba umožňující operátorům omezit konkrétní komunikační služby pro účastníka, například odchozí hovory nebo SMS, za účelem správy zdrojů a vynucování politik.

## Popis

Operator Determined Barring (ODB) je účastnická služba definovaná ve specifikacích 3GPP, která umožňuje síťovému operátorovi uvalit omezení na telekomunikační služby, které může účastník používat. Funguje na úrovni jádra sítě, primárně v rámci Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) v GSM/UMTS nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v EPS a 5GC. Službu vynucuje Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro služby s přepojováním okruhů a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro služby s přepojováním paketů. Když se účastník pokusí zahájit službu (např. odchozí hovor), obsluhující síťový uzel zkontroluje profil účastníka, který obsahuje příznaky ODB stažené z HLR/HSS během registrace. Pokud je aktivní relevantní podmínka blokování, síť žádost o službu odmítne, často s konkrétním kódem příčiny.

Architektura se opírá o sadu kategorií blokování uložených jako součást účastnických dat. Klíčové kategorie zahrnují Barring of All Outgoing Calls ([BAOC](/mobilnisite/slovnik/baoc/)), Barring of Outgoing International Calls ([BOIC](/mobilnisite/slovnik/boic/)), Barring of Outgoing International Calls except those directed to the Home PLMN Country (BOIC-exHC), Barring of All Incoming Calls ([BAIC](/mobilnisite/slovnik/baic/)) a Barring of Incoming Calls when roaming outside the home PLMN (BIC-Roam). Existují také kategorie pro blokování konkrétních služeb, jako jsou paketově orientované služby, hovory s přepojováním okruhů pro data nebo doplňkové služby. Tyto příznaky nastavují administrativní systémy operátora, jako je Customer Relationship Management (CRM) nebo provizní systémy, a jsou propagovány do HLR/HSS.

ODB funguje ve spojení s dalšími mechanismy blokování, jako je Access Class Barring (ACB) pro řízení přetížení rádiového rozhraní a Service Specific Access Control (SSAC) pro IMS nouzová sezení, ale ODB je specificky vázána na smluvní nebo administrativní status účastníka. Její vynucování je síťově centrické a typicky není pod kontrolou účastníka, což ji odlišuje od doplňkových služeb blokování hovorů (např. Call Barring, CB), které jsou programovatelné uživatelem. Služba hraje klíčovou roli v síťovém managementu, neboť umožňuje operátorům zmírňovat ztráty výnosů z nezaplacených faktur, předcházet podvodnému využití, kontrolovat náklady na roaming a spravovat síťové zatížení dočasným omezením neesenciálních služeb během špiček nebo mimořádných událostí.

## K čemu slouží

ODB byla vytvořena, aby poskytla operátorům mobilních sítí výkonný administrativní nástroj pro správu účastníků a sítě. Před její standardizací měli operátorů omezené technické prostředky, jak proaktivně omezovat služby konkrétním účastníkům z administrativních důvodů (např. nezaplacení, podezření z podvodu) bez fyzického zablokování SIM karty. Tento reaktivní přístup byl neefektivní a mohl vést k významným únikům výnosů. ODB zavedla standardizovaný, sítí vynucovaný mechanismus pro dynamické blokování služeb na základě kritérií definovaných operátorem, přímo integrovaný do profilu správy mobility účastníka.

Služba řeší několik klíčových provozních problémů. Za prvé umožňuje řízení kreditu a správu dluhů tím, že operátorům dovoluje blokovat odchozí služby (hovory, SMS) účastníkům, kteří překročili kreditní limity nebo nezaplatili, zatímco potenciálně stále povoluje příchozí hovory nebo nouzové služby. Za druhé jde o klíčový nástroj pro správu podvodů, umožňující rychlou reakci na podezřelou aktivitu blokováním mezinárodních hovorů nebo datových služeb, které jsou častými vektory podvodů. Za třetí napomáhá správě roamingových dohod a nákladů tím, že umožňuje operátorům blokovat odchozí hovory nebo data, když se účastník nachází v roamingu v určitých regionech, čímž chrání jak operátora, tak účastníka před neočekávanými poplatky.

Historicky zavedení ODB ve verzi Release 4 (ačkoli koncepty existovaly dříve) formalizovalo a rozšířilo tyto schopnosti v rámci se vyvíjející architektury jádra sítí GSM/UMTS. Řešilo omezení dřívějších, primitivnějších metod, které často vyžadovaly manuální zásah na ústředně nebo postrádaly granularitu. Tím, že je ODB součástí standardizovaných účastnických dat, zajišťuje konzistentní vynucování napříč různými síťovými dodavateli a když účastníci přecházejí do roamingu v jiných sítích podporujících tuto funkci, čímž poskytuje spolehlivou a škálovatelnou kontrolní vrstvu pro globální mobilní operace.

## Klíčové vlastnosti

- Podrobné kategorie blokování pro odchozí hovory (BAOC, BOIC, BOIC-exHC)
- Blokování všech příchozích hovorů (BAIC) a příchozích hovorů v roamingu (BIC-Roam)
- Blokování specifických přenosových služeb (např. dat s přepojováním okruhů, paketově orientovaných služeb)
- Sítí vynucované a operátorem spravované, nezávislé na uživatelském nastavení
- Integrované do účastnických dat v HLR/HSS a vynucované MSC, SGSN a MME
- Poskytuje konkrétní kódy příčin uživatelskému zařízení při zamítnutí služby

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 24.315** (Rel-19) — Operator Determined Barring (ODB) for IMS
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 24.629** (Rel-19) — Explicit Communication Transfer (ECT) Protocol
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [ODB na 3GPP Explorer](https://3gpp-explorer.com/glossary/odb/)
