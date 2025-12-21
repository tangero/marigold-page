---
author: Marisa Aigen
category: kryptoměny
date: '2025-12-20 12:02:00'
description: Tvrdby, že kvantové počítání zničí Bitcoin, mohou být přehnané, ale Bitcoin
  bude muset být upraven, aby odolal této hrozbě.
importance: 5
layout: tech_news_article
original_title: Will Quantum Computing Kill Bitcoin?
publishedAt: '2025-12-20T12:02:00+00:00'
slug: will-quantum-computing-kill-bitcoin
source:
  emoji: 📰
  id: null
  name: ComputerWeekly.com
title: Zabije kvantové počítání Bitcoin?
url: https://www.computerweekly.com/opinion/Will-Quantum-Computing-Kill-Bitcoin
urlToImage: https://www.computerweekly.com/visuals/German/article/quantum-computing-2-adobe.jpg
urlToImageBackup: https://www.computerweekly.com/visuals/German/article/quantum-computing-2-adobe.jpg
---

### Souhrn
Kvantové počítače by teoreticky mohly prolomit kryptografické mechanismy Bitcoinu pomocí algoritmu Shor, což ohrožuje bezpečnost peněženek. Autor článku, Eli Ben-Sasson z StarkWare, argumentuje, že riziko je omezené a Bitcoin se dokáže přizpůsobit, aniž by došlo k úplnému kolapsu sítě. Evoluce protokolu je již v plánu.

### Klíčové body
- Kvantové počítače mohou prolomit eliptické křivky (ECDSA) v Bitcoinu, ale pouze u adres s veřejně známými veřejnými klíči.
- Nelze přepsat blockchain, falšovat mince ani ovládnout konsenzus sítě.
- Bitcoin prošel dříve významnými upgrady a připravuje se na kvantově odolnou kryptografii.
- StarkWare, firma zaměřená na škálovatelnost blockchainu pomocí zero-knowledge důkazů, podporuje adaptaci.
- Diskuse s experty jako Scott Aaronson ukazuje, že panika je předčasná.

### Podrobnosti
Eli Ben-Sasson, spoluzakladatel a generální ředitel StarkWare – společnosti specializující se na technologie zero-knowledge proofs pro zlepšení škálovatelnosti blockchainových sítí –, analyzuje dlouhodobou debatu o dopadu kvantového počítání na Bitcoin. Bitcoin spoléhá na kryptografické předpoklady založené na eliptických křivkách (elliptic-curve cryptography, ECC), konkrétně na algoritmu ECDSA pro digitální podpisy. Kvantový počítač s dostatečným počtem stabilních qubitů by mohl spustit Shorovův algoritmus, který efektivně faktorizuje velká čísla a diskrétní logaritmy, čímž by odhalil soukromé klíče z veřejných.

Toto riziko je však specifické: postihuje pouze adresy, kde byl veřejný klíč odhalen, například při transakcích. Adresy s neodhalenými veřejnými klíči (pay-to-public-key-hash, P2PKH) zůstávají bezpečné, dokud nejsou použity. Kvantové počítače nemohou měnit transakce v blockchainu, protože ten je decentralizovaný a chráněný konsenzem proof-of-work. Nemohou ani vytvářet mince z ničeho, protože to vyžaduje platné podpisy a schválení sítě.

Současné kvantové počítače, jako ty od IBM nebo Google, mají stovky qubitů, ale trpí vysokou chybovostí a krátkou kohärenční dobou. Cesta k „quantum advantage“ pro Shorův algoritmus vyžaduje miliony logických qubitů, což je vzdálené o desetiletí. Bitcoin není statický: v minulosti přijal SegWit pro lepší škálovatelnost a Taproot pro lepší soukromí. Příští upgrady mohou integrovat post-kvantovou kryptografii, jako lattice-based schémata (např. Kyber nebo Dilithium z NIST standardů), které odolávají kvantovým útokům. StarkWare přispívá svými STARK proofs, které umožňují ověřitelnost bez odhalení dat, což je klíčové pro kvantově bezpečné transakce.

Ben-Sasson diskutoval s výzkumníky jako Scott Aaronson, expertem na kvantové výpočty z University of Texas, který potvrzuje, že hrozba je reálná, ale ne okamžitá. Panika je neopodstatněná, protože kryptoměnový ekosystém sleduje vývoj a připravuje migrační plány.

### Proč je to důležité
Tento článek podtrhuje nutnost přechodu na post-kvantovou kryptografii v celém IT průmyslu, nejen v kryptoměnách. Bitcoin s tržní kapitalizací přes bilion dolarů ovlivňuje globální finance; jeho kolaps by způsobil domino efekt na DeFi, NFT a další blockchainy. Pro uživatele znamená doporučení: nepřesouvat prostředky do starých P2PK adres a sledovat upgrady jako soft forks. V širším kontextu urychluje tlak na NIST standardy a investice do kvantově odolných systémů, což posílí celkovou kyberbezpečnost. Adaptace Bitcoinu ukáže, jak se technologie vyvíjejí v reakci na nové hrozby, podobně jako přechod z SHA-1 na SHA-256.

---

[Číst původní článek](https://www.computerweekly.com/opinion/Will-Quantum-Computing-Kill-Bitcoin)

**Zdroj:** 📰 ComputerWeekly.com
