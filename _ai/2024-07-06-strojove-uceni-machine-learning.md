---
layout: post
title: "Úvod do strojového učení - Machine Learning"
date: 2024-07-06
order: 4 
hide: true
---

Strojové učení je poddisciplína umělé inteligence (AI), která se zabývá vývojem algoritmů umožňujících počítačům se samostatně učit z dat. Namísto explicitního programování počítače na vyřešení konkrétního problému mu poskytujeme data a necháme jej, aby si z těchto dat vytvořil vlastní modely a pravidla, které použije při rozhodování. Tento proces umožňuje strojům přizpůsobit se novým situacím a zlepšovat svou výkonnost na základě zkušeností. Jeho podstatnou výhodou také je, že počítač může v datech tímto způsobem vidět souvislosti, které nás nenapadly a tím dojít k inovativním závěrům. To by v momentě, kdybychom mu výslovně řekli, jak má při zpracování dat postupovat, nebylo možné. 

## Typy strojového učení

Existují tři hlavní typy strojového učení: učení s učitelem, učení bez učitele a učení posilováním.

### Učení s učitelem
Učení s učitelem (supervised learning) zahrnuje trénování modelu na datové sadě, která obsahuje vstupy a odpovídající výstupy. Příkladem může být predikce ceny nemovitostí na základě historických dat o prodeji. Model se učí z těchto dat a snaží se nalézt vztah mezi vstupními vlastnostmi (velikost domu, lokalita, počet pokojů) a výstupem (cena domu). Díky tomu, že zná výsledek na obsáhlé sadě dat, je pro něj jednodušší najít souvislosti. 

### Učení bez učitele

Učení bez učitele (unsupervised learning) pracuje s daty, která nejsou označena, otagována. Cílem je najít skryté struktury nebo vzory v datech. Příkladem může být clustering, kde se snažíme seskupit data do skupin s podobnými vlastnostmi. To se často používá v marketingu pro segmentaci zákazníků na základě jejich nákupního chování. Tím, že v průběhu tohoto učení není dopředu znám kýžený výsledek, je výstup považovaný za volnější a například u ceny nemovitostí může počítač dojít k inovativním závěrům, že cena závisí i na faktorech, jako je stav domu nebo sousedé. 

### Učení posilováním

Učení posilováním (reinforcement learning) je přístup, kde se model učí na základě interakce s prostředím a zpětné vazby ve formě odměn nebo trestů. Představte si robota, který se učí procházet bludištěm. Za každý krok správným směrem dostane odměnu, zatímco za krok špatným směrem dostane trest. Cílem je maximalizovat *celkovou odměnu*. Povšimněte si, že odezvu umožňuje třeba ChatGPT - palcem nahoru nebo dolů lze dát modelu zpětnou vazbu, zda jste byli s výstupem spokojeni. 

### Příklad použití strojového učení: Velké jazykové modely (LLM)

Velké jazykové modely, jako je GPT (Generative Pre-trained Transformer) vyvinutý společností OpenAI, jsou konkrétním příkladem hlubokého učení. GPT je trénován na obrovském množství textových dat z internetu, což mu umožňuje generovat text, který je velmi podobný lidskému.

Jak funguje trénink LLM?

Trénink LLM zahrnuje následující kroky:

1.	Sběr dat: Obrovské množství textových dat je shromážděno z různých zdrojů, jako jsou knihy, články, webové stránky.
2.	Předzpracování dat: Textová data jsou vyčištěna a transformována do formátu vhodného pro trénink. To zahrnuje odstranění nežádoucích znaků, tokenizaci textu (rozdělení na menší části, jako jsou slova nebo fráze) a další normalizační kroky.
3.	Trénink modelu: Model je trénován pomocí techniky zvané transformer, která je schopna zpracovávat sekvence textu a učit se vztahy mezi slovy v kontextu celé věty nebo odstavce.
4.	Ladění a optimalizace: Model je následně laděn a optimalizován, aby zlepšil svou přesnost a schopnost generovat smysluplný text.

### Příklad: Klasifikace e-mailů

Představme si, že chceme vytvořit systém pro automatickou klasifikaci e-mailů na spam a legitimní zprávy. To je typický příklad úlohy učení s učitelem.

1. **Sběr dat**: Shromáždíme velké množství e-mailů, které jsou již označeny jako spam nebo legitimní.

2. **Předzpracování**: Převedeme text e-mailů na číselné vektory. Například můžeme použít metodu "bag of words", kde každý e-mail je reprezentován vektorem četností slov.

3. **Trénink modelu**: Použijeme algoritmus strojového učení, například logistickou regresi nebo rozhodovací strom, který se naučí rozlišovat mezi spamem a legitimními zprávami na základě těchto vektorů.

4. **Testování**: Ověříme přesnost modelu na nových, dříve neviděných e-mailech.

5. **Nasazení**: Pokud je model dostatečně přesný, můžeme ho nasadit do produkčního prostředí pro automatickou klasifikaci nových e-mailů. A samozřejmě kontinuálně monitorujeme, které emaily lidé označují za spamy a kde jsou naopak naštvaní, že došlo k "false positive" - tedy legitimní email byl označený za spam. Inu, spam filtry jsou docela věda, nepočítejte s tím, že po přečtení tohoto článku si nějaký spam filtr hned naprogramujete. 


## Klasické strojové učení vs. hluboké učení

Jaký je rozdíl mezi klasickým a hlubokým učením? Hlavní rozdíl spočívá v komplexitě modelů a množství dat, které jsou schopny zpracovat. Zatímco klasické modely mohou být efektivní pro jednodušší úlohy s menším množstvím dat, hluboké učení je vhodné pro komplexní problémy vyžadující analýzu velkého množství dat.

### Klasické strojové učení

Klasické strojové učení zahrnuje použití algoritmů, jako jsou lineární regrese, rozhodovací stromy nebo k-means clustering. Tyto algoritmy jsou často jednodušší a rychlejší na trénování než hluboké učení, ale mohou být méně efektivní při řešení komplexních problémů, kde je třeba zpracovat velké množství dat nebo se naučit složité vzory.

### Hluboké učení. - Deep Learning

Hluboké učení je podmnožinou strojového učení, která využívá neuronové sítě s mnoha vrstvami (tzv. hluboké neuronové sítě). Tyto modely jsou schopny se naučit velmi složité vztahy a vzory v datech, což je činí ideálními pro úlohy, jako je rozpoznávání obrazu, přirozeného jazyka nebo generování textu.

Podívejme se na pár příkladů, kde se používá klasické strojové učení a kde je vhodné naopak hluboké učení. 

Klasické strojové učení se často používá v aplikacích, kde je k dispozici omezené množství dat nebo kde je důležitá rychlost trénování a interpretovatelnost modelu. Příkladem může být:

- Predikce výnosů akcií na základě historických dat.
- Analýza sentimentu na sociálních médiích.
- Identifikace anomálií ve finančních transakcích.

Hluboké učení se uplatňuje v situacích, kde je potřeba zpracovat obrovské množství dat a kde jsou požadovány složité modely schopné se učit jemné vzory. Příklady:
	
- Rozpoznávání obrazu a videa.
- Přirozené zpracování jazyka (NLP), jako je překlad textu nebo generování odpovědí.
- Autonomní řízení vozidel, kde je potřeba analyzovat obrazy z kamer v reálném čase.

### Neuronové sítě a strojové učení?

Asi jste si v případě hlubokého učení povšimli zmínky o neuronových sítích. Jaký je tedy vztah mezi strojovým učením a neuronovými sítěmi? Neuronové sítě jsou klíčovou součástí strojového učení, zejména v oblasti hlubokého učení. Strojové učení je širší oblast umělé inteligence, která zahrnuje různé přístupy a techniky pro vytváření modelů, které se učí z dat. Neuronové sítě jsou jedním z mnoha typů modelů používaných ve strojovém učení. Pro jaké použití se neuronové sítě v ML hodí?

- Zpracování přirozeného jazyka (NLP): Rekurentní neuronové sítě (RNN) a transformery
- Počítačové vidění: Konvoluční neuronové sítě (CNN)
- Generativní modely: Generative Adversarial Networks (GAN)

Existuje ale celá řada dalších modelů, které se ve strojovém učení využívají.


## Výzvy a budoucí směry

Strojové učení, zejména v kontextu AI a LLM, má řadu svých problémů pod čarou ponoru, s nimiž se autoři modelů musí vypořádat. Zrekapitulujme si je, protože v případě práce se strojovým učením jim budete ve větší či menší míře čelit také... 

1. **Potřeba velkých dat**: Hluboké modely vyžadují obrovské množství dat pro efektivní trénink.

2. **Výpočetní náročnost**: Trénování velkých modelů je extrémně výpočetně náročné a energeticky nákladné.

3. **Interpretovatelnost**: Hluboké modely jsou často považovány za "černé skříňky", což ztěžuje pochopení jejich rozhodovacího procesu.

4. **Bias a férovost**: Modely mohou zachycovat a zesilovat předsudky přítomné v trénovacích datech.

5. **Generalizace**: Zajištění, aby modely dobře fungovaly na nových, neviděných datech, zůstává výzvou.

Budoucí směry výzkumu zahrnují:

- **Efektivnější architektury**: Hledání modelů, které dokáží dosáhnout podobných výsledků s menším počtem parametrů.
- **Učení s méně daty**: Vývoj technik, které umožní efektivní učení i s omezeným množstvím dat.
- **Multimodální učení**: Integrace různých typů dat (text, obraz, zvuk) do jednotných modelů.
- **Kontinuální učení**: Vývoj systémů, které se mohou průběžně učit bez "zapomínání" předchozích znalostí.

Strojové učení a jeho poddisciplíny hrají klíčovou roli ve vývoji moderní umělé inteligence. Zatímco klasické strojové učení nabízí rychlá a interpretovatelná řešení pro jednodušší problémy, hluboké učení umožňuje řešení komplexních úloh vyžadujících zpracování velkého množství dat. Velké jazykové modely, jako je GPT, jsou příkladem toho, jak hluboké učení může být použito k dosažení úžasných výsledků v oblasti přirozeného zpracování jazyka a generování textu.