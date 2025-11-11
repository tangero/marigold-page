---
author: Marisa Aigen
category: kybernetická bezpečn
companies:
- Docker
- Kubernetes
date: '2025-11-09 15:11:12'
description: Tři nově odhalené zranitelnosti v runtime runC, používaném v Dockeru
  a Kubernetes, mohou útočníkům umožnit obejít izolaci kontejnerů a získat zápis na
  hostitelský systém s právy roota.
importance: 4
layout: tech_news_article
original_title: Dangerous runC flaws could allow hackers to escape Docker containers
  - BleepingComputer
publishedAt: '2025-11-09T15:11:12+00:00'
slug: dangerous-runc-flaws-could-allow-hackers-to-escape
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Nebezpečné chyby v runC umožňují útěk z Docker kontejnerů a kompromitaci hostitele
url: https://www.bleepingcomputer.com/news/security/dangerous-runc-flaws-could-allow-hackers-to-escape-docker-containers/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/08/28/hacker.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/08/28/hacker.jpg
---

## Souhrn
Nově zveřejněné zranitelnosti CVE-2025-31133, CVE-2025-52565 a CVE-2025-52881 v kontejnerovém runtime runC umožňují za určitých podmínek obejít izolaci Docker a Kubernetes kontejnerů a získat zápis na hostitelský systém s právy roota. Pro provozovatele kontejnerové infrastruktury jde o kritickou chybu v základním stavebním prvku celého ekosystému. Opravy jsou dostupné v nových verzích runC, avšak dopad závisí na rychlosti aktualizací a kvalitě bezpečnostní konfigurace.

## Klíčové body
- Tři zranitelnosti v runC umožňují únik z kontejneru a potenciální kompromitaci hostitele.
- CVE-2025-31133 a CVE-2025-52881 postihují všechny verze runC, CVE-2025-52565 verze od 1.0.0-rc3.
- Problémy zneužívají způsob, jakým runC pracuje s bind-mounty a speciálními soubory jako /dev/null a /dev/console.
- Opravy jsou dostupné v runC 1.2.8, 1.3.3, 1.4.0-rc.3 a novějších verzích.
- Doporučuje se okamžitá aktualizace a revize bezpečnostních politik v prostředích Docker a Kubernetes.

## Podrobnosti
runC je nízkoúrovňový runtime pro kontejnery a referenční implementace podle Open Container Initiative (OCI). Používají jej nástroje jako Docker, containerd či Kubernetes k vytváření a spuštění kontejnerů, nastavení jmenných prostorů, připojení souborových systémů a cgroups. Pokud je problém v runC, nejde o marginální chybu jednoho nástroje, ale o slabinu v infrastruktuře, na níž stojí velká část cloudových a interních služeb.

CVE-2025-31133 se týká způsobu, jakým runC maskuje citlivé soubory hostitele pomocí bind-mountu /dev/null. Pokud útočník během inicializace kontejneru nahradí /dev/null symbolickým odkazem, může runC omylem připojit útočníkem řízený cíl jako zapisovatelný do kontejneru. To může umožnit zápis do /proc a zneužití k úniku z kontejneru.

CVE-2025-52565 zneužívá bind-mount /dev/console. Pomocí závodních podmínek (race conditions) a symbolických odkazů lze přesměrovat mount na neočekávaný cíl ještě před aplikací ochranných mechanismů. Tím se opět otevírá cesta k zapisovatelnému přístupu k kritickým pseudo-souborům a potenciálnímu prolomení izolace.

CVE-2025-52881 umožňuje zneužít runC k zápisům do /proc, které jsou přesměrovány na cíle kontrolované útočníkem. V některých scénářích lze obejít mechanismy typu LSM (například SELinux) a proměnit legitimní zápisy runC v libovolné zápisy do citlivých souborů, včetně /proc/sysrq-trigger, což může vést k restartu systému nebo dalším destruktivním akcím.

Zranitelnosti samy o sobě typicky vyžadují, aby útočník měl možnost spouštět kontejnery nebo mít škodlivý obraz kontejneru. V multi-tenant cloudu, CI/CD prostředích, u poskytovatelů služeb nebo ve velkých interních platformách však jde o realistický scénář. Fixy jsou dostupné, ale skutečné riziko závisí na tom, zda provozovatelé rychle aktualizují runC (přímo či přes Docker, containerd, Kubernetes distribuce) a zda mají omezené schopnosti uživatelů manipulovat s mounty a speciálními zařízeními.

## Proč je to důležité
Tyto chyby míří na samotný základ kontejnerové izolace. Kontejnery jsou často mylně vnímány jako plnohodnotná bezpečnostní hranice; tento případ opět ukazuje, že jde primárně o izolační mechanismus sdílející jádro hostitele. Pro firmy provozující Docker a Kubernetes ve víceuživatelském či multi-tenant režimu se z technického problému v runC stává potenciálně kritická bezpečnostní událost: úspěšný útok může znamenat přístup k hostitelskému systému, datům dalších kontejnerů, tajným klíčům, CI/CD pipeline a dalším službám.

Z praktického hlediska je nutné:
- bezodkladně nasadit verze runC 1.2.8, 1.3.3, 1.4.0-rc.3 nebo novější (přímo, nebo skrze aktualizace Dockeru, containerd a Kubernetes distribucí),
- omezit možnost uživatelů vytvářet své vlastní privilegované kontejnery a manipulovat s /dev a mounty,
- revidovat předpoklady o důvěře v kontejnerovou izolaci, zejména v prostředích s nedůvěryhodnými nájemci.

Z hlediska širšího ekosystému tato zranitelnost zdůrazňuje potřebu systematické bezpečnostní analýzy nízkoúrovňových komponent, důsledné segmentace, využívání dalších vrstev ochrany (LSM, seccomp, sandboxing, runtime politiky) a opatrnosti při návrhu služeb závislých na kontejnerech jako na jediné bezpečnostní bariéře.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/dangerous-runc-flaws-could-allow-hackers-to-escape-docker-containers/)

**Zdroj:** 📰 BleepingComputer
