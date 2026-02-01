---
author: Marisa Aigen
category: kybernetika
companies:
- ESET
date: '2026-01-30 16:09:00'
description: Výzkumníci ESET identifikovali nový mazací malware DynoWiper použitý
  proti energetické společnosti v Polsku. Taktiky, techniky a postupy (TTPs) připomínají
  útok s wiperem ZOV na Ukrajině, přičemž ESET připisuje útok ruské skupině Sandworm
  s střední jistotou.
importance: 5
layout: tech_news_article
original_title: Russian Sandworm group attacks energy company in Poland with DynoWiper,
  ESET Research discovers
publishedAt: '2026-01-30T16:09:00+00:00'
slug: russian-sandworm-group-attacks-energy-company-in-p
source:
  emoji: 📰
  id: null
  name: GlobeNewswire
title: Skupina Sandworm z Ruska zaútočila na energetickou společnost v Polsku pomocí
  DynoWiper, objevila výzkum ESET
url: https://www.globenewswire.com/news-release/2026/01/30/3229631/0/en/Russian-Sandworm-group-attacks-energy-company-in-Poland-with-DynoWiper-ESET-Research-discovers.html
urlToImage: https://ml.globenewswire.com/Resource/Download/d6434bd9-71ad-46f5-b1c8-81bd2b967640
urlToImageBackup: https://ml.globenewswire.com/Resource/Download/d6434bd9-71ad-46f5-b1c8-81bd2b967640
---

## Souhrn
Výzkumníci společnosti ESET, která se specializuje na detekci a prevenci kybernetických hrozeb, objevili nový typ mazacího malwaru nazvaného DynoWiper. Tento malware byl nasazen proti energetické společnosti v Polsku, což představuje vzácný případ útoku rusky orientované skupiny na cíl mimo Ukrajinu. ESET připisuje autorství skupině Sandworm s střední mírou jistoty na základě podobnosti taktik, technik a postupů (TTPs) s předchozími incidenty.

## Klíčové body
- Nový mazací malware DynoWiper nasazen 29. prosince 2025 v sdíleném adresáři oběti, pravděpodobně po testech na virtuálních strojích.
- ESET PROTECT (EDR/XDR řešení pro detekci a reakci na koncových zařízeních) zablokovalo spuštění malwaru a omezilo škody.
- TTPs shodné s wiperem ZOV použitým na Ukrajině, včetně symbolů Z, O, V odkazujících na ruské vojenské značky.
- Sandworm: Ruská hackerská skupina spojená s GRU, zodpovědná za útoky jako NotPetya a útoky na ukrajinskou energetiku.
- CERT Polska provedlo podrobnou analýzu incidentu, dostupnou na svém webu.

## Podrobnosti
ESET v roce 2025 vyšetroval více než 10 incidentů s destruktivním malwarovým připisovaným Sandwormu, převážně na Ukrajině. DynoWiper je datový wiper, což znamená, že jeho primárním cílem je trvalé vymazání dat na disku, což může paralyzovat systémy bez možnosti obnovy. Na rozdíl od ransomwaru, který šifruje data za účelem vydírání, wipery slouží k čisté destrukci, často v kontextu hybridní války nebo sabotáže kritické infrastruktury.

Útok proběhl 29. prosince 2025, kdy operátoři Sandwormu nasadili vzorky malwaru do sdíleného adresáře v doméně oběti. Před nasazením pravděpodobně testovali na virtuálních strojích, což je standardní taktika pro minimalizaci rizik odhalení. ESET PROTECT, který kombinuje endpoint detection and response (EDR) s extended detection and response (XDR) pro širokou síťovou viditelnost, detekoval a zablokoval spuštění, čímž významně omezil dopad. Tato platforma slouží k monitorování chování, detekci anomálií a automatické reakci na hrozby v reálném čase.

Skupina Sandworm, známá také jako APT44 nebo Voodoo Bear, je spojena s ruskou vojenskou zpravodajskou službou GRU. Mezi jejich významné operace patří útok NotPetya v roce 2017, který způsobil globální škody v miliardách dolarů, a opakované útoky na ukrajinskou energetickou síť v letech 2015–2016, včetně wiperu Industroyer. Wiper ZOV, použitý nedávno na Ukrajině, sdílí s DynoWiper podobné TTPs, jako je inicializace přes sdílené složky a specifické mazací mechanismy. ESET dospěl k připisání s střední jistotou kvůli shodám v chování, ale bez jednoznačných indikátorů jako unikátní kódy.

CERT Polska, národní tým pro reakci na počítačové nouzové situace v Polsku, provedlo forenzní analýzu a zveřejnilo detailní zprávu. Tento incident podtrhuje evoluci wiperů: DynoWiper je navržen pro maximální ničení, s možností šíření v lokální síti.

## Proč je to důležité
Tento útok signalizuje eskalaci ruské kybernetické agrese směrem k NATO zemím, konkrétně Polsku, které hraničí s Ukrajinou a podporuje Kyjev. Energetická infrastruktura je kritická – její paralýza by mohla způsobit výpadky proudu, ekonomické ztráty a chaos. Na rozdíl od ukrajinských incidentů, kde wipery způsobily reálné výpadky, zde EDR minimalizovalo škody, což zdůrazňuje nutnost robustní obrany.

Pro průmysl to znamená zvýšené riziko pro energetiku v Evropě: organizace by měly implementovat EDR/XDR, segmentaci sítí a pravidelné zálohy mimo síť. V širším kontextu posiluje to debatu o hybridní válce, kde kyberútoky doplňují konvenční konflikty. ESETovo odhalení přispívá k globálnímu sdílení indikátorů hrozeb (IoC), což pomáhá prevenci. Celkově to připomíná, že státní aktéři jako Sandworm neváhají cílit civilní infrastrukturu, což vyžaduje koordinovanou odpověď EU a NATO.

---

[Číst původní článek](https://www.globenewswire.com/news-release/2026/01/30/3229631/0/en/Russian-Sandworm-group-attacks-energy-company-in-Poland-with-DynoWiper-ESET-Research-discovers.html)

**Zdroj:** 📰 GlobeNewswire
