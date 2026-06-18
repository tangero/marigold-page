---
slug: "anl"
url: "/mobilnisite/slovnik/anl/"
type: "slovnik"
title: "ANL – Autonomous Network Level"
date: 2025-01-01
abbr: "ANL"
fullName: "Autonomous Network Level"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/anl/"
summary: "ANL je rámec pro měření a srovnávání úrovně automatizace (zralosti automatizace) mobilní sítě. Definuje víceúrovňovou škálu (L0–L5), která kvantifikuje míru autonomie sítě od manuálních operací po pln"
---

ANL je rámec pro měření a srovnávání úrovně automatizace (zralosti automatizace) mobilní sítě pomocí víceúrovňové škály od manuálních po plně samoučící se operace.

## Popis

Rámec Autonomous Network Level (ANL), standardizovaný 3GPP, poskytuje strukturovanou metodologii pro hodnocení a vyjadřování míry automatizace v telekomunikační síti. Nejde o konkrétní technologii nebo protokol, ale o model zralosti definovaný napříč více dimenzemi, včetně nasazování služeb, jejich zajištění (assurance) a správy životního cyklu. Jádrem ANL je šestistupňová škála, kde úroveň 0 (L0) představuje plně manuální, člověkem řízené operace a úroveň 5 (L5) představuje plně autonomní síť schopnou samokonfigurace, samoléčení, samooptymalizace a samovývoje s minimálním nebo žádným zásahem člověka. Každá úroveň je charakterizována konkrétními schopnostmi a mírou, do jaké jsou lidský operátoři zapojeni do rozhodovacích a výkonných smyček.

Z architektonického hlediska je hodnocení ANL integrováno do systémů správy sítě, jako je služba Management Data Analytics Service ([MDAS](/mobilnisite/slovnik/mdas/)) a funkce Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) v 5G. Rámec hodnotí klíčové domény automatizace: nasazení a poskytování služeb, zajištění kvality služeb a uživatelského zážitku (QoS/[QoE](/mobilnisite/slovnik/qoe/)), energetickou účinnost a správu zabezpečení. Pro každou doménu jsou ve specifikacích, jako je 3GPP TS 28.100 a TR 28.910, definovány soubory hodnotících kritérií a klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)). Tato kritéria měří schopnost sítě vnímat své prostředí, analyzovat data, rozhodovat a provádět akce autonomně.

Jak to funguje, zahrnuje kontinuální cyklus měření, analýzy a srovnávání. Funkce správy sítě sbírají provozní data a telemetrii. Analytické nástroje pak tato data zpracovávají vůči předem definovaným kritériím ANL pro každou doménu. Systém vyhodnocuje dosaženou míru automatizace – například zda je detekce chyb manuální ([L1](/mobilnisite/slovnik/l1/)), automatizovaná s lidským schválením ([L3](/mobilnisite/slovnik/l3/)) nebo plně automatizovaná s proaktivní predikcí (L5). Výsledkem je složené skóre ANL nebo profil ukazující úrovně podle domén, což operátorům poskytuje jasný, standardizovaný pohled na jejich úroveň automatizace. To umožňuje cílené investice do [AI/ML](/mobilnisite/slovnik/ai-ml/) a orchestračních platforem pro postup na vyšší úrovně.

Role ANL je klíčová pro transformaci síťových operací z reaktivních, na člověka orientovaných modelů na proaktivní, softwarem řízené paradigma. Poskytuje společný jazyk pro výrobce a operátory, aby sladili své plány a schopnosti v oblasti automatizace. Kvantifikací autonomie pomáhá ověřovat návratnost investic do automatizačních technologií a zajišťuje, že různé síťové řezy nebo služby mohou být provozovány s definovanými úrovněmi autonomie, čímž podporuje širší cíle řízení sítě a služeb bez zásahu člověka (ZSM).

## K čemu slouží

ANL byl vytvořen, aby řešil rostoucí složitost a provozní nákladové výzvy v moderních sítích 5G a budoucích sítích 6G. Jak se sítě stávají více softwarově definovanými, virtualizovanými a řezy (slicing), tradiční manuální správa se stává nepraktickou, náchylnou k chybám a pomalou. Odvětví potřebovalo standardizovaný, objektivní způsob, jak měřit pokrok v automatizaci, který by překročil tvrzení specifická pro jednotlivé výrobce. ANL poskytuje toto měřítko, což operátorům umožňuje systematicky plánovat svou evoluci od starších [OSS](/mobilnisite/slovnik/oss/)/BSS k AI řízeným autonomním sítím.

Historicky byla síťová automatizace implementována v izolovaných silách bez jednotné škály zralosti, což ztěžovalo porovnávání řešení nebo stanovení cílů v celém odvětví. Omezení předchozích přístupů zahrnovala nedostatek jasných metrik pro posouzení efektivity investic do automatizace a neschopnost orchestračně řídit autonomní chování napříč doménami. ANL tyto problémy řeší vytvořením vícedimenzionálního rámce, který pokrývá celý životní cyklus síťových služeb od plánování přes optimalizaci až po samoléčení.

Motivace pro zavedení ANL v 3GPP Release-17 vycházela z naléhavé potřeby podporovat provoz sítě bez zásahu člověka (zero-touch), snížit OPEX a umožnit nové agilní služby, jako je síťové řezy (network slicing). Souladí se širšími iniciativami, jako je Zero-touch network and Service Management (ZSM) od ETSI a rámec Autonomous Network od TM Fora, a poskytuje technické definice a integrační body specifické pro 3GPP potřebné pro mobilní sítě. Tím, že definuje, co každá úroveň znamená v praktických termínech, pomáhá ANL odvětví přecházet k samojízdným sítím schopným splňovat přísné požadavky SLA pro rozmanité případy užití.

## Klíčové vlastnosti

- Definuje šestistupňovou škálu zralosti (L0 až L5) pro síťovou autonomii
- Poskytuje vícedoménové hodnocení pokrývající správu služeb, zdrojů a energie
- Standardizuje klíčové ukazatele výkonu (KPI) a hodnotící kritéria pro automatizaci
- Umožňuje srovnávání a plánování cestovní mapy (roadmap) pro automatizační cestu operátorů
- Integruje se s architekturami správy 3GPP, jako je MDAS a NWDAF, pro sběr dat
- Podporuje vizi řízení sítě a služeb bez zásahu člověka (ZSM)

## Definující specifikace

- **TS 28.100** (Rel-19) — Autonomous Network Concepts and Framework
- **TR 28.910** (Rel-19) — Enhancement of Autonomous Network Levels

---

📖 **Anglický originál a plná specifikace:** [ANL na 3GPP Explorer](https://3gpp-explorer.com/glossary/anl/)
