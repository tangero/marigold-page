---
audio_url: http://www.marigold.cz/audio/2020-10-31-programovani_pro_pokrocile_deti_a_pro_ty_co_skutecne_zacinaji.mp3
audiooff: false
categories:
- "Programov\xE1n\xED"
- "Vzd\u011Bl\xE1v\xE1n\xED"
- "\u0160kolstv\xED"
date: 31.10.2020
excerpt: "M\xEDrn\u011B osobn\xED a sp\xED\u0161e brainstormovac\xED \u010Dl\xE1nek.\
  \ \u0158e\u0161\xEDm te\u010F pro syna Vojtu (10 let) programov\xE1n\xED. Chod\xED\
  \ (chodil, bo COVID) ve \u0161kole na  [Javorkovic krou\u017Eek programov\xE1n\xED\
  ](https://www.programovanihrou.cz/), skv\u011Bl\xE9. Jen\u017Ee v\u0161echno je\
  \ to takov\xE9 hran\xED. Scratch je skv\u011Bl\xFD pro men\u0161\xED d\u011Bti,\
  \ ale skute\u010Dn\xE9mu programov\xE1n\xED se tam jen p\u0159ibl\xED\u017E\xED\
  te. Tak\xE9 s Microbitem je z\xE1bava, Vojta tady t\xFDden p\u0159eprogramov\xE1\
  val hry Scratch hry, aby je mohl ovl\xE1dat sv\xFDm vlastn\xEDm ovlada\u010Dem postaven\xFD\
  m na desce Microbitu. Skv\u011Bl\xFD seznam materi\xE1l\u016F pro prvn\xED stupe\u0148\
  \  [vytv\xE1\u0159\xED Miroslav Such\xFD](https://github.com/xsuchy/programovani_pro_deti/),\
  \ doporu\u010Duji tam zapo\u010D\xEDt studium t\xE9matu. Ale taky se to \u010Dasem\
  \ omrz\xED. A tady p\u0159ich\xE1z\xED probl\xE9m. Je velk\xE1 mezera mezi *hrac\xED\
  m* programov\xE1n\xEDm a t\xEDm *skute\u010Dn\xFDm*?"
layout: post
summary_points:
- "Scratch a Microbit jsou z\xE1bavn\xE9, ale nenau\u010D\xED skute\u010Dn\xE9 programov\xE1\
  n\xED."
- "Velk\xE9 programovac\xED jazyky jsou pro d\u011Bti neintuitivn\xED a slo\u017E\
  it\xE9."
- "Chyb\xED mezistupe\u0148 mezi hrav\xFDm a profesion\xE1ln\xEDm programov\xE1n\xED\
  m."
- "Low-code a no-code platformy jsou drah\xE9 a cloudov\u011B z\xE1visl\xE9."
title: Programov\xE1n\xED pro pokro\u010Dil\xE9 d\u011Bti a pro ty, co skute\u010D\ n\u011B za\u010D\xEDnaj\xED
---

Mírně osobní a spíše brainstormovací článek. Řeším teď pro syna Vojtu (10 let) programování. Chodí (chodil, bo COVID) ve škole na  [Javorkovic kroužek programování](https://www.programovanihrou.cz/), skvělé. Jenže všechno je to takové hraní. Scratch je skvělý pro menší děti, ale skutečnému programování se tam jen přiblížíte. Také s Microbitem je zábava, Vojta tady týden přeprogramovával hry Scratch hry, aby je mohl ovládat svým vlastním ovladačem postaveným na desce Microbitu. Skvělý seznam materiálů pro první stupeň  [vytváří Miroslav Suchý](https://github.com/xsuchy/programovani_pro_deti/), doporučuji tam započít studium tématu. Ale taky se to časem omrzí. A tady přichází problém: je velká mezera mezi „hracím“ programováním a tím „skutečným“?

Abych to objasnil. Nejsem programátor. Moje programování skončilo u Fortranu, Pascalu a Assembleru. Znám Python, PHP, ale nikdy jsem v nich rutinně nic nedělal, používal jsem je, když vznikaly, asi před sto lety. Pokud si prohlížím cizí kód, chápu čistotu kódu, strukturu i samotný kód, ale už mám problémy řešit framework či knihovny, protože je konkrétně neznám. A to začíná být dnes problém: velká část viditelného programování je správné volání správných kódů, které vytvořil někdo jiný. Pokud je neznáte, jste namydlení. Pokud nevíte, že Flask nebo Django, tak si s pythonem moc webů nenakreslíte. Abych byl přesný: jasně, že to jde, ale  [vynaložíte neúměrně síly](https://realpython.com/python-web-applications/#static-web-app), což vás rychle omrzí.

### Velké jazyky jsou pro mládež neintuitivní

Teprve, když se podíváte na vývoj aplikací očima dětí, pochopíte, jak neintuitivní to je. Nejde o to, že se musíte naučit příkazy, ty jsou vcelku pochopitelné. A vlastně všude stejné, FOR je FOR od Fortranu a Cobolu přes C++ až po Haskel.  _Kecám, v Haskelu je to jinak, ale co naděláte, není to procedurální jazyk…_

Tak například de-facto standardní GUI v Pythonu je TKINTER. Potřebujete to vědět  _(z čeho byste to jméno odvodili, jako u FOR cyklu z angličtiny?)_  a zavolat jej. Podívejte se někdy na začátek programu, ve kterém používáte tkinter, django nebo turbogear. Začátek zápisu je hodně nesrozumitelný, což vám s lety praxe samozřejmě nepřijde a uvědomíte si to až se zvídavou otázkou dítěte.

Ve výsledku se mi zdá, že chybí nějaký mezistupeň mezi Scratchem a vyššími programovacími jazyky. Takový, který by umožnil dosahovat rychle přiměřených výsledků a byl intuitivní. A dost možná nebyl založený na otrockém textovém zápisu.

Rozumějte: udělat webovou stránku by mělo být průchozí i bez abstrakce do tří vrstev – to je přeci jen míra abstrakce dětem nemilá. Ano, vím,  [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/from-scratch.html). To je vlastně nejblíže tomu, co jsem myslel. Umožňuje to tvořit dostatečně důstojně daleko od Scratche a přitom se držet na mělčině.

### Low-code a No-code

Proč o tom vlastně píšu? Delší dobu se zájmem pozoruji posuny v low-code a no-code hnutí. Myšlenka osvobodit programování od datlování příkazů  [je samozřejmě dobrá](https://medium.com/swlh/why-low-or-no-coding-is-the-future-of-programming-38f59b907e22)  z mnoha pohledů, od omezení chybovosti, po zpřístupnění širším masám. Její limity ponechme stranou, ty jsou od toho, aby se odstraňovaly. Low-code a No-code platformy ovšem nejsou standalone záležitosti, jde zpravidla o striktně cloudové záležitosti, které je třeba platit, i když váš kód neběží a až na výjimky nejde o levné záležitosti ([Outsystems](https://www.outsystems.com/pricing-and-editions/)  je na hraní levný).

Co s tím? Zatím není mnoho dalších cest, snad zkombinovat low/no-code záležitosti s [transcodery](https://github.com/facebookresearch/TransCoder)  (proč asi do nich investuje Facebook) a nechat je generovat cílový kód, ale to se zase míjí s oblíbenou momentální módou lidi nechat platit za cloudy a služby v nich

### My jsme začínali od píky, ale za nás všechno to vznikalo

Je to tak. Když já jsem začínal s Pythonem, neexistovalo Django. Když přišlo, byl to pomalý nástup, který jste snadno vstřebali. Když se dnes posadíte před Python 3.9, sedíte před strašlivě široce rozkročeným jazykem, který lze použít od frontendu, přes backend až po mikrokernel. Je těžké začít a mít výsledek, který by přesvědčoval, že to dává smysl, když vstupujete do takhle širokého proudu řeky.

Moje zkušební aplikace? Poznámkový webový bloček, ve kterém si napíšete řádek textu, co jste právě udělal, přidáte tag, datum a čas a kolik jste tomu věnovali minut. A z druhé strany si to podle těch kritérií můžete vypsat. Work-log. Vlastně nemůže existovat triviálnější úloha. V Excelu nebo Google Sheet za minutu. Za jak dlouho ji uděláte ve vašem jazyce tak, aby vypadala rozumně a nebyl to trapný command prompt? Kolik kódu budete muset vytvořit a kolik ho přilinkujete?

Odpověď na otázku onboardingu do programování je přitom důležitá. Pozice programátora je povoláním nejbližší budoucnosti, jenže není efektivní, aby každý programátor měl znalosti na úrovni PhD. Ve skutečnosti většina programátorů jsou učňovské profese, stačí dobře zvládnout řemeslo. K němu ale potřebujete nástroje, jak učební, tak produkční. Zdá se mi, že tohle chybí a bude důležité pro cenovou efektivitu, jak se nám podaří problém vyřešit tak, aby běžná dvacetiletá mládež mohla programovat tak, jako kdysi mohla řezat dřevo.

Výsledek? Pomalu se proklikáváme Pythonem, já pošilhávám po [Elixíru](https://elixir-lang.org/)  /  [ELM](https://elmprogramming.com/)  či [Julii](https://julialang.org/), jen tak pro svoji duševní hygienu a s otázkou, zda by to dětem nevyhovovalo lépe. Ale ta propast, ta je patrná. Děti se snadno nalákají na možnosti programování, ale pak se výsledky nedostavují dostatečně rychle, ačkoliv k tomu není velký důvod. Už s malým úsilím by se daly dělat dobré webové aplikace, byť třeba unifikovaného vzhledu. Takhle se člověk snadno dostane ke vstupu z příkazové řádky, ale další kvalitativní posuny vyžadují velký znalostní skok kupředu, pro děti příliš těžké.

Samozřejmě je možné nechat to do věku patnácti, dvaceti let, kdy možnosti abstrakce i znalosti tuhle propast dotáhnou, ale připadá mi to škoda.

_Pokud máte nějaké myšlenky a tipy, dejte vědět. Možná jsem jenom něco neodhalil, možná se na to dívám špatně._

_PS: Ano, očekávám, že opravdoví programátoři budou zděšeni. Jak by někdo mohl nevědět, jak se používá Django! A ať se to sakra naučí, když už se to museli naučit i oni!!! Jenže…_