---
author: Marisa Aigen
category: kryptoměny
companies:
- Solana
- Aptos
date: '2025-12-19 00:05:19'
description: Vývojáři těchto blockchainových platforem začali testovat novou kryptografii,
  která má chránit transakce a peněženky před paděláním v době, kdy kvantové počítače
  představují rostoucí hrozbu.
importance: 4
layout: tech_news_article
original_title: Solana, Aptos Move to Harden Blockchains Against Future Quantum Attacks
publishedAt: '2025-12-19T00:05:19+00:00'
slug: solana-aptos-move-to-harden-blockchains-against-fu
source:
  emoji: 📰
  id: null
  name: Decrypt
title: Solana a Aptos posilují blockchany proti budoucím kvantovým útokům
url: https://decrypt.co/352961/solana-aptos-harden-blockchains-future-quantum-attacks
urlToImage: https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2025/10/google-quantum-decrypt-style-01-2-gID_7.jpg
urlToImageBackup: https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2025/10/google-quantum-decrypt-style-01-2-gID_7.jpg
---

### Souhrn
Vývojáři blockchainů Solana a Aptos spustili testování kryptografických algoritmů odolných vůči kvantovým útokům. Cílem je ochránit digitální peněženky a transakce před budoucími kvantovými počítači, které by mohly rozlousknout současné šifrovací standardy. Tento krok předchází potenciálním ztrátám v hodnotě bilionů dolarů v kryptoměnách.

### Klíčové body
- Solana a Aptos testují post-kvantovou kryptografii na testovacích sítích.
- Zaměření na ochranu podpisů transakcí (ECDSA) a generování klíčů peněženek.
- Použití algoritmů jako Dilithium nebo Falcon, standardizovaných NISTem.
- Aptos využívá programovací jazyk Move pro implementaci změn.
- Solana integruje změny do svého high-throughput protokolu.

### Podrobnosti
Solana je vysoce výkonný blockchain známý svou rychlostí zpracování až 65 000 transakcí za sekundu díky Proof-of-History konsenzu. Aptos, naopak, vychází z jazyka Move původně vyvinutého pro projekt Diem od Facebooku, což umožňuje bezpečnější smart kontrakty s prevencí chyb jako reentrancy útoky. Oba projekty nyní řeší slabinu současné kryptografie: asymetrické algoritmy jako ECDSA nebo EdDSA, používané pro digitální podpisy v blockchainu, jsou zranitelné vůči Shorovu algoritmu na kvantových počítačích. Tento algoritmus dokáže efektivně rozložit velká čísla na faktory, což umožní odvodit soukromé klíče z veřejných.

Vývojáři na Solaně začali s testy na devnetu, kde nahrazují ECDSA post-kvantovými alternativami, jako jsou lattice-based schémata (např. CRYSTALS-Dilithium pro podpisy) nebo hash-based (Falcon). Tyto algoritmy odolávají známým kvantovým útokům, protože spoléhají na matematické problémy jako Learning With Errors (LWE), které kvantové počítače nedokážou efektivně řešit. Aptos jde podobně, s důrazem na Move modul, který umožňuje plynulou migraci bezpečných podpisů do existujících kontraktů. Testy zahrnují simulace útoků, měření výkonu (zvýšení velikosti podpisů o 5-10x oproti ECDSA) a kompatibilitu s existujícími nástroji jako Solana CLI nebo Aptos SDK.

Tento přístup není úplně nový – NIST od roku 2016 standardizuje post-kvantovou kryptografii a v roce 2024 oznámil první sadu algoritmů (ML-KEM, ML-DSA, SLH-DSA). Solana a Aptos tak následují stopy Ethereum, které zvažuje podobné upgrady v rámci Pectra hard forku. Pro uživatele to znamená nutnost budoucí migrace peněženek na nové klíče, aby se vyhnuli "harvest now, decrypt later" útokům, kde útočníci sbírají šifrovaná data pro pozdější dešifrování.

### Proč je to důležité
Kvantové počítače, jako ty od IBM nebo Google s stovkami qubitů, se blíží k praktickým aplikacím – odhaduje se, že 1-2 miliony stabilních qubitů postačí k rozbití 256-bit ECDSA. S tržní kapitalizací kryptoměn přes 3 biliony USD by útok znamenal masivní krádeže a ztrátu důvěry. Tato iniciativa Solany (tržní kap. SOL ~200 mld. USD) a Aptosu posiluje odolnost ekosystému, ovlivňuje DeFi protokoly, NFT a staking. V širším IT kontextu urychluje adopci post-kvantové kryptografie napříč sektory, od bankovnictví po IoT, a nutí projekty jako Bitcoin zvážit podobné kroky. Bez toho hrozí systémová selhání, když kvantové technologie dosáhnou zralosti do 10-15 let.

---

[Číst původní článek](https://decrypt.co/352961/solana-aptos-harden-blockchains-future-quantum-attacks)

**Zdroj:** 📰 Decrypt
