---
ID: 1354
author: Patrick Zandl
categories:
- UMTS
- 3G
- Turboúvod do mobilních sítí
layout: post
oldlink: 'https://www.marigold.cz/item/turbouvod-do-umts-ims-aneb-ip-multimedia-subsystem

  '
post_date: 2004-10-08 11:44:28
post_excerpt: ''
published: true
summary_points:
- UMTS Release 5 integruje All-IP koncept IMS pro paketový přenos dat, hlasu a obrazu.
- IMS v UMTS posouvá síť k bezdrátovému modelu s protokoly SIP a IPV6.
- IMS dělí okruhovou doménu na Media Gateway a MSC server pro efektivnější směrování.
- IMS zatím není vhodný pro realtime aplikace, ale pro Push To Talk služby.
title: 'Turboúvod do UMTS: IMS aneb IP Multimedia Subsystem'
---

<p>
Sliboval jsem minule, že se podíváme, jak by bylo možno přidat poměrně obstarožnímu UMTS Release 99 na rychlosti přenášených dat a přitom se pokusit redukovat počet krabic v schématu sítě, o kterých jsme si ještě ani neřekli, že existují. </p>

<p>
Na další radikální změny v UMTS jsme si museli počkat až do Release 5. Dejme si nyní malou odbočku k číslování UMTS specifikací. Nebojte, jen malou, našel jsem svůj text, který jsem na to téma napsal (a nepublikoval), je to stránka hutného textu, jak rozumět číslování specifikací UMTS. Někdy to postnu, to ale už není pro blázny, spíš pro magory. </p>

<p>
Jak jste si všimli, UMTS Release coby označení specifikace se číslují nějakým hypotetickým datem, ke kterému je standard uzavřen. Na příkladu Release 99 (uzavřenému v roce 2000) jsme si také ukázali, že číslo vyjadřuje spíše zbožné přání o roce, ke kterému má být standard uzavřen, než realitu, pár měsíců ale nehraje ve standardizaci roli. Po Release 99 následuje jako další skutečná Release 4. Číslo 4 označuje letopočet, jenže protože Release 0 za rok 2000 neexistuje, počítá se to od jedničky a tak je třeba jedničku odečíst. Release 4 byla projednávána v roce 2003, Release 5 je projednávána v roce 2004 s uzávěrkou v září. Release 0 až 2 neexistují, číslice 3 se používá pro Release 99, pokud se uvádí v desetinném tvaru při číselném zápisu specifikace. Nejnověji plánovaná je Release 6, která se bude projednávat v roce 2005 a přesouvají se do ní všechny změny a návrhy, které se už v Release 5 nestihly projednat. Konec poučky o číslování.
</p>

<!--more--><p>
Povšimli jsme si již, že UMTS síť je stále rozdělena prakticky na dvě části, na síť paketovou a okruhově spínanou. Zatímco paketovou sítí běhají data, okruhově spínanou sítí běhají vyhrazené datové okruhy (něco jako je HSCSD nebo normální vytáčené připojení v GSM sítích) a hlavně normální telefonní hovory a také videotelefonáty. </p>

<p>
Na tomto příkladu je vidno, jak starý je návrh Release 99. Na konci devadesátých let bylo už dávno zřejmé, že přenášet videohovory přes spínaný okruh, který zabere kapacitu čtyř hovorových kanálů, je trochu out-to-date. A stejně to tak UMTS realizuje, namísto toho, aby videohovor protlačilo přes paketová data. </p>

<h4>IMS aneb IP Multimedia Subsystem</h4>
<p>
Jenže heslem moderní doby je All-IP, tedy všechny záležitosti v síti protlačené pod IP vrstvou jako paketová data. A to si přečetli v nějakém tom moderním časopise i standardizátoři UMTS a tak Release 5 obsahuje převedení veškerého provozu do režimu All-IP. Pro zmatení protivníka se tento koncept jmenuje IP Multimedia Subsystem (zkráceně IMS) a snaží se tím názvem vyjádřit fakt, že veškerá data i multimediální záležitosti jako hlas a obraz napříště v UMTS síti poputují paketově.  A protože paketový a okruhově-spínaný provoz se v UMTS označuje jako dvojice provozních domén, přibyl IMS jako třetí doména. </p>

<p>
Celá myšlenka je značně ušlechtilá, když se na UMTS ale nyní podíváte, tak celou síť v podstatě posouvá do roviny takové větší WiFi sítě s připojenou rychlotiskárnou faktur a ústřednou. Převedením celého provozu na IMS se totiž UMTS posouvá z oblasti mobilních sítí do oblasti sítí bezdrátových. Mimo jiné vsází i na standardní protokoly bezdrátových sítí jako je SIP pro přenos hovorů a IPV6 pro adresaci. Pro spravedlnost je třeba říci, že IPV6 přijde později, ranná fáze počítá s IPV4 a přechodem na IPV6. </p>

<h4>UMTS okleštíme na bezdrátovou síť</h4>
<p>
Je to pro vás kacířská myšlenka? Ona je ale docela reálná, protože takový je i okolní tlak. Co se týká hlasového provozu, bohatě totiž postačují současné GSM sítě a pokud se UMTS má nějak uživit, mělo by nabízet rychlá data, skutečně rychlá data v řádu sdílených megabitů nebo spíše desítek megabitů. A také musí nabízet přijatelné zpoždění a rozptyl dat při přenosu. Zatímco rozptyl se daří v UMTS stabilizovat podporou QoS, s tím zbytkem by byl problém. Zpoždění totiž v UMTS nabíhá na autorizačních mechanismech, což je většinou jednorázová záležitost při sestavování spojení a pak na průchodu přenášeného toku příliš mnoha aktivními prvky, které jej nějak zpracovávají a na tom nabírají zpoždění. Když jsem to jednou počítal, tak průměrně projde datový tok v klasickém UMTS Release 99 zhruba čtrnácti skoky v síti, přičemž na každém nabere přes 10 ms zpoždění.  Na mobilce udělá dalších 20-50 ms a dostáváme se k hranici >200 ms reálného zpoždění při přenosu dat jen v UMTS síti. To ale UMTS data diskvalifikuje z takových radovánek, jako je online hraní her, protože realtime pařby potřebují latenci do 100 ms. </p>

<p>
Kombinace hlasového provozu na bázi okruhů a paketových dat tedy kapacitě UMTS sítě neprospívá, ostatně i s ohledem na to, že většina (potenciálních) UMTS operátorů vlastní GSM licence a může tedy hlasový provoz pokrýt přes GSM. Větší výjimkou je snad jen operátor 3.</p>

<h4>S IMS jsou i potíže</h4>
<p>
Nevýhodou je, že IMS má ve standardu několik fází a to, o čem jsme si povídali doteď, je spíše výhled do budoucna, než to IMS, jak je implementováno v Release 5. Doposud standardizované IMS zatím není vhodné pro nějaké velké realtime aplikace, k tomu se dopracuje zřejmě až v Release 6. Pro IMS Release 5 se počítá spíše se službami typu Push To Talk over cellular, tedy službami, které nejsou náročné na zpracování v reálném čase, než s videotelefonáty, které real-time zpracování potřebují. Takže je to zatím jen další hrůza navíc. </p>

<h4>IMS v síti</h4>
<p>
Podívejme se, jak IMS vypadá v UMTS síti. Přestavbu provádí IMS v okruhové doméně, v níž rozděluje ústřednu (MSC) na dvě části – Media Gateway (MGW) a MSC server, do budoucna stále označovaný jako MSC, tedy ústředna. Na obrázku MSC není, protože obrázek zakresluje jen vztah mezi paketovou a IMS doménou. Řídící logika zůstává na MSC serveru, zatímco MGW přejímá samotné spínání, tedy přenos dat. Oddělení řízení od samotného datového provozu dovoluje síti využívat efektivnější směrování pro vysokorychlostní data, neboť malé řídící povely se přenášejí jinou cestou a nemíchají se s velkými objemy dat. </p>

![IMS architektura](/assets/20041008-ims.jpg)

<p>
Z hlediska konstrukčního se předpokládá, že MSC i MGW může být dodáváno ve společném fyzickém provedení nebo odděleně a to v závislosti na tom, jak se dodavateli podaří ne/vyřešit upgrade stávajícího MSC u operátora. </p>

<p>
K IMS navíc přistupuje celá řada dalších aplikačních serverů poskytujících nejrůznější služby, jako jsou PTT, herní platformy, chaty, sdílení dat a další. </p>

<p>
IMS jsme probrali jako malou odbočku, protože zatím se v praxi neprosazuje, jednou by ale mohla být zajímavým tahounem pro sjednocování a zjednodušování služeb v UMTS sítích a šetření jejich kapacity. </p>

<p>
Příště se snad konečně dostaneme k tomu, proč a jak zrychlují data v UMTS.
</p>