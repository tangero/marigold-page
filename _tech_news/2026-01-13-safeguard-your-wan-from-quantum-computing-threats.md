---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Cisco
date: '2026-01-13 16:00:31'
description: Kvantové počítače prolomí současné šifrování veřejným klíčem, což činí
  provoz WAN sítí zvláště zranitelným vůči útokům harvest now, decrypt later (HNDL).
  Nové bezpečné routry řady Cisco 8000 Series umožňují brzkou ochranu proti kvantovým
  hrozbám pomocí post-quantum předem sdílených klíčů.
importance: 5
layout: tech_news_article
original_title: Safeguard Your WAN from Quantum Computing Threats
publishedAt: '2026-01-13T16:00:31+00:00'
slug: safeguard-your-wan-from-quantum-computing-threats
source:
  emoji: 📰
  id: null
  name: Cisco.com
title: Ochrante svou WAN síť před hrozbami kvantových počítačů
url: https://blogs.cisco.com/networking/safeguard-your-wan-from-quantum-computing-threats
urlToImage: https://blogs.cisco.com/gcs/ciscoblogs/1/2026/01/PQC-blog-feature.png
urlToImageBackup: https://blogs.cisco.com/gcs/ciscoblogs/1/2026/01/PQC-blog-feature.png
---

## Souhrn
Kvantové počítače představují reálnou hrozbu pro současné šifrovací metody založené na veřejném klíči, které chrání data přenášená WAN sítěmi. Útoky typu harvest now, decrypt later (HNDL) umožňují útočníkům sbírat šifrovaný provoz nyní a dešifrovat ho později pomocí kryptograficky relevantního kvantového počítače (CRQC). Cisco řada 8000 Series Secure Routers zavádí post-quantum cryptography (PQC) prostřednictvím post-quantum předem sdílených klíčů, což poskytuje okamžitou ochranu pro kritické sítě.

## Klíčové body
- Současné asymetrické šifrování (RSA, ECC) je zranitelné vůči kvantovým algoritmům jako Shor's algorithm.
- HNDL útoky cílí na dlouhodobě citlivá data v WAN, kde útočníci zachytí šifrovaný provoz a veřejné klíče pro budoucí dešifrování.
- WAN sítě spojují datová centra, pobočky a cloud a nesou data s dlouhou životností, což je činí prioritou pro PQC.
- Cisco 8000 Series podporuje IPsec tunely s post-quantum pre-shared keys, kompatibilní s NIST PQC standardy.
- Doporučení: Okamžitý přechod na quantum-safe řešení kvůli blížícímu se vývoji CRQC.

## Podrobnosti
Kvantové počítače mění základy kybernetické bezpečnosti tím, že dokážou efektivně prolomit asymetrické šifrovací algoritmy, na nichž stojí protokoly jako TLS nebo IPsec. Tyto metody spoléhají na obtížnost faktorizace velkých čísel (RSA) nebo diskrétního logaritmu na eliptických křivkách (ECC). Kvantový algoritmus Shor's umožní CRQC – počítači s tisíci stabilních qubitů – odvodit soukromé klíče z veřejných během minut, což je v klasických počítačích nemožné.

HNDL útoky fungují takto: Útočník zachytí šifrovaný WAN provoz, včetně veřejných klíčů z key exchange fází (např. Diffie-Hellman). Data zůstávají šifrovaná symetrickým session key, který je odvozen z asymetrického handshake. Až CRQC získá soukromý klíč, dešifruje session key a přistoupí k obsahu. Pro podniky to znamená, že dnešní přenosy citlivých dat – jako zdravotnické záznamy, finanční transakce nebo průmyslové tajemství – mohou být kompromitovány za 5–10 let, kdy CRQC stanou dostupnými státům nebo velkým aktérům.

WAN sítě jsou klíčové, protože spojují vzdálené lokace a přenášejí data s délkou životnosti desítek let. Cisco, dominantní hráč v síťovém vybavení, řadu 8000 Series Secure Routers navrhuje pro high-end WAN nasazení. Tyto routry podporují modulární architekturu s vysokou propustností (až 400 Gbps na slot) a integrovat PQC do existujících IPsec VPN. Klíčovou funkcí jsou post-quantum pre-shared keys (PQ-PSK), kde se symetrické klíče generují pomocí PQC algoritmů jako Kyber (NIST standardizovaný KEM pro key encapsulation). To obchází potřebu plně post-quantum PKI, která ještě není nasazená, a umožňuje bezpečné tunelování bez změny infrastruktury. Cisco také integruje detekci kvantových hrozeb a podporu hybridních schémat (klasické + PQC). Kriticky: PQC algoritmy prošly NIST výběrem v roce 2022 (Kyber, Dilithium, Falcon), ale plná standardizace probíhá, takže PQ-PSK je praktickým meziřešením.

## Proč je to důležité
Tento vývoj urychluje přechod na quantum-safe kryptografii v podnikových sítích, kde zpoždění může vést k masivním únikům dat a neregulerním pokutám (GDPR, HIPAA). WAN-first strategie je logická, protože tvoří vstupní bránu do celého ekosystému – datových center, cloudu (AWS, Azure) a IoT. V širším kontextu posiluje to globální snahu o migraci PQC, jak doporučuje NSA v CNSA 2.0. Pro uživatele znamená snížení rizika HNDL, zvláště v odvětvích jako finance nebo obrana. Nicméně, plná ochrana vyžaduje end-to-end PQC, včetně klientů a serverů, což Cisco řeší jen částečně – firmy musí auditovat celý stack.

---

[Číst původní článek](https://blogs.cisco.com/networking/safeguard-your-wan-from-quantum-computing-threats)

**Zdroj:** 📰 Cisco.com
