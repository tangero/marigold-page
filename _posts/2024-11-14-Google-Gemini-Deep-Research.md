---
title: "Google Gemini Deep Research - skvělý průzkum tématu s pomocí AI"
author: Patrick Zandl
post_excerpt: "Google představil funkci pro průzkum tématu nazvanou příhodně Deep Research. Jak ji můžete využít?"
layout: post
categories: [AI, Google, Gemini]
thumbnail: https://cdn.iphoneincanada.ca/wp-content/uploads/2024/12/Gemini_Research.jpg
---

Tahle funkce [Google Gemini](https://gemini.google.com) je naprosto úžasná v případě, že potřebujete důkladně prozkoumat nějaké téma. Jmenuje se Deep Research a dělá přesně to, co píše: hluboký průzkum, ze kterého pak udělá zprávu. 

Nejprve upozornění: Deep Research funguje jen v angličtině, pokud máte produkty Gemini a Google obecně přepnuté do češtiny, nemůžete ji použít. Stačí si nicméně v Nastavení přepnout jazyk na Angličtinu a v menu se vám model Gemini 1.5 Pro with Deep Research objeví. Nicméně odteď můžete komunikovat jen anglicky, čili je nutné si nejdříve formulovat zadání v angličtině. Hloubkový výzkum běží v rámci Gemini Advanced (počínaje angličtinou) na počítači a mobilním webu a v mobilní aplikaci bude k dispozici na začátku roku 2025. 

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

A dostail jsem dobrou a vyčerpávající odpověď, která mne uspokojila jak rozsahem, tak hloubkou úvahy. 

### Doporučené workflow pro češtinu 

I v případě, že anglicky nevládnete perfektně, lze službu opravdu silně doporučit. Jen si vypomůžeme s překladovými službami. [https://www.deepl.com](Deepl.com) umí přeložit kratší texty zdarma, takže je ideální minimálně na vytvoření dotazu. Prostě dotaz vymyslíte v češtině, přeložíte jej do angličtiny a zadáte do Deep Research. Stejně tak si poradíte při upřesňování výzkumného plánu. 

Výslednou práci si můžete nechat převést do Google Dokumentu a buďto si jej stáhnout a převést pomocí Deepl do češtiny (vzhledem k rozsahu placené) nebo použít funkci Dokumentů Nástroje → Přeložit dokument, kdy vám bude dokument přeložen službou Google Translator. Překlad není tak čtivý, ale je srozumitelné a můžete jej použít. Podívat se na přeloženou [českou verzi zprávy o vážení automobilů kamerami můžete zde](https://docs.google.com/document/d/1dqK74vVQoGuFTb2LjSQMSRzxF1Kd2yvBjgwhv5XKOFo/edit?usp=sharing). 

Tak ať se vám Google Gemini Deep Research dobře používá!

Pro porovnání dávám výstup, který mi na stejný dotaz [dává Perplexity.ai](https://www.perplexity.ai/search/research-all-the-possibilities-n10dzsMUSt2bUgdPZCHH0g) v placené Pro verzi. 

![Perplexity.ai odpověď](/assets/perplexity-pretezovani.png)