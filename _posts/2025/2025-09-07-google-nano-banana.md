---
author: Patrick Zandl
categories:
- AI
- Google Gemini
- generování obrázků
- Nano Banana
layout: post
post_excerpt: Komplexní průvodce technikami generování a editace obrázků pomocí modelu Nano Banana - Google Gemini 2.5 Flash - s důrazem na správné promptování a praktické využití.
summary_points:
- Základní princip - popisujte scény jako příběh, ne seznam klíčových slov
- Gemini 2.5 Flash nabízí nativní multimodální zpracování textu a obrázků
- Konverzační editace umožňuje postupné vylepšování bez složitých masek
- Možnost kombinace více obrázků a přenosu stylů mezi nimi
- Přesné vykreslování textu v obrázcích pro loga a diagramy
- Různé přístupy pro fotorealistické scény versus stylizované ilustrace
title: Nano Banana a kompletní průvodce generováním obrázků pomocí Google Gemini 2.5 Flash
thumbnail: https://www.marigold.cz/assets/nanobanana_10_55AM.jpeg
---

Když se v srpnu zjevil obrazový model nazvaný Nano Banana, strhl se kolem toho velký povyk. Především proto, že byl prostě velmi dobrý v práci s obrázky. A tím myslím VELMI dobrý. Záhy se ukázalo, že je to dílo Google a ten jej počátkem záři začlenil do Google Gemini 2.5 Flash. Takže jej nyní mohou používat v rámci tohoto modelu všichni uživatelé. Pojďme se na Nano Banana model podívat - musím se omluvit, označení Gemini 2.5 Flash mi k srdci vážně nepřirostlo...  

Google Gemini 2.5 Flash je velkým posunem v oblasti generování obrázků díky své nativní multimodální architektuře. Na rozdíl od předchozích modelů byl tento systém od základu trénován na současném zpracování textu a obrázků v jediném, unifikovaném kroku. To umožňuje schopnosti přesahující prosté generování obrázků - konverzační editaci, kompozici více obrázků a logické uvažování o obrazovém obsahu. Je tedy o parník dále, než konkurenční GPT-5 a o dvě letadlové lodě Kuzněcov od modelů Anthropicu, které obrázky nějak rozpoznávají, vytvářet je ale moc neumí (definice SVG neberu v potaz). 

Použít model můžete jak na [gemini.google.com](https://gemini.google.com) tak na [aistudio.google.com](https://aistudio.google.com). 

## Základní princip úspěšného promptování

Nejdůležitější pravidlo pro práci s Gemini 2.5 Flash zní: **popisujte scénu, nevyjmenovávejte jen klíčová slova**. Model je velmi dobrý v hlubokém porozumění jazyku, proto souvislý, popisný odstavec téměř vždy vytvoří lepší a koherentnější obrázek než seznam slov.

Místo promptu typu _"stařec, keramika, dílna, zlaté světlo"_ použijte:
_"Fotorealistický portrét zblízka staršího japonského keramika s hlubokými vráskami vyřezanými sluncem a vřelým, znaleckým úsměvem. Pečlivě zkoumá čerstvě glazovanou čajovou misku. Prostředí je jeho rustikální, sluncem zalitá dílna. Scénu osvětluje měkké světlo zlaté hodiny proudící oknem, zvýrazňující jemnou texturu hlíny."_

![Tady jsme použili prompt: stařec, keramika, dílna, zlaté světlo](/assets/nanobanana_10_26AM.jpeg)

![A tady jsme použili komplexní prompt](/assets/nanobanana_10_27AM.jpeg)

**Obrázek 1: Fotorealistický portrét japonského keramika ve své dílně - v prvním případě jsme použili jen soupis klíčových slov, v druhém jsme detailně popsali scénu, jak je uvedeno výše**

## Režimy generování obrázků

### Základní generování z textu

Nejběžnější způsob vytváření obrázků spočívá v popisu toho, co chcete vidět. Gemini podporuje několik specializovaných přístupů:

#### 1. Fotorealistické scény

Pro realistické obrázky přemýšlejte jako fotograf. Zmiňte úhly kamery, typy objektivů, osvětlení a jemné detaily:

**Šablona:**
_"Fotorealistický [typ záběru] [subjektu], [akce nebo výraz], zasazený do [prostředí]. Scéna je osvětlena [popis osvětlení], vytváří [náladu] atmosféru. Zachyceno [detaily kamery/objektivu], s důrazem na [klíčové textury a detaily]. Obrázek by měl být ve formátu [poměr stran]."_

#### 2. Stylizované ilustrace a samolepky

Pro vytváření samolepek, ikon nebo grafických prvků buďte explicitní ohledně stylu a požadujte bílé pozadí:

_"Samolepka ve stylu kawaii zobrazující veselou červenou pandu s malým bambusovým kloboučkem. Žvýká zelený bambusový list. Design má výrazné, čisté obrysy, jednoduché stínování a živou barevnou paletu. Pozadí musí být bílé."_

![Samolepka pandy](/assets/nanobanana_10_34AM.jpeg)

**Obrázek 2: Kawaii samolepka červené pandy s bambusovým kloboučkem**

#### 3. Přesný text v obrázcích

Gemini 2.5 Flash vyniká ve vykreslování textu. Buďte jasní ohledně přesného znění, stylu písma a celkového designu:

"Vytvořte moderní, minimalistické logo pro kavárnu s názvem 'Patrickovo kafíčko'. Text by měl být čistým, tučným bezpatkovým písmem. Design by měl obsahovat jednoduchou, stylizovanou ikonu kávového zrna plynule integrovanou s textem. Barevné schéma je černobílé."

![Minimalistické logo](/assets/nanobanana_ 10_36AM.jpeg)

**Obrázek 3: Minimalistické logo kavárny s integrovaným textem**

#### 4. Produktové fotografie

Pro čisté, profesionální snímky produktů používejte fotografickou terminologii:

"Vysoké rozlišení, studiově osvětlená produktová fotografie minimalistického keramického hrnku na kávu v matné černé barvě s výše vygenerovaným inverzním logem "Patrickovo kafíčko", prezentovaného na leštěném betonovém povrchu. Osvětlení je třítbodové softboxové nastavení navržené pro vytvoření měkkých, rozptýlených odlesků a eliminaci ostrých stínů. Úhel kamery je mírně zvýšený 45stupňový záběr pro zvýraznění čistých linií."

![Produktová fotografie s logem](/assets/nanobanana_10_38AM.jpeg)

**Obrázek 4: Studiová produktová fotografie keramického hrnku**

#### 5. Minimalistický design s negativním prostorem

Vynikající pro vytváření pozadí webových stránek nebo prezentací:

_"Minimalistická kompozice s jediným, jemným červeným javorovým listem umístěným v pravém dolním rohu snímku. Pozadí je rozsáhlé, prázdné krémové plátno vytvářející významný negativní prostor. Měkké, jemné osvětlení. Čtvercový formát."_

![Minimalistická kompozice](/assets/nanobanana_10_40AM.jpeg)

**Obrázek 5: Minimalistická kompozice s javorovým listem a negativním prostorem**

#### 6. Sekvenční umění pro komiksy a storyboardy

"Jediný komiksový panel v drsném noir stylu s vysokým kontrastem černobílých inkoustů. Prostředí města Praha. Ulice Žižkova. V popředí stojí detektiv v plášti do deště pod blikající pouliční lampou, déšť mu promáčí ramena. V pozadí se neonová cedule opuštěného baru odráží v louži. Textové pole nahoře říká 'Město bylo vždy tvrdé místo pro udržení tajemství.' Osvětlení je ostré, vytváří dramatickou, ponurou náladu."

![Komixový panel](/assets/nanobanana_10_45AM.jpeg)

**Obrázek 6: Noir komiksový panel s detektivem v dešti**

## Pokročilé techniky editace obrázků

### Přidávání a odebírání prvků

Poskytněte obrázek a jednoduše popište požadovanou změnu. Model analyzuje původní styl, osvětlení a perspektivu obrázku:

_"Použij poskytnutou fotografii. Běžícímu muži v popředí přidej vysoký černý kouzelnický klobouk."_

![Patrick běží](/assets/patrick-bezi.jpeg)
![Patrick běží - a teď už má klobouk...](/assets/nanobanana_11_02AM.jpeg)
**Obrázek 7: Původní fotka, jak běžím - a pak a do toho jsem si přidal klobouk**

### Sémantické maskování (Inpainting)

Konverzačně řekněte modelu, aby upravil pouze jednu část obrázku při zachování zbytku:

_"Použij poskytnutou fotografii. Běžícímu muži v popředí dej místo trička bílou košili, kravatu s jasně barevným vzorkem a tmavě šedé sako. Respektuj světlo a pohyb osoby."_

![Patrick běží - a teď už má sako...](/assets/nanobanana_10_55AM.jpeg)
**Obrázek 8: Na původní fotku, jak běžím jsem si místo trička přidal sako, které jsem si původně na běh vzít chtěl, ale nevzal...**


### Přenos stylu

Poskytněte fotografii a požádejte model o její převedení do specifického uměleckého stylu:

"Transformujte poskytnutou fotografii moderní městské ulice ve dne do uměleckého stylu Vincenta van Gogha 'Hvězdná noc'. Zachovejte původní kompozici budov a aut, ale vykreslete všechny prvky vírovými tahy štětce impasto a dramatickou paletou hlubokých modří a jasných žlutí."

![Olomouc ve dne](/assets/IMG_5272.jpeg)
![Olomouc podle van Gogha](/assets/nanobanana_11_10AM.jpeg)

**Obrázek 9: Městská ulice před a po transformaci do stylu van Gogha**

### Pokročilá kompozice více obrázků

Poskytněte více obrázků jako kontext pro vytvoření nové, složené scény:

_"Vytvořte profesionální módní fotografii pro e-shop. Vezměte modré květované šaty z prvního obrázku a nechte je obléct ženě z druhého obrázku. Vygenerujte realistický celotělový záběr ženy v šatech s osvětlením a stíny upravenými pro venkovní prostředí."_

![Kompozice obrázků](/assets/Model_Gemini2.5-PromptUpdate.original.png)
**Obrázek 10: Kompozice šatů a modelky do finální módní fotografie**

## Osvědčené postupy a strategie

### Buďte hyperspecifičtí
Čím více detailů poskytnete, tím větší kontrolu máte. Místo "fantazijní brnění" popište: "ozdobné elfí plátové brnění, vyleptané vzory stříbrných listů, s vysokým límcem a ramenními pláty ve tvaru sokolích křídel."

### Poskytněte kontext a záměr
Vysvětlete účel obrázku. Model lépe porozumí kontextu a vytvoří relevantnější výsledek. "Vytvořte logo pro prémiovou, minimalistickou značku péče o pleť" přinese lepší výsledky než pouhé "vytvořte logo."

### Iterujte a vylepšujte
Neočekávejte perfektní obrázek napoprvé. Využijte konverzační povahu modelu pro postupné úpravy: "To je skvělé, ale můžete udělat osvětlení trochu teplejší?" nebo "Ponechte vše stejné, ale změňte výraz postavy na vážnější."

### Používejte postupné instrukce
Pro složité scény s mnoha prvky rozdělte prompt na kroky: "Nejprve vytvořte pozadí klidného, mlžného lesa za úsvitu. Poté do popředí přidejte mechem pokrytý starověký kamenný oltář. Nakonec umístěte na vrchol oltáře jediný, zářící meč."

### Sémantické negativní prompty
Místo "žádná auta" popište požadovanou scénu pozitivně: "prázdná, opuštěná ulice bez známek dopravy."

### Ovládejte kameru
Používejte fotografický a filmový jazyk pro kontrolu kompozice. Termíny jako širokoúhlý záběr, makro záběr, perspektiva zdola, portrétní objektiv 85mm nebo holandský úhel vám dávají přesnou kontrolu nad finálním obrázkem.

## Současná omezení

Model má několik omezení, která je třeba brát v úvahu:

- Nejlepší výkon poskytuje v angličtině, španělštině, japonštině, čínštině a hindštině - pokud se vám nedaří to vysvětlit česky, zkuste jeden z těchto jazyků... 
- Nepodporuje zvukové nebo video vstupy pro generování obrázků
- Ne vždy dodržuje přesný počet požadovaných výstupních obrázků
- Nejlépe funguje s maximálně 3 vstupními obrázky
- Při generování textu v obrázcích nejprve vygenerujte text, poté požádejte o obrázek s tímto textem
- Nahrávání obrázků dětí není momentálně podporováno v EU a Velké Británii
- Všechny vygenerované obrázky obsahují vodoznak SynthID, aby bylo rozpoznatelné, že je to AI obrázek

## Praktické využití v různých oblastech

Model nachází uplatnění v řadě profesionálních oblastí. Grafičtí designéři jej využívají pro rychlé prototypování konceptů a vytváření variací návrhů. Marketingoví specialisté generují vizuály pro sociální média a reklamní kampaně. Vývojáři her vytvářejí konceptové umění a herní prvky. Architekti vizualizují interiérové návrhy s různými variantami nábytku a osvětlení.

Konverzační povaha modelu umožňuje postupné vylepšování bez nutnosti začínat od začátku, což významně zrychluje kreativní proces. Schopnost kombinovat více vstupních obrázků otevírá nové možnosti pro vytváření produktových mockupů nebo kreativních koláží.

## Závěr

Google Gemini 2.5 Flash představuje významný posun v generování obrázků díky své nativní multimodální architektuře. Klíčem k úspěchu je pochopení, že model nejlépe reaguje na popisné, narativní prompty spíše než na seznamy klíčových slov. S postupným osvojením různých technik a strategií popsaných v tomto průvodci můžete vytvářet vysoce kvalitní vizuální obsah pro širokou škálu profesionálních aplikací.

Model neustále prochází vývojem a vylepšováním, přičemž Google aktivně pracuje na odstranění současných omezení. Pro začátek doporučujeme experimentovat s různými styly promptů v prostředí Google AI Studio, kde můžete techniky okamžitě testovat a iterovat své výtvory v reálném čase.

Pro vývojáře je podstatné, že tyto funkce lze používat také přes API a to včetně OpenRouter.ai, kde se stalo Gemini Flash 2.5 (Nano Banana) [první podporovaným obrazovým modelem](https://openrouter.ai/announcements/the-first-ever-image-model-is-up-on-openrouter). 