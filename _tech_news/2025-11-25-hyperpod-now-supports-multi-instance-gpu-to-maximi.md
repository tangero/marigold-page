---
author: Marisa Aigen
category: ai infrastruktura
companies:
- Amazon
- NVIDIA
date: '2025-11-25 16:10:39'
description: Amazon SageMaker HyperPod nyní podporuje technologii NVIDIA Multi-Instance
  GPU (MIG), která umožňuje rozdělit výkonné GPU na několik izolovaných instancí pro
  paralelní spouštění různých úloh, jako je inference, výzkum nebo interaktivní práce.
importance: 3
layout: tech_news_article
original_title: HyperPod now supports Multi-Instance GPU to maximize GPU utilization
  for generative AI tasks
publishedAt: '2025-11-25T16:10:39+00:00'
slug: hyperpod-now-supports-multi-instance-gpu-to-maximi
source:
  emoji: 📰
  id: null
  name: Amazon.com
title: HyperPod nyní podporuje Multi-Instance GPU pro lepší využití GPU při generativních
  AI úlohách
url: https://aws.amazon.com/blogs/machine-learning/hyperpod-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-generative-ai-tasks/
urlToImage: https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/ML-19983-2-1144x630.png
urlToImageBackup: https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/ML-19983-2-1144x630.png
---

## Souhrn
Amazon SageMaker HyperPod nyní plně podporuje technologii NVIDIA Multi-Instance GPU (MIG), díky čemuž lze jednotlivá GPU rozdělit na více izolovaných instancí. Tato funkce zvyšuje využití výpočetních a paměťových prostředků při běhu lehkých AI úloh, jako je inference jazykových modelů, prototypování modelů nebo práce v Jupyter notebooku.

## Klíčové body
- HyperPod nyní umožňuje paralelní běh více úloh na jednom fyzickém GPU pomocí MIG.
- Podpora zahrnuje GPU založené na architektuře NVIDIA Ampere, například A100 (EC2 P4) a A10G (EC2 G5).
- Izolace mezi instancemi zajišťuje bezpečnost a stabilitu výkonu jednotlivých úloh.
- Administrátoři clusterů mohou efektivněji alokovat zdroje mezi různé týmy (datoví vědci, ML inženýři, infrastruktura).
- Snížení čekacích dob na GPU a zkrácení vývojových cyklů.

## Podrobnosti
NVIDIA Multi-Instance GPU (MIG) byla představena v roce 2020 spolu s architekturou Ampere. Umožňuje rozdělit jedno GPU (např. A100) na až sedm nezávislých instancí, z nichž každá má vlastní paměť, cache a výpočetní jednotky. Amazon nyní tuto technologii integroval do SageMaker HyperPod – spravované platformy pro škálovatelný vývoj a nasazení AI modelů. Díky tomu mohou uživatelé spouštět lehké úlohy, které by jinak nevyužívaly plný výkon celého GPU, na menších izolovaných částech. Například inference jazykového modelu nebo experimenty s klasifikací obrazu v Jupyter notebooku mohou běžet paralelně na stejném hardwaru bez vzájemného ovlivnění. Platforma zároveň poskytuje přehled o využití výpočetních a paměťových zdrojů na úrovni jednotlivých MIG instancí.

## Proč je to důležité
Tato funkce přináší významné zlepšení efektivity výpočetních clusterů, zejména v prostředích, kde běží směs lehkých a náročných úloh. Pro organizace, které provozují vlastní AI infrastrukturu v cloudu, to znamená nižší náklady a lepší využití investic do drahých GPU. Zároveň podporuje agilnější vývoj – datoví vědci nemusí čekat na uvolnění celého GPU, ale mohou okamžitě využít dostupnou MIG instanci. V kontextu rostoucí poptávky po generativní AI jde o pragmatický krok k optimalizaci existujících zdrojů, nikoli o zásadní průlom, ale jistě o užitečné vylepšení pro praxi.

---

[Číst původní článek](https://aws.amazon.com/blogs/machine-learning/hyperpod-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-generative-ai-tasks/)

**Zdroj:** 📰 Amazon.com
