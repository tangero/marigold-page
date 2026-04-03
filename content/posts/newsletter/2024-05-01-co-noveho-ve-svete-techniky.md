---
slug: 'co-noveho-ve-svete-techniky'

author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Google
- AI
- Sociální sítě
- Internet
- EU
- Automotive
date: '2024-05-01'
original_newsletter: '#75: Jak na zápisy ze schůzek a porad pomocí AI aplikací (plus
  Tesla a Apple novinky)'
summary_points:
- Apple chystá nové iPady a vyvíjí vlastní AI řešení pro iOS 18.
- OpenELM, nový LLM od Apple, má levnější trénink a rychlejší výstup.
- Meta vydala Llama 3 8B a 70B, nejvýkonnější open source modely.
- Copilot Workspace, Memory od OpenAI a roboty Boston Dynamics jsou novinky.
title: ✅ Co nového ve světě techniky?
---

Nejvíce excitující je čekání na květnové uvedení nových Apple produktů, tady zřejmě půjde o nové iPady, které budou rychlejší, lepší, hezčí - a to je to, co bychom čekali, to je zbytečné zmiňovat. 

### **🍏 Apple se pere s umělou inteligencí**

Samo vyvíjí vlastní AI řešení, vydalo několik vědeckých zpráv o technologiích, které umožňují rychlejší trénování nebo lepší chod AI v rámci zařízení s omezenými zdroji, typicky v mobilu. A všichni napnutě vyčkávají, jak to bude s iOS 18 - a jestli tam Apple nic z AI nepředstaví, tak jej upálí. Apple si to zjevně uvědomuje, takže podle zpráv vyjednává s Google i OpenAI o možnosti použití jejich AI v rámci Apple technologií. K čemu, s kým a jak, to se zatím samozřejmě neví. Ale jejich nové **uživatelské rozhraní nazvané Ferret** nevypadá špatně ([zde vydaná výzkumná zpráva o něm](https://arxiv.org/abs/2404.05719)). 

[![](https://substack-post-media.s3.amazonaws.com/public/images/cdf52ddc-1bad-42cd-ba55-a86c97f480a3.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdf52ddc-1bad-42cd-ba55-a86c97f480a3.heic)

![](https://substack-post-media.s3.amazonaws.com/public/images/cdf52ddc-1bad-42cd-ba55-a86c97f480a3.heic)

Novinkou ze strany Apple je pak **vydání otevřeného LLM nazvaného OpenELM**. Ten využívá strategii škálování po vrstvách k efektivnímu přidělování parametrů v rámci každé vrstvy transformačního modelu, což vede ke zvýšení přesnosti. Zjednodušeně řečeno má být trénink takového modelu levnější a výstup z něj rychlejší i přesnější. Pro zájemce [je model na GitHubu](https://github.com/apple/corenet) a k dalšímu hraní na [Hugging Face](https://huggingface.co/apple/OpenELM). 

Nervy trhu na pochodu dokladuje **údajné uvolnění GPT-5** do betaprovozu v rámci jedné služby, kde se objevil model nazvaný [GPT2-Chatbot](https://rentry.co/GPT2?utm_source=marigold.cz) \- a prý je to tajně testované GPT-5. Model sám říká, že je založený na GPT-4 technologiích. Sice jsou jeho výsledky pozoruhodné, spíše se ale také přikláním k názoru, že jde o nějakou zkušební verzi modelu vyvíjeného OpenAI a uvolněné v rámci zvyšování paniky, ale ne o testované GPT-5. Velmi názorné je vynechání onoho lomítka - mohlo by jít o druhou generaci GPT, ne o druhou verzi z roku 2019… Ale nepředbíhejme, uvidíme :)

**Github uvolnil Copilot Workspace** , což je nástroj pro vývojáře, který jim umožňuje dokončovat funkce a řešit chyby pomocí AI. 

**OpenAI uvolnilo funkci Memory** , která umožňuje zapamatovat si data a přenášet je přes jednotlivé relace, čili rozhovory. Můžete ji tak nechat si zapamtovat třeba vaše oblíbené zvíře nebo kusy textů. Zatím to ale nefunguje v EU a Korei, jinak byste si to mohli povolit v nastavení. 

Společnost **Meta vydala model Llama 3 8B a 70B** s výrazně vyšším výkonem, zejména v oblasti argumentace, délky kontextu a kódu. Stále trénuje model s parametry 400B, který se výkonem vyrovná modelu Opus. Tyto modely jsou nejvýkonnějšími dostupnými open source modely a za týden od vydání mají přes milion stažení. Pokud potřebujete použít model u sebe, vyplatí se podívat na Llamu (a ještě Mixtral).

**Boston Dynamics vydal nové humanoidní roboty** , které si nikdy nekoupíte, ale je [zajímavé vidět je na videu](https://www.youtube.com/watch?v=29ECwExc-_M) a jsou dalším výrazným posunem na poli robotiky. Zlom to ale opět není. 

A protože se v dubnu jinak nestalo v technice nic tak podstatného, podíváme se na moje stěžejní téma, které se probírá snad na všech mých firemních workshopech věnovaných umělé inteligenci. Čím by vám konkrétně AI mohla pomoci? Třeba tím, že za vás udělá zápis z porady.