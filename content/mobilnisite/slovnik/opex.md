---
slug: "opex"
url: "/mobilnisite/slovnik/opex/"
type: "slovnik"
title: "OPEX – Operational Expenditures"
date: 2025-01-01
abbr: "OPEX"
fullName: "Operational Expenditures"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/opex/"
summary: "Průběžné náklady, které má operátor mobilní sítě na provoz a údržbu své sítě a služeb. Specifikace 3GPP poskytují rámce pro minimalizaci OPEX prostřednictvím automatizace, úspor energie a zjednodušení"
---

OPEX jsou průběžné náklady, které má operátor mobilní sítě na provoz a údržbu své sítě a služeb.

## Popis

Operational Expenditures (OPEX) v telekomunikačním kontextu označují opakující se náklady potřebné pro každodenní fungování sítě, na rozdíl od jednorázových kapitálových výdajů ([CAPEX](/mobilnisite/slovnik/capex/)) na nákup zařízení. Specifikace 3GPP řeší snížení OPEX definováním architektur, protokolů a funkcí, které automatizují procesy, optimalizují využití zdrojů a zjednodušují správu sítě. Mezi klíčové oblasti ovlivňující OPEX patří správa a orchestrace sítě, spotřeba energie síťových prvků, odstraňování poruch a poskytování služeb.

Z architektonického pohledu jsou pro snížení OPEX klíčové standardy 3GPP, jako jsou ty definující funkci Management Data Analytics Function ([MDAF](/mobilnisite/slovnik/mdaf/)) a Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)). Tyto funkce shromažďují obrovská množství dat o výkonu a poruchách z celé sítě (RAN, přenosová část, core). Pomocí analytiky a strojového učení mohou předpovídat zahlcení sítě, identifikovat potenciální selhání zařízení dříve, než k nim dojde (prediktivní údržba), a automaticky doporučovat nebo provádět nápravné akce. Tím se operace přesouvají z reaktivního, manuálního odstraňování problémů na proaktivní, automatizované zajištění služeb, což výrazně snižuje náklady na práci a výpadky služeb.

Další významnou složkou je úspora energie. Specifikace jako TS 38.913 a TS 38.864 definují funkce pro rádiový přístupový síť (RAN), například režimy spánku buněk (kdy jsou komponenty základnové stanice vypnuty během období nízkého provozu), návrh úsporného nosiče a dynamické sdílení spektra. Tyto funkce umožňují, aby spotřeba energie sítě odpovídala síťovému vytížení. V core síti virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a cloud-nativní principy, podporované 3GPP, umožňují efektivní škálování a konsolidaci úloh, čímž se snižuje počet fyzických serverů a s tím spojené náklady na energii a chlazení. Automatizovaná správa životního cyklu služeb, včetně vytváření, škálování a ukončování síťových řezů, navíc snižuje potřebu manuálního zásahu pro každého podnikového zákazníka, čímž se snižují provozní režie.

## K čemu slouží

Zaměření na OPEX ve standardech 3GPP bylo motivováno ekonomickými výzvami, kterým čelí síťoví operátoři, zejména při přechodu na 5G. Zatímco 5G slibuje nové zdroje příjmů, jeho nasazení s sebou nese vysoké [CAPEX](/mobilnisite/slovnik/capex/) za nové spektrum, hustší sítě a upgrady core sítě. Pro zajištění ziskovosti se stalo nezbytným drasticky snížit průběžné náklady na provoz těchto stále složitějších sítí. Historicky byly síťové operace vysoce manuální a spoléhaly se na týmy inženýrů konfigurujících zařízení a reagujících na alarmy, což není ani škálovatelné, ani nákladově efektivní pro slibované měřítko 5G s miliony zařízení a službami s ultra-nízkou latencí.

Předchozí generace sítí měly omezené vestavěné možnosti automatizace a samooptymalizace. Omezení těchto přístupů vyšlo najevo s explozí datového provozu: provozní týmy rostly, účty za energii prudce stoupaly a uvedení nových služeb na trh bylo pomalé kvůli manuálnímu poskytování. Práce 3GPP na snížení OPEX, zejména od Release 7 se zavedením konceptů Self-Organizing Networks ([SON](/mobilnisite/slovnik/son/)), měla za cíl řešit tyto problémy. Účelem je definovat standardizovanou cestu k autonomním sítím, které se umí samy konfigurovat, optimalizovat a opravovat, čímž se minimalizuje lidský zásah, snižuje spotřeba energie a v konečném důsledku se provoz sítí stává udržitelným a ekonomicky životaschopným v éře 5G a dalších generací.

## Klíčové vlastnosti

- Specifikace funkcí Self-Organizing Network (SON) pro automatickou konfiguraci a optimalizaci
- Funkce Energy Saving (ES) pro RAN a core síť, včetně režimu dormance buněk a dynamického škálování kapacity
- Rámce Management and Orchestration (MANO) sladěné s ETSI NFV pro automatizovanou správu životního cyklu služeb
- Analytické rámce (MDAF, NWDAF) pro daty řízené, prediktivní síťové operace a údržbu
- Automatizovaná správa poruch a analýza hlavní příčiny pro snížení střední doby do opravy (MTTR)
- Standardizovaná rozhraní pro zero-touch provisioning a automatizované vynucování politik

## Související pojmy

- [CAPEX – Capital Expenditures](/mobilnisite/slovnik/capex/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 23.820** (Rel-9) — IMS Restoration Procedures
- **TS 25.824** (Rel-8) — HSPA Evolution for 1.28Mcps TDD Study
- **TS 25.913** (Rel-9) — Evolved UTRA and UTRAN Requirements
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.826** (Rel-10) — Study on Energy Savings Management in LTE/SAE Networks
- **TS 32.827** (Rel-10) — UE Management over Itf-N for MDT/SON
- **TS 32.831** (Rel-10) — 3GPP-TMF PM Alignment Study
- **TS 32.832** (Rel-10) — Alarm Correlation and Root Cause Analysis Study
- **TS 32.835** (Rel-12) — HetNet Management Information Selection
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study
- **TS 36.887** (Rel-12) — Energy Saving Enhancement for E-UTRAN Study
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [OPEX na 3GPP Explorer](https://3gpp-explorer.com/glossary/opex/)
