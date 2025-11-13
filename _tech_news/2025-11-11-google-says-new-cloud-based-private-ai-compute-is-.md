---
author: Marisa Aigen
category: ai bezpečnost
companies:
- Google
- Apple
date: '2025-11-11 21:34:10'
description: Google zavádí systém Private AI Compute, který umožňuje zašifrované zpracování
  dat v cloudu na specializované infrastruktuře s cílem nabídnout výkon pokročilých
  modelů Gemini při úrovni ochrany blízké lokálnímu výpočtu.
importance: 4
layout: tech_news_article
original_title: Google says new cloud-based “Private AI Compute” is just as secure
  as local processing - Ars Technica
publishedAt: '2025-11-11T21:34:10+00:00'
slug: google-says-new-cloud-based-private-ai-compute-is-
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: 'Google představuje Private AI Compute: cloudové zpracování dat má být stejně
  bezpečné jako lokální'
url: https://arstechnica.com/google/2025/11/google-says-new-cloud-based-private-ai-compute-is-just-as-secure-as-local-processing/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/Google_Private_Inference-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/Google_Private_Inference-1152x648.jpg
---

## Souhrn
Google představil Private AI Compute, nový systém pro bezpečné cloudové zpracování dat, který má uživatelům umožnit využívat výkonné modely Gemini bez toho, aby k datům měl přístup samotný Google. Řešení kombinuje vlastní čipy Tensor Processing Units (TPU), šifrované spojení a Trusted Execution Environment (TEE) a míří na scénář, kdy lokální výkon telefonů a notebooků nestačí.

## Klíčové body
- Private AI Compute využívá chráněné běhové prostředí (TEE) nad TPU s oddělenou a šifrovanou pamětí.
- Google tvrdí, že k datům zpracovávaným v Private AI Compute nemá přístup ani interně, podobně jako u konceptu Apple Private Cloud Compute.
- Systém má umožnit používání velkých modelů Gemini v situacích, kde on‑device AI (např. Gemini Nano) výkonově nestačí.
- Bezpečnostní architekturu posuzovala nezávislá společnost NCC Group, Google se odvolává na shodu s vlastními přísnějšími zásadami ochrany soukromí.
- Google se strategicky snaží sjednotit edge AI a cloud AI do jedné architektury a tím snížit obavy z odesílání osobních dat do cloudu.

## Podrobnosti
Private AI Compute je navržen jako vyhrazené, izolované prostředí v datových centrech Googlu, postavené na vlastních čipech TPU a bezpečnostních funkcích procesorů AMD. Trusted Execution Environment (TEE) zde funguje jako hardwarově vynucené oddělení, kde jsou data i běžící modely šifrovány v paměti a mají být nepřístupné hostitelskému systému, administrátorům i jiným službám. Klientské zařízení se připojuje k tomuto prostředí přes koncové šifrování, takže Google deklaruje, že nedisponuje čitelnými vstupy ani výstupy mimo TEE.

Z hlediska použití má Private AI Compute sloužit jako rozšíření edge AI. Na zařízení běží menší modely, jako Gemini Nano v telefonech Pixel, které zvládají jednodušší úlohy přímo lokálně: sumarizace textu, offline přepis, základní asistent. Jakmile je potřeba větší kontext, multimodální zpracování či komplexnější generování, může se požadavek přesměrovat do Private AI Compute, kde běží větší modely Gemini s výrazně vyšším výpočetním výkonem. Uživatel tak formálně neopouští „privátní režim“, ale technicky dochází k odeslání dat do cloudové infrastruktury.

Google se tímto přibližuje konceptu Apple Private Cloud Compute: cloud jako rozšíření zařízení, nikoliv jako plně důvěryhodný prostředník. Rozdíl je v implementaci a v tom, že Google explicitně staví na své AI infrastruktuře (TPU stack) a chce tento přístup použít napříč produkty – od Pixel zařízení po podnikové služby Google Cloud. Nezávislé posouzení NCC Group má dodat důvěryhodnost tvrzení, že ani Google jako provozovatel nemá mít realistickou možnost data číst nebo zneužít.

Pro uživatele a firmy může být praktický přínos v tom, že získají přístup k výkonným AI funkcím bez nutnosti rezignovat na základní principy ochrany dat. V praxi však přijde na detailní implementaci: jak transparentní bude auditovatelnost, jak budou omezeny logy, jak se zabrání kombinaci metadat s jinými zdroji, a do jaké míry budou tyto záruky závazně zakotveny v podmínkách služeb.

## Proč je to důležité
Private AI Compute je důležitý krok ve sporu mezi dvěma modely vývoje AI služeb: čistě lokální zpracování vs. centralizovaný cloud. Google se snaží zavést třetí cestu: cloudový výkon s deklarovaně lokální úrovní soukromí. Pokud bude architektura skutečně technicky i smluvně vynutitelná, může to snížit bariéru pro nasazení generativní AI v regulovaných sektorech (finance, zdravotnictví, veřejná správa), kde je dnes odesílání dat do cloudu problematické.

Zároveň jde o konkurenční reakci na Apple a další hráče, kteří propagují on‑device AI jako bezpečnější alternativu. Google tím uznává, že bez důvěry v ochranu dat nebude masové přijímání generativní AI udržitelně růst. Kriticky je však nutné sledovat, zda „bez přístupu Googlu k datům“ zůstane pouze marketingovým tvrzením, nebo bude podloženo otevřenou dokumentací, nezávislým auditem, možností kryptografické verifikace a transparentní regulací. Pro celý ekosystém AI bezpečnosti je tento model testem, zda lze velké cloudové modely provozovat způsobem, který respektuje minimální nutnost důvěry v poskytovatele.

---

[Číst původní článek](https://arstechnica.com/google/2025/11/google-says-new-cloud-based-private-ai-compute-is-just-as-secure-as-local-processing/)

**Zdroj:** 🔬 Ars Technica
