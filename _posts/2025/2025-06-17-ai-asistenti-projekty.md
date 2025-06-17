---
author: Patrick Zandl
categories:
- AI
- AI asistent
layout: post
post_excerpt: V AI existuje celá řada postupů, které se snaží pomáhat s automatizací práce i neprogramátorům. Jsou to především Projekty, GPTs a GEM od všech tří hlavních firem nabízejících LLM. Souhrnně jim říkejem asistenti. Pojďme si ukázat, jak můžete vytvořit asistenty pro opakující se úkoly.
thumbnail: https://www.marigold.cz/assets/ai-asistenti.png 
title: "Asistenti, Projekty, GEMy, GPTs a základy automatizace práce pomocí AI"
---


V AI existuje celá řada "technologií", které se snaží pomáhat s automatizací práce i neprogramátorům. Jsou to především Projekty, GPTs a GEM od všech tří hlavních firem nabízejících LLM. Souhrnně jim říkejem asistenti. Pojďme si ukázat, jak můžete vytvořit asistenty pro opakující se úkoly.

Tak za prvé, nejsou to agenti. Agenti fungují samostatně. Asistenti jsou vám k ruce a na váš příkaz něco dost predikovatelného udělají, ale nerozpoutají při tom třetí světovou ani v scifi knížce. Ve skutečnosti se asistenti u jednotlivých firem jmenují různě a my si v tom dneska trochu děláme pořádek.

### Projekty v ChatGPT a Claude

Pokud si platíte za ChatGPT nebo Claude, jistě jste si všimli záložky Projects - Projekty. Ještě před týdnem byla jejich užitečnost rozporuplná, ale minulý týden jak Antrhopic, tak OpenAI provedly podstatné updaty, mezi něž patří hlavně dostupnost moderních LLM v Projektech - do té doby tam byl k dispozici jen model 4o. Nově si můžete vybrat i přemýšlecí model o3, 4.1 a 4.5 - to je dost silná sestava.

**K čemu Projekty slouží?** Já je používám k opakujícím se úkolům, které chci jen pro sebe. Tak například mám projekt Thumbnaily pro Marigolda, který mi slouží k tomu, aby mi AI připravila obrázek na titulní stránku Marigolda a já se s tím nemusel dělat v grafickém editoru.

### Jak asistent funguje? 

Založím si nový projekt v ChatGPT a vytvořím pro něj prompt, který si vyladím. Vždycky, když pak chci vygenerovat úvodní obrázek pro svůj blog, jdu do projektu a prompt mě provede tvorbou obrázku, čili se doptá na věci, které potřebuje vědět.

Jak takový prompt vypadá? Tady je jeho příklad. Pevně jsem definoval barvy, které se mají používat, když použijete slovní popis, tak bude LLM střílet rozdílné barvy v jednotlivých generováních. Definoval jsem, co se má na úvodním obrázku vytvořit.

        Vytvoř grafiku ve formátu, který ti určím. 
    
    Pokud chci formát thumbnail, vygeneruj strannový poměr obrázku 3:2 tedy 600 x 400 pixelů.
    Pokud neznáš některá z požadovaných následujících dat, zeptej se mě tato data. 
    
    DATA
    ----
    • Název článku: "{title}"
    • Krátké shrnutí (max 40 znaků): "{excerpt}"
    • URL podkladu: {podklad_url} nebo požádej o téma k vygenerování
    • Jako logo projektu (avatar) si vyžádej obrázek
    
    
    POŽADAVKY NA OBRAZ
    ------------------
    1. Rozměr: {dimensions} px, 300 DPI, RGB.
    2. Umísti podklad přes celou plochu; zachovej kompozici tak,
       aby klíčový motiv nebyl zakryt textem.
    3. Přidej poloprůhledný overlay barvy #1D1D1F s neprůhledností {overlay_opacity}%.
    4. Logo projektu (avatar) vlož do spodního pravého rohu; průměr ≈ 18 % šířky.
    5. Headline vlož do {headline_box_position}; písmo Poppins Bold,
       velikost adaptivně, barva #FFFFFF, zarovnat na střed.
    6. Podheadline (excerpt) pod headline, Poppins Medium, barva #FFFFFFAA,
       menší velikost, max 1 řádek.
    7. Přidej call‑to‑action text "{cta_text}" v pravém dolním rohu,
       Poppins Medium, velikost 28 b, barva #CABBA0.
    8. Udržuj čistý, tech‑friendly styl, žádné další ozdoby
       (stíny, outline, emodži apod.).
    9. Exportuj jako PNG.
    
    VÝSTUP
    ------
    Popiš výsledný layout (pro kontrolu) a přilož odkaz ke stažení obrázku ve formátu PNG.


Jedním zádrhelem tohoto příkladu je použití avatara, tedy ikonky serveru, kterou používám na obrázku. Projekty mají způsob, jakým se mohou odkazovat na soubory, které jste si do nich uložili, a to */mnt/data/jmenosouboru.pripona* - jenže tyto soubory nelze zobrazovat, jen použít při zpracování. Což znamená, že by mělo být možné v rámci Projektu nahrát si předem ikonku, která se do úvodního obrázku přidá. Bohužel, když ji přidáte mezi soubory projektu, to tak zatím nefunguje a není úplně zřejmé, proč. Zatím je tedy řešením při prvním generování obrázku avatara nahrát ručně a pak se na něj jen odvolávat. Pokud máte v Settings nastaveno, že jednotlivé chaty vidí svoje data, můžete se takto odvolávat na avatara i při generování dalšího obrázku. 

Chcete-li v projektech povolit plnou funkčnost paměti, ujistěte se, že jsou v nastavení zapnuty funkce *Odkazovat se na informace uložené v paměti* i *Historie referenčního chatu* v *Personalizace / Přizpůsobení*

Možná se ptáte, **proč nepoužít rovnou prompt, jaká je výhoda v tom, používat Projekty?** 

**První důvod je jednodušší organizace** - Projekty a jejich chaty jsou vidět hned na prvním místě a nemusíte zoufale hledat, kde jste ten prompt měli, když ho chcete znovu použít. To za prvé. 

**Za druhé můžete v novém chatu vždy odladit pohodlně** nový obrázek (napoprvé se asi nepovede nebo nelíbí) a nemusí se vám to plést s předchozími obrázky, které máte v tom samém chatu. Navíc LLM má tendenci to pak všechno zmastit dohromady. 

Každý uživatel může vytvářet neomezený počet projektů (každý až s 20 soubory, s ohledem na omezení sazby předplatného). Pokud s Projektem v ChatGPT skončíte, můžete jej odstranit kliknutím na nabídku se třemi tečkami vedle názvu Projektu. Tím se trvale vymažou všechny konverzace, soubory a vlastní pokyny. Je dobré odstranit nepotřebné chaty a soubory, abyste měli jistotu, že vám nikdy nedojde místo. Po smazání je obsah do 30 dnů vymazán, proto si nezapomeňte zálohovat vše důležité.

Co je důležité si pamatovat? 

Především: soubory poskytnuté jako Znalosti v Projektu jsou používány primárně a cituje se z nich. Čili pokud se bojíte, že vám LLM něco vyhalucunuuje, není se toho bát, pokud je správná odpověď v poskytnutých dokumentech. 

Můžete si do Projektu přesunout i vlákna, která jste dříve otevřeli mimo projekt a tím se stanou jeho součástí. 

Jakmile se chat nachází uvnitř projektu, převezme prioritně vlastní pokyny tohoto projektu a může odkazovat na všechny nahrané soubory. To vytváří souvislé vlákno kontextu, které pomáhá ChatGPT poskytovat chytřejší a konzistentnější odpovědi. 

To také znamená, že můžete projektu nařídit, být komisnější, nebo naopak uvolněnější, než je tomu v "hlavním" chatu, tedy mimo projekt. Díky tomu si můžete pohrát se slovníkem a způsobem vyjadřování a přizpůsobit si zcela tón v rámci projektu, aniž byste tím měnili tón hlavního chatu. Pokud si tak necháváte zpracovávat marketingové materiály, můžete si tak držet různé způsoby komunikace v samostatných projektech. 

A nejde jen o styl, já například používám různé projekty pro různé formáty odpovědí, pokud si je přesně specifikuji, například rovnou v markdown nebo CSV formátu. 

O tom, jak si vytvořit pomocí promptu specifické styly vyjadřování, si řekneme blíže něco příště.

**Stejnou strukturu práce má Claude Project** - jenže Claude narozdíl od ChatGPT neumí moc s obrázky, může řešit jen diagramy a nákresy ve formátu SVG. Proto je na tyto kombinované záležitosti méně nevhodný a užitečný je spíše tam, kde se pracuje jen s textovými daty.

Velkou výhodou Claude naopak je použití mechanismu RAG. [RAG je způsob](https://support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects), jak obejít velikostní omezení kontextu, tedy velikost dat, které lze do chatu (a do Projektů) podstrčit. Donedávna byl Claude Projekt omezený velikostí kontextu, tedy na 200 000 [tokenů](/ai/tokeny-versus-slova/), cca 100 000 slov v češtině, což není zase tak moc. Nemohli jste například do Projektu nahrát dvě knihy, stěží se vešla jedna. Od června 2025 ale má Claude podporu RAG, což je inteligentní způsob, jak z nahraných dokumentů vybrat kontext, který je potřeba. Není to tedy úplně přesně to, že by veškerý text byl součástí kontextu, ale RAG má mechanismus, jak vybrat z předložených dokumentů těch 200 000 tokenů, které se vztahují k tomu, co děláte. Má to sice svá omezení, ale je to dobré. Jak to nyní používám já? Například mám v projektu nahraných několik knih věnovaných obrazům a pokud si chci nechat zhodnotit nějaký obraz, Claude mi v projektu provede zevrubnou kritiku podle názoru nejrůznějších kunsthistoriků. Tuto vlastnost naopak nemá OpenAI ani Google Gemini, jeho modely ale umí až 1 milion tokenů kontext. Kolik dokumentů přesně můžete nahrát, záleží - kolem 2 milionů tokenů. Proč je to důležité? Pokud potřebujete zpracovávat větší množství dat, je Claude Project prostě lepší.

Poněkud **problém je ve sdílení Projektů**. 

ChatGPT sdílení má řešení pro Projekty stejně, jako pro každé jiné chaty - můžete poslat sdílení odkaz jinému uživateli, ale pokud máte firemní účet, nelze to automaticky nasdílet vaší pracovní skupině. Není to tedy příliš elegantní a rychle ztratíte přehled, komu jste co nasdíleli, rozhodně to nejde používat nijak rutinně. Naopak v Claude můžete projekt mít buďto privátní, nebo jej sdílet se svou firmou (u firemních účtů). Jen pro pořádek připomínám, že OpenAI má ještě projekty ve firemním API přístupu, kde jde sdílení široce konfigurovat, ale to nejde o takto zpřístupněné projekty.

Google Gemini zatím žádnou obdobu Projektů nemá. Místo toho nabízí GEM, čehož obdobou u OpenAI jsou GPTs. Claude nic podobného zatím nemá. Takže si pojďme říci, k čemu to je.

### Kdy si vybrat GPTs (gépétéčka) a GEM?

Projekty jsou mechanismy, kdy vy pracujete s chatem a data do něj vkládáte ručně. OpenAI vymyslelo před nějakou dobou chytrý způsob, jak napojit cizí aplikace do OpenAI bez většího programování - a vytvořit tak svůj vlastní "marketplace". Této funkci se říká GPTs (česky gépétéčka nebo džípítýs).

V zásadě fungují GPTs podobně, jako projekty. Můžete si nadefinovat vlastní úpravy promptů, ale především můžete nahrát vlastní "znalosti" - "knowledge" - tedy až 20 souborů, každý o rozsahu 2 miliony tokenů, až 512 MB dat v souboru. I tady se používá mechanismus RAG.

Co to znamená? Například to, že sem můžete nahrát všechny vnitrofiremní předpisy nebo třeba zákony - a používat GPTs jako daňového poradce. Přes přednastavený prompt ovlivňujete způsob, jakým pak takové GPTs odpovídá. A co je důležitá novinka od června 2025: můžete si pro GPTs vybrat ze všech modelů, není třeba používat jednoduché 4o, které bylo jedinou nabídkou do té doby.

Může se také stát, že byste potřebovali do GPTs předávat data online. K tomu slouží ActionsGPT a je to taková vyšší dívčí, umožňuje to importovat data z jiných systémů online přes volání endpointů API. Uživatel se může ověřit přes OAuth nebo API klíč, dává to tedy vcelku slušné možnosti sáhnout si do vašeho interního systému, z něj ověřeně vzít data a ty dále zpracovat v GPTs. Účinné v případě, kdy nestačí statická sada dat.

GPTs můžete otevřít veřejnosti, takže budou vidět v přehledu GPTs na stránkách OpenAI nebo je nasdílet lidem přes URL. Pokud si chcete nějaké GPTs vyzkoušet, tady je třeba moje pro vyhledávání GPS souřadnic, kde byl pořízena fotografie. Detailněji  [popisuji postup zde](https://www.marigold.cz/item/urceni-polohy-fotky-chatgpt-o3/).

OpenAI zjevně připravuje možnost GPTs zpoplatnit z pohledu uživatele, tedy připravit skutečné tržiště, dnes se to obchází tak, že GPTs autorizují uživatele vůči nějaké službě (třeba Figma) a vyžadují zaplatit v ní.

Pamatujte si tedy hlavní znak GPTs vůči Projektům: umožňují lepší přizpůsobení, více dat v znalostní bázi, napojení na jiné online služby (zejména vaše) a lepší zpřístupnění služby veřejnosti, pokud si to přejete.

A Google Gemini Gem? Je spíše obdobou projektů, umožňuje zadat prompt a nahrát soubory do knowledge base a zvolit model, nicméně žádné napojení na online svět (kromě online vyhledávání dat z modelů Gemini) natož autentizace uživatele tu přítomné nejsou. Zatím ani není možné Gemy sdílet s jinými uživateli, ačkoliv se tato funkce zřejmě chystá. Jakkoliv jsou modely Google silné a dobré, jejích síla momentálně tkví v přístupu přes API a středně pokročilým uživatelům, kteří by si rádi udělali svého asistenta, nemají moc co nabídnout.

### Tahák: Kdy co používat?

Kdy tedy jaký přístup používat? Pojďme si to říct jednoduše a na placato:

1.  **Běžný prompt** používejte na řešení záležitostí, které se neopakují, nebo opakují příliš zřídka. A také v případě, že nepotřebujete pracovat s příliš obsáhlou znalostní bází navíc (čili chat neprotestuje, že jste do něj nahráli moc dat). V takovýchto případech nemá smysl řešit nic jiného, prostě promptujte.
    
2.  **Projekt** používejte v případě, že se vaše komunikace s LLM na nějaké **téma opakuje**. V takovém případě si odlaďte v běžném chatu správný prompt a pak jej zadejte jako prompt do projektu. Tip: dejte do něj spouštěcí slovo. Popište, co se má dělat a zapište do promptu, že se to má stát v případě, když řeknete "pracuj". Nebo naopak výslovně stanovte, že se má chat aktivně doptat na data, která mu chybí. Tak si vytvoříte svého osobního asistenta a bude se vám lépe hledat.
    
3.  **Projekt** používejte také v případě, že potřebujete **analyzovat větší množství dat**, typicky, kdy se potřebujete bavit o větším množství dlouhých dokumetů, které obslouží RAG technologie. Vždycky, když vás pro délku dokumentů odmítne obsloužit běžný prompt, je správná chvíle přejít do projektu (nebo soubory promazat, že ano). Pokud používáte Google, je v tomto momentě chvíle pro práci s GEMem.
    
4.  **OpenAI GPTs** používejte v případě, že se potřebujete **napojit na online systémy**, ať již interní nebo externí. Nebo v případě, že svou znalostní bázi chcete zpřístupnit ostatním lidem.
    
5.  Pokud potřebujete ještě větší variabilitu, musíte už pracovat s LLM pomocí API, čili si vytvořit propojení mezi vaším kódem a LLM modelem. Nemusíte ale nutně programovat, můžete použít nějakou vibecoding platformu nebo integrační služby jako Zappier nebo [Make.com](https://make.com/).
    

### Moje doporučení?

Běžný prompt také slouží pro odladění stavení Projektu/GEM nebo GPTs - protože jejich základem je také prompt. Můj oblíbený postup tedy je takovýto: vždy začínám věci používat jako prompt a pokud vidím, že se k tomuto promptu často vracím, udělám z něj Projekt. Projekt pak obnáší méně ruční práce, ale pořád je to do určité míry copy-paste metoda.

V momentě, kdy jsem přesvědčený, že mám workflow odladěné a chci to takto používat, zvážím, zda to překlopit do API. Vyhodnocuji při tom, jak moc mne oběžuje provádět to ručně. Například automatizaci generování obrázků ke článkům nevidím moc dobře, stejně si chci vybrat a uložit obrázek do GIT struktury je pro mne snadné, takže přepracování na API by mi mnoho nepřineslo. Kromě toho každý kód komunikující s API vyžaduje údržbu, která už bývá náročná. Osobní asistent nad projekty nebo jako GPTs je oproti tomu na údržbu velmi nenáročný.

Prompty lze navíc vytvářet i dosti složité a rozvětvené. Můžete se nechat v chatu provést dotazníkem a po jeho vyplnění LLM provede to, co mu z dotazníku plyne. Pokud vám nevadí textové rozhraní pro ovládání, mohou být projekty a GPTs velmi silným nástrojem.

Určitou Nevýhodou Projektů také je, že v nich nelze používat Úlohy z OpenAI. Já často používám hlídání například changelogů na konkrétní tématické zmínky, například na funkce, které používám - a nezajímají mne jiné změny v changelogu. Nastavím si Úlohu v ChatGPT a když se aktualizuje moje oblíbená funkce, dozvím se to. To mi ale vyskočí jako nejnovější chat a přijde mi notifikace a na úlohy jsem zatím nenašel reálný model, kde bych potřeboval používat velkou bázi dat z Projektů, takže mi to nevadí.

### A co Grok?

Možná někdo používáte Grok od xAI, i když je v českém prostředí málo oblíbený (a SuperGrok je relativně drahý). Zajímavý je především kvůli možnosti extrahovat data z Twitteru/[X.com](https://x.com/), což je jinde omezené a ze strany X cíleně blokované). Inu propojení skrze Muska je tu výhodou.

Grok nabízí Workspace, tedy obdobu projektů. Můžete si vybrat model, režim (DeepSearch a DeeperSearch je tu. navíc) a nahrávat sem soubory, nicméně jsem nikde nenašel žádné dobré popisy, jaké jsou limity. Navíc Grok je jediný velký model, který si neplatím, takže jsem limity osobně nevyzkoušel. Výhodou je, že Grok je multimodální, podobně jako OpenAI si tedy poradí také s obrázky. Grok 3 má ovšem problémy s češtinou a také nepochopil prompt a na jeho ladění jsem nevěnoval moc času. Udělal hezkou fotku, ale formát měl být na šířku, ne na výšku - a čeština velký špatný. Obecně bych Grok nedoporučoval, pokud potřebujete pracovat rutinně s češtinou, i když v běžném použití limity nejsou zřetelné.

### Moje způsoby použití Asistentů

Na co já osobně používám projekty:

-   vytváření obrázků pro sociální sítě či pro poutání na blogu na titulní stránce 
-   rutinní prověřování materiálů do zastupitelstva či do výboru pro development, kdy nahraju dokument a Claude mi rovnou řekne, jaké jsou zde nesoulady s podmínkami města.
-   kontroly rozpočtů na náležitosti, kdy už mám připravenou sadu informací, které chci vidět a vědět a Projekt mi udělá okamžitě tabulku s přehledem
-   předpřipravování materiálů ke článkům, kdy nahraju technické definice a tiskové zprávy a Projekt mi z nich vytahá vše podstatné
-   pro psaní beletrie používám Projekt jako mého prvního čtenáře a editora. Mám sadu zásad, jak moje kapitola má vypadat a nechávám kontrolovat Projekt, zda se držím těchto zásad, například zda v dialogu osoba, která má být zlá, také zle hovoří a nevypadává z role.
    

Na závěr jedno **pojmologické okénko**, aby nedošlo ke zmatení. OpenAI totiž provozuje [Assistants jako službu v API](https://platform.openai.com/docs/assistants/overview), což umožňuje vytvořit AI asistenty ve vašich aplikacích. To je také důvod, proč jsem se dlouhodobě vyhýbal používání pojmu asistenti pro výše uvedené služby, protože to kolidovalo s Assistants API. Nicméně se ukazuje, že tuto službu nikdo moc nezná, takže žádná kolize moc nehrozí. Proto pro výše uvedené postupy nadále používám označení asistenti - a pro tu službu OpenAI budu používat Assistants API.

A co vy, na co byste rádi vytvořili asistenta? Můžeme se tu v komentářích nad tím zamyslet, jak na to!
