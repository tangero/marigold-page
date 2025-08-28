---
categories:
- Apple
excerpt: Apple nově představil technologii pro odhalování takzvané CSAM (Child Sexual Abuse Material), tedy dětské pornografie. Technologie má přijít do iOS v některém z update chystané verze iOS 15 a má pomoci v boji s dětskou pornografií.
featured: true
layout: post
title: Apple jde do dětského porna
---


Apple nově představil  [technologii pro odhalování takzvané CSAM (Child Sexual Abuse Material)](https://www.apple.com/child-safety/), tedy dětské pornografie. Technologie má přijít do iOS v některém z update chystané verze iOS 15 a má pomoci v boji s dětskou pornografií. To ovšem dosti kontroverzním způsobem. iOS zařízení zanalyzuje fotky ukládané na iCloud Photo a pokud tam najde dětskou pornografii, provede akci, u níž se zastavíme pozdějí. Fotky, které jsou uložené jen lokálně, se takto neanalyzují - proto, že se dále nešíří. A Apple deklaruje svůj zájem omezit šíření dětské pornografie. Další věc, která je důležitá: fotografie se analyzují přímo na mobilním telefonu. To ostatně iOS zařízení dělají již dnes, fotky analyzují a popisují pomocí AI, takže si pak můžete nechat vyhledat fotky "moře" a ono vám je najde. Proč je to podstatné? Zařízení neohrožuje end-to-end šifrování ani v iCloudu, ani ve Facetime (kde také fotky analyzuje, fakticky jdou přes iCloud). Technicky vzato vytvoří Apple digitální podpis fotky nazvaný NeuralHash a porovná jej s podpisy v databázích fotek organizací bojujících s dětskou pornografií. Vcelku jednoduché, byť se ukazuje, že to může být problematické, neboť zcela nevinná fotka může mít vinný NeuralHash ([viz zde](https://blog.roboflow.com/nerualhash-collision/)).

  

Apple se hájí. Vše je bezpečné, chvályhodné a technicky perfektní. Nikdo ze zaměstnanců Apple se nehrabe ve fotkách, nic takového. Dokonce i false positive hlášení nebudou problém.

  

Jenže příklad z Princetonské univerzity ukazuje, že tak přímočaré osudy technologií být nemusí. Univerzita v Princetonu podobný systém vymyslela před lety a experimentálně zprovoznila. Vlastně technicky úplně stejný, jen si jej nemohla vynutit v mobilech. Problém nastal v momentu, kdy si průzkumníci uvědomili, že pro vládu nemusí být těžké vynutit si přidání dalších fotek do té zdrojové databáze, například fotky politických oponentů. A tím od nicnetušících občanů získávat samoudání.

  

Podobných výhrad zaznívá celá řada a je pozoruhodné, jak rychle se firmě Apple podařilo prokoučovat roky budovanou image ochránce dat i soukromí. Apple se hájí, že boj proti dětské pornografii a zneužívání je důležitý, což má pravdu. Je. Ale důležitý je i boj proti hospodářské kriminalitě a vraždám - a to není důvod, proč by měl nějaký AI robot prolézat vaše zprávy a v rámci pre-crime vás varovat, že se chystáte na něco nekalého a že příště upozorní vašeho sociálního kurátora.

  

Na Apple je nyní vyvíjen velký tlak a uvidíme, jak to firma ustojí. Odhodlání vedení je velké, ale argumenty proti velmi dobré. Technologické firmy tu nejsou proto, aby hlídaly dodržování zákonů, to si Apple spletl roli s policií a vemlouvavé pasáže o společenské zodpovědnosti nemohou zastřít, že na tohle připraveni nejsme a otázka zní, zda se na to připravovat chceme.