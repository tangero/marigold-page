---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- agenti
layout: post
post_excerpt: OpenAI, Anthropic a Google představili v krátkém sledu nové AI nástroje pro zdravotnictví. Nerozumíte lékařské zprávě? Přečte vám ji. Doktorovi poradí se snímkem či mu pomůže hlídat vaši medikaci. Ideální? Ve skutečnosti jde o souboj tří přístupů ke zdravotnictví a miliardovému trhu... 
summary_points:
- OpenAI, Anthropic a Google představili v krátkém sledu nové AI nástroje pro zdravotnictví.
- Produkty jako ChatGPT Health a Claude for Healthcare mají pomoci s orientací v lékařských datech.
- Skutečným cílem je ovládnout rozhraní mezi uživatelem a jeho zdravotními záznamy.
- Načasování oznámení odpovídá konání významné konference J.P. Morgan Healthcare Conference.
- Technologičtí giganti usilují o integraci do systémů pojišťoven, nemocnic a farmaceutických firem.
title: Závod o vaše zdravotní záznamy
thumbnail: https://anonyviet.com/wp-content/uploads/2026/01/chatgpt-health-5.jpg
---

Nejprve OpenAI, o den později Anthropic a nyní i Google spustili konkurenční zdravotnické produkty založené na umělé inteligenci. Nejde o to vám pomoci, ale o to, stát se rozhraním mezi vámi a vašimi zdravotními daty. Protože tam jsou peníze. A jak víme, peníze AI potřebuje, aby mohla žít. 

Během pouhých několika dnů tohoto měsíce oznámili tři technologičtí giganti produkty, které "mění pravidla hry". Alespoň tak se všichni tváří. Dne 7. ledna představila OpenAI službu  **ChatGPT Health**. 11. ledna spustil Anthropic službu  **Claude for Healthcare**. A pouhé dva dny na to, 13. ledna, Google tiše vypustil  **MedGemma 1.5**  a  **MedASR**. Všichni slibují, že vám pomohou porozumět výsledkům laboratorních testů, připravit se na návštěvy lékaře a orientovat se v matoucí složitosti moderní medicíny. Včetně napojení na vaše chytrá zařízení, která o vás produkují mraky dat, jimž stejně už nevěnujete pozornost, nesledujete je a vlastně jim nerozumíte, kromě toho, že jste rádi, že jste udělali 10 000 kroků. 

Načasování nebylo náhodné. Všechna oznámení byla směřována kolem důležité konference  **J.P. Morgan Healthcare Conference**  v San Franciscu (12.–15. ledna), kde se uzavírají ty největší obchody ve zdravotnictví. Nešlo o uvedení produktů pro spotřebitele. Byla to nabídka pro nemocnice, pojišťovny a farmaceutické společnosti v hodnotě stovek miliard potenciálních příjmů. A kolem takové akce nejde se neochomýtnout s připravenými podklady, když chcete v oboru něco znamenat. 

Sázky nemohou být vyšší. Ten, kdo se stane výchozím rozhraním mezi vámi a vašimi zdravotními daty, získá jeden z největších trhů na světě.

#### Čísla, která vše vysvětlují

OpenAI ve svém oznámení uvedla statistiku, která vysvětluje celou strategii:  **230 milionů lidí se každý týden ptá ChatGPT na otázky týkající se zdraví.**  To není překlep. Více než čtvrtina z jejich 800+ milionů týdenních uživatelů již používá ChatGPT jako lékařský zdroj. Někteří chtějí interpretovat lékařskou zprávu, jiní chtějí poradit, jaký si vzít lék na rýmičku nebo si jen přidávají druhý názor k tomu, co jim řekl lékař. Či ani k doktorovi nejdou, protože to prostě v jejich zemi je drahé. 

Odhaduje se, že trh s AI ve zdravotnictví dosáhne do roku 2034 hodnoty 696 miliard dolarů. Zdravotnictví představuje jeden z významných sektorů globální ekonomiky – jen v USA jde o průmysl v hodnotě 4,9 bilionu dolarů. Pro AI společnosti, které utrácejí miliardy za výpočetní náklady, to je  **TA**  příležitost.

Průzkum AMA zjistil, že 66 % amerických lékařů využívalo AI ve své praxi v roce 2024, což je nárůst z pouhých 38 % v roce 2023. Otázkou není, zda AI přetvoří zdravotnictví. Otázkou je, kdo ji bude ovládat.

### Co ve skutečnosti nabízejí: Tři různé cesty

Zatímco OpenAI a Anthropic budují „uzavřené zahrady“, Google zvolil jinou strategii.

1.  **OpenAI (ChatGPT Health):**  Vytváří izolované prostředí (sandbox), kde jsou konverzace o zdraví šifrovány a odděleny. Partnerství s  **b.well**  zajišťuje napojení na systémy poskytovatelů. A data se nemíchají s jinými konverzacemi v ChatGPT, nebojte se 🤡
    
2.  **Anthropic (Claude for Healthcare):**  Cílí silně na podniky přes partnerství s  **HealthEx**  a  **Function Health**. Zaměřuje se na procesy a infrastrukturu kompatibilní s HIPAA, tedy s tím, co je v USA povinné či důležité.
    
3. **Google (MedGemma 1.5 & MedASR):**  Místo hotové aplikace Google 13. ledna uvolnil  **open-source modely**.

-   **MedGemma 1.5**  je multimodální model schopný analyzovat nejen text, ale i  **vysokorozměrné snímky**  – dokáže číst 3D CT skeny, MRI a celé histopatologické snímky, což konkurence zatím neumí.
    
-   **MedASR**  je specializovaný model pro převod řeči na text, který rozumí lékařskému žargonu a diktátu.
    

Tím, že Google nabízí tyto modely jako „open weights“, umožňuje nemocnicím provozovat AI na vlastních serverech (on-premise), čímž obchází obavy o soukromí dat, které trápí cloudová řešení OpenAI a Anthropicu.

**Google navíc okamžitě mobilizuje armádu vývojářů.**  Souběžně s vydáním modelu spustil na platformě Kaggle soutěž  **MedGemma Impact Challenge**. Strategie je jasná: zatímco konkurence musí najímat drahé obchodní týmy, Google prostřednictvím soutěže efektivně outsourcuje inovace na globální komunitu. Motivuje tisíce nezávislých datových vědců, aby našli ta nejlepší využití pro jeho modely a vyřešili za něj „poslední míli“ implementace. Google sází na to, že vybuduje ekosystém dříve, než se uzavřená řešení konkurence stihnou masově rozšířit.

Jaký přístup je ten správný? Inu, já bych hlasoval pro soukromí, jenže také si uvědomuju, že soukromí je mnohdy "obtěžující", komplikuje technickou integraci a lidé jej ani příliš nepožadují. Takže ještě uvidíme, kudy poběží "zajíc". 

### Stíny nad vstupem AI na zdravotnický trh

Důležité je to, co společnosti ve svých oznámeních nezmínily:  **žaloby**.

OpenAI čelí žalobám za zavinění smrti z nedbalosti (případ Adama Rainea), kde je obviňována z toho, že její chatbot nezabránil sebevraždám uživatelů. Character.AI (nyní s vazbami na Google) nedávno urovnal podobné spory. Soudy začínají rozhodovat, že AI může být považována za „produkt“, což otevírá dveře k odpovědnosti za "vadu výrobku". Což by obnášel zodpovědnost "výrobce" za to, co její produkt způsobí. 

Na tomto pozadí firmy uvádějí produkty určené k diskuzi o zdraví a lékařském rozhodování. Ta kognitivní disonance je pozoruhodná.

### Skutečným zákazníkem nejste vy

Spotřebitelské produkty jsou jen viditelnou vrstvou. Skutečnou strategií je  **B2B**.

-   **OpenAI**  již zavádí „ChatGPT for Healthcare“ v nemocnicích jako Boston Children's či Stanford Medicine.
    
-   **Anthropic**  se zaměřuje na automatizaci „předběžné autorizace“ (prior authorization) pro pojišťovny a farmaceutické firmy jako Novo Nordisk.
    
-   **Google**  s MedGemma cílí na vývojáře a radiologická oddělení. Schopnost modelu analyzovat  **časové řady rentgenových snímků**  (porovnat váš dnešní snímek s tím z minulého roku) je přesně to, za co jsou nemocnice ochotny platit miliony, aby zrychlily diagnostiku.
    

Spotřebitelské produkty slouží dvěma účelům: budují značku a generují tréninková data. Nejste jen zákazník. Jste také (a často především) zdroj tréninkových dat.

### Otázky, na které nikdo neodpovídá

Mezera v přesnosti zůstává. Ačkoliv Google tvrdí, že MedGemma 1.5 má o 14 % vyšší přesnost u MRI nálezů než předchozí verze a Claude exceluje v lékařských výpočtech, chybovost není nulová. U složitých úkolů tyto modely stále selhávají v desítkách procent případů. Co to znamená? Že třem lidem z deseti je řečena špatná diagnóza, což je záležitost, kterou nemůžete ignorovat.

Kdo nese odpovědnost, když AI přehlédne nádor na CT skenu, který MedGemma analyzovala?  Lékař? Nemocnice? Nebo Google, který poskytl open-source kód s disclaimerem? V tom ještě bude "veselo". Za lékaře ručí nemocnice. Bude ručit za kód? 

#### Problém nevyhnutelnosti

Závod o vaše zdravotní záznamy je v plném proudu. Máme zde tři giganty s odlišnými zbraněmi:

-   OpenAI s masivní uživatelskou základnou.
    
-   Anthropic s důrazem na bezpečnost a procesy.
    
-   Google s hlubokou technologickou expertízou v zobrazovacích metodách (imaging).
    
Cílovou páskou je budoucnost, kde AI sedí mezi vámi a každým zdravotním rozhodnutím. Zda to bude utopie nebo dystopie, závisí na tom, kdo vyhraje a jaká pravidla nastavíme. Nastavíme? Nenastavujeme je - právě o ně vzplane obchodní válka a americká administrativa rozhodně nebude nic nastavovat...