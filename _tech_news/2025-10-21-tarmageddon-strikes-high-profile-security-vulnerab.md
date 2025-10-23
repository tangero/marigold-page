---
category: kybernetická bezpečn
date: '2025-10-21 14:38:00'
description: Bezpečnostní výzkumníci odhalili závažnou zranitelnost CVE-2025-62518
  v knihovně async-tar pro Rust, která umožňuje vzdálené spuštění kódu. Problém postihuje
  i správce balíčků uv pro Python.
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
title: 'TARmageddon: Kritická bezpečnostní chyba v populární knihovně pro Rust'
url: https://www.phoronix.com/news/Rust-TARmageddon
urlToImage: https://www.phoronix.net/image.php?id=2025&image=tarmageddon
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=tarmageddon
---

## Souhrn

Bezpečnostní společnost Edera zveřejnila kritickou zranitelnost s označením CVE-2025-62518, známou jako TARmageddon, která postihuje populární knihovnu async-tar pro programovací jazyk Rust a její odnože včetně tokio-tar. Chyba umožňuje vzdálené spuštění kódu prostřednictvím přepisování souborů, což představuje vážné bezpečnostní riziko pro projekty jako správce balíčků uv pro Python a další nástroje využívající tyto knihovny.

## Klíčové body

- Zranitelnost CVE-2025-62518 postihuje knihovnu async-tar a její fork tokio-tar, které slouží k práci s TAR archivy v asynchronním kódu
- Chyba je klasifikována jako vysoké riziko a umožňuje vzdálené spuštění kódu (RCE) přes útoky přepisováním souborů
- Problém se týká i kódu psaného v Rustu, který je běžně propagován pro své záruky paměťové bezpečnosti
- Knihovna tokio-tar je fakticky opuštěná bez aktivní údržby, což komplikuje opravu
- Edera koordinovala decentralizované záplatování klíčových projektů včetně Binstalk a opa-wasm

## Podrobnosti

TARmageddon představuje kritickou chybu v parsování hranic v knihovně async-tar, která je široce používána v ekosystému Rustu pro asynchronní práci s TAR archivy. Tyto knihovny umožňují vývojářům efektivně rozbalovat a vytvářet TAR soubory bez blokování hlavního vlákna aplikace, což je klíčové pro výkonné síťové aplikace a nástroje.

Zranitelnost spočívá v nesprávném zpracování hraničních případů při parsování TAR archivů, což útočníkům umožňuje vytvořit speciálně upravené archivy, které při rozbalení přepíší libovolné soubory v systému. To může vést ke vzdálenému spuštění kódu, pokud útočník přepíše kritické systémové soubory nebo spustitelné programy.

Zajímavým aspektem této zranitelnosti je, že postihuje kód napsaný v Rustu, programovacím jazyce, který je intenzivně propagován právě pro své záruky paměťové bezpečnosti. TARmageddon však ukazuje, že i Rust nemůže zabránit logickým chybám v kódu, které mohou mít stejně závažné bezpečnostní dopady jako klasické paměťové chyby v jazycích jako C nebo C++.

Situaci komplikuje fakt, že tokio-tar, jeden z hlavních forků async-tar, je prakticky opuštěný projekt bez aktivní údržby. To znamená, že neexistuje centrální místo, kde by byla chyba opravena a záplata distribuována všem uživatelům. Společnost Edera proto musela koordinovat decentralizované záplatování s jednotlivými projekty, které knihovnu používají.

Mezi postiženými projekty je i uv, moderní správce balíčků pro Python, který si získal popularitu díky své rychlosti a je napsán právě v Rustu. Další postižené projekty zahrnují Binstalk, nástroj pro instalaci předkompilovaných binárních souborů, a opa-wasm, implementaci Open Policy Agent pro WebAssembly.

## Proč je to důležité

TARmageddon je významnou připomínkou, že bezpečnost softwaru nezávisí pouze na výběru programovacího jazyka. I když Rust poskytuje silné záruky proti paměťovým chybám, logické chyby v kódu mohou být stejně nebezpečné. Tento incident také upozorňuje na problém opuštěných open-source projektů, které jsou stále široce používány, ale nemají aktivní údržbu. V ekosystému Rustu, kde je běžné spoléhat se na velké množství malých knihoven, může absence údržby jedné komponenty ohrozit bezpečnost mnoha navazujících projektů. Organizace by měly pečlivě auditovat své závislosti a mít připravené plány pro situace, kdy klíčová knihovna přestane být udržována.

---

[Číst původní článek](https://www.phoronix.com/news/Rust-TARmageddon)

**Zdroj:** 📰 Phoronix
