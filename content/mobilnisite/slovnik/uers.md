---
slug: "uers"
url: "/mobilnisite/slovnik/uers/"
type: "slovnik"
title: "UERS – UE Request Session"
date: 2025-01-01
abbr: "UERS"
fullName: "UE Request Session"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/uers/"
summary: "UE Request Session (UERS) je koncept správy definovaný v 3GPP pro sběr výkonnostních měření a dat trasování. Reprezentuje specifickou, uživatelskou iniciovanou relaci pro získání detailních informací"
---

UERS je koncept správy pro uživatelskou iniciovanou relaci, která shromažďuje výkonnostní měření a data trasování o chování UE a výkonu sítě pro optimalizaci a řešení problémů.

## Popis

UE Request Session (UERS) je formalizovaný postup v rámci managementového frameworku 3GPP, detailně specifikovaný v TS 28.307 a referencovaný v TS 28.404. Vytváří řízenou relaci pro operátora sítě, aby shromáždil data performance managementu ([PM](/mobilnisite/slovnik/pm/)) a fault managementu ([FM](/mobilnisite/slovnik/fm/)) přímo asociované s konkrétním User Equipment (UE) nebo skupinou UE. Tato relace je iniciována na základě requestu, typicky z network management systemu ([NMS](/mobilnisite/slovnik/nms/)) nebo operation support systemu ([OSS](/mobilnisite/slovnik/oss/)), pro získání granularních dat, které nejsou částí standardního periodického reportování.

Architektonicky UERS funguje v ekosystému Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)) a Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)), nebo více tradičně v frameworku Trace Collection Entity ([TCE](/mobilnisite/slovnik/tce/)). Relace zahrnuje několik síťových funkcí. Iniciující managementový systém zasílá request na aktivaci relace příslušné síťové node (např. gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE), která pak konfiguruje nezbytné sondy a body sběru dat pro cílové UE. Shromážděná data proudí od Radio Access Network (RAN) a Core Network (CN) funkcí k určenému sběrnému bodu.

Relace definuje parametry jako délku, typy měření (např. radio link failures, handover success rates, application throughput) a granularitu dat trasování (např. signaling messages, user plane packets). Funguje aktivací specifických measurement jobs a zaznamenávání trasování na zapojených síťových entitách pouze pro délku a scope relace. Tento targeted přístup minimalizuje celkové síťové overheady ve srovnání s kontinuálním blanket trasováním.

Jeho role je klíčová pro hlubokou síťovou diagnostiku, management zkušenosti zákazníka a service assurance. Díky možnosti získat on-demand detailní insight do UE-specific relací mohou operátoři izolovat a řešit komplexní problémy, validovat výkon sítě po změnách a shromažďovat data pro capacity planning a optimalizační algoritmy. Transformuje reactive troubleshooting na více proactive a precise managementovou schopnost.

## K čemu slouží

UERS byl vytvořen pro řešení limitací širokého, celosíťového performance monitoringu a neefektivity permanentní, high-volume aktivace trasování. Před jeho formalizací sběr detailních UE-specific dat často vyžadoval aktivaci rozsáhlého trasování přes velké síťové segmenty, generující masivní objemy dat nákladné na uložení a zpracování, a potenciálně ovlivňující výkon sítě. To byl blunt instrument pro řešení specifických, user-reported problémů.

Technologie řeší problém targeted acquisition dat. Umožňuje síťovým operátorům chirurgicky shromažďovat high-fidelity data spojené s specifickou service issue, problematickou geografickou oblastí nebo chováním konkrétního modelu UE, bez zahlcení managementových systémů irelevantními informacemi. To je zvláště kritické v 5G a dalších generacích, s network slicing, diverzními service requirements (eMBB, URLLC, mMTC) a dynamic resource allocation, kde je pochopení end-to-end výkonu specifického slice nebo service instance paramount.

Historicky jeho introdukce v Release 15 se shoduje s 5G phase 1 standardy, které zdůrazňovaly síťovou automatizaci, data-driven operaci a enhanced management capabilities. UERS poskytuje foundational mechanism pro closed-loop automatizaci, kde analytics (např. z NWDAF) mohou triggerovat sběrnou relaci pro investigation anomaly, a výsledky mohou být feedbackem do systému pro triggerování corrective akcí, umožňující self-optimizing networks (SON) a AI-driven operations.

## Klíčové vlastnosti

- On-demand aktivace a deaktivace relace pro targeted sběr dat
- Konfigurovatelný scope targeting specifické UE, skupiny UE nebo geografické oblasti
- Podpora sběru dat Performance Measurement (PM) i detailních Trace dat
- Definované parametry lifetime relace zahrnující start time, duration a stop conditions
- Integrace s management systémy (OSS/NMS) a analytics funkcemi (NWDAF)
- Standardizované interfaces a data formáty pro consistent sběr přes multi-vendor sítě

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 28.307** (Rel-19) — QoE Measurement Collection IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [UERS na 3GPP Explorer](https://3gpp-explorer.com/glossary/uers/)
