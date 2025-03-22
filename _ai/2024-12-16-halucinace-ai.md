---
layout: post
title: Halucinace v umělé inteligenci -  Co to je, proč vznikají, jak je rozpoznat a minimalizovat
date: 2024-12-16
order: 4
thumbnail: https://datascientest.com/en/files/2024/03/AI_hallucinations-1024x585-1.jpg
---
__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc}

Halucinace ve světě umělé inteligence nejsou metaforickým popisem mystických vizí, nýbrž zcela konkrétním a nežádoucím jevem, kdy model (například velký jazykový model typu GPT, LLaMA či PaLM) generuje informace, které buď neodpovídají realitě, nebo jsou zcela smyšlené. 

Tyto halucinace představují zásadní problém zejména v oblastech, kde je vyžadována absolutní přesnost a důvěryhodnost, jako jsou právní dokumenty, medicínské diagnózy či technické specifikace. Přestože se jedná o poměrně známý fenomén, pochopení jeho vzniku, možností detekce a opatření proti němu je klíčové pro efektivní a odpovědné nasazování pokročilých AI systémů.

### Co jsou halucinace v kontextu umělé inteligence?

Halucinací nazýváme situaci, kdy model, trénovaný zejména na predikci dalšího symbolu v sekvenci, vyprodukuje nesprávný či zcela vymyšlený obsah. Jde tedy o „faktografické omyly“ nebo smyšlené informace bez opory v tréninkových datech či kontextu. Halucinace se mohou pohybovat od drobných chyb v datech, například nesprávné citace, až po zcela vykonstruované a neexistující teorie či skutečnosti. Uživatel, který takový výstup obdrží, může mylně nabýt dojmu, že je model spolehlivým zdrojem pravdivých informací.

### Proč halucinace vznikají?

Příčiny halucinací jsou vnitřně spjaty s principem fungování velkých jazykových modelů (LLMs – Large Language Models):

1. **Statistická podstata modelu**: Modely jako GPT jsou trénovány na obrovských objemech textu tak, aby se naučily predikovat pravděpodobnost výsktu následujícího tokenu (slova či symbolu). Nemají implicitní porozumění „pravdě“ či světu kolem nás, ale pouze statistickou reprezentaci souvislostí mezi tokeny. Pokud se ocitnou v situaci, kdy je pravděpodobnost mnoha slibně vypadajících, ale nekorektních odpovědí podobná, mohou zvolit „nejpravděpodobnější znející“ variantu, která je ovšem zcela smyšlená.

2. **Nedostatek kontextu**: Pokud model nemá k dispozici dostatek kontextových informací, často se uchýlí k „logickým domýšlením“. Výsledkem může být vytvoření zdánlivě koherentní, avšak nepravdivé odpovědi. Model se jednoduše snaží „vyplnit mezery“ tak, aby výsledek působil věrohodně.

3. **Absence robustního fakt-checkingu**: Běžné LLM nemají vnitřní mechanismus pro ověřování faktů. Nejsou vybaveny skutečnou kontrolou dat proti externím zdrojům v reálném čase, pokud k tomu nejsou speciálně navrženy (např. přes retrieval-augmented generování, kdy si model dynamicky dotahuje informace z databází či znalostních bází).

4. **Bias a kvalita tréninkových dat**: Nedostatečně kvalitní, nevyvážená či zavádějící tréninková data mohou vést k tomu, že model přijme nesprávné vzorce a bude je následně „halucinovat“ i v situacích, které to nevyžadují.

### Statistická podstata modelu

Zásadním aspektem vzniku halucinací je vrozená pravděpodobnostní povaha generativních jazykových modelů. Při generování každého tokenu model pracuje s pravděpodobnostní distribucí možných následujících tokenů, přičemž výběr je ovlivněn parametrem teploty (temperature). Tento parametr určuje míru "kreativnosti" modelu - při vyšších hodnotách je distribuce pravděpodobností plošší, což vede k diverzifikovanějším, ale potenciálně méně přesným výstupům.

Kumulativní nejistota v dlouhých sekvencích představuje další kritický faktor. S každým generovaným tokenem se nejistota modelu akumuluje, což může vést k postupnému odklonu od fakticky správných informací. Tento jev je zvláště patrný při generování delších textů, kde model musí udržovat konzistenci napříč mnoha vzájemně provázanými tvrzeními.

### Nedostatek kontextu

Omezená kontextová délka představuje fundamentální limitaci současných architektur. Modely pracují s fixním kontextovým oknem, jsou schopny si tedy „zapamatovat“ kolem řešeného problému typicky několik tisícovek slov, typicky několika tisíc tokenů, což omezuje jejich schopnost udržet konzistenci napříč delšími texty. Informace mimo toto okno jsou efektivně zapomenuty, což může vést k vnitřním kontradikcím v generovaném obsahu.

### Nekvalitní výuková data

Znáte to, když se sami učíte ze špatné učebnice, od zkoušek vás vyhodí. To samé funguje u umělé inteligence. Kvalita a struktura trénovacích dat fundamentálně ovlivňuje schopnost modelu generovat přesné a fakticky správné informace. Neúplnost nebo nepřesnost v trénovacích datech se přímo promítá do generovaného obsahu. Model může například narazit na konflikty mezi různými zdroji informací v trénovacím datasetu, což vede k nejistotě při generování odpovědí.

Nedostatečné pokrytí okrajových případů v trénovacích datech představuje významný problém. Model má tendenci interpolovat mezi známými případy, což může vést k nepřesnostem při konfrontaci s novými nebo neobvyklými situacemi. Toto je zvláště problematické v odborných a technických doménách, kde přesnost a specifičnost jsou kritické.

Kontaminace trénovacích dat představuje subtilní, ale závažný problém. Data mohou obsahovat faktické chyby, předsudky nebo záměrně nepravdivé informace. Model nemá inherentní schopnost rozlišit pravdivé od nepravdivého a může tak reprodukovat nebo amplifikovat existující nepřesnosti v trénovacích datech.

Kombinace statistické podstaty modelu, nedostatečně velkého konetxtu a problematických výukových dat je pro LLM modely velmi problematická. V praxi to znamená, že zejména obsáhlé dotazy, nebo dotazy, v nichž je potřeba zpracovávat příliš široký záběr dat, vytvářet příliš širokou úvahu na okrajové téma, které se v trénovacích datech neobjevovalo příliš často, nutně vedene do určité míry k halucinacím. 

Dnešní LLM systémy jsou ale stavěné tak, aby halucinace pokud možno rozpoznávaly a z odpovědi je odstranily. Jak?

## Jak halucinace rozpoznat?

Rozpoznání halucinací je úkolem, který vyžaduje kombinaci technických i uživatelských přístupů:

1. **Logická kontrola odpovědí**: Technicky vzdělaný uživatel by měl systematicky ověřovat tvrzení modelu. Zcela smyšlená jména osob, organizací, institucí či neexistující referenční materiály jsou častým znakem halucinací. Čili tohle je na vás. 

2. **Křížová verifikace s externími zdroji**: Pokud existuje možnost, měl by být výstup modelu porovnán s důvěryhodnými zdroji. Ať už jde o vyhledání informace pomocí externího vyhledávače, porovnání s ověřenou databází nebo citování specifických technických norem, validační krok dokáže odhalit falešné informace.

3. **Promyšlené testování modelu**: Techniky jako tzv. adversariální testování, kdy uživatel cíleně klade otázky tak, aby model na ně sám sebe usvědčil z nekonzistence, mohou pomoci halucinace identifikovat. Zadáním mírně pozměněných dotazů a sledováním odlišných odpovědí lze odhalit, kde model „klopýtá“.

4. **Metaanalýza kontextu a stylu**: Určité jazykové modely mají tendenci halucinovat s vyšší frekvencí v určitých typech dotazů. Pomoci může analýza, zda výstup obsahuje neurčitá tvrzení bez opory v konkrétních faktech, nebo příliš obecné fráze bez detailů.

### Jak se halucinacím bránit a minimalizovat je

Minimalizace halucinací je klíčová pro nasazení AI v praxi. Existuje několik přístupů, jak riziko halucinací snížit:

1. **Retrieval-Augmented Generation (RAG)**: Místo spoléhání se čistě na interní váhy modelu lze použít přístup, kdy model dotahuje informace z externí znalostní báze, databáze, nebo indexovaných dokumentů. Model tak nedělá „dojmy z prázdna“, ale pracuje s reálnými daty.

2. **Faktografické trénování**: Jemné dolaďování (fine-tuning) modelu na přesných a ověřených datech, případně specializovaný trénink, který posílí schopnost modelu verifikovat fakta, může podstatně snížit míru halucinací.

3. **Využití řetězcového uvažování (Chain-of-Thought)**: Pokud model generuje svůj postup řešení krok za krokem a je schopen svůj „myšlenkový“ proces reflektovat, může sám odhalit nekonzistentní prvky ještě předtím, než je poskládá do finální odpovědi.

4. **Hybridní systémy a lidský dohled**: Častým přístupem je kombinace automatizovaného generování odpovědí s lidskou supervizí nebo s dalšími AI modely, které slouží jako kontrolní mechanismy. Lidský odborník či specializovaný validační model může odfiltrovat chybné výstupy předtím, než se dostanou ke koncovému uživateli.

5. **Nastavení teploty a jiných parametrů generování**: Úprava hyperparametrů modelu, jako je tzv. teplota (temperature), může pomoci snížit míru kreativních, ale nepodložených výstupů. Nižší teplota obecně vede k konzervativnějším a tedy méně halucinujícím odpovědím.

### Závěr

Halucinace v umělé inteligenci jsou přímým důsledkem statistické povahy současných generativních modelů a nedostatku jejich „porozumění“ reálnému světu. Přestože jsou tyto modely neocenitelné pro mnoho úloh (summarizace textu, jazykové překlady, generování kódu, asistenční systémy), uvědomění si jejich inherentních limitací je zásadní. Technicky zdatní čtenáři by měli být obeznámeni s tím, jak halucinace vznikají, jak je spolehlivěji rozpoznávat a jak se jim bránit. Různé strategie, ať už využití externích zdrojů, jemné dolaďování, řetězcové uvažování či lidský dohled, v kombinaci povedou k robustnějším, důvěryhodnějším a obecně spolehlivějším AI systémů.

