---
author: Patrick Zandl
categories:
- Convex
- Supabase  
layout: post
post_excerpt: Vývojáři webových a AI aplikací stojí před rozhodnutím, které určí rychlost jejich vývoje na roky dopředu. Trh Backend-as-a-Service (BaaS) dospěl a rozdělil se do tří generací. Zatímco dříve byla volba jednoduchá _Dej tam Firebase_, dnes, v éře AI a TypeScriptu, stará řešení naráží na své limity. Pojďme se na tento vývoj podívat. 
summary_points:
- Trend Integrated Stack nahrazuje složité lepení služeb pro zrychlení vývoje AI aplikací
- Firebase a AWS Amplify naráží u moderních projektů na limity v oblasti NoSQL a složité infrastruktury
- Supabase přináší SQL renesanci s nativní podporou vektorů a odstraněním nutnosti psát API server
- Convex nabízí end-to-end TypeScript prostředí s automatickou reaktivitou a ACID transakcemi
- Fenomén Vibe coding favorizuje nástroje s silnou typovou kontrolou a minimem konfiguračních souborů
- Tradiční VPS hosting zůstává ekonomickou volbou pro provoz, ale brzdí rychlost vývoje AI funkcí
title: Konec lepení služeb - Od Firebase k modernímu Integrated Stacku (2026 Edition)
---

Vývojáři webových a AI aplikací stojí před rozhodnutím, které určí rychlost jejich vývoje na roky dopředu. Trh Backend-as-a-Service (BaaS) dospěl a rozdělil se do tří generací. Zatímco dříve byla volba jednoduchá ("Dej tam Firebase"), dnes, v éře AI a TypeScriptu, stará řešení naráží na své limity.

Pojďme se podívat na to, jak si stojí moderní vyzyvatelé (**[Convex](https://convex.dev/referral/PATRIC951), [Supabase](https://supabase.com/)**) proti zavedeným gigantům (**Firebase, AWS Amplify**).

Vývojáři totiž tráví desítky hodin psaním kódu, který nedělá nic jiného, než že přesouvá data z jedné API do druhé, řeší, co se stane, když jedna služba odpoví a druhá ne, a synchronizuje stavy. V éře AI agentů a RAG (Retrieval-Augmented Generation), kde aplikace čtou a zapisují data s vysokou frekvencí, se toto "lepidlo" stává úzkým hrdlem stability i rychlosti vývoje.

Na scénu proto přichází nový trend: **Integrated Stack** (Integrovaný stack). Dvěma nejvýraznějšími představiteli tohoto posunu, byť s odlišnou filozofií, jsou **Convex** a **Supabase**. Pojďme se na posuny od Backend as a Service k Integrovanému stacku podívat podrobněji.

## První generace: Průkopníci (Firebase)

Když Google v roce 2014 integroval [Firebase](https://firebase.google.com/) do svého ekosystému, pro vývojáře to působilo jako technologické zjevení. Byla to první generace nástrojů, která skutečně demokratizovala backend. Frontendový vývojář poprvé získal možnost postavit kompletní aplikaci bez jediného řádku konfigurace serveru. Kombinace Realtime Database (a později Firestore) s neuvěřitelně snadnou autentizací byla magická. Chatovací aplikace nebo živé dashboardy, které dříve vyžadovaly týdny práce s websockety, byly najednou hotové za odpoledne. Narodil se přístup Backend as a Service.

Jenže se začaly projevovat limity. Největším problémem zůstává samotná povaha databáze. Firestore je dokumentová NoSQL databáze, což je skvělé pro jednoduchá data, ale jakmile začnete modelovat reálný byznys – vztahy mezi entitami, transakce a integritu dat – narazíte. Místo aby tyto vazby hlídal databázový engine, píšete tuny defenzivního, špagetového kódu v aplikaci, jen abyste suplovali chybějící relační integritu.

Dnes navíc narážíme na bariéry i v oblasti výkonu a AI. Serverless funkce (Cloud Functions) stále trpí na tzv. "cold starts", které dokáží interakci s aplikací nepříjemně zbrzdit. A přidat moderní AI funkce? Podpora pro vektorové vyhledávání je řešena přes externí rozšíření (jako Genkit), která byla k platformě přilepená dodatečně. Není to nativní součást jádra, což v době, kdy jsou embeddings srdcem aplikace, prostě nestačí. Firebase zůstává legendou, která odstartovala serverless revoluci, ale pro nároky roku 2026 už potřebuje pořádný refresh.

## Druhá generace: Enterprise Wrappery (AWS Amplify)

Odpovědí Amazonu na úspěch Firebase se stalo v roce 2017 [AWS Amplify](https://aws.amazon.com/amplify/), typický zástupce druhé generace, kterou bych nazval "Enterprise Wrappery". Filozofie zněla lákavě: vezmeme průmyslové standardy jako DynamoDB, Cognito a Lambda a zabalíme je do přívětivého CLI kabátu. Obrovskou výhodou zůstává fakt, že "pod kapotou" běžíte na čistém AWS – limit škálování prakticky neexistuje a vaše infrastruktura zvládne jakýkoliv nápor.

V praxi se však Amplify často projevuje jako učebnicový příklad "děravé abstrakce". Jakmile opustíte vyšlapanou cestu jednoduchých tutoriálů, iluze komfortu se rozplyne a vy se ocitnete v pekle ladění IAM rolí a generovaných šablon CloudFormation. Z pohledu dnešních AI aplikací je to cítit dvojnásob – zprovoznění RAG pipeline zde neznamená napsat funkci, ale integrovat těžkotonážní služby jako OpenSearch nebo Bedrock. Místo vývoje produktu se tak vracíte k roli DevOps inženýra, které jste se výběrem této služby chtěli původně vyhnout.

## Třetí generace: Moderní vyzyvatelé (Supabase & Convex)

Třetí generace nástrojů přináší na scénu moderní vyzyvatele, kteří se poučili z chyb svých předchůdců. Trh se zde štěpí na dvě odlišné filozofie, z nichž každá řeší dilema "jednoduchost versus kontrola" po svém.

### Cesta A: SQL Renaissance (Supabase)

[Supabase](https://supabase.com/) ztělesňuje návrat k osvědčeným standardům. Tvůrci pochopili, že vývojáři milovali jednoduchost Firebase, ale nenáviděli omezení NoSQL. Supabase proto vzala onen přívětivý uživatelský zážitek a posadila ho na robustní základy PostgreSQL.

Zásadní inovací, která z „pouhé“ databáze dělá kompletní backendové řešení, je **odstranění API vrstvy**. Supabase umožňuje klientovi komunikovat přímo s databází, aniž byste museli psát a udržovat vlastní Node.js server pro běžné operace. Frontend se dotazuje přímo a bezpečnostní logiku, kterou dříve řešil backendový kód, přebírají robustní pravidla Row Level Security (RLS) uvnitř samotného Postgresu.

* **Odpověď na Firebase:** Místo limitujícího dokumentového modelu dostáváte plnohodnotné relační SQL s integritou dat.
* **Odpověď na AWS:** Otevřenost. Díky open-source povaze nehrozí vendor lock-in; nakonec je to „jen Postgres“, který můžete vzít a provozovat kdekoli.
* **AI:** Díky rozšíření `pgvector` se stala standardem pro AI vývojáře, kteří chtějí mít aplikační data i vektorové embeddingy na jednom místě, dotazovatelné známým jazykem SQL.

### Cesta B: The Integrated Runtime (Convex)

[Convex](https://convex.dev/referral/PATRIC951) je evolucí myšlenky Firebase, ovšem postavenou na moderních technologiích, které řeší bolesti distribuovaných systémů. V podání Convexu infrastruktura pro vývojáře v podstatě mizí a zůstává jen kód.

* **Odpověď na Firebase:** Convex se zbavil volného JSONu a nahradil ho striktním schématem a garancí ACID transakcí, čímž eliminuje stavy nekonzistentních dat.
* **Odpověď na AWS:** Totální abstrakce. Infrastruktura pro vývojáře v podstatě mizí a zůstává jen kód – žádná konfigurace serverů či kontejnerů.
* **AI:** V kontextu umělé inteligence jde Convex nejdál: vektorové vyhledávání a plánování úloh nejsou externí služby, ale přirozená součást transakčního toku, což zjednodušuje architekturu AI aplikací na naprosté minimum.

## Příklad, kde se láme chleba: AI a RAG

Při vývoji AI aplikací je klíčová práce s vektory (embeddings) a kontextem. Zde se rozdíly v přístupech projevují nejvíce.

### Přístup Supabase: Síla `pgvector`

Supabase sází na rozšíření PostgreSQL `pgvector`.

* **Jak to funguje:** Vektory jsou jen dalším sloupcem v tabulce. Můžete dělat složité SQL dotazy, které kombinují fulltextové vyhledávání, filtrování podle metadat (např. `user_id`) a vektorovou podobnost v jednom kroku.
* **Pro koho:** Pro týmy, které potřebují maximální kontrolu nad indexováním (HNSW, IVFFlat) a chtějí využívat široký ekosystém nástrojů (LangChain, LlamaIndex), které mají pro Postgres přímou podporu.

### Přístup Convex: Transakční paměť

Convex integroval vektorové vyhledávání přímo do svého transakčního enginu.

* **Jak to funguje:** Vložení dokumentu a jeho vektoru probíhá v jedné ACID transakci. Nemůže se stát, že se text uloží, ale vektor ne. Vyhledávání je nativní TypeScript metoda.
* **Pro koho:** Pro vývojáře produktů, kteří nechtějí spravovat synchronizaci mezi "zdrojem pravdy" a "vektorovým indexem". Umožňuje to extrémně rychlou iteraci při tvorbě AI agentů, kteří potřebují "paměť".

## Éra vibecodingu

Popularita Supabase i mladšího Convexu raketově vzrostla souběžně s nástupem vibe codingu na sklonku roku 2024 a hlavně v polovině roku 2025. Proč jsou Convex a Supabase králové Vibe Codingu?

První důvod je prostý: vývojáři jsou přeci jen konzervativní a chvíli jim trvá, než novinku absorbují, jakkoliv je výhodná.

Druhý důvod je paradoxní – oba nástroje jsou skvěle popsané pro použití v AI. Klíčem je **"Low Context, High Power"**. AI modely (jako Claude Sonnet v Cursoru/CC) mají omezené kontextové okno a "pozornost". Čím méně souborů a konfigurace musí AI číst, tím lépe kóduje. Supabase i Convex se tomu okamžitě přizpůsobily a vibe kódovací nástroje se s nimi rychle naučily.

### Convex: skvělá typová bezpečnost pro AI

Convex je pro vibe coding pravděpodobně nejefektivnější volba současnosti z jednoho prostého důvodu: **End-to-End TypeScript.**

* **Jeden jazyk, jedna pravda:** AI vidí soubor `schema.ts` na backendu a okamžitě ví, jaké typy má použít v React komponentě na frontendu. Nemusí halucinovat API endpointy.
* **Žádné "přemostění":** V tradičním stacku by AI musela vygenerovat SQL migraci, pak backend kontroler, pak API definici a nakonec frontend fetch. V Convexu AI napíše jednu TypeScript funkci a frontend ji hned volá. Šance na chybu se radikálně snižuje.
* **Reaktivita:** AI nemusí psát logiku pro `useEffect` nebo manuální aktualizaci stavu. Prostě použije `useQuery` a "ono to funguje". To odpovídá mentalitě vibe codingu – rychle vidět výsledek.

### Supabase: Standard, který LLM znají nazpaměť

Supabase vítězí díky tomu, že LLM modely (trénované na celém internetu) perfektně znají **PostgreSQL** a **SQL**.

* **Odstranění backendu:** Jak jsme zmínili, Supabase umožňuje volat databázi přímo z klienta (`supabase.from('users').select()`). Pro AI je mnohem snazší vygenerovat tento jeden řádek v komponentě, než psát celý Express/NestJS backend.
* **SQL je deklarativní:** AI je extrémně dobrá v psaní SQL a definování tabulek. Stačí napsat do chatu v Cursoru: *"Vytvoř mi tabulku pro blog posty s RLS, aby je mohl editovat jen autor"*, a Supabase (resp. AI) vygeneruje přesné SQL, které stačí spustit.

## A co PHP či Python na vlastním VPS?

A co ten starý dobrý svět českého levného hostingu, kam strčíte pár PHP souborů za desetikačku měsíčně? Samozřejmě, používat PHP (např. Laravel) nebo Python (Django/FastAPI) na vlastním VPS je stále **naprosto validní, levná a robustní cesta**. Na této architektuře běží většina internetu.

V kontextu rychlého vývoje pomocí vibe codingu ovšem existují vážné důvody, proč se vývojáři přesouvají k řešením jako Convex nebo Supabase.

Není to o tom, že by PHP bylo špatné, ale o tom, že **tradiční stack klade AI (a vývojáři) do cesty více překážek.**

### 1. Problém "Kontextového okna" u AI

AI modely mají omezenou "paměť" (kontext). Čím více souborů jim musíte ukázat, aby pochopily, co chcete změnit, tím hůře pracují.

* **Tradiční stack (MVC - Laravel/Django):** Abyste přidali jednu funkci, musíte často upravit 4-5 souborů: Migraci (DB), Model, Controller, Route definici a View (šablonu). AI se v tom může ztratit nebo zapomenout upravit jeden ze souborů.
* **Moderní stack (Convex/T3):** Díky principu "Locality of Behavior" je často backendová funkce i frontendové volání ve velmi úzkém propojení (nebo v jednom souboru). AI vidí vše na jednom místě a dělá méně chyb.

### 2. DevOps je zabiják "Flow"

Vibe coding je o rychlosti myšlenky. "Napadne mě to -> AI to napíše -> vidím to."

* **VPS:** Musíte řešit SSH klíče, aktualizace Linuxu, konfiguraci Nginx/Apache, SSL certifikáty (Certbot), nastavení Firewallu, verzování databáze, CI/CD pipeliny pro nasazení. Každá tato činnost vás vytrhne z "vibe" kódování aplikace.
* **Managed (Convex/Vercel/Supabase):** Napíšete příkaz `npx convex deploy` (nebo jen pushnete do Gitu) a je to online. Infrastruktura je pro vývojáře neviditelná.

### 3. Typová kontrola vs. Halucinace

Toto je kritický bod pro práci s AI.

* **PHP/Python:** Jsou to (většinou) dynamické jazyky. Pokud AI vymyslí metodu, která neexistuje (halucinuje), často to zjistíte až ve chvíli, kdy aplikaci spustíte a ona spadne na Error 500.
* **TypeScript (Convex stack):** Pokud AI vymyslí neexistující funkci, editor (VS Code/Cursor) to okamžitě podtrhne červeně. Zpětná vazba je v milisekundách. AI se dokáže v TypeScriptu "opravit sama" mnohem lépe než v Pythonu, protože typový systém ji vede za ruku.

### 4. Real-time je v PHP/Pythonu složitý

Dnešní aplikace (chaty, notifikace, kolaborace) vyžadují reálný čas.

* **VPS:** HTTP protokol je bezstavový. Pro real-time musíte na server instalovat další služby (Redis, WebSockets server), řešit long-polling nebo platit za Pusher. Je to spousta "lepidla" navíc.
* **Convex/Supabase:** Reálný čas je výchozí stav. Nemusíte nic instalovat. Pro AI je snadné napsat chat, protože jen použije `useQuery`, které se samo aktualizuje.

---

### Kdy je naopak PHP/Python a VPS lepší volba?

Abychom byli fér, existují scénáře, kdy je "stará škola" lepší:

1.  **Cena při škálování:** VPS má fixní cenu (např. 5 $ měsíčně). Serverless řešení (Convex, Vercel) mohou být při obrovském provozu drahá (platíte za využití).
2.  **Dlouhotrvající procesy:** Serverless funkce mají limity (např. musí doběhnout do 60 sekund). Pokud potřebujete, aby Python skript chroustal data 10 minut, VPS je nutnost.
3.  **Data Sovereignty:** Pokud chcete mít 100% kontrolu nad tím, kde fyzicky leží vaše data a nechcete záviset na americké nebo čínské firmě, vlastní server je jistota.
4.  **Python pro AI Backend:** Pokud vaše aplikace dělá těžké AI výpočty (ne jen volání API, ale běh vlastních modelů v PyTorch/TensorFlow), Python na GPU serveru je jediná rozumná volba.

---

## Verdikt pro rok 2026: Co vybrat?

* **Zůstaňte u Firebase, pokud:** Udržujete starší mobilní aplikace nebo potřebujete specifické integrace s Google Analytics/Ads. Pro nové webové AI projekty je ale často limitující svým dokumentovým modelem a absencí nativních vektorů.
* **Zvolte AWS Amplify, pokud:** Jste korporace s přísnými požadavky na compliance, máte tým certifikovaných AWS inženýrů a "Time-to-market" není absolutní prioritou. Zvolte ho, pokud potřebujete infrastrukturu, která "neuhne" ani o milimetr.
* **Zvolte Supabase, pokud:** Chcete moderní stack, milujete SQL, bojíte se vendor lock-inu a chcete mít možnost aplikaci v budoucnu hostovat sami. Je to bezpečná volba "zlaté střední cesty" pro většinu standardních projektů.
* **Zvolte Convex, pokud:** Chcete maximální rychlost vývoje (Developer Experience) a naskakujete na vlnu "Vibe Codingu". Stavíte komplexní, reaktivní aplikaci (např. kolaborativní nástroj nebo AI agenta) a jste ochotni vyměnit "standardní SQL" za "dokonalou integraci TypeScriptu" a automatickou reaktivitu.
* **Zvolte tradiční VPS (PHP/Python), pokud:** Je pro vás prioritou **cena provozu** a **nezávislost**. Frameworky jako Laravel (PHP) nebo Django/FastAPI (Python) jsou extrémně stabilní a na pronajatém serveru (Hetzner/DigitalOcean) vyjdou násobně levněji než serverless cloudy. Je to ideální volba, pokud potřebujete spouštět těžké výpočty (např. vlastní Python AI modely) nebo pokud vám nevadí investovat čas do správy serveru (DevOps) výměnou za plnou kontrolu.

### A co self-host "Indie" řešení?

Pro menší projekty nebo interní nástroje stojí za zmínku **PocketBase** nebo **Appwrite**. Nabízejí podobný zážitek jako Firebase/Supabase (tedy backend v krabičce), ale v balení, které snadno nasadíte na levný VPS za $5 měsíčně.

Pro škálování globálních AI aplikací sice často postrádají pokročilou edge infrastrukturu, kterou nabízí Convex nebo Supabase Cloud, a při extrémní zátěži se s nimi budete více potýkat – ale buďme upřímní: v běžném českém prostředí (tisíce až desítky tisíc uživatelů) na tyto limity narazíte spíše výjimečně.