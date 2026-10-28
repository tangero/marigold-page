---
title: Rumsfeldova matice ve fuzzy prostoru, AI a ověření, zda zákony fungovaly
slug: zakony-rumsfeldova-matice-ve-fuzzy-prostoru
author: Patrick Zandl
categories:
  - AI
  - Politika
summary_points: []
thumbnail: /assets/rumsfeldova-matice.webp
audio_url: ''
hide: false
---

Dneska vám povím o tom, co dělám, a také o jedné politické službě, kterou právě spouštím. Proč se chci zastavit u něčeho tak nezajímavého, jako je to, čím se živím a co dělám? Protože to právě předznamenává tu službu, o které chci mluvit.

Třicet let se živím tříděním informací. Nejdřív jako obyčejný novinář, který se naučil, že aby měl atraktivní článek, musí obšlápnout celou řadu zdrojů a postavit je proti sobě. A zároveň jako vývojář, který vidí, jak zpracování informací počítačům prospívá.

No a pak přišla umělá inteligence a já jsem najednou zjistil, že to, co dělám, je vlastně vektorizace Rumsfeldovy matice ve fuzzy prostoru. Laicky řečeno: převádím rozptýlené informace do podoby, v níž lze porovnávat jejich význam, shody a rozpory — a hledat nejen odpovědi, ale také otázky, na něž jsme se dosud ani nezeptali. Právě v tom umí umělá inteligence člověku výrazně pomoct. Ne proto, že by sama věděla, co je pravda, ale protože dokáže mnohem rychleji odhalit souvislosti a mezery, kterých bychom si jinak nevšimli.

Ale právě Rumsfeldova matice popisuje jeden ze základních problémů práce s informacemi. Lidé nějaké informace mají a vědí, že je mají. Jiné nemají, ale alespoň vědí, že jim chybí. Další informace už k dispozici mají, jen si neuvědomují, že je potřeba je začlenit a dát do souvislostí. A nakonec existuje celá řada informací, které nemají, aniž by tušili, že jim chybí.

![](/assets/rumsfeldova-matice.webp)

To, jak umíte pracovat s těmito mezerami, zásadně ovlivňuje, jak realisticky nahlížíte na skutečnost. Chybějící informaci lze obvykle doplnit, pokud víte, že vám chybí. Mnohem nebezpečnější je odmítnout připustit, že by vám chybět mohla. A největší slepé místo vzniká tehdy, když ani nevíte, že byste se měli na něco zeptat.

Až sem to možná zní jako nudná přednáška na pomezí matematiky, statistiky, psychologie a novinařiny. Mezioborová témata mi ale byla vždycky blízká. Jejich jediná vada je, že si o nich nemám s kým povídat. Nezajímají skoro nikoho — _snad jen Pepu Šlerku, a ten by mi řekl, že si na to dávno postavil malé udělátko v Rku a má to vyřešené_.

To je v krátkosti to, čím se živím. Vytvářím systémy, které hledají odpovědi v datech, a princip je podobný, ať už jde o situaci na bojišti, práci se sítěmi 3GPP nebo vývoj českého školství. Praktické uplatnění to dlouho mělo omezené, protože taková analýza byla velmi drahá. Právě to ale umělá inteligence začíná měnit. Vždycky mě bavilo dívat se hluboko pod povrch věcí. Míň už mě baví účet z datového centra za terabajty nasbíraných dat.

A tím se dostáváme k té politické službě. Asi už vás to taky někdy napadlo. Když je přijat nový zákon, mělo by být po určité době samozřejmostí ověřit, jestli dosáhl cílů, kvůli nimž vznikl, co stál a jaké měl vedlejší účinky. A pokud nefunguje, mělo by být možné ho změnit nebo zrušit.

Tahle hříšná a buřičská myšlenka překvapivě napadla i ty nic nedělající úředníky v Evropské unii a OECD. Takže vznikla RIA a dnes se každý vládní návrh zákona musí zapsat včetně předpokladů a termínu vyhodnocení. 

Světe, div se, ne vždycky to dopadne. K tomu vyhodnocení nedochází zdaleka vždycky. A tak jsem se rozhodl vyzkoušet, co s touto legislativou udělá nasazení našeho Orchestrai.

Jak Orchestrai na legislativě funguje? Vlastně „jednoduše". Bere ze všech možných i nemožných datových zdrojů všechno o konkrétní legislativě včetně průběhu její přípravy. Všechno. Pak stanoví mapu předpokladů, na níž ta legislativa vznikla. Stanoví, pokud nebylo dříve řečeno výslovně, jak je možné ověřit, že předpoklady, s nimiž ta legislativa vznikla, byly naplněny. A pak z celé jiné řady datových zdrojů, které získává, ověří, zda byly předpoklady naplněny. A dá verdikt. Neutrální, založený na zdrojích, z nichž nejsilnější je tvrzení „sama vláda předpokládala, že se stane X, stalo se Y“.

Teď to trochu zní jako nástroj, který si přečte dva novinové články a postaví je proti sobě. Ale tak to vůbec není. Nástroj prochází veškeré podklady, veškeré důvodové zprávy, stenografické záznamy z jednání sněmovny atd a novinových článků si všímá v podstatě nejméně, protože ty nejsou primární informací. To je jenom pěna dní. To samé je u vyhodnocení, kde je potřeba opírat se především o účetní a statistická data. Nástroj má přístup k účetnictví šesti a půl tisíce obcí. Takže pokud například ministerstvo tvrdí, že jeho nový zákon o odpadovém hospodářství se obcí nijak finančně nedotkne, můžeme ho snadno usvědčit z omylu nebo mu přitakat. Na vyhodnocení jednoho zákona se tak procházejí stovky megabajtů dat. A ačkoliv naprostá většina těch podkladů je vata nebo opakování řečeného, projít se musí, protože je potřeba vypsat a validovat všechna fakta.

### Ověření dopadu zákonů na RozpočtováSkladba.cz

Nějakou dobu jsem se tím bavil sám pro sebe, protože bylo nesmírně zajímavé a poučné sledovat jednotlivá tvrzení, rozpory mezi výsledky a také souvislosti, které vyniknou až po zpracování celého souboru. Orchestrai přitom nepracuje jen s dokumenty. Simuluje také jednotlivé persony, zamýšlí se nad tím, k jakým výsledkům vede jejich činnost, a tyto poznatky zohledňuje při dalším zpracování. Jednou může jít o náhodu, ale opakovaný vzorec už si zaslouží vysvětlení. To je také odpověď na to, jak moc levné to je. Nepříliš, za což může právě fuzzy povaha celé té informační sady.

No a když jsem si vzpomněl, že mám doménu [Rozpočtová skladba](https://www.rozpoctovaskladba.cz), bylo rozhodnuto. Z mé soukromé zábavy se měla stát veřejně použitelná služba. Nechal jsem proto Orchestrai vygenerovat prvních pár datových sad včetně interpretace. Můžete se na ně podívat a můžete je použít. Berte je trochu s rezervou. Články mohou být kostrbaté, protože se snaží být přesné a akurátní, méně pak zábavné. A to není jednoduché sladit. Aby byly věcně správně, musí se přeci jen trochu držet nudného úředního jazyka dokumentů. Ale to neznamená, že si je nemůžete přepsat.

Postupně bych rád doplňoval další a další témata a pokrýval zákony, na které se v hodnocení RIA nedostalo. Nejde to udělat pro všechno, najednou, protože servery v ceně milionů každou věc počítají skoro hodinu, nevyjde to tedy zrovna levně a tak to pouštím jen v momentě, kdy je volno. Samozřejmě vůbec netuším, jestli to k něčemu bude, nebo jestli česká rezignace na politickou scénu už je za tímto bodem, kdy faktografická práce pomůže. Ale když nic, tak alespoň víte, co dělám, když zrovna neškolím lidi v tom, jak vyvíjet takovéhle (trochu jednodušší) aplikace s AI, nebo s někým neřeším, na co dalšího by se Rumsfeldova matice dala použít...
