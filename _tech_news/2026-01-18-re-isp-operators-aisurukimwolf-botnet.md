---
author: Marisa Aigen
category: kybernetika
date: '2026-01-18 01:42:30'
description: Diskuse na mailing listu NANOG odhaluje problémy internetových poskytovatelů
  s botnetem AISURU/Kimwolf, který infikuje zařízení pro nelegální TV vysílání a způsobuje
  přetížení sítí. Experti navrhují publikovat článek v New York Times, ale pochybují
  o dopadu na obyčejné uživatele.
importance: 4
layout: tech_news_article
original_title: 'Re: ISP Operators AISURU/Kimwolf botnet'
people:
- Mel Beckman
- David Pogue
publishedAt: '2026-01-18T01:42:30+00:00'
slug: re-isp-operators-aisurukimwolf-botnet
source:
  emoji: 📰
  id: null
  name: Seclists.org
title: Operátoři ISP a botnet AISURU/Kimwolf
url: https://seclists.org/nanog/2026/Jan/77
urlToImage: https://seclists.org/images/nanog-img.png
urlToImageBackup: https://seclists.org/images/nanog-img.png
---

### Souhrn
Diskuse na mailing listu NANOG mezi odborníky na sítě ukazuje, jak botnet AISURU/Kimwolf ohrožuje operátory internetových služeb (ISP). Tento botnet infikuje levná zařízení pro nelegální přístup k televiznímu obsahu, což vede k masivnímu přenosu dat a přetížení připojení až na 1 Gbps. Účastníci debaty, včetně Mela Beckmana, navrhují napsat článek pro širokou veřejnost, ale upozorňují na nízkou pravděpodobnost, že postižení uživatelé informace přijmou.

### Klíčové body
- Botnet AISURU/Kimwolf se šíří přes spotřebitelská zařízení jako TV piracy boxy, které uživatelé nakupují pro zdarma sportovní přenosy a kabelové kanály.
- Infikovaná zařízení generují obrovský provoz, který saturuje domácí připojení a sítě ISP.
- Uživatelé v sociálních skupinách ignorují varování a deaktivují bezpečnostní služby ISP, jako Comcast XFi Security nebo AT&T Active Armor.
- Odborníci odkazují na článek Briana Krebsa s fotografiemi infikovaných zařízení pro lepší povědomí.
- Navrženo publikovat v New York Times přes Davida Poguea, ale není to úkol pro ISP.

### Podrobnosti
Mailing list NANOG, určený pro operátory sítí a internetové specialisty, se stal místem debaty o botnetu AISURU/Kimwolf. Tento botnet, pojmenovaný podle variant, ovládá tisíce zařízení připojených k internetu, především levných Android-based TV boxů prodávaných pro nelegální streamování obsahu. Tyto boxy, často označované jako "pirate boxes", umožňují uživatelům sledovat placené sportovní přenosy nebo kabelové kanály bez předplatného, ale za cenu bezpečnostních chyb.

Podle Tima Burkea z Mid.net tyto zařízení způsobují, že 1Gbps připojení se stává zdrojem botnetového provozu. Uživatelé, často bez IT znalostí, se připojují k sociálním skupinám věnovaným těmto zařízením, kde sdílejí tipy. Když bezpečnostní služby ISP, jako Comcast XFi Security (která monitoruje síťový provoz a blokuje hrozby) nebo AT&T Active Armor (podobná služba s detekcí malware), upozorní na podezřelou aktivitu, reakce je typicky odmítavá. Lidé deaktivují tyto funkce s tvrzením, že ISP je "nutí kupovat kabelové předplatné". Burke popisuje to jako syndrom Stockholmského, kdy uživatelé brání svým útočníkům.

Mel Beckman, bývalý kolega Davida Poguea z Macworld magazine, souhlasí a navrhuje napsat článek pro sekci technologie New York Times. Odkazuje na článek Briana Krebsa, který obsahuje fotografie reálných zařízení – od IPTV boxů po chytré TV – což by podle něj pomohlo uživatelům rozpoznat své vlastní hardware. Roland Dobbins původně spustil debatu odkazem na Krebsův materiál. Beckmann však uznává, že publikace v mainstreamových médiích není úkol pro ISP, protože ti nemají vliv na novináře.

Botnet funguje tak, že malware ovládne zařízení a využívá ho k distribuci spamu, DDoS útokům nebo těžbě kryptoměn. Pro ISP to znamená nejen přetížení routerů a linků, ale i riziko blacklistingů IP adres, což ovlivňuje nevinné zákazníky. Bezpečnostní služby ISP slouží k detekci anomálií v síťovém provozu, blokaci známých malware podpisů a ochraně proti phishingu, ale jejich efektivita závisí na uživatelské spolupráci.

### Proč je to důležité
Tato debata odhaluje systémový problém v kyberbezpečnosti: slabá zabezpečení IoT zařízení kombinovaná s nelegálním použitím vede k šíření botnetů, které ohrožují celé sítě. Pro ISP to znamená vyšší náklady na údržbu a mitigaci, pro uživatele riziko kompromitace osobních dat a pro průmysl potřebu lepšího vzdělávání. V širším kontextu ukazuje, jak pirátství podněcuje malware ekosystém – bez řešení na straně výrobců levných boxů (často z Číny) a lepšího prosazování zákonů bude problém persistovat. Experti jako ti na NANOG zdůrazňují nutnost kombinace technických opatření a veřejné kampaně, aby se přerušil cyklus ignorace.

---

[Číst původní článek](https://seclists.org/nanog/2026/Jan/77)

**Zdroj:** 📰 Seclists.org
