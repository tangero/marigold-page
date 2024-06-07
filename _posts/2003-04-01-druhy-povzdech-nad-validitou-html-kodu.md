---
ID: 212
title: Druhý povzdech nad validitou HTML kódu
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/druhy-povzdech-nad-validitou-html-kodu
published: true
post_date: 2003-04-01 12:44:00
---
<p>
Když jsem včera sliboval dva povzdechy, dostalo se jen na jeden - na faxování přes Českou poštu. Jen připomínám, že faxování z počítače a po internetu by mi nepomohlo, protože jsem potřeboval ihned odeslat formulář vyplněný rukou a s podpisem a kopii pasu a neměl jsem tu scanner...</p>

<p>
<STRONG>Druhý povzdech se týká validity HTML kódu</STRONG>. Netušil jsem, kolik moje zamyšlení nad smyslem validity HTML kodu zdvihne reakcí :) Takže popořadě - Jiří Lavička soudí, že by mi <STRONG>snad nedalo tolik práce udržet těch 10% kodu validního</STRONG>. Právě to je ten nesmysl - nejvíce práce dá oněch 10% chyb - těch 90 % se řeší snadno. Kupříkladu co mám dělat se znakem &amp;, který někdy importuji&#160;v přehledu cizích článků. Sám se entitou nenahradí a nahrazovat ho softwarově by znamenalo štourat se do scriptu pro import a to by bylo na hodinu. Tu hodinu, kterou jsem <STRONG><A href="/adsl"><STRONG>raději věnoval aktualizaci přehledu&#160;cen ADSL</STRONG></A></STRONG>. Neříkám, kdybych neměl na Marigolda o čem psát, to bych to ladil do aleluja... jenže problém je opačný. A opravovat to neustále ručně? To se mi nechce - nemá to smysl.</p>

<p>
Další se <STRONG>pozastavila Sova v síti, </STRONG>to když se M. Prokop ptal, zda je <A href="http://www.sovavsiti.cz/weblog/2003/03/29.html#bp20030329_valid_html">Validní HTML jen pro fanjšmekry?</A> A první věc, kterou mi vytýká je, že nemá Marigold nastavené kódování v metatagu. Jistěže nemá. Marigold používá kódování češtiny na straně serveru. Takže i starší prohlížeče, které neumí dokument překódovat do správné znakové sady, dostanou dokument čitelný. A kdybych dal metatag s natvrdo nastaveným kódováním, mohlo by se to lidem špatně překódovat (vyzkoušeno v praxi). Čili mám na výběr: buďto odstranit chybičku, která dělá problém jen validátorům, nebo nutit lidi se starými prohlížeči k upgrade. Zatím vsázím na to, vykašlat se na metatag kódování. </p>

<p>
Dalším problémem je třeba uzavírání tagů P. Tyhle tagy dávám ručně, když vkládám zprávu napsanou v textovém editoru, abych nepoužíval import z Wordu (ten HTML dobře zmrví). A jsem líný dávat koncový tag. Problém? Jen pro validitu. Prohlížeč vše zobrazí. </p>

<p>
Což mne donutilo <STRONG>zamyslet se trochu nad smyslem validity</STRONG>. Na povinnost validního kódu nadávám od doby WML - pokud máte WML stránku špatně, mobilní telefon ji ve wapu nezobrazí. Pamatuji si, jak jsme začali všechny možné internetové systémy nutit do generování validního WML a jaký to byl horor. Dodneška je <STRONG>velký problém tvorby složitějšího WAPového obsahu</STRONG> fakt, že stránka se při jediné chybě v zápisu <EM>(třeba právě zápisu znaku &amp; jako znaku místo entity) </EM>nezobrazí.</p>

<p>
Prvotní příčina ovšem <STRONG>nebyla buzerovat lidi, aby dělali validní kód</STRONG>. Prvotní příčina byla umožnit zobrazení stránek i na zařízeních, která mají jednoduchý prohlížeč, jenž si nedomyslí špatně ukončený znak. Opravdu - dnešní velké prohlížeče jsou velké mimo jiné proto, že myslí za tvůrce webu - neuzavřenou tabulku uzavřou, neukončený odstavec ukončí atd. Wap prohlížeče v telefonu nebo hodinkách (fakt to existuje i v hodinkách) se musí nacpat do malé paměti a na pomalý procesor, proto je požadavek na validní kód. Jenže dneska jsou paměti telefonů a procesory hodinek tak velké, že i běžné prohlížeče v těchto zařízeních by s tím problém neměly (a také nemají).</p>

<p>
A tak si můžeme vybrat. <STRONG>Buďto budeme důsledně lpět na podle mne zcela nesmyslném mýtu 100% validního kódu, nebo se smíříme s tím, že takové věci za nás mají domyslet stroje a programy.</STRONG> Druhá cesta je podle mne lepší, protože nechává více prostoru lidem na to, co dělat chtějí a netlačí je do něčeho, co dělat musí.</p>

<p>
A tak jsem rád, že <STRONG>se mnou souhlasí alespoň Yuhůův weblog</STRONG>, když říká, že <A href="http://dusan.pc-slany.cz/weblog/archiv/200303.html#validita2">Účelnost validace je sporná</A> a klade pro to řadu argumentů. Pozor - neříkám nic o tom, že je&#160;nemoudré dělat stránky v CSS - opravdu od té doby, co tu používáme CSS je kód mnohem přehlednější. Ale z mnoha drobných příčin není kód validní. A asi ani jen tak nebude - minimálně do doby, než s tím začnou mít supermoderní prohlížeče problémy... a to doufám nikdy nenastane...</p>
