---
author: Marisa Aigen
category: elektronická válka
date: '2026-01-14 00:30:05'
description: Írán ruší Starlink pomocí vojenských elektronických válkových nástrojů,
  pravděpodobně dovezených z Číny a Ruska, nasazených na mobilních platformách jako
  náklaďáky nebo drony. To vytváří lokální, patchy rušení s packet loss eskalujícím
  z 30 % na přes 80 % v postižených oblastech.
importance: 4
layout: tech_news_article
original_title: Iran Jamming of Starlink and Ways to Overcome Jamming
publishedAt: '2026-01-14T00:30:05+00:00'
slug: iran-jamming-of-starlink-and-ways-to-overcome-jamm
source:
  emoji: 📰
  id: next-big-future
  name: Next Big Future
title: Íránské rušení Starlinku a způsoby překonání rušení
url: https://www.nextbigfuture.com/2026/01/iran-jamming-of-starlink-and-ways-to-overcome-jamming.html
urlToImage: https://nextbigfuture.s3.amazonaws.com/uploads/2022/05/starlinkmobile.jpeg
urlToImageBackup: https://nextbigfuture.s3.amazonaws.com/uploads/2022/05/starlinkmobile.jpeg
---

### Souhrn
Írán nasazuje vojenské elektronické válkové (EW) systémy k rušení služby Starlink, což brání protestujícím v sdílení informací. Rušení je lokální a mobilní, zaměřené především na uplink (odesílání dat), a využívá slabiny GPS i RF signálů Starlinku. Eskalace packet loss z 30 % na více než 80 % ukazuje na rostoucí efektivitu těchto opatření.

### Klíčové body
- Použití vojenských EW nástrojů z Číny a Ruska na mobilních platformách (náklaďáky, drony) pro lokální rušení.
- Prioritní rušení uplinku k blokování odesílání médií protestujícími.
- Barrage jamming a spoofing GPS signálů v pásmu L1 (1,575 GHz) s výkonem -160 dBW.
- Přímé RF rušení downlinku/uplinku s výkony 100–500 W v dosahu 5–20 km.
- Mobilita jammerů umožňuje dynamické cílení na místa protestů.

### Podrobnosti
Starlink terminály od firmy SpaceX, která se specializuje na satelitní internetovou síť s tisíci nízké oběžné dráhy satelitů, potřebují přesné polohové údaje z GPS pro zaměření na satelity nad hlavou a synchronizaci paprsků. Íránské síly tyto slabé GPS signály, které dorazí na zem s minimálním výkonem kolem -160 dBW, zahlcují vysokoenergetickým šumem prostřednictvím barrage jamming. Tím zvyšují úroveň šumu a snižují poměr signál-šum (SNR) pod použitelnou hranici, obvykle pod 10 dB, což znemožňuje terminálům vypočítat pozici a předat spoj na další satelit.

Další technikou je spoofing, při kterém se vstřikují falešné signály, aby terminály byly uklamány v poloze. Přímé RF rušení pak přetěžuje frekvence downlinku (satelit-země) a uplinku (země-satelit) širokopásmovým šumem. Starlink signály mají na zemi nízkou hustotu výkonu kolem -120 dBm díky nízkému výkonu paprsků satelitů (1–10 W), což činí terminály citlivými na rušení. Pozemní jammery s výkonem 100–500 W tak dominují v okruhu 5–20 km v závislosti na terénu, směrové antény zaměřují energii do denial zón.

Jammery nejsou pevné, ale vozidlové, což umožňuje rychlé přesuny k protestním horkým místům. Jsou energeticky náročné a nemohou pokrýt celý Írán, proto vytvářejí přerušované regionální výpadky. Propagace RF signálů podléhá zákonu inverzního čtverce vzdálenosti, takže účinnost klesá s dálkou; v městském prostředí budovy a kopce tlumí signály multipath fadingem nebo stíněním. Uplink je rušit snazší než downlink díky vyšší citlivosti terminálů na odchozí signály. Celkově rušení eskalovalo z 30 % na přes 80 % packet loss v cílových oblastech, což asymetricky brání odesílání videí a fotek ven.

### Proč je to důležité
Toto rušení představuje reálnou výzvu pro Starlink v autoritářských režimech, kde slouží k obcházení cenzury a podporuje svobodnou komunikaci. Ukazuje limity současných satelitních systémů vůči státním EW schopnostmi, což nutí SpaceX vyvíjet protiopatření jako adaptivní frekvence, anti-jamming antény nebo integraci s jinými GNSS (např. Galileo). V širším kontextu posiluje to zájem o odolné komunikace v konfliktních zónách a ovlivňuje geopolitiku, kde satelitní přístup mění dynamiku protestů. Pro průmysl to znamená rychlejší inovace v RF odolnosti, zatímco pro uživatele v Íránu omezuje spolehlivost služby.

---

[Číst původní článek](https://www.nextbigfuture.com/2026/01/iran-jamming-of-starlink-and-ways-to-overcome-jamming.html)

**Zdroj:** 📰 Next Big Future
