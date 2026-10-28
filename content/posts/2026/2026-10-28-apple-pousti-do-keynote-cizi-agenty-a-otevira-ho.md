---
title: Apple pouští do Keynote cizí agenty. A z jednotlivých AI funkcí skládá asistenta
slug: apple-pousti-do-keynote-cizi-agenty-a-otevira-ho
author: Patrick Zandl
categories:
  - Apple
  - AI
summary_points: []
thumbnail: /assets/Apple-Creator-Studio-intelligent-assistant.webp
audio_url: ''
hide: false
---

_Kdo dělá prezentace v Keynote, mohl si o AI agentech jen číst. Formát souborů iWork byl pro ostatní nástroje uzavřený a AI v aplikacích se omezovala na jednotlivá tlačítka: vygeneruj obrázek, udělej slajdy z osnovy, doplň sloupec. Listopadová aktualizace Apple Creator Studia na tom mění dvě zásadní věci: externí agenti dostanou přes MCP přístup přímo do Keynote, Pages a Numbers a Keynote získá otevřený formát souborů čitelný pro stroje. K tomu přibude konverzační asistent postavený na modelech Applu a OpenAI, generativní úpravy obrázků a chytřejší Logic Pro. Kolik z toho uvidíte v Česku?_

Apple novinky oznámil 27. října 2026 v [tiskové zprávě](https://www.apple.com/newsroom/2026/10/apple-creator-studio-adds-powerful-new-ai-features-and-even-more-creative-tools/). Creator Studio je za předplatné, které Apple spustil letos v lednu: za 299 Kč měsíčně (2 990 Kč ročně, studenti a učitelé 69 Kč měsíčně) dostanete Final Cut Pro, Logic Pro, Pixelmator Pro, Motion, Compressor a MainStage a k tomu prémiové funkce do jinak bezplatných aplikací Keynote, Pages, Numbers a Freeform. Aktualizace přijde v listopadu a stávající předplatitelé ji dostanou zdarma.

***

## Agenti v kanceláři: MCP pro Keynote, Pages a Numbers

**Tohle je podle mne nejdůležitější zpráva celého oznámení.** Keynote, Pages a Numbers podporují Model Context Protocol (MCP). Jde o otevřený protokol, který v listopadu 2024 představil Anthropic a který slouží k propojení jazykových modelů s aplikacemi a daty. 

Podle Applu mohou externí agenti a nástroje číst obsah dokumentů, provádět úpravy a spouštět automatizované akce. Prakticky si to představuji tak, že Claude, Codex nebo jiný agent na vašem Macu otevře tabulku v Numbers, přepočítá ji, výsledky přenese do zprávy v Pages a z ní udělá prezentaci v Keynote. Bez exportů, kopírování a přeformátovávání. Tak, jako to nyní jde například v Excelu. 

Ovládat iWork zvenčí šlo i dřív, přes AppleScript. Ten ale musel někdo napsat a žádný jazykový model s ním nepracuje tak přirozeně jako s MCP, které dnes podporují všichni velcí hráči včetně Microsoftu a Googlu.

**Do iWorku to nepřišlo samo od sebe.** Apple chystá podporu MCP na úrovni systému od betaverzí macOS 26.1 (přes rámec App Intents, kterým aplikace systému popisují, co umí) a Safari v macOS 27 dostává vlastní MCP server. Keynote, Pages a Numbers jsou tedy první velké aplikace Applu, na kterých je ta strategie vidět. Čekám, že další budou následovat.

**Má to ovšem háček.** MCP v iWorku vyžaduje macOS 27 a na iPadu ani iPhonu zatím není. Apple ho v tiskové zprávě řadí mezi funkce pro předplatitele, výslovně ale nepíše, jestli bez předplatného fungovat nebude.

***

## Keynote otevírá svůj formát

Druhá novinka pro agenty je nenápadnější, ale dlouhodobě může mít větší dopad. Keynote dostává Keynote Interchange Format (.keyx), otevřený formát postavený na JSONu. Apple ho výslovně určuje pro externí nástroje, vývojáře a AI agenty.

Proč na tom záleží? Formát souborů iWork byl dosud pro cokoli mimo aplikace Applu prakticky nečitelný. Když jste chtěli nechat AI vygenerovat prezentaci, šlo to přes PowerPoint a následný import, při kterém se rozpadlo písmo, rozložení nebo animace. S formátem .keyx může model zapisovat přímo to, čemu Keynote rozumí.

A tady je příjemná zpráva: .keyx je **pro všechny uživatele**, bez předplatného. Zatím jako beta, takže bych na něm nestavěl nic, co se nesmí rozbít. Pokud ale stavíte nástroje na generování prezentací, máte nový cíl.

***

## Z tlačítek asistent

AI v iWorku není novinka. Writing Tools a Image Playground z Apple Intelligence tu jsou od prosince 2024 a Creator Studio v lednu přidalo generování prezentace z osnovy, poznámek pro řečníka, obrázků a tvarů a v Numbers funkci Magic Fill, která podle vzoru doplňuje data a vzorce. Šlo ale o jednotlivé funkce, každou na svém tlačítku.

Teď z nich Apple skládá asistenta, který rozumí obsahu otevřeného dokumentu a se kterým se dá mluvit. V Keynote pomáhá navrhovat slajdy, přidávat animace a dolaďovat prezentaci. V Pages píše koncepty, přeskupuje text a upravuje ho. V Numbers počítá, vytváří vzorce, doporučuje typy grafů s náhledem na jedno klepnutí a umí sestavit tabulku z obecných znalostí modelu (třeba seznam evropských metropolí s počtem obyvatel).

Podobný asistent přichází do Logic Pro pro Mac. Umí založit novou skladbu, připravit vokální stopu na základě jednoho promptu nebo poradit s rozpracovaným projektem. Pro začátečníky, kteří v Logicu bloudí mezi stovkami nastavení, to může být užitečnější než pro profesionály.

**Zajímavé je, co za tím stojí.** Apple píše, že asistenty pohání kombinace vlastních modelů a OpenAI. S OpenAI spolupracuje v iWorku už od ledna, generování prezentací běží na jeho modelech. Generování obrázků, tvarů a poznámek pro řečníka naopak podle [podpory Applu](https://support.apple.com/en-gb/127888) běží na Google Cloud. A ty „vlastní modely"? Apple a Google v lednu společně oznámili, že další generace Apple Foundation Models staví na Gemini. Které modely přesně asistent používá, Apple neuvádí, ale je dost možné, že se za značkou Applu skrývá kombinace Gemini a OpenAI. Apple tak nakupuje AI u dvou konkurentů zároveň a je z toho vidět, jak daleko má k vlastním špičkovým modelům.

**Pro nás je to zatím jen ukázka.** Oba asistenti jsou v betě, fungují jen v americké angličtině a vyžadují zařízení s podporou Apple Intelligence a systém verze 27. Asistent v iWorku navíc vyžaduje předplatné Creator Studia. Apple ho už zkusil pustit ve verzi 15.4.1 pro iPhone a iPad, aktualizaci ale krátce po vydání stáhl a asistent podle Macworldu nefungoval ani předplatitelům. Kdy přijde čeština, Apple neuvádí (a vzhledem k tomu, jak dlouho trvalo počeštění Apple Intelligence, bych nečekal zázraky).

***

## Generování a úpravy obrázků

**Pixelmator Pro dostává Generate Fill.** Pixelmator je původně litevská firma, kterou Apple koupil v roce 2024, a jeho editor je dnes součástí Creator Studia. Nová funkce funguje tak, že zakroužkujete část obrázku a popíšete, co v ní chcete změnit. Pro přesnější výběr můžete použít klasické nástroje pro výběr. Výsledek by se měl přizpůsobit osvětlení, perspektivě a textuře okolí, vygenerovaný obsah se automaticky zvětší, aby zůstal ostrý, a může se vložit jako nová vrstva s maskou pro další úpravy.

Je to obdoba funkce Generative Fill, kterou Adobe nabízí ve Photoshopu od roku 2023. Apple tu tedy dohání konkurenci se tříletým zpožděním. Pro uživatele, kteří nechtějí platit Adobe kolem 70 USD měsíčně, je to ale podstatný argument.

**Generování obrázků z textu** přibývá ve Final Cut Pro a v Motion, takže si můžete chybějící ilustraci nebo pozadí vytvořit rovnou v projektu. Freeform v prosinci dostane úpravy obrázků přes Pixelmator a generování upravitelných tvarů z textového popisu.

Na jakém modelu běží Generate Fill, Apple neuvádí. Generování obrázků v iWorku, Pixelmatoru a Freeformu už dnes pohání Google Cloud, takže lze čekat, že nové funkce půjdou stejnou cestou. Česko mezi vyloučenými zeměmi není, generování obrázků tu funguje.

***

## Hudba: co se pozná podle zvuku

Logic Pro dostává předělaný prohlížeč zvuků, který na jednom místě sdružuje smyčky, nástroje a efekty, včetně knihovny služby Splice (populární předplatné zvukových vzorků pro producenty). Zajímavější je funkce, kterou Apple nazývá „music understanding". Jde o analýzu zvuku běžící přímo v počítači, která sama roztřídí a otaguje vaše zvuky. Potom můžete hledat v celé sbírce, nebo do prohlížeče přetáhnout smyčku a nechat si najít podobné.

Tohle mi dává smysl víc než chatovací asistent. Kdo má na disku desítky gigabajtů vzorků, ví, že ručně je neotaguje nikdo.

Stem Splitter (nástroj, který z hotové nahrávky oddělí jednotlivé nástroje) teď umí oddělit i bicí a jednotlivé části bicí soupravy izolovat, nahradit nebo vyvážit. Funkce Voice Memo Studio Sound zase odstraní z nahrávek pořízených na iPhonu ozvěnu místnosti a šum na pozadí.

***

## Video: hlavně obsah, méně AI

Final Cut Pro na Macu dostává zabudovanou knihovnu MotionVFX. Jde o firmu, která dlouhodobě dělá šablony, přechody, titulky a efekty pro Final Cut Pro, a teď je v předplatném tisíce jejích prvků včetně nástrojů pro rotoskopii, sledování pohybu a barevné korekce. Content Hub (knihovna fotek a grafiky od Applu) nově obsahuje i video a je dostupný přímo ve Final Cut Pro a v iWorku.

Z AI pohledu je tu jedna drobnost: Final Cut Pro přidává přepis řeči ve 23 dalších jazycích, což usnadňuje titulkování a hledání v záznamech. Jestli mezi nimi je čeština, Apple nepíše.

***

## Co v oznámení chybí

**Kudy tečou data u asistenta.** U dosavadních funkcí Apple v podpoře popisuje, že požadavky jdou k OpenAI nebo Google Cloud bez vazby na Apple Account a bez IP adresy, poskytovatel je neukládá a nesmí na nich trénovat. U nového asistenta, který vidí celý otevřený dokument, Apple zatím nic podobného nezveřejnil. A ani u starších funkcí neříká, kde se data zpracovávají. Pro každého, kdo smluvně slíbil klientům, že jejich data neopustí EU, to bude první otázka.

**Bezpečnost MCP.** Když agent může v dokumentech číst, upravovat a spouštět akce, chci vědět, jaká oprávnění dostane, jestli se na ně aplikace ptá a jak se brání podvrženým instrukcím schovaným v dokumentu. O tom Apple zatím mlčí.

**Původ obrázků.** Na čem byly trénované modely pro Generate Fill a generování obrázků a jak jsou ošetřena autorská práva, se nedozvíme.

***

## Co si z toho odnést

Pro české uživatele bude od listopadu použitelná většina novinek: Generate Fill, generování obrázků, analýza zvuků v Logicu, formát .keyx a s macOS 27 také MCP. Mimo dosah zůstávají jen asistenti, kteří zatím mluví pouze americkou angličtinou.

Já jsem ze všeho nejvíc zvědavý na MCP. Asistent uvnitř aplikace je pohodlný, ale vždycky bude tak dobrý, jak dobrý model mu Apple zrovna koupí. Otevřené rozhraní znamená, že si do Keynote přivedete svého agenta a svůj model, a to je pro práci s dokumenty podstatně silnější. Jestli to Apple dotáhne i na iPad a nezamkne MCP za předplatné, bude iWork poprvé po letech zajímavý i pro lidi, kteří ho dosud brali jako bezplatný doplněk k Macu.

A za 299 Kč měsíčně je Creator Studio pro tvůrce, kteří nechtějí platit Adobe, čím dál rozumnější nabídka. Tečka.

***

_Zdroje:_ [_tisková zpráva Applu z 27. 10. 2026_](https://www.apple.com/newsroom/2026/10/apple-creator-studio-adds-powerful-new-ai-features-and-even-more-creative-tools/)*,* [_podpora Applu k AI funkcím Creator Studia_](https://support.apple.com/en-gb/127888)*,* [_9to5Mac k aktualizaci iWorku_](https://9to5mac.com/2026/10/27/apple-creator-studio-gets-powerful-new-ai-features-using-openai-models/)*,* [_9to5Mac k MCP v macOS 26.1_](https://9to5mac.com/2025/09/22/macos-tahoe-26-1-beta-1-mcp-integration/)*,* [_Android Authority k dohodě Applu s Googlem_](https://www.androidauthority.com/apple-siri-google-gemini-deal-3631890)*,* [_Apfelpatient ke stažené verzi 15.4.1_](https://www.apfelpatient.de/news/pages-keynote-numbers-ki-update-zurueckgezogen)*, české ceny podle* [_Letem světem Applem_](https://www.letemsvetemapplem.eu/?p=798421)*. Stav k 28. 10. 2026, aktualizace pro Mac vychází v listopadu a podmínky se mohou do vydání změnit.*
