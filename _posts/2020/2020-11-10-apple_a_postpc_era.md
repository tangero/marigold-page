---
categories:
- Apple
- ARM
- PostPC
- Počítače
date: 10.11.2020
excerpt: Na úterní presentaci představil Apple dlouho očekávanou řadu počítačů vybavených
  vlastním procesorem Apple M1 namísto dosavadně používaných procesorů Intel. O tomto
  kroku se ví již nějakou dobu, byl i oficiálně oznámen Timem Cookem, jenže na konkrétní
  parametry se čekalo.
featured: true
layout: post
summary_points:
- Apple představil nové počítače s procesorem M1, nahrazujícím Intel.
- Procesor M1 nabízí vyšší výkon a nižší spotřebu než Intel.
- Apple tvrdí, že M1 má nejrychlejší integrovanou grafiku na trhu.
- Přechod na ARM architekturu znamená konec éry Intelu v Apple zařízeních.
thumbnail: https://fossbytes.com/wp-content/uploads/2020/11/Apple-ARM-M1-Chip-MacBook-Apple-Silicon-681x383.jpg
title: Apple s ARM procesory a PostPC éra
---

Na úterní presentaci představil Apple dlouho očekávanou řadu počítačů vybavených vlastním procesorem Apple M1 namísto dosavadně používaných procesorů Intel. O tomto kroku se ví již nějakou dobu, byl i oficiálně oznámen Timem Cookem, jenže na konkrétní parametry se čekalo.

Trojice přestavených počítačů v podstatě kopíruje dosavadní řadu. Macbook Air (startuje na 1000$), třináctipalcový MacBook Pro (1300$ a výše) a Mac Mini od sedmi stovek, tam je to o stovku méně, než dosavadní Mini na Intelu, který byl už poněkud přepálený. Parametry i vzhled tak, jak je znáte, snad jen  [USB 4.0 / Thunderbolt 3](https://www.pocket-lint.com/laptops/news/intel/147329-usb-4-specs-news-features)  s přenosovou rychlostí 20-40 Gb/s se zjevilo v komerčně prodávaném hardware snad poprvé, specifikace je teprve rok stará. A WiFi se posunulo na 802.11ax, ale to je spíš perlička pro fajnšmekry.

Důležité je předvším  **seběvědomí,**  s nímž Apple mluví o rychlosti nových notebooků. Má mít nejrychlejší integrovanou grafickou kartu (součást M1), video zpracovává 4x rychleji, grafiku 7x rychleji, než cenově stejně orientovaný počítač Apple od Intelu. Konkrétně se porovnává osmijádro M1 se čtyřjádrem Core i7 na 1,2 GHz nebo čtyřjádrem i3 na 3,6 GHz. To samozřejmě nejsou nejrychlejší procesory, které kdy Intel vyrobil, ale jejich použití je do srovnatelných typů počítačů a spotřeba je výrazně větší. Apple udává výdrž Air z dvanácti hodin na Intel verzi na osmnáct hodin ARM verze při koukání na Apple TV. To není vůbec malý rozdíl, doposud se optimalizace pohybovaly kolem do deseti procent

Jinak v rámci pouzdra ([SoC – systém na čipu](https://en.wikipedia.org/wiki/System_on_a_chip)) je kromě grafické karty také ještě jednotka pro umělointeligenční výpočty (pro které se hodí jiný typ zpracování kódu), vstupně/výstupní rozhraní a další čipy včetně DRAM. Což je podstatné, paměť integrovanou v rámci SoC nebude možné zřejmě nijak upgradovat a musíte ji zvolit uvážlivě při nákupu počítače. Odměnou za to je rychlejší práce s pamětí díky nulové latenci. O procesoru Apple M1 najdete  [český dobrý článek zde](https://www.letemsvetemapplem.eu/2020/11/10/apple-m1/). Apple říká, že je to nejlepší procesor světa a v té konzumní sféře procesorů mu to tvrzení můžeme směle věřit. Hlavní výhodou má být efektivita: tedy poměr výkonu versus spotřeby a s tím související absence aktivního chlazení v Airu a jen minimálního větráčku v Mini / Pro.

**Jak je možné, že Apple postaví lepší procesory, než Intel?**

Úkrok stranou. Jak je tohle možné? Jak může být Apple procesor výkonější a lepší, než procesory od Intelu, který je dělá o pár desetiletí déle? To máte tak: Intel je CISC procesor, Apple M1 je architekturou ARM, tedy RISC procesor. Ve skutečnosti se nedá říct, že jeden je rychlejší, než druhý, při podobných parametrech, každý se hodí na trochu jiný typ úloh. Rozdíl mezi těmito procesory na nejvyšší vrstvě je zajímavý i pro lajka. Intel používá architekturu procesorů s velmi složitou instrukční sadou, díky níž procesor zvládá za běhu optimalizovat vykonávání kódu. ARM používá procesory s redukovanou instrukční sadou a o veškerou optimalizaci se stará překladač při překladu. Překladače pro ARM mají za sebou tři desetiletí vývoje a optimalizovat už umí hodně dobře. Kdyby vás to zajímalo mírně detailněji,  [pak česky tady](http://lucie.zolta.cz/index.php/pocitace-a-site/37-architektura-mikroprocesoru).

A tady se blížíme k bodu singularity našeho vyprávění. Apple již dříve procesory s RISC architekturou používal, šlo o procesory PowerPC vyvíjené Motorolou, IBM a Apple. Z PowerPC ovšem Apple v roce 2005 vystoupil, procesory v té době signifikantně ztrácely na výkonu oproti Intelu. Někdy to bývá bráno jako důkaz toho, že RISC architektura proti CISC neobstojí, ve skutečnosti za to mohlo nedostatečné odhodlání Motoroly investovat do dalšího vývoje PowerPC. Intel to prostě svojí technologickou a výrobní mašinérií převálcoval. Tedy, až donedávna. Nyní se i kolos Intelu zadrhl a nedaří se mu zvládnout nové výrobní procesy. Nedávno oznámil, že procesory z výrobního procesu 7 nanometrů bude  [dodávat až v roce 2023](https://www.tomshardware.com/news/intel-announces-delay-to-7nm-processors-now-one-year-behind-expectations)kvůli defektu způsobujícímu degradaci procesoru. Což je pitomé, konkurenční AMD bude v té době dodávat pětinanometrové ([skvělý přehled zde](https://en.wikipedia.org/wiki/5_nm_process)) a taiwanské TSMC vyrábějící procesory pro Apple (zřejmě včetně M1) v té době již poběží na  [třínanometrovém procesu](https://en.wikipedia.org/wiki/3_nm_process). Přitom právě nanometry rozhodují o energetické účinnosti, ale Dennardův škálovací zákon si probereme někdy příště.

Zatím není jasné, zda jde o drobnou odchylku od tzv. **Moorova zákona**  predikujícího vývoj procesorů, nebo o fundamentální problém. Je ale jisté, že Apple narazil na neschopnost Intelu dodávat mu energeticky úsporné a přitom dostatečně výkonné procesory – Core i3 to opravdu není. To za prvé. Za druhé, návrh procesoru CISC má vysoké finanční i časové náklady na design, což je znevýhodňuje v soupeření s RISC procesory, jako je ARM. Navíc se návrh v roce 2007 kvůli iPhone přesunul k SoC, systémy na čipu, které lze dobře skládat modularitou a spoluprací s jinými návrháři. Velmi podrobný článek, který doporučuji pozornosti, najdete zde:  [A New Golden Age for Computer Architecture](https://cacm.acm.org/magazines/2019/2/234352-a-new-golden-age-for-computer-architecture/fulltext?mobile=false#body-3).

Tyto problémy ostatně pochopil i **Microsoft**, který přispěchal s verzí Windows 10 pro procesory ARM a také se svými „vlastními“ procesory rodiny SQ, nejnověji pak s SQ2. Jde o procesory „spoluvyvinuté“ s Qualcommem, přesněji Snapdragon 8cx SoC (verze se liší vestavěným GPU). Procesory Microsoft dodává do svých konvertibilních tabletů Surfaxe Pro X, které jsou sice milé, ale prodejních čísel Macbooků rozhodně nedosahují. Uvidíme, jak dlouho bude Microsoft bavit podporovat vlastní procesory a hlavně ARM verzi operačního systému, která jinak většího rozšíření nedoznala už proto, že vývojáři do ní moc neportují vlastní aplikace.

No a to je ten zádrhel, který Apple řeší Rosetou, online překladačem instrukcí mezi Intelem a ARM instrukční sadou. Opět jde o něco, s čím firma měla zkušenosti z doby přechodu od PowerPC a nyní je oprášila. K podobnému kroku se odhodlal i Microsoft a letos v září potvrdil, že pro ARM verzi Windows  [bude dodávat podobný realtime překladač](https://www.theverge.com/2020/9/30/21495510/microsoft-windows-on-arm-x64-app-emulation).

**PostPC éra**

Intel od svého vrcholu v roce 2011 ze slávy značně ustoupil a většinu mu jí sebral právě ARM. Procesory ARM všech provedení a výrobců dnes představují více jak 95% všech prodaných procesorů a postupují stále dál. Od jednoúčelových počítačů, přes mobilní telefony a tablety, až po servery a nyní i osobní počítače, kdysi tak vynucující kompatibilitu s Intelovskou architekturou x86, protože bez ní nefungovaly Windows a bez Windows nebyl počítač počítačem.

Intelu odchází významný zákazník, ale drama samo o sobě to pro něj není. Apple dělá Intelu cca pět procent obratu. Není to zlom, ten přišel dávno, v roce 2007 spolu s celou architekturou iPhone a post-PC érou. Je to jen potvrzení neodvratného. Éra PC – osobních počítačů – končí. Teď už jsou počítače všude a mluvit o nich jako o osobních, postrádá smysl.

A jak Apple může zahubit sebe sama? Inu tak, že přechod na ARM nezvládne a stane se mu to samé, co s PowerPC, tedy zaspí s kontinuálním vývojem. Nicméně o tom pochybuji. Apple je dnes firmou neomezených zdrojů, může si dovolit výzkum procesorů financovat v libovolném rozsahu a kromě toho jich může desítky milionů ročně odebrat a uplatnit. K jakým odběrům se fabrice TSMC zavázal, není přesně známo, ale fakt je, že když s ní letos podepsal kontrakt, mohla si firma dovolit začít s investicí 12 miliard dolarů do výrobních kapacit.

A aby to všechno Apple organizačně zvládl, koupil si v roce 2008 společnost  [P.A. Semi](https://moorinsightsstrategy.com/apples-plan-to-dominate-silicon/).

**Co bude zajímavé sledovat, jakou vlnu to strhne.**  Nejdříve žádnou: finanční výtlak a převahu v integrovaném ekosystému jako Apple nemá nikdo, snad jen Microsoft a čínští výrobci, kteří jsou v poněkud jiné situaci a nemusí se podvolovat nutnosti kompatibility s Wintelem (platformou Windows – Intel). Jenže Post-PC éra bude pokračovat dále a erodovat jak postavení Intelu, tak Windows a pojetí počítače, jako něčeho, před co usedáme za pracovním stolem. Počítače za deset let budou úplně jiné, než dnes a úplně jiné, než před deseti lety.