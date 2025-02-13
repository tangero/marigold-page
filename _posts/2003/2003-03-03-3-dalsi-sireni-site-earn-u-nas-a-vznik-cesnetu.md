---
ID: 1067
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/3-dalsi-sireni-site-earn-u-nas-a-vznik-cesnetu

  '
post_date: 2003-03-03 09:49:00
post_excerpt: ''
published: true
summary_points:
- Československo se připojilo do EARNu, ale pouze pražská akademická pracoviště.
- EARN nebyl perspektivní kvůli specifickým protokolům a nemožnosti propojení s jinými
  sítěmi.
- Vznikla myšlenka celostátní páteřní sítě pro akademická pracoviště, budoucí CESNET.
- Pro CESNET se zvažovaly protokoly X.25 (levnější) a TCP/IP (modernější), zvolen
  TCP/IP.
title: 3. Další šíření sítě EARN u&nbsp;nás a&nbsp;vznik CESNETu
---

Československo se sice připojilo do EARNu, ale jen pražská akademická pracoviště. A tak se začalo pracovat na celostátní páteřní akademické síti - ta později dostala jméno CESNET.<!--more--><p>
Připojením do sítě EARN&#160;ovšem bylo vyřešeno připojení jednoho pracoviště v Praze - akademických pracovišť, která by logicky měla být napojena do sítě EARN, byly ale v české republice desítky. Problém představovala telekomunikační infrastruktura nalézající se v té době v neuspokojivém stavu. Cena za pronájem analogové linky nevalné kvality a hlavně nevalné přenosové rychlosti tehdy neumožňovala připojit většinu pracovitšť pevnou linkou. Proto se EARN rozšířil rychle v rámci Prahy, kde poplatky a vzdálenosti mezi pracovišti nebyly velké, z ostatních měst se ale dostal pouze do Brna a Bánské Bystrice. Ostatní pracoviště se musely připojovat terminálovým přístupem pomocí komutované telefonní linky, tedy za klasické telefonní poplatky a tomu odpovídající rychlost 2400 nebo 9600 bps. V tomto případě šlo o velmi nekomfortní, dlouhodobě neperspektivní a vzhledem ke kvalitě služeb i velmi drahé řešení a bylo třeba začít hledat východisko. 
<p>
Jedno takové řešení nabídlo IBM v rámci své Akademické iniciativy. V Praze na svoje náklady vybudovalo akademické pracoviště vybavené počítačem IBM3090 a proměnilo jej v uzel sítě EARN (CSPUNI21). Dále si pronajalo vyhrazené okruhy na univerzity do Brna a do Bratislavy a zde zřídilo terminálové pracoviště poskytující všechny služeby EARN. Situaci ostatních vysokých škol a výzkumných pracovišť ovšem tato akce nemohla změnit a bylo nutno hledat další, pokud možno systémové řešení. 
<H4>EARN neprespektivní</H4>
<p>
V té době se zároveň jasně ukazovalo, že dlouhodobě není síť EARN perspektivní. Hlavním důvodem byla skutečnost, že EARN používá specifické přenosové protokoly a nenabízí jednoduchou možnost, jak přenosové cesty pro něj vyhrazené využít současně i pro přenosové protokoly jiných sítí. Navíc v té době se již v zahraničí ozývaly hlasy o nutnosti přerodu EARNu v interaktivní síť a o nutnosti jeho zblížení či splynutí s internetem. Dlouhodobá orientace na EARN se ukázala být neudržitelnou. 
<H4>Páteřní síť CESNET</H4>
<p>
Již v polovině roku 1991 se objevuje myšlenka, vybudovat <STRONG>celostátní páteřní síť sloužící k propojení akademických pracovišť</STRONG>. A protože již tehdy bylo jasné, že počítačové sítě prožívají prudký rozvoj, bylo navrhnuto, aby takováto páteřní síť byla co nejotevřenější a nejuniverzálnější. Měla tedy splňovat několik hlavních kritérií: 
<OL>
<LI><STRONG>pokrývat území celého Československa</STRONG> (delení republiky přišlo na přetřes až v roce 1992)</LI>
<LI><STRONG>sloužit pro akademická</STRONG> a vzdělávací pracoviště</LI>
<LI><STRONG>multiprotokolový provoz</STRONG>, tedy schopnost pracovat s více protokoly současně. Tím by mohla do budocna propojit i více různých typů sítí a být otevřená pro budoucí protokoly.</LI>
<LI><STRONG>jednotný management</STRONG>, jak technický, tak finanční a organizační.</LI></OL>
<p>
První vzrušená rozprava týkající se tohoto projektu začala ihned u hledání jeho jména. V duchu tradic byla navržena zkratka - jenže Federal Educational and Research Network (<STRONG>FERNET</STRONG>) měla jak své skalní zastánce, tak odpůrce. Nakonec byl zvolen méně recesistický a více diplomatický název <STRONG>FESNET</STRONG> (Federal Educational and Scientific Network). Ovšem vinou politické situace neměl mít ani tento název dlouhého trvání. 
<p>
Záhy byla ustavena koordinační rada projektu FESNET a začala připravovat tehnickou koncepci páteřní sítě a zároveň hledala partnera a zejména také finančního garanta pro celý projekt. Tím se posléze stalo Ministerstvo školství, které v té době velmi předvídavě pochopilo význam celého projektu pro vzdělávací sféru. Finančí prostředky byly přislíbeny a mohlo se přistoupit k řešení praktických problémů. 
<H4>Technické řešení</H4>
<p>
Páteřní síť měla být budována výhraně na bázi pevného propojení a toto pevné propojení mělo být shopno přenášet více různých protokolů současně, aby bylo možno používat různé typy sítí. V tom panovala shoda. Již menší shoda ale panovala v tom, jak multiprotokolového přenosu dosáhnout. V zásadě byly uvažovány dvě koncepce: 
<BLOCKQUOTE dir=ltr style="MARGIN-RIGHT: 0px">
<H5>Protokol X.25</H5>
<p>
První koncepce předpokládala vybudování páteřní sítě na bázi protokolu X.25 a všechny ostatní protokoly pak "balit" při přenosu sítí do tohoto protokolu. Tato technika, nazývaná jako encapsulation, má svoji výhodu ve finanční nenáročnosti na hardware, nevýhodou ale byla značná režie na výpočetní výkon obstarávající "balení" a "vybalování". 
<H5>Protokol TCP/IP</H5>
<p>
Druhou zvažovanou variantou bylo vybudování páteřní sítě na bázi protokolu TCP/IP a na jednotlivých uzlech použít taková zařízení (routery apod), které by uměly pracovat a směřovat i jiné protokoly. </p>
</BLOCKQUOTE>
<p>
Řešení <STRONG>na bázi X.25</STRONG> odpovídalo evropskému standardu - vycházelo z filosofie a koncepce podobných páteřních sítí v Evropských státech, například sítí JANET ve Velké Británii, DFN resp. WIN v Německu a obecně i jiných datových evropských sítích. Vzhledem k tomu, že technologie pro X.25 již byla delší dobu na trhu, byla ověřená, relativně dostupná a v neposlední řadě zde byly nabídky i odborné pomoci či dokonce dodávky částí technologie se slevou i zdarma od zahraničních institicí, zejména z Německa. 
<p>
Řešení <STRONG>na bázi TCP/IP</STRONG> se prosazovalo zejména v USA, odtud se ale šířilo především díky rozšiřování internetu. Technologie vhodná pro nasazení na sítě TCP/IP je podstatěn dražší, než pro X.25, na druhou stranu byla již v té době technicky vyspělejší, když nabízela vzdálenou konfirugraci, automatické šíření směrových informací atd. Navíc v případě TCP/IP nemuselo docházet k žádnému "balení" jako u X.25, takže i režijní nároky na počítačový hardware byly nižší. 
<p>
<STRONG>Volba se tak zúžila na dvě varianta</STRONG> a to zjednodušeně takto: zvolit lacinější a méně perspektivní řešení, nebo jít do řešení dražšího, ale do budoucna otevřenějšího? 
<p>
Již v té době některé osobnosti zahraniční akademické sféry upozorňovaly na nepřehlédnutelné výhody TCP/IP do budoucna oproti již zastarávajícímu X.25 a tak i u nás po dlouhých odborných diskusích zvítězila varianta páteřní sítě s TCP/IP. 
<p>
Dnes, s odstupem několika let, je možno říci, že toto řešení bylo kromobyčejně šťastným. Valná většina evropských akademických sítí se již vzdala protokolu X.25 a například i ve Velké Británii, kde protokol X.25 měl v akademické sféře dlouhou tradici při nasazení v síti JANET, se při realizaci sítě Super-JANET přistoupilo k použití protokolu TCP/IP. </p>