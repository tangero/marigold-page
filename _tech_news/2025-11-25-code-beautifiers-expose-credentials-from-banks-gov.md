---
author: Marisa Aigen
category: kybernetická bezpečn
date: '2025-11-25 12:01:20'
description: Tisíce přihlašovacích údajů, autentizačních klíčů a konfiguračních dat
  citlivých organizací se ocitly veřejně dostupné v JSON snipcích nahrávaných do online
  nástrojů JSONFormatter a CodeBeautify.
importance: 4
layout: tech_news_article
original_title: Code beautifiers expose credentials from banks, govt, tech orgs
publishedAt: '2025-11-25T12:01:20+00:00'
slug: code-beautifiers-expose-credentials-from-banks-gov
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Nástroje pro formátování kódu vystavily citlivé přihlašovací údaje bank, státních
  institucí a technologických firem
url: https://www.bleepingcomputer.com/news/security/code-beautifiers-expose-credentials-from-banks-govt-tech-orgs/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/04/16/2.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/04/16/2.jpg
---

## Souhrn
Bezpečnostní výzkumníci odhalili, že online nástroje pro formátování kódu JSONFormatter a CodeBeautify nechránily uživatelské „uložené“ snipy, což vedlo k úniku více než 80 000 citlivých fragmentů kódu obsahujících přihlašovací údaje, API klíče a další tajné informace z bank, státních úřadů, zdravotnictví i kritické infrastruktury.

## Klíčové body
- Nástroje JSONFormatter a CodeBeautify umožňují uživatelům „uložit“ kód pro dočasné sdílení, ale vytvořené stránky s nedávnými odkazy (Recent Links) jsou veřejně přístupné bez autentizace.
- Výzkumníci společnosti WatchTowr, specializující se na správu externí útočné plochy, shromáždili přes 5 GB dat z těchto veřejných stránek.
- Mezi uniklými daty jsou Active Directory přihlašovací údaje, cloudové a databázové klíče, soukromé kryptografické klíče, tokeny pro CI/CD systémy, platební brány i záznamy SSH relací.
- URL adresy Recent Links stránek jsou predikovatelné, což umožňuje snadné prohledávání celého archivu pomocí jednoduchého crawleru.

## Podrobnosti
Online služby jako JSONFormatter a CodeBeautify slouží vývojářům k přehlednému formátování a ladění JSON dat. Když uživatel stiskne tlačítko „uložit“, platforma vygeneruje jedinečnou URL a přidá ji na veřejnou stránku „Recent Links“, která není nijak chráněna heslem ani autentizací. Tato stránka je přístupná komukoli, kdo zná její adresu – a protože formát URL je systematický (např. /recent/12345), lze celý archiv prohledat automaticky. Společnost WatchTowr tak získala data z pěti let provozu JSONFormatteru a jednoho roku CodeBeautify, včetně citlivých údajů z organizací v sektorech jako bankovnictví, vládní správa, letecký průmysl či zdravotnictví. Mnoho z těchto údajů bylo aktivních – tedy okamžitě zneužitelných k neoprávněnému přístupu do interních systémů.

## Proč je to důležité
Tento případ ukazuje, jak i zdánlivě neškodné vývojářské nástroje mohou způsobit závažné bezpečnostní incidenty, pokud nejsou správně navrženy. Ukládání citlivých dat do veřejně přístupných služeb bez šifrování nebo expirace je běžnou chybou, ale zde byl problém zhoršen tím, že samotná archivace byla veřejná a prohledatelná. Pro organizace to znamená nutnost lepší vnitřní kontroly používání externích nástrojů a zavedení politik pro správu tajných údajů (secrets management). Pro vývojáře je to varování: i dočasné sdílení kódu může vést k trvalému úniku, pokud není služba řádně zabezpečena.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/code-beautifiers-expose-credentials-from-banks-govt-tech-orgs/)

**Zdroj:** 📰 BleepingComputer
