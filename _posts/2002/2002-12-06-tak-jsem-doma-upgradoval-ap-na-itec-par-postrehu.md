---
ID: 5
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/tak-jsem-doma-upgradoval-ap-na-itec-par-postrehu

  '
post_date: 2002-12-06 10:12:00
post_excerpt: ''
published: true
summary_points:
- iTec Access Point měl kusý manuál, neuvádějící nutnost adresy 192.168.0.1.
- Kabeláž iTec vyžadovala přímý kabel, na rozdíl od staršího Z-Comu s kříženým.
- Nová WiFi síť od iTecu ztrácí signál každou čtvrt hodinu.
- Noname WiFi technika, jako iTec, se hůře konfiguruje než značková.
title: Tak jsem doma upgradoval AP na iTec – pár postřehů
---

Jak jsem se zmínil, nakoupil jsem včera <STRONG>nový Acces Point od iTecu </STRONG>a tak jsem se večer věnoval upgrade domácí WiFi sítě. Byla to legrace. Především manuál od iTecu je dosti kusý a jako většina manuálů se věnuje hlavně tomu, co je jasné. V manuálu se sice dozvíte, že AP je potřeba připojit na stejný segmet sítě, jako počítač, ze kterého chcete AP konfigurovat, už se ale nedozvíte, že AP musí od DHCP dostat adresu 192.168.0.1. V návodu se píše, že AP si chytne adresu z DHCP, ale až řadou pokusů jsem došel k tomu, že mimo tenhle segment máte smůlu. Tož jsem nejdříve rekonfiguroval SMC router tak, abych celou vnitřní síť měl adresovanou jako 192.168.0.x. Když ani potom AP nebylo k nalezení, podle nesvítící diodky Link jsem detekoval problém na kabelu. Inu, ukázalo se, že zatímco AP od Z-Comu vyžadoval křížený kabel, iTech zase chtěl klasický a já jsem samozřejmě pouze přepojil kabel ze starého Z-Comu do iTecu. Po výmněně kabelů už šlo všechno hladce. Konfigurační program si APčko našel, nastavil jsem parametry, rebootnul APčko a nové WiFi běží. Až na to, že jednou za čtvrt hodiny se ztratí signál z AP a zatím jsem nepřišel na to proč. Nu, mám na to celý víkend :) A tímto textíkem jsem vám také chtěl vysvětlit, čím se liší noname (promiňte, ale iTec je noname) WiFi technika od těch značkových výrobků - ty značkové se podstatně snáze konfigurují, ale zase si někdy přidávají své vymyšlenosti a rozšíření, na kterých můžete zadrhnout...