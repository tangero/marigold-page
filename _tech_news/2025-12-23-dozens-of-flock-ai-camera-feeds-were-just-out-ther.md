---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Flock
date: '2025-12-23 16:09:58'
description: Živé přenosy z více než 60 AI kamer firmy Flock pro dohled byly dostupné
  na webu bez autentizace, což umožnilo kdokoli s odkazem sledovat lidi a vozidla
  v reálném čase. Chybu odhalili youtuber Benn Jordan a 404 Media přes vyhledávač
  Shodan.
importance: 4
layout: tech_news_article
original_title: Dozens of Flock AI camera feeds were just out there
publishedAt: '2025-12-23T16:09:58+00:00'
slug: dozens-of-flock-ai-camera-feeds-were-just-out-ther
source:
  emoji: ⚡
  id: the-verge
  name: The Verge
title: Desítky živých přenosů z AI kamer Flock byly volně dostupné na internetu
url: https://www.theverge.com/news/849624/flock-ai-camera-feeds-exposed-benn-jordan
urlToImage: https://platform.theverge.com/wp-content/uploads/sites/2/2025/12/STK471_Government_Surveillance_CVirginia_C.jpg?quality=90&strip=all&crop=0%2C10.732984293194%2C100%2C78.534031413613&w=1200
urlToImageBackup: https://platform.theverge.com/wp-content/uploads/sites/2/2025/12/STK471_Government_Surveillance_CVirginia_C.jpg?quality=90&strip=all&crop=0%2C10.732984293194%2C100%2C78.534031413613&w=1200
---

## Souhrn
Živé přenosy z přes 60 kamer Condor od firmy Flock, které využívají umělou inteligenci k automatickému sledování lidí a vozidel, byly exponované na internetu bez jakýchkoli přihlašovacích údajů. Kdo měl odkaz, mohl volně sledovat intimní momenty jako odchody z domů v New Yorku nebo hádky na ulici v Atlantě. Tato chyba konfigurace ohrožuje soukromí v systému, který spolupracuje s policií a firmami po celých USA.

## Klíčové body
- Exponované livestreamy z kamer Condor, které automaticky rotují, naklánějí a zoomují díky AI na lidi a vozidla.
- Objeveno youtuberem Bennem Jordanem a expertem Jonem Gainesem (GainSec) přes Shodan, databázi internetových zařízení.
- Flock spolupracuje s tisíci policejními složkami a nedávno s Ringem pro sdílení záběrů z aplikace Neighbors.
- Kamery primárně skenují poznávací značky vozidel, ale Condor modely trackují i jednotlivce.
- Žádné důkazy o úmyslném útoku, ale chyba umožnila volný přístup.

## Podrobnosti
Firma Flock Safety se specializuje na nasazení sítě AI kamer pro veřejnou bezpečnost a spolupracuje s tisíci policejními agenturami a soukromými firmami v USA. Jejich kamery automaticky čtou poznávací značky vozidel a ukládají data do centrální databáze, kterou mohou strážníci prohledávat. Nedávno uzavřeli partnerství s Ringem, což umožňuje zákazníkům Flock žádat záběry z domácích kamer přes aplikaci Neighbors. Kamery Condor, které byly v tomto případě exponované, jdou dál než standardní modely: díky AI funkce pan-tilt-zoom (otočka, naklonění, přiblížení) automaticky sledují pohybující se objekty, jako jsou lidé nebo auta, a zaměřují se na detaily.

Tech youtuber Benn Jordan v spolupráci s Jonem Gainesem, který dříve odhalil další bezpečnostní chyby v systému Flock, prohledal Shodan – vyhledávač internetově připojených zařízení. Našli tak desítky veřejně dostupných livestreamů bez jakéhokoli hesla nebo uživatelského jména. Jordan ve videu popisuje konkrétní pozorování: muž odcházející z domu v New Yorku ráno, osamělá běžkyně na lesní stezce v Georgii, muž na kolečkových bruslích, který si během pauzy pustil videa na telefonu – kamera AI automaticky zoomovala právě na toto. Další příklad byl pár hádající se na pouličním trhu v Atlantě. Tyto záběry ukazují, jak AI nejen sleduje, ale i inteligentně vybírá cíle, což zvyšuje riziko zneužití.

Podle zprávy 404 Media Flock na chybu reagoval a livestreamy uzavřel, ale neposkytl detaily o počtu postižených kamer nebo délce expozice. Gaines předtím w 2023 varoval před podobnými slabinami, jako jsou slabě chráněné API endpointy. Tato chyba není zero-day exploit, ale typický problém špatné konfigurace cloudových služeb, kde vývojáři zapomenou omezit přístup.

## Proč je to důležité
Tato incident podtrhuje rizika rychlé expanze AI dohledových systémů bez dostatečné kybernetické hygieny. Flock pokrývá tisíce lokalit a data z jejich kamer slouží k vyšetřování zločinů, což znamená, že exponované záběry mohly odhalit polohy obětí, svědků nebo podozřelých. V širším kontextu posiluje to debatu o masovém dohledu: AI kamery nejen sbírají data o autech, ale díky pokročilému trackování ohrožují soukromí jednotlivců bez jejich vědomí. Pro průmysl to signalizuje nutnost auditů veřejně dostupných služeb, zejména u firem spolupracujících s policií. V době rostoucího nasazení podobných systémů (jako je partnerství s Ringem) může taková chyba vést k regulacím nebo ztrátě důvěry, což ovlivní celý sektor AI surveillance.

---

[Číst původní článek](https://www.theverge.com/news/849624/flock-ai-camera-feeds-exposed-benn-jordan)

**Zdroj:** ⚡ The Verge
