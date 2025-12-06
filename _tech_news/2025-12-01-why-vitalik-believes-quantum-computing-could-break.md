---
author: Marisa Aigen
category: kryptoměny
date: '2025-12-01 16:04:04'
description: Buterin varuje, že kvantové počítače by mohly ohrozit kryptografii Ethereum
  dříve, než se očekává, a načrtává, jak se síť může bezpečně připravit.
importance: 5
layout: tech_news_article
original_title: Why Vitalik believes quantum computing could break Ethereum’s cryptography
  sooner than expected
people:
- Vitalik Buterin
publishedAt: '2025-12-01T16:04:04+00:00'
slug: why-vitalik-believes-quantum-computing-could-break
source:
  emoji: 📰
  id: null
  name: Cointelegraph
title: Proč Vitalik věří, že kvantové počítače by mohly prolomit kryptografii Ethereum
  dříve, než se očekává
url: https://cointelegraph.com/news/why-vitalik-believes-quantum-computing-could-break-ethereum-s-cryptography-sooner-than-expected
urlToImage: https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1200/https://s3.cointelegraph.com/uploads/2025-12/019ada9d-c6d9-7a76-842f-29d0375f8b07
urlToImageBackup: https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1200/https://s3.cointelegraph.com/uploads/2025-12/019ada9d-c6d9-7a76-842f-29d0375f8b07
---

## Souhrn
Spoluzakladatel Ethereum Vitalik Buterin odhaduje 20% šanci, že kvantové počítače prolomí současnou kryptografii do roku 2030, a doporučuje okamžitou přípravu sítě. Hlavní riziko spočívá v algoritmu ECDSA, kde veřejné klíče viditelné na blockchainu umožní budoucím kvantovým počítačům odvodit soukromé klíče. Buterin navrhuje nouzový plán včetně rollbacku bloků, zmrazení externích účtů (EOA) a přechodu na kvantově odolné peněženky na bázi smart kontraktů.

## Klíčové body
- Podle predikční platformy Metaculus je 20% pravděpodobnost kryptograficky relevantního kvantového počítače do 2030, medián kolem 2040.
- ECDSA, základ Ethereum a Bitcoinu, je zranitelné: viditelné veřejné klíče umožní Shorův algoritmus získat soukromý klíč.
- Nouzový plán: rollback bloků, zmrazení EOA, přesun fondů do smart kontraktových peněženek s kvantově odolnými podpisy.
- Doporučení: NIST schválené post-kvantové podpisy a crypto-agile infrastruktura pro snadnou výměnu algoritmů.
- Časový rámec: příprava do čtyř let, riziko před volbami v USA 2028.

## Podrobnosti
Vitalik Buterin v prosinci 2025 na konferenci Devconnect v Buenos Aires kvantifikoval riziko kvantových počítačů, které by pomocí Shorova algoritmu prolomily eliptickou křivkovou kryptografii (ECDSA). Tento algoritmus slouží k digitálním podpisům a generování klíčů v Ethereu, Bitcoinech i většině moderních blockchainů. Problém nastává, když je veřejný klíč exponován na blockchainu – například při transakcích z legacy adres – což umožní kvantovému počítači rychle odvodit soukromý klíč. Data z Etherscanu ukazují přes 350 milionů unikátních adres Ethereum k roku 2025, z čehož mnohé mají exponované klíče.

Buterinův nouzový plán zahrnuje několik kroků: rollback nedávných bloků pro odstranění poškozených transakcí, dočasné zmrazení externích účtů (EOA, Externally Owned Accounts), které jsou standardními uživatelskými adresami ovládanými soukromými klíči, a rychlý přesun prostředků do smart kontraktových peněženek. Tyto peněženky, napsané v Solidity, umožňují multisig schémata nebo sociální obnovu a lze je upgradovat na kvantově odolné algoritmy jako Dilithium nebo Falcon, schválené NIST. Dále navrhuje crypto-agile infrastrukturu, kde lze algoritmy měnit bez narušení sítě, podobně jako u TLS v webových prohlížečích.

Toto není první varování – Metaculus predikce ukazují medián kolem 2040, ale Buterin zdůrazňuje ocasovou rizikovost 2020s. Ethereum má výhodu díky programovatelnosti smart kontraktů, na rozdíl od Bitcoinu, kde změny vyžadují hard fork. Příprava zahrnuje testování post-kvantových podpisů v testnete a postupný rollout. Kriticky: i když 20% není jistota, ignorování by mohlo vést k miliardovým ztrátám, protože kvantové počítače od firem jako IBM nebo Google rychle napredují v qubitové kapacitě.

## Proč je to důležité
Riziko kvantových počítačů ohrožuje nejen Ethereum s tržní kapitalizací přes 300 miliard USD, ale celý kryptoprvok, včetně Bitcoinu a DeFi protokolů. Prolomení ECDSA by umožnilo krádeže z exponovaných adres, což by podkopalo důvěru v decentralizované finance. Ethereum může reagovat rychleji díky upgradovatelným smart kontraktům, ale vyžaduje to koordinaci vývojářů, validátorů a uživatelů. V širším kontextu to urychluje přechod na post-kvantovou kryptografii v celém IT průmyslu, včetně bankovnictví a HTTPS. Buterinovo kvantifikování rizika (20% do 2030) posouvá debatu z sci-fi do reálné roadmapy, což může stimulovat výzkum v kvantově bezpečných protokolech a ovlivnit investice do quantum-resistant technologií.

---

[Číst původní článek](https://cointelegraph.com/news/why-vitalik-believes-quantum-computing-could-break-ethereum-s-cryptography-sooner-than-expected)

**Zdroj:** 📰 Cointelegraph
