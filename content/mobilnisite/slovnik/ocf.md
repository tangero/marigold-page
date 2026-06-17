---
slug: "ocf"
url: "/mobilnisite/slovnik/ocf/"
type: "slovnik"
title: "OCF – Offline Charging Function"
date: 2026-01-01
abbr: "OCF"
fullName: "Offline Charging Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ocf/"
summary: "Funkce offline účtování (OCF) je komponenta jádra sítě odpovědná za sběr a zpracování záznamů o účtování (CDR) pro zákazníky s post-paid tarifem. Shromažďuje informace o využití z prvků sítě, formátuj"
---

OCF je funkce jádra sítě, která sbírá údaje o využití, formátuje je do záznamů o účtování (CDR) a předává je pro účtování služeb zákazníkům s post-paid tarifem.

## Popis

Funkce offline účtování (OCF) je základním prvkem systému účtování 3GPP, konkrétně navrženým pro scénáře offline (post-paid) účtování. Funguje na principu sběru informací o využití síťových prostředků až poté, co byly tyto prostředky spotřebovány. OCF se nachází uvnitř funkce spouštěče účtování ([CTF](/mobilnisite/slovnik/ctf/)), která je integrována v různých prvcích sítě, jako jsou SGSN, GGSN, [MSC](/mobilnisite/slovnik/msc/) nebo IMS entity. Když je služba poskytnuta, CTF detekuje události relevantní pro účtování a vygeneruje účtovací data ([CD](/mobilnisite/slovnik/cd/)). Tato data jsou následně odeslána přes referenční bod Rf do funkce účtovacích dat ([CDF](/mobilnisite/slovnik/cdf/)). CDF, klíčová podkomponenta architektury OCF, je zodpovědná za sestavení přijatých účtovacích událostí do souvislých, na relaci založených záznamů o účtování ([CDR](/mobilnisite/slovnik/cdr/)). Tyto CDR jsou formátovány podle specifikací 3GPP a obsahují podrobné informace, jako je identita účastníka, využitá služba, objem dat, doba trvání, časová razítka a obsluhující prvek sítě. CDF poté dokončené CDR předává přes referenční bod Ga do funkce brány účtování ([CGF](/mobilnisite/slovnik/cgf/)). CGF funguje jako brána a provádí úkoly, jako je ukládání CDR do vyrovnávací paměti, validace, konsolidace a korelace, než záznamy nakonec přenese do fakturační domény ([BD](/mobilnisite/slovnik/bd/)) síťového operátora pro další zpracování a generování faktur. Celý proces OCF se řídí architekturou offline účtování definovanou v 3GPP TS 32.240, což zajišťuje standardizovaný, spolehlivý a auditovatelný tok účtovacích informací od využití sítě k finančnímu vypořádání. Její role je z pohledu řízení služby pasivní, protože neovlivňuje poskytování služby v reálném čase, ale je klíčová pro komerční a provozní backend.

## K čemu slouží

OCF byla vytvořena, aby poskytla operátorům standardizovaný, spolehlivý a škálovatelný mechanismus pro účtování služeb zákazníkům za využití sítě a služeb po jejich uskutečnění (post-paid fakturace). Před standardizovaným offline účtováním se operátoři spoléhali na proprietární systémy v každém prvku sítě pro zaznamenávání využití, což vedlo k nekonzistenci, problémům s integrací a obtížím při vytváření jednotných zákaznických faktur. Architektura OCF definovaná 3GPP tyto problémy řeší vytvořením jasného oddělení mezi prvky sítě, které generují účtovací události, a centralizovanými funkcemi, které je zpracovávají do fakturovatelných záznamů. Řeší kritickou obchodní potřebu zajištění příjmů tím, že zajišťuje zachycení všech zpoplatnitelných událostí, jejich přesné zaznamenání a doručení do fakturačního systému. Vytvoření OCF ve verzi Release 99 bylo motivováno přechodem na paketově přepínané služby ([GPRS](/mobilnisite/slovnik/gprs/)) a rostoucí složitostí nabídek služeb, což vyžadovalo robustnější a flexibilnější rámec účtování, než jaký byl dostupný pro starší okruhově přepínanou hlasovou službu. Poskytuje základ pro položkovou fakturaci, řešení sporů ohledně účtování a finanční reporting.

## Klíčové vlastnosti

- Standardizovaný sběr účtovacích událostí přes referenční bod Rf
- Generování záznamů o účtování (CDR) kódovaných v ASN.1
- Korelace účtovacích dat založená na relacích a událostech
- Spolehlivý přenos CDR do fakturační domény přes rozhraní Ga
- Podpora korelace napříč více síťovými prvky a doménami
- Definované formáty CDR specifické pro různé typy služeb (např. GPRS, IMS)

## Související pojmy

- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [CDF – Cumulative Distribution Function](/mobilnisite/slovnik/cdf/)
- [CGF – Charging Gateway Functionality](/mobilnisite/slovnik/cgf/)
- [CTF – Charging Trigger Function](/mobilnisite/slovnik/ctf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.297** (Rel-19) — Charging Data Record File Transfer
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [OCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ocf/)
