---
ID: 2237
author: Patrick Zandl
categories:
- Adobe
- Flash
layout: post
oldlink: 'https://www.marigold.cz/item/adobe-flash-ve-verzi-10-prinasi-podporu-p2p

  '
post_date: 2008-05-16 11:22:37
post_excerpt: ''
published: true
summary_points:
- Flash 10 beta představuje P2P technologii, což je zásadní novinka.
- Flash 10 umožňuje ukládat soubory na disk a dynamický streaming videa.
- RTMFP protokol ve Flash 10 umožňuje P2P komunikaci mezi klienty.
- Adobe integruje P2P do Flashe, umožní aplikace typu Skype nebo Joost.
title: "'Adobe Flash ve verzi 10 přináší podporu P2P"

  '
---

Tento týden představila firma Adobe betaverzi Flash 10 (kodové jméno Astro), to jste jistě nepřehlédli. Řada vylepšení se týká renderovacích schopností, filtrů, 3D zobrazení a efektů, od toho nyní abstrahujme, protože žádná z těch novinek není přelomová, v tomto ohledu Flash prostě jde s dobou (a začasté na špici). Detaily zde</a>. 

Co pozornosti většiny médií uniklo, je podpora P2P technologie ve Flashi. A to je něco, co (u)dělá z desáté verze Flashe stejně přelomovou verzi, jako z verze deváté AS3 + podpora H.264, ačkoliv na využití té technologie si počkáme. Však používat H.264 ve Flash 9 se jednotlivé projekty teprve učí a to je rok od doby, co se devítka objevila. 

Pravda také je, že o P2P se přímo v popisu novinek v desítce nedočteme. Adobe ji nijak nezdůrazňuje, proč, o tom lze spekulovat. 

Trochu popořádku. Klíčové změny ve Flash 10 souvisí právě s videem a P2P. Tak za prvé Flash 10 umožní ukládat soubory na disk klientského počítače. Zjevné bezpečnostní riziko, řeknete si, ale také zjevná možnost, jak s Flashem jít dále k plnohodnotným aplikacím. Za druhé jsou tu nové funkce pro média:
dynamický streaming, RTMFP a audio kodek Speex. A to jsou slušné změny. 

Dynamický streaming umožní vybrat přehrávači kvalitu videa (či audia) ve kvalitě přiměřené stavu linky a získávát ze serveru tu. Drobný zádrhel: dle dokumentace to potřebuje FMS v nové verzi, nepůjde to asi s jinými streamovacími servery. Zda to tak skutečně bude, se uvidí, tohle se říkalo i o podpoře H.264 a nakonec chodí i z jiných serverů, ne jen z FMS. 

Zvukový kodek Speex je důležitý pro VoIP aplikace, je to open source kodek vytvořený Xiph.org a kontajnerovaný v rámci Ogg. S oblibou používán v Asterisku na PBX. 

Zkratka RTMFP vypadá nenápadně. Jako maličké rozšíření protokolu pro streamign videa. Není to tak jednoduché, Real Time Media Flow Protocol je zvláštním protokolem vyvinutým firmou Amicima. Jde o síťový rozšířený point to point protokol založený na UDP pro komunikaci mezi klienty a klientem a serverem. Důležité je, že firmu Amicima koupil v roce 2006 Adobe, její produkty pro VoIP a IM postavené na tomto protokolu zmizely z webu, doposud open-source protokol MFP zmizel z očí a dva roky se viditelného nedělo nic. 

Až zmínka v Release Note pro Flash 10 přinesla rozuzlení. Adobe do Flash 10 integruje podporu P2P komunikace na bázi MFP. Ve Flash 10 bude možné nabídnout P2P aplikace používající autentizaci vůči serveru, komunikaci mezi klienty, AES kódování, klíče RSA, QoS a to znamená vyvíjet aplikace velmi podobné Joostu nebo Skype.  

Jak daleko podpora P2P půjde, není zatím vůbec jasné. Oficiální zprávy Adobe jsou velmi stručné, je tu jen zmínka o RTMFP a o tom, že její využití "bude zpřístupněno přes budoucí verzi FMS nebo jiné serverové produkty Adobe". 

Blogy, které si této věci povšimly, už spekulují, jak Adobe nechá zkrachovat business CDNkových firem jako Akamai, tak jednoduše to ale nevidím. Zatím nic nenasvědčuje tomu, že Flash 10 by nasadil P2P nějak bezhlavě, plošně. Zatím to spíše vypadá tak, že AŽ když se Flash 10 aplikace přihlásí na FMS s podporou RTMFP, bude aplikace schopna používat P2P distribuci dat, které servíruje danná FMS aplikace. FMS bude koordinátorem, takovým supernodem - a také bude mít kompletní sestavu dat. P2P distribuce serveru ulehčí, ale zatím to nevypadá tak, že KAŽDÝ, kdo bude mít instalovaný Flash 10, se automaticky stane členem superinternetové P2P sítě ovládané Adobe. Ačkoliv je to zajímavý model, podle dokumentace Amicima (baže už staré dva roky) se uživatel k P2P síti musí dobrovolně přihlásit, jinak to nejde. 

Do toho Adobe ještě podepsalo smlouvu s VeriSignem, majitelem CDN Kontiki, což mi do hypotetických plánů na likvidaci sítí na distribuci obsahu (CDN) moc nezapadá. Výklady ve stylu <em>Adobe tím získá páteř pro podporu P2P</em> mi připadají příliš přitažené za vlasy. 

V každém případě s podporou MFP v rámci Adobe produktů bude ještě švanda. Ano, nemýlíte se. Ve Flash 10 si budete moci vytvořit P2P aplikaci velmi obdobnou ke Skype, Joostu, nebo cokoliv vás napadne. Obsluhovat ji budete farmou distribuovaných FMS serverů, vyvíjet budete v Adobe nástrojích, na webu to nasadíte ve Flashi, časem se podpora MFP dostane do Airu, tím jsem si jist, takže i na klientské stanice. 

Prostě s P2P ve Flashi podle mne bude legrace, ačkoliv vážně k nám tahle technologie začne promlouvat tak za dva roky.