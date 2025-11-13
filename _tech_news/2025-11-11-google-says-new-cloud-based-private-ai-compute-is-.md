---
author: Marisa Aigen
category: ai bezpečnost
companies:
- Google
date: '2025-11-11 21:34:10'
description: Google zavádí systém Private AI Compute, který umožňuje zařízením bezpečně
  využívat výkonné cloudové AI modely přes šifrované prostředí s hardwarově oddělenou
  pamětí. Tvrdí, že ochrana dat je srovnatelná s lokálním zpracováním na zařízení.
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
title: 'Google představuje cloudové „Private AI Compute“: slibuje bezpečnost na úrovni
  lokálního zpracování'
url: https://arstechnica.com/google/2025/11/google-says-new-cloud-based-private-ai-compute-is-just-as-secure-as-local-processing/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/Google_Private_Inference-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/Google_Private_Inference-1152x648.jpg
---

## Souhrn
Google spouští Private AI Compute, cloudovou architekturu pro provoz AI, která má umožnit využití největších modelů Gemini bez toho, aby měl k datům přístup samotný Google. Využívá kombinaci vlastních čipů TPU, šifrovaného přenosu a Trusted Execution Environment (TEE), a cílí na to, aby bezpečnost odpovídala lokálnímu zpracování na telefonu či notebooku.

## Klíčové body
- Private AI Compute umožňuje zařízením napojit se přímo do izolovaného a šifrovaného prostředí v cloudu Google.
- Běží na vlastních čipech TPU se zabudovanými bezpečnostními prvky a TEE založeném na platformě AMD.
- Google tvrdí, že k uživatelským datům v tomto prostředí nemá přístup ani interně.
- Systém má zkombinovat výhody lokálního zpracování s výkonem velkých modelů Gemini v cloudu.
- Bezpečnostní architekturu posuzovala externí společnost NCC Group.

## Podrobnosti
Private AI Compute je technická a politická odpověď Google na rostoucí tlak kolem ochrany soukromí při využití generativní AI. Koncept je podobný Apple Private Cloud Compute: uživatelská data jsou zpracována v odděleném, hardwarově chráněném prostoru v datových centrech, přičemž poskytovatel služby deklaruje, že k obsahu nemá přímý přístup.

Technicky je systém postaven na „jednotném stacku Google“, který zahrnuje vlastní čipy TPU pro akceleraci AI a Trusted Execution Environment (TEE) založený na architektuře AMD. TEE zajišťuje, že paměť využívaná pro konkrétní AI úlohy je šifrovaná a izolovaná jak od hostitelského systému, tak od ostatních procesů. Komunikace mezi zařízením uživatele a tímto prostředím probíhá přes šifrovaný kanál, takže data nemají procházet běžnou interní infrastrukturou Google v čitelné podobě.

V praxi to znamená, že zařízení (například telefony Pixel) mohou rozhodovat, zda úlohu zpracovat lokálně pomocí modelu Gemini Nano, nebo ji poslat do Private AI Compute pro složitější operace, které vyžadují větší výkon a přístup k robustnějším modelům Gemini. Lokální AI na zařízení je stále preferovaná pro citlivé a menší úlohy, ale nepostačuje pro komplexní generování, analýzu větších objemů dat nebo pokročilé multimodální funkce.

Google dále argumentuje nezávislým posouzením bezpečnostní architektury společností NCC Group, která se zabývá kybernetickým zabezpečením. Klíčový claim je, že tento přístup dosahuje srovnatelné bezpečnostní úrovně jako zpracování dat pouze na zařízení, přestože fyzicky probíhá v cloudu.

## Proč je to důležité
Private AI Compute je strategický krok v boji o definici „bezpečné AI v cloudu“. Google potřebuje přístup k výkonným modelům na straně serveru, ale zároveň musí uklidnit uživatele, regulátory a firemní zákazníky, že jejich data nejsou využívána k tréninku modelů nebo interní analýze bez kontroly. Pokud bude architektura technicky i procesně dodržena, může významně snížit bariéry pro nasazení generativní AI v regulovaných odvětvích, jako jsou finance, zdravotnictví nebo veřejná správa.

Současně jde o posun v debatě „edge vs. cloud“. Google implicitně přiznává, že čistě lokální AI nestačí pro nejnáročnější scénáře, a snaží se normalizovat model, kde citlivá data opouštějí zařízení, ale jen do kryptograficky a hardwarově omezeného prostoru. Skutečná důvěryhodnost konceptu bude záviset na transparentnosti implementace, dostupnosti nezávislých auditů, jasných smluvních zárukách (zejména ohledně netrénování na soukromých datech) a na tom, jak se tento přístup bude chovat v praxi při reálných útocích a incidentových scénářích.

---

[Číst původní článek](https://arstechnica.com/google/2025/11/google-says-new-cloud-based-private-ai-compute-is-just-as-secure-as-local-processing/)

**Zdroj:** 🔬 Ars Technica
