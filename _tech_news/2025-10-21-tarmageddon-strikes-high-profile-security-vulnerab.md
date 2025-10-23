---
category: kybernetická bezpečn
companies:
- Nemám k dispozici celý text článku
- 'pouze nadpis a popis. Z poskytnutých informací nelze identifikovat žádné konkrétní
  technologické firmy.


  žádné'
date: '2025-10-21 14:38:00'
description: Bezpečnostní zranitelnost CVE-2025-62518 v knihovně async-tar a jejích
  odvozeninách jako tokio-tar ohrožuje projekty včetně správce balíčků uv pro Python.
  Chyba umožňuje vzdálené spuštění kódu přes přepisování souborů.
importance: 4
layout: tech_news_article
original_title: 'TARmageddon Strikes: High Profile Security Vulnerability In Popular
  Rust Library - Phoronix'
publishedAt: '2025-10-21T14:38:00+00:00'
slug: tarmageddon-strikes-high-profile-security-vulnerab
source:
  emoji: 📰
  id: null
  name: Phoronix
title: 'TARmageddon: Kritická bezpečnostní chyba v populární Rust knihovně umožňuje
  vzdálené spuštění kódu'
url: https://www.phoronix.com/news/Rust-TARmageddon
urlToImage: https://www.phoronix.net/image.php?id=2025&image=tarmageddon
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=tarmageddon
---

## Souhrn

Bezpečnostní výzkumníci ze společnosti Edera odhalili kritickou zranitelnost s označením CVE-2025-62518, nazvanou TARmageddon, která postihuje populární Rust knihovnu async-tar a její odvozeniny včetně tokio-tar. Chyba v parsování hranic umožňuje útočníkům vzdálené spuštění kódu prostřednictvím přepisování souborů, což má dopad na řadu projektů včetně správce balíčků uv pro Python.

## Klíčové body

- Zranitelnost CVE-2025-62518 postihuje async-tar a její forky jako tokio-tar, které jsou používány v mnoha projektech
- Chyba je klasifikována jako vysoké závažnosti a umožňuje vzdálené spuštění kódu (RCE) přes útoky přepisováním souborů
- Problém se vyskytl navzdory tomu, že kód je napsán v Rustu, který je propagován pro své záruky paměťové bezpečnosti
- Knihovna tokio-tar je fakticky opuštěná bez aktivní údržby
- Edera koordinovala decentralizované záplatování klíčových downstream forků s projekty jako Binstalk a opa-wasm

## Podrobnosti

Zranitelnost TARmageddon představuje významný bezpečnostní problém v ekosystému Rustu. Jedná se o chybu v parsování hranic v knihovně async-tar, která slouží k asynchronnímu zpracování TAR archivů. Tato knihovna a její forky jsou široce používány v různých projektech, což zvyšuje rozsah dopadu.

Zvláště problematická je situace kolem tokio-tar, což je fork async-tar integrovaný s populárním asynchronním runtime frameworkem Tokio. Tato knihovna je fakticky opuštěná bez aktivní upstream údržby, což komplikuje řešení zranitelnosti standardním způsobem prostřednictvím aktualizace od původních vývojářů.

Společnost Edera, která zranitelnost objevila, musela zvolit netradiční přístup a koordinovat decentralizované záplatování přímo s projekty, které tyto knihovny používají. Mezi klíčové projekty, se kterými Edera spolupracovala, patří Binstalk (nástroj pro instalaci binárních souborů z různých zdrojů) a opa-wasm (WebAssembly runtime pro Open Policy Agent).

Dopad na správce balíčků uv pro Python je obzvláště významný, protože uv se rychle stává populární alternativou k tradičním nástrojům jako pip. Uživatelé těchto nástrojů by měli co nejdříve aktualizovat na opravené verze.

## Proč je to důležité

Tato zranitelnost je významná ze dvou hlavních důvodů. Za prvé, vyvrací běžnou představu, že kód napsaný v Rustu je automaticky bezpečný. Zatímco Rust skutečně poskytuje silné záruky paměťové bezpečnosti, které eliminují celé třídy zranitelností jako buffer overflow, nezabraňuje logickým chybám v kódu. TARmageddon je příkladem toho, že i v Rustu mohou vzniknout kritické bezpečnostní problémy.

Za druhé, případ ukazuje na širší problém v open source ekosystému - opuštěné projekty, které jsou stále široce používány. Tokio-tar není udržován, ale zůstává závislostí mnoha aktivních projektů. To vytváří bezpečnostní riziko a komplikuje proces záplatování. Decentralizovaný přístup Edery, kdy museli koordinovat opravy přímo s downstream projekty, je sice funkční, ale není škálovatelný pro budoucí zranitelnosti.

Pro vývojáře a organizace používající Rust je to připomínka, že je nutné pravidelně auditovat závislosti a mít plán pro situace, kdy upstream projekt přestane být udržován.

---

[Číst původní článek](https://www.phoronix.com/news/Rust-TARmageddon)

**Zdroj:** 📰 Phoronix
