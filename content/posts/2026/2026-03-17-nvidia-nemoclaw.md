---
slug: 'nvidia-nemoclaw'

author: Patrick Zandl 
categories:
- AI
- NVIDIA
- OpenClaw
- OpenShell
- bezpečnost
- agentní AI 
summary_points:
- NVIDIA na konferenci GTC 2026 oznámila NemoClaw, open-source stack pro bezpečné nasazení autonomních agentů OpenClaw
- Jádrem je nový runtime OpenShell, který agenty izoluje v sandboxu s řízeným přístupem k souborům, síti a systémovým voláním
- NemoClaw kombinuje lokální modely Nemotron s bezpečnostními politikami a směrovačem soukromí pro hybridní lokální/cloudový provoz
- Na kompatibilitě s OpenShell spolupracují CrowdStrike, Cisco, Google a Microsoft Security
- OpenShell je v alfa fázi a zatím podporuje pouze režim jednoho uživatele — podnikové nasazení je výhled, ne realita
- OpenClaw zůstává rizikovým softwarem s dokumentovanými bezpečnostními incidenty, NemoClaw řeší jen část problému 
title: "NVIDIA NemoClaw: bezpečnostní pancíř pro OpenClaw, nebo chytrá cesta k vendor lock-inu?"
thumbnail: https://www.marigold.cz/assets/NVIDIA-NemoClaw-Jensen.jpg
---

NVIDIA právě představila průlomové řešení, které na první pohled nezní nijak průlomově. Na konferenci GTC 2026 v San José představila [NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/), tedy open-source stack, který má řešit chronický problém agentní platformy OpenClaw. Bezpečnost. 

OpenClaw je nejrychleji rostoucí open-source projekt v historii GitHubu s více než 300 tisíci hvězdami na Githubu za necelé dva měsíce, funguje jako autonomní AI agent běžící nepřetržitě na uživatelově počítači. Jenže agent s přístupem k souborům, e-mailu, shellu a síti je z bezpečnostního hlediska noční můra. NemoClaw přidává mezi agenta a infrastrukturu novou vrstvu — runtime [OpenShell](https://github.com/NVIDIA/OpenShell), který vynucuje bezpečnostní politiky mimo dosah samotného agenta. Instalace jedním příkazem, licence Apache 2.0. Zní to dobře, ale realita je složitější.

## Co je OpenClaw a proč potřebuje bezpečnostní vrstvu

OpenClaw (dříve Clawdbot a Moltbot) vytvořil rakouský vývojář Peter Steinberger, zakladatel firmy PSPDFKit, kterou prodal prý za 800 milionů dolarů. Projekt OpenClaw vznikl v listopadu 2025 jako vedlejší experiment a do února 2026 překonal na GitHubu počtem hvězd React, Linux i Kubernetes. V únoru 2026 Steinbergera ulovila firma OpenAI a projekt přešel pod nezávislou open-source nadaci s finanční podporou od OpenAI.

OpenClaw je v podstatě démon běžící na uživatelově stroji, který propojuje jazykový model (Claude, GPT, Gemini, DeepSeek nebo lokální model) s desítkami komunikačních platforem — WhatsApp, Telegram, Slack, Discord, Signal, iMessage — a dává mu přístup k lokálním souborům, shellu, prohlížeči a dalším nástrojům. Agent dokáže autonomně spouštět příkazy, spravovat soubory, odesílat e-maily a provádět akce bez průběžného souhlasu uživatele. Systém dovedností (skills) umožňuje rozšiřování přes komunitní tržiště [ClawHub](https://github.com/topics/openclaw-skill), které dnes obsahuje přes 10 tisíc rozšíření.

Jenže to všechno fungovalo od počátku s velmi mlžnou bezpečnostní hranicí a také s celou řadou chyb. V lednu 2026 odhalil výzkumník Mav Levin zranitelnost [CVE-2026-25253](https://nvd.nist.gov/) (CVSS 8.8) — chybu v autorizaci přes WebSocket, kdy jakákoliv webová stránka mohla ukrást přístupový token a získat vzdálené spuštění kódu na počítači uživatele. Platforma Moltbook, sociální síť pro AI agenty postavená na OpenClaw, utrpěla rozsáhlý únik dat — veřejně přístupná databáze Supabase odhalila 1,5 milionu klíčů API agentů a desítky tisíc e-mailových adres. Student informatiky zjistil, že jeho OpenClaw agent si bez jeho vědomí vytvořil profil na seznamovací platformě MoltMatch a autonomně vybíral partnery. V březnu 2026 Čína zakázala státním institucím používat OpenClaw kvůli bezpečnostním obavám.

Jeden z vlastních správců projektu, vystupující pod přezdívkou Shadow, na Discordu OpenClaw napsal varování, které situaci shrnuje nejlépe: pokud nerozumíte tomu, jak funguje příkazový řádek, je tento projekt pro vás příliš nebezpečný.

Přesto jej používají tisíce lidí, často bez povědomí o tom, co všechno se může stát. Nebo - a to je horší - s vědomím tohoto jej poučtí na svůj osobní počítač, kde mají svá osobní data. Jak z toho ven?

## NemoClaw: co přesně přidává

NemoClaw není konkurent OpenClaw, jak se původně spekulovalo. Je to integrační vrstva, která do OpenClaw zabalí komponenty z [NVIDIA Agent Toolkit](https://nvidianews.nvidia.com/news/ai-agents) — konkrétně runtime OpenShell, modely Nemotron a směrovač soukromí. Instalace probíhá jedním příkazem:

```
openshell sandbox create --remote spark --from openclaw
```

Výsledkem je OpenClaw běžící uvnitř izolovaného prostředí, které řídí OpenShell. Agent nevyžaduje žádné změny kódu — OpenShell se chová jako transparentní vrstva mezi agentem a operačním systémem.

### OpenShell: jádro celého řešení

[OpenShell](https://github.com/NVIDIA/OpenShell) je open-source runtime pod licencí Apache 2.0, který stojí na třech pilířích:

**Sandbox** — izolované prostředí navržené specificky pro dlouhodobě běžící agenty. Na rozdíl od generické kontejnerové izolace počítá s tím, že agent si za běhu instaluje balíčky, učí se nové dovednosti a spouští subagenty. Politiky se aktualizují živě, každé povolení i zamítnutí se zaznamenává do auditního logu. Agent může navrhnout úpravu politiky (například požádat o přístup k novému adresáři), ale konečné schválení zůstává na uživateli.

**Politikový engine** — vynucuje omezení na úrovni souborového systému, sítě a procesů. Klíčové je, že politiky jsou definované v deklarativním YAML formátu a vynucují se mimo proces agenta (out-of-process enforcement). Agent tedy nemůže politiky obejít, ani pokud je kompromitovaný prompt injection útokem. Engine kontroluje každou akci na úrovni binárky, cílové adresy, metody i cesty. Agent smí nainstalovat ověřenou dovednost, ale nesmí spustit neprověřenou binárku.

**Směrovač soukromí** (privacy router) — rozhoduje, kam směřovat inferenci. Citlivý kontext zpracovávají lokální modely Nemotron na GPU uživatele. Do cloudových modelů (Claude, GPT) se odesílají jen dotazy, kde to politika dovoluje. Rozhodnutí dělá směrovač podle nastavené politiky, ne agent sám.

Architektonicky jde o model inspirovaný bezpečností webových prohlížečů: každá session je izolovaná, oprávnění se ověřují runtimem před provedením jakékoliv akce. Nástroje jako Claude Code nebo Cursor mají vlastní interní bezpečnostní mechanismy, ale ty žijí uvnitř procesu agenta. OpenShell přesouvá řídicí bod zcela mimo dosah agenta.

Na Linuxu OpenShell využívá pro izolaci souborového systému mechanismus Landlock (dostupný od jádra 5.13), který umožňuje neprivilegovaným procesům omezit si přístup k souborovému systému. Pro filtrování systémových volání používá seccomp-BPF a síťovou izolaci řeší přes jmenné prostory (network namespaces). Na GitHubu projektu je nicméně uvedeno, že jde o alfa software v režimu jednoho uživatele — podpora více tenantů a podnikových nasazení je ve výhledu, ne v aktuální verzi.

### Bezpečnostní partnerství

NVIDIA na GTC oznámila spolupráci s bezpečnostními firmami na kompatibilitě jejich nástrojů s OpenShell. [CrowdStrike](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-nvidia-unveil-secure-by-design-ai-blueprint-for-ai-agents/) představil Secure-by-Design AI Blueprint, který integruje ochranu platformy Falcon přímo do OpenShell — koncová ochrana lokálních agentů na DGX Spark a DGX Station, cloudová ochrana pro agenty postavené na NVIDIA AI-Q Blueprint a správa identit pro řízení přístupu agentů k datům a API. Cisco AI Defense přidá bezpečnostní kontroly pro řízení akcí agentů. Na kompatibilitě pracují také Google, Microsoft Security a TrendAI.

Je třeba říct, že většina těchto integrací je zatím v oznámení, ne v produkčním nasazení. CrowdStrike v tiskovém prohlášení sám upozorňuje, že jde o výhledové plány, které se mohou lišit od skutečného výsledku.

## Kde NemoClaw běží

NemoClaw podporuje několik platforem s různou úrovní výkonu:

|Platforma|Popis|Poznámka|
|---|---|---|
|**NVIDIA DGX Spark**|Stolní systém s GPU pro lokální AI|Primární cílová platforma, v prodeji|
|**NVIDIA DGX Station**|Výkonnější varianta pro frontierové modely|Objednávky otevřeny od 16. března 2026|
|**RTX notebooky/PC**|Jakýkoliv systém s NVIDIA RTX GPU|Závisí na VRAM pro lokální modely|
|**Cloud (Brev, AWS, Azure, GCP)**|Cloudové nasazení|Přes partnery a poskytovatele|

NVIDIA při této příležitosti pozicuje své stolní systémy DGX Spark a DGX Station jako dedikované vývojářské platformy pro tvorbu agentů. Jensen Huang v tiskovém prohlášení přirovnal OpenClaw k operačnímu systému pro osobní AI, podobně jako Mac a Windows jsou operační systémy pro osobní počítač. A to je moc hezký posun :)

## Kritický pohled: co NemoClaw skutečně řeší a co ne

NemoClaw je technicky zajímavý projekt, ale nadšení kolem něj (především na sociálních sítích) přeskakuje několik důležitých faktů.

Za prvé, OpenShell je v alfa fázi. README na GitHubu výslovně uvádí, že jde o software v režimu jednoho uživatele, s očekávanými hrubými "hranami". Tvrzení o „enterprise-ready OpenClaw jedním příkazem", které koluje na X.com, je v tuto chvíli přehnané. Cesta od alfa verze s jedním uživatelem k produkčnímu podnikovému nasazení je dlouhá a plná problémů, které se v tiskových prohlášeních neobjevují.

Za druhé, sandboxování řeší jen část bezpečnostního problému. OpenShell může agentovi zabránit v přístupu k zakázaným souborům nebo síťovým adresám, ale neřeší fundamentální riziko autonomních agentů: že agent udělá něco nežádoucího v rámci svých povolených oprávnění. Pokud agent smí odesílat e-maily a má přístup ke kontaktům, žádný sandbox nezabrání tomu, aby odeslal nevhodný e-mail správné osobě. Problém prompt injection — kdy útočník vloží škodlivé instrukce do dat, která agent zpracovává — sandbox zmírňuje, ale neodstraňuje. Agent kompromitovaný prompt injection útokem sice nemůže překročit hranice sandboxu, ale může způsobit škodu v rámci svých oprávnění.

Za třetí, ekosystémová hra NVIDIA je zřejmá. NemoClaw instaluje modely Nemotron, preferuje běh na NVIDIA GPU, primárními cílovými platformami jsou DGX Spark a DGX Station. Směrovač soukromí, který udržuje citlivá data na lokálním GPU, je zároveň argumentem pro nákup dražšího hardwaru. OpenShell je agnostický vůči modelům (funguje s Claude Code, OpenAI Codex i dalšími), ale ekosystémový tah je nepřehlédnutelný. NVIDIA nemusí vyhrát soutěž o nejlepší model — stačí jí vlastnit vrstvu pod ním.

Za čtvrté, komunitní ekosystém dovedností (skills) zůstává rizikem. Cisco při testování OpenClaw zjistilo, že komunitní skill prováděl exfiltraci dat a prompt injection bez vědomí uživatele. Tržiště dovedností postrádá dostatečné ověřování. OpenShell může omezit, co dovednost smí na úrovni systému dělat, ale kvalitu a důvěryhodnost samotného kódu dovedností neřeší.

## Širší kontext: závod o bezpečnostní vrstvu pro agenty

NemoClaw není osamocený pokus. Problém bezpečnosti autonomních agentů řeší paralelně několik projektů. Cursor nedávno zveřejnil vlastní sandboxovací řešení pro své AI agenty, využívající na macOS mechanismus Seatbelt, na Linuxu Landlock a seccomp. OpenAI Codex používá podobnou kombinaci Landlock a seccomp pro izolaci na Linuxu. Existuje i řada komunitních nástrojů — SecureClaw pro bezpečnostní audit, ClawBands jako middleware pro schvalování akcí nástrojů, APort Agent Guardrails pro blokování nebezpečných vzorců.

Rozdíl NemoClaw oproti těmto řešením je v ambici: nejde jen o sandbox pro jeden nástroj, ale o kompletní runtime vrstvu s politikovým enginem, směrovačem soukromí a auditním systémem, kolem které NVIDIA buduje partnerský ekosystém bezpečnostních firem. Zda tato ambice odpovídá realitě alfa softwaru, ukáží příští měsíce.

## Závěr

NemoClaw představuje logický a potřebný krok. Autonomní agenti typu OpenClaw mají reálný potenciál, ale bez bezpečnostní infrastruktury jsou pro seriózní použití příliš riskantní. Out-of-process vynucování politik, jak ho implementuje OpenShell, je architektonicky správný přístup — výrazně lepší než spoléhání na to, že se agent sám omezí.

Současně je třeba vidět, že jde o alfa verzi, která teprve musí prokázat spolehlivost v reálném provozu. Bezpečnostní partnerství s CrowdStrike, Cisco a dalšími jsou zatím na úrovni tiskových prohlášení. A celý stack tiše posiluje pozici NVIDIA v hodnotovém řetězci AI — od GPU přes modely až po runtime, na kterém agenti běží.

Pro vývojáře, kteří experimentují s OpenClaw, má smysl NemoClaw vyzkoušet. Pro podnikové nasazení je zatím příliš brzy. Pro nadšené solo-podnikatele s IT erudicí je do dobrý moment...

**Odkazy:**

- [NemoClaw — produktová stránka NVIDIA](https://www.nvidia.com/en-us/ai/nemoclaw/)
- [OpenShell — repozitář na GitHubu](https://github.com/NVIDIA/OpenShell)
- [Technický blog NVIDIA o OpenShell](https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell/)
- [Oznámení NVIDIA Agent Toolkit](https://nvidianews.nvidia.com/news/ai-agents)
- [CrowdStrike Secure-by-Design AI Blueprint](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-nvidia-unveil-secure-by-design-ai-blueprint-for-ai-agents/)
- [OpenClaw — Wikipedie](https://en.wikipedia.org/wiki/OpenClaw)
- [The New Stack: NemoClaw je OpenClaw se záchytnými mechanismy](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/)
