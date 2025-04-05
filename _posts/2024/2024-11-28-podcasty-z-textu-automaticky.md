---
author: Patrick Zandl
categories:
- AI
- NotebookLM
- podcasty
layout: post
post_excerpt: 'Nové služby nabízejí zajímavou funkci: vezmou vaše materiály a vytvoří
  z nich atraktivní podcast, v němž se dvojice moderátorů baví o vašich materiálech.
  Můžete to používat pro sebevzdělávání i pro své posluchače. Jak na to a jakou službu
  zvolit? Podíváme se zde.'
summary_points:
- NotebookLM umožňuje analýzu dokumentů a generování podcastů.
- GenFM vytváří podcasty z dokumentů s podporou češtiny.
- Superpodcast nabízí nastavení podcastů, ale je přetížený.
- Audio Přehledy v NotebookML jsou kvalitní, ale pouze v angličtině.
thumbnail: https://www.marigold.cz/assets/google-notebookml.png
title: Audio podcast z vašich textů automaticky. NotebookLM a Elevenlabs GenFM
---

Umělá inteligence přinesla řadu úžasných nástrojů pro analýzu dat. Jednou z forem výstupu takové analýzy může být i hlasová podcast. Představíme si tři nástroje, do nichž můžete nasypat své podklady, nechat si vygenerovat hlasový výstup - a ten si pak nahrát do mobilu a poslouchat jej za běhání či v autě.

## Google NotebookLM

Prvním projektem je  [NotebookLM](https://notebooklm.google.com/)  - služba společnosti Google, kterou bychom mohli nazvat "zakladatel žánru". Projekt byl původně představen v roce 2023 pod názvem “Project Tailwind”. Na jeho vývoji se podílel populární vědecký autor Steven Johnson a produktová manažerka Raiza Martin.

Základem služby NotebookML je možnost nahrát do ní dokumenty ke zkoumanému tématu v několika formátech: od PDF, přes Google Docs a Slides až po webové stránky. Následně služba vygeneruje sadu doporučených dotazů ke zkoumání těchto dokumentů a můžete samozřejmě pokládat vlastní dotazy. Dotazy jsou zodpovídány pomocí AI z dokumentů, které jste do služby nahráli. Můžete si nechat vygenerovat nejrůznější souhrny, analýzy, můžete nechat službu porovnat dokumenty proti sobě. Je to zkrátka super záležitost, pokud potřebujete analyzovat podkladové materiály za účelem studia, přípravy firemních podkladů a dalších prací, kde potřebujete pracovat s větším množstvím materiálů.

![Google NotebookLM pracovní rozhraní](/assets/notebookml.png)

Naprosto úžasnou z této služby ale dělá funkce  **Audio Overviews**  - Audio Přehledy. Přehledy vám totiž vygenerují souhrn jako hlasový podcast, ve kterém dva moderátoři vedou rozhovor na bázi podkladů, které jste jim poskytli. Rozhovor si můžete přizpůsobit klasicky tím, že dopředu řeknete, na co se má rozhovor zaměřit a také jakou má mít délku. Zda pár minut do půl hodiny či delší.

Přehledy jsou naprosto fenomenální funkce. NotebookML do nich opravdu vybírá zajímavé věci z materiálů, zvuk je velmi dobře udělaný a rozhovor vypadá naprosto přirozeně. Dokonce jsou v něm taková ta přitakávání a různé odmlky, které jej dělají naprosto přirozeným. Co je podstatná nevýhoda: dobře to funguje jen v angličtině, do jiného jazyka se Přehledy ani oficiálně nedají přepnout. Lze to sice obejít, pokud se vyznáte v promptování AI, ale kvůli použitému modelu Gemini 1.5 není český výstup nijak zvláště kvalitní, zní dosti všeslovansky. Jelikož ale NotebookML byl v září 2024 převeden na oficiální Google produkt a dokonce je zařazen v nabídce pro firmy, dá se předpokládat, že se v nějaké dohledné době přejde na jazykové modely s lepší podporou češtiny. A pak budou i Přehledy v češtině kvalitnější. Takže vám ani nebudu říkat, jak to máte ohackovat, občas se tím hackováním přes prompt jazyky pomíchají a nestojí moc za to česky Přehledy používat...


Jelikož se v Institutu Pí zabýváme optimalizací státní správy, jeden z materiálů, které jsme si nechávali pomocí NotebookML zpracovávat, jsou postupy oprav komunikací. Vygeneroval jsem k tomu dva Audiopřehledy, můžete si je porovnat:

-   anglicky namluvená verze  [US-China Economic Conflicts: Trade Wars and Industrial Policy](https://notebooklm.google.com/notebook/af5484ff-4c05-403b-9c88-913ef11ff35d/audio)
    
-   česky namluvená verze  [EU Road Surface Maintenance](https://notebooklm.google.com/notebook/44ae89f2-a328-4fc2-9e0a-35c183fb9122/audio)

**Update duben 2025:** 

Google se projektu NotebookLM dále intenzivně věnuje. Nejenom, že v prosinci vylepšil možnosti přidávání souborů, nyní dokonce přidal funkci [Discover sources](https://blog.google/technology/google-labs/notebooklm-discover-sources/?ref=marigold), která umožní **prohledat  hlubiny webu a najít další materiály** k těm, které již máte. Funkci najdete v panelu Sources, kde je tlačítko Discover. 

Druhým vylepšením z jara 2025 je **funkce Mind Mapy**, která transformuje způsob, jakým studenti pracují s informacemi. Tato inovativní funkce generuje interaktivní vizuální diagramy, které přehledně mapují strukturální vazby mezi různými koncepty ve studijních materiálech. Uživatelé mohou intuitivně prozkoumávat myšlenkové mapy, přibližovat konkrétní oblasti zájmu a díky možnosti kliknout na jednotlivé koncepty okamžitě získat jejich shrnutí. Tento vizuální přístup k učení výrazně usnadňuje pochopení komplexních témat, neboť ukazuje, jak spolu jednotlivé myšlenky souvisejí, a pomáhá odhalit vztahy mezi zdánlivě nesouvisejícími koncepty. Na základě zpětné vazby uživatelů NotebookLM zjistil, že tento způsob vizualizace významně zlepšuje schopnost studentů uchopit a zapamatovat si i nejnáročnější studijní látku.

Současně s tím NotebookLM zásadně **vylepšil svůj přístup k práci s PDF dokumenty**, což řeší jeden z nejčastějších požadavků uživatelů. Nová funkce rozpoznávání obsahu PDF souborů nyní dokáže komplexně analyzovat veškerý obsah dokumentů, včetně obrazového materiálu a grafů. Toto vylepšení je důležitá pro lidi pracující s odbornými texty a akademickými publikacemi, které často obsahují složité vizuální prvky nesoucí klíčové informace. 


## Elevenlabs GenFM

Služba  [GenFM](https://elevenlabs.io/genfm)  je čerstvou listopadovou novinkou společnosti Elevenlabs zabývající se hlasovými službami na bázi AI. Pokud něco se strojově generovaným hlasem chcete podnikat, rozhodně si nabídku Elevenlabs projděte, jsou hodně daleko a nabízejí například schopnost dubbovat video včetně synchronizace pohybu rtů.

Pro nás je ale teď důležitá služba GenFM, která zatím funguje jen v mobilních aplikacích (v listopadu 2024  [byla jen v iOS](https://apps.apple.com/us/app/elevenlabs-reader-ai-audio/id6479373050), pro Android se chystá), nemá webové rozhraní, což ji zatím dost limituje. Ale s ohledem na to, že je stará doslova pár hodin a Elevenlabs jsou dosti agilní, se dá čekat, že služba se bude rychle posouvat.

Služba opět funguje vcelku jednoduše. Nahrajete do ní dokument, můžete ho také ofotit, dát odkaz na článek nebo na Youtube video - a po stisku GenFM tlačítka je vám vygenerován podcast, v němž se dva moderátoři baví o tématu.

![Elevenlabs GenFM na iOS](/assets/elevenlabs-genfm.jpeg)

Oproti NotebookML jde o citelně jednodušší službu. Výstup nemůžete prakticky nijak přizpůsobovat, kromě toho, že si můžete vybrat hlasy a písmo zobrazovaného textu. Co je ale podstatné: služba díky backendu Elevenlabs funguje výborně i v češtině. Sice není podcast zdaleka tak přirozený, jako v NotebookML, ale je poslouchatelný - a pokud si přejete, je v češtině nebo v dalším z cca 30 jazyků.

Co je momentálně velká nevýhoda, je nemožnost soubor nějak uložit nebo někomu nasdílet. Jistě, v nabídce aplikace je Export Audio, ale ta vás přehodí na web, kde nic takového možné není. Snad se to rychle doplní.

Na web se vygeneruje jen náhled v omezené délce 1 min 11 vteřin, celý podcast od někoho jiného si musíte zobrazit v mobilní aplikaci Elevenlabs Reader. Ale dva příklady si tedy dejme:

-   toto je můj  [článek o neplacení daní Apple v Irsku](https://elevenreader.io/app/reader/genfm/7fb5de89f5ef0abc3d2d7be429b6830e7ebddb85a808a7aa0f4fbed33e337425/u:moKlgU3JI0OBO2GjsjIL)  pro Lidové noviny převedený do formy podcastu
    
-   a toto je  [článek věnovaný novým frekvencím pro sítě 6G](https://elevenreader.io/app/reader/genfm/7fb5de89f5ef0abc3d2d7be429b6830e7ebddb85a808a7aa0f4fbed33e337425/u:NvTWzpiqlN1nmLX3eoRA), který jsem GenFM nechal načíst [z URL na Marigoldovi](https://www.marigold.cz/item/nova-frekvenci-pasma-5g-6g/).
    

  

## Superpodcast

Třetí službou je  [Superpodcast](https://www.superpodcast.ai/), menší nezávislá služba umožňující nahrát dokumenty v několika formátech a zadat k nim upřesňující prompt, na co se má vygenerovaný podcast zaměřit. V nabídce podpory je i čeština, bohužel v době psaní článku se podcasty negenerovaly, takže vám český podcast nemohu zalinkovat - doplním později. Anglické podcasty jsou dobře nahrané, zvuk a jeho tok subjektivně lepší, než Elevenlabs a horší, než NotebookML, ale jsou dosti na jedno brdo, což ruší, když jich posloucháte více za sebou.

Superpodcast umožňuje dost nastavení, je v tom příjemnější, než oba výše zmíněné nástroje, ale momentálně je služba dost přetížená.

-   vzorový podcast  [AI voice cloning revolution](https://studio.superpodcast.ai/podcast/76bbdc3f-9ad6-4992-8767-8394096656ba)
    

  

## Doporučení

**Používání služby NotebookML vám výrazně doporučuji**, pokud potřebujete analyzovat nějaké množství dokumentů. Služba je momentálně zdarma a práce s ní je proti jiným podobným službám příjemná a svižná. Google navíc slibuje, že dokumenty do ní nahrané nepoužívá pro trénink AI.

NotebookML pro vás momentálně bude skvělým rozhraním do studia nějakého tématu a pro věci typu bakalářka, disertace, firemní studie či analýza, je to naprosto nepostradatelný nástroj. Můžete jej také využít pro přípravu podklad na schůzku nebo třeba pro přípravu materiálů na sociální sítě.

Audio Přehled je momentálně asi funkce navíc, protože bez kvalitního českého hlasu to v angličtině příliš nevyužijete.

GenFM chybí možnost audiosoubory exportovat, ale je to nadějné - zatím spíše pro osobní použití. A Superpodcast zatím spíše slíbil...