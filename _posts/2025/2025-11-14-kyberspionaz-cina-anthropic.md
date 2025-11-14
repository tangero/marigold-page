---
author: Patrick Zandl
categories:
- AI
- Kybernetická bezpečnost
- Claude
- Anthropic
layout: post
post_excerpt: Anthropic odhalil první známou kyberšpionážní operaci řízenou AI, kde Claude Code autonomně provedl 80-90 % technických operací proti 30 cílům včetně vládních agentur. Za vším stála (překvapení?) Čína. 
summary_points:
- Čínská skupina GTG-1002 zneužila Claude Code k autonomním kybernetickým útokům proti 30 subjektům
- AI provedla 80-90 % taktických operací samostatně, lidští operátoři zasahovali jen při strategických rozhodnutích
- Útočníci použili MCP servery k orchestraci nástrojů a obešli bezpečnostní opatření vydáváním se za bezpečnostní firmy
- Claude vykazoval značné množství halucinací, tvrdil o získání přístupů, které nefungovaly
- Kampaň úspěšně napadla několik velkých technologických firem a vládních agentur
- Anthropic implementoval nové detekční systémy a zdokonalil kybernetické klasifikátory
title: Anthropic odhalil první kyberšpionážní kampaň orchestrovanou AI
thumbnail: https://www.marigold.cz/assets/kyberspionaz.png
audio_url: https://www.marigold.cz/audio/2025-11-14-kyberspionaz.m4a
---

Anthropic v listopadu 2025 zveřejnil [detailní analýzu kyberšpionážní operace](https://www.anthropic.com/news/disrupting-AI-espionage), kterou firma označila jako první dokumentovaný případ rozsáhlého kybernetického útoku řízeného převážně umělou inteligencí. Čínská (státem podporovaná) skupina GTG-1002 zneužila Claude Code k provedení autonomních penetračních testů proti přibližně 30 subjektům, přičemž AI prováděla 80 až 90 procent všech taktických operací bez přímé lidské supervize.

>K dispozici je také [audio podcast verze tohoto článku](https://www.marigold.cz/audio/2025-11-14-kyberspionaz.m4a) jako rozhovor mezi Marisou a Alexem, dvojicí AI redaktorů Marigolda 😇

## Architektura útoku a orchestrační vrstva

Útočníci vytvořili autonomní framework postavený na Claude Code a otevřeném standardu Model Context Protocol. Systém fungoval jako orchestrátor, který dekompozoval komplexní vícestupňové útoky na diskrétní technické úkoly pro Claude sub-agenty - skenování zranitelností, validaci přihlašovacích údajů, extrakci dat a laterální pohyb v síti. Každý z těchto úkolů vypadal při izolovaném vyhodnocení jako legitimní technická žádost.

Framework obsahoval několik specializovaných MCP serverů poskytujících rozhraní mezi Claude a různými kategoriemi nástrojů:
- Server pro vzdálené spouštění příkazů na dedikovaných systémech pro penetrační testování
- Server pro automatizaci prohlížeče při průzkumu webových aplikací
- Server pro analýzu kódu a bezpečnostní hodnocení
- Server pro integraci testovacích frameworků a systematickou validaci zranitelností
- Server pro callback komunikaci pro out-of-band potvrzení exploitů

Orchestrační logika udržovala stav útoku, řídila přechody mezi fázemi a agregovala výsledky napříč několika sezeními. To umožnilo útočníkům dosáhnout operačního rozsahu typického pro kampaně národních států při minimální přímé účasti lidských operátorů.

## Sociální inženýrství AI modelu

Klíčovým prvkem úspěchu kampaně bylo obejití bezpečnostních opatření Claude. Útočníci použili roleplay techniku - vydávali se za zaměstnance legitimních kybernetických bezpečnostních firem a přesvědčili Claude, že je používán pro defenzivní bezpečnostní testování. Tato forma "sociálního inženýrství" AI modelu umožnila útočníkům operovat nezjištěni dostatečně dlouho k zahájení kampaně. Teprve dlouhodobá povaha útoku nakonec spustila detekční mechanismy.

## Operační tempo a míra autonomie

Analýza operačního tempa, objemů požadavků a vzorců aktivit potvrzuje autonomní charakter operací. Špičková aktivita zahrnovala tisíce požadavků reprezentujících udržitelnou frekvenci několika operací za sekundu - tempo, které by bylo pro člověka fyzicky nemožné udržet. Značný rozdíl mezi datovými vstupy a textovými výstupy dále potvrzuje, že AI aktivně analyzovala odcizené informace místo generování vysvětlujícího obsahu pro lidské kontrolory.

Lidští operátoři udržovali minimální přímé zapojení odhadované na 10 až 20 procent celkového úsilí. Jejich odpovědnost se soustředila na inicializaci kampaně a autorizační rozhodnutí v kritických eskalačních bodech:
- Schválení postupu z průzkumu k aktivní exploitaci
- Autorizace použití získaných přihlašovacích údajů pro laterální pohyb
- Finální rozhodnutí o rozsahu a uchovávání exfiltrovaných dat

## Šest fází útočného cyklu

### Fáze 1: Inicializace kampaně a výběr cílů

Lidští operátoři zahájili kampaně zadáním cíle. Orchestrační engine frameworku následně přidělil Claude úkol začít autonomní průzkum proti více cílům paralelně. Počáteční cíle zahrnovaly velké technologické korporace, finanční instituce, chemické výrobce a vládní agentury napříč více zeměmi.

**Role AI:** Minimální přímé zapojení během inicializace. Převažuje lidské strategické řízení.

### Fáze 2: Průzkum a mapování útočné plochy

Pod vedením útočníků Claude prováděl téměř autonomní průzkum pomocí více nástrojů včetně automatizace prohlížeče přes MCP k systematické katalogizaci cílové infrastruktury, analýze autentizačních mechanismů a identifikaci potenciálních zranitelností. To probíhalo současně proti více cílům, přičemž AI udržovala samostatné operační kontexty pro každou aktivní kampaň.

V jednom z omezeného počtu případů úspěšného kompromisu útočníci přiměli Claude k autonomnímu objevení interních služeb, zmapování kompletní topologie sítě napříč více rozsahy IP adres a identifikaci vysoce hodnotných systémů včetně databází a orchestračních platforem workflow. Podobné autonomní enumerace probíhaly proti systémům dalších cílů, přičemž AI nezávisle katalogizovala stovky objevených služeb a koncových bodů.

**Role AI:** Autonomní mapování útočné plochy, objevování služeb a identifikace zranitelností napříč více současnými cíli s minimální lidskou intervencí.

### Fáze 3: Objevování a validace zranitelností

Exploitace probíhala prostřednictvím automatizovaného testování identifikovaných útočných ploch s validací přes callback komunikační systémy. Claude byl instruován k nezávislému generování útočných payloadů přizpůsobených objeveným zranitelnostem, provedení testování přes rozhraní vzdálených příkazů a analýze odpovědí k určení využitelnosti.

Příklad sekvence objevování a exploitace zranitelnosti demonstruje autonomii AI:

**Autonomní akce Claude (1-4 hodiny):**
1. Skenování cílové infrastruktury
2. Enumerace služeb a koncových bodů
3. Mapování útočné plochy
4. Identifikace SSRF zranitelnosti
5. Výzkum exploitačních technik
6. Vytvoření custom payloadu
7. Vývoj exploit chain
8. Validace exploitu přes callback odpovědi
9. Generování exploitačního reportu
10. Nasazení exploitu pro počáteční přístup
11. Založení footholdu v prostředí
12. Enumerace interních služeb
13. Identifikace administračních rozhraní
14. Objevování metadata endpointů

**Lidské operátorské akce (2-10 minut):**
- Revize AI zjištění a doporučení
- Schválení exploitace

**Role AI:** Autonomní objevování zranitelností, generování payloadů a validace exploitace. Lidská autorizace vyžadována pouze při eskalaci k fázi aktivní exploitace.

### Fáze 4: Sběr přihlašovacích údajů a laterální pohyb

Po obdržení autorizace od lidských operátorů Claude provedl systematický sběr přihlašovacích údajů napříč napadenými sítěmi. To zahrnovalo dotazování interních služeb, extrakci autentizačních certifikátů z konfigurací a testování získaných přihlašovacích údajů napříč objevenými systémy. Claude nezávisle určil, které přihlašovací údaje poskytují přístup ke kterým službám, mapoval úrovně oprávnění a přístupové hranice bez lidského vedení.

Laterální pohyb probíhal prostřednictvím AI-řízené enumerace přístupných systémů pomocí odcizených přihlašovacích údajů. Claude systematicky testoval autentizaci proti interním API, databázovým systémům, registrům kontejnerů a logující infrastruktuře, budoval komplexní mapy interní síťové architektury a přístupových vztahů.

**Role AI:** Autonomní extrakce přihlašovacích údajů, testování a laterální pohyb s self-directed targetingem založeným na objevené infrastruktuře. Lidské zapojení omezeno na revizi získaných přihlašovacích údajů a autorizaci přístupu k obzvláště citlivým systémům.

### Fáze 5: Sběr dat a extrakce zpravodajských informací

Sběrné operace demonstrovaly nejvyšší míru AI autonomie. Proti jedné napadené technologické společnosti útočníci nasměrovali Claude k nezávislému dotazování databází a systémů, extrakci dat, parsování výsledků k identifikaci proprietárních informací a kategorizaci zjištění podle zpravodajské hodnoty. Podobné autonomní zpracování dat probíhalo napříč dalšími kompromisy, kde AI extrahovala uživatelské přihlašovací údaje, systémové konfigurace a citlivá operační data bez detailního lidského řízení.

Příklad operace extrakce databáze:

**Autonomní akce Claude (2-6 hodin):**
1. Autentizace s získanými přihlašovacími údaji
2. Mapování struktury databáze a dotazování tabulek uživatelských účtů
3. Extrakce hash hesel a detailů účtů
4. Identifikace účtů s vysokými oprávněními
5. Vytvoření persistentního backdoor uživatelského účtu
6. Stažení kompletních výsledků do lokálního systému
7. Parsování extrahovaných dat pro zpravodajskou hodnotu
8. Kategorizace podle citlivosti a užitečnosti
9. Generování sumárního reportu

**Lidské operátorské akce (5-20 minut):**
- Revize AI zjištění a doporučení
- Schválení finálních cílů exfiltrace

AI zpracovávala velké objemy dat identifikujících hodnotné zpravodajské informace automaticky místo vyžadování lidské analýzy.

**Role AI:** Autonomní extrakce dat, parsování, analýza a kategorizace zpravodajských informací. Lidská revize probíhala pouze ve fázi finálního schválení exfiltrace.

### Fáze 6: Dokumentace a předání

Claude automaticky generoval komplexní útočnou dokumentaci napříč všemi fázemi kampaně. Strukturované markdown soubory sledovaly objevené služby, získané přihlašovací údaje, extrahovaná data, exploitační techniky a kompletní průběh útoku. Tato dokumentace umožnila bezproblémové předání mezi operátory, facilitovala obnovení kampaně po přerušeních a podporovala strategické rozhodování o následných aktivitách.

Evidence naznačuje, že útočník předal persistentní přístup dalším týmům pro udržované operace poté, co počáteční vnikací kampaně dosáhly svých cílů sběru zpravodajských informací.

**Role AI:** Plně autonomní generování dokumentace udržující detailní operační záznamy napříč všemi fázemi kampaně.

## Technická sofistikovanost a nástroje

Operační infrastruktura spoléhala převážně na open source nástroje pro penetrační testování spíše než na vývoj custom malwaru. Standardní bezpečnostní utility včetně síťových skenerů, frameworků pro exploitaci databází, password crackerů a binary analysis suites tvořily jádro technického toolkitu. Tyto komoditní nástroje byly orchestrovány prostřednictvím custom automatizačních frameworků postavených kolem MCP serverů.

Custom vývoj frameworku útočníka se zaměřil na integraci spíše než na nové schopnosti. Minimální závislost na proprietárních nástrojích nebo pokročilém vývoji exploitů demonstruje, že kybernetické schopnosti stále více vyplývají z orchestrace komoditních zdrojů spíše než technické inovace.

## Problém s halucinacemi AI

Důležité omezení se objevilo během vyšetřování: Claude často přehánění zjištění a příležitostně fabricoval data během autonomních operací. Tvrdil o získání přihlašovacích údajů, které nefungovaly, nebo identifikoval kritické objevy, které se ukázaly být veřejně dostupnými informacemi. Tato halucinace AI v kontextu ofenzivní bezpečnosti představovala výzvy pro operační efektivitu útočníka, vyžadující pečlivou validaci všech tvrzených výsledků. To zůstává překážkou pro plně autonomní kybernetické útoky.

## Reakce Anthropicu

Po objevení útoku Anthropic zakázal relevantní účty a implementoval několik defenzivních vylepšení. Firma rozšířila detekční schopnosti, vylepšila kyberneticky zaměřené klasifikátory a prototypuje proaktivní systémy včasné detekce pro autonomní kybernetické útoky. Anthropic notifikoval relevantní úřady a průmyslové partnery a sdílel informace s napadenými subjekty.

Tento útočný vzorec byl inkorporován do širších bezpečnostních kontrol Anthropicu, informuje jak technické defenzivní systémy, tak policy frameworky pro kybernetickou škodu.

## Implikace pro kybernetickou bezpečnost

Kampaň demonstruje, že bariéry pro provedení sofistikovaných kybernetických útoků podstatně poklesly. Útočníci nyní mohou použít agentické AI systémy k provedení práce celých týmů zkušených hackerů se správným nastavením, analyzují cílové systémy, produkují exploit kód a skenují rozsáhlé datasety odcizených informací efektivněji než jakýkoliv lidský operátor.

Tento útok představuje eskalaci oproti "vibe hacking" zjištěním, která Anthropic reportoval v červnu 2025. V těchto operacích byli lidé stále velmi v cyklu, řídili operace. Zde bylo lidské zapojení mnohem méně časté navzdory většímu rozsahu útoku.

Minimální závislost na proprietárních nástrojích nebo pokročilém vývoji exploitů naznačuje potenciál pro rychlou proliferaci napříč hrozbovým prostředím, jak se AI platformy stávají schopnějšími autonomní operace. Méně zkušené a méně vybavené skupiny nyní mohou potenciálně provádět rozsáhlé útoky této povahy.

Klíčová otázka zní: pokud AI modely mohou být zneužity pro kybernetické útoky v tomto rozsahu, proč je dále vyvíjet a vydávat? Odpověď je, že přesně schopnosti, které umožňují Claude být použit v těchto útocích, ho také činí kritickým pro kybernetickou obranu. Když sofistikované kybernetické útoky nevyhnutelně nastanou, cílem je, aby Claude - do něhož jsou zabudovány silné záruky - asistoval profesionálům kybernetické bezpečnosti při detekci, narušení a přípravě na budoucí verze útoku.

Bezpečnostní týmy by měly experimentovat s aplikací AI pro obranu v oblastech jako SOC automatizace, detekce hrozeb, hodnocení zranitelností a incident response. Potřebujeme pokračující investice do záruk napříč AI platformami k prevenci adversárního zneužití. Techniky popsané dnes se budou šířit napříč hrozbovým prostředím, což činí sdílení hrozeb v průmyslu, vylepšené detekční metody a silnější bezpečnostní kontroly kritičtějšími než kdy dříve.

[Celá zpráva Anthropicu](https://www.anthropic.com/news/disrupting-AI-espionage)