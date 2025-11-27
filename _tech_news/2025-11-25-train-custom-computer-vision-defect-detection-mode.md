---
author: Marisa Aigen
category: počítačové vidění
companies:
- Amazon
- AWS
date: '2025-11-25 22:44:22'
description: Amazon ukončuje službu Lookout for Vision a doporučuje zákazníkům přechod
  na SageMaker AI s využitím předtrénovaných modelů z AWS Marketplace pro detekci
  vad ve výrobních procesech.
importance: 3
layout: tech_news_article
original_title: Train custom computer vision defect detection model using Amazon SageMaker
publishedAt: '2025-11-25T22:44:22+00:00'
slug: train-custom-computer-vision-defect-detection-mode
source:
  emoji: 📰
  id: null
  name: Amazon.com
title: Trénování vlastního modelu počítačového vidění pro detekci vad pomocí Amazon
  SageMaker
url: https://aws.amazon.com/blogs/machine-learning/train-custom-computer-vision-defect-detection-model-using-amazon-sagemaker/
urlToImage: https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-6-2-775x630.jpeg
urlToImageBackup: https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-6-2-775x630.jpeg
---

## Souhrn
Amazon oznámil ukončení služby Lookout for Vision ke konci října 2025 a zákazníkům doporučuje přechod na Amazon SageMaker AI. K usnadnění migrace zpřístupnil na AWS Marketplace předtrénovaný model pro detekci vad, který lze fine-tunovat podle konkrétních požadavků průmyslových aplikací.

## Klíčové body
- Služba Amazon Lookout for Vision bude ukončena 31. října 2025.
- AWS poskytuje předtrénovaný model pro detekci vad na AWS Marketplace, určený k fine-tuningu v SageMakeru.
- Model podporuje dva typy úloh: binární klasifikaci a sémantickou segmentaci.
- Uživatelé získávají plnou kontrolu nad hyperparametry a architekturou modelu.
- Řešení lze nasadit jak v cloudu, tak na periferních (edge) zařízeních.

## Podrobnosti
Amazon Lookout for Vision byl specializovaný nástroj pro automatizovanou kontrolu kvality založenou na počítačovém vidění, určený především pro průmyslové aplikace. Jeho ukončení vede k potřebě alternativního řešení, které AWS nabízí prostřednictvím SageMakeru – univerzální platformy pro vývoj, trénování a nasazení modelů strojového učení. Na AWS Marketplace je nyní k dispozici předtrénovaný model zaměřený na detekci vad, který lze přizpůsobit konkrétním datům zákazníka. Tento model podporuje jak binární klasifikaci (vadný/nevadný), tak sémantickou segmentaci (přesné lokalizování vad na obrázku). Díky integraci se SageMakerem mohou uživatelé využít výkonné GPU instance pro rychlejší trénink, upravovat hyperparametry nebo dokonce měnit architekturu modelu – například vypnout binární klasifikační hlavu u multi-head modelu pro sémantickou segmentaci. Tato flexibilita umožňuje lepší přizpůsobení řešení specifickým požadavkům výrobních linek a integraci s existující infrastrukturou.

## Proč je to důležité
Přechod z uzavřené služby Lookout for Vision na otevřenější SageMaker poskytuje zákazníkům větší kontrolu a škálovatelnost, ale zároveň vyžaduje hlubší technické znalosti. Pro průmyslové podniky to znamená možnost vytvářet robustnější a přesnější systémy kontroly kvality, avšak s vyššími nároky na interní AI týmy. Tento krok také odráží širší trend AWS: místo specializovaných „black-box“ služeb preferovat univerzální platformy s modulárními komponentami, které umožňují větší přizpůsobitelnost a dlouhodobou udržitelnost řešení.

---

[Číst původní článek](https://aws.amazon.com/blogs/machine-learning/train-custom-computer-vision-defect-detection-model-using-amazon-sagemaker/)

**Zdroj:** 📰 Amazon.com
