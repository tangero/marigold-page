---
author: Marisa Aigen
category: důvěrný výpočet
companies:
- AWS
- Red Hat
date: '2025-12-01 00:00:00'
description: Důvěrný výpočet chrání citlivá data nejen při ukládání nebo přenosu,
  ale i během zpracování v paměti, což je tradičně nejslabší fáze. Článek ukazuje
  implementaci bezpečného prostředí za běhu pomocí AWS Nitro Enclaves pro aplikace
  na instancích EC2 s Red Hat Enterprise Linux 9.6 a vyššími verzemi.
importance: 3
layout: tech_news_article
original_title: Confidential computing on AWS Nitro Enclave with Red Hat Enterprise
  Linux
publishedAt: '2025-12-01T00:00:00+00:00'
slug: confidential-computing-on-aws-nitro-enclave-with-r
source:
  emoji: 📰
  id: null
  name: Redhat.com
title: Důvěrný výpočet na AWS Nitro Enclave s Red Hat Enterprise Linux
url: https://www.redhat.com/en/blog/deploy-confidential-computing-aws-nitro-enclaves-red-hat-enterprise-linux
urlToImage: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
urlToImageBackup: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
---

## Souhrn
Článek popisuje, jak nasadit důvěrný výpočet na platformě AWS pomocí Nitro Enclaves v kombinaci s Red Hat Enterprise Linux (RHEL) 9.6 a novějšími verzemi. Tato technologie chrání data během jejich aktivního zpracování v paměti před hrozbami jako jsou privilegovaní uživatelé, kompromitovaní hypervizory nebo pokročilý malware. Autor poskytuje praktický návod pro nasazení na EC2 instancích nebo ROSA clusterech.

## Klíčové body
- AWS Nitro Enclaves vytváří Trusted Execution Environment (TEE) s šifrovanou pamětí a přísnou kontrolou přístupu.
- RHEL 9.6+ podporuje hardwareové funkce jako AMD SEV-SNP, Intel TDX a IBM Secure Execution pro šifrované virtuální stroje.
- Systém zjednodušuje konfiguraci pomocí bezpečnostních profilů, nástrojů pro attestation a správy životního cyklu.
- Vyžaduje přístup k AWS Console a nasazený RHEL 9.6+ nebo ROSA.
- Zaměřeno na ochranu dat v cloudu před poskytovatelem, administrátory i systémovým softwarem.

## Podrobnosti
Důvěrný výpočet řeší zranitelnost dat během jejich zpracování v paměti, kde v konvenčních prostředích hrozí útoky od privilegovaných insiderů, kompromitovaných hypervizorů nebo malwaru schopného čtení paměti serveru. AWS Nitro Enclaves, postavené na Nitro architektuře, poskytují hardwarově chráněné TEE, které šifruje paměť a blokuje nepovolený přístup. Tím zajišťují, že ani cloudový poskytovatel, systémoví administrátoři ani software na úrovni systému nemohou data prohlížet nebo měnit.

Red Hat Enterprise Linux hraje klíčovou roli jako vyzrálý operační systém kompatibilní s těmito technologiemi. RHEL integruje podporu pro CPU-level funkce: AMD SEV-SNP pro bezpečné šifrování virtuálních strojů, Intel TDX pro podobnou ochranu na Intel platformách a IBM Secure Execution pro Power architektury. Tyto funkce umožňují vytvářet šifrované virtuální stroje a bezpečné enklávy. RHEL abstrahuje složitost konfigurace – nabízí bezpečnostní profily pro snadné nastavení, nástroje pro attestation (ověření integrity prostředí) a nástroje pro správu životního cyklu enkláv, což usnadňuje nasazení v produkčním prostředí.

Pro praktickou implementaci je nutný přístup k AWS Console, nasazený RHEL 9.6+ na EC2 nebo ROSA (Red Hat OpenShift Service on AWS). Článek předpokládá znalost předchozích materiálů o konceptech, použitích a zdůvodnění důvěrného výpočtu. Hardware Nitro zajišťuje bezpečné spojení a certifikaci. Workloady běžící v TEE zůstávají izolované, což je ideální pro aplikace zpracovávající citlivá data jako zdravotnické záznamy, finanční transakce nebo AI modely trénované na proprietárních datech.

## Proč je to důležité
V éře cloud computingu, kde firmy outsourcovat výpočty na veřejné cloudy, roste potřeba ochrany před riziky na straně poskytovatele. Důvěrný výpočet posiluje důvěru v AWS pro regulované odvětví jako finance, zdravotnictví nebo vláda, kde je attestation klíčová pro compliance (např. GDPR, HIPAA). Integrace s RHEL rozšiřuje použitelnost na enterprise prostředí, kde je stabilita a podpora rozhodující. Pro průmysl to znamená snížení rizik datových úniků během zpracování, což je kritické pro AI aplikace s citlivými daty, kde tradiční šifrování nestačí. Tento přístup nenahrazuje jiné bezpečnostní vrstvy, ale doplňuje je, čímž zvyšuje celkovou odolnost proti pokročilým hrozbám.

---

[Číst původní článek](https://www.redhat.com/en/blog/deploy-confidential-computing-aws-nitro-enclaves-red-hat-enterprise-linux)

**Zdroj:** 📰 Redhat.com
