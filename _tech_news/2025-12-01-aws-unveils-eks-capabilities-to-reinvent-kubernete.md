---
author: Marisa Aigen
category: kubernetes
companies:
- Amazon Web Services Inc
date: '2025-12-01 21:46:24'
description: Amazon Web Services oznámila Amazon EKS Capabilities, plně spravovaný
  balík nástrojů nativních pro Kubernetes, které integrují populární open-source řešení
  přímo do řídicí roviny EKS. Tato novinka reaguje na explozivní růst AI úloh na Kubernetes
  a snižuje provozní složitost pro podnikové týmy.
importance: 3
layout: tech_news_article
original_title: AWS unveils EKS capabilities to reinvent Kubernetes operations as
  AI workloads surge
publishedAt: '2025-12-01T21:46:24+00:00'
slug: aws-unveils-eks-capabilities-to-reinvent-kubernete
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: AWS představuje nové schopnosti EKS pro přetvoření provozu Kubernetes v době
  růstu úloh umělé inteligence
url: https://siliconangle.com/2025/12/01/aws-unveils-eks-capabilities-reinvent-kubernetes-operations-ai-workloads-surge/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/Eswar-Bala-AWS.jpg
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/Eswar-Bala-AWS.jpg
---

## Souhrn
Amazon Web Services představila Amazon EKS Capabilities, sadu plně spravovaných nástrojů pro Kubernetes integrovaných přímo do služby Amazon EKS. Tyto nástroje cílí na zjednodušení správy infrastruktur pro rostoucí objem úloh umělé inteligence, kde Kubernetes slouží jako standardní řídicí rovina. AWS přebírá údržbu, škálování a aktualizace, aby vývojáři mohli soustředit na tvorbu aplikací.

## Klíčové body
- Integrace Argo CD: deklarativní GitOps systém pro automatizované nasazování aplikací z Git repozitářů, spravovaný AWS včetně vysoké dostupnosti a škálování.
- AWS Controllers for Kubernetes (ACK): umožňuje spravovat AWS cloudové zdroje přímo přes Kubernetes API, bez nutnosti samostatné správy kontrolních rovin.
- Podpora pro AI workloads: zaměření na GPU batch jobs, multimodální inference a agentické úlohy s ročním zdvojnásobením použití GPU v Kubernetes.
- Snížení provozní zátěže: vývojáři dnes tráví 70 % času správou infrastruktury, EKS Capabilities tento podíl snižuje.
- Tři plně spravované komponenty pro Kubernetes ve velkém měřítku.

## Podrobnosti
Amazon EKS Capabilities představují významný krok v optimalizaci Kubernetes pro podnikové prostředí, zejména v kontextu umělé inteligence. Služba Amazon EKS, což je spravovaná verze Kubernetes od AWS, nyní nativně integruje open-source nástroje jako Argo CD a AWS Controllers for Kubernetes (ACK). Argo CD funguje jako GitOps nástroj, který deklarativně synchronizuje stav aplikací definovaný v Git repozitářích s Kubernetes klastrem. To znamená, že týmy definují požadovaný stav v kódu a systém automaticky nasadí změny, což minimalizuje manuální zásahy a chyby. AWS se stará o veškerou infrastrukturu Argo CD, včetně upgradů, záplat, vysoké dostupnosti a automatického škálování, což podle AWS používá téměř polovina Kubernetes týmů v produkci.

AWS Controllers for Kubernetes umožňují organizacím řídit AWS služby, jako jsou databáze nebo úložiště, přímo jako nativní Kubernetes zdroje. Například lze vytvořit custom resource pro Amazon RDS databázi a Kubernetes ji automaticky nasadí a spravuje, bez nutnosti opouštět Kubernetes API. AWS přebírá nasazování, provoz a řešení problémů těchto integrací. Třetí komponentou je Kubernetes Resource Orchestrator, který pomáhá s orchestrací zdrojů ve velkém měřítku.

Podle Eswara Balu, ředitele inženýrství kontejnerů u AWS, Kubernetes se stal výchozí řídicí rovinou pro AI, s ročním zdvojnásobením použití GPU. Zákazníci potřebují automatizaci pro agentické workloads, multimodální inference a GPU batch jobs. EKS Capabilities tyto požadavky řeší tím, že přesouvají zátěž správy z vývojářů na AWS, což podle Baly snižuje čas vynaložený na infrastrukturu z 70 % na minimum. Novinka byla oznámena před konferencí re:Invent v prosinci 2025.

## Proč je to důležité
Tato aktualizace posiluje pozici Kubernetes jako standardu pro AI workloads v cloudu, kde AWS konkuruje Azure AKS a Google GKE. Pro podnikové týmy znamená méně provozních starostí a vyšší produktivitu, což je klíčové při škálování AI modelů na GPU clustery. V širším ekosystému urychluje adopci GitOps a operator patternů, standardizuje správu hybridních cloudů a snižuje rizika spojená s custom integracemi. Nicméně závislost na AWS může omezit flexibilitu pro multicloud strategie, a dlouhodobý úspěch závisí na výkonu oproti open-source alternativám.

---

[Číst původní článek](https://siliconangle.com/2025/12/01/aws-unveils-eks-capabilities-reinvent-kubernetes-operations-ai-workloads-surge/)

**Zdroj:** 📰 SiliconANGLE News
