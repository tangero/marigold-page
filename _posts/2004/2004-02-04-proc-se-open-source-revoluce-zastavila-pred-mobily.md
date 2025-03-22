---
ID: 832
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/proc-se-open-source-revoluce-zastavila-pred-mobily

  '
post_date: 2004-02-04 07:41:00
post_excerpt: ''
published: true
summary_points:
- Open-source revoluce v IT se zastavila před mobilními technologiemi.
- Důvodem absence open-source v mobilech je složitost hardwaru a frekvencí.
- Softwarově definované rádio a vyšší vysílací výkony jsou klíčové pro open-source
  mobily.
- P2P open-source mobilní sítě čekají na svého Linuse a uvolnění frekvenčního pásma.
title: Proč se open-source revoluce zastavila před mobily?
---

<p>
Na máločem se lze v IT shodnout, ale snad každý připustí, že open-source způsobilo v IT výrazné změny, jež by se daly nazvat i revolucí. Můžeme debatovat nad tím, zda jsou změny k lepšímu (svoboda, transparentnost, zrychlení vývoj&#160;peníze) nebo k horšímu (hackeři, zpomalení vývoje, ohrožení stability hospodářství), ale to je tak všechno. Jenže <STRONG>proč se u všech čertů zastavil open source před mobily?</STRONG> Neříkejte mi, že kohokoliv s open source komunity dojímají nějaké uzavřené standardy jako GSM, CDMA nebo UMTS a že kohokoliv z programátorů trápí to, že by museli vyvýjet řešení obcházející či nahrazující něčí patenty. </p>

<p>
Myslím, že dojetí zavedenými standardy si můžeme škrtnout a v zásadě tu máme dvě další možnosti, proč open source zatím mobily pominul:</p>

<UL>
<LI>nutná hardwarová platforma, která má daleko ke standardu podobnému PC</LI>
<LI>nutná alokace frekvencí, ideálně bezlicenčních a bezadministrativních, což byl donedávna problém</LI></UL>
<p>
<IMG height=209 alt="WiFi telefon od Pulver inovation" src="/wp-content/uploads/wifitelefon.jpg" width=195 align=right border=1>Oba problémy se řeší. Bezlicenční frekvence v pásmu 2,4 a 5GHz jsou alokované a volně přístupné, jen ty vysílací výkony jsou zde trochu na prd pro účel plošných mobilních aplikací. I hardwarová platforma je na pochodu - založená na WiFi. Například telefon na straně je něco jako bezdrátový telefon, jenže místo DECTu je vybavený WiFi a podporou SIP. Stačí se k ním připojit kdekoliv k WiFi síti a volat přes svého VoIP operátora podporujícího SIP, což jsou dnes prakticky všichni vyjma Skype a Fayn.</p>

<p>
Celá ta hračka má samozřejmě svoje omezení - má malý dosah a <STRONG>neprovedete s ní žádný handover</STRONG> na jinou základnovou stanici. Jenže <STRONG>technologie handoveru je až zatraceně prostá</STRONG> a není to nic, co by pár tisíc řádků zdrojáků nevyřešilo. Tak kde to vázne?</p>

<p>
Hardwarová platforma by přeci jen měla vypadat nějak jinak - ideálně by mělo jít o <STRONG>softwarově definované rádio</STRONG>, tedy WiFi podpora by v něm neměla být natvrdo, ale celá <STRONG>aplikace pro radiovou vrstvu by se tam nahrávala</STRONG>. Přijde se zítra na něco lepšího než WiFi? Downloadujte si update svého telefonu. Dále by bylo potřeba, aby ta platforma mohla pracovat s <STRONG>vyššími vysílacími výkony</STRONG>, aby uživatelská stanice mohla mít tak alespoň jeden watt a základnová stanice tak alespoň deset wattů. To už znamená požadavek na přidělení jiného frekvenčního pásma a aby se návrháři takové sítě nezezelenali z frekvenčního plánování, obnášelo by to také použití nějakého radiového rozhraní, které <STRONG>nepředpokládá nutost frekvenčního plánování</STRONG>, třeba jako je CDMA <EM>(zatížené nechutnými patenty, ale což, v základu je stejně bude umořovat výrobce techniky).</EM> </p>

<p>
Tím by se zájemcům dostal na stůl <STRONG>"prázdný telefon"</STRONG> - krabička vybavená displejem a tlačítky, do které je třeba nasypat firmware, tedy obdoba PC, na které si instalujete Linux nebo něco podobného. Pak už by bylo na open source komunitě, jak by se takové možnosti chytla, nevěřím ale tomu, že by se jí nepodařilo vyvinout a nakódovat celou mobilní síť s handoverem, s výstupem na telefonní síť a to všechno decentralizovaně na bázi P2P. Jste telekomunikační odborník a vstávají vám vlasy hrůzou na hlavě? Nevěříte tomu, že se taková věc dá udělat bez signalizace v reálném čase a synchronizace času? Věřte tomu, dá. Jen při handoveru vám telefon zapípá do sluchátka, že hovor je přidržen do provedení handoveru, což vzhledem k tomu, že hovoříte zadarmo s kámošem na druhé straně města, tak nějak přežijete... </p>

<p>
<STRONG>Open-source mobilní sítě založené na P2P architektuře</STRONG> jen čekají na svoje objevení. Hardware pomalu začíná být připravené, osobní počítače mají dnes podobný výkon, jako gigantické tranzitní ústředny před dvaceti lety. Tyto sítě čekají na svého Linuse, který nakóduje základní aplikaci a <STRONG>s charisma čaroděje ji protlačí do celého světa</STRONG>. Nejprve - a pohříchu - na WiFi, o čtyři roky později do volného pásma, které WRC uvolní, protože tlak příznivců bude příliš velký, než aby se mu dalo odolávat. <EM>Přijde hype.</EM>&#160;To už budou na trhu tři roky čínské výrobky a Siemens zrovna vydal tiskovou zprávu, že hodlá nabídnout ucelenou řadu hardware pro softwarově definované mobily. <EM>A to bude právě ta chvíle, kdy bude šéf Hutchinsonu stát na parapetu okna ve svém hongkongském mrakodrapu, ještě se ohlídne na exekutory vynášející nábytek (splácejí se jím UMTS sítě), než...</EM></p>

<p>
Ale vážně. <STRONG>P2P mobilní sítě budou zajímavá záležitost</STRONG> a já se těším na to, že se jí dočkám. Do deseti let přijdou a jestli někoho nepotěší, tak to budou mobilní operátoři, stejně jako VoIP netěší pevné telefonní operátory a jako Linux nepotěšil Microsoft...</p>