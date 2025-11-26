---
author: Marisa Aigen
category: kryptoměny
date: '2025-11-25 16:05:28'
description: 21. listopadu došlo na hlavní síti Cardano k rozštěpení blockchainu způsobenému
  chybnou transakcí delegování stake, která aktivovala latentní chybu v novější verzi
  uzlového softwaru. Síť byla rozdělena na více než 14 hodin.
importance: 4
layout: tech_news_article
original_title: 'FBI called as Cardano split in two by a single transaction: Lessons
  for ETH and SOL client diversity'
publishedAt: '2025-11-25T16:05:28+00:00'
slug: fbi-called-as-cardano-split-in-two-by-a-single-tra
source:
  emoji: 📰
  id: null
  name: CryptoSlate
title: 'FBI zasahuje po rozštěpení Cardana jedinou transakcí: Ponaučení pro klienty
  Ethereum a Solany'
url: https://cryptoslate.com/cardano-split-in-two-by-a-single-transaction-lessons-for-eth-and-sol-client-diversity/
urlToImage: https://cryptoslate.com/wp-content/uploads/2025/11/cardano-split.jpg
urlToImageBackup: https://cryptoslate.com/wp-content/uploads/2025/11/cardano-split.jpg
---

## Souhrn
21. listopadu došlo na hlavní síti Cardano k vážnému rozštěpení (forku), kdy se síť rozdělila na dvě konkurenční historie bloků. Příčinou byla jediná chybně vytvořená transakce delegování stake, která využila dosud neaktivní chybu v novější verzi uzlového softwaru. Incident trval přibližně 14,5 hodiny a vyvolal zásah federálních orgánů, včetně FBI.

## Klíčové body
- Rozštěpení bylo způsobeno jedinou transakcí s chybnou strukturou delegování stake.
- Chyba byla přítomna pouze v novějších verzích uzlového softwaru Cardano, starší verze ji neobsahovaly.
- Síť se obnovila až po koordinovaném přechodu většiny stake pool operátorů na jednotnou verzi softwaru.
- Incident odhalil rizika nedostatečné diverzity klientů – paradoxně i příliš vysoké sjednocení může být zranitelné.
- Událost má přímé implikace pro jiné blockchainy, zejména Ethereum a Solanu, které se snaží zvýšit diverzitu svých klientů.

## Podrobnosti
Rozštěpení Cardana nebylo způsobeno útokem, ale technickou chybou v implementaci protokolu. Konkrétně šlo o transakci delegování stake, která obsahovala neplatný parametr, jenž byl v novější verzi uzlového softwaru (node software) špatně zpracován. Zatímco starší verze transakci odmítly jako neplatnou, novější verze ji akceptovaly a začaly budovat alternativní řetězec bloků. Výsledkem bylo dočasné rozdělení sítě na dvě paralelní historie, což ohrozilo konsenzus a důvěru v integritu blockchainu.

K řešení došlo až po manuální koordinaci mezi operátory stake poolů, kteří museli přepnout své uzly na jednotnou verzi softwaru. Tento proces trval více než 14 hodin, během nichž byla síť de facto nefunkční pro mnoho aplikací. Zásah FBI naznačuje, že incident byl považován za potenciální hrozbu pro finanční stabilitu nebo za možný pokus o manipulaci s trhem.

## Proč je to důležité
Tento případ ukazuje, že i vyspělé blockchainové sítě nejsou imunní vůči chybám v softwarové implementaci. Zároveň odhaluje paradox diverzity klientů: příliš malá diverzita (např. většina uzlů používá stejný software) zvyšuje riziko systémového selhání při chybě v jedné implementaci. Naopak příliš velká diverzita může komplikovat koordinaci při opravách. Ethereum a Solana, které aktivně podporují vývoj více nezávislých klientů (např. Geth, Nethermind pro ETH; Agave, Jito pro SOL), mají z tohoto incidentu jasnou výstrahu – diverzita musí být vyvážená a doprovázena robustními testovacími a koordinačními mechanismy. Pro uživatele a vývojáře to znamená, že bezpečnost blockchainu není jen otázkou kryptografie, ale i kvality softwarového inženýrství a komunitní spolupráce.

---

[Číst původní článek](https://cryptoslate.com/cardano-split-in-two-by-a-single-transaction-lessons-for-eth-and-sol-client-diversity/)

**Zdroj:** 📰 CryptoSlate
