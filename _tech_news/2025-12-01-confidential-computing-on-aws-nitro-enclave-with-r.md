---
author: Marisa Aigen
category: konfidenciální výpoč
companies:
- AWS
- Red Hat
date: '2025-12-01 00:00:00'
description: Článek popisuje, jak implementovat bezpečné prostředí pro zpracování
  citlivých dat v paměti pomocí AWS Nitro Enclaves na instancích EC2 s Red Hat Enterprise
  Linux 9.6 a vyšší. Zaměřuje se na ochranu dat před hrozbami jako jsou privilegovaní
  útočníci nebo poškozené hypervizory.
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
title: Konfidenciální výpočty na AWS Nitro Enclave s Red Hat Enterprise Linux
url: https://www.redhat.com/en/blog/deploy-confidential-computing-aws-nitro-enclaves-red-hat-enterprise-linux
urlToImage: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
urlToImageBackup: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
---

## Souhrn
Článek vysvětluje principy konfidenciálních výpočtů, které chrání data během jejich aktivního zpracování v paměti pomocí hardwarově chráněného prostředí Trusted Execution Environment (TEE). Demonstruje implementaci na platformě AWS Nitro Enclaves pro instance EC2 s operačním systémem Red Hat Enterprise Linux (RHEL) 9.6 a vyšší. Tento přístup řeší zranitelnosti tradičních prostředí, kde jsou data v paměti vystavena rizikům.

## Klíčové body
- AWS Nitro Enclaves poskytují hardwarovou izolaci paměti pro workloads na EC2 instancích.
- RHEL 9.6+ integruje podporu pro technologie jako AMD SEV-SNP, Intel TDX a IBM Secure Execution.
- Prostředí chrání data před cloudovými provozovateli, administrátory a systémovým softwarem.
- Vyžaduje přístup k AWS Console a nasazení RHEL nebo ROSA.
- RHEL zjednodušuje konfiguraci pomocí bezpečnostních profilů a nástrojů pro attestation.

## Podrobnosti
Konfidenciální výpočty se zaměřují na ochranu dat v fázi, kdy jsou aktivně zpracovávána v operační paměti, což je tradičně nejslabší článek řetězce bezpečnosti. V konvenčních prostředích mohou data uniknout privilegovaným uživatelům, poškozeným hypervizorům nebo pokročilému malwaru schopnému číst obsah paměti serveru. AWS Nitro Enclaves tento problém řeší vytvořením izolovaného prostředí uvnitř TEE, kde je paměť šifrována a přístup striktně omezen.

Hardwarová základna spočívá v architektuře AWS Nitro, která zajišťuje bezpečné spojení a certifikaci. Pro praktickou implementaci je nutný přístup k AWS Console a nasazení RHEL 9.6 nebo vyšší na EC2 instancích, případně na clusteru ROSA (Red Hat OpenShift Service on AWS). RHEL hraje klíčovou roli díky své podpoře moderních CPU funkcí: AMD SEV-SNP pro šifrované virtuální stroje, Intel TDX pro podobnou ochranu a IBM Secure Execution pro enclaves. Tyto technologie umožňují spouštět workloads v šifrovaném stavu, kde ani provozovatel cloudu nemůže data prohlížet nebo upravovat.

RHEL abstrahuje složitost konfigurace prostřednictvím bezpečnostních profilů, nástrojů pro attestation (ověření integrity) a řízení životního cyklu. Například attestation slouží k důkazům, že enclave běží v autentickém stavu bez tamperingu. Pro nasazení je třeba připravit EC2 instanci s podporovaným hardwarem, nainstalovat RHEL, nakonfigurovat Nitro Enclaves a spustit aplikace uvnitř izolovaného prostředí. Článek předpokládá znalost předchozích materiálů o konfidenciálních výpočtech pro lepší pochopení use cases, jako je zpracování citlivých zdravotních dat nebo finančních transakcí.

## Proč je to důležité
V éře rostoucích hrozeb v cloudu, kde se data zpracovávají na sdílené infrastruktuře, konfidenciální výpočty zvyšují důvěru v cloudové služby tím, že omezují viditelnost dat i pro poskytovatele. Pro firmy to znamená snížení rizik úniků a lepší shoda s regulacemi jako GDPR nebo HIPAA. AWS a Red Hat tak posilují pozici v segmentu enterprise bezpečnosti, kde RHEL zajišťuje stabilní podporu pro produkční nasazení. Nicméně implementace vyžaduje odborné znalosti a kompatibilní hardware, což omezuje přístupnost na velké organizace. V širším kontextu to přispívá k vývoji TEE technologií, které se stávají standardem proti pokročilým persistentním hrozbám.

---

[Číst původní článek](https://www.redhat.com/en/blog/deploy-confidential-computing-aws-nitro-enclaves-red-hat-enterprise-linux)

**Zdroj:** 📰 Redhat.com
