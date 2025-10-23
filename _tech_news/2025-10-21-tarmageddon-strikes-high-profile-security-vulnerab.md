---
category: kybernetická bezpečn
companies:
- Nemám k dispozici celý text článku
- 'pouze nadpis a popis. Z poskytnutých informací nelze identifikovat žádné konkrétní
  technologické firmy.


  žádné'
date: '2025-10-21 14:38:00'
description: Bezpečnostní výzkumníci odhalili závažnou zranitelnost CVE-2025-62518
  v knihovně async-tar pro jazyk Rust, která postihuje správce balíčků uv a další
  projekty. Chyba umožňuje vzdálené spuštění kódu přes přepsání souborů.
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

Bezpečnostní firma Edera zveřejnila kritickou zranitelnost s označením CVE-2025-62518, známou jako TARmageddon, která postihuje populární knihovnu async-tar pro programovací jazyk Rust a její odnože včetně tokio-tar. Chyba umožňuje útočníkům vzdálené spuštění kódu prostřednictvím přepsání souborů, což představuje vážné bezpečnostní riziko pro projekty jako správce balíčků uv pro Python a další nástroje využívající tyto knihovny.

## Klíčové body

- Zranitelnost TARmageddon (CVE-2025-62518) postihuje knihovnu async-tar a její odnože jako tokio-tar, které slouží ke zpracování TAR archivů v asynchronním Rust kódu
- Chyba je klasifikována jako vysoká závažnost a umožňuje vzdálené spuštění kódu (RCE) prostřednictvím útoků přepisujících soubory
- Problém se týká kritické chyby při parsování hranic v archivech, což dokazuje, že ani Rust s jeho zárukami paměťové bezpečnosti není imunní vůči všem typům zranitelností
- Knihovna tokio-tar je fakticky opuštěná bez aktivní údržby, což komplikuje řešení problému
- Edera koordinovala decentralizované záplatování klíčových projektů včetně Binstalk, opa-wasm a dalších

## Podrobnosti

Zranitelnost TARmageddon představuje významný bezpečnostní incident v ekosystému jazyka Rust, který je běžně prezentován jako bezpečnější alternativa k jazykům jako C nebo C++ díky svým zárukami paměťové bezpečnosti. Tato chyba však ukazuje, že paměťová bezpečnost není všelék - problém spočívá v logické chybě při parsování hranic v TAR archivech, nikoli v klasických paměťových chybách jako buffer overflow.

Knihovny async-tar a tokio-tar slouží ke zpracování TAR archivů v asynchronním Rust kódu, což je běžný požadavek v moderních aplikacích pracujících s komprimovanými soubory. Tyto knihovny používá řada významných projektů, včetně správce balíčků uv pro Python, který získal v poslední době značnou popularitu jako rychlejší alternativa k pip.

Situaci komplikuje fakt, že tokio-tar, jedna z nejpoužívanějších odnožích, je prakticky opuštěná bez aktivní údržby. To znamená, že neexistuje centrální místo, kde by mohla být chyba opravena pro všechny uživatele. Bezpečnostní firma Edera proto zvolila netradiční přístup decentralizovaného záplatování, kdy koordinovala opravu přímo s vývojáři klíčových downstream projektů jako Binstalk (nástroj pro instalaci binárních souborů) a opa-wasm (WebAssembly runtime pro Open Policy Agent).

Útok využívající TARmageddon může útočníkovi umožnit přepsat libovolné soubory v systému při rozbalování speciálně připraveného TAR archivu, což může vést ke spuštění škodlivého kódu s právy aplikace provádějící rozbalení.

## Proč je to důležité

Tato zranitelnost má několik významných dopadů na technologický ekosystém. Především zpochybňuje představu, že přechod na Rust automaticky řeší všechny bezpečnostní problémy - zatímco jazyk skutečně eliminuje celé třídy paměťových chyb, logické chyby v kódu zůstávají problémem. Pro vývojáře to znamená, že i při použití moderních bezpečných jazyků je nutné provádět důkladné bezpečnostní audity.

Dále případ ukazuje na problém opuštěných knihoven v open-source ekosystému. Tokio-tar byla široce používaná knihovna, ale bez aktivní údržby se stala bezpečnostním rizikem pro všechny závislé projekty. To vyvolává otázky o dlouhodobé udržitelnosti open-source infrastruktury.

Pro uživatele nástrojů jako uv je důležité co nejdříve aktualizovat na opravené verze, protože zranitelnost může být zneužita při instalaci balíčků ze škodlivých zdrojů. Organizace používající postižené knihovny by měly provést audit svých závislostí a aplikovat dostupné záplaty.

---

[Číst původní článek](https://www.phoronix.com/news/Rust-TARmageddon)

**Zdroj:** 📰 Phoronix
