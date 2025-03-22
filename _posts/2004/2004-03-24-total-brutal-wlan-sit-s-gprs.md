---
ID: 944
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/total-brutal-wlan-sit-s-gprs

  '
post_date: 2004-03-24 08:33:00
post_excerpt: ''
published: true
summary_points:
- Komunitní síť ve vesnici v horách řeší nedostupnost pevného internetu WiFi sítí.
- GPRS připojení pomocí dvou mobilů naráží na omezení BTS stanice.
- Směrová anténa na mobilu vyřešila problém s rychlostí připojením k jiné BTS.
- Linuxový router kombinuje rychlost dvou mobilů a řídí P2P stahování.
title: Totál brutál WLAN síť s GPRS
---

<p>
Nedávno mi psal o radu jeden čtenář s problémem tak pikantním, že mi to nedá se o něj podělit. Bydlí v jakési vísce v horách, kde o nějakém pevném připojení za rozumnou cenu nikdy neslyšeli a podle všeho ani dlouho neuslyší, nicméně se rozhodl spolu s kamarády, že si tam zasíťují své chalupy a přivedou do vesnice internet. A tak se tu vzdělali a postavili si komunitní síť na WiFi. A pak přišel ten pikantní problém - oni tu síť připojovali do internetu pomocí GPRS a aby měli větší rychlost, koupili si dva mobily a dvě nostop připojení via gprs. Jenže se ukázalo, že obslužná BTSka nemá dva mobily najednou ráda a rychlost shodí prakticky na rychlost jediného připojeného mobilu. A tak jsme špekulovali, co s tím, až se to vyřešilo tak, že se k mobilu přidělala směrovka a ta se namířila na jinou BTSku na druhé straně údolí&#160;:)</p>

<p>
A abych nastínil magičnost toho řešení, oni to na linuxu rozchodili nějak tak, že opravdu ta rychlost těch dvou mobilů (v zásadě oddělených připojení) se spojuje a aby vyřešili i sosání z P2P sítí, tak tam mají nějaký linux software na počítači sloužícím coby router, který vždy, když má síť volnou kapacitu, začne centrálně stahovat požadavky, které se mu zadávají přes web rozhraní. A když začnou uživatelé se síti pracovat, sosání se vypne. Inu, tomu se říká ekonomika provozu, aneb nouze naučila ... </p>