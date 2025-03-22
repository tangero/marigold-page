---
ID: 1437
author: Michal Krsek
layout: post
oldlink: 'https://www.marigold.cz/item/story-o-sousedskych-sitich-13

  '
post_date: 2004-12-11 09:22:32
post_excerpt: ''
published: true
summary_points:
- Pražský CLOUD, autonomní systém, trpí útoky komerční firmy rušící WiFi spoje.
- Gubernátor CLOUDu nedokázal donutit firmu posílat agregované prefixy pro směrování.
- V CZFree.Net probíhají spory o definici CZF kvůli různorodosti členů a technologií.
- Otevřen byl první NCX bod Zápech, propojující dva CLOUDy pomocí switche.
title: "Story o sousedských sítích (13.)"
---

<p>
Když už nás Noname tak hezky popíchl, zkusím sesumírovat několik zajímavostí ze světa komunitních sítí(=CZFree.Net).<br/> <br/>Pohybuji se v pražském CLOUDu (což je de facto jeden autonomní systém), který je podle mého názoru ztělesněním anarachie, kdy duchovní vůdci (provozovatelé AP) dobrovolně respektují rozumná rozhodnutí gubernátora.  On je naštěstí rozumný, takže zjevné blbosti, které u duchovních vůdců narazí,  nijak netlačí. Takže například nastavení OSPF v jedné části CLOUDu vypadá tak, že výpadek okruhu je detekován až po čtyřech minutách - to aby nestabilní Linuxy měly dost času naběhnout po zresetování.</p>

<p>
Tento CLOUD se potýká s velkým problémem. Z jedné strany (ne z té naší) na něj útočí komerční firma, která provozuje vedlejší CLOUD. Firma vytváří svoje NODY v regionu &#8220;našeho&#8221; CLOUDu, což při nasazení WiFi ruší naše spoje. legrační jest, že náš gubernátor nebyl schopen firmu donutit, aby nám posílala agregované prefixy (doufám, že tam alespoň běží BGP),  takže naše směrovací tabulky jsou plné /24 sítí vedlejšího CLOUDu.</p>

<p>
Vůbec v CZF se začínají objevovat docela slušné hádky na téma, kdo a co je ještě CZF. Máme tady stav, kdy je gubernátor zároveň šéfem firmy, která prodává konektivitu (například xchaos nebo djdodo), máme tu občanská sdružení (zvláště mimo Prahu - například klfree.net nebo czela.net) a máme tady anarchistické bandy chaotů (jako je i náš CLOUD).  S tím, jak se zaplnilo WiFi pásmo a nejbližší další bez pochyb legální technologií je 10,5 GHz nebo optická pojítka, se projevuje technologické zaostávání  band chaotů. Domnívám se ovšem, že se skutečným uvolněním 5 Ghz pásma se situace zlepší. Ale nemyslí si to všichni (a můžete začít od začátku odstavce <img  alt="" src="/nucleus/plugins/wysiwyg/editor/images/smiley/msn/shades_smile.gif"/> ).</p>

<p>
Ale zdařilo se otevřít první NCX bod. Pravda, není to žádná převratná technologie - jeden switch, ale zase se podařilo zabránit tomu, aby propojovací centrum bylo PCčko s Linuxem, které bude konfigurovat deset lidí (najlépe najednou). Tento NCX bod je Zápech, zatím jsou do něj připojeny dva CLOUDy.</p>