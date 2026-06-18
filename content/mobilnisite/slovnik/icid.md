---
slug: "icid"
url: "/mobilnisite/slovnik/icid/"
type: "slovnik"
title: "ICID – IM CN subsystem Charging Identifier"
date: 2025-01-01
abbr: "ICID"
fullName: "IM CN subsystem Charging Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/icid/"
summary: "Jedinečný identifikátor používaný v rámci architektury účtování IP Multimedia Subsystem (IMS) ke korelaci záznamů o účtovacích datech (CDR) generovaných různými síťovými funkcemi během jedné servisní"
---

ICID je jedinečný identifikátor používaný v účtování IMS ke korelaci záznamů o účtovacích datech (CDR) z různých síťových funkcí pro jednu servisní relaci.

## Popis

Identifikátor účtování podsystému [IM](/mobilnisite/slovnik/im/) CN (ICID) je klíčový parametr účtování definovaný v architektuře IP Multimedia Core Network Subsystem (IMS) dle 3GPP. Jeho hlavní funkcí je poskytnout jedinečný korelační klíč, který spojuje všechny záznamy o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) vygenerované pro konkrétní relaci IMS služby napříč více síťovými funkcemi. Relace IMS, například volání Voice over LTE (VoLTE) nebo videokonference, zahrnuje několik uzlů IMS: Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), který je prvním kontaktním bodem, Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), který zpracovává řízení relace, a potenciálně Application Servers ([AS](/mobilnisite/slovnik/as/)) poskytující služby. Každý z těchto uzlů může generovat účtovací události nezávisle.

ICID je generován prvním síťovým subjektem IMS, který iniciuje účtování pro relaci, typicky P-CSCF nebo S-CSCF, na začátku dialogu nebo transakce. Tento identifikátor je globálně jedinečný řetězec, často vytvořený kombinací hostname nebo IP adresy generujícího uzlu a časového razítka nebo pořadového čísla, aby byla zajištěna jedinečnost. Jakmile je vygenerován, je ICID zahrnut ve všech účtovacích zprávách založených na protokolu Diameter (jako například příkazy Accounting-Request ([ACR](/mobilnisite/slovnik/acr/)) používající referenční body Ro nebo Rf) odesílaných z uzlů IMS do funkce Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)). Je také šířen v signalizaci IMS pomocí hlaviček SIP, jako je P-Charging-Vector, aby všechny následné uzly zapojené do relace použily stejný ICID pro své účtovací hlášení.

Ve fakturačním systému nebo funkci Charging Gateway Function (CGF) slouží ICID jako primární klíč ke korelaci dílčích CDR od P-CSCF, S-CSCF a AS do jednoho konsolidovaného záznamu relace. Tato korelace je nezbytná pro vygenerování přesného a sjednoceného účtu pro uživatele. Architektura se spoléhá na flexibilitu protokolu Diameter pro přenos ICID jako dvojice atribut-hodnota (AVP) a na rozšiřitelnost protokolu SIP pro jeho přenos mezi uzly IMS, což zajišťuje plynulý tok účtovacích informací v souladu se signalizační cestou relace.

## K čemu slouží

ICID byl zaveden, aby vyřešil problém korelace účtování v dekomponované, na relaci založené architektuře IMS. Před IMS mohla spojově orientovaná hlasová volání typicky zahrnovat jediný přepínací uzel (MSC), který mohl generovat jediný CDR pro celé volání. IMS je však distribuovaný, IP-based systém, kde jsou řídicí a servisní funkce odděleny a mohou být poskytovány různými fyzickými uzly. Bez společného identifikátoru by fakturační systém přijímal nesouvisející účtovací události od P-CSCF, S-CSCF a AS bez spolehlivého způsobu, jak je propojit jako součást stejné uživatelské relace, což by vedlo k fakturačním chybám, duplicitním poplatkům nebo ztraceným příjmům.

Jeho vytvoření v 3GPP Release 5 bylo motivováno potřebou robustního frameworku pro online a offline účtování služeb IMS, jak je definováno v TS 32.260. ICID poskytuje základní mechanismus pro korelaci relací, což je předpokladem pro jakékoli sofistikované modely účtování, jako je účtování založené na událostech, účtování založené na relacích nebo složené účtování pro služby zahrnující více aplikací. Řeší omezení dřívějšího účtování datových paketů, které často spoléhalo na identifikátory jako PDP kontext, které nebyly vhodné pro aplikační vrstvu a víceuzlovou povahu relací IMS. ICID umožňuje operátorům implementovat přesné a spolehlivé účtování pro komplexní služby nové generace, což bylo klíčové pro komerční životaschopnost IMS.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor generovaný na relaci nebo dialog IMS
- Používaný jako korelační klíč napříč více záznamy o účtovacích datech (CDR)
- Šířený přes signalizaci SIP v hlavičce P-Charging-Vector
- Zahrnutý jako dvojice atribut-hodnota (AVP) v účtovacích zprávách Diameter (Rf/Ro)
- Umožňuje korelaci offline a online účtovacích událostí
- Generovaný prvním uzlem IMS iniciujícím účtování (např. P-CSCF/S-CSCF)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study
- **TR 33.978** (Rel-8) — Interim Security for Early IMS

---

📖 **Anglický originál a plná specifikace:** [ICID na 3GPP Explorer](https://3gpp-explorer.com/glossary/icid/)
