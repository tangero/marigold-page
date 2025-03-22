---
author: Patrick Zandl
categories:
- AI
- Google
- Gemini
layout: post
post_excerpt: Google představil funkci pro průzkum tématu nazvanou příhodně Deep Research.
  Jak ji můžete využít?
summary_points:
- 1. Deep Research v Gemini provádí hloubkový výzkum a vytváří zprávy.
- 2. Funkce funguje pouze v angličtině, vyžaduje přepnutí jazyka.
- 3. AI může "halucinovat" při nedostatku dat, ověřte výsledky.
- 4. Výstup zahrnuje podrobné analýzy s odkazy na zdroje.
- 5. Pro češtinu použijte překladače jako Deepl nebo Google Translator.
thumbnail: https://cdn.iphoneincanada.ca/wp-content/uploads/2024/12/Gemini_Research.jpg
title: "Google Gemini Deep Research - skvělý průzkum tématu s pomocí AI"
---

Tahle funkce [Google Gemini](https://gemini.google.com) je naprosto úžasná v případě, že potřebujete důkladně prozkoumat nějaké téma. Jmenuje se Deep Research a dělá přesně to, co píše: hluboký průzkum, ze kterého pak udělá zprávu. 

Nejprve upozornění: Deep Research funguje jen v angličtině, pokud máte produkty Gemini a Google obecně přepnuté do češtiny, nemůžete ji použít. Stačí si nicméně v Nastavení přepnout jazyk na Angličtinu a v menu se vám model Gemini 1.5 Pro with Deep Research objeví. Nicméně odteď můžete komunikovat jen anglicky, čili je nutné si nejdříve formulovat zadání v angličtině. Hloubkový výzkum běží v rámci Gemini Advanced (počínaje angličtinou) na počítači a mobilním webu a v mobilní aplikaci bude k dispozici na začátku roku 2025. 

> **Upozornění:** Zejména v případě, že k tématu je příliš málo dat, má AI tendenci "halucinovat". Ověřte si tedy všechna tvrzení, na kterých záleží. Počítejte také s tím, že DR vám nenavrhne nové přelomové řešení, spíše sumarizuje (na webu) existující možnosti a navrhne další postup. Samotný další výzkum ale už neprovede.  

![Volba Deep Research je vidět jen v anglické verzi](/assets/deep-research-option.png)

Vyzkoušíme něco složitého, na co nejde "vygooglovat" jednoduchá a přímočará odpověď, ale na co je opravdu udělat průzkum.

Moje téma: chci zjistit, jaké jsou možnosti zjištění váhy vozidla pouze na bázi jeho fotografie ke zjištění přetěžování silnic. Dávám tedy dotaz: 

> Research all the possibilities of estimating the vehicle weight from camera images to detect overloading of the road by high vehicle weight. 

Po zadání otázky vytvoří Deep Research vícestupňový plán výzkumu, který můžete buď upravit, nebo schválit. Vypadá to nějak takhle:

![Vstupní zadání a návrh plánu výzkumu](/assets/deep-research-input.png)

Jakmile jej schválíte (přijal jsem jej beze změn), začne za vás hloubkově analyzovat relevantní informace z celého webu, které trvá "několik minut" - já si šel uvařit čaj, když jsem se za pár minut vrátil, bylo hotovo. K dispozici je plný textový výstup, který si na požádání můžete převést do Google Dokumentů, na [tomto linku je výstup pro tento výzkum](https://docs.google.com/document/d/174FI2IgVk-xXkpvVFePtpTx1i0I_M_gyqozAgbDMY_0/edit?usp=sharing).  



Výstupem je v tomto případě obsáhlý článek 25 000 znaků včetně linků na zdroje. Musím říct, že jsem byl velmi překvapen. Zvolené téma mi nepřijde nijak jednoduché a nelze jej jen tak vygooglovat. Přitom článek nabízí několik zajímavých možností, například detekci deformace pneumatik a načtení jejich parametrů přes OCR spolu s technickými parametry vozidla, což by umožnilo velmi zajímavě predikovat hmotnost takového vozidla. Nebo třeba měření průhybu mostu pomocí kvalitní kamery a dopočet hmotnosti vozidla. Je tu cca 18 postupů, které mohou nabídnout nějaký výpočet nebo jeho zlepšení. Jsou zde rozebrána rizika i omezení všech přístupů a na závěr jsou uvedeny konkrétní práce, kde se lze dočíst více. 

Po provedení výzkumu už nemůžete plán výzkumu upravovat, editovat, můžete si jej jen zkopírovat a použít znovu. Ale můžete klást doprovodné otázky a systém využije informací, které již nashromáždil. Například já se zeptal anglicky:

> Není levnější používat jiné možnosti zjištění váhy projíždějícího vozidla? 

A dostal jsem dobrou a vyčerpávající odpověď, která mne uspokojila jak rozsahem, tak hloubkou úvahy. 

### Doporučené workflow pro češtinu 

I v případě, že anglicky nevládnete perfektně, lze službu opravdu silně doporučit. Jen si vypomůžeme s překladovými službami. [Deepl.com](https://www.deepl.com) umí přeložit kratší texty zdarma, takže je ideální minimálně na vytvoření dotazu. Prostě dotaz vymyslíte v češtině, přeložíte jej do angličtiny a zadáte do Deep Research. Stejně tak si poradíte při upřesňování výzkumného plánu. 

Výslednou práci si můžete nechat převést do Google Dokumentu a buďto si jej stáhnout a převést pomocí Deepl do češtiny (vzhledem k rozsahu placené) nebo použít funkci Dokumentů Nástroje → Přeložit dokument, kdy vám bude dokument přeložen službou Google Translator. Překlad není tak čtivý, ale je srozumitelné a můžete jej použít. Podívat se na přeloženou [českou verzi zprávy o vážení automobilů kamerami můžete zde](https://docs.google.com/document/d/1dqK74vVQoGuFTb2LjSQMSRzxF1Kd2yvBjgwhv5XKOFo/edit?usp=sharing). 

Tak ať se vám Google Gemini Deep Research dobře používá!

Pro porovnání dávám výstup, který mi na stejný dotaz [dává Perplexity.ai](https://www.perplexity.ai/search/research-all-the-possibilities-n10dzsMUSt2bUgdPZCHH0g) v placené Pro verzi ve všeobecném režimu:

![Perplexity.ai odpověď](/assets/perplexity-pretezovani.png)

A pokud se zeptáte v Pro módu v akademickém režimu, dostanete výrazně stručnější odpověď, ale také dobře návodnou:

## Perplexity Pro Akademický režim

Existuje několik moderních přístupů k odhadu hmotnosti vozidel pomocí kamerových systémů, které pomáhají monitorovat přetížení na silnicích.

### Metody založené na deformaci pneumatik

Základním principem je měření kontaktní plochy mezi pneumatikou a vozovkou. Systém využívá fyzikální vztah, kde síla je rovna součinu tlaku a plochy[1]. Tento přístup zahrnuje:

- Měření deformačních parametrů pneumatik pomocí počítačového vidění
- Rozpoznávání značení na bočnicích pneumatik pro zjištění doporučeného tlaku
- Využití detekce hran a optického rozpoznávání znaků pro přesné měření[10]

### Pokročilé systémy detekce

**Fúze více technologií**
Moderní systémy kombinují několik metod pro zvýšení přesnosti:
- Dynamické vážení
- Obrazové snímání
- Laserové skenování

Tento komplexní přístup dokáže udržet chybu měření celkové hmotnosti v rozmezí ±2,5%[6].

**Pravděpodobnostní přístup**
Využití fyzikálně podmíněných generativních adversariálních sítí (GAN) umožňuje:
- Odhad pravděpodobnostního rozložení hmotnosti náprav
- Zohlednění nejistoty měření
- Aplikaci pro různé typy vozidel a zatížení[9]

### Automatizované systémy kontroly

Pro praktické využití byly vyvinuty systémy, které:
- Automaticky monitorují zatížení vozidla
- Okamžitě upozorňují řidiče na přetížení
- Mohou být propojeny se systémem zapalování pro prevenci jízdy přetíženého vozidla[3]

Tyto systémy jsou zvláště důležité v rozvojových zemích, kde nejsou běžně dostupné vážní stanice, a pomáhají předcházet poškození infrastruktury a nehodám způsobeným přetěžováním vozidel.