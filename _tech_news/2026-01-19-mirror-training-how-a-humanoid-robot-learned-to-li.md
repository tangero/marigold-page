---
author: Marisa Aigen
category: robotika
date: '2026-01-19 16:03:30'
description: Silikonové rty se přesně pohybovaly s každou slabikou, tvořily kulatý
  tvar pro „hello“ a uzavřenou polohu pro „world“. Poprvé se robot naučil synchronizovat
  řeč a pohyb rtů ne manuálním programováním, ale sledováním sebe sama v zrcadle.
importance: 5
layout: tech_news_article
original_title: 'Mirror Training: How a Humanoid Robot Learned to Lip Sync Using AI
  and a Reflection'
publishedAt: '2026-01-19T16:03:30+00:00'
slug: mirror-training-how-a-humanoid-robot-learned-to-li
source:
  emoji: 📰
  id: null
  name: ScienceBlog.com
title: 'Zrcadlový trénink: Jak se humanoidní robot naučil synchronizovat rty se řečí
  pomocí AI a odrazu'
url: https://scienceblog.com/mirror-training-how-a-humanoid-robot-learned-to-lip-sync-lip-using-ai-and-a-reflection/
urlToImage: https://scienceblog.com/wp-content/uploads/2026/01/face.jpeg
urlToImageBackup: https://scienceblog.com/wp-content/uploads/2026/01/face.jpeg
---

## Souhrn
Výzkumníci z laboratoře Hod Lipsona na Columbia University vyvinuli humanoidního robota, který se naučil synchronizovat pohyb rtů se slovy pomocí umělé inteligence a zrcadla. Robot pozoroval svůj vlastní odraz, analyzoval ho AI modelem a postupně upravoval mechanické pohyby pro přesnou shodu s výslovností. Tento přístup nahrazuje tradiční manuální programování a přispívá k překonání tzv. uncanny valley v robotické mimice.

## Klíčové body
- Robot s 10 stupni svobody v oblasti rtů: dva motory pro každý roh, tři pro horní ret, jeden pro čelist a dva pro dolní ret.
- Trénink založený na zrcadle: robot sleduje svůj odraz a AI porovnává vizuální data s audio signálem.
- Překonání tradičních limitů: žádné pevně nastavené pravidla pro fonémy, místo toho učení podobné lidskému napodobování.
- Zaměření na obličej: lidé věnují během konverzace téměř polovinu vizuální pozornosti pohybu rtů.
- Hardware s magnetickými konektory pro snadnou výměnu a úpravu obličeje.

## Podrobnosti
Laboratoř Creative Machines Lab na Columbia University, vedená Hod Lipsonem, se dlouhodobě zabývá vývojem humanoidních robotů schopných přirozeně interagovat s lidmi. Klíčovým problémem byl obličej, zejména ústa, kde i pokročilé roboty pohybují rty pouze hrubě – otevíráním a zavíráním podobně jako loutky. Lidé jsou na chyby v mimice extrémně citliví: během tváří v tvář konverzace směřuje přibližně polovina vizuální pozornosti na rty a nesoulad i o zlomek sekundy okamžitě odhalíme.

Tým Lipsona navrhl hardware s vysokou flexibilitou: oblast rtů má 10 stupňů svobody. Dva motory ovládají každý roh rtů, umožňují stažení nebo vysunutí pro těsné uzavření nutné u zvuků jako „b“ nebo „p“. Horní ret má tři motory pro jemné zakřivení, čelist jeden pro vertikální pohyb a dolní ret dva pro boční a vertikální úpravy. Silikonová kůže je připojena magnetickými konektory, což usnadňuje demontáž a úpravy. Tento design umožňuje tvořit subtilní tvary odpovídající fonémům, jako kulatý tvar pro „o“ nebo zašpičatělý pro „u“.

Tradiční metody spočívaly v manuálním mapování pohybů na jednotlivé zvuky (fonémy), což bylo pracné a vedlo k nepřirozeným výsledkům – podobně jako programování chůze krok za krokem místo učení zkušeností. Nový přístup, nazvaný mirror training, funguje tak, že robot vyslovuje slova (audio signál) a současně sleduje svůj odraz v zrcadle. AI model, pravděpodobně založený na neuronových sítích pro počítačové vidění a reinforcement learning, analyzuje video a porovnává pohyb rtů s očekávaným tvarem z tréninkových dat. Robot pak upravuje motory, aby minimalizoval chybu. Tento sebe-supervizovaný trénink umožňuje generalizaci na nová slova bez explicitního programování.

Text zmiňuje pokračování systému s magnetickými konektory, což naznačuje modulární design pro další iterace. Laboratoř se zaměřuje na kreativní stroje, které se učí autonomně, podobně jako v předchozích pracích na samoorganizujících se robotech.

## Proč je to důležité
Tento vývoj představuje zásadní posun v robotice směrem k autonomnímu učení obličeje, což je klíčové pro humanoidní roboty v sociálních rolích – péče o seniory, vzdělávání nebo zákaznický servis. Překonání uncanny valley zlepší důvěru a přirozenost interakce, kde současné roboty jako ti od Boston Dynamics excelují v pohybu těla, ale selhávají v mimice. V širším kontextu posiluje integraci AI do robotiky: podobné techniky lze aplikovat na emoce, gesta nebo dokonce celkovou antropomorfii. Pro průmysl znamená méně závislosti na expertním programování, rychlejší nasazení a škálovatelnost. Nicméně zůstává výzvou real-time výpočetní náročnost a robustnost v reálném světě mimo kontrolované prostředí laboratoře. Tento pokrok může urychlit komercializaci humanoidů od firem jako Figure nebo Tesla Optimus.

---

[Číst původní článek](https://scienceblog.com/mirror-training-how-a-humanoid-robot-learned-to-lip-sync-lip-using-ai-and-a-reflection/)

**Zdroj:** 📰 ScienceBlog.com
