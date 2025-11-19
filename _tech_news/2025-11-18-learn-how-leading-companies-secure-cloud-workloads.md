---
author: Marisa Aigen
category: cloudová bezpečnost
date: '2025-11-18 11:55:00'
description: Přechod do cloudu přináší rychlost a flexibilitu, ale také zvyšuje rizika
  spojená s přístupem a zranitelnostmi. Zvláště u kontejnerů je nutné řešit bezpečnost
  již od fáze vývoje až po provoz.
importance: 3
layout: tech_news_article
original_title: Learn How Leading Companies Secure Cloud Workloads and Infrastructure
  at Scale
publishedAt: '2025-11-18T11:55:00+00:00'
slug: learn-how-leading-companies-secure-cloud-workloads
source:
  emoji: 📰
  id: null
  name: Internet
title: Jak přední firmy zabezpečují cloudové úlohy a infrastrukturu ve velkém měřítku
url: https://thehackernews.com/2025/11/learn-how-leading-companies-secure.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbcnxxrLCNLtK2nayB0ljqkqYjos86JEosexUyndcUIx-1Bq4QIjQ7HEsPubzDGy_ZQiwc8Otm_rOZ94X_R8mDzqhCdwjETneYetBvv54f7askg7riPyV0GEVIYA6RIo6bkbFw8g6HCJPok_liEsSirCMxE3jkrLczdpV_4Sq2vw5NMJzqU2Z8btfgyfY/s790-rw-e365/webinar.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbcnxxrLCNLtK2nayB0ljqkqYjos86JEosexUyndcUIx-1Bq4QIjQ7HEsPubzDGy_ZQiwc8Otm_rOZ94X_R8mDzqhCdwjETneYetBvv54f7askg7riPyV0GEVIYA6RIo6bkbFw8g6HCJPok_liEsSirCMxE3jkrLczdpV_4Sq2vw5NMJzqU2Z8btfgyfY/s790-rw-e365/webinar.jpg
---

## Souhrn
Bezpečnost cloudové infrastruktury a kontejnerů se stává kritickou výzvou pro firmy, které škálují své služby v prostředí jako AWS, Azure nebo Google Cloud. Článek shrnuje pět klíčových postupů pro zabezpečení kontejnerů od fáze sestavení (build) až po běh (runtime), což je nezbytné pro prevenci útoků a dodržení compliance.

## Klíčové body
- Zabezpečení začíná už při vývoji – skenování závislostí a základních obrazů (base images)
- Použití podepisování obrazů (image signing) pro zajištění integrity
- Minimální oprávnění a izolace běžících kontejnerů
- Kontinuální monitorování chování kontejnerů v provozu
- Automatizovaná odpověď na detekované hrozby

## Podrobnosti
Kontejnery, zejména v orchestraci Kubernetes, se vytvářejí a likvidují v řádu sekund, což komplikuje tradiční přístupy k bezpečnosti. Proto je nutné implementovat bezpečnostní opatření již v CI/CD pipeline. To zahrnuje skenování obrazů nástroji jako Trivy nebo Snyk, které odhalují známé zranitelnosti v knihovnách a operačním systému. Dále je důležité používat podepisování obrazů pomocí technologií jako Cosign nebo Notary, aby bylo možné ověřit, že spuštěný kontejner pochází z důvěryhodného zdroje.

V provozu je klíčové omezit oprávnění kontejnerů – například zakázat privilegovaný režim a používat security context v Kubernetes. Runtime ochrana pak zahrnuje detekci anomálií chování, například nečekané síťové spojení nebo přístup k citlivým souborům. Nástroje jako Falco nebo Aqua Security umožňují tyto aktivity monitorovat a případně automaticky izolovat ohrožený kontejner.

## Proč je to důležité
S rostoucím nasazením mikroslužeb a serverless architektur se útočná plocha rozšiřuje. Bez systematického přístupu k bezpečnosti kontejnerů hrozí únik dat, kompromitace celého clusteru nebo výpadek kritických služeb. Tento přístup není jen otázkou technického nastavení, ale i kultury DevSecOps, kde bezpečnostní týmy spolupracují s vývojáři od samého počátku. V kontextu cloudové bezpečnosti jde o jednu z nejvíce citlivých oblastí, kde zanedbání základních principů může vést k vážným incidentům.

---

[Číst původní článek](https://thehackernews.com/2025/11/learn-how-leading-companies-secure.html)

**Zdroj:** 📰 Internet
